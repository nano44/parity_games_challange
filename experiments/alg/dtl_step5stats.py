"""L-ALG succ. 6 (produced on Opus 5.5, 2026-10-17 box 6), GAP-C Step 5: statistics of depth-0 SEGMENTS.
A segment = a depth-0 P piece (Dom(prevV, R) with Q empty, dtl.cpp 962-991) and the depth-0 pieces after it up to the next
depth-0 P piece (the first segment may start with S, Theorem A's case). Over every search of p with D := W_p(G') != {} and
no dominion (Zielonka on G'), counts:
  TRAP    : at every depth-0 P piece, R is a p-trap of G' (no p-vertex of R has an edge out of R) [PROVED; checked];
  PREM    : what a depth-0 P piece removes: D-vertices / W_{1-p}-vertices / mixed;
  ATTR    : every D-vertex removed by a depth-0 P piece lies in Attr_p^{G[R]}(D ∩ R') (R' = R minus the piece);
  SEG-ALL : every segment whose start context meets D learns a tangle inside D (any depth, any piece of the segment);
  SEG-LAST: the last segment whose start context meets D learns a tangle inside D;
  K       : K(R) = the subgame on (D ∩ R) minus the p-attractor to X = G' \\ R (X a p-won sink) has a nonempty p-winning
            region; true at R = G', false at R_end; K-FIRST: the first depth-0 piece after which K fails learns inside D;
  LASTD   : the depth-0 piece removing the last vertex of D (a T piece together with its recursion) learns inside D.
Games: the files given, and with UNIONS=k also k random disjoint unions of two of them (UM_CROSS=c cross edges, seed SEED).
RANDOM=k adds k random games (gen.random_game, n = 4..14). ALLSEARCH=1 keeps searches that find a dominion.
Only mixed searches (|W_{1-p}| >= 3) with MIXED=1. DTL_ORDER = oink | stable. Usage: dtl_step5stats.py G.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, dtl_step5 as S5, dtl_orphan as O


def attr(d, p, A, R):
    """Plain p-attractor of A inside R (edges leaving R ignored for both players: the subgame G[R])."""
    A = set(A); ch = True
    while ch:
        ch = False
        for v in R:
            if v in A: continue
            out = [w for w in d.outs[v] if w in R]
            if (d.ow[v] == p and any(w in A for w in out)) or (d.ow[v] != p and out and all(w in A for w in out)):
                A.add(v); ch = True
    return A


def hyb(d, p, S):
    """p-winning region of the game on S: edges leaving S deleted; a vertex with no successor in S loses for p (whoever
    owns it), and so does everything the opponent attracts to such vertices; the rest is solved by Zielonka."""
    S = set(S)
    if not S: return set()
    L = set(); ch = True
    while ch:
        ch = False
        for v in S - L:
            out = [w for w in d.outs[v] if w in S]
            if not out or (d.ow[v] != p and any(w in L for w in out)) or (d.ow[v] == p and all(w in L for w in out)):
                L.add(v); ch = True
    rest = S - L
    return O.winning(d, rest, p) if rest else set()


def jf(d, p, S, R):
    """Greatest B ⊆ S with: every opponent vertex of B has all its R-edges in B (none at all is allowed: forgiven), every
    p-vertex of B has an R-edge into B. Returns B if it holds a p-priority vertex, else the empty set."""
    B = set(S); ch = True
    while ch:
        ch = False
        for v in list(B):
            out = [w for w in d.outs[v] if w in R]
            ok = any(w in B for w in out) if d.ow[v] == p else all(w in B for w in out)
            if not ok: B.discard(v); ch = True
    return B if any(d.pr[v] % 2 == p for v in B) else set()


def kq(d, p, Dw, R, G):
    """K(R): X := G' \\ R is a p-won sink (as DTL's threshold step and forgiving regions treat it). Q := (D ∩ R) minus the
    p-attractor (inside D ∩ R) of the vertices with an edge into X (p-vertex: some edge; opponent: all its edges lie in X ∪
    the attractor). Returns the p-winning region of the subgame G[Q] (a vertex with no successor in Q loses for its owner)."""
    S = Dw & R; X = G - R
    A = set(); ch = True
    while ch:
        ch = False
        for v in S - A:
            out = [w for w in d.outs[v] if w in G]
            if d.ow[v] == p: ok = any(w in X or w in A for w in out)
            else: ok = all(w in X or w in A for w in out)
            if ok: A.add(v); ch = True
    Q = S - A
    # dead ends: drop p-vertices without successor in Q (they lose), then the opponent attractor to them
    L = set(); ch = True
    while ch:
        ch = False
        for v in Q - L:
            out = [w for w in d.outs[v] if w in Q]
            if (d.ow[v] == p and all(w in L for w in out)) or (d.ow[v] != p and any(w in L for w in out)):
                L.add(v); ch = True
    rest = Q - L
    return O.winning(d, rest, p) if rest else set()


def kqT(d, p, Dw, R, G, nt):
    """K^T(R): as kq, but the attractor to X also takes stored p-tangles (the first nt, not deleted) that lie in D and
    whose every vertex is in R or already attracted and every escape in G' is in X or attracted (no threshold)."""
    S = Dw & R; X = G - R
    tg = [(set(v for v, _ in d.tv[i]), d.tout[i]) for i in range(nt) if d.tpr[i] != -1 and d.tpr[i] % 2 == p]
    tg = [(T, E) for T, E in tg if T <= Dw]
    A = set(); ch = True
    while ch:
        ch = False
        for v in S - A:
            out = [w for w in d.outs[v] if w in G]
            if d.ow[v] == p: ok = any(w in X or w in A for w in out)
            else: ok = all(w in X or w in A for w in out)
            if ok: A.add(v); ch = True
        for T, E in tg:
            if T <= (S | A) and not T <= A and all(e in X or e in A or e not in G for e in E):
                A |= T; ch = True
    Q = S - A
    L = set(); ch = True
    while ch:
        ch = False
        for v in Q - L:
            out = [w for w in d.outs[v] if w in Q]
            if (d.ow[v] == p and all(w in L for w in out)) or (d.ow[v] != p and any(w in L for w in out)):
                L.add(v); ch = True
    rest = Q - L
    return O.winning(d, rest, p) if rest else set()


def lowdom(d, p, DR, R):
    """W* = a p-dominion of G[R] inside DR with the least maximum priority (as dtl_pnl.lowdom): (c, W) or (None, set())."""
    for c in sorted({d.pr[v] for v in DR if d.pr[v] % 2 == p}):
        W = closed_dom(d, p, {v for v in DR if d.pr[v] <= c}, R)
        if W: return c, W
    return None, set()


def closed_dom(d, p, S, R):
    """A nonempty p-dominion of the subgame G[R] inside S, if any: the greatest B ⊆ S with every opponent vertex having all
    its R-edges in B (at least one) and every p-vertex an R-edge into B, then W_p(G[B]) (B is a trap for the opponent)."""
    B = set(S); ch = True
    while ch:
        ch = False
        for v in list(B):
            out = [w for w in d.outs[v] if w in R]
            ok = any(w in B for w in out) if d.ow[v] == p else (bool(out) and all(w in B for w in out))
            if not ok: B.discard(v); ch = True
    return O.winning(d, B, p) if B else set()


def kthr_core(d, p, Dw, R, G, c):
    """The core W_p(F_c) of KT at level c (see kthr)."""
    S0 = Dw & R; X = G - R; S = {v for v in S0 if d.pr[v] <= c}
    A = set(); ch = True
    while ch:
        ch = False
        for v in S - A:
            outs = [w for w in d.outs[v] if w in G]
            ok = any(w in X or w in A for w in outs) if d.ow[v] == p else all(w in X or w in A for w in outs)
            if ok: A.add(v); ch = True
    Q = S - A; L = set(); ch = True
    while ch:
        ch = False
        for v in Q - L:
            outs = [w for w in d.outs[v] if w in Q]
            if not outs or (d.ow[v] == p and all(w in L for w in outs)) or (d.ow[v] != p and any(w in L for w in outs)):
                L.add(v); ch = True
    rest = Q - L
    return O.winning(d, rest, p) if rest else set()


def kthr(d, p, Dw, R, G):
    """KT(R) (GAP-C §18g): for some c of p's parity, with S_c = D ∩ R ∩ {priority ≤ c} and A_c the plain p-attractor of
    X = G' \\ R inside S_c (an opponent vertex enters only if ALL its edges lie in X ∪ A_c), the game on Q_c = S_c \\ A_c in
    which the opponent's edges leaving Q_c are deleted and a vertex without successor loses for p has a nonempty p-winning
    region. Returns the list of c for which it holds."""
    S0 = Dw & R; X = G - R; out_c = []
    for c in sorted({d.pr[v] for v in S0 if d.pr[v] % 2 == p}):
        S = {v for v in S0 if d.pr[v] <= c}
        A = set(); ch = True
        while ch:
            ch = False
            for v in S - A:
                outs = [w for w in d.outs[v] if w in G]
                ok = any(w in X or w in A for w in outs) if d.ow[v] == p else all(w in X or w in A for w in outs)
                if ok: A.add(v); ch = True
        Q = S - A
        L = set(); ch = True                          # dead ends and what the opponent forces into them: lost for p
        while ch:
            ch = False
            for v in Q - L:
                outs = [w for w in d.outs[v] if w in Q]
                if not outs or (d.ow[v] == p and all(w in L for w in outs)) or (d.ow[v] != p and any(w in L for w in outs)):
                    L.add(v); ch = True
        rest = Q - L
        if rest and O.winning(d, rest, p): out_c.append(c)
    return out_c


def segments(pcs):
    top = [pc for pc in pcs if pc["depth"] == 0]; segs, cur = [], []
    for pc in pcs:
        if pc["depth"] == 0 and pc["kind"] == "P" and cur: segs.append(cur); cur = []
        cur.append(pc)
    if cur: segs.append(cur)
    return segs


def games(files):
    gs = [pg.read(f) for f in files]
    for f, g in zip(files, gs): yield f, g
    import gen
    for i in range(int(os.environ.get("RANDOM", "0"))):                 # random games, n = 4..14, out-degree 1..3
        n = 4 + i % 11; yield f"random{i}", gen.random_game(n, n, 1, 3, int(os.environ.get("SEED", "1")) * 100000 + i)
    k = int(os.environ.get("UNIONS", "0")); rnd = random.Random(int(os.environ.get("SEED", "1"))); nmax = int(os.environ.get("NMAX", "32"))
    small = [g for g in gs if g.n <= nmax]
    for i in range(k):
        a, b = rnd.sample(small, 2); off = a.n
        succ = [list(s) for s in a.succ] + [[w + off for w in s] for s in b.succ]
        for _ in range(int(os.environ.get("UM_CROSS", "0"))):
            u = rnd.randrange(a.n + b.n); w = rnd.randrange(off, a.n + b.n) if u < off else rnd.randrange(0, off)
            succ[u] = sorted(set(succ[u]) | {w})
        yield f"union{i}", pg.Game(list(a.prio) + list(b.prio), list(a.owner) + list(b.owner), succ)


if __name__ == "__main__":
    sys.setrecursionlimit(100000); tab = {}; mixed = os.environ.get("MIXED") == "1"; shown = {}
    def inc(k, f=None):
        tab[k] = tab.get(k, 0) + 1
        if f and "VIOL" in k and shown.get(k, 0) < 3: shown[k] = shown.get(k, 0) + 1; print(k, f, flush=True)
    for f, g in games(sys.argv[1:]):
        d = S5.build(g); d.run()
        for tr in d.trace:
            Dw, G, p = tr["Wp"], tr["G"], tr["p"]
            if not Dw or (tr["dom"] and os.environ.get("ALLSEARCH") != "1") or (mixed and len(G - Dw) < 3): continue
            inc("searches")
            pcs = tr["pieces"]
            for i, pc in enumerate(pcs):
                if pc["depth"] != 0 or pc["kind"] != "P": continue
                R = set(pc["R"]); rem = pc["rem"]
                inc("TRAP holds" if all(not (d.ow[v] == p and any(w not in R for w in d.outs[v] if w in G)) for v in R) else "TRAP VIOLATION", f)
                a, b = len(rem & Dw), len(rem - Dw)
                inc("PREM " + ("D only" if b == 0 else "W_1-p only" if a == 0 else "mixed"))
                if a:
                    Rn = R - rem
                    inc("ATTR holds" if rem & Dw <= attr(d, p, Dw & Rn, R) else "ATTR VIOLATION", f)
                    if not (Dw & Rn): inc("P piece removes the last of D", f)
            segs = segments(pcs); meet = []
            for sg in segs:
                if not (sg[0]["R"] & Dw): continue
                learned = any(C <= Dw for pc in sg if pc["kind"] == "S" for C in pc["new"])
                meet.append(learned); inc("SEG learned inside D" if learned else "SEG barren (start meets D)")
            if meet:
                inc("SEG-ALL holds" if all(meet) else "SEG-ALL VIOLATION", f)
                inc("SEG-LAST holds" if meet[-1] else "SEG-LAST VIOLATION", f)
            inc(f"segments meeting D: {len(meet)}")
            # HYB: hyb(R) = p-winning region of the game on D ∩ R (edges leaving D ∩ R deleted, a vertex left without
            # successors LOSES FOR p whoever owns it). A depth-0 piece BREAKS hyb if hyb(R_j) != {} and hyb(R_{j+1}) = {}.
            top = [i for i, pc in enumerate(pcs) if pc["depth"] == 0]; firstK = [None]
            for a_, i in enumerate(top):
                pc = pcs[i]
                if pc["kind"] == "E": continue
                h0 = hyb(d, p, Dw & pc["R"]); h1 = hyb(d, p, Dw & (pc["R"] - pc["rem"]))
                if h0 and not h1:
                    nxt = top[a_ + 1] if a_ + 1 < len(top) else len(pcs)
                    learned = any(C <= Dw for q in pcs[i:nxt] if q["kind"] == "S" for C in q["new"])
                    inc(f"HYB broken by {pc['kind']} " + ("which learns inside D" if learned else "VIOLATION (barren)"), f)
                if h0 and h1: inc(f"HYB kept by {pc['kind']}")
                R0 = set(pc["R"]); R1 = R0 - pc["rem"]
                j0 = jf(d, p, Dw & R0, R0); j1 = jf(d, p, Dw & R1, R1)
                if j0 and not j1:
                    nxt = top[a_ + 1] if a_ + 1 < len(top) else len(pcs)
                    learned = any(C <= Dw for q in pcs[i:nxt] if q["kind"] == "S" for C in q["new"])
                    inc(f"JD broken by {pc['kind']} " + ("which learns inside D" if learned else "VIOLATION (barren)"), f)
                if not j0: inc(f"JD already false before {pc['kind']}", f if a_ == 0 else None)
                k0 = kq(d, p, Dw, R0, G); k1 = kq(d, p, Dw, R1, G)
                if k0 and not k1:
                    nxt = top[a_ + 1] if a_ + 1 < len(top) else len(pcs)
                    learned = any(C <= Dw for q in pcs[i:nxt] if q["kind"] == "S" for C in q["new"])
                    inc(f"K broken by {pc['kind']} " + ("which learns inside D" if learned else "(barren)"))
                    if firstK[0] is None:
                        before = any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"])
                        firstK[0] = 1; inc(f"K FIRST break by {pc['kind']} " + ("learns inside D" if learned else "barren, learned inside D before it" if before else "VIOLATION (barren, nothing learned inside D before)"), f)
                if not k0: inc(f"K already false before {pc['kind']}", f if a_ == 0 else None)
                if k0 and k1: inc(f"K kept by {pc['kind']}")
                nt1 = pcs[top[a_ + 1]]["nt"] if a_ + 1 < len(top) else len(d.tv)
                t0 = kqT(d, p, Dw, R0, G, pc["nt"]); t1 = kqT(d, p, Dw, R1, G, nt1)
                if t0 and not t1:
                    nxt = top[a_ + 1] if a_ + 1 < len(top) else len(pcs)
                    learned = any(C <= Dw for q in pcs[i:nxt] if q["kind"] == "S" for C in q["new"])
                    before = any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"])
                    inc(f"KT broken by {pc['kind']} " + ("which learns inside D" if learned else "barren, D-learning before" if before else "VIOLATION (barren, nothing learned inside D before)"), f)
                if t0 and t1: inc(f"KT kept by {pc['kind']}")
                h0 = kthr(d, p, Dw, R0, G); h1 = kthr(d, p, Dw, R1, G)
                if h0 and not h1:
                    nxt = top[a_ + 1] if a_ + 1 < len(top) else len(pcs)
                    learned = any(C <= Dw for q in pcs[i:nxt] if q["kind"] == "S" for C in q["new"])
                    before = any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"])
                    inc(f"KTHR broken by {pc['kind']} " + ("which learns inside D" if learned else "barren, D-learning before" if before else "VIOLATION (barren, nothing learned inside D before)"), f)
                if h0 and h1: inc(f"KTHR kept by {pc['kind']}")
                if not h0 and a_ == 0: inc("KTHR false at G' (start)", f)
                if pc["kind"] == "S" and h0 and not h1 and not any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"]):
                    c = h0[0]; U = kthr_core(d, p, Dw, R0, G, c)
                    ins = [(tp, C) for tp, C in pc["tops"] if C <= U]
                    tag = "S-STEP (S piece breaks KT, nothing learned before): " + ("learns inside the least-level core U" if ins else "learns inside D, not inside U" if any(C <= Dw for C in pc["new"]) else "VIOLATION barren")
                    if ins: tag += ", its top " + ("in U" if all(tp in U for tp, C in ins) else "not always in U")
                    tag += ", V* " + ("meets U" if pc["V"] & U else "avoids U")
                    inc(tag, f if not ins else None)
                    if pc.get("passes"):
                        low = pc["passes"][0][-1]
                        ok = any(tp == low for tp, C in pc["tops"]) or pc.get("domf")
                        inc("S-LOW (first KT-breaking S piece, lowest top of the first pass) " + ("learns" if ok else "VIOLATION: does not learn"), f if not ok else None)
                    cW, Wst = lowdom(d, p, Dw & R0, R0)
                    if not Wst: inc("S-W*: no p-dominion of G[R] inside D at this S piece")
                    else:
                        lw = any(C <= Wst for C in pc["new"])
                        inc("S-W*: W* exists; learned tangle " + ("inside W*" if lw else "NOT inside W*") + ", W* " + ("meets" if Wst & pc["rem"] else "avoids") + " the removed set, V* " + ("meets" if pc["V"] & Wst else "avoids") + " W*")
                    cores = {cc: kthr_core(d, p, Dw, R0, G, cc) for cc in h0}
                    anyc = [cc for cc, Uc in cores.items() if any(C <= Uc for C in pc["new"])]
                    tag2 = "S-LOC: learned tangle inside the core of " + ("the least level" if anyc and anyc[0] == h0[0] else "a higher level only" if anyc else "NO level (VIOLATION)")
                    if anyc:
                        Uc = cores[anyc[0]]; tag2 += ", that core " + ("meets V*" if pc["V"] & Uc else "avoids V*")
                        tag2 += ", KT after at that level " + ("fails" if anyc[0] not in h1 else "holds")
                    inc(tag2, f if not anyc else None)
                if pc["kind"] == "S" and h0 and not any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"]):
                    for cc in h0:
                        if cc in h1: continue
                        Uc = kthr_core(d, p, Dw, R0, G, cc)
                        if not (pc["V"] & Uc): inc("S-LEVEL: core at level c killed, V* avoids it"); continue
                        ok = any(C <= Uc for C in pc["new"])
                        inc("S-LEVEL: core at level c killed and meets V*: " + ("learns inside it" if ok else "VIOLATION (no tangle inside that core)"), f)
                if pc["kind"] == "T" and h0 and not any(C <= Dw for q in pcs[:i] if q["kind"] == "S" for C in q["new"]):
                    c = h0[0]; U = kthr_core(d, p, Dw, R0, G, c); t = pc["t"]
                    nxt = top[a_ + 1] if a_ + 1 < len(top) else len(pcs)
                    newin = [C for q in pcs[i:nxt] if q["kind"] == "S" for C in q["new"] if C <= Dw]
                    tag = "T-STEP (nothing learned before): least KT level c " + ("< t" if c < t else "= t" if c == t else "> t")
                    tag += ", core " + ("meets Z_T" if U & pc["rem"] else "avoids Z_T")
                    if U & pc["rem"]: tag += ", core ∩ rest " + ("≠ ∅" if U & pc["rest"] else "= ∅")
                    tag += ", KT after " + ("holds" if h1 else "FAILS") + (", recursion learns " + ("inside core" if any(C <= U for C in newin) else "inside D only") if newin else ", recursion barren")
                    inc(tag, f if not h1 else None)
                    if not h1:
                        # CORE-PASS: the recursion context Z' (X empty there) has a KT core inside D: KT_1(Z')
                        k1 = kthr(d, p, Dw, set(pc["rest"]), set(pc["rest"]))
                        inc("T-STEP CORE-PASS (KT fails after T): " + ("recursion context has a KT core" if k1 else "VIOLATION: recursion context has no KT core"), f)
                        Zr = set(pc["rest"]); Wc = closed_dom(d, p, Dw & Zr, Zr)
                        inc("T-STEP CORE-PASS-closed: " + ("Z' holds a p-dominion of G[Z'] inside D" if Wc else "VIOLATION: no p-dominion of G[Z'] inside D"), f)
            if firstK[0] is None: inc("K never broken at depth 0", f)
            # LASTD: the depth-0 piece that removes the last vertex of D (with its recursion, for T) learns inside D
            top = [i for i, pc in enumerate(pcs) if pc["depth"] == 0]
            endR = pcs[top[-1]]["R"] if pcs[top[-1]]["kind"] == "E" else frozenset()
            if endR & Dw: inc("LASTD: D meets R_end (no last piece)", f); continue
            j = max(i for i in top if pcs[i]["rem"] & Dw); nxt = next((i for i in top if i > j), len(pcs))
            learned = any(C <= Dw for pc in pcs[j:nxt] if pc["kind"] == "S" for C in pc["new"])
            inc(f"LASTD piece {pcs[j]['kind']} " + ("learns inside D" if learned else "VIOLATION"), f)
    for k in sorted(tab): print(f"  {k}: {tab[k]}")
