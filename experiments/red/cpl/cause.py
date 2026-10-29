#!/usr/bin/env python3
"""L-RED successor 27: per switch (transition t, vertex v, target w): MENU if (v, w) was not in v's improving set at state t-1 (it
entered the menu at t: own side's doing, since I_sigma depends on sigma only and I_tau on tau only), STALL-k if (v, w) was improving at
states t-k..t but not taken before (released by a W-change; 'other side moved at t-1' marks whether the opponent changed at t-1 -> t).
Usage: cause.py GAME.pg START|S3"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cpl, n5b
g = n5b.pg.read(sys.argv[1]); lab = cpl.labels(sys.argv[1]); L = lambda v: lab.get(v, str(v))
s0, t0 = (None, None) if sys.argv[2] == "S3" else n5b.read_start(sys.argv[2], g)
N, tr, fb = cpl.run(g, s0, t0)
I = []
for s, t in tr:
    Is = N.improving(N.SG, list(s), N.ev(N.SG, list(s))); It = N.improving(N.SD, list(t), N.ev(N.SD, list(t)))
    I.append((Is, It))
for t in range(len(tr) - 1):
    out = []
    for side in (0, 1):
        A, B = tr[t][side], tr[t + 1][side]
        for v in range(g.n):
            if A[v] != B[v]:
                w = B[v]; k = 0
                while t - k - 1 >= 0 and tr[t - k - 1][side][v] == A[v] and w in I[t - k - 1][side].get(v, []):
                    k += 1
                other = 1 - side; om = t >= 1 and tr[t - 1][other] != tr[t][other]
                tag = "MENU" if k == 0 else f"STALL{k}{'/opp-moved' if om else ''}"
                out.append(f"{'s' if side == 0 else 't'}:{L(v)}->{L(w)}[{tag}]")
    print(t, "FB" if fb[t] else "  ", " ".join(out))
