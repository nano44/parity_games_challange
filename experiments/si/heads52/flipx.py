#!/usr/bin/env python3
"""L-SI box 52: second-engine check of a sbar-flip with both targets' Xi fixed (flipc.py NONE), on L-COMP's n5b SPEC engine
(experiments/n5-second/n5b.py: N5 trace and SpecSI.evaluate_choice for sbar). Prints, for every Odd o and transition k -> k+1 of the
n5b trace with tau_(k+1) = tau_k and sbar_(k+1)(o) != sbar_k(o): the old and new targets, and whether each target's valuation changed.
Usage: flipx.py GAME.pg START"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "n5-second"))
import n5b
g = n5b.pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g)
N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []; N.run(s0, t0, trace=tr, fbtrace=fb)
ev = [N.SG.evaluate_choice(tuple(s)) for s, _ in tr]
for k in range(len(tr) - 1):
    if tuple(tr[k][1]) != tuple(tr[k + 1][1]): continue
    (v0, c0), (v1, c1) = ev[k], ev[k + 1]
    for o in range(g.n):
        if c0[o] != -1 and c0[o] != c1[o]:
            h, h2 = c0[o], c1[o]
            print(f"FLIP k {k} o {o} tau {tr[k][1][o]} old {h} new {h2} oldXi_changed {v0[h] != v1[h]} newXi_changed {v0[h2] != v1[h2]} "
                  f"sigma_changed {[v for v in range(g.n) if tr[k][0][v] != tr[k + 1][0][v]]}")
