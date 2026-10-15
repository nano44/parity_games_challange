#!/usr/bin/env python3
"""G11 check: HKP Thm 4 (layered fatal attractors are winning). HKP's proof (tex:1067-1125) defines the strategy
'select the successor with minimal rank r(v) = (d,i)'. Instance (min-parity colours, p = 0): w colour 0 in X; v, u colour 1,
both owned by player 0, v -> {w, u}, u -> {w, v}, w -> {v}. Layer 0: stage 1 adds v and u (successor w in the target),
stage 2 adds w (successor v in Z). So r(v) = r(u) = (0,1) < r(w) = (0,2): the minimal-rank strategy sends v to u and u to v,
and the play v u v u ... has min Inf = 1: lost by player 0, although X = {w} ⊆ layeredAttr is fatal and the WITNESS
strategy (v -> w, u -> w) wins.  Computed below with the REFEREE-2 pmattr (stages recorded)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2lib import Game, colours, layered_attr_hkp
# max-parity encoding with M = 2: w pr 2 (colour 0), v,u pr 1 (colour 1)
g = Game([2, 1, 1], [0, 0, 0], [[1], [0, 2], [0, 1]])   # 0 = w, 1 = v, 2 = u
c = colours(g); V = frozenset(range(3)); X = frozenset({0})
A = layered_attr_hkp(g, c, V, 0, X)
print("colours", c, "layeredAttr(X={w}) =", sorted(A), "fatal:", X <= A)
# stages of PMAttr(X, 0)
Z, stage, rank = set(), 0, {}
while True:
    stage += 1
    new = {x for x in V - Z if (g.owner[x] == 0 and any(y in Z | X for y in g.succ[x])) or (g.owner[x] == 1 and all(y in Z | X for y in g.succ[x]))}
    if not new: break
    for x in new: rank[x] = (0, stage)
    Z |= new
print("ranks:", {['w', 'v', 'u'][x]: r for x, r in sorted(rank.items())})
succ_min = {x: min(g.succ[x], key=lambda y: rank[y]) for x in (1, 2)}
print("minimal-rank strategy: v ->", ['w', 'v', 'u'][succ_min[1]], ", u ->", ['w', 'v', 'u'][succ_min[2]], "=> play v u v u ..., min Inf colour 1: LOST by player 0")
print("witness strategy: v -> w, u -> w => play v w v w ..., min Inf colour 0: won by player 0")
