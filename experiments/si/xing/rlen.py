#!/usr/bin/env python3
"""L-SI box 4: per vertex, entries into R inside θ-constant intervals of a phase: route length (edges to o under (σ, τ)) and route
key (Ξ − θ as an Engine key difference is not available, so the route is recorded as the vertex sequence) at each entry.
Reports max entries of one vertex per θ-constant interval and whether route lengths at successive entries strictly increase.
Usage: rlen.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xclass import *

def route(g, r, y, o):
    nxt = lambda v: r["s"][v] if g.owner[v] == 0 else r["t"][v]
    p = [y]
    while p[-1] != o: p.append(nxt(p[-1]))
    return p

def scan(path):
    g = load(path); rows, ph = profile(g); assert_run(g, rows); o = annotate(g, rows)
    mx = (0, None); nonincr = 0; pairs = 0
    for (x, y) in ph:
        a = x
        while a < y:
            b = a
            while b < y and rows[b + 1]["th"] == rows[a]["th"]: b += 1
            ent = {}
            for k in range(a, b):
                for v in rows[k + 1]["R"] - rows[k]["R"]: ent.setdefault(v, []).append((k, len(route(g, rows[k + 1], v, o)) - 1))
            for v, L in ent.items():
                if len(L) > mx[0]: mx = (len(L), (v, L, (a, b)))
                for (k1, l1), (k2, l2) in zip(L, L[1:]):
                    pairs += 1; nonincr += l2 <= l1
            a = b + 1 if b > a else a + 1
    return g.n, mx, pairs, nonincr

if __name__ == "__main__":
    for p in sys.argv[1:]:
        n, mx, pairs, ni = scan(p)
        print(os.path.basename(p), "n", n, "max entries of one vertex in a θ-constant interval", mx[0], mx[1], "| successive-entry pairs", pairs, "route length not increasing", ni)
