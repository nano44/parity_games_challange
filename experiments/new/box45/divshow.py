#!/usr/bin/env python3
"""Box 45: show one DIV instance (premise (Στ)): N5 on G from the given start pair, its first transition, D, G'_E, and the SPEC and
N5^tau steps on G'_E. Usage: divshow.py FILE.pg FILE.start"""
import sys, os, ast
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, Engine, dual
from eprestrict import restrict, step_tau
g = load(sys.argv[1]); L = open(sys.argv[2]).read().split("\n")
s = ast.literal_eval(L[0].split(" ", 1)[1]); t = ast.literal_eval(L[1].split(" ", 1)[1])
E, Ed = Engine(g), Engine(dual(g)); Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
vs, sb = E.evaluate(tuple(s)); vt, _ = Ed.evaluate(tuple(t)); It = sorted(Ed.improving(tuple(t), vt)); Is = sorted(E.improving(tuple(s), vs))
r = step(g, E, Ed, s, t); vs1, sb1 = E.evaluate(tuple(r[0]))
D = [q for q in Q if sb[q] != t[q]]
print("Q", Q, "sbar|Q", [sb[q] for q in Q], "tau|Q", [t[q] for q in Q], "D", D, "Is", Is, "It", It)
print("G step: sigma", s, "->", r[0], "tau", t, "->", r[1], "fb", r[4])
print("in-phase:", list(r[1]) == list(t) and [x[0] for x in vs] == [x[0] for x in vs1], "| sbar|Q after", [sb1[q] for q in Q])
W = Engine(restrict(g, set(), t, t)).evaluate(tuple(s))[0]
print("W == Xi:", list(W) == list(vs), "| Xi(u) per u in D:", [(u, vs[u]) for u in D])
gp = restrict(g, set(D), t, sb); Ep, Edp = Engine(gp), Engine(dual(gp))
print("G'_E succ:", gp.succ, "| Xi' == Xi:", list(Ep.evaluate(tuple(s))[0]) == list(vs), "| sbar' on D:", [(u, Ep.evaluate(tuple(s))[1][u]) for u in D])
rs = step_tau(gp, Ep, Edp, s, t, spec=True); rt = step_tau(gp, Ep, Edp, s, t)
print("SPEC on G'_E: sigma ->", rs[0], "tau ->", rs[1], "fb", rs[2]); print("N5^tau on G'_E: sigma ->", rt[0], "tau ->", rt[1], "fb", rt[2], "moved", rt[3])
