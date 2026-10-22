#!/usr/bin/env python3
"""Box 10: trace N5's run (n5_lock.step, best-reward start) and report, for the longest σ̄-segment λ-phase, every iteration: Even moves
(vertex: old->new), whether the honest valuation Ξσ changed at all (value-changing vs value-flat), fallback flag, Odd moves count, and the
stalled Even vertices (honest-improving edge available, vertex did not move). Usage: segtrace.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
p = sys.argv[1]; g = pg.read(p); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
rows = []
while True:
    vs, sbar = E.evaluate(tuple(s)); Is = E.improving(tuple(s), vs)
    key = (tuple(sbar[v] if g.owner[v] == 1 else -1 for v in range(g.n)), tuple(vs[v][0] for v in range(g.n)))
    r = step(g, E, Ed, s, t)
    if r is None: break
    ns, nt = r[0], r[1]; vs2, _ = E.evaluate(tuple(ns))
    em = [(v, s[v], ns[v]) for v in range(g.n) if g.owner[v] == 0 and ns[v] != s[v]]
    stalled = sorted({v for v, w in Is if ns[v] == s[v]})
    rows.append((key, em, [E.key(vs2[v]) != E.key(vs[v]) for v in range(g.n)].count(True), r[2], sum(1 for v in range(g.n) if g.owner[v] == 1 and nt[v] != t[v]), stalled, len(Is)))
    s, t = ns, nt
# longest segment-phase by Even-moving iterations
best = (0, 0, 0); i = 0
while i < len(rows):
    j = i
    while j < len(rows) and rows[j][0] == rows[i][0]: j += 1
    cnt = sum(1 for k in range(i, j) if rows[k][1])
    if cnt > best[0]: best = (cnt, i, j)
    i = j
cnt, i, j = best
nE = sum(1 for v in range(g.n) if g.owner[v] == 0)
print(f"{os.path.basename(p)} n={g.n} (Even vertices {nE}) iterations={len(rows)}; longest segment-phase: iterations {i}..{j-1}, Even-moving iterations {cnt}, of which value-changing {sum(1 for k in range(i, j) if rows[k][1] and rows[k][2] > 0)}, value-flat {sum(1 for k in range(i, j) if rows[k][1] and rows[k][2] == 0)}")
for k in range(i, j):
    key, em, nchg, fb, om, stalled, nIs = rows[k]
    print(f"  it {k}: Even moves {em} | values changed at {nchg} vertices | fallback {fb} | Odd moves {om} | |Iσ| {nIs} | stalled Even vertices {stalled}")
