#!/usr/bin/env python3
"""Box 32: the finite dormant R -> R gate edges (the only ones NO-WAKE is about, by Lemma WAKE of docs/new/N5-L-box32.md §4): state type
at k+1 (rf = both frames in route form; U2; U3; U23), rank order of c_θ and c_w, and (route form) whether the level lies strictly between
rank c_θ and rank c_w (Lemma BAND) with equal W path sets. Usage: rrdorm.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from dormant import *

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f); rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]
        for k in range(len(rows) - 2):
            if rows[k]["ph"] != rows[k + 1]["ph"] or rows[k + 1]["ph"] != rows[k + 2]["ph"] or rows[k]["fb"] or rows[k + 1]["fb"]: continue
            if not (rows[k]["R"] == rows[k + 1]["R"] == rows[k + 2]["R"]): continue
            L = relL(g, ev, rows, k)
            if L == -2: continue
            r = rows[k + 1]; s = r["s"]; Xi = ev[k + 1][0]; W = r["W"]; R = set(r["R"]) | {o}
            st = "rf" if r["rfX"] and r["rfW"] else ("U2" if r["rfW"] else ("U3" if r["rfX"] else "U23"))
            ct, cw = E.rank[Xi[o][0]], E.rank[W[o][0]]
            for y, z in E.improving(tuple(s), Xi):
                l = lev(Xi[s[y]], Xi[z])
                if l <= L or l >= 99 or s[y] not in R or z not in R: continue
                key = f"RR_{st}_{'cw>cθ' if cw > ct else ('cw<cθ' if cw < ct else 'cw=cθ')}"
                if st == "rf": key += "_band" if (ct < l < cw and W[z][1] == W[s[y]][1]) else "_NOTBAND"
                acc[key] = acc.get(key, 0) + 1; acc.setdefault("ex_" + key, (os.path.basename(f), k + 1, y, s[y], z, l, L))
    for k in sorted(acc): print(k, acc[k])
