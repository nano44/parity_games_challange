#!/usr/bin/env python3
"""L-RED successor 24: level-1 template (farrise25 anatomy): gate q1 (tau -> T1, sbar -> x1 -> Y), source s1 -> {Z1, q1},
chain c_i -> {q1, c_{i-1}}, c_0 = s1, reader x1 -> {Y, c_m}. Usage: lvl1.py m"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "sel"))
from dsl import build
import trace as T
from fbphase import fstats
def spec(m, B=100):
    S = [("T", 1, 1, ["T"], None), ("q1", 1, B + 5, ["T1", "x1"], "T1"), ("T1", 0, B + 20, ["T"], None),
         ("x1", 0, B + 4, ["Y", "c%d" % m], "Y"), ("Y", 1, B + 31, ["T"], None), ("s1", 0, B + 26, ["Z1", "q1"], "Z1"),
         ("Z1", 1, B + 29, ["T"], None)]
    for i in range(1, m + 1):
        S.append(("c%d" % i, 0, 2 * i + 1, ["q1", "s1" if i == 1 else "c%d" % (i - 1)], "q1"))
    return S
if __name__ == "__main__":
    m = int(sys.argv[1]); g, st, nm = build(spec(m))
    if "-v" in sys.argv: T.run(g, st, nm=dict(enumerate(nm)))
    print("m", m, "n", g.n, "f, phase, it =", fstats(g, st))
