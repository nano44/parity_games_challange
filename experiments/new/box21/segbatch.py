#!/usr/bin/env python3
"""Box 21: random games, N5 from (sigma_0, tau*) (frozen, tau* = final tau of the plain run). Records per run: the longest
sigma-bar-segment ∩ joint-λ-phase (iterations), the number of sigma-bar changes, and checks segment <= n - 1.
Usage: segbatch.py N nmin nmax seed [oneodd]"""
import sys, random
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))  # box21 -I: find sibling modules
from n5x import *
N, a, b, seed = map(int, sys.argv[1:5]); one = len(sys.argv) > 5; rng = random.Random(seed)
worst = (-10 ** 9, None); maxbr = (0, None); viol = 0
for i in range(N):
    n = rng.randint(a, b)
    owner = [rng.randrange(2) for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
    if one:
        owner = [0] * n; o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3, 4)))))
    g = pg.Game([rng.randrange(n) for _ in range(n)], owner, succ); E, Ed = Engine(g), Engine(dual(g))
    st, _ = trace(g, check=False); s0, ts = st[0][0], st[-1][1]
    fs, _ = trace(g, ({v: s0[v] for v in range(n) if owner[v] == 0}, {v: ts[v] for v in range(n) if owner[v] == 1}), check=False)
    key = []
    for s, t in fs:
        X, sb = E.evaluate(s); key.append((tuple(sb), tuple(x[0] for x in X)))
    br = sum(key[k][0] != key[k - 1][0] for k in range(1, len(key)))
    best = cur = 0
    for k in range(1, len(fs)):
        cur = cur + 1 if k > 1 and key[k - 1] == key[k - 2] else 1; best = max(best, cur)
    if best - (n - 1) > worst[0]: worst = (best - (n - 1), (n, best, i))
    if best > n - 1: viol += 1
    if br > maxbr[0]: maxbr = (br, (n, i, len(fs) - 1))
print(f"runs {N}: longest segment minus (n-1), worst = {worst}; segments > n-1: {viol}; most sigma-bar changes = {maxbr}")
