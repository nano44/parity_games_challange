#!/usr/bin/env python3
"""box 80: per-move trigger analysis. For each move of x at step u (to option c), the step v <= u - 1 at which pi(x) last became c
(v = 0 if from the start) and the movers on x's option chains (under s_(v-1)) that moved at v."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'box76'))
from sim80 import Sim, stats, keyorder
def chain(sim, st, x, k):
    out = []; y = sim.xt[x][k]
    while y >= 0: out.append(y); y = sim.xt[y][st[y]]
    return out
def pis(sim, st):
    c = sim.cv(st); return [0 if sim.v(c, x, 0) > sim.v(c, x, 1) else 1 for x in range(sim.N)]
G = json.load(open(sys.argv[1])); sim = Sim(G); S = sim.run(); T, F, mv = stats(sim, S)
P = [pis(sim, s) for s in S]
X = [int(a) for a in sys.argv[2].split(",")] if len(sys.argv) > 2 else range(sim.N)
for x in X:
    lst = []
    for u in range(1, T + 1):
        if S[u][x] != S[u - 1][x]:
            c = S[u][x]; v = u - 1
            while v >= 1 and P[v - 1][x] == c: v -= 1
            # pi_(s_v)(x) = c and pi_(s_(v-1))(x) != c (or v = 0)
            src = []
            if v >= 1:
                for k in range(2):
                    for y in [x] + chain(sim, S[v - 1], x, k):
                        if S[v][y] != S[v - 1][y] and y != x: src.append(y)
            lst.append("%d:%d<%d[%s]" % (u, c, v, ",".join(map(str, sorted(set(src))))))
    print("x %d lev %d xt %s moves %d: %s" % (x, x // 2, sim.xt[x], mv[x], " ".join(lst)))
