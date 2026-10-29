#!/usr/bin/env python3
"""L-SI box 24: greedy random option addition to an Odd gate Q (env Q, default 5) for RUN-LIN'. Each trial adds an Even vertex x with 2-4
random successors (from all vertices) and a random priority in [0, 2n + 4], plus the edge Q -> x; a trial is kept if the longest fallback-free
run rises by >= MIN (env, default 3). ROUNDS rounds of TRIALS trials. Usage: optadd.py G.pg G.start ROUNDS TRIALS SEED OUT"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from stretchall import run
from growclimb import save
from common import load, readstart
import pg
g = load(sys.argv[1]); s0, t0 = readstart(sys.argv[2]); rounds, trials, seed, out = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
Q = int(os.environ.get("Q", "5")); MIN = int(os.environ.get("MIN", "3")); rng = random.Random(seed)
cur = run(g, (s0, t0)); print("start run", cur, "n", g.n, flush=True)
for k in range(rounds):
    best = None
    for _ in range(trials):
        x = g.n; succ = [list(s) for s in g.succ]; succ.append(sorted(rng.sample(range(g.n), rng.randint(2, 4))))
        succ[Q] = sorted(set(succ[Q]) | {x}); p = rng.randint(0, 2 * g.n + 4)
        h = pg.Game(list(g.prio) + [p], list(g.owner) + [0], succ); s = dict(s0); s[x] = rng.choice(succ[x])
        try: r = run(h, (s, t0))
        except Exception: continue
        if best is None or r > best[0]: best = (r, h, s)
    if best is None or best[0] < cur + MIN: print("round", k + 1, "no gain; best", best[0] if best else None, flush=True); continue
    cur, g, s0 = best
    save("%s_o%d" % (out, k + 1), g, [s0.get(v, t0.get(v)) for v in range(g.n)])
    print("round", k + 1, "run", cur, "n", g.n, "run-2n", cur - 2 * g.n, "deg(Q)", len(g.succ[Q]), flush=True)
