#!/usr/bin/env python3
"""Box 44 DATA: list the Delta-RT disagreements of crd.py (gate edges inside R_D, not W-improving, at states with (hD), (h3D),
|D| >= 2): state index k, fallback flag of k -> k+1, D_k, edge (x, z), terminals u(sigma_k x), u(z), M_D, and whether S4a/S4c
switched x at k -> k+1 and to what. Usage: rtdump.py FILE.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import pg
from n5x import load, step, start_pair, Engine, dual
from f1d import hD
from crd import term, coarse
g = load(sys.argv[1]); E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); k = 0
while True:
    vs, sb = E.evaluate(tuple(s)); D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]); U = term(g, s, t, D)
    gt = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)])
    Eg = Engine(gt); W, _ = Eg.evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
    r = step(g, E, Ed, s, t)
    if r is None: break
    if hD(g, s, t, sb, D) and all(vs[u][0] == W[u][0] for u in D) and len(D) >= 2:
        M = max((vs[u][1] ^ W[u][1]).bit_length() - 1 for u in D)
        for x, z in r[2]:
            if U[x] is not None and U[z] is not None and Eg.key(W[z]) <= Eg.key(W[s[x]]):
                print(f"k {k} fb {r[4]} D {sorted(D)} M_D {M} edge ({x},{z}) u(sx) {U[s[x]]} u(z) {U[z]} coarse-equal "
                      f"{coarse(vs[z], M) == coarse(vs[s[x]], M)} new sigma(x) {r[0][x]}")
    s, t = r[0], r[1]; k += 1
