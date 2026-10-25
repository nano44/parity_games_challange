#!/usr/bin/env python3
"""Box 33: per phase, grow crossings (R gains a vertex), shrink crossings, the max number of times one vertex joins R, θ-changes,
and whether every joining vertex has λ_Ξ = c_θ (it must: λ fixed in the phase). Prints the per-phase maxima.
Usage: xgrow.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from dormant import *

def phases(g):
    rows, o = rows_w(g); out = []; k = 0
    while k < len(rows) - 1:
        j = k
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[k]["ph"]: j += 1
        out.append((k, j)); k = j + 1
    return rows, o, out

def stats(g, name, acc):
    rows, o, phs = phases(g)
    for (k, j) in phs:
        gr = sh = th = 0; joins = {}; lamok = True
        for i in range(k, j):
            a, c = rows[i], rows[i + 1]; R0, R1 = set(a["R"]) | {o}, set(c["R"]) | {o}
            if a["th"] != c["th"]: th += 1
            if R1 - R0: gr += 1
            if R0 - R1: sh += 1
            for v in R1 - R0:
                joins[v] = joins.get(v, 0) + 1
                if a["Xi"][v][0] != a["Xi"][o][0]: lamok = False
        mj = max(joins.values()) if joins else 0
        if not lamok: acc["LAMBDA_FAIL"] = acc.get("LAMBDA_FAIL", 0) + 1
        for key, val in (("grow", gr), ("shrink", sh), ("joins1", mj)):
            if val > acc.get("max_" + key, (0,))[0]: acc["max_" + key] = (val, dict(n=g.n, T=j - k, grow=gr, shrink=sh, joins1=mj, th=th), name)

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        try: stats(g, os.path.basename(f), acc)
        except Exception: acc["ERR"] = acc.get("ERR", 0) + 1
    for k in sorted(acc): print(k, acc[k])
