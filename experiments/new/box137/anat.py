#!/usr/bin/env python3
"""L-NEW box 137: anatomy of every double re-entry (x re-enters option y twice in one FL run): x's move sequence with, per move,
the W-key (root-first) of old/new option, Xi_(j-1) of both, the Xi-cycle node, and the Even vertices on the new option's W-path
that moved since x last left it. Usage: anat.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rel
from n5x import load, readstart
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
R, ex, K = rel.analyse(g, st); L = rel.LAST; S, T, E, runs = L["S"], L["T"], L["E"], L["runs"]; n, own = g.n, g.owner
print("REL", {k: R[k] for k in ("runs", "fl", "ret", "retmax", "movmax", "cwmov", "wwmov")})
for a, b in runs:
    tau = T[a]; W = L["wval"](a); lvl = [W[v][2] for v in range(n)]
    def path(j, y):
        p = [y]; v = y
        while lvl[v] > 0: v = S[j][v] if own[v] == 0 else tau[v]; p.append(v)
        return p
    def key(j, y): return tuple(reversed(path(j, y)[:-1]))
    XI = {j: E.evaluate(S[j])[0] for j in range(a, b + 1)}
    for x in range(n):
        if own[x] or lvl[x] == 0: continue
        seq = [(j, S[j - 1][x], S[j][x]) for j in range(a + 1, b + 1) if S[j][x] != S[j - 1][x]]
        ys = [y for (_, _, y) in seq]
        if not any(ys.count(y) + (y == S[a][x]) >= 3 for y in ys): continue
        print(f"RUN [{a},{b}] x {x} lvl {lvl[x]} start option {S[a][x]} T_x {[y for y in g.succ[x] if E.extend(x, W[y]) == W[x]]}")
        for j, o, y in seq:
            mv = [v for v in path(j, y)[:-1] if own[v] == 0 and v != y and any(S[i][v] != S[i - 1][v] for i in range(a + 1, j + 1))]
            print(f"  j {j}: {o} -> {y} | key {key(j - 1, o)} -> {key(j, y)} (new opt key at j-1 {key(j - 1, y)}) | Xi(j-1) old {XI[j - 1][o]}"
                  f" new {XI[j - 1][y]} | Xi(j-1)(y) cyc {XI[j - 1][y][0]} W cyc {W[y][0]} | moved-in-run on new path {mv}")
