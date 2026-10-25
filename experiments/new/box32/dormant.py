#!/usr/bin/env python3
"""Box 32: dormant gate edges (level > L_k, Lemma HI) at NO-WAKE-checked steps (lcheck.py conditions, relevant L as in lcheck.py):
how many have FINITE level (the ones NO-WAKE is about; level-∞ ones can never be taken inside a phase, R25 NOINF), and where their ends lie
(σ(y), z in R or F; R includes o: reach_o returns R minus o). Usage: dormant.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from mblock import *

def relL(g, ev, rows, k):
    a, c = rows[k], rows[k + 1]; Xi = ev[k][0]; L = -2
    for y in range(g.n):
        if g.owner[y] == 0 and a["s"][y] != c["s"][y] and Xi[y][0] != y: L = max(L, lev(Xi[a["s"][y]], Xi[c["s"][y]]))
    for u in range(g.n):
        if g.owner[u] == 1 and ev[k][1][u] != ev[k + 1][1][u] and Xi[u][0] != u: L = max(L, lev(Xi[ev[k][1][u]], Xi[ev[k + 1][1][u]]))
    return L

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f); rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]
        for k in range(len(rows) - 2):
            if rows[k]["ph"] != rows[k + 1]["ph"] or rows[k + 1]["ph"] != rows[k + 2]["ph"] or rows[k]["fb"] or rows[k + 1]["fb"]: continue
            if not (rows[k]["R"] == rows[k + 1]["R"] == rows[k + 2]["R"]): continue
            L = relL(g, ev, rows, k)
            if L == -2: continue
            s = rows[k + 1]["s"]; Xi = ev[k + 1][0]; R = set(rows[k + 1]["R"]) | {o}; acc["steps"] = acc.get("steps", 0) + 1; fin = 0
            for y, z in E.improving(tuple(s), Xi):
                l = lev(Xi[s[y]], Xi[z])
                if l <= L: continue
                key = ("inf" if l >= 99 else "fin") + "_" + ("R" if s[y] in R else "F") + ("R" if z in R else "F")
                acc[key] = acc.get(key, 0) + 1; fin += l < 99
            if fin: acc["steps_with_finite_dormant"] = acc.get("steps_with_finite_dormant", 0) + 1
    for k in sorted(acc): print(k, acc[k])
