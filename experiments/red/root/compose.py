#!/usr/bin/env python3
"""L-RED box 7 (produced on Opus 5.5): can #DIRTY per phase ADD across copies? Takes copies of a game (ids shifted, copy j's
priorities raised by j * SHIFT so later copies sit above earlier ones when SHIFT > 0), adds c random cross edges
(c = 0..CMAX), and scores with root/rootfit.py (L-ALG dtl_rootmono.py unmodified) in the given order. Prints every union
whose max dirty per phase exceeds BASE (the single-copy value) and the best seen.
Usage: compose.py SEED COUNT ORDER COPIES SHIFT CMAX BASE G.pg OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rootfit
sys.path.insert(0, os.path.join(os.environ["LALGR_DIR"], "experiments", "harness"))
import pg
seed, cnt, order, copies, shift, cmax, base, src, out = (int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]),
                                                         int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), sys.argv[8], sys.argv[9])
g = pg.read(src); rng = random.Random(seed); os.makedirs(out, exist_ok=True); best = (-1, None)
for i in range(cnt):
    prio, own, succ = [], [], []
    for j in range(copies):
        o = len(prio); prio += [p + j * shift for p in g.prio]; own += list(g.owner); succ += [[w + o for w in s] for s in g.succ]
    N = len(prio)
    for _ in range(rng.randint(0, cmax)):
        u = rng.randrange(N); w = rng.randrange(N); succ[u] = sorted(set(succ[u]) | {w})
    h = pg.Game(prio, own, succ); fn = os.path.join(out, f"cmp_{seed}_{i}.pg"); open(fn, "w").write(pg.dumps(h))
    m = rootfit.measure(fn, order)
    if m["hit"] or m["maxdirty"] > base or m["maxdirty"] > best[0]:
        print("UNION", i, m, fn, flush=True)
        if m["maxdirty"] > best[0]: best = (m["maxdirty"], fn)
    if not (m["hit"] or m["maxdirty"] > base): os.unlink(fn)
    if i % 50 == 0: print("progress", i, "best", best, flush=True)
print("done", cnt, "best", best)
