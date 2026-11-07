#!/usr/bin/env python3
"""L-NEW box 158, DATA: the three level-0 segments of a degree-2 run (before the first level-0 move, between the first and the last
level-0 move, after the last one) and the counts of level-0 steps. Usage: three.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P)}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G); S, _ = g.run(G["start"]); T = len(S) - 1; N = g.N; d = max(g.lev) + 1
    cuts = [t for t in range(1, T + 1) if any(g.lev[v] == 0 and S[t][v] != S[t - 1][v] for v in range(N))]
    if not cuts: print(f"{os.path.basename(f)} d {d} T {T} cuts [] seg1 {T}"); continue
    seg1 = cuts[0] - 1; mid = cuts[-1] - cuts[0] + 1 - len(cuts); tail = T - cuts[-1]
    print(f"{os.path.basename(f)} d {d} N {N} T {T} cuts {cuts} seg1 {seg1} mid {mid} tail {tail}")
