#!/usr/bin/env python3
"""Side check (not part of the claim): is (p,d)-peelability independent of the admissible d?  Lemma 0 of TA1-proof.md
gives d -> d+2; the converse is 'not needed'.  Compares PA** computed at d_p against d_p + 2 and d_p + 4 on random games."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2lib import *
n, K, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
rnd = random.Random(seed); diff = 0
for _ in range(K):
    g = random_game(rnd, n, n, [1, 2, 3])
    WE, WO = zielonka(g); ok = make_peelable(g)
    a = ok(frozenset(WE), d_p(g, 0), 0) and ok(frozenset(WO), d_p(g, 1), 1)
    b = ok(frozenset(WE), d_p(g, 0) + 2, 0) and ok(frozenset(WO), d_p(g, 1) + 2, 1)
    c = ok(frozenset(WE), d_p(g, 0) + 4, 0) and ok(frozenset(WO), d_p(g, 1) + 4, 1)
    if not (a == b == c):
        diff += 1; print("differs:", g.oneline(), a, b, c)
print(f"n={n} K={K} seed={seed}: PA** at d_p vs d_p+2 vs d_p+4 differs on {diff} games")
