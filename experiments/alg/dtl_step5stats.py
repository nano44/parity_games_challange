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
            if not Dw or tr["dom"] or (mixed and len(G - Dw) < 3): continue
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
            if firstK[0] is None: inc("K never broken at depth 0", f)
            # LASTD: the depth-0 piece that removes the last vertex of D (with its recursion, for T) learns inside D
            top = [i for i, pc in enumerate(pcs) if pc["depth"] == 0]
            endR = pcs[top[-1]]["R"] if pcs[top[-1]]["kind"] == "E" else frozenset()
            if endR & Dw: inc("LASTD: D meets R_end (no last piece)", f); continue
            j = max(i for i in top if pcs[i]["rem"] & Dw); nxt = next((i for i in top if i > j), len(pcs))
            learned = any(C <= Dw for pc in pcs[j:nxt] if pc["kind"] == "S" for C in pc["new"])
            inc(f"LASTD piece {pcs[j]['kind']} " + ("learns inside D" if learned else "VIOLATION"), f)
    for k in sorted(tab): print(f"  {k}: {tab[k]}")
