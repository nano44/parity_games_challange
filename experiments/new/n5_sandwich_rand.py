#!/usr/bin/env python3
"""Box 4: the sandwich check of n5_sandwich.py on random games (n5_lock.rgame), best-reward start. Usage: n5_sandwich_rand.py games seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import step, play_val, rgame
from n5 import Engine, dual
games, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); steps = bm = bs = 0
for _ in range(games):
    g = rgame(rng.randint(6, 40), 3, rng); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    while True:
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, f, _, _ = r
        if f and nt == t and ns != s:
            V0 = play_val(E, g, s, t); V1 = play_val(E, g, ns, t); X1 = E.evaluate(tuple(ns))[0]; steps += 1
            bm += sum(E.key(V1[v]) > E.key(V0[v]) for v in range(g.n)); bs += sum(E.key(X1[v]) > E.key(V1[v]) for v in range(g.n))
        s, t = ns, nt
print(f"games={games} seed={seed}: Even-fallback steps {steps}; V increases at {bm} vertex-steps; Xi above V at {bs} vertex-steps")
