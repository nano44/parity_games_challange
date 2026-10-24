#!/usr/bin/env python3
"""Box 26: crossings (x enters or leaves R) inside (τ, joint-λ, θ, w)-stretches with (h): total per stretch, max per vertex per
stretch, and how many crossings sit at the hysteresis thresholds (entry: honest route⊕θ ▷ o-free value; leave: o-free ▷ route⊕w).
Usage: crossings.py game.pg [start]"""
from common import *
from thtrace import Rset
from wdrop_h import oncycle
from collections import Counter
if __name__ == "__main__":
    g = load(sys.argv[1]); st0 = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; st, _ = trace(g, st0)
    E, Ed = Engine(g), Engine(dual(g)); o = odd_choice(g); rows = []
    for s, t in st:
        Xi, sb = E.evaluate(s); U, _ = Ed.evaluate(t); _, W = wvals(g, s, t)
        h = not oncycle(g, s, sb, o) and not oncycle(g, s, t, o) and Xi[o][0] == W[o][0]
        rows.append((((tuple(x[0] for x in Xi), tuple(y[0] for y in U), t[o]), E.key(Xi[o]), E.key(W[o])), h, Rset(g, s, t, o)))
    per = Counter(); tot = 0; best_tot = 0; best_v = 0
    for k in range(len(rows) - 1):
        if rows[k][0] != rows[k + 1][0] or not (rows[k][1] and rows[k + 1][1]): per = Counter(); tot = 0; continue
        d = rows[k][2] ^ rows[k + 1][2]
        if d:
            tot += 1
            for x in d: per[x] += 1
            best_tot = max(best_tot, tot); best_v = max(best_v, max(per.values()))
    print(sys.argv[1], "n", g.n, "max crossing transitions per stretch", best_tot, "max crossings of one vertex per stretch", best_v)
