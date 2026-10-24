#!/usr/bin/env python3
"""Box 27: for the vertex with the most crossings in one (θ, w)-stretch, print per transition: side, its route value (if R) or
o-free value (if F) as rank-free sets, the switch made, and which vertices crossed. Usage: xtrace.py game.pg"""
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from reentry import path
from collections import Counter
g = load(sys.argv[1]); st, _ = trace(g); E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g)
rows = []
for s, t in st:
    Xi, sb = E.evaluate(s); U, _ = Ed.evaluate(t); _, W = wvals(g, s, t)
    h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
    rows.append(dict(s=s, t=t, key=((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o])), h=h, R=Rset(g, s, t, o), Xi=Xi, W=W, th=vset(E, Xi[o]), w=vset(E, W[o])))
per = Counter()
for k in range(len(rows) - 1):
    if rows[k]["key"] == rows[k + 1]["key"]:
        for x in rows[k]["R"] ^ rows[k + 1]["R"]: per[x] += 1
x = max(per, key=per.get); print("vertex", x, "crossings", per[x], "prio", g.prio[x], "succ", g.succ[x])
print("θ", rows[1]["th"], "w", rows[1]["w"])
for k, r in enumerate(rows):
    side = "R" if x in r["R"] else "F"
    v = vset(E, r["Xi"][x]); cr = sorted(r["R"] ^ rows[k + 1]["R"]) if k + 1 < len(rows) else []
    print(f"{k:2d} {side} σ(x)={r['s'][x]} Ξ(x)=({v[0]},{sorted(v[1])},{v[2]}) h={r['h']} crossing-now={cr}")
