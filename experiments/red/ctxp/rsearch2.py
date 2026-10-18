#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): random search for transitions whose first difference lies at search_rec depth >= 1
(ctxfit.py rule). Saves every improvement. Usage: rsearch2.py SEED TRIES NMIN NMAX OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ctxfit as CF, pg
seed, tries, nmin, nmax, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); os.makedirs(out, exist_ok=True); best = (0, 0)
for it in range(tries):
    n = rng.randint(nmin, nmax)
    pr = [rng.randint(0, n) for _ in range(n)]; ow = [rng.randint(0, 1) for _ in range(n)]
    su = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    g = pg.Game(pr, ow, su)
    try: tr, cx, deep = CF.summary(CF.run(g))
    except RecursionError: continue
    if (deep, cx) > best:
        best = (deep, cx); f = os.path.join(out, f"d_s{seed}_i{it}_n{n}_deep{deep}_cx{cx}.pg"); pg.write(g, f); print(it, n, tr, cx, deep, f, flush=True)
print("done best", best)
