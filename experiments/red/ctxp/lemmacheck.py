#!/usr/bin/env python3
"""L-RED box 11 (produced on Opus 5.5): random check of (DEEP-STAB): the first best_vertices call of every search_rec call at
depth >= 1 returns 0 or -1, never 1. Prints any game that violates it. Usage: lemmacheck.py SEED TRIES NMIN NMAX OUTDIR"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import depthscan as DS, pg
seed, tries, nmin, nmax, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); os.makedirs(out, exist_ok=True); nsub = 0; nd1 = 0
for it in range(tries):
    n = rng.randint(nmin, nmax)
    pr = [rng.randint(0, n) for _ in range(n)]; ow = [rng.randint(0, 1) for _ in range(n)]
    su = [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 3)))) for _ in range(n)]
    g = pg.Game(pr, ow, su); d = DS.scan(g)
    nsub += sum(1 for r in d.rows for _, y in r["recs"] if y > 0); nd1 += DS.deepres1(d)
    if DS.firstbv1(d):
        f = os.path.join(out, f"viol_s{seed}_i{it}.pg"); pg.write(g, f); print("VIOLATION", f, flush=True)
print(f"done tries {tries} nonempty-subcalls {nsub} deep-res1 {nd1}")
