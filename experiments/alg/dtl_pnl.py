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
import pg, dtl_step5 as S5, dtl_step5stats as ST
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


class PN(S5.S5):
    def best_vertices(s, V, R, p):
        """dtl_pyref.best_vertices verbatim, recording the region union of every round."""
        s.rounds = []; s.cur_p = p; s.cur_R = frozenset(R)
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
            s.rounds.append(frozenset(Z))
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
            V -= set(cand)
            if not cand: s.note_rounds(1); return 1
            if not V:
                V.clear(); V.update(prevV); s.note_rounds(-1); return -1

    def note_rounds(s, res):
        for a, b in zip(s.rounds, s.rounds[1:]):
            s.tab["MONO all pairs " + ("holds" if b <= a else "VIOLATION")] = s.tab.get("MONO all pairs " + ("holds" if b <= a else "VIOLATION"), 0) + 1
            if not b <= a:
                k = "R-MONO (p-closed part of Z^{r+1} inside Z^r) " + ("holds" if pclosed(s, s.cur_p, b, s.cur_R) <= a else "VIOLATION")
                s.tab[k] = s.tab.get(k, 0) + 1
        s.last_rounds = list(s.rounds)

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
                rounds = s.last_rounds
                s.dom(V, R, X_, p); Y0 = R0 - frozenset(R)
                s.check(p, R0, Y0, rounds, depth)

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
    sys.setrecursionlimit(100000); tab = {}; shown = [0]; kd = [0]
    for f, g in ST.games(sys.argv[1:]):
        d0 = S5.build(g); d = PN(d0.pr, d0.ow, d0.outs, ins_desc=(os.environ.get("DTL_ORDER") == "oink")); d.idx = d0.idx; d.trace = []
        d.tab = tab; d.shown = shown[0]; d.fname = f; d.last_rounds = []; d.cur_new = []; d.kd = kd[0]
        d.run(); shown[0] = d.shown; kd[0] = d.kd
    for k in sorted(tab): print(f"  {k}: {tab[k]}")
