#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5; from k4b/umix.py): random interacting unions of 2-3 corpus games (priorities kept, ids shifted) plus
c random cross edges (c = 0..CMAX), scored with meet/meetfit.py in both orders; prints (MEET) failures / incomplete runs
and a near (meet = 1 straddle) histogram. Usage: umeet.py SEED COUNT OUTDIR CMAX NMAX G.pg ..."""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "meet"))
import meetfit, pg
seed, cnt, out, cmax, nmax = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]), int(sys.argv[5])
gs = []
for f in sys.argv[6:]:
    try:
        g = pg.read(f)
        if g.n <= nmax: gs.append(g)
    except Exception: pass
rng = random.Random(seed); os.makedirs(out, exist_ok=True); hist = {}; runs = 0
for i in range(cnt):
    parts = rng.sample(gs, rng.choice([2, 2, 3])); prio, own, succ, offs = [], [], [], []
    for h in parts:
        o = len(prio); offs.append(o); prio += h.prio; own += h.owner; succ += [[w + o for w in s] for s in h.succ]
    N = len(prio)
    for _ in range(rng.randint(0, cmax)):
        u = rng.randrange(N); w = rng.randrange(N); succ[u] = sorted(set(succ[u]) | {w})
    g = pg.Game(prio, own, succ)
    for order in ("oink", "stable"):
        try: m = meetfit.measure_game(g, order)
        except RecursionError: continue
        if m["wsearch"] == 0: continue
        runs += 1; hist[m["near"]] = hist.get(m["near"], 0) + 1
        if m["incomplete"] or m["meetfail"]:
            fn = os.path.join(out, f"um_{seed}_{i}_{order}.pg"); open(fn, "w").write(pg.dumps(g)); print("HIT", order, m, fn, flush=True)
    if i % 500 == 0: print("progress", i, runs, sorted(hist.items()), flush=True)
print("done", cnt, runs, sorted(hist.items()))
