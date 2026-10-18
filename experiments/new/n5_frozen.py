#!/usr/bin/env python3
"""Box 4 test of K2 on dummygift games: start N5 (n5.run, unmodified, --start semantics) with the ORIGINAL game's Odd vertices at
their final strategy τ* of a plain run and every dummy at the gift g; prints iterations, fallbacks, longest lock.
Usage: n5_frozen.py dummygame.pg n_original"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n5
from n5 import pg
from n5_taustar import final_pair
from n5_lock import step
from n5 import Engine, dual
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n0 = int(sys.argv[2]); G = n0
_, tstar, it0, fb0, _ = final_pair(g)
ts = {v: (tstar[v] if v < n0 else G) for v in range(g.n) if g.owner[v] == 1}
it, fb, *_ = n5.run(g, start=({}, ts))
E, Ed = Engine(g), Engine(dual(g)); s = list(E.initial("best")); t = list(Ed.initial("best"))
for v, w in ts.items(): t[v] = w
run = cur = 0
while True:
    r = step(g, E, Ed, s, t)
    if r is None: break
    s, t = r[0], r[1]; cur = cur + 1 if r[2] else 0; run = max(run, cur)
print(f"plain: it={it0} fb={fb0} | frozen-start: it={it} fb={fb} longest lock={run}")
