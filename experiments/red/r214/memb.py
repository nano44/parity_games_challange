#!/usr/bin/env python3
"""L-RED R214 MEMB: membership of a box150-style JSON genome in R110's L^R_d (R104 IDEAL model, acyclic Xi-graph), condition by
condition, written from the RESULTS R104 / R110 text (no other lane's code). Conditions:
 C1 levels 0..d-1, movers 2l, 2l+1 on level l, N = 2d, no other movers;  C2 every mover has degree 2 (and 'deg', if present, agrees);
 C3 W-target of option (x, k): none (-1) at level 0, mover 2(l-1)+k at level l >= 1;  C4 Xi-target a mover != x or the exit (-1);
 C5 Xi-graph x -> xt(x, k) acyclic;  C6 beta ranks distinct (a permutation of 0..M-1 over the options' beta indices), parities in {0,1};
 C7 gate indices distinct;  C8 beta indices distinct over options;  C9 start: one option index in {0, 1} per mover.
Usage: memb.py g.json ...  Prints PASS or the failed conditions."""
import sys, json
def check(G):
    bad = []; N = G["N"]; lev = G["lev"]; opts = G["opts"]; d = max(lev) + 1
    if N != 2 * d or lev != [v // 2 for v in range(N)]: bad.append("C1")
    if any(len(opts[v]) != 2 for v in range(N)) or ("deg" in G and (list(G["deg"]) if isinstance(G["deg"], list) else [G["deg"]] * N) != [2] * N): bad.append("C2")
    for v in range(N):
        for k, o in enumerate(opts[v]):
            if o[0] != (2 * (lev[v] - 1) + k if lev[v] > 0 else -1): bad.append(f"C3({v},{k})")
            if not (o[1] == -1 or (0 <= o[1] < N and o[1] != v)): bad.append(f"C4({v},{k})")
    col = {}
    def cyc(v):
        col[v] = 1
        for o in opts[v]:
            w = o[1]
            if w >= 0 and (col.get(w) == 1 or (w not in col and cyc(w))): return True
        col[v] = 2; return False
    if any(v not in col and cyc(v) for v in range(N)): bad.append("C5")
    bi = [o[2] for v in range(N) for o in opts[v]]; M = len(bi)
    if len(set(bi)) != M: bad.append("C8")
    rk = [G["br"][i] for i in bi]
    if sorted(rk) != sorted(set(rk)) or len(set(rk)) != M or any(G["bp"][i] not in (0, 1) for i in bi): bad.append("C6")
    gt = [g for v in range(N) for g in G["gate"][v]]
    if len(set(gt)) != len(gt) or len(gt) != M: bad.append("C7")
    if len(G["start"]) != N or any(s not in (0, 1) for s in G["start"]): bad.append("C9")
    return d, bad
for f in sys.argv[1:]:
    d, bad = check(json.load(open(f))); print(f"{f}: d {d} {'PASS' if not bad else 'FAIL ' + ' '.join(bad)}")
