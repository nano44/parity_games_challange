#!/usr/bin/env python3
"""L-SI box 9 §12: kinds and levels (vs L = last fallback level) of Even switches at S4a steps after an in-scope fallback. Usage: ffprobe.py game.pg ..."""
import sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reltrace import *
C = Counter()
for p in sys.argv[1:]:
    g = load(p)
    if odd_choice(g) is None: continue
    runs, d_o, exits, out = runs_of(g, p); o = odd_choice(g)
    for S in runs:
        L = None
        for e in S:
            if e["k"] == "F": L = e["M"]; continue
            if L is None or L < 0: continue
            a, b = out[e["i"]], out[e["i"] + 1]
            for y in range(g.n):
                if g.owner[y] == 0 and a["s"][y] != b["s"][y]:
                    z = b["s"][y]; l = lev(a["Xi"][a["s"][y]], a["Xi"][z])
                    kind = ("R" if y in a["R"] else "F") + ("R" if (z in a["R"] or z == o) else "F")
                    C[kind + ("_eqL" if l == L else ("_ltL" if l < L else "_gtL"))] += 1
print(dict(sorted(C.items())))
