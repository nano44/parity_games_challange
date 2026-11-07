#!/usr/bin/env python3
"""L-NEW box 135 DMERGE: the merge-segment digraph D' of every maximal FL run (box132/anchor.py detection). At every state s of the run
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
R = dict(runs=0, fl=0, acyc=0, cyc=0, hmax=0, cascviol=0, segedges=0, maxl=0, selfl=0, cnmov=0)
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
            for i in range(len(os_)):
                for k in range(i + 1, len(os_)):
                    y, z = os_[i], os_[k]
                    if vs[y][0] != vs[z][0]: continue
                    py, _ = play(succ1, y); pz, _ = play(succ1, z); w = vs[y][0]
                    yw = py[:py.index(w) + 1]; zw = pz[:pz.index(w) + 1]; c = 0
                    while c < min(len(yw), len(zw)) and yw[-1 - c] == zw[-1 - c]: c += 1
                    for v in yw[:len(yw) - c] + zw[:len(zw) - c]:
                        if own[v] == 0:
                            adj[x].add(v)
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
    if cyc: R["cyc"] += 1
    else:
        H = max(h.values(), default=0); R["acyc"] += 1; R["hmax"] = max(R["hmax"], H); R["cascviol"] += (b - a) > H + 1
R["runs"] = len(runs)
print(("DMERGES " if os.environ.get("STRETCH") == "1" else "DMERGE ") + f"{os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()))
