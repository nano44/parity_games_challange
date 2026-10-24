#!/usr/bin/env python3
"""L-SI box 4 (c): the parametric one-player game H(θ) WITHOUT a gadget. Odd vertices other than o forced to τ; o is a TERMINAL whose
valuation is θ (an Engine valuation of G). A play from y either reaches o (valuation = route ⊕ θ via Engine.extend along the route;
flagged 'overlap' if a route vertex lies on θ's path set or is θ's cycle node) or closes a cycle avoiding o (ordinary VJ valuation of
the play). Even's optimum: switch-all SI on this one-player game (improvement by Engine.key of extend(y, val[z])).
API: hopt(g, E, t, o, theta, s0) -> (s*, val*, overlaps)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xclass import *

def play_val(g, E, s, t, o, theta, y):
    nxt = lambda v: s[v] if g.owner[v] == 0 else t[v]
    path = [y]; pos = {y: 0}; ov = False
    while True:
        u = path[-1]
        if u == o:
            val = theta
            for v in reversed(path[:-1]):
                if v == theta[0] or (E.bit[v] & theta[1]): ov = True
                val = E.extend(v, val)
            return val, True, ov
        x = nxt(u)
        if x in pos:
            cyc = path[pos[x]:]; w = max(cyc, key=lambda v: E.rank[v]); i = path.index(w)
            mask = 0
            for v in path[:i]:
                if E.rank[v] > E.rank[w]: mask |= E.bit[v]
            return (w, mask, i), False, False
        pos[x] = len(path); path.append(x)

def hopt(g, E, t, o, theta, s0, cap=200):
    s = list(s0)
    for _ in range(cap):
        vals = [play_val(g, E, s, t, o, theta, y) if y != o else (theta, True, False) for y in range(g.n)]
        ch = False
        for y in range(g.n):
            if g.owner[y] != 0 or y == o: continue
            cur = E.key(vals[y][0]); best = (cur, s[y])
            for z in g.succ[y]:
                if z == s[y]: continue
                kz = E.key(E.extend(y, vals[z][0]))
                if kz > best[0]: best = (kz, z)
            if best[1] != s[y]: s[y] = best[1]; ch = True
        if not ch:
            return s, vals
    raise RuntimeError("hopt cap")
