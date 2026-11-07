#!/usr/bin/env python3
"""L-NEW box 138 DMERGE3: Theorem CASC-M''' check. S-STRETCHES = maximal sub-intervals of an FL run (box132/anchor.py detection) with the
cycle node of Xi constant at every vertex and no move of a W-cycle node; sbar MAY change inside (unlike box 135's stretches).
D''' (union over the S-stretch's states s): box 135's D' edges (Even x not in CN -> Even v on the pre-merge segments Y', Z' of every pair
of options in T_x u {sigma_s(x)} with equal Xi-cycle node, and -> Even v on the W-key paths), PLUS x -> every ODD vertex on those
segments, PLUS for every Odd vertex o that lies on some segment at s: o -> every vertex (Even or Odd) on the pre-merge segments of every
pair of successors of o with equal Xi_s-cycle node. EHEIGHT = height counting Even vertices only (Odd vertices add no delay: sbar_s is a
function of sigma_s). CASCVIOL: an acyclic S-stretch longer than EHEIGHT + 1. TIES (hypothesis NT): number of (s, o) with o on a segment
and two successors of o with EQUAL Xi_s value; SBIN: sbar changes inside S-stretches (they would have cut box 135's stretches).
SBSTR / SBACYC / SBFL: S-stretches containing an sbar change / those with acyclic D''' / their FL transitions.
SHOWCYC=1 prints one cycle per cyclic S-stretch.
Usage: dmerge3.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "..", "box132", "anchor.py")).read().split("R = dict(runs")[0]
exec(src.replace("os.path.dirname(os.path.abspath(__file__))", repr(os.path.join(HERE, "..", "box132"))))
R = dict(sstretches=0, fl=0, acyc=0, cyc=0, eheight=0, cascviol=0, edges=0, maxl=0, cnmov=0, sbin=0, ties=0, oddnodes=0, sbstr=0, sbacyc=0, sbfl=0)
def play(succ1, v):
    seq = []; pos = {}
    while v not in pos: pos[v] = len(seq); seq.append(v); v = succ1[v]
    return seq
def segs(succ1, vs, y, z):
    py, pz = play(succ1, y), play(succ1, z); w = vs[y][0]
    if w not in py or w not in pz: return []
    yw = py[:py.index(w) + 1]; zw = pz[:pz.index(w) + 1]; c = 0
    while c < min(len(yw), len(zw)) and yw[-1 - c] == zw[-1 - c]: c += 1
    return yw[:len(yw) - c] + zw[:len(zw) - c]
def sstretches(a, b):
    out = []; s0 = a; W0 = wval(a); CN0 = {v for v in range(n) if W0[v][2] == 0}
    cyc = lambda j: tuple(E.evaluate(S[j])[0][v][0] for v in range(n))
    for j in range(a + 1, b + 1):
        if any(S[j][c] != S[j - 1][c] for c in CN0 if own[c] == 0):
            R["cnmov"] += 1
            if j - 1 > s0: out.append((s0, j - 1))
            s0 = j; continue
        if cyc(j - 1) != cyc(s0):
            if j - 1 > s0: out.append((s0, j - 1))
            s0 = j - 1
    if b > s0: out.append((s0, b))
    return out
for a0, b0 in runs:
  for a, b in sstretches(a0, b0):
    R["sstretches"] += 1
    tau = T[a]; W = wval(a); CN = {v for v in range(n) if W[v][2] == 0}
    Tx = {x: [y for y in g.succ[x] if (W[y][2] == W[x][2] - 1 and W[y][0] == W[x][0])] for x in range(n) if own[x] == 0 and x not in CN}
    adj = {v: set() for v in range(n)}
    for s in range(a, b + 1):
        vs, sb = E.evaluate(S[s]); succ1 = [S[s][v] if own[v] == 0 else sb[v] for v in range(n)]
        if s > a: R["sbin"] += sum(1 for o in range(n) if own[o] == 1 and sb[o] != E.evaluate(S[s - 1])[1][o])
        todo = []
        for x, opts in Tx.items():
            os_ = sorted(set(opts) | {S[s][x]})
            for i in range(len(os_)):
                for k in range(i + 1, len(os_)):
                    y, z = os_[i], os_[k]
                    if vs[y][0] != vs[z][0]: continue
                    for v in segs(succ1, vs, y, z):
                        if v != x: adj[x].add(v)
                        if own[v] == 1: todo.append(v)
        done = set()
        while todo:
            o = todo.pop()
            if o in done: continue
            done.add(o); su = sorted(set(g.succ[o]))
            keys = [E.key(vs[w]) for w in su]
            if len(set(keys)) < len(keys) and min(keys) in [k for k in keys if keys.count(k) > 1]: R["ties"] += 1
            for i in range(len(su)):
                for k in range(i + 1, len(su)):
                    y, z = su[i], su[k]
                    if vs[y][0] != vs[z][0]: continue
                    for v in segs(succ1, vs, y, z):
                        if v != o: adj[o].add(v)
                        if own[v] == 1: todo.append(v)
        R["oddnodes"] += len(done)
        sW = [S[s][v] if own[v] == 0 else tau[v] for v in range(n)]
        for x, opts in Tx.items():
            for y in set(opts) | {S[s][x]}:
                v = y
                while W[v][2] > 0:
                    if own[v] == 0 and v != x: adj[x].add(v)
                    v = sW[v]
    sbhere = sum(1 for s2 in range(a + 1, b + 1) for o in range(n) if own[o] == 1 and E.evaluate(S[s2])[1][o] != E.evaluate(S[s2 - 1])[1][o])
    R["fl"] += b - a; R["maxl"] = max(R["maxl"], b - a); R["edges"] += sum(len(e) for e in adj.values())
    state = {}; h = {}; cyc = False
    for v0 in adj:
        if v0 in state: continue
        st = [(v0, iter(adj[v0]))]; state[v0] = 1
        while st and not cyc:
            v, it = st[-1]; nx = next(it, None)
            if nx is None:
                state[v] = 2; h[v] = (1 if own[v] == 0 else 0) + max((h[w] for w in adj[v]), default=0); st.pop()
            elif state.get(nx) == 1:
                cyc = True
                if os.environ.get('SHOWCYC'): pth = [u for u, _ in st]; print('CYCLE', [(u, 'E' if own[u] == 0 else 'O') for u in pth[pth.index(nx):]] + [nx], 'stretch', (a, b))
            elif nx not in state: state[nx] = 1; st.append((nx, iter(adj[nx])))
        if cyc: break
    R["sbstr"] += sbhere > 0
    if sbhere and not cyc: R["sbacyc"] += 1; R["sbfl"] += b - a
    if cyc: R["cyc"] += 1
    else:
        H = max([h[x] - 1 for x in Tx if x in h] + [0]); R["acyc"] += 1; R["eheight"] = max(R["eheight"], H); R["cascviol"] += (b - a) > H + 1
print(f"DMERGE3 {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k.upper()} {v}" for k, v in R.items()))
