#!/usr/bin/env python3
"""Box 31 (b'): are the U2/U3 residual transitions tame in L-SI's sense (docs/si/P-N5-FB-box7.md §1: M_k = max gate level,
tame iff COARSE_{M_k}(Ξ_{k+1}) = COARSE_{M_k}(Ξ_k) pointwise)? Classes, inside U2 / U3 stretches: EV (U3 W-flat transition with an
event), KW (non-fallback transition with a W-change on R), FLAT (other W-flat transitions with a switch on R). lev/coarse are read from
experiments/si/coarse/mono.py (read-only). Usage: tamecheck.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
from mono import lev, coarse
from u23check import *

def classify(g, acc):
    rows, o = rows_u(g); E = Engine(g); n = g.n
    Xi = []; M = []
    for r in rows:
        x, _ = E.evaluate(tuple(r["s"])); Is = E.improving(tuple(r["s"]), x); Xi.append(x)
        M.append(max([lev(x[r["s"][y]], x[z]) for y, z in Is]) if Is else -3)
    tame = lambda i: all(coarse(Xi[i + 1][v], M[i]) == coarse(Xi[i][v], M[i]) for v in range(n))
    k = 0
    while k < len(rows):
        j = k
        while j + 1 < len(rows) and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
        r0 = rows[k]; kind = "U2" if (not r0["rfX"] and r0["rfW"]) else ("U3" if (r0["rfX"] and not r0["rfW"]) else ("U23" if not r0["rfX"] else None))
        if kind:
            Rs = [v for v in r0["R"] if v != o]; cw = r0["cw"]
            for i in range(k, j):
                a, b = rows[i], rows[i + 1]
                if a["fb"]: continue
                wch = any(a["Wk"][v] != b["Wk"][v] for v in Rs); sw = [v for v in Rs if g.owner[v] == 0 and a["s"][v] != b["s"][v]]
                if wch: cl = "KW"
                elif sw:
                    ev = kind != "U2" and any(v == cw or ((cw in route(a["nxt"], v, o)) != (cw in route(b["nxt"], v, o))) for v in sw)
                    cl = "EV" if ev else "FLAT"
                else: continue
                key = f"{kind}_{cl}_{'tame' if tame(i) else 'NONTAME'}"; acc[key] = acc.get(key, 0) + 1
        k = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            classify(g, acc); d += 1
    else:
        for f in a:
            g = load(f)
            if len([v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1]) != 1: continue
            classify(g, acc)
    print("TAME", acc)
