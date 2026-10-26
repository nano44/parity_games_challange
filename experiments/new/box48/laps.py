#!/usr/bin/env python3
"""Box 48 DATA: for the longest phase of one run, print per state: config id, D, fallback flag, and the Even vertices whose sigma differs
from the state with the same config id at its first occurrence (lap comparison). Usage: laps.py GAME.pg START"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from multi import load, step, start_pair, Engine, dual
from n5x import readstart
g = load(sys.argv[1]); st = readstart(sys.argv[2]); E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); rows = []
Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
while True:
    vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
    rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), s=tuple(s), sb=tuple(sb), fb=r[4] if r else 0))
    if r is None: break
    s, t = r[0], r[1]
ph = []; i = 0
while i < len(rows):
    j = i
    while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
    ph.append((i, j)); i = j + 1
a, b = max(ph, key=lambda p: p[1] - p[0]); ids = {}; first = {}
print("Q", Q, "phase", a, b)
for k in range(a, b + 1):
    c = tuple(rows[k]["sb"][q] for q in Q); cid = ids.setdefault(c, len(ids))
    D = [q for q in Q if rows[k]["sb"][q] != rows[k]["t"][q]]
    diff = ""
    if cid in first:
        k0 = first[cid]; diff = "vs " + str(k0) + ": " + " ".join(f"{v}:{rows[k0]['s'][v]}->{rows[k]['s'][v]}" for v in range(g.n)
                                                       if g.owner[v] == 0 and rows[k0]["s"][v] != rows[k]["s"][v])
    else: first[cid] = k
    print(k, "c", cid, "sb|Q", c, "D", D, "FB" if rows[k]["fb"] else "", diff)
