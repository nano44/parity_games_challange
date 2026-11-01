#!/usr/bin/env python3
"""L-RED R185: adversarial climb against Lemma CN-UP. SCORE = 10^6 * DOWN_NOSHORT + 100 * DOWN + CNMOVES (cnidx.analyse, default
S3 start). Mutations r179/climb179.mut. Usage: cnupclimb.py seed.pg iters seed out.pg"""
import sys, os, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r179"), os.path.join(H, "..", "..", "new", "box21")]
import cnidx, climb179
from n5x import load
def score(g):
    try: R, _ = cnidx.analyse(g, None)
    except Exception: return -1, None
    return 10 ** 6 * R["down_noshort"] + 100 * R["down"] + R["cnmoves"], R
src, iters, seed, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
g = load(src); bs, R = score(g); print("START", bs, R, flush=True)
for it in range(iters):
    h = climb179.mut(g, rng); hs, HR = score(h)
    if hs >= bs:
        if hs > bs: print("IT", it, HR, flush=True)
        g, bs, R = h, hs, HR; climb179.write(g, out + ".tmp"); os.replace(out + ".tmp", out)
print("BEST", R, flush=True)
