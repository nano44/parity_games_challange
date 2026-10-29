#!/usr/bin/env python3
"""L-SI box 31: list the late adoptions of one same-pair frozen W-phase [a, b] (as core/late.py): tau, x, old -> new successor, basin of x at
tau / tau+1, basin of z at tau, the earlier refusal states of (x, z). Usage: lateshow.py GAME START|- a b"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, os.path.join(HERE, "..", "tord"))
from common import rows, load, readstart
from gates import basins
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if sys.argv[2] != "-" else None; a, b = int(sys.argv[3]), int(sys.argv[4])
E, R = rows(g, st, cap=b + 2); n = g.n
D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
print("n", n, "D", sorted(D))
REF = {}
for k in range(a, b):
    Fk = basins(R[k]["wn"], D, n); F1 = basins(R[k + 1]["wn"], D, n); G3k = {d for d in D if Fk[R[k]["t"][d]] != d and Fk[R[k]["sb"][d]] != d}; Is = {}
    for x, z in E.improving(tuple(R[k]["s"]), R[k]["vs"]): Is.setdefault(x, set()).add(z)
    for x in range(n):
        if g.owner[x] != 0: continue
        z = R[k + 1]["s"][x]
        if z != R[k]["s"][x] and (x, z) in REF:
            print("tau", k, "x", x, R[k]["s"][x], "->", z, "basin x", Fk[x], "->", F1[x], "basin z", Fk[z], "refused at", REF[(x, z)][:6], len(REF[(x, z)]))
        al = {R[k]["s"][x]} | Is.get(x, set()) | {w for w in g.succ[x] if Fk[w] == -1}
        if Fk[x] != -1 and Fk[x] in G3k: al |= {w for w in g.succ[x] if Fk[w] == Fk[x]}
        for w in g.succ[x]:
            if w not in al: REF.setdefault((x, w), []).append(k)
