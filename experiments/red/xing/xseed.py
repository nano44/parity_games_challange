#!/usr/bin/env python3
"""Box 32 seed family for the (X) scaling: for each n, the first random o-cyclic C^1O game from L-NEW's rand_c1o (forced=0.0,
rng = Random(1000 + n)) that L-NEW's box28 xclimb.fit accepts. Run from inside a checkout of l-new's experiments/new/box28 (07614f6e).
Usage: xseed.py n out.pg   (prints the seed's fitness (X - O, phase length))"""
import sys, os, random
sys.path.insert(0, os.getcwd())
import xclimb as XC
from common import rand_c1o
n, out = int(sys.argv[1]), sys.argv[2]; rng = random.Random(1000 + n)
while True:
    g = rand_c1o(rng, n, n, forced=0.0)
    if g is None: continue
    G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = XC.fit(G)
    if f[0] >= 0: break
open(out, "w").write(f"parity {n-1};\n" + "".join(f"{v} {G[0][v]} {G[1][v]} {','.join(map(str, G[2][v]))};\n" for v in range(n)))
print(n, f)
