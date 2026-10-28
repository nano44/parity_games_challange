#!/usr/bin/env python3
"""L-SI box 24 (successor 20): subdivide a two-way corridor edge pair u <-> w of a game by a new Even vertex x (u: w -> x, w: u -> x,
x: {u, w}), for each priority p in a range and each start sigma0(x); print the longest fallback-free run. Usage: stretch.py G.pg G.start u w"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, HERE)
from common import rows, load, readstart
from trace import runs
import pg
g = load(sys.argv[1]); s0, t0 = readstart(sys.argv[2]); u, w = int(sys.argv[3]), int(sys.argv[4])
def run(h, st):
    E, R = rows(h, st); return max((b - a for a, b, i, j in runs(R)), default=0)
print("base", run(g, (s0, t0)), "n", g.n)
x = g.n; res = []
for p in range(0, 70):
    succ = [list(s) for s in g.succ]
    succ[u] = sorted((set(succ[u]) - {w}) | {x}); succ[w] = sorted((set(succ[w]) - {u}) | {x}); succ.append(sorted({u, w}))
    h = pg.Game(list(g.prio) + [p], list(g.owner) + [0], succ)
    for y in (u, w):
        s = dict(s0)
        if s.get(u) == w: s[u] = x
        if s.get(w) == u: s[w] = x
        s[x] = y
        try: r = run(h, (s, t0))
        except Exception as e: r = -1
        res.append((r, p, y))
res.sort(reverse=True); print("best", res[:6])
