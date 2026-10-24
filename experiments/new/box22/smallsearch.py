#!/usr/bin/env python3
"""Box 22: random search for small C^1O games (canonical run) with an I1 violation inside a fallback-free stretch with (h)
(HREQ=1 NOFB=1 semantics of shrinkP.violation). Usage: smallsearch.py N n seed"""
import sys, os, random
os.environ["HREQ"] = "1"; os.environ["NOFB"] = "1"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shrinkP import violation
N, n, seed = map(int, sys.argv[1:4]); INV = sys.argv[4] if len(sys.argv) > 4 else "I1"; rng = random.Random(seed); found = 0
for i in range(N):
    owner = [0] * n; o = rng.randrange(n); owner[o] = 1
    succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
    succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3)))))
    G = [[rng.randrange(n + 4) for _ in range(n)], owner, succ]
    v = violation(G, INV)
    if v:
        found += 1; print("FOUND", i, v, G, flush=True)
        if found >= 2: break
print("searched", i + 1, "found", found)
