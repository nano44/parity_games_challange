#!/usr/bin/env python3
"""L-RED R177: abstract model with Xi-target = W-target on the ladder (beta per target vertex). Random gate orders / beta ranks /
parities / starts; prints the best FL length. Usage: sameface.py d trials seed"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import abs177 as A
d, trials, seed = (int(a) for a in sys.argv[1:4]); rng = random.Random(seed); best = 0
for t in range(trials):
    g = A.laddergen(d, rng)
    g["opts"] = [[[o[0], ("X" if o[0] == "W" else o[0])] for o in opts] for opts in g["opts"]]
    # beta ranks: lower level = more relevant (CDAG-like) with prob 1/2, else random
    if rng.random() < 0.5:
        g["brank"] = [2 * d - 1 - i for i in range(2 * d)]
    s = A.score(g)
    if s > best: best = s; print("T", t, "FL", s, flush=True)
print("SAMEFACE d", d, "best", best)
