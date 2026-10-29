#!/usr/bin/env python3
"""L-RED successor 29: longest tau-stretch of an N5 run (n5b SPEC): max number of sigma-changes between consecutive tau-changes,
against n + m (L-NEW CONJECTURE FRAME-STRETCH, N5-DW-box62 §5). Usage: tstretch.py GAME.pg [START]"""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, R + "/experiments/n5-second"); sys.path.insert(0, R + "/experiments/hard-families"); sys.path.insert(0, R + "/experiments/harness")
import n5b, pg
g = pg.read(sys.argv[1]); s = n5b.N5(g, mode="spec")
sig, tau = n5b.read_start(sys.argv[2], g) if len(sys.argv) > 2 else (None, None)
tr = []; win, strat, it, fb = s.run(sig, tau, trace=tr)
m = sum(len(set(x)) for x in g.succ)
best = cur = tc = 0
for (a, b), (c, d) in zip(tr, tr[1:]):
    if b != d: tc += 1; cur = 0
    if a != c: cur += 1; best = max(best, cur)
print(f"n {g.n} m {m} n+m {g.n + m} iterations {it} fb {fb} tau-changes {tc} max-tau-stretch {best} ratio {best / (g.n + m):.3f}")
