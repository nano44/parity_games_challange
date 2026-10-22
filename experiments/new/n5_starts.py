#!/usr/bin/env python3
"""Box 4: N5 (n5.run, unmodified) from random start pairs on a game; prints max / mean iterations and fallbacks.
Usage: n5_starts.py game.pg samples seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n5
from n5 import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); k, seed = int(sys.argv[2]), int(sys.argv[3])
rng = random.Random(seed); its = []
for _ in range(k):
    st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1})
    it, fb, *_ = n5.run(g, start=st); its.append((it, fb))
print(f"n={g.n} samples={k}: max iterations {max(i for i, _ in its)}, mean {sum(i for i, _ in its)/k:.1f}, max fallbacks {max(f for _, f in its)}")
