#!/usr/bin/env python3
"""Box 21: is W = V_{sigma, tau} (play values against the frozen tau) monotone along frozen-tau N5 runs, including S4c fallback
steps? Random games, runs from (sigma_0, tau*). Usage: wmono.py NGAMES nmin nmax seed"""
import sys, random
from n5x import *
from h1 import wvals
rng = random.Random(int(sys.argv[4])); N, a, b = map(int, sys.argv[1:4]); dec = {"arena": 0, "fallback": 0}; steps = {"arena": 0, "fallback": 0}; ex = None
for _ in range(N):
    n = rng.randint(a, b)
    G = pg.Game([rng.randrange(n) for _ in range(n)], [rng.randrange(2) for _ in range(n)], [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)])
    E, Ed = Engine(G), Engine(dual(G))
    states, _ = trace(G, check=False); s0, ts = states[0][0], states[-1][1]
    s = list(s0); t = list(ts)
    while True:
        r = step(G, E, Ed, s, t)
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r; assert nt == t
        Eg, W = wvals(G, s, t); _, W2 = wvals(G, ns, t); kind = "fallback" if fb else "arena"; steps[kind] += 1
        if any(Eg.key(W2[v]) < Eg.key(W[v]) for v in range(n)):
            dec[kind] += 1
            if ex is None: ex = (G.prio, G.owner, G.succ, s, t, kind)
        s = ns
print("steps", steps, "steps where W decreases somewhere", dec); print("example", ex)
