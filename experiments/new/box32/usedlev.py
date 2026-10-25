#!/usr/bin/env python3
"""Box 32: the USED level L_k := max over changed edges (Even switches σ_k(y) -> σ_{k+1}(y), Odd changes σ̄_k(u) -> σ̄_{k+1}(u)) of
lev(Ξ_k(old), Ξ_k(new)) (R25 lev). With λ_k = λ_{k+1}, R25's Claim (T) applied with L = L_k (proof of Lemma TAME, any L ≥ every changed
edge's level) gives COARSE_{L_k}(Ξ_{k+1}) = COARSE_{L_k}(Ξ_k). Checks that (FREEZE-L, assertion), and measures, inside every phase:
the M_k = ∞ share, the L_k sequence and its RISES (L_{k+1} > L_k), at residual (U2/U3/U23) transitions and overall.
Usage: usedlev.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from mblock import *

def used(g, E, a, c):
    L = -2
    for y in range(g.n):
        if g.owner[y] == 0 and a["s"][y] != c["s"][y]: L = max(L, lev(a["Xi"][a["s"][y]], a["Xi"][c["s"][y]]))
    return L

def run(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); n = g.n
    sb = []
    for r in rows: sb.append(E.evaluate(tuple(r["s"]))[1])
    prevL = None
    for i in range(len(rows) - 1):
        a, c = rows[i], rows[i + 1]
        if a["ph"] != c["ph"]: prevL = None; continue
        L = used(g, E, a, c)
        for u in range(n):
            if g.owner[u] == 1 and sb[i][u] != sb[i + 1][u]: L = max(L, lev(a["Xi"][sb[i][u]], a["Xi"][sb[i + 1][u]]))
        acc["tr"] = acc.get("tr", 0) + 1
        if L < 99 and not all(coarse(c["Xi"][v], L) == coarse(a["Xi"][v], L) for v in range(n)):
            acc["FREEZE_L_FAIL"] = acc.get("FREEZE_L_FAIL", 0) + 1; acc.setdefault("ex_fail", (name, i, L))
        if L >= 99: acc["L_inf"] = acc.get("L_inf", 0) + 1
        if a["M"] >= 99: acc["M_inf"] = acc.get("M_inf", 0) + 1
        resid = (not a["rfX"]) or (not a["rfW"])
        if prevL is not None and L > prevL and not a["fb"] and not rows[i - 1]["fb"]:
            acc["L_rise"] = acc.get("L_rise", 0) + 1
            if resid: acc["L_rise_resid"] = acc.get("L_rise_resid", 0) + 1
        prevL = L

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if len([v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]) != 1: continue
        run(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
