#!/usr/bin/env python3
"""Box 47: write game number I of the sample `--rand C LO HI GSEED` (same generator and order as xd2.py) to OUT.pg.
Usage: dumprand.py C LO HI GSEED I OUT.pg"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "../box43"))
from multi import rand_ckO
cnt, lo, hi, seed, I = map(int, sys.argv[1:6]); out = sys.argv[6]; rng = random.Random(seed)
for i in range(cnt):
    g = rand_ckO(rng, lo, hi, rng.randint(2, 4))
    if i == I: break
with open(out, "w") as f:
    f.write(f"parity {g.n - 1};\n")
    for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
