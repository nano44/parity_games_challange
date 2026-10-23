#!/usr/bin/env python3
"""N8d §0b C1 check: kl_single.py (kl.py priority COMPRESSION) vs L-COMP kl2.py (p+2, no compression), R2 seeds 1-3, pivot counts
and regions per instance. Usage: c1diff.py RNGSEED gap|rand COUNT"""
import sys, random
import os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
sys.path[:0] = [R + "/new/kl", R + "/n8d-second", R + "/harness"]
import pg, kl, kl_single, kl2
def mk(n, prio, owner, succ): return pg.Game(prio, owner, succ, [None]*n)
def run(g, seed):
    a = kl_single.solve(g, "r2", seed); w2, s2, pp, pd = kl2.solve(g, "r2", seed)
    return (a["it"], a["it_dual"]), (pp, pd), a["win"] == w2
rng = random.Random(int(sys.argv[1])); diffs = 0; tot = 0; mode = sys.argv[2]
for t in range(int(sys.argv[3])):
    n = rng.randint(2, 7)
    if mode == "gap":     # one odd priority class of n-1 nodes plus one node with a far priority (compression differs from p+2)
        P = rng.choice([1, 3]); prio = [P] * n; prio[rng.randrange(n)] = rng.choice([P + 3, P + 5, P + 7, P + 4, P + 6])
    else:                 # random priorities with gaps
        prio = [rng.choice([0, 1, 3, 4, 7, 8, 11]) for _ in range(n)]
    owner = [rng.randint(0, 1) for _ in range(n)]
    succ = [rng.sample(range(n), rng.randint(1, min(3, n))) for _ in range(n)]
    g = mk(n, prio, owner, succ)
    for s in (1, 2, 3):
        a, b, ok = run(g, s); tot += 1
        if a != b or not ok:
            diffs += 1
            if diffs <= 5: print("DIFF", a, b, ok, n, prio, owner, succ, "seed", s)
print(mode, "runs", tot, "diffs", diffs)
