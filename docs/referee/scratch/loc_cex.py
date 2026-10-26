#!/usr/bin/env python3
"""REFEREE succ. 16: the one-vertex counterexample to LOC's 'any deterministic rule' (P-N5-GCX §4), run on abs_model.py.
v = 0 with terminal successors a = 1 (h 0, T 0), b = 2 (h 1, T 5), c = 3 (h 2, T 5); w(v) = 0; s_0(v) = a."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collections import Counter
import abs_model as A
g = A.Abs(1, [[1, 2, 3]], [0], [0, 1, 2], [0, 5, 5])
for rule in ["basic", "lowidx", "anti", "sizedep"]:
    seq = [[1]]
    for _ in range(3):
        s2, stt, Al = A.step(g, seq[-1], rule, Counter()); seq.append(s2)
    print(rule, "s_t(v) for t = 0..3:", [x[0] for x in seq], " (M, N)(v):", [(g.vals(x)[0][0], g.vals(x)[1][0]) for x in seq])
