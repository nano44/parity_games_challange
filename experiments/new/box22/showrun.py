#!/usr/bin/env python3
"""Box 22: print a canonical N5 run on a C^1O game: per state the multi-choice Even edges, τ(o), σ̄(o), θ = Ξ(o), w = W(o),
R (o's reach set), Ξ and W (cycle node, signed path weight, length) per vertex, Iσ, and whether the step was a fallback.
Usage: showrun.py game.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from h1 import wvals
from lemmaG import reach
g = load(sys.argv[1]); E, Ed = Engine(g), Engine(dual(g)); n = g.n
o = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1][0]
print("o =", o, "succ", g.succ[o], "prio", g.prio)
s, t = start_pair(g, E, Ed); k = 0
f = lambda val: (val[0], E.weight(val[1]), val[2])
while True:
    X, sb = E.evaluate(tuple(s)); Eg, W = wvals(g, s, t); I = E.improving(tuple(s), X)
    print(f"state {k}: σ {[(v, s[v]) for v in range(n) if g.owner[v]==0 and len(g.succ[v])>1]} τ(o)={t[o]} σ̄(o)={sb[o]} θ={f(X[o])} w={f(W[o])} R={sorted(reach(g, s, o))}")
    print("   Ξ:", {v: f(X[v]) for v in range(n)}); print("   W:", {v: f(W[v]) for v in range(n)}); print("   Iσ:", I)
    r = step(g, E, Ed, s, t)
    if r is None: break
    print("   -> fallback" if r[4] else "   -> arena step", [(v, s[v], r[0][v]) for v in range(n) if s[v] != r[0][v]], "Odd:", [(v, t[v], r[1][v]) for v in range(n) if t[v] != r[1][v]])
    s, t = r[0], r[1]; k += 1
