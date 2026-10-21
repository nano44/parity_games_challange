#!/usr/bin/env python3
"""Box 11: do best-reply changes coincide with cycle-node changes? Along N5's run (n5_lock.step), for each iteration where σ̄ changes, record
whether λ(Ξσ) (the cycle-node vector of Even's honest valuation) also changed at that iteration, and whether the changed Odd vertices' own
cycle node changed; same for τ̄ vs λ(Ξτ). If every σ̄ change came with a λ change, changes ≤ n(n−1)+1. Usage: brphase.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
tot = {"sb": [0, 0, 0], "tb": [0, 0, 0]}   # changes, with global λ change, with λ change at a changed vertex
for p in sys.argv[1:]:
    g = pg.read(p); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best"))
    O = [v for v in range(g.n) if g.owner[v] == 1]; V0 = [v for v in range(g.n) if g.owner[v] == 0]
    prev = None; c = {"sb": [0, 0, 0], "tb": [0, 0, 0]}
    while True:
        vs, sb = E.evaluate(tuple(s)); vt, tb = Ed.evaluate(tuple(t))
        cur = {"sb": (tuple(sb[v] for v in O), tuple(vs[v][0] for v in range(g.n))), "tb": (tuple(tb[v] for v in V0), tuple(vt[v][0] for v in range(g.n)))}
        if prev is not None:
            for key, verts in (("sb", O), ("tb", V0)):
                (b0, l0), (b1, l1) = prev[key], cur[key]
                if b1 != b0:
                    c[key][0] += 1
                    if l1 != l0: c[key][1] += 1
                    if any(l1[v] != l0[v] for j, v in enumerate(verts) if b1[j] != b0[j]): c[key][2] += 1
        prev = cur
        r = step(g, E, Ed, s, t)
        if r is None: break
        s, t = r[0], r[1]
    for key in c:
        for i in range(3): tot[key][i] += c[key][i]
    print(f"{os.path.basename(p)} n={g.n} | σ̄ changes {c['sb'][0]}, with any λ(Ξσ) change {c['sb'][1]}, with λ change at a switched Odd vertex {c['sb'][2]} | τ̄ changes {c['tb'][0]}, with any λ(Ξτ) change {c['tb'][1]}, at a switched Even vertex {c['tb'][2]}")
print("TOTAL σ̄:", tot["sb"], "τ̄:", tot["tb"])
