#!/usr/bin/env python3
"""L-SI box 24: Even switches per vertex in the longest fallback-free run, and the transitions with exactly one switch.
Usage: swcount.py G.pg [G.start|-]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, HERE)
from common import rows, load, readstart
from trace import runs
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E, R = rows(g, st); a, b, i, j = max(runs(R), key=lambda r: r[1] - r[0])
C = Counter(); one = 0
for k in range(a, b):
    sw = [v for v in range(g.n) if g.owner[v] == 0 and R[k]["s"][v] != R[k + 1]["s"][v]]; C.update(sw); one += len(sw) == 1
print("n", g.n, "run", b - a, "single-switch transitions", one, "total switches", sum(C.values()))
print("switches per vertex histogram", sorted(Counter(C.values()).items()), "vertices that never switch", g.n - len(C))
