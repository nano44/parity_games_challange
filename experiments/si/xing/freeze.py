#!/usr/bin/env python3
"""L-SI box 6: CONJECTURE FREEZE(L): after a carry (W-lowering transition) of level L, while w is constant, every transition up to and
including the next carry changes every Ξ(v) only at levels ≤ L (lev as carries.py). Also checks the carry transition itself (A: a carry
of level L changes Ξ only at levels ≤ L). Reports violations with the vertex, its kind of change and the state kind.
Scope: transitions up to the last carry of the phase (after it no carry needs the bound).
Usage: freeze.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from carries import *

def scan4(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    for r in rows: r["Xi"], _ = E.evaluate(tuple(r["s"]))
    x, y = max(ph, key=lambda p: p[1] - p[0]); L = None; w0 = None; c = dict(tr=0, viol=0, carryA=0, carryAviol=0); ex = []
    carries_k = [k for k in range(x, y) if any(rows[k + 1]["Wk"][v] < rows[k]["Wk"][v] for v in range(g.n))]
    lastc = max(carries_k) if carries_k else -1
    for k in range(x, y):
        a, b = rows[k], rows[k + 1]
        if a["w"] != w0: L, w0 = None, a["w"]
        mx = max((lev(E, a["Xi"][v], b["Xi"][v]), v) for v in range(g.n))
        carry = any(b["Wk"][v] < a["Wk"][v] for v in range(g.n))
        if carry:
            S, act, pas = classify(g, rows, k, o)
            Lk = max([lev(E, a["Xi"][v], b["Xi"][v]) for v, kd in act if kd.startswith("L")] or [-3])
            c["carryA"] += 1
            if mx[0] > Lk: c["carryAviol"] += 1; ex.append(("A", k, mx, Lk))
        if L is not None and b["w"] == w0 and k <= lastc:   # scope: up to and including the LAST carry of the phase
            c["tr"] += 1
            if mx[0] > L:
                c["viol"] += 1
                ex.append(("F", k, mx, L, "fb" if a["fb"] else "ar", "in R" if mx[1] in a["R"] else "in F", "θch" if a["th"] != b["th"] else "-"))
        if carry: L = Lk
    return g.n, c, ex

if __name__ == "__main__":
    T = dict(tr=0, viol=0, carryA=0, carryAviol=0)
    for p in sys.argv[1:]:
        n, c, ex = scan4(p)
        for kk in T: T[kk] += c[kk]
        if c["tr"] or c["carryA"]: print(f"{os.path.basename(p):22s} n {n:3d}", c, ex[:3])
    print("TOTAL", T)
