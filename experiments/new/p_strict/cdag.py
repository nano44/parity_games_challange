#!/usr/bin/env python3
"""Box 8: explicit family against (P*) / (P_strict) (R-N5K9 §(2)-(3)). CDAG_n: one-player parity game, all vertices Even (⊕);
vertex 0: priority 0, self-loop (the sink); vertex v = 1..n: priority 2(n+1-v), edges to every u < v. ⊖ has no vertices.
Chain gen(n) of single switches from σ0 = (all -> 0):  gen(1) = [];  gen(m) = [(m, m-1)] + gen(m-1) with every step (m-1, u)
replaced by (m, u), (m-1, u), (m, m-1).  Length 2^n - n - 1.  This script CHECKS every step with L-SI's VJ00 engine
(experiments/si/si.py, read-only): the switch is in Engine.improving(σ) (VJ00 §4.4 improvement), and Ω strictly increases
(Ω_{σ'} ≥ Ω_σ everywhere, > somewhere; compared by Engine.key). Also writes the game in pgsolver format.
Usage: cdag.py n [game.pg]"""
import sys, os, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "si")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
import pg
from si import Engine
def game(n):
    return pg.Game([0] + [2 * (n + 1 - v) for v in range(1, n + 1)], [0] * (n + 1), [[0]] + [list(range(v)) for v in range(1, n + 1)])
def gen(m):
    if m <= 1: return []
    out = [(m, m - 1)]
    for x, u in gen(m - 1):
        out += [(m, u), (m - 1, u), (m, m - 1)] if x == m - 1 else [(x, u)]
    return out
n = int(sys.argv[1]); g = game(n); E = Engine(g); ch = gen(n)
if len(sys.argv) > 2:
    pg.write(g, sys.argv[2]); print("wrote", sys.argv[2], "sha1", hashlib.sha1(open(sys.argv[2], 'rb').read()).hexdigest())
s = [0] * (n + 1); val, _ = E.evaluate(tuple(s)); strict = 0
for k, (x, u) in enumerate(ch):
    imp = set(E.improving(tuple(s), val))
    assert (x, u) in imp, f"step {k}: ({x},{u}) not improving"
    s[x] = u; nv, _ = E.evaluate(tuple(s))
    ge = all(E.key(nv[v]) >= E.key(val[v]) for v in range(n + 1)); gt = any(E.key(nv[v]) > E.key(val[v]) for v in range(n + 1))
    assert ge and gt, f"step {k}: not an Ω-strict improvement"
    strict += 1; val = nv
print(f"n={n} vertices={n+1} edges={sum(len(x) for x in g.succ)} chain={len(ch)} (2^n-n-1={2**n-n-1}) all steps VJ00-improving and Ω-strict={strict}")
print("final strategy optimal (no improvement left):", not E.improving(tuple(s), val))
