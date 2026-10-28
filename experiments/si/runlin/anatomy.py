#!/usr/bin/env python3
"""L-SI box 24 (successor 20): anatomy of the longest fallback-free run (docs/si/N5-RUNLIN-box24.md §1).
Prints: n, m_E, run [a, b] and its phase, length; single-switch transitions; total switches; switches-per-vertex histogram;
FRESH / NOFRESH transitions (C5: a transition is FRESH if some Even vertex switches to an edge it held at no earlier state of the run);
sigma-bar-changing transitions G and the sigma-bar-constant pieces (lengths), max piece; lambda_W changes inside the run.
Usage: anatomy.py G.pg [G.start|-]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, HERE)
from common import rows, load, readstart
from trace import runs

def main():
    g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
    E, R = rows(g, st); a, b, i, j = max(runs(R), key=lambda r: r[1] - r[0])
    mE = sum(len(g.succ[v]) for v in range(g.n) if g.owner[v] == 0)
    C = Counter(); one = 0; held = {v: {R[a]["s"][v]} for v in range(g.n) if g.owner[v] == 0}; fresh = 0; G = 0; pieces = []; p0 = a; lw = 0
    for k in range(a, b):
        A, B = R[k], R[k + 1]
        sw = [v for v in held if A["s"][v] != B["s"][v]]; C.update(sw); one += len(sw) == 1
        if any(B["s"][v] not in held[v] for v in sw): fresh += 1
        for v in sw: held[v].add(B["s"][v])
        if A["sb"] != B["sb"]: G += 1; pieces.append(k + 1 - p0); p0 = k + 1
        if [x[0] for x in A["W"]] != [x[0] for x in B["W"]]: lw += 1
    pieces.append(b - p0)
    print("n %d m_E %d phase [%d,%d] run [%d,%d] len %d (%.3fn)" % (g.n, mE, i, j, a, b, b - a, (b - a) / g.n))
    print("single-switch %d total-switches %d hist %s never %d" % (one, sum(C.values()), sorted(Counter(C.values()).items()), len(held) - len(C)))
    print("FRESH %d NOFRESH %d sigmabar-changing G %d pieces %s maxpiece %d lambdaW-changes %d" % (fresh, b - a - fresh, G, pieces, max(pieces), lw))

if __name__ == "__main__":
    main()
