#!/usr/bin/env python3
"""L-SI box 4 (b): at each leave transition of the longest phase: state kind, u* (top-rank vertex of P(θ) Δ P(w); None if equal path
sets), its Engine rank, θ/w change flags since the previous leave transition, |R| before/after.
Tests CONJECTURE (U*-DROP): between consecutive leave transitions with w unchanged, rank(u*) strictly decreases.
Usage: ustar.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from leaves import *

def scan(path, show=True):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows); E = Engine(g)
    viol = checks = 0
    for (x, y) in ph:
        prev = None
        for k in range(x, y):
            if not (rows[k]["R"] - rows[k + 1]["R"]): continue
            Xi, _ = E.evaluate(tuple(rows[k]["s"])); _, W = wvals(g, rows[k]["s"], rows[k]["t"])
            a, b = vset(E, Xi[o]), vset(E, W[o]); d = a[1] ^ b[1]
            u = max(d, key=lambda v: E.rank[v]) if d else None; ru = E.rank[u] if u is not None else -1
            cur = (k, u, ru, rows[k]["w"])
            if prev is not None and prev[3] == cur[3]:
                checks += 1; ok = ru < prev[2]; viol += not ok
            else: ok = None
            if show and y - x >= 4: print(f"  {os.path.basename(path)} k {k} kind {kindstate(rows[k])} fb {rows[k]['fb']} u* {u} rank {ru} |R| {len(rows[k]['R'])}->{len(rows[k+1]['R'])} w-same-as-prev {prev is not None and prev[3] == cur[3]} drop {ok}")
            prev = cur
    return checks, viol

if __name__ == "__main__":
    T = V = 0
    for p in sys.argv[1:]:
        c, v = scan(p, show="--quiet" not in sys.argv) if not p.startswith("--") else (0, 0); T += c; V += v
    print("U*-DROP checks", T, "violations", V)
