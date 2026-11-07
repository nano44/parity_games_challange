#!/usr/bin/env python3
"""REFEREE successor 22: lambda_W-phase count under two readings on one game (FILE.pg with FILE.start). strict: a transition j -> j+1 is
in a phase only if lambda_W(j) = lambda_W(j+1) (the line wording: 'consecutive transitions at whose states' lambda_W is constant).
first-state: transition j is in the phase of state j (s21 gate_probe.py and the lane gate.py). Own engine rl_engine. Usage: gate_strict.py FILE.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, stair_probe as SP, core_probe as CP
p = sys.argv[1]; g = RE.parse(p); ex = CP.parse_start(g, p[:-3] + ".start")
st = RE.run(g, ex); n = g.n; K = len(st) - 1
W = [[RE.play_value(g, SP.nxs(g, s["s"], s["t"]), v) for v in range(n)] for s in st]
lam = [tuple(x[0] for x in w) for w in W]
k = 0
while k < K:
    if st[k]["t"] != st[k+1]["t"]: k += 1; continue
    a = k
    while k < K and st[k]["t"] == st[k+1]["t"]: k += 1
    ch = [j for j in range(a, k) if lam[j] != lam[j+1]]
    # strict phases: maximal runs of transitions j with lam[j] == lam[j+1] == phase value
    best = cur = 0; firstst = curf = 0
    for j in range(a, k):
        if lam[j] == lam[j+1]:
            cur += W[j] != W[j+1]; best = max(best, cur)
        else: cur = 0
    for j in range(a, k):
        if j > a and lam[j] != lam[j-1]: curf = 0
        curf += W[j] != W[j+1]; firstst = max(firstst, curf)
    print("K", K, "n", n, "stretch", a, k, "len", k-a, "lam-changes at", ch, "strict", best, "first-state", firstst, "fallbacks", sum(1 for s in st if s["fb"]))
