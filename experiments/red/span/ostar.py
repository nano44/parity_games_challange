#!/usr/bin/env python3
"""L-RED successor 31 (R129): O* and the tau-part of B* from L-SI P-N5-CUT §8 (l-si 2678f6c6), on L-COMP's n5b SPEC trace.
lambda-run: maximal run of states with Xi's cycle-node map constant; lambda^U-run: the same for U = Odd's valuation on G^d (n5b's dual
engine). O* := max over lambda^U-runs R' of the transitions t -> t+1 with t, t+1 in R' at which tau changes; TB* := max over lambda-runs R of
the tau-changing transitions inside R (B*'s tau part); FB* := max over lambda-runs of Even S4c fallbacks inside R (B*'s other part).
Usage: ostar.py GAME.pg START"""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for p in ("experiments/n5-second", "experiments/hard-families", "experiments/harness"): sys.path.insert(0, os.path.join(R, p))
import n5b, pg
g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g)
N = n5b.N5(g, mode="spec"); tr = []; fb = []; N.run(s0, t0, trace=tr, fbtrace=fb); T = len(tr) - 1
lam = [tuple(x[0] for x in N.SG.evaluate(list(s[0]))) for s in tr]
lamU = [tuple(x[0] for x in N.SD.evaluate(list(s[1]))) for s in tr]
tch = [tuple(tr[t][1]) != tuple(tr[t + 1][1]) for t in range(T)]
efb = [bool(fb[t]) and tuple(tr[t][0]) != tuple(tr[t + 1][0]) for t in range(T)] if len(fb) >= T else [False] * T
def per_run(lm, flag):
    best = cur = 0
    for t in range(T):
        if lm[t] != lm[t + 1]: cur = 0; continue
        cur += flag[t]; best = max(best, cur)
    return best
print(f"OSTAR {os.path.basename(sys.argv[1])} n {g.n} iter {T} tau-changes {sum(tch)} lambda-runs {1 + sum(lam[t] != lam[t + 1] for t in range(T))} "
      f"lambdaU-runs {1 + sum(lamU[t] != lamU[t + 1] for t in range(T))} O* {per_run(lamU, tch)} TB* {per_run(lam, tch)} FB* {per_run(lam, efb)}")
