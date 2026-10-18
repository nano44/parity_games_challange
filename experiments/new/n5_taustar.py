#!/usr/bin/env python3
"""Box 4 regime test: N5 (n5.run, unmodified) started at (best-reward σ0, τ*) where τ* = Odd's FINAL strategy of a plain N5 run
(there Iτ = ∅, so τ stays τ* for the whole second run: N5 becomes Even's one-sided process against a fixed optimal Odd).
Prints iterations/fallbacks of both runs. Usage: n5_taustar.py game.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n5
from n5_trace import pg
from n5_lock import step
from n5 import Engine, dual
def final_pair(g, start=None):
    E, Ed = Engine(g), Engine(dual(g)); sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[1].items(): tau[v] = w
    it = fb = 0; fbs = []
    while True:
        r = step(g, E, Ed, sigma, tau)
        if r is None: return sigma, tau, it, fb, fbs
        sigma, tau, f, a, b = r; it += 1; fb += f; fbs.append(f)
if __name__ == "__main__":
    g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
    s, t, it, fb, _ = final_pair(g)
    ts = {v: t[v] for v in range(g.n) if g.owner[v] == 1}
    it2, fb2, *_ = n5.run(g, start=({}, ts))
    s2, t2, it3, fb3, fbs = final_pair(g, ({}, ts)); assert (it3, fb3) == (it2, fb2) and t2 == t
    print(f"plain N5: it={it} fb={fb} | from (best, tau*): it={it2} fb={fb2} pattern={''.join(map(str,fbs))}")
