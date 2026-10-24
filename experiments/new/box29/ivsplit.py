#!/usr/bin/env python3
"""Box 29: per crossing-free interval of each phase (R constant): |R|, |F|, TC clauses (H1, H2, H3 at the first state; types seen),
F-value-changing transitions, R-only value-changing transitions, w-changes, OTHER-touching transitions; per phase the crossings.
Usage: ivsplit.py game.pg [start]"""
import sys
from otherx import *
g = load(sys.argv[1]); rows, out = phases(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None); o = odd_choice(g)
_, ph = profile(g, readstart(sys.argv[2]) if len(sys.argv) > 2 else None)
for (x, y) in ph:
    if y - x < 4: continue
    X = sum(rows[k]["R"] != rows[k + 1]["R"] for k in range(x, y)); O = sum(rows[k]["other"] or rows[k + 1]["other"] for k in range(x, y))
    print(f"phase {x}..{y} ({y-x} it): crossings {X}, OTHER-touching {O}")
    k = x
    while k <= y:
        j = k
        while j + 1 <= y and rows[j + 1]["R"] == rows[j]["R"]: j += 1
        R = rows[k]["R"]; F = [v for v in range(g.n) if v not in R and v != o]; Rs = R | {o}
        fch = ronly = wc = ot = 0
        for i in range(k, j):
            a, b = rows[i], rows[i + 1]
            ch = [v for v in range(g.n) if a["Xk"][v] != b["Xk"][v] or a["Wk"][v] != b["Wk"][v]]
            ot += a["other"] or b["other"]; wc += a["w"] != b["w"]
            if any(v in F for v in ch): fch += 1
            elif ch: ronly += 1
        types = "".join(sorted({("O" if r["other"] else ("E" if r["Xk"] == r["Wk"] else "T")) for r in rows[k:j + 1]}))
        print(f"  states {k}..{j}: |R| {len(R)} |F| {len(F)} clauses {clause(rows[k]['h'])} types {types} | F-changing {fch} (≤ {max(0,len(F)-1)}) R-only {ronly} (≤ |R|? {ronly <= len(R)}) w-changes {wc} OTHER-touching {ot}")
        k = j + 1
