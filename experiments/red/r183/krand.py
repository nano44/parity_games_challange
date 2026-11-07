#!/usr/bin/env python3
"""L-RED R183: ovtkey.analyse on random games (n in [6, 30], out-degree 1..4, priorities 0..n, random owners), default S3 start.
Usage: krand.py count seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
import ovtkey, pg
N, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); T = {}
for i in range(N):
    n = rng.randint(6, 30)
    g = pg.Game([rng.randint(0, n) for _ in range(n)], [rng.randint(0, 1) for _ in range(n)], [sorted(set(rng.randrange(n) for _ in range(rng.randint(1, 4)))) for _ in range(n)])
    R = ovtkey.analyse(g, None, cap=2000)
    for k, v in R.items(): T[k] = T.get(k, 0) + v
print("KRAND", N, seed, " ".join(f"{k.upper()} {v}" for k, v in T.items()))
