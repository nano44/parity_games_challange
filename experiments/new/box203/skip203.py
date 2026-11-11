#!/usr/bin/env python3
"""P-N5-QN fixes entry 1, LN-5 (L-NEW successor 69): how many genomes lam203.py skips for lfail (k > 12, fvs202.kfvs returns ">12").
Replays exactly lam203.py --rand's genome stream (same seed, same rand191.rgen / k1srch202.mk calls, same k filter) without the IDEAL-CYC
run, and prints the genome count, the skip count and the distribution of k. Usage: skip203.py MODE SEED COUNT (MODE rand / k1 / k2)."""
import sys, os, random, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gfc203
sys.path.insert(0, os.path.join(gfc203.ROOT, "experiments/new/box191"))
import fvs202
mode, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); c = collections.Counter(); n = 0
import rand191
os.environ["K1_MODE"] = "2" if mode == "k2" else "1"
import k1srch202
while n < cnt:
    if mode == "rand": G = rand191.rgen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
    else:
        G = k1srch202.mk(rng)
        if G is None or fvs202.kfvs(G)[0] != (2 if mode == "k2" else 1): continue
    k = fvs202.kfvs(G)[0]; n += 1; c[k] += 1
skip = sum(v for k, v in c.items() if not isinstance(k, int))
print(mode, "seed", seed, "genomes", n, "skipped_k_gt_12", skip, "k_distribution", sorted(c.items(), key=str), flush=True)
