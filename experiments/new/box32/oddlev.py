#!/usr/bin/env python3
"""Box 32: Lemma OE (N5-L-box32.md §4c): at a crossing-free phase transition with H1, the relevant σ̄(o) change has level ≤ the max relevant
Even level of the same transition. Counts, per class (H1 / ¬H1; crossing or not): transitions with a relevant σ̄(o) change, those whose Odd
level exceeds the Even level (OE_FAIL under H1 without crossing), and non-tame transitions (R25 J). Usage: oddlev.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from dormant import *

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f); rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
        for k in range(len(rows) - 1):
            a, c = rows[k], rows[k + 1]
            if a["ph"] != c["ph"]: continue
            X0, X1 = ev[k][0], ev[k + 1][0]
            cls = ("H1" if a["h1"] else "nH1") + ("_x" if a["R"] != c["R"] else "")
            tame = all(coarse(X1[v], a["M"]) == coarse(X0[v], a["M"]) for v in range(n))
            if not tame: acc["J_" + cls] = acc.get("J_" + cls, 0) + 1
            if ev[k][1][o] == ev[k + 1][1][o] or X0[o][0] == o: continue
            Ev = max([lev(X0[a["s"][y]], X0[c["s"][y]]) for y in range(n) if g.owner[y] == 0 and a["s"][y] != c["s"][y] and X0[y][0] != y] + [-2])
            Od = lev(X0[ev[k][1][o]], X0[ev[k + 1][1][o]])
            acc["so_" + cls] = acc.get("so_" + cls, 0) + 1
            if Od > Ev:
                acc["ODD_ABOVE_" + cls] = acc.get("ODD_ABOVE_" + cls, 0) + 1; acc.setdefault("ex_" + cls, (os.path.basename(f), k, Od, Ev))
    for kk in sorted(acc): print(kk, acc[kk])
