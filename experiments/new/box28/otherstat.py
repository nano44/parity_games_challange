#!/usr/bin/env python3
"""Box 28: clause pattern of OTHER states ((h) fails, Ξ ≠ W) and of non-(h) Ξ = W states, on random o-cyclic C^1O runs.
Usage: otherstat.py N lo hi seed [--randstart]"""
import sys, random
from nhprof import *
a = sys.argv[1:]; RS = "--randstart" in a; N, lo, hi, seed = map(int, a[:4]); rng = random.Random(seed)
cnt = {}; runs = 0
for i in range(N):
    g = rand_c1o(rng, lo, hi, forced=0.0)
    if g is None: continue
    start = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
             {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
    rows, ph = profile(g, start); runs += 1
    for r in rows:
        if all(r["h"]): continue
        key = ("OTHER" if r["Xk"] != r["Wk"] else "EQ-nonh", clause(r["h"]), "split" if r["split"] else "coinc")
        cnt[key] = cnt.get(key, 0) + 1
print(f"runs {runs}"); [print(k, v) for k, v in sorted(cnt.items())]
