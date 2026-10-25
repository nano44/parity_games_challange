#!/usr/bin/env python3
"""Box 32: describe every wake (P-N5-LP §3 definition) of a run: state type, whether c_w is above every R-vertex (W length-only,
Lemma KW-LEN regime), whether W changes on R at the wake transition, whether W(y) changes, the W-levels of a vs z. Usage: wakeinfo.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from dormant import *

if __name__ == "__main__":
    for f in sys.argv[1:]:
        g = load(f); rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
        Ls = [relL(g, ev, rows, k) if rows[k]["ph"] == rows[k + 1]["ph"] else None for k in range(len(rows) - 1)]
        prev = None
        for k in range(len(Ls)):
            if Ls[k] is None: prev = None; continue
            if Ls[k] == -2: continue
            if prev is not None:
                seg = range(prev, k + 1)
                if not any(rows[j]["fb"] for j in seg) and all(rows[j]["R"] == rows[j + 1]["R"] for j in seg):
                    a_, c_ = rows[k], rows[k + 1]
                    for y in range(n):
                        if g.owner[y] != 0 or a_["s"][y] == c_["s"][y] or ev[k][0][y][0] == y: continue
                        a, z = a_["s"][y], c_["s"][y]; l = lev(ev[k][0][a], ev[k][0][z])
                        if l <= Ls[prev]: continue
                        R = set(a_["R"]) | {o}; cw = a_["W"][o][0]
                        st = "rf" if a_["rfX"] and a_["rfW"] else ("U2" if a_["rfW"] else ("U3" if a_["rfX"] else "U23"))
                        lenonly = all(E.rank[cw] > E.rank[v] for v in R if v != cw)
                        wch = any(a_["W"][v] != c_["W"][v] for v in R)
                        print(os.path.basename(f), "k", k, "y", y, a, "->", z, "lev", l, "L_prev", Ls[prev], st, "c_w", cw, "lenonly", lenonly,
                              "Wchange_on_R", wch, "W(y)", a_["W"][y], "->", c_["W"][y], "W(a)", a_["W"][a], "W(z)", a_["W"][z], "->", c_["W"][z])
            prev = k
