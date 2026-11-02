#!/usr/bin/env python3
"""L-RED R179 LASSOCK: independent re-check of odxi's FL / XICH findings. sigma, tau, sigma-bar come from N5's own run (n5x; sigma-bar
from the engine, as SPEC defines it); W and Xi are recomputed WITHOUT si.py as lasso valuations of the functional graphs
(sigma + tau) and (sigma + sigma-bar): cycle node = max (priority, index) on the cycle, P = vertices before the cycle node above it,
length = steps to the cycle node; compared by SPEC S1. Prints LASSOCK <game> fltrans xich (must equal odxi's). Usage: lassock.py G.pg [START|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, readstart, Engine, dual, step
def lasso(succ, pr, x):
    seq = []; pos = {}; y = x
    while y not in pos: pos[y] = len(seq); seq.append(y); y = succ[y]
    cyc = seq[pos[y]:]; c = max(cyc, key=lambda z: (pr[z], z)); pre = seq[:seq.index(c)]
    return (c, frozenset(z for z in pre if (pr[z], z) > (pr[c], c)), len(pre))
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n, own, pr = g.n, g.owner, g.prio; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st)
S, T, F = [list(s)], [list(t)], []
while len(S) <= 2000:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(list(r[0])); T.append(list(r[1])); F.append(r[4])
SB = [E.evaluate(tuple(x))[1] for x in S]
fl = 0; xich = 0
for j in range(1, len(S)):
    if F[j - 1] or T[j] != T[j - 1] or SB[j] != SB[j - 1] or S[j] == S[j - 1]: continue
    sw = lambda k: [S[k][v] if own[v] == 0 else T[j - 1][v] for v in range(n)]
    sx = lambda k: [S[k][v] if own[v] == 0 else SB[j][v] for v in range(n)]
    W1 = [lasso(sw(j), pr, v) for v in range(n)]; W0 = [lasso(sw(j - 1), pr, v) for v in range(n)]
    if W1 != W0: continue
    fl += 1
    X1 = [lasso(sx(j), pr, v) for v in range(n)]; X0 = [lasso(sx(j - 1), pr, v) for v in range(n)]
    xich += sum(1 for o in range(n) if own[o] == 1 and SB[j][o] != T[j - 1][o] and X1[o] != X0[o])
print(f"LASSOCK {os.path.basename(sys.argv[1])} fltrans {fl} xich {xich}")
