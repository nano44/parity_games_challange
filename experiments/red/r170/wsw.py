#!/usr/bin/env python3
"""R170: per TWO-FIX window (length >= MINL): switches per Even vertex (max, distinct switched vertices), returns (a vertex switching
back to a successor it held earlier in the window), steps with |Is| = 1, and fallbacks. Usage: wsw.py G.pg START|-"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from freeze import run, windows, load, readstart, start_pair, Engine, dual
from n5x import step
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
s, t = start_pair(g, Engine(g), Engine(dual(g)), st); S, T, F, E = run(g, s, t); W, SB = windows(g, S, T, E)
minl = int(os.environ.get("MINL", "4"))
for a, b in W:
    if b - a < minl: continue
    cnt, ret, held = {}, 0, {}
    for j in range(a, b):
        for v in range(g.n):
            if g.owner[v] == 0:
                held.setdefault(v, {S[a][v]})
                if S[j + 1][v] != S[j][v]:
                    cnt[v] = cnt.get(v, 0) + 1; ret += S[j + 1][v] in held[v]; held[v].add(S[j + 1][v])
    one = sum(1 for j in range(a, b) if len(E.improving(S[j], E.evaluate(S[j])[0])) == 1)
    print(f"WSW {os.path.basename(sys.argv[1])} n {g.n} [{a},{b}] L {b-a} fb {sum(F[a+1:b+1])} switched {len(cnt)} maxsw {max(cnt.values())} total {sum(cnt.values())} returns {ret} Is1 {one}")
