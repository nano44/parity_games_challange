#!/usr/bin/env python3
"""L-NEW box 52: in the longest phase of a game's N5 run, the pair (a, b) of vertices with the same Xi cycle node at every state of the
phase whose Xi order flips most often (states with Xi(a) = Xi(b) skipped). Prints "a b flips phase". Usage: flippair.py GAME [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, load, readstart, phases
g = load(sys.argv[1]); E, R = rows(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None, cap=20000)
i, j = max(phases(R), key=lambda p: p[1] - p[0]); X = [[E.key(x) for x in R[k]["vs"]] for k in range(i, j + 1)]; n = g.n
cn = [{R[k]["vs"][v][0] for k in range(i, j + 1)} for v in range(n)]; best = (-1, 0, 0)
for a in range(n):
    if len(cn[a]) != 1: continue
    for b in range(a + 1, n):
        if cn[b] != cn[a]: continue
        prev = None; fl = 0
        for x in X:
            if x[a] == x[b]: continue
            o = x[a] < x[b]
            if prev is not None and o != prev: fl += 1
            prev = o
        best = max(best, (fl, a, b))
print(best[1], best[2], best[0], (i, j))
