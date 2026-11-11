#!/usr/bin/env python3
"""L-SI box 82 (draft): per-level anatomy of an IDEAL-CYC Howard run. Per level l: GF(l) = (step, gate of a level-l option) sigma-bar
changes; RF(l) = R-steps with a sigma-bar change at a level-l gate; MV(l) = mover moves at level l; KF(l) = key-order flips of pair l
(R104 key: gate indices along the W-chain). Also: labels, Xi-cycles (as lists of movers), U(G), max ascents (census81).
Usage: anal82.py GENOME.json BOX81DIR"""
import sys, os, json
sys.path[:0] = [sys.argv[2], os.path.join(sys.argv[2], "ref", "experiments", "new", "box191"), os.path.join(sys.argv[2], "ref", "experiments", "new", "box189")]
import idealcyc, gamma3, census81

G = json.load(open(sys.argv[1])); N = G["N"]; d = max(G["lev"]) + 1
h, s0, movers, inv = idealcyc.build(G); E = idealcyc.Engine(h); st = idealcyc.run(G)
_, _, _, V = gamma3.build(G, set())
gl = {V[("g", (x, k))]: G["lev"][x] for x in range(N) for k in range(len(G["opts"][x]))}
gi = {}
for x in range(N):
    for v in h.succ[movers[x]]: gi[(x, inv[v])] = v
def keyorder(s):
    K = [None] * N
    for x in sorted(range(N), key=lambda x: G["lev"][x]):
        w = G["opts"][x][s[x]][0]; g = G["gate"][x][s[x]]; K[x] = (g,) if w < 0 else K[w] + (g,)
    return [int(K[2 * j] < K[2 * j + 1]) for j in range(d)] if N == 2 * d else []
GF = [0] * d; RF = [0] * d; MV = [0] * d; KF = [0] * d; lab = []; prev = None
for t, s in enumerate(st):
    cur = list(s0)
    for x in range(N): cur[movers[x]] = gi[(x, s[x])]
    vs, sb = E.evaluate(tuple(cur))
    lam = [vs[v][0] for v in range(h.n)]
    if prev is not None:
        pl, psb, ps = prev
        ch = [g for g in gl if sb[g] != psb[g]]
        L = "C" if lam != pl else ("R" if any(sb[v] != psb[v] for v in range(h.n) if h.owner[v] == 1) else "p"); lab.append(L)
        for g in ch:
            GF[gl[g]] += 1
        if L == "R":
            for l in {gl[g] for g in ch}: RF[l] += 1
        for x in range(N):
            if s[x] != ps[x]: MV[G["lev"][x]] += 1
        ko, pko = keyorder(s), keyorder(ps)
        for j in range(len(ko)): KF[j] += ko[j] != pko[j]
    prev = (lam, list(sb), s)
# Xi-cycles of the full Xi-graph (simple, by DFS from each node, small N only)
adj = {x: sorted({o[1] for o in G["opts"][x] if o[1] >= 0}) for x in range(N)}
cyc = set()
def dfs(start, x, path):
    for y in adj[x]:
        if y == start: cyc.add(tuple(path))
        elif y > start and y not in path and len(path) < 8: dfs(start, y, path + [y])
for x in range(N): dfs(x, x, [x])
r, _, _ = census81.census(G)
print(os.path.basename(sys.argv[1]), "N", N, "T", len(st) - 1, "labels", "".join(lab), "R", lab.count("R"), "C", lab.count("C"))
print("  GF", GF, "RF", RF, "MV", MV, "KF", KF, "U", r["U"], "maxasc", r["maxasc"], "hist", r["hist"], "maxDE", r["maxDE"])
print("  Xi-cycles (movers, level):", [[(x, G["lev"][x]) for x in c] for c in sorted(cyc, key=len)][:12], "count", len(cyc))
