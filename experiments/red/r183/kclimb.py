#!/usr/bin/env python3
"""L-RED R183: adversarial climb against Lemma OVT-KEY. SCORE = 10^6 * (RET_IN + OVER + KBOUND) + RETURNS (ovtkey.analyse, default S3
start). Mutations r179/climb179.mut. Usage: kclimb.py seed.pg iters seed out.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r179"), os.path.join(HERE, "..", "..", "new", "box21")]
import ovtkey, climb179
from n5x import load
def score(g):
    try: R = ovtkey.analyse(g, None, cap=600)
    except Exception: return -1, None
    return 10 ** 6 * (R["ret_in"] + R["over"] + R["kbound"]) + R["returns"], R
src, iters, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
g = load(src); bs, R = score(g); print("START", bs, R, flush=True)
for it in range(iters):
    h = climb179.mut(g, rng); hs, HR = score(h)
    if hs >= bs:
        if hs > bs: print("IT", it, HR, flush=True)
        g, bs, R = h, hs, HR; climb179.write(g, out)
print("BEST", R, flush=True)
