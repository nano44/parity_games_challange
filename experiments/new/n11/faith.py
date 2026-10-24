#!/usr/bin/env python3
"""N11 condition 2 (faithfulness): on random games, (a) n5ht.run(ht=False) traces equal N5's (box21/n5x.trace, itself asserted equal
to n5.run); (b) every N5-HT run with 0 conflicts in every iteration has a trace equal to N5's. Usage: faith.py N nmax seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
import n5ht
from n5x import trace, pg
N, nmax, seed = map(int, sys.argv[1:]); rng = random.Random(seed); a = b = bconf = 0
for _ in range(N):
    n = rng.randint(3, nmax)
    g = pg.Game([rng.randrange(n) for _ in range(n)], [rng.randrange(2) for _ in range(n)], [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)])
    ref, _ = trace(g, check=True)
    it0, fb0, c0, _, _, s0 = n5ht.run(g, ht=False, trace=True); assert s0 == ref, "ht=False differs from N5"; a += 1
    it1, fb1, c1, _, _, s1 = n5ht.run(g, ht=True, trace=True)
    if c1 == 0: assert s1 == ref, "0-conflict N5-HT run differs from N5"; b += 1
    else: bconf += 1
print(f"(a) {a} runs: ht=False == N5 trace; (b) {b} zero-conflict N5-HT runs == N5 trace; {bconf} runs had conflicts")
