#!/usr/bin/env python3
"""L-NEW box 163 (DATA): reconstruct an optimal unlimited-flip forced run of a genome (exact search, box 162 cstep), print per frame
the bit c, the movers, the Xi-unhappy set and the frozen remainders R_0, R_1 (runs of the c-step held constant)."""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box162", "flipcheck.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read(), ns); Gen, cstep = ns["Gen"], ns["cstep"]
G = json.load(open(sys.argv[1])); g = Gen(G); memo = {}
def rinf(u):
    if u in memo: return memo[u]
    b = (0, None)
    for c in (0, 1):
        u2 = cstep(g, u, c)
        if u2[2:] != u[2:]: b = max(b, (1 + rinf(u2)[0], c))
    memo[u] = b; return b
def R(u, c):
    n = 0
    while True:
        u2 = cstep(g, u, c)
        if u2[2:] == u[2:]: return n
        u, n = u2, n + 1
u = tuple(G["start"]); print("T_inf from start", rinf(u)[0], "levels", G["lev"])
while True:
    v, c = rinf(u)
    if c is None: break
    u2 = cstep(g, u, c); mv = [x for x in range(2, g.N) if u2[x] != u[x]]
    unh = [x for x in range(2, g.N) if len(g.avail(u, x)) > 1]
    print(f"c {c} R0 {R(u, 0)} R1 {R(u, 1)} Rinf {v} unhappy {unh} movers {mv}"); u = u2
