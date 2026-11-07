#!/usr/bin/env python3
"""L-RED R183: per N5 step on a realized IDEAL game: #gates with tau != W-face, #gates with sigma-bar != Xi-face, sigma moves,
fallback. Usage: realdiag.py G.pg G.start"""
import sys, os
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r170"), os.path.join(H, "..", "..", "new", "box21")]
from n5x import load, readstart, start_pair, Engine, dual
from freeze import run
g = load(sys.argv[1]); st = readstart(sys.argv[2]); s, t = start_pair(g, Engine(g), Engine(dual(g)), st)
S, T, F, E = run(g, s, t); n = g.n
gates = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) == 2]
wf = {v: t[v] for v in gates}; xf = {v: [w for w in g.succ[v] if w != t[v]][0] for v in gates}
for j in range(len(S)):
    vs, sb = E.evaluate(S[j])
    print(j, "fb", F[j], "tau!=W", sum(T[j][v] != wf[v] for v in gates), "sbar!=X", sum(sb[v] != xf[v] for v in gates),
          "sbar=W", sum(sb[v] == wf[v] for v in gates), "moves", sum(S[j][v] != S[j - 1][v] for v in range(n) if g.owner[v] == 0) if j else 0)
