#!/usr/bin/env python3
"""L-SI box 31: diagnose a Lemma-P lag in one frozen W-phase [a, b] (core/sp.py's DEFA): at state k, the vertices x with W_k(x) < BF_j(x)
on the admitted graph for j = min(k - a, JA); prints x, W_k(x), the BF path and its value. Usage: diag.py GAME START|- a b k"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, load, readstart
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if sys.argv[2] != "-" else None; a, b, K = map(int, sys.argv[3:6])
E, R = rows(g, st, cap=b + 2); n = g.n; t = R[a]["t"]; lam = [w[0] for w in R[a]["W"]]
adm = [set() for _ in range(n)]
for k in range(a, b + 1):
    for x in range(n):
        if g.owner[x] == 0: adm[x].add(R[k]["s"][x])
    if k < b:
        for x, z in E.improving(tuple(R[k]["s"]), R[k]["vs"]): adm[x].add(z)
P = [((x, 0, 0), 1 << x, [x]) if lam[x] == x else None for x in range(n)]
for j in range(min(K - a, n)):
    Q = list(P)
    for x in range(n):
        for z in (adm[x] if g.owner[x] == 0 else [t[x]]):
            if P[z] is None or (P[z][1] >> x) & 1: continue
            v = E.extend(x, P[z][0])
            if Q[x] is None or E.key(v) > E.key(Q[x][0]): Q[x] = (v, P[z][1] | (1 << x), [x] + P[z][2])
    P = Q
W = R[K]["W"]; bad = [x for x in range(n) if P[x] is not None and E.key(W[x]) < E.key(P[x][0])]
print("k", K, "j", K - a, "bad", len(bad))
for x in bad[:6]:
    print("x", x, "own", g.owner[x], "W", (W[x][0], E.weight(W[x][1]), W[x][2]), "BF", (P[x][0][0], E.weight(P[x][0][1]), P[x][0][2]), "path", P[x][2][:25])
    y = x; pl = [x]
    for _ in range(30):
        y = R[K]["wn"][y]; pl.append(y)
    print("   play", pl)
