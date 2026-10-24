#!/usr/bin/env python3
"""Box 24, o-cyclic C^1O: search for the smallest game (canonical N5) where the o-acyclic chain breaks, i.e. a PURE transition
(σ|X and τ unchanged; X = vertices with no path to o) from a state with θ ◁ w (L1 fails). Usage: cycsearch.py N n seed"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from h1 import wvals
from pureY import split
def l1fail(g, st):
    n = g.n; o = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]; E = Engine(g)
    Y = split(g, o); X = [v for v in range(n) if v not in Y and g.owner[v] == 0]
    for k in range(len(st) - 1):
        if all(st[k + 1][0][v] == st[k][0][v] for v in X) and st[k + 1][1] == st[k][1]:
            s, t = st[k]; Xi, _ = E.evaluate(s); _, W = wvals(g, s, t)
            if E.key(Xi[o]) < E.key(W[o]): return k
    return None
if __name__ == "__main__":
    N, n, seed = map(int, sys.argv[1:]); rng = random.Random(seed); cyc = 0
    for i in range(N):
        owner = [0] * n; o = rng.randrange(n); owner[o] = 1
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3))))) for _ in range(n)]
        succ[o] = sorted(set(rng.sample(range(n), rng.choice((2, 3)))))
        g = pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ); Ys = split(g, o)
        if not any(w in Ys for w in succ[o]): continue
        cyc += 1; st, _ = trace(g, check=False); k = l1fail(g, st)
        if k is not None:
            print("FOUND n", n, "at state", k, "prio", g.prio, "owner", g.owner, "succ", g.succ, flush=True); break
    print("o-cyclic games searched", cyc)
