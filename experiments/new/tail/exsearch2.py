#!/usr/bin/env python3
"""Box 10: like exsearch.py (random exploit assignments on the gadgeted Odd-CDAG) but with a RANDOM start tau0 (each Odd vertex picks a random
CDAG target) instead of all -> sink. Fitness = tail steps with sigma optimal. Usage: exsearch2.py n K seed"""
import sys, random
from tailsim import build, tail
n, K, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed)
edges = [(x, u) for x in range(1, n + 1) for u in range(x)]; targets = list(range(n + 1)) + edges
best = 0; bestno = 0; hist = {}
for _ in range(K):
    ex = {}
    for e in edges:
        k = rng.choice([0, 1, 1, 2]); ts = [t for t in rng.sample(targets, k) if t != e[1] and t != e]
        if ts: ex[e] = ts
    g, sigma, gid = build(n, ex)
    t0 = [-1] * g.n; t0[0] = 0
    for x in range(1, n + 1): t0[x] = gid[(x, rng.randrange(x))]
    r = tail(g, sigma, t0, cap=2000)
    if r["optimal_sigma"]:
        hist[r["steps"]] = hist.get(r["steps"], 0) + 1
        if r["steps"] > best: best = r["steps"]; print("OPT steps", r["steps"], "tau0", [t0[x] for x in range(1, n + 1)], "exploits", ex, flush=True)
    elif r["steps"] > bestno: bestno = r["steps"]
print(f"DONE n={n} K={K} best optimal-sigma tail={best} (distribution {dict(sorted(hist.items()))}); best non-optimal run={bestno}")
