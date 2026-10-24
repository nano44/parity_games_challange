#!/usr/bin/env python3
"""Why (h) fails, per transition of the longest joint λ-phase (canonical start, o-cyclic C^1O; L-NEW box25 helpers, unmodified):
SB = o on a cycle of (σ, σ̄); TAU = o on a cycle of (σ, τ); CN = cycle nodes of Ξ(o) and W(o) differ. Also prints the phase's
length, its θ / w changes and its throttled count. Usage: LNEW_BOX25=... nhwhy.py game.pg"""
import sys, os
sys.path.insert(0, os.environ["LNEW_BOX25"])
from common import *
from wdrop_h import oncycle
from collections import Counter
g = load(sys.argv[1]); E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); s, t = start_pair(g, E, Ed, None); rows = []; k = 0
while k < 2000:
    Xi, sb = E.evaluate(tuple(s)); U, _ = Ed.evaluate(tuple(t)); _, W = wvals(g, s, t)
    a, b, c = oncycle(g, s, sb, o), oncycle(g, s, t, o), Xi[o][0] != W[o][0]
    rows.append((((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o])), a, b, c, E.key(Xi[o]), E.key(W[o])))
    r = step(g, E, Ed, s, t)
    if r is None: break
    s, t = list(r[0]), list(r[1]); k += 1
ph = []; st = 0
for i in range(1, len(rows) + 1):
    if i == len(rows) or rows[i][0] != rows[st][0]: ph.append((st, i)); st = i
a, b = max(ph, key=lambda p: p[1] - p[0])
why = Counter("+".join(n for n, f in zip(("SB", "TAU", "CN"), r[1:4]) if f) or "h" for r in rows[a:b])
th = sum(rows[i][4] != rows[i - 1][4] for i in range(a + 1, b)); wc = sum(rows[i][5] != rows[i - 1][5] for i in range(a + 1, b))
print(f"{os.path.basename(sys.argv[1])} n={g.n} iterations={k} phases={len(ph)} longest phase {a}..{b} ({b - a} states): {dict(why)} theta-changes={th} w-changes={wc}")
