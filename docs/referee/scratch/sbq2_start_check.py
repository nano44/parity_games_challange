#!/usr/bin/env python3
"""REFEREE s21: sbq2_K8_m16.start gives Odd 242 -> 243, not an edge. Run N5 (rl_engine) from the start with tau(242) repaired to each
successor of 242, and report states, sigma-bar(260) flips and the W-tie W(242) = W(259) count (the box-54 W-rank DEAD's figures).
Usage: sbq2_start_check.py GAME.pg GAME.start"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
g = RE.parse(sys.argv[1]); s = [None] * g.n; t = [None] * g.n
for l in open(sys.argv[2]):
    for p in l.split()[1:]:
        v, w = map(int, p.split(":")); (s if g.owner[v] == 0 else t)[v] = w
for v in range(g.n):
    x = s if g.owner[v] == 0 else t
    if x[v] is None: x[v] = g.succ[v][0]
for rep in g.succ[242]:
    t2 = list(t); t2[242] = rep
    st = RE.run(g, (s, t2))
    nx = lambda q: [q["s"][v] if g.owner[v] == 0 else q["t"][v] for v in range(g.n)]
    ties = sum(1 for q in st if RE.play_value(g, nx(q), 242) == RE.play_value(g, nx(q), 259))
    flips = sum(1 for a, b in zip(st, st[1:]) if a["sb"][260] != b["sb"][260])
    print("tau(242) :=", rep, "states", len(st), "Wtie", ties, "sbflips260", flips)
