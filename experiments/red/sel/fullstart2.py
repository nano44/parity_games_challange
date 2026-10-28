#!/usr/bin/env python3
"""L-RED successor 23: write a FULL start file (every vertex) for GAME.pg: S3 (best-reward, SPEC FIX 1) overridden by the valid entries of
START (entries whose edge is missing in GAME are dropped, as xrclimb.py's vstart does). Usage: fullstart2.py GAME.pg START|S3 OUT.start"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace as T
g = T.pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
E, Ed = T.Engine(g), T.Engine(T.dual(g))
s, t = list(E.initial("best")), list(Ed.initial("best"))
if sys.argv[2] != "S3":
    s0, t0 = T.readstart(sys.argv[2])
    for v, w in s0.items():
        if v < g.n and g.owner[v] == 0 and w in g.succ[v]: s[v] = w
    for v, w in t0.items():
        if v < g.n and g.owner[v] == 1 and w in g.succ[v]: t[v] = w
with open(sys.argv[3], "w") as f:
    f.write("SIGMA0 " + " ".join("%d:%d" % (v, s[v]) for v in range(g.n) if g.owner[v] == 0) + "\n")
    f.write("TAU0 " + " ".join("%d:%d" % (v, t[v]) for v in range(g.n) if g.owner[v] == 1) + "\n")
