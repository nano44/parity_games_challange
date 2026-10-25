#!/usr/bin/env python3
"""Box 32: the levels of W-changes on R inside U2 / U3 / U23 stretches (the (K_W) core). For each non-fallback transition with a W-change at
some v in R: lev_W = lev(W_k(v), W_{k+1}(v)); classes: LEN (lev_W = -1: lengths only), PATH_le_L (lev_W >= 0 and <= the used level L_k of
lcheck.py), PATH_gt_L (lev_W > L_k), INF (cycle node of W(v) changes). Per stretch: the number of transitions with a PATH-type W-change.
Usage: kwlev.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from dormant import *

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f); rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]
        for i in range(len(rows) - 1):
            a, c = rows[i], rows[i + 1]
            if a["ph"] != c["ph"] or a["fb"] or a["R"] != c["R"] or a["th"] != c["th"] or a["w"] != c["w"]: continue
            st = "rf" if a["rfX"] and a["rfW"] else ("U2" if a["rfW"] else ("U3" if a["rfX"] else "U23"))
            if st == "rf": continue
            L = relL(g, ev, rows, i); R = set(a["R"]) | {o}; kinds = set()
            for v in R:
                if a["W"][v] == c["W"][v]: continue
                lw = lev(a["W"][v], c["W"][v])
                kinds.add("INF" if lw >= 99 else ("LEN" if lw == -1 else ("PATH_le_L" if lw <= L else "PATH_gt_L")))
            for kd in kinds: acc[f"{st}_{kd}"] = acc.get(f"{st}_{kd}", 0) + 1
            if "PATH_gt_L" in kinds: acc.setdefault(f"ex_{st}_PATH_gt_L", (os.path.basename(f), i, L))
            if kinds: acc[f"{st}_KWtrans"] = acc.get(f"{st}_KWtrans", 0) + 1
    for k in sorted(acc): print(k, acc[k])
