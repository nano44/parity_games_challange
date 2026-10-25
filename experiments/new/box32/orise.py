#!/usr/bin/env python3
"""Box 32: σ̄(o)-rises of the used level (P-N5-LP §4 step 2's "S_o" case) classified with crossings tested FIRST: for consecutive relevant
k < k′ with L_{k′} > L_k and every relevant Even level at k′ ≤ L_k: FB (a fallback in [k, k′]), X (a crossing in [k, k′]), else ORISE_H1 /
ORISE_notH1 by H1 at k′. CONJECTURE ORISE: the last two are 0; under H1 it is PROVED (N5-L-box32.md §4c). Usage: orise.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from dormant import *

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f); rows, o = rows_w(g); E = Engine(g); ev = [E.evaluate(tuple(r["s"])) for r in rows]; n = g.n
        Ls = [relL(g, ev, rows, k) if rows[k]["ph"] == rows[k + 1]["ph"] else None for k in range(len(rows) - 1)]
        prev = None
        for k in range(len(Ls)):
            if Ls[k] is None: prev = None; continue
            if Ls[k] == -2: continue
            if prev is not None and Ls[k] > Ls[prev]:
                Ev = max([lev(ev[k][0][rows[k]["s"][y]], ev[k][0][rows[k + 1]["s"][y]]) for y in range(n) if g.owner[y] == 0
                          and rows[k]["s"][y] != rows[k + 1]["s"][y] and ev[k][0][y][0] != y] + [-2])
                if Ev <= Ls[prev]:
                    seg = range(prev, k + 1)
                    c = "FB" if any(rows[j]["fb"] for j in seg) else ("X" if any(rows[j]["R"] != rows[j + 1]["R"] for j in seg) else
                         ("ORISE_H1" if rows[k]["h1"] else "ORISE_notH1"))
                    acc[c] = acc.get(c, 0) + 1
                    if c.startswith("ORISE"): acc.setdefault("ex_" + c, (os.path.basename(f), k))
            prev = k
    for kk in sorted(acc): print(kk, acc[kk])
