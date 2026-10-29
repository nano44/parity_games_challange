#!/usr/bin/env python3
"""L-SI box 24: for every two-way Even pair u <-> w, subdivide it by a new Even vertex x (u: w -> x, w: u -> x, x: {u, w}) for priorities in
range(0, P, 3) and both starts sigma0(x); print the best longest-fallback-free-run per pair. Usage: stretchall.py G.pg G.start [P]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, HERE)
from common import rows, load, readstart
from trace import runs
import pg
def run(h, st):
    E, R = rows(h, st); return max((b - a for a, b, i, j in runs(R)), default=0)
def sub(g, s0, u, w, p, y):
    x = g.n; succ = [list(s) for s in g.succ]
    succ[u] = sorted((set(succ[u]) - {w}) | {x}); succ[w] = sorted((set(succ[w]) - {u}) | {x}); succ.append(sorted({u, w}))
    h = pg.Game(list(g.prio) + [p], list(g.owner) + [0], succ); s = dict(s0)
    if s.get(u) == w: s[u] = x
    if s.get(w) == u: s[w] = x
    s[x] = y; return h, s
if __name__ == "__main__":
    g = load(sys.argv[1]); s0, t0 = readstart(sys.argv[2]); P = int(sys.argv[3]) if len(sys.argv) > 3 else 2 * g.n + 4
    print("base", run(g, (s0, t0)), "n", g.n, flush=True)
    for u in range(g.n):
        for w in g.succ[u]:
            if w <= u or u not in g.succ[w] or g.owner[u] or g.owner[w]: continue
            best = (0,)
            for p in range(0, P, 3):
                for y in (u, w):
                    h, s = sub(g, s0, u, w, p, y)
                    try: r = run(h, (s, t0))
                    except Exception: r = -1
                    best = max(best, (r, p, y))
            print(u, w, best, flush=True)
