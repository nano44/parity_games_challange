#!/usr/bin/env python3
"""REFEREE: H1 -> not-H1 transitions at PHASE EXITS (key (lambda_Xi, tau) changes) with P(theta_k) != {} -- tests whether H1-INT (b) /
H1-DROP need both ends in the phase. Also H1 and not H2 at s with an S4a step leaving the phase (H2-STICK's 'of a phase').
Usage: l2_exitdrop.py lib | rand N nmin nmax seed"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u1_probe as U, l2_probe as L
def run(g, c, name):
    E, o, st, it, fb = L.states(g)
    for k in range(len(st) - 1):
        a, b = st[k], st[k + 1]
        if a["key"] == b["key"]: continue
        c["exits"] += 1
        if a["H1"] and not b["H1"]:
            c["exit_drop"] += 1
            if a["Xi"][o][1] != 0: c["exit_drop_Pnonempty"] += 1; print("  exit drop with P(theta)!={}", name, k, flush=True)
        if not a["fb"] and a["H1"] and not a["H2"]:
            c["exit_H1nH2_S4a"] += 1
            if b["H2"]: c["exit_H2S_violation"] += 1; print("  exit H2 regained", name, k, flush=True)
a = sys.argv[1:]; c = Counter()
if a[0] == "rand":
    N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
    for i in range(N):
        g = U.rand_c1o(rng, lo, hi)
        if g is not None: run(g, c, "rand%d" % i)
else:
    for p in L.libfiles(): run(U.load(p), c, os.path.basename(p))
print(dict(c))
