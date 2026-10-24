#!/usr/bin/env python3
"""Box 25 helpers (o-cyclic C^1O). Read-only use of box21/n5x.py, box21/h1.py, box22/pureY.py, si.py."""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box21", "../box22"): sys.path.insert(0, os.path.join(HERE, p))
from n5x import *            # load, trace, step, Engine, pg, dual
from h1 import wvals
from pureY import split
from si import subgame

def odd_choice(g):
    return [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]

def vset(E, val):
    """Engine valuation -> rank-free form (cycle node, frozenset of path vertices, length)."""
    w, mask, ln = val; inv = {E.rank[v]: v for v in range(E.n)}
    return (w, frozenset(inv[r] for r in range(E.n) if mask >> r & 1), ln)

def opt_one_player(h):
    """Optimal valuation of a one-player (Even) game h: Even's best counterstrategy on the dual, then evaluate."""
    Ed = Engine(dual(h)); _, best = Ed.evaluate(tuple(-1 if h.owner[v] == 0 else h.succ[v][0] for v in range(h.n)))
    E = Engine(h); s = tuple(best[v] if h.owner[v] == 0 else -1 for v in range(h.n)); val, _ = E.evaluate(s)
    return E, val

def rand_c1o(rng, lo, hi, cyclic=True, forced=0.15):
    """Random C^1O game; with cyclic=True keep only o-cyclic ones (some exit reaches o). Returns None if rejected."""
    n = rng.randint(lo, hi); owner = [0] * n; o = rng.randrange(n); owner[o] = 1
    for v in range(n):
        if v != o and rng.random() < forced: owner[v] = 1
    succ = [sorted(set(rng.sample(range(n), min(n, rng.choice((1, 2, 2, 3)))))) for _ in range(n)]
    for v in range(n):
        if owner[v] == 1 and v != o: succ[v] = succ[v][:1]
    succ[o] = sorted(set(rng.sample(range(n), min(n, rng.choice((2, 3, 4))))))
    if len(succ[o]) < 2: return None
    g = pg.Game([rng.randrange(n + 3) for _ in range(n)], owner, succ)
    Y = split(g, o)
    if cyclic != any(w in Y for w in succ[o]): return None
    return g
