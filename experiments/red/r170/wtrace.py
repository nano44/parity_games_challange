#!/usr/bin/env python3
"""R170: trace an N5 run: per transition the switched Even edges, |Is|, |It|, fallback flag, whether tau / sbar moved. Usage: wtrace.py G.pg START|-"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); n = g.n; k = 0
sb = E.evaluate(tuple(s))[1]
while True:
    r = step(g, E, Ed, s, t)
    if r is None: break
    ns, nt, Is, It, fb, vs, vt = r; nsb = E.evaluate(tuple(ns))[1]
    sw = [(v, s[v], ns[v]) for v in range(n) if g.owner[v] == 0 and ns[v] != s[v]]
    tm = [(v, t[v], nt[v]) for v in range(n) if g.owner[v] == 1 and nt[v] != t[v]]
    bm = [(v, sb[v], nsb[v]) for v in range(n) if g.owner[v] == 1 and nsb[v] != sb[v]]
    print(f"{k}->{k+1} fb {fb} |Is| {len(Is)} |It| {len(It)} sw {sw} tau {tm} sbar {bm}")
    s, t, sb = ns, nt, nsb; k += 1
