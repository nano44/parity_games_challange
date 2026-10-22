"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C Step 5 candidate (PNL*): a P piece (best_vertices returned -1
and no vertex of R attracts to X, so Dom(prevV, R) is removed; dtl.cpp 962-991) never contains a nonempty set B ⊆ R that
holds a p-priority vertex, in which every opponent vertex has all its R-edges in B (and at least one) and every p-vertex
has an edge into B ("p-closed in G[R]"). Checked through the greatest such B inside the removed set Y_0.
Also checks the two steps of the proof route:
  (YZ)   Y_0 equals the union Z_f of the final round's regions of the -1 call (Dom vs regions; they can differ only by
         stored tangles that straddle X or an earlier region);
  (R-MONO) when (MONO) fails, the greatest p-closed subset of Z^{r+1} still lies in Z^r;
  (MONO) along the rounds of one best_vertices call, the region union never grows: Z^{r+1} ⊆ Z^r (regions of the
         surviving tops, same R and tangles); counted over every round pair of every call, and separately the pairs
         that the PNL* proof uses (calls returning -1 at a P piece).
DTL_ORDER = oink | stable. Usage: dtl_pnl.py G.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_step5stats as ST, dtl_orphan as O
D = S5.D


def pclosed(s, p, Y, R):
    """Greatest B ⊆ Y with: every opponent vertex of B has all its R-edges in B (and at least one), every p-vertex of B
    has an R-edge into B."""
    B = set(Y); ch = True
    while ch:
        ch = False
        for v in list(B):
            out = [w for w in s.outs[v] if w in R]
            ok = (any(w in B for w in out)) if s.ow[v] == p else (bool(out) and all(w in B for w in out))
            if not ok: B.discard(v); ch = True
    return B


def ST2_attr(s, p, Dw, R, G):
    """A_D(R) of GAP-C §18b (X = G' minus R a p-won sink), plain attractor inside D ∩ R."""
    S = Dw & R; X = G - R; A = set(); ch = True
    while ch:
        ch = False
        for v in S - A:
            out = [w for w in s.outs[v] if w in G]
            ok = any(w in X or w in A for w in out) if s.ow[v] == p else all(w in X or w in A for w in out)
            if ok: A.add(v); ch = True
    return A


class PN(S5.S5):
    def best_vertices(s, V, R, p):
        """dtl_pyref.best_vertices verbatim, recording the region union of every round."""
        s.rounds = []; s.rv = []; s.cur_p = p; s.cur_R = frozenset(R)
        V.clear(); V.update(v for v in R if s.pr[v] % 2 == p)
        if not V: return 0
        while True:
            prevV = set(V)
            Z = set(); CurR = set(R)
            for top in range(s.n - 1, -1, -1):
                if top not in V or top in Z: continue
                CurZ = {top}; s.Q = [top]
                s.tattr(p, CurZ, CurR, CurR, s.pr[top], CurR)
                Z |= CurZ
            s.rounds.append(frozenset(Z)); s.rv.append(frozenset(V))
            C = pclosed(s, p, Z, R); pv = {v for v in C if s.pr[v] % 2 == p}
            k = "KEEP (p-priority vertices of the greatest p-closed subset of Z^r are in V_r) " + ("holds" if pv <= V else "VIOLATION")
            s.tab[k] = s.tab.get(k, 0) + 1
            if not pv <= V and os.environ.get("KEEPDUMP") and s.kd < 2:
                s.kd += 1; L = lambda S: sorted(s.idx[v] for v in S)
                print("KEEP VIOLATION", s.fname, "p", p, "|R|", len(R), "round", len(s.rounds), "V_r", L(V), "C_r", L(C), "pruned p-prio in C_r", L(pv - V))
                for i, Zi in enumerate(s.rounds): print("   Z^%d" % (i + 1), L(Zi))
                print("   R", [(s.idx[v], s.pr[v], s.ow[v], [s.idx[w] for w in s.outs[v] if w in R]) for v in sorted(R)])
            cand = [v for v in sorted(V, reverse=True) if not s.attracts(p, v, Z, R)]
            if not cand: s.note_rounds(-0); return 1
            for t in [0] + [q for q in s.prios if q > 0 and q <= s.maxpr]:
                s.Q = sorted(Z)
                s.tattr(p, Z, R, R, t, None)
                keep = []
                for i, u in enumerate(cand):
                    if s.pr[u] <= t: keep += cand[i:]; break
                    if not s.attracts(p, u, Z, R): keep.append(u)
                cand = keep
            s.amax = frozenset(Z)
            V -= set(cand)
            if not cand: s.note_rounds(1); return 1
            if not V:
                V.clear(); V.update(prevV); s.note_rounds(-1); return -1

    def note_rounds(s, res):
        if res == -1 and len(s.rounds) > 1 and os.environ.get("MONODUMP") and not all(b <= a for a, b in zip(s.rounds, s.rounds[1:])) and s.kd < int(os.environ.get("MONODUMP")):
            s.kd += 1; L = lambda S: sorted(s.idx[v] for v in S)
            print("MONO-1", s.fname, "p", s.cur_p, "|R|", len(s.cur_R), "rounds", len(s.rounds), flush=True)
            for i, (Z, Vi) in enumerate(zip(s.rounds, s.rv)):
                print("   r%d V=%s new-vs-prev=%s gone-vs-prev=%s" % (i + 1, L(Vi), L(Z - s.rounds[i - 1]) if i else "-", L(s.rounds[i - 1] - Z) if i else "-"), flush=True)
            print("   final union", L(s.rounds[-1]), flush=True)
        if res == -1 and s.rounds:
            fm = all(s.rounds[-1] <= z for z in s.rounds)
            k = "FM (-1 calls: Z_f ⊆ Z^r for every round r) " + ("holds" if fm else "FAILS")
            s.tab[k] = s.tab.get(k, 0) + 1
            if not fm and os.environ.get("FMDUMP") and s.shown < 4:
                s.shown += 1; print("FM FAILS", s.fname, "rounds", len(s.rounds), [sorted(s.idx[v] for v in s.rounds[-1] - z) for z in s.rounds], flush=True)
        for a, b in zip(s.rounds, s.rounds[1:]):
            s.tab["MONO all pairs " + ("holds" if b <= a else "VIOLATION")] = s.tab.get("MONO all pairs " + ("holds" if b <= a else "VIOLATION"), 0) + 1
            if not b <= a:
                k = "R-MONO (p-closed part of Z^{r+1} inside Z^r) " + ("holds" if pclosed(s, s.cur_p, b, s.cur_R) <= a else "VIOLATION")
                s.tab[k] = s.tab.get(k, 0) + 1
        s.last_rounds = list(s.rounds); s.last_rv = list(s.rv)

    def search_rec(s, R, p, depth):
        X_ = set()
        while True:
            V = set(); R0 = frozenset(R)
            res = s.best_vertices(V, R, p)
            if res == 0: return
            if res == 1:
                while s.sptl(V, set(R), p): pass
                s.dom(V, R, X_, p); continue
            t = 0; Z = set(); s.Q = []
            for v in range(s.n):
                if v not in R: continue
                if s.pr[v] > t:
                    if s.Q: break
                    t = s.pr[v]
                if s.attracts(p, v, X_, R): Z.add(v); s.str[v] = -1; s.Q.append(v)
            if s.Q:
                s.tattr(p, Z, R, R, t, R)
                for u in range(s.n - 1, -1, -1):
                    if s.pr[u] < t: break
                    if u in Z and s.pr[u] == t: X_.add(u); s.Q.append(u)
                while s.Q:
                    u = s.Q.pop(); Z.discard(u); s.attractVertices(1 - p, u, Z, X_, Z, t)
                X_ |= Z
                s.search_rec(Z, p, depth + 1)
            else:
                rounds = s.last_rounds; amax = s.amax; rv = s.last_rv
                if s.Wp & R:
                    k = "P-A (D ∩ R not inside the final rescue attractor A_max) " + ("holds" if not (s.Wp & R) <= amax else "FAILS")
                    s.tab[k + (" depth 0" if depth == 0 else " depth >= 1")] = s.tab.get(k + (" depth 0" if depth == 0 else " depth >= 1"), 0) + 1
                    if depth == 0 and (s.Wp & R) <= amax and os.environ.get("PADUMP") and s.kd < 3:
                        s.kd += 1; L = lambda S: sorted(s.idx[v] for v in S)
                        print("P-A FAILS", s.fname, "p", p, "R", L(R), "D∩R", L(s.Wp & R), "prevV", L(V), "Z_f", L(rounds[-1]), "A_max", L(amax), "#rounds", len(rounds))
                if depth == 0 and s.Wp & R:
                    s.case1(p, frozenset(R), rounds, rv); s.pkt(p, frozenset(R), rounds[-1])
                    mono = all(b <= a for a, b in zip(rounds, rounds[1:]))
                    s.tab["P pieces (depth 0, D ∩ R != {}) whose -1 call " + ("is MONO" if mono else "has a MONO failure (deficit round; proof of 18h does not apply, data only)")] = s.tab.get("P pieces (depth 0, D ∩ R != {}) whose -1 call " + ("is MONO" if mono else "has a MONO failure (deficit round; proof of 18h does not apply, data only)"), 0) + 1
                s.dom(V, R, X_, p); Y0 = R0 - frozenset(R)
                s.check(p, R0, Y0, rounds, depth)

    def thr(s, p, Z, R, t):
        """Threshold-t tangle attractor of Z within R (best_vertices 722-731), without side effects on str."""
        sv = list(s.str); Z = set(Z); s.Q = sorted(Z); s.tattr(p, Z, R, R, t, None); s.str = sv; return Z

    def lowdom(s, p, DR, R):
        """W1 = a p-dominion of H = G[R] inside D ∩ R with the least maximum c1 (GAP-C §18h): for c of p's parity,
        increasing, the greatest S ⊆ D ∩ R ∩ {priority ≤ c} closed in H (opponent R-edges in S, every p-vertex an R-edge
        into S), then W_p(G[S]); the first nonempty one."""
        for c in sorted({s.pr[v] for v in DR if s.pr[v] % 2 == p}):
            S = {v for v in DR if s.pr[v] <= c}; ch = True
            while ch:
                ch = False
                for v in list(S):
                    out = [w for w in s.outs[v] if w in R]
                    ok = any(w in S for w in out) if s.ow[v] == p else (bool(out) and all(w in S for w in out))
                    if not ok: S.discard(v); ch = True
            if S:
                W = O.winning(s, S, p)
                if W: return c, W
        return None, set()

    def pkt(s, p, R, Zf):
        """Lemma P-KT (§18h): W1 ⊄ Z_f ∪ A_{c1}(R'), A_{c1}(R') the plain p-attractor of X ∪ Z_f inside D ∩ R' ∩ {≤ c1}."""
        def inc(k): s.tab[k] = s.tab.get(k, 0) + 1
        DR = s.Wp & R; c1, W1 = s.lowdom(p, DR, R)
        if c1 is None: inc("P-KT: no p-dominion of H inside D ∩ R (impossible)"); return
        if s.pr[max(W1, key=lambda v: s.pr[v])] != c1: inc("P-KT: max of W1 != c1 (unexpected)")
        G = set(s.G0); Rn = R - Zf; X = G - Rn; Sc = {v for v in DR & Rn if s.pr[v] <= c1}
        A = set(); ch = True
        while ch:
            ch = False
            for v in Sc - A:
                outs = [w for w in s.outs[v] if w in G]
                ok = any(w in X or w in A for w in outs) if s.ow[v] == p else all(w in X or w in A for w in outs)
                if ok: A.add(v); ch = True
        # the deficit vertices Delta_r = Z_f \\ Z^r at the rounds r(x) of D-vertices x of priority c1 (Lead 06:48Z)
        for x in DR:
            if s.pr[x] != c1: continue
            r = max(i for i, Vi in enumerate(s.last_rv) if x in Vi)
            Dl = Zf - s.last_rounds[r]
            if not Dl: inc("WM_c1 round: Z_f ⊆ Z^r (no deficit vertex)"); continue
            mx = max(s.pr[v] for v in Dl); inA = Dl <= s.thr(p, s.last_rounds[r], R, c1 - 1)
            inc("WM_c1 round: deficit vertices, max priority " + ("< c1" if mx < c1 else ">= c1") + (", all in A^r_{c1-1}" if inA else ", NOT all in A^r_{c1-1}"))
            if s.shown < 8 and os.environ.get("DLDUMP"):
                s.shown += 1; L = lambda S: sorted((s.idx[v], s.pr[v]) for v in S)
                print("DELTA", s.fname, "p", p, "c1", c1, "round", r + 1, "of", len(s.last_rv), "Delta (id, pr)", L(Dl), "in A", inA, flush=True)
        U = W1 - Zf - A
        inc("P-KT " + ("holds (W1 survives)" if U else "VIOLATION (W1 inside Z_f ∪ A_c1)"))
        if not U and s.shown < 6: s.shown += 1; print("P-KT VIOLATION", s.fname, "p", p, "c1", c1, flush=True)

    def case1(s, p, R, rounds, rv):
        """Case split of the (P-K) proof (GAP-C §18f): M = max priority of D ∩ R; Case 1 = M of p's parity. (WM): for every
        w ∈ T_M (D-vertices of priority M), Z_f ⊆ A^{r(w)}_{M-1}, r(w) the round in which w left V."""
        def inc(k): s.tab[k] = s.tab.get(k, 0) + 1
        DR = s.Wp & R; M = max(s.pr[v] for v in DR)
        okg = True                                       # global (WM): every p-priority x of R, Z_f ⊆ A^{r(x)}_{pr(x)-1}
        cache = {}
        for x in R:
            if s.pr[x] % 2 != p: continue
            r = max(i for i, Vi in enumerate(rv) if x in Vi)
            key = (r, s.pr[x] - 1)
            if key not in cache: cache[key] = s.thr(p, rounds[r], R, s.pr[x] - 1)
            if not rounds[-1] <= cache[key]: okg = False; break
        inc("WM-global " + ("holds" if okg else "FAILS"))
        if M % 2 != p:
            inc("CASE 2 (max priority of D ∩ R has the opponent's parity)")
            import dtl_step5stats as ST2
            Rn = R - rounds[-1]; G = set(s.G0)
            Qn = set(DR & Rn) - ST2_attr(s, p, s.Wp, Rn, G)
            OM = {v for v in DR if s.pr[v] == M}
            inc("CASE 2: O_M meets Z_f" if OM & rounds[-1] else "CASE 2: O_M avoids Z_f")
            s.margins.append((len(Qn), len(DR), len(R), s.fname))
            if os.environ.get("QDUMP") and len(Qn) <= 1:
                L = lambda S: sorted(s.idx[v] for v in S)
                print("QDUMP", s.fname, "p", p, "|R|", len(R), "Q(R')", [(s.idx[v], s.pr[v], s.ow[v], [s.idx[w] for w in s.outs[v] if w in R]) for v in Qn], "M", M, "O_M", L(OM), "Z_f", L(rounds[-1]), "V_f", L(rv[-1]), "#rounds", len(rv))
            inc("CASE 2: O_M meets Q(R')" if OM & Qn else "CASE 2: O_M avoids Q(R')")
            pq = {v for v in Qn if s.pr[v] % 2 == p}
            inc("CASE 2: max priority in Q(R') " + ("p-parity" if Qn and max(s.pr[v] for v in Qn) % 2 == p else "opponent parity" if Qn else "Q empty"))
            if os.environ.get("C2DUMP") and len(R) <= int(os.environ.get("C2DUMP")) and s.kd < 4:
                s.kd += 1; L = lambda S: sorted(s.idx[v] for v in S)
                print("CASE2", s.fname, "p", p, "|R|", len(R), "D∩R", L(DR), "Z_f", L(rounds[-1]), "Q(R')", L(Qn), "O_M", L(OM), "V_f", L(rv[-1]))
                print("   ", [(s.idx[v], s.pr[v], s.ow[v], [s.idx[w] for w in s.outs[v] if w in R]) for v in sorted(R)])
            return
        TM = [v for v in DR if s.pr[v] == M]; Zf = rounds[-1]; ok = True; allf = True
        for w in TM:
            r = max(i for i, Vi in enumerate(rv) if w in Vi)
            if r != len(rv) - 1: allf = False
            if not Zf <= s.thr(p, rounds[r], R, M - 1): ok = False
        inc("CASE 1 " + ("T_M ⊆ V_f (WM trivial)" if allf else "T_M pruned earlier") + (", WM holds" if ok else ", WM FAILS"))

    def check(s, p, R0, Y0, rounds, depth):
        tag = "depth 0" if depth == 0 else "depth >= 1"
        def inc(k): s.tab[k] = s.tab.get(k, 0) + 1
        inc(f"P pieces ({tag})")
        inc(f"YZ {tag} " + ("Y_0 = Z_f" if Y0 == rounds[-1] else "Y_0 > Z_f" if Y0 > rounds[-1] else "Y_0 < Z_f" if Y0 < rounds[-1] else "Y_0, Z_f incomparable"))
        for a, b in zip(rounds, rounds[1:]): inc(f"MONO at P pieces {tag} " + ("holds" if b <= a else "VIOLATION"))
        B = set(Y0); ch = True                    # greatest p-closed set inside Y_0 (G[R0] edges)
        while ch:
            ch = False
            for v in list(B):
                out = [w for w in s.outs[v] if w in R0]
                ok = (any(w in B for w in out)) if s.ow[v] == p else (bool(out) and all(w in B for w in out))
                if not ok: B.discard(v); ch = True
        bad = any(s.pr[v] % 2 == p for v in B)
        inc(f"PNL* {tag} greatest p-closed subset of Y_0 " + ("empty" if not B else "nonempty, no p-priority vertex" if not bad else "has a p-priority vertex"))
        inc(f"PNL* {tag} " + ("VIOLATION" if bad else "holds"))
        if bad and s.shown < 3: s.shown += 1; print(f"PNL* VIOLATION {tag}", s.fname, "p", p, "|R|", len(R0), "B", sorted(s.idx[v] for v in B), flush=True)
        if s.Wp & R0:
            inc(f"PNL(D) {tag} " + ("VIOLATION: Y_0 ⊇ D ∩ R" if s.Wp & R0 <= Y0 else "holds"))


if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}; shown = [0]; kd = [0]; margins = []
    for f, g in ST.games(sys.argv[1:]):
        d0 = S5.build(g); d = PN(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.trace = []
        d.tab = tab; d.shown = shown[0]; d.fname = f; d.last_rounds = []; d.cur_new = []; d.kd = kd[0]; d.margins = margins
        d.run(); shown[0] = d.shown; kd[0] = d.kd
    for k in sorted(tab): print(f"  {k}: {tab[k]}")
    if margins: print("CASE 2 smallest |Q(R')| (|Q|, |D ∩ R|, |R|, file):", sorted(margins)[:6])
