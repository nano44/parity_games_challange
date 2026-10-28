#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA: for every pair {y, z} of one class, an Even reader e with edges {y, z} (start y): is the run SAME, and how
many Even switches does e make? Prints the best pairs. Usage: pairs.py BASE.pg BASE.start OUT_PREFIX"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import dress
from dress import load, rows, phases, readstart
base, bst, out = sys.argv[1:4]
g = load(base); E, R = rows(g, readstart(bst)); P = max(phases(R), key=lambda p: p[1] - p[0]); A = R[P[0]]
res = []; diff = 0
for y in range(g.n):
    for z in range(y + 1, g.n):
        if A["vs"][y][0] != A["vs"][z][0]: continue
        dress.build(base, bst, out, [f"0:0:{y},{z}:{y}"]); r = dress.compare(base, bst, out + ".pg", out + ".start", quiet=True)
        if not r["same"]: diff += 1; continue
        row = max(r["rows"], key=lambda x: x["length"]); res.append((row["new"][0][3], row["new"][0][2], y, z))
res.sort(reverse=True)
print(f"pairs SAME {len(res)} DIFFERENT {diff} n_dressed {g.n + 1} phase {P}")
print("best (switches, XR, y, z):", res[:10])
