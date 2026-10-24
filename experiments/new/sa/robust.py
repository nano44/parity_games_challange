#!/usr/bin/env python3
"""Robustness of the N9a gaps: with the strict constraints tightened from +1 to +STRICT (> 1) the LP is harder; if SA+_{k*-1}
is still feasible, the original gap holds with margin (not a solver-tolerance artefact)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from twoout import circ, rotations
from sa import sa_feasible
strict = float(sys.argv[1])
for n, k in [(4, 1), (7, 2), (10, 3), (11, 3)]:
    print(f"circ({n},1,2) SA+_{k} with strict {strict}: feasible={sa_feasible(circ(n, 1, 2), k, group=rotations(n), strict=strict)}", flush=True)
