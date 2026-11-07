#!/usr/bin/env python3
"""L-COMP box 28 (Lead 05:18Z: restarts every ~40 min, units <= ~25 min): pre-split each root of an acube28 TAG to DEPTH levels by the
SAME complete rule acube28 uses on a timeout: a node at depth j gets one child per value of the Xi-target domain of option j (cnf.py
opts order: (0,0), (0,1), (1,0), ...); XCUBE j:c adds the unit «Xi-target of option j = the c-th value». Coverage: the encoders
(cnf.py and cnf2.py share this family) require exactly one Xi-target per option, so the children of a node partition its solutions.
Writes <id>.split files (acube28 format) only where none exists and no .res exists. Env ISO as for the run (domain sizes differ).
Usage: presplit.py TAG d DEPTH root..."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box27"))
import cnf
TAG, d, D = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); roots = sys.argv[4:]
DIR = os.path.join(HERE, "cubes", TAG); os.makedirs(DIR, exist_ok=True)
os.environ["SYM"] = "1"; os.environ.pop("CUBE", None); os.environ.pop("XCUBE", None)
C, I = cnf.build(d, 1, None, "R"); dom = lambda j: len(I["Xv"][I["opts"][j]])
made = 0
def rec(cid, j):
    global made
    if j >= D: return
    if os.path.exists(os.path.join(DIR, cid + ".res")): return
    n = dom(j); kids = [f"{cid}.{c}" for c in range(n)]
    f = os.path.join(DIR, cid + ".split")
    if not os.path.exists(f): open(f, "w").write(f"presplit depth {j} (option {I['opts'][j]}, {n} values); children {' '.join(kids)}\n"); made += 1
    for k in kids: rec(k, j + 1)
for r in roots: rec(r, 0)
print(f"presplit {TAG} ISO {os.environ.get('ISO')} depth {D}: domains {[dom(j) for j in range(D)]}, new split files {made}")
