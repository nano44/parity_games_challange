#!/usr/bin/env python3
"""L-RED 53 R215: run N5'-xi for K iterations from S3, then continue with MODE2 (spec / xi); prints total. Usage: fromstate.py GAME K MODE2"""
import sys, os
WT = os.environ["WT"]
sys.path[:0] = [os.path.join(WT, "experiments/new/box190"), os.path.join(WT, "experiments/new/box21"), os.path.join(WT, "experiments/harness")]
import n5v, n5x
from si import Engine
g = n5x.load(sys.argv[1]); K = int(sys.argv[2]); m2 = sys.argv[3]
E, Ed = Engine(g), Engine(n5v.dual(g)); s, t = n5x.start_pair(g, E, Ed, None); it = 0
while True:
    r = n5v.step(g, E, Ed, s, t, "xi" if it < K else m2)
    if r is None: break
    s, t = r[0], r[1]; it += 1
print(f"K {K} then {m2}: total {it}")
