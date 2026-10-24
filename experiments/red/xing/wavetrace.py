#!/usr/bin/env python3
"""Per transition of the longest joint λ-phase: θ-change level (VJ rank of the top of P(θ_k) Δ P(θ_{k+1}); 'L' = length only; '.' none),
R entries / leaves (R = vertices whose (σ, τ)-play reaches o, o excluded: L-NEW fbre.reach_o), fallback flag, and w change.
Usage: LNEW_BOX25=... wavetrace.py game.pg"""
import sys, os
sys.path.insert(0, os.environ["LNEW_BOX25"])
from common import *
from thtrace import Rset
from h1 import wvals
g = load(sys.argv[1]); E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); rows = []; k = 0
while k < 2000:
    Xi, _ = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
    rows.append(dict(key=(tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), th=Xi[o], w=E.key(W[o]), R=frozenset(v for v in Rset(g, s, t, o) if v != o), fb=0))
    r = step(g, E, Ed, s, t)
    if r is None: break
    rows[-1]["fb"] = int(bool(r[4])); s, t = list(r[0]), list(r[1]); k += 1
ph = []; a = 0
for i in range(1, len(rows) + 1):
    if i == len(rows) or rows[i]["key"] != rows[a]["key"]: ph.append((a, i)); a = i
a, b = max(ph, key=lambda p: p[1] - p[0]); X = 0; out = []
for j in range(a, b - 1):
    x, y = rows[j]["th"], rows[j + 1]["th"]
    lv = "." if x == y else ("cyc" if x[0] != y[0] else (str((x[1] ^ y[1]).bit_length() - 1) if x[1] != y[1] else "L"))
    en, lvv = len(rows[j + 1]["R"] - rows[j]["R"]), len(rows[j]["R"] - rows[j + 1]["R"]); X += (en + lvv) > 0
    out.append(f"{j}:{lv}{'+' + str(en) if en else ''}{'-' + str(lvv) if lvv else ''}{'F' if rows[j]['fb'] else ''}{'W' if rows[j]['w'] != rows[j + 1]['w'] else ''}")
print(f"{os.path.basename(sys.argv[1])} n={g.n} phase {a}..{b - 1} transitions={b - 1 - a} X={X}")
print(" ".join(out))
