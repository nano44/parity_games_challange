#!/usr/bin/env python3
"""debug: at original state t, print plays (with priorities) from given original nodes, original vs genome. Usage: fdbg.py n t node..."""
import sys, os
sys.path.insert(0, os.path.join(os.environ["WT3"], "experiments/new/box191"))
import idealcyc, gamma3, pg
from si import Engine
from fried import game, howard
from comp import compile_
n, t = int(sys.argv[1]), int(sys.argv[2]); V = game(n); nm = {v[0]: v[4] for v in V}; byname = {v[4]: v[0] for v in V}
T, traj = howard(V); g = pg.Game([v[1] for v in V], [v[2] for v in V], [v[3] for v in V]); E = Engine(g)
vs, sb = E.evaluate(traj[t])
def play(v, nx):
    out = []; seen = set()
    while v not in seen: seen.add(v); out.append(v); v = nx(v)
    return out, v
for q in sys.argv[3:]:
    p, last = play(byname[q], lambda v: traj[t][v] if g.owner[v] == 0 else sb[v])
    print("ORIG", q, [f"{nm[v]}:{g.prio[v]}" for v in p], "->", nm[last])
G, ix = compile_(n); h, s0, movers, inv = idealcyc.build(G); E2 = Engine(h); st = idealcyc.run(G); _, _, _, VV = gamma3.build(G, set())
rv = {v: k for k, v in VV.items()}; iname = {i: s for s, i in ix.items()}
cur = list(s0)
for x in range(G["N"]): cur[movers[x]] = VV[("g", (x, st[t][x]))]
vs2, sb2 = E2.evaluate(tuple(cur))
def nm2(v):
    k = rv[v]
    if k[0] == "x": return iname[k[1]]
    if isinstance(k, tuple) and len(k) == 2 and isinstance(k[1], tuple): return f"{k[0]}:{iname[k[1][0]]}.{k[1][1]}"
    return str(k)
for q in sys.argv[3:]:
    p, last = play(movers[ix["h_" + q]], lambda v: cur[v] if h.owner[v] == 0 else sb2[v])
    print("GEN ", q, [f"{nm2(v)}:{h.prio[v]}" for v in p if h.prio[v] > 1], "->", nm2(last))
