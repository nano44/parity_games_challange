#!/usr/bin/env python3
"""L-SI box 23 (successor 19): DATA for docs/si/N5-ALT-box23.md §8. Runs N5 on BASE and on BASE + reader vertex o (the last vertex of WITH),
checks that sigma and tau on the old vertices, the fallback flags, the phases and every old vertex's Xi agree at every state (SAME), and prints
per phase the number of Xi-changes of o (XR_o) and the most Xi-changes of any vertex (XR_max), against n of WITH.
Usage: orcheck.py BASE.pg BASE.start WITH.pg WITH.start"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from common import rows, phases, load, readstart
from collections import Counter
g0, g1 = load(sys.argv[1]), load(sys.argv[3]); n0, n = g0.n, g1.n; o = n - 1
E0, R0 = rows(g0, readstart(sys.argv[2])); E1, R1 = rows(g1, readstart(sys.argv[4]))
n0s = range(n0)
ss = all(R0[k]["s"][:n0] == R1[k]["s"][:n0] for k in range(min(len(R0), len(R1))))
st = all([R0[k]["t"][v] for v in n0s if g0.owner[v] == 1] == [R1[k]["t"][v] for v in n0s if g0.owner[v] == 1] for k in range(min(len(R0), len(R1))))
sf = all(R0[k]["fb"] == R1[k]["fb"] for k in range(min(len(R0), len(R1))))
sb = all([R0[k]["sb"][v] for v in n0s if g0.owner[v] == 1] == [R1[k]["sb"][v] for v in n0s if g0.owner[v] == 1] for k in range(min(len(R0), len(R1))))
# Xi of old vertices compared by cycle node, path-set as a vertex set, and length (ranks shift when o is added, the order does not)
vset = lambda E, m: frozenset(v for v in range(len(E.rank)) if m >> E.rank[v] & 1)
sx = all([(R0[k]["vs"][v][0], vset(E0, R0[k]["vs"][v][1]), R0[k]["vs"][v][2]) for v in n0s] == [(R1[k]["vs"][v][0], vset(E1, R1[k]["vs"][v][1]), R1[k]["vs"][v][2]) for v in n0s] for k in range(min(len(R0), len(R1))))
same = len(R0) == len(R1) and ss and st and sf and sb and sx
print("sigma", ss, "tau", st, "fallbacks", sf, "sigma-bar", sb, "Xi (as vertex sets)", sx)
print("SAME" if same else "DIFFERENT", "states", len(R0), len(R1), "n", n)
P0, P1 = list(phases(R0)), [(i, j) for i, j in phases(R1)]
print("phases_equal", P0 == P1)
for i, j in P1:
    tr = Counter()
    for k in range(i, j):
        for z in range(n):
            if R1[k]["vs"][z] != R1[k + 1]["vs"][z]: tr[z] += 1
    if j - i >= n: print(f"phase [{i},{j}] len {j - i} XR_o {tr[o]} XR_max {max(tr.values())} (vertex {tr.most_common(1)[0][0]}) 2n {2 * n} XR_o > 2n: {tr[o] > 2 * n}")
