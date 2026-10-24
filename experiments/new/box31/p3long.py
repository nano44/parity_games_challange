#!/usr/bin/env python3
"""Box 31: P3′ pieces (route form, c_θ more relevant than c_w): |R|, length, transitions with a change on R, index of the last κ
change (κ = route vertices above c_θ; P3′ step 1: ≤ |R| − 1), and the P3′ bound |R| + (|R| − 2)(|R| − 1). Usage: p3long.py game.pg"""
import sys
from casccheck import *
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box29"))
from p3check import route
g = load(sys.argv[1]); rows, o = rows_of(g); E = Engine(g); k = 0
while k < len(rows):
    if not rows[k]["rf"]: k += 1; continue
    j = k
    while j + 1 < len(rows) and rows[j + 1]["rf"] and all(rows[j + 1][f] == rows[k][f] for f in ("ph", "R", "th", "w")): j += 1
    if j > k and E.rank[rows[k]["cth"]] > E.rank[rows[k]["cw"]]:
        Rs = sorted(v for v in rows[k]["R"] if v != o); hi = {v for v in range(g.n) if E.rank[v] > E.rank[rows[k]["cth"]]}
        nxt = lambda r: [r["s"][v] if g.owner[v] == 0 else (rows[k]["ph"][2] if v == o else g.succ[v][0]) for v in range(g.n)]
        kap = [tuple(frozenset(route(nxt(r), v, o)) & hi for v in Rs) for r in rows[k:j + 1]]
        last = max([i for i in range(1, len(kap)) if kap[i] != kap[i - 1]] or [0])
        ch = sum(1 for i in range(k, j) if any(rows[i]["Wk"][v] != rows[i + 1]["Wk"][v] or rows[i]["s"][v] != rows[i + 1]["s"][v] for v in Rs))
        nR = len(rows[k]["R"]) + 1; print(f"P3 piece {k}..{j} |R| (o counted) {nR} length {j - k} R-changing {ch} last kappa change {last} bound {nR + (nR - 2) * (nR - 1)} ok {ch <= nR + (nR - 2) * (nR - 1) and last <= nR - 1}")
    k = j + 1
