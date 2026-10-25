#!/usr/bin/env python3
"""Box 32: for every finite dormant gate edge (y, z) at k+1 (level l > L_k, NO-WAKE-type step k -> k+1 -> k+2 as dormant.py), the W-gap
g = lev(W_{k+1}(z), W_{k+1}(a)), a = σ_{k+1}(y). Lemma WAKE-RF (docs/new/N5-L-box32.md §4): an R -> F dormant edge can be woken at k+1
only if g <= L_k or W(z) = W(a). Counts g > L_k (safe), g <= L_k (LOWGAP), ties, by kind (R->F, R->R), and checks W(z) ⊴ W(a) (DF).
Usage: wgap.py game.pg ..."""
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
            s = rows[k + 1]["s"]; Xi = ev[k + 1][0]; W = rows[k + 1]["W"]; R = set(rows[k + 1]["R"]) | {o}
            for y, z in E.improving(tuple(s), Xi):
                l = lev(Xi[s[y]], Xi[z])
                if l <= L or l >= 99: continue
                a = s[y]; kind = ("R" if a in R else "F") + ("R" if z in R else "F")
                if E.key(W[z]) > E.key(W[a]): acc["DF_FAIL"] = acc.get("DF_FAIL", 0) + 1
                gg = lev(W[z], W[a])
                t = "tie" if gg == -2 else ("LOWGAP" if gg <= L else "safe")
                acc[kind + "_" + t] = acc.get(kind + "_" + t, 0) + 1
                if t != "safe": acc.setdefault("ex_" + kind + "_" + t, (os.path.basename(f), k + 1, y, z, l, L, gg))
    for k in sorted(acc): print(k, acc[k])
