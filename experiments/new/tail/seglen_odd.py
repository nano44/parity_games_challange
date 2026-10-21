#!/usr/bin/env python3
"""Box 10: the dual of (SEG-LEN) for Odd. Along N5's run (n5_lock.step, best-reward start), a τ̄-segment-phase = maximal run of iterations with
Even's best reply τ̄ (on Even vertices) constant AND every cycle node of Ξτ constant. Reports the max number of Odd-moving iterations inside one
such segment-phase, per instance, against n − 1. Usage: seglen_odd.py game.pg [...]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, ".."))
from n5_lock import step
from n5 import pg, Engine, dual
worst = (0, 0, "")
for p in sys.argv[1:]:
    g = pg.read(p); E, Ed = Engine(g), Engine(dual(g)); s, t = list(E.initial("best")), list(Ed.initial("best")); V0 = [v for v in range(g.n) if g.owner[v] == 0]
    seg = None; k = mx = 0; it = 0
    while True:
        vt, tbar = Ed.evaluate(tuple(t)); key = (tuple(tbar[v] for v in V0), tuple(vt[v][0] for v in range(g.n)))
        if key != seg: seg, k = key, 0
        r = step(g, E, Ed, s, t)
        if r is None: break
        if r[1] != t: k += 1; mx = max(mx, k)
        s, t = r[0], r[1]; it += 1
    print(f"{os.path.basename(p)} n={g.n} iterations={it} max Odd moves in one τ̄-segment λ-phase = {mx} (n-1 = {g.n - 1})")
    if mx > worst[0]: worst = (mx, g.n, p)
print("worst", worst)
