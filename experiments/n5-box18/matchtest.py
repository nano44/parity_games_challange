#!/usr/bin/env python3
"""Box 18: nm.matched against L-LIT's brute-force match() (docs/lit/T32-match-check.py @ l-lit a06dc24a, functions only, passed as
FILE): every ordered pair (A, B), A != B, of subsets of K ranks, for ALL 2^K parity patterns (K <= 6), not only improving pairs.
Usage: matchtest.py T32-match-check.py K"""
import itertools, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nm import matched
src = open(sys.argv[1]).read(); ns = {}
exec(src[:src.index("random.seed(1)")], ns)          # the definitions (weight, w, phi, match), not the script's own loop
K = int(sys.argv[2]); tot = dis = carries = imp = 0
subs = [frozenset(c) for k in range(K + 1) for c in itertools.combinations(range(K), k)]
for pm in range(1 << K):
    par = [(pm >> r) & 1 for r in range(K)]; w = {r: ns["w"](r, par) for r in range(K)}
    for A in subs:
        for Bs in subs:
            if A == Bs: continue
            tot += 1; m = matched(A, Bs, w)
            if m != ns["match"](A, Bs, par): dis += 1
            if ns["weight"](Bs, par) > ns["weight"](A, par):
                imp += 1; carries += not m
print(f"MATCHTEST K {K} pairs {tot} disagreements {dis} improving {imp} carries among improving {carries}")
