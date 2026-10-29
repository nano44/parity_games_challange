#!/usr/bin/env python3
"""L-SI box 24: add options to an Odd gate by cloning. For each option y of gate Q (env Q, default 5) and each priority shift d in -3..3 and each
extra edge choice (none / copy -> y / y -> copy for Even y), add a copy y' (same owner, priority prio(y)+d, same successors) and the edge Q -> y';
print the best longest-fallback-free run. Usage: optclone.py G.pg G.start"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from stretchall import run
from common import load, readstart
import pg
g = load(sys.argv[1]); s0, t0 = readstart(sys.argv[2]); Q = int(os.environ.get("Q", "5"))
base = run(g, (s0, t0)); print("base", base, "n", g.n, flush=True); res = []
for y in g.succ[Q]:
    for d in range(-3, 4):
        for mode in ("none", "to", "from"):
            if g.owner[y] == 1 and mode != "none": continue
            x = g.n; succ = [list(s) for s in g.succ]; succ.append(sorted(set(succ[y]) - {y}) or [y])
            if mode == "to": succ[x] = sorted(set(succ[x]) | {y})
            if mode == "from": succ[y] = sorted(set(succ[y]) | {x})
            succ[Q] = sorted(set(succ[Q]) | {x})
            h = pg.Game(list(g.prio) + [max(0, g.prio[y] + d)], list(g.owner) + [g.owner[y]], succ)
            s = dict(s0); t = dict(t0)
            if g.owner[y] == 0: s[x] = succ[x][0]
            else: t[x] = succ[x][0]
            try: r = run(h, (s, t))
            except Exception: continue
            res.append((r, y, d, mode))
res.sort(reverse=True); print("best", res[:8])
