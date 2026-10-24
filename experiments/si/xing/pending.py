#!/usr/bin/env python3
"""L-SI box 6: pending eviction level P_k at EVERY state of the longest phase: max lev(Ξ_k(σ_k y), Ξ_k(z)) over honest-improving edges
y -> z with y ∈ R_k, z ∈ F_k (−3 if none). Tests the invariant I(L): after a carry of level L, P_k ≤ L at every state until the next
carry, while w is constant. Reports violations with the state kind and what changed at the transition into the violating state.
Usage: pending.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carries import *

def pend(g, E, r, o):
    Xi = r["Xi"]; best = -3; arg = None
    for y in r["R"]:
        if g.owner[y] != 0: continue
        sy = r["s"][y]
        for z in g.succ[y]:
            if z == sy or z in r["R"] or z == o: continue
            if E.key(Xi[z]) > E.key(Xi[sy]):
                l = lev(E, Xi[sy], Xi[z])
                if l > best: best, arg = l, (y, z)
    return best, arg

def scan3(path, show=False):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    for r in rows: r["Xi"], _ = E.evaluate(tuple(r["s"]))
    x, y = max(ph, key=lambda p: p[1] - p[0]); L = None; w0 = None; checks = viol = 0; ex = []
    for k in range(x, y + 1):
        r = rows[k]
        if r["w"] != w0: L, w0 = None, r["w"]
        P, arg = pend(g, E, r, o)
        if L is not None and k > 0 and not rows[k - 1]["fb"]:
            checks += 1
            if P > L:
                viol += 1
                prev = rows[k - 1]; S, act, pas = classify(g, rows, k - 1, o)
                ex.append(dict(k=k, P=P, L=L, pair=arg, kind=("E" if r["Xk"] == r["Wk"] else "T" if all(r["h"]) else "N"),
                               into=dict(fb=prev["fb"], θch=prev["th"] != r["th"], act=act[:4], ent=len(r["R"] - prev["R"]))))
        if k < y and any(rows[k + 1]["Wk"][v] < r["Wk"][v] for v in range(g.n)):      # carry at k -> k+1
            S, act, pas = classify(g, rows, k, o)
            L = max([lev(E, r["Xi"][v], rows[k + 1]["Xi"][v]) for v, kd in act if kd.startswith("L")] or [-3])
    return g.n, checks, viol, ex

if __name__ == "__main__":
    T = [0, 0]
    for p in sys.argv[1:]:
        n, c, v, ex = scan3(p); T[0] += c; T[1] += v
        if c: print(f"{os.path.basename(p):22s} n {n:3d} checks {c:3d} violations {v:3d}", ex[:2])
    print("TOTAL checks, violations:", T)
