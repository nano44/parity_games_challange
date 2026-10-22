#!/usr/bin/env python3
"""Box 5: is N5's step a superset of SSI's (every vertex SSI switches, N5 switches too)? Checked at every state of N5's run and of
SSI's run on random games (n5_lock.rgame); counts violations of each kind and saves the first witness.
Usage: n5_superset.py games seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from n5_lock import step, rgame
from n5 import pg, Engine, dual
games, seed = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(seed); states = 0; viol = {"E_keeps": 0, "E_other": 0, "O_keeps": 0, "O_other": 0}; wit = None
for gi in range(games):
    g = rgame(rng.randint(4, 24), 3, rng); E, Ed = Engine(g), Engine(dual(g))
    for path in ("n5", "ssi"):
        s, t = list(E.initial("best")), list(Ed.initial("best"))
        for _ in range(500):
            vs, sbar = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs); vt, tbar = Ed.evaluate(tuple(t)); It = Ed.improving(tuple(t), vt)
            if not Is and not It: break
            ns, nt = list(s), list(t)
            for v, w in Is:
                if tbar[v] == w: ns[v] = w
            for v, w in It:
                if sbar[v] == w: nt[v] = w
            r = step(g, E, Ed, s, t); states += 1
            for v in range(g.n):
                if g.owner[v] == 0 and ns[v] != s[v] and r[0][v] != ns[v]:
                    k = "E_keeps" if r[0][v] == s[v] else "E_other"; viol[k] += 1; wit = wit or (g.prio, g.owner, g.succ, path, s, t, v)
                if g.owner[v] == 1 and nt[v] != t[v] and r[1][v] != nt[v]:
                    k = "O_keeps" if r[1][v] == t[v] else "O_other"; viol[k] += 1; wit = wit or (g.prio, g.owner, g.succ, path, s, t, v)
            s, t = (r[0], r[1]) if path == "n5" else (ns, nt)
print(f"games={games} seed={seed}: states {states}; SSI switches that N5 does not make: {viol}")
print("first witness:", wit)
