#!/usr/bin/env python3
r"""REFEREE-2 successor 23 (Opus 5.5, D15): random test of my Lemma OWN (not in the packet): if Even strategies s, s' differ only on a set X
of Even vertices and every x in X is its own Xi-cycle node under s AND under s', then Xi_s = Xi_s' (SPEC S1, si.py Engine, read-only).
No improvement hypothesis. Control X_ONE: drop "own under s'" (only under s): Xi differs somewhere (expected > 0).
Usage: own_check.py N nmin nmax seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
from si import Engine
N, nmin, nmax, seed = map(int, sys.argv[1:5]); rng = random.Random(seed)
c = {"pairs": 0, "OWN_viol": 0, "X_ONE_differs": 0, "X_ONE": 0}
for i in range(N):
    g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO"); n = g.n; E = Engine(g)
    Even = [v for v in range(n) if g.owner[v] == 0 and len(g.succ[v]) > 1]
    if not Even: continue
    for _ in range(8):
        s = [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(n)]
        xs, _ = E.evaluate(tuple(s))
        own = [v for v in Even if xs[v][0] == v]
        if not own: continue
        X = rng.sample(own, rng.randint(1, len(own)))
        s2 = list(s)
        for x in X: s2[x] = rng.choice(g.succ[x])
        if s2 == s: continue
        xs2, _ = E.evaluate(tuple(s2))
        if all(xs2[x][0] == x for x in X):
            c["pairs"] += 1
            if list(xs2) != list(xs):
                c["OWN_viol"] += 1
                if c["OWN_viol"] <= 3: print("VIOLATION", g.prio, g.owner, g.succ, s, s2, X)
        else:
            c["X_ONE"] += 1
            if list(xs2) != list(xs): c["X_ONE_differs"] += 1
print(c); print("RESULT", "PASS" if c["OWN_viol"] == 0 else "FAIL")
