#!/usr/bin/env python3
"""L-SI box 17: hand-readable N5 trace of one vertex V: per state D, tau on D, sigma(V), V's first gate, Xi(V), W(V), the offset
w(P(W V)) - w(P(Xi V)), whether the gates' two values equal those of state 0, and the fallback flag. Usage: trace.py GAME START V"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import wval, lasso
g = load(sys.argv[1]); st = readstart(sys.argv[2]); v = int(sys.argv[3])
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); g0 = None
for k in range(3001):
    vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
    wn = (lambda s, t: (lambda x: s[x] if g.owner[x] == 0 else t[x]))(list(s), tuple(t))
    D = [u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]]
    Wv = wval(E, wn, v); gate = next((x for x in lasso(wn, v)[0] if x in D), None)
    gv = {u: (vs[u], wval(E, wn, u)) for u in D}
    if g0 is None: g0 = gv
    print(k, "D", D, "tau", [t[u] for u in D], "sigma(v)", s[v], "gate", gate, "Xi(v)", vs[v], "W(v)", Wv,
          "offset", E.weight(Wv[1]) - E.weight(vs[v][1]), "gates as at 0", gv == g0, "lambda_Xi", sorted({x[0] for x in vs}),
          "fallback", r[4] if r else "STOP")
    if r is None: break
    s, t = r[0], r[1]
