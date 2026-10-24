#!/usr/bin/env python3
"""REFEREE-2: statement A of P-N5-FB §6 on the named set (own code on fb_check). At every in-phase evicting fallback (a fallback with a
leaver y in Rbar_k, sigma_{k+1}(y) not in Rbar_k, != o): L := max leaver lev(Xi_k y, Xi_{k+1} y); M_k; tame?  Checks L <= M_k at tame
ones (PROVED part) and counts L = M_k (DATA part). Usage: a_check.py game.pg ..."""
import sys, os
from collections import Counter
import fb_check as F
import pg as lpg
c = Counter(); bad = []
for p in sys.argv[1:]:
    g = lpg.parse("".join(l for l in open(p) if not l.lstrip().startswith("%"))); o = F.one_odd(g)
    s, t = F.start(g, None, False)
    states, fbs, E, Ed = F.run_n5(g, s, t)
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k in range(len(fbs)):
        if not fbs[k]: continue
        if not (A[k].lam == A[k + 1].lam and A[k].lamU == A[k + 1].lamU and states[k][1] == states[k + 1][1]): continue
        R = A[k].Rbar
        lv = [y for y in range(g.n) if g.owner[y] == 0 and states[k][0][y] != states[k + 1][0][y] and y in R
              and states[k + 1][0][y] not in R and states[k + 1][0][y] != o]
        if not lv: continue
        L = max(F.lev(A[k].Xi[y], A[k + 1].Xi[y]) for y in lv); M = A[k].M
        tame = all(F.coarse(A[k + 1].Xi[v], M) == F.coarse(A[k].Xi[v], M) for v in range(g.n))
        c["evicting_inphase_fallbacks"] += 1; c[f"tame={tame}"] += 1; c[f"L==M:{L == M}"] += 1
        if tame and L > M: bad.append((p, k, L, M))
for k in sorted(c): print(k, c[k])
print("VIOLATIONS", bad); print("RESULT", "FAIL" if bad else "OK")
