#!/usr/bin/env python3
"""L-SI box 24: greedy stretching with priority-0 subdividers only (fast form of stretchiter.py): each round try every two-way Even pair and
both starts, apply the longest run. Prints run, n, run - 2n per round; saves OUT_g<k>. Usage: stretch0.py G.pg G.start ROUNDS OUT"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from stretchall import run, sub
from growclimb import save
from common import load, readstart
g = load(sys.argv[1]); s0, t0 = readstart(sys.argv[2]); rounds, out = int(sys.argv[3]), sys.argv[4]
print("round 0 run", run(g, (s0, t0)), "n", g.n, flush=True)
for k in range(1, rounds + 1):
    best = None
    for u in range(g.n):
        for w in g.succ[u]:
            if w <= u or u not in g.succ[w] or g.owner[u] or g.owner[w]: continue
            for y in (u, w):
                h, s = sub(g, s0, u, w, 0, y)
                try: r = run(h, (s, t0))
                except Exception: continue
                if best is None or r > best[0]: best = (r, u, w, y, h, s)
    r, u, w, y, g, s0 = best
    save("%s_g%d" % (out, k), g, [s0.get(v, t0.get(v)) for v in range(g.n)])
    print("round", k, "pair", (u, w), "run", r, "n", g.n, "run-2n", r - 2 * g.n, "ratio %.3f" % (r / g.n), flush=True)
