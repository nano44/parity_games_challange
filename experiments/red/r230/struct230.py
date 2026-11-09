#!/usr/bin/env python3
"""L-RED 64 R230: script check of B-ONLY3's structural premises on built Gamma3(G) (L-NEW gamma3.build, all pads, env LNEW as bonly3_230):
 RANK  only c_W, K0, K3 outrank an e-vertex (rank by (priority, index)); every e even
 INE   e_g's only in-edge is from pe_g; pe_g's only in-edge is from g; c_W's in-edges = e's with W-target c_W + its loop
 CORE  in the frame, K3's only in-edge is pA (pA's only in-edge K0); every edge from outside {K0..K3, pA, s, q, r} into it ends at K0
 FRAMEK sigma(K0) = pA, sigma(K1) = s, sigma(K3) = K2 (so nothing in the core returns to K0)
Usage: struct230.py G.json ... | struct230.py rand SEED COUNT"""
import sys, os, json, random
from bonly3_230 import gamma3, Engine, rgen, PADS
def chk(G):
    gm, sig, tau, V = gamma3.build(G, PADS); n = gm.n; rk = Engine(gm).rank; N = G["N"]; opts = G["opts"]
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]; ev = {V[("e", q)] for q in O}; emin = min(rk[e] for e in ev)
    pred = [[] for _ in range(n)]
    for v in range(n):
        for w in gm.succ[v]: pred[w].append(v)
    K = [V[("K", i)] for i in range(4)]; core = set(K) | {V[c] for c in ("pA", "s", "q", "r")}; cW = V["cW"]; f = []
    above = {v for v in range(n) if rk[v] > emin and v not in ev}
    if above != {cW, K[0], K[3]}: f.append(("RANK", above))
    if any(gm.prio[e] % 2 for e in ev): f.append("RANK-par")
    for q in O:
        if pred[V[("e", q)]] != [V[("pe", q)]] or pred[V[("pe", q)]] != [V[("g", q)]]: f.append(("INE", q))
    if sorted(pred[cW]) != sorted([cW] + [V[("e", q)] for q in O if opts[q[0]][q[1]][0] < 0]): f.append("INE-cW")
    if pred[K[3]] != [V["pA"]] or pred[V["pA"]] != [K[0]]: f.append("CORE-K3")
    if any(w in core and w != K[0] for v in range(n) if v not in core for w in gm.succ[v]): f.append("CORE-in")
    if (sig[K[0]], sig[K[1]], sig[K[3]]) != (V["pA"], V["s"], K[2]): f.append("FRAMEK")
    return f
fails = cnt = 0
if sys.argv[1] == "rand":
    rng = random.Random(int(sys.argv[2])); Gs = (rgen(rng, rng.randint(1, 4), rng.randint(1, 3), rng.choice([2, 3])) for _ in range(int(sys.argv[3])))
else: Gs = (json.load(open(f)) for f in sys.argv[1:])
for G in Gs:
    if not (isinstance(G, dict) and "opts" in G): continue
    cnt += 1; f = chk(G)
    if f: fails += 1; print("FAIL", cnt, f[:3])
print(f"genomes {cnt} structural fails {fails}")
