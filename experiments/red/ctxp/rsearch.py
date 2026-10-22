#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): random search for games that learn tangles inside a search_rec call of depth >= 1
(the R39 §9 necessary condition for a hidden clock). Usage: rsearch.py SEED TRIES NMIN NMAX OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import depthscan as DS, pg
seed, tries, nmin, nmax, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); os.makedirs(out, exist_ok=True); best = 0
for it in range(tries):
    n = rng.randint(nmin, nmax); deg = rng.choice([2, 2, 3])
    pr = [rng.randint(0, n) for _ in range(n)]; ow = [rng.randint(0, 1) for _ in range(n)]
    su = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, deg)))) for _ in range(n)]
    g = pg.Game(pr, ow, su)
    try: d = DS.scan(g)
    except RecursionError: continue
    b = DS.deepres1(d) + 100 * DS.deepborn(d)
    if b > best:
        best = b; f = os.path.join(out, f"deep_s{seed}_i{it}_n{n}_b{b}.pg"); pg.write(g, f); print(it, n, b, f, flush=True)
print("done best", best)
