#!/usr/bin/env python3
"""L-SI box 24 (successor 20): keeper data (docs/si/N5-RUNLIN-box24.md §3). Along the longest fallback-free run: at each state, D
(Odd u with sigma-bar(u) != tau(u)), whether I_tau is empty, and whether (u, sigma-bar(u)) is in I_tau for u in D.
Usage: keeper.py G.pg [G.start|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, HERE)
from common import rows, load, readstart
from trace import runs
from n5x import Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
E, R = rows(g, st); a, b, i, j = max(runs(R), key=lambda r: r[1] - r[0]); Ed = Engine(dual(g))
inD = itne = sbin = 0
for k in range(a, b + 1):
    A = R[k]; D = [u for u in range(g.n) if g.owner[u] == 1 and A["sb"][u] != A["t"][u]]
    vt, _ = Ed.evaluate(tuple(A["t"])); It = set(Ed.improving(tuple(A["t"]), vt))
    inD += bool(D); itne += bool(It); sbin += any((u, A["sb"][u]) in It for u in D)
print("states", b - a + 1, "with D nonempty", inD, "with I_tau nonempty", itne, "with some (u, sigma-bar(u)) in I_tau, u in D", sbin)
