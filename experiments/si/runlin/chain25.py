#!/usr/bin/env python3
"""L-SI box 24: repeatedly subdivide the pair (U, last) next to U (env U, default 25), new vertex priority 0, best of both starts and of the
two pair choices (U, x) / (x, y_old); print run and run - 2n per step. Usage: chain25.py G.pg G.start STEPS OUT"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from stretchall import run, sub
from growclimb import save
from common import load, readstart
g = load(sys.argv[1]); s0, t0 = readstart(sys.argv[2]); steps, out = int(sys.argv[3]), sys.argv[4]; U = int(os.environ.get("U", "25"))
last = max(w for w in g.succ[U] if U in g.succ[w] and g.owner[w] == 0)
print("start run", run(g, (s0, t0)), "n", g.n, "pair", (U, last), flush=True)
for k in range(steps):
    best = None
    for p in (0, 1, 2):
        for y in (U, last):
            h, s = sub(g, s0, U, last, p, y)
            r = run(h, (s, t0))
            if best is None or r > best[0]: best = (r, p, y, h, s)
    r, p, y, g, s0 = best; last = g.n - 1
    save("%s_c%d" % (out, k + 1), g, [s0.get(v, t0.get(v)) for v in range(g.n)])
    print("step", k + 1, "run", r, "n", g.n, "run-2n", r - 2 * g.n, "prio", p, flush=True)
