#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): disjoint stack of lagfam copies with distinct D (copy i's priorities shifted by an even
amount above copy i-1, so parity and in-copy order are kept). Usage: stack.py out.pg D1 D2 ..."""
import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import lagfam
pr, ow, sc, shift = [], [], [], 0
for D in map(int, sys.argv[2:]):
    g = lagfam.build(D); o = len(pr)
    pr += [p + shift for p in g.pr]; ow += list(g.ow); sc += [[w + o for w in s] for s in g.out]
    shift = max(pr) + 1 + (max(pr) + 1) % 2
with open(sys.argv[1], "w") as f:
    f.write(f"parity {len(pr) - 1};\n")
    for v in range(len(pr)): f.write(f"{v} {pr[v]} {ow[v]} {','.join(map(str, sorted(set(sc[v]))))};\n")
