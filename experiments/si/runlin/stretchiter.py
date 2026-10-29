#!/usr/bin/env python3
"""L-SI box 24: greedy iterated corridor stretching. Each round: try every two-way Even pair and priorities range(0, P, 3), both starts; apply
the subdivision with the longest run (ties: higher run - 2n first); stop when no subdivision keeps run - 2n from falling by more than SLACK
(env, default 1). Saves each round's game as OUT_r<k>.pg/.start. Usage: stretchiter.py G.pg G.start ROUNDS OUT"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from stretchall import run, sub
from growclimb import save
from common import load, readstart
SLACK = int(os.environ.get("SLACK", "1"))
g = load(sys.argv[1]); s0, t0 = readstart(sys.argv[2]); rounds, out = int(sys.argv[3]), sys.argv[4]
cur = run(g, (s0, t0)); print("round 0 run", cur, "n", g.n, "run-2n", cur - 2 * g.n, flush=True)
for k in range(1, rounds + 1):
    P = 2 * g.n + 4; best = None
    for u in range(g.n):
        for w in g.succ[u]:
            if w <= u or u not in g.succ[w] or g.owner[u] or g.owner[w]: continue
            for p in range(0, P, 3):
                for y in (u, w):
                    h, s = sub(g, s0, u, w, p, y)
                    try: r = run(h, (s, t0))
                    except Exception: continue
                    if best is None or r > best[0]: best = (r, u, w, p, y, h, s)
    if best is None or best[0] - 2 * (g.n + 1) < cur - 2 * g.n - SLACK: print("stop", best[:5] if best else None); break
    r, u, w, p, y, g, s0 = best; cur = r
    st = [s0.get(v, t0.get(v)) for v in range(g.n)]; save("%s_r%d" % (out, k), g, st)
    print("round", k, "pair", (u, w), "prio", p, "run", r, "n", g.n, "run-2n", r - 2 * g.n, "ratio %.3f" % (r / g.n), flush=True)
