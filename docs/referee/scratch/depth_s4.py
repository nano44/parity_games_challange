#!/usr/bin/env python3
"""REFEREE succ. 16: P-N5-DEPTH §4's instance and the one-vertex game of loc_cex.py, run on my abs_model.py under every rule.
Prints the run, max d*, the fixed time, and the GEN test."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from collections import Counter
import abs_model as A
from abs_depth import plays_from, nval
games = {"DEPTH_s4": (A.Abs(3, [[1, 3], [0, 2, 5], [0, 4, 5]], [-1, 1, 1], [-1, 1, -1], [0, 1, 1]), [3, 5, 0]),
         "loc_cex": (A.Abs(1, [[1, 2, 3]], [0], [0, 1, 2], [0, 5, 5]), [1])}
for name, (g, s0) in games.items():
    gen = all(len({nval(g, p) for p in plays_from(g, v)}) == len(plays_from(g, v)) for v in range(g.n))
    for rule in A.RULES:
        seq = [s0]
        for _ in range(12):
            s2, stt, _ = A.step(g, seq[-1], rule, Counter())
            if s2 is None: break
            seq.append(s2)
            if s2 == seq[-2]: break
        ss = seq[-1]; dmax = max(len(g.play(ss, v)[0]) for v in range(g.n))
        fixed = next(t for t in range(len(seq)) if seq[t] == ss)
        print(name, rule, "GEN" if gen else "non-GEN", "run", seq, "max d*", dmax, "fixed after", fixed, "LONGER" if fixed > dmax else "")
