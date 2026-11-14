#!/usr/bin/env python3
"""Box 210 (L-NEW successor 72): the SCALE PROFILE of a Howard run (DATA / READING, nothing is claimed from it). Engine and run as
gen210.py (split form, start si.Engine.initial("best")). For every priority theta of the game, from the top down:
  loud(theta) := the number of steps at which, for some vertex, Lambda or the part of Pi of priority >= theta changes
(the value truncated at theta; theta = the top priority + 1 gives the steps at which some Lambda changes).
Printed: T, the number of Lambda-loud steps, and per ORIGINAL priority p (e = even, o = odd): loud(p).
With --blocks: the same list cut where loud grows, as «priority range: loud» blocks.
Usage: scale210.py [--blocks] FILE.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import gen210
a = sys.argv[1:]; blocks = a[0] == "--blocks"
for fn in (a[1:] if blocks else a):
    n, n0, pr, ow, succ, start = gen210.frompg(fn); E, hist = gen210.howard(n, n0, pr, ow, succ, start, 20000); rank = E.rank
    val = [h[1] for h in hist]; T = len(hist) - 1; ths = sorted(set(pr[v] for v in range(n0, n)), reverse=True)
    lam = sum(1 for t in range(T) if any(val[t][v][0] != val[t + 1][v][0] for v in range(n))); prof = []
    for th in ths:
        mask = sum(1 << rank[v] for v in range(n) if pr[v] >= th)
        prof.append((th - 2, sum(1 for t in range(T) if any(val[t][v][0] != val[t + 1][v][0] or (val[t][v][1] ^ val[t + 1][v][1]) & mask for v in range(n)))))
    if blocks:
        out = []; i = 0
        while i < len(prof):
            j = i
            while j + 1 < len(prof) and prof[j + 1][1] == prof[i][1]: j += 1
            out.append("%d..%d:%d" % (prof[i][0], prof[j][0], prof[i][1])); i = j + 1
        print("scale210", os.path.basename(fn), "T", T, "Lambda-loud", lam, "blocks", " ".join(out), flush=True)
    else:
        print("scale210", os.path.basename(fn), "T", T, "Lambda-loud", lam, "profile", " ".join("%d%s:%d" % (p, "e" if p % 2 == 0 else "o", l) for p, l in prof), flush=True)
