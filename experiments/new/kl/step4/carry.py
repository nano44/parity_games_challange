#!/usr/bin/env python3
"""N8d §0b C1 check: chain games where Tighten carries out of a full digit; counts carries in both codes and compares pivots."""
import sys, random
import os
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
sys.path[:0] = [R + "/new/kl", R + "/n8d-second", R + "/harness"]
import pg, kl, kl_single, kl2
C = {"kl": 0, "kl2": 0}
ot = kl.tighten
def t1(G, mu, v, w):
    r = ot(G, mu, v, w)
    if mu[w] is not kl.TOP and G.pi[v] % 2 == 1:
        k = kl.klen(G, G.pi[v])
        if mu[w][k-1] == G.base - 1: C["kl"] += 1
    return r
kl.tighten = t1
o2 = kl2.KL.tighten
def t2(self, mu, v, w):
    r = o2(self, mu, v, w); p = self.pi[v]
    if mu[w] is not kl2.TOP and p % 2 == 1 and mu[w][self.K[p]-1] == self.ell - 1: C["kl2"] += 1
    return r
kl2.KL.tighten = t2
def chain(n, top):   # node 0: priority top (even), Even self-loop; 1..n-1 priority 1 chain to 0; Odd n-1 also has arc to 1 (and to 0 first)
    prio = [top] + [1] * (n - 1); owner = [0] + [1] * (n - 1)
    succ = [[0]] + [[i + 1] for i in range(1, n - 1)] + [[0, 1]]
    return pg.Game(prio, owner, succ, [None] * n)
for n in range(3, 9):
    for top in (2, 4, 6):
        g = chain(n, top)
        for s in (1, 2):
            C["kl"] = C["kl2"] = 0
            a = kl_single.solve(g, "r2", s); w, st, pp, pd = kl2.solve(g, "r2", s)
            print(n, top, s, (a["it"], a["it_dual"]), (pp, pd), a["win"] == w, "carries", dict(C))
