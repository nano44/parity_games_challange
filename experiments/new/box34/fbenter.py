#!/usr/bin/env python3
"""Box 34: CONJECTURE E1 (docs/new/N5-REL-box34.md §9): inside a scope run, every transition with an R-entry that comes after a fallback
is preceded, since the last fallback, by a θ-change; and (E1') by a θ-change at a level >= the entering edge's honest gain? Here only E1
and the level of the first θ-change after each fallback vs the fallback level. Usage: fbenter.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from fbclus import *

def check(g, acc, name):
    rows, o = rows_w(g)
    for tr in scope_runs(rows, o):
        last = None; thsince = False
        for k in tr:
            A, B = rows[k], rows[k + 1]
            ent = set(B["R"]) - set(A["R"])
            if last is not None and ent and not A["fb"]:
                bump(acc, "entries_after_fb_checked")
                if not thsince: bump(acc, "E1_FAIL"); acc.setdefault("ex_e1", (name, last, k, sorted(ent)))
            if A["fb"]: last = k; thsince = False
            elif A["th"] != B["th"]: thsince = True

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
