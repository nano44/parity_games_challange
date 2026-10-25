#!/usr/bin/env python3
"""Box 33: per vertex, joins of R inside one phase, split by θ-runs (maximal runs with θ = Ξ(o) constant) and fallback-free segments.
Reports the max joins of one vertex per (θ-run, fb-free segment) block, and per θ-run. Usage: xjoin.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from xgrow import *

def jstats(g, name, acc):
    rows, o, phs = phases(g)
    for (k, j) in phs:
        blk = {}; thr = {}; b = t = 0
        for i in range(k, j):
            a, c = rows[i], rows[i + 1]
            if i > k and rows[i]["th"] != rows[i - 1]["th"]: t += 1
            R0, R1 = set(a["R"]) | {o}, set(c["R"]) | {o}
            for v in R1 - R0:
                blk[(t, b, v)] = blk.get((t, b, v), 0) + 1; thr[(t, v)] = thr.get((t, v), 0) + 1
                if blk[(t, b, v)] >= 2: acc.setdefault("ex_blk2", []).append((name, i, v)) if len(acc.get("ex_blk2", [])) < 5 else None
            if a["fb"]: b += 1
            if c["th"] != a["th"]: pass
        for key, d in (("blk", blk), ("thrun", thr)):
            m = max(d.values()) if d else 0
            h = acc.setdefault("hist_" + key, {}); h[m] = h.get(m, 0) + 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        try: jstats(g, os.path.basename(f), acc)
        except Exception as e: acc["ERR"] = acc.get("ERR", 0) + 1
    for k in sorted(acc): print(k, acc[k])
