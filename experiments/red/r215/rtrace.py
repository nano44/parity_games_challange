#!/usr/bin/env python3
"""L-RED 53 R215 (2): per-step trace of IDEAL-CYC (box191 idealcyc, env WT3): label (C/R/p), movers that switched, gates whose Odd
best response (sigma-bar) changed (as (mover, option): face e / beta). Usage: rtrace.py G.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["WT3"], "experiments/new/box191"))
import idealcyc, subrun191, gamma3
G = json.load(open(sys.argv[1])); h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G); lab = subrun191.labels(G)
gid = {}; _, _, _, V = gamma3.build(G, set()); EV = {V[("e", q)] for q in [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]}
for x in range(G["N"]):
    for v in h.succ[movers[x]]: gid[v] = (x, inv[v])
prev = None
print(G["N"], "movers; opts (W-target, Xi-target, gate):", G["opts"])
for t, s in enumerate(st):
    cur = list(s0)
    for x in range(G["N"]):
        cur[movers[x]] = [v for v in h.succ[movers[x]] if inv[v] == s[x]][0]
    vs, sb = E.evaluate(tuple(cur))
    gf = {gid[v]: ("e" if sb[v] in EV else "b") for v in gid}
    other = tuple(sb[v] for v in range(h.n) if h.owner[v] == 1 and v not in gid)
    lam = {x: vs[movers[x]][0] for x in range(G["N"])}
    if prev:
        sw = [x for x in range(G["N"]) if s[x] != prev[0][x]]; fl = sorted(q + (gf[q],) for q in gf if gf[q] != prev[1][q])
        print(f"{t:3d} {lab[t-1]} switch {sw} flips {fl}")
    if prev and other != prev[2]: print("     (non-gate Odd choice changed)")
    prev = (s, gf, other)
