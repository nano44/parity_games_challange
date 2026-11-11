#!/usr/bin/env python3
"""Box 203 (L-NEW successor 68): random sweep of gfc203.census on IDEAL-CYC. Sets: MODE=rand (box191 rand191.rgen with d 1-6, w 1-3, degree 2-3, the shape of RESULTS R123's
1,000-genome set) or MODE=k1 (box202 k1srch202.mk: eg195 'acyc' + edges into one mover f, kept only if k = 1 by fvs202.kfvs).
Prints TOTALS of the must-0 counters (gfc203.MUST0) and the maxima of maxflip, maxDE, T, and the number of genomes.
Usage: rnd203.py MODE SEED COUNT  (ROOT default from this file's place)."""
import sys, os, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gfc203
sys.path.insert(0, os.path.join(gfc203.ROOT, "experiments/new/box191"))
mode, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); tot = collections.Counter(); mx = collections.Counter()
import rand191, k1srch202, fvs202
while tot["genomes"] < cnt:
    if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))   # R123's set shape: d 1-6, w 1-3, degree 2-3
    else:
        G = k1srch202.mk(rng)
        if G is None or fvs202.kfvs(G)[0] != 1: continue
    r = gfc203.census(G); tot["genomes"] += 1
    for k in gfc203.MUST0: tot[k] += r.get(k, 0)
    for k in ("maxflip", "maxDE", "T", "maxquiet"): mx[k] = max(mx[k], r.get(k, 0))
    tot["flips_total_maxgate"] += r["maxflip"]
print(mode, "seed", seed, "genomes", tot["genomes"], " ".join(f"{k} {tot[k]}" for k in gfc203.MUST0), "| max", dict(mx), flush=True)
