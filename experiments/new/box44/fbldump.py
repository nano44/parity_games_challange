#!/usr/bin/env python3
"""Box 44 DATA: at every S4c fallback k -> k+1 inside a phase with (hD) at k, list the gate edges (x, z) with x in R_D, with
terminals, W-improvement, (h3D), M_D, coarse equality, and S4c's choice for x. Usage: fbldump.py FILE.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, HERE)
from multi import pg
from n5x import load, step, start_pair, Engine, dual
from f1d import hD
from crd import term, coarse
g = load(sys.argv[1]); E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); k = 0; prev = None
while True:
    vs, sb = E.evaluate(tuple(s)); D = frozenset(u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]); U = term(g, s, t, D)
    gt = pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)])
    Eg = Engine(gt); W, _ = Eg.evaluate(tuple(s[v] if g.owner[v] == 0 else -1 for v in range(g.n)))
    r = step(g, E, Ed, s, t)
    if r is None: break
    lam = tuple(x[0] for x in vs)
    if r[4] and hD(g, s, t, sb, D):
        vs2, _ = E.evaluate(tuple(r[0]))
        if tuple(x[0] for x in vs2) == lam and tuple(r[1]) == tuple(t):
            h3 = all(vs[u][0] == W[u][0] for u in D); M = max([(vs[u][1] ^ W[u][1]).bit_length() - 1 for u in D] or [-1])
            for x, z in r[2]:
                if U[x] is None: continue
                print(f"k {k} D {sorted(D)} h3 {h3} M_D {M} edge ({x},{z}) sigma(x) {s[x]} u(x) {U[x]} u(z) {U[z]} "
                      f"Wimp {Eg.key(W[z]) > Eg.key(W[s[x]])} Xi z {vs[z]} Xi sx {vs[s[x]]} W z {W[z]} W sx {W[s[x]]} new {r[0][x]}")
    s, t = r[0], r[1]; k += 1
