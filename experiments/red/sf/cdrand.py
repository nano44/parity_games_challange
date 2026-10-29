#!/usr/bin/env python3
"""L-RED successor 29 (R117 §3): random sample of cdmask.py reader configs. Usage: cdrand.py n K seed"""
import sys, os, random
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cdmask.py")).read().split("if __name__")[0])
n = int(sys.argv[1]); K = int(sys.argv[2]); random.seed(int(sys.argv[3]))
edges = [(v, u) for v in range(2, n + 1) for u in range(1, v)]
bps = list(range(5, 4 * n + 7, 2)); best = (0,)
hist = {}
for _ in range(K):
    cfg = {}
    for e in edges:
        if random.random() < 0.8: cfg[e] = (random.randint(0, n), random.choice(bps))
    r = run(build(n, cfg), n)
    if r is None: continue
    hist[r[0]] = hist.get(r[0], 0) + 1
    if r[0] > best[0]: best = (r[0], r[1], cfg); print(best, flush=True)
print("hist", sorted(hist.items()))
