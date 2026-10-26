#!/usr/bin/env python3
"""REFEREE-2 succ. 14: for the non-vacuous FRZ-U_H3 freeze runs, report L = max(max_S M_D, -1), the top rank n - 1, and whether any W path
set on the run has a vertex ranked above L (i.e. whether the coarse freeze has content beyond the cycle-node map). Usage: level_content.py
game.pg game.start"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h3_check as H
g = H.pg.read(sys.argv[1]); s = [x[0] for x in g.succ]; t = [x[0] for x in g.succ]
for line in open(sys.argv[2]):
    p = line.split()
    if not p or p[0].startswith("#") or p[0] == "score": continue
    tg = s if p[0] == "SIGMA0" else t
    for kv in p[1:]: v, w = map(int, kv.split(":")); tg[v] = w
states, fbs = H.DC.Runner(g).run(s, t)
ctx = H.Ctx(g); n = g.n; I = [H.state_info(ctx, a, b) for a, b in states]
lam = [tuple(S["xi"][v][0] for v in range(n)) for S in I]
tk = [tuple(b[v] for v in range(n) if g.owner[v] == 1) for _, b in states]
k0 = 0
while k0 < len(states):
    k1 = k0
    while k1 + 1 < len(states) and (lam[k1 + 1], tk[k1 + 1]) == (lam[k0], tk[k0]): k1 += 1
    a = k0
    while a <= k1:
        b = a
        while b < k1 and not fbs[b]: b += 1
        if b - a >= n and all(I[k]["h3"] for k in range(a, b + 1)):
            L = int(max(max(I[k]["MD"] for k in range(a, b + 1)), -1))
            above = sum(1 for k in range(a, b + 1) for v in range(n) if I[k]["w"][v][1] >> (L + 1))
            print(os.path.basename(sys.argv[1]), f"run {a}..{b} n {n} L {L} top-rank {n - 1} W-path-set vertices above L: {above}")
        a = b + 1
    k0 = k1 + 1
