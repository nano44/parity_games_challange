#!/usr/bin/env python3
"""L-RED R139: second per-vertex Xi-change counter (n5b SPEC valuations, independent of l-new n5x/pch.py). Per W-run (tau constant, no
fallback): XICH(v) = transitions where Xi(v) = val(sigma, sigma-bar)(v) changes. Prints |F| of the longest W-run and the top vertex by XICH.
Usage: xichc.py GAME.pg START"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); EXP = os.path.abspath(os.path.join(HERE, "..", ".."))
for p in ("n5-second", "harness"): sys.path.insert(0, os.path.join(EXP, p))
import n5b
names = {}
for l in open(sys.argv[1]):
    a = l.strip().rstrip(";").split()
    if len(a) >= 5 and a[0].isdigit(): names[int(a[0])] = a[4].strip('"')
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g); N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []
N.run(s0, t0, trace=tr, fbtrace=fb)
best = (0, None, 0); cnt = {}; F = 0; prev = None
for i, (s, t) in enumerate(tr):
    x = N.ev(N.SG, list(s))
    if i == 0 or t != tr[i - 1][1] or fb[i - 1]: cnt = {}; F = 0
    elif prev is not None:
        F += 1
        for v in range(g.n):
            if x[v] != prev[v]:
                cnt[v] = cnt.get(v, 0) + 1
                if cnt[v] > best[0]: best = (cnt[v], names.get(v, v), F)
    prev = x
print(f"XICHC {os.path.basename(sys.argv[1])} n {g.n} iterations {len(tr) - 1} max-XICH {best[0]} at {best[1]} (W-run length so far {best[2]})")
