#!/usr/bin/env python3
"""Box 4: empirical check of G-N5-TERM-reading.md Lemma B. In every N5 iteration where a side's valuation does not change
(Ξσ' = Ξσ although σ' ≠ σ, or the same for τ on G^d), every switched vertex v must be its own cycle node (Λ(v) = v), with old and
new successor both of cycle node v and empty path set (length-only switch). Random games n5_lock.rgame, equal priorities allowed.
Usage: n5_flatcheck.py games seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import step, rgame
from n5 import pg, Engine, dual
games, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); flat = viol = 0
def check(En, old, new):
    global flat, viol
    xo = En.evaluate(tuple(old))[0]; xn = En.evaluate(tuple(new))[0]
    if old == new or xo != xn: return
    flat += 1
    for v in range(len(old)):
        if old[v] != new[v]:
            a, b = xo[old[v]], xo[new[v]]
            if not (xo[v][0] == v and a[0] == v and b[0] == v and a[1] == 0 and b[1] == 0): viol += 1
for _ in range(games):
    n = rng.randint(4, 30); g = rgame(n, 3, rng)
    if rng.random() < 0.5: g = pg.Game([p // 3 for p in g.prio], g.owner, g.succ)      # many equal priorities
    E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: break
        check(E, s, r[0]); check(Ed, t, r[1]); s, t = r[0], r[1]
print(f"games={games} seed={seed}: flat side-steps {flat}; Lemma B violations {viol}")
