#!/usr/bin/env python3
"""L-SI box 23 (successor 19): cross-check of a run against L-COMP's independent implementation experiments/n5-second/n5b.py (SPEC mode,
its own trace hook; that file is imported, not edited). Prints whether the (sigma, tau) state sequences of n5b and of n5x (common.rows) are
identical, n5b's iterations and fallbacks, and, from n5b's trace alone, the most switches of one Even vertex inside one maximal run of
constant tau and constant lambda (lambda from n5x's states, which must coincide).
Usage: n5bcmp.py GAME.pg START"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import n5b
n5b.MODE = "spec"
from common import rows, load, readstart, phases
gp, sp = sys.argv[1], sys.argv[2]
g = n5b.pg.read(gp); s = n5b.N5(g); s.mode = "spec"
sig, tau = n5b.read_start(sp, g); tr = []
win, strat, it, fb = s.run(sig, tau, trace=tr)
g1 = load(gp); E, R = rows(g1, readstart(sp))
A = [(tuple(x for x in a if x >= 0), tuple(x for x in b if x >= 0)) for a, b in tr]
B = [(tuple(R[k]["s"][v] for v in range(g1.n) if g1.owner[v] == 0), tuple(R[k]["t"][v] for v in range(g1.n) if g1.owner[v] == 1)) for k in range(len(R))]
print("n5b iterations", it, "fallbacks", fb, "states", len(tr), "| n5x states", len(R), "| identical state sequences:", A == B)
Ev = [v for v in range(g1.n) if g1.owner[v] == 0]
for i, j in phases(R):
    sw = Counter()
    for k in range(i, j):
        for x, w in enumerate(Ev):
            if A[k][0][x] != A[k + 1][0][x]: sw[w] += 1
    if sw:
        w, c = sw.most_common(1)[0]
        print(f"phase [{i},{j}] (n5x lambda/tau) len {j - i}: n5b trace gives Even vertex {w} switching {c} times; n = {g1.n}; > n: {c > g1.n}")
