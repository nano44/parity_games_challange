#!/usr/bin/env python3
"""REFEREE-2 succ. 20: G^d's order is the exact reverse of G's on ALL valuations (any cycle nodes), si.py keys, random games.
Fact B1 (same cycle node, P != P') is the special case. Prints pairs checked and violations."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
rng = random.Random(int(sys.argv[2]) if len(sys.argv) > 2 else 7); pairs = bad = eq = 0
for _ in range(int(sys.argv[1]) if len(sys.argv) > 1 else 300):
    g = DC.rand_game(rng, rng.randint(2, 30), "kO"); E, Ed = DC.Engine(g), DC.Engine(DC.dual(g)); n = g.n
    def rv():
        c = rng.randrange(n); m = sum(E.bit[u] for u in range(n) if E.rank[u] > E.rank[c] and rng.random() < 0.4)
        return (c, m, rng.randrange(2 * n))
    for _ in range(500):
        X, Y = rv(), rv(); pairs += 1
        if E.key(X) == E.key(Y): eq += 1; bad += Ed.key(X) != Ed.key(Y); continue
        bad += (Ed.key(X) < Ed.key(Y)) != (E.key(Y) < E.key(X))
print(f"pairs {pairs} equal-keys {eq} violations {bad}")
