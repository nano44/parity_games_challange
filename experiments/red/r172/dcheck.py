#!/usr/bin/env python3
"""R172: min / max |D_j| over the states of the longest TWO-FIX window (D_j := vertices whose (sigma_j, sbar)-play visits O, O := Odd
vertices with sbar != tau; L-NEW box 122). Usage: dcheck.py G.pg START"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "r170"))
from freeze import run, windows, load, readstart, start_pair, Engine, dual
g = load(sys.argv[1]); s, t = start_pair(g, Engine(g), Engine(dual(g)), readstart(sys.argv[2])); S, T, F, E = run(g, s, t); W, SB = windows(g, S, T, E)
a, b = max(W, key=lambda w: w[1] - w[0]); O = {v for v in range(g.n) if g.owner[v] == 1 and SB[a][v] != T[a][v]}
def D(sig):
    nxt = [sig[v] if g.owner[v] == 0 else SB[a][v] for v in range(g.n)]; out = 0
    for x in range(g.n):
        seen, y = set(), x
        while y not in seen:
            if y in O: out += 1; break
            seen.add(y); y = nxt[y]
    return out
ds = [D(S[j]) for j in range(a, b + 1)]
print(f"DCHECK window [{a}, {b}] |O| {len(O)} min|D| {min(ds)} max|D| {max(ds)} n {g.n}")
