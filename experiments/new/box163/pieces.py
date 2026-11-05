#!/usr/bin/env python3
"""L-NEW box 163 (DATA): for a genome and k, an optimal <= k-flip forced run over all starts (exact search), cut into its constant-bit
pieces (SWAP-RUN): bit, length, and the frozen remainders R_0, R_1 at each cut. Usage: pieces.py genome.json k"""
import os, sys, json
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box162", "flipcheck.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read(), ns); Gen, cstep, allstates = ns["Gen"], ns["cstep"], ns["allstates"]
G = json.load(open(sys.argv[1])); g = Gen(G); k = int(sys.argv[2]); memo = {}
def best(u, c, f):
    key = (u, c, f)
    if key in memo: return memo[key]
    u2 = cstep(g, u, c); r = ((1 + best(u2, c, f)[0]), "step") if u2[2:] != u[2:] else (0, "stop")
    if f > 0:
        b = best(u, 1 - c, f - 1)
        if b[0] > r[0]: r = (b[0], "flip")
    memo[key] = r; return r
def R(u, c):
    n = 0
    while True:
        u2 = cstep(g, u, c)
        if u2[2:] == u[2:]: return n
        u, n = u2, n + 1
starts = [s for s in allstates(g.N) if s[:2] == (0, 0)]
v, u, c = max((best(s, c, k)[0], s, c) for s in starts for c in (0, 1))
print(f"{os.path.basename(sys.argv[1])} k {k} V_k {v}")
f = k; pieces = []; cur = [c, 0, R(u, 0), R(u, 1)]
while True:
    val, act = best(u, c, f)
    if act == "stop": break
    if act == "flip": pieces.append(cur); c, f = 1 - c, f - 1; cur = [c, 0, R(u, 0), R(u, 1)]; continue
    u = cstep(g, u, c); cur[1] += 1
pieces.append(cur)
for p in pieces: print(f"  piece bit {p[0]} length {p[1]}  at its start R_0 {p[2]} R_1 {p[3]}")
