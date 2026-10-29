#!/usr/bin/env python3
"""Random search for long runs of abs2 (two-order switch-best). Usage: search.py N TRIALS SEED [same]"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from abs2 import run, paths
def rew(p): return p if p % 2 == 0 else -p
def inst(n, rnd, same=False):
    while True:
        G = []
        for x in range(n):
            d = rnd.randint(1, 3)
            G.append(sorted(set(rnd.sample([y for y in range(n + 1) if y != x], min(d, n)))))
        pv = rnd.sample(range(2, 4 * n + 8), n + 2)
        pp = pv[:n]; th1, th2 = pv[n], pv[n + 1]
        if same: th2 = th1
        if th1 != th2 and rew(th2) < rew(th1): th1, th2 = th2, th1
        # random initial strategy reaching t
        for _ in range(50):
            rho = [rnd.choice(G[x]) for x in range(n)]
            if all(p is not None for p in paths(rho, n).values()): return G, rho, pp, th1, th1 % 2, th2, th2 % 2
n, T, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); same = len(sys.argv) > 4
rnd = random.Random(seed); best = (-1,); from collections import Counter; C = Counter()
for i in range(T):
    r = inst(n, rnd, same)
    if r is None: continue
    w, s, why, h = run(*r)
    C[why] += 1
    if w > best[0]: best = (w, s, why, r)
print(dict(C)); print("best W-changing steps", best[0], "n", n, "inst", best[3])
