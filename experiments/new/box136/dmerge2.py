#!/usr/bin/env python3
"""L-NEW box 136 DMERGE2 (box135/dmerge.py with z-WORLD comparisons, Lemma C-STATIC-Xi): for a pair (y, z) the comparison is evaluated
with x's strategy set to z (the only states where f_x uses it), x itself is excluded from the segments (its choice is fixed to z there),
and w is the cycle node of the z-world play (most relevant vertex on the final cycle). With DOM=1 (Lemma DOM, data form): if the most relevant vertex (above w) of the symmetric difference of the two
segments' HEADS (up to and including the first Even vertex other than x) is more relevant than every vertex (above w) on their tails at that
state, the comparison adds no edge: the heads are fixed by sbar and x's choice, the first Even vertex's choice only moves the tail
(DOMCUT counts such comparisons). Box 135 text: the merge-segment digraph D' of every maximal FL run (box132/anchor.py detection). At every state s of the run
and every Even x not a W-cycle node, for every pair of options y != z in T_x u {sigma_s(x)} whose Xi_s-plays (sigma_s at Even, sbar_s
at Odd) have the same cycle node w: edges x -> every Even vertex on the
parts of y's and z's plays up to w that precede their longest common suffix (the merge point m; Lemma MERGE), x itself included
(SELFL counts such self-edges: x on its own option's Xi-play before m). Also W-key edges x -> Even vertices on the W-play of every option
of x before its W-cycle node (the BFS key's support). Pairs with different cycle nodes add no edge (their order is decided by the cycle nodes; CYC-MONO).
Union over the run's states. Prints per game: RUNS, FL, D'-acyclic runs ACYC, cyclic CYC, the largest height HMAX over acyclic runs,
CASCVIOL (an acyclic run longer than height + 1), and SEGEDGES (total edges).
With STRETCH=1: the same on STRETCHES (maximal sub-intervals of a run with sbar and the cycle node of Xi at every vertex constant and no
move of a W-cycle node; CNMOV counts the W-cycle-node moves cut out), printed as DMERGES.
Usage: [STRETCH=1] dmerge.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box132", "anchor.py")).read().split("R = dict(runs")[0]
exec(src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.join(HERE, "..", "box132"))))
R = dict(runs=0, fl=0, acyc=0, cyc=0, hmax=0, cascviol=0, segedges=0, maxl=0, selfl=0, cnmov=0, domcut=0)
def play(succ1, v):
    seq = []; pos = {}
    while v not in pos: pos[v] = len(seq); seq.append(v); v = succ1[v]
    return seq, pos
def stretches(a, b):
    out = []; s0 = a
    W0 = wval(a); CN0 = {v for v in range(n) if W0[v][2] == 0}
    def sig(j):
        vs, sb = E.evaluate(S[j]); return (tuple(sb[o] for o in range(n) if own[o] == 1), tuple(vs[v][0] for v in range(n)))
    for j in range(a + 1, b + 1):
        cnmove = any(S[j][c] != S[j - 1][c] for c in CN0 if own[c] == 0)
        if cnmove:
            R["cnmov"] += 1
            if j - 1 > s0: out.append((s0, j - 1))
            s0 = j; continue
        if sig(j - 1) != sig(s0):
            if j - 1 > s0: out.append((s0, j - 1))
            s0 = j - 1
    if b > s0: out.append((s0, b))
    return out
RUNS = runs
if os.environ.get("STRETCH") == "1": runs = [st for a, b in RUNS for st in stretches(a, b)]
for a, b in runs:
    tau = T[a]; W = wval(a); CN = {v for v in range(n) if W[v][2] == 0}
    Tx = {x: [y for y in g.succ[x] if (W[y][2] == W[x][2] - 1 and W[y][0] == W[x][0])] for x in range(n) if own[x] == 0 and x not in CN}
    adj = {x: set() for x in range(n) if own[x] == 0}
    for s in range(a, b + 1):
        vs, sb = E.evaluate(S[s]); succ1 = [S[s][v] if own[v] == 0 else sb[v] for v in range(n)]
        for x, opts in Tx.items():
            os_ = sorted(set(opts) | {S[s][x]})
            for z in os_:
                sz = list(succ1); sz[x] = z
                def cn(v):
                    seq, pos = play(sz, v); cyc = seq[pos[sz[seq[-1]]]:]
                    return max(cyc, key=lambda u: E.rank[u]), seq
                wz, pz = cn(z)
                for y in os_:
                    if y == z: continue
                    wy, py = cn(y)
                    if wy != wz: continue
                    w = wz; yw = py[:py.index(w) + 1]; zw = pz[:pz.index(w) + 1]; c = 0
                    while c < min(len(yw), len(zw)) and yw[-1 - c] == zw[-1 - c]: c += 1
                    Yp, Zp = yw[:len(yw) - c], zw[:len(zw) - c]
                    def head(P):
                        for i, v in enumerate(P):
                            if own[v] == 0 and v != x: return P[:i + 1], P[i + 1:]
                        return P, []
                    hy, ty = head(Yp); hz, tz = head(Zp)
                    rw = E.rank[w]
                    Dh = [v for v in set(hy) ^ set(hz) if E.rank[v] > rw]
                    tails = [v for v in ty + tz if E.rank[v] > rw]
                    dom = bool(Dh) and (not tails or max(E.rank[v] for v in Dh) > max(E.rank[v] for v in tails))
                    if os.environ.get("DOM") == "1" and dom:
                        R["domcut"] += 1
                        continue
                    for v in Yp + Zp:
                        if own[v] == 0 and v != x: adj[x].add(v)
                        if v == x: R["selfl"] += 1
        sW = [S[s][v] if own[v] == 0 else tau[v] for v in range(n)]
        for x, opts in Tx.items():
            for y in set(opts) | {S[s][x]}:
                v = y
                while W[v][2] > 0:
                    if own[v] == 0 and v != x: adj[x].add(v)
                    v = sW[v]
    R["fl"] += b - a; R["maxl"] = max(R["maxl"], b - a); R["segedges"] += sum(len(e) for e in adj.values())
    # cycle check + height (iterative DFS)
    state = {}; h = {}; cyc = False
    for v0 in adj:
        if v0 in state: continue
        st = [(v0, iter(adj[v0]))]; state[v0] = 1
        while st and not cyc:
            v, it = st[-1]; nx = next(it, None)
            if nx is None:
                state[v] = 2; h[v] = 1 + max((h[w] for w in adj[v]), default=-1); st.pop()
            elif state.get(nx) == 1: cyc = True
            elif nx not in state: state[nx] = 1; st.append((nx, iter(adj[nx])))
        if cyc: break
    if cyc:
        R["cyc"] += 1
        if os.environ.get("SHOWCYC"):
            path = [v for v, _ in st]; i = path.index(nx); print("CYCLE run", a, b, path[i:] + [nx], "levels", [W[v][2] for v in path[i:]], "cnodes", [W[v][0] for v in path[i:]])
    else:
        H = max(h.values(), default=0); R["acyc"] += 1; R["hmax"] = max(R["hmax"], H); R["cascviol"] += (b - a) > H + 1
R["runs"] = len(runs)
print((("DMERGE2S" if os.environ.get("STRETCH") == "1" else "DMERGE2") + ("D " if os.environ.get("DOM") == "1" else " ")) + f"{os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()))
