#!/usr/bin/env python3
"""REFEREE succ. 18: per tau-stretch |S|, Q (fallback or lambda_W-changing transitions), fb_S, FL_S, n on one game (own engine). Used for the
RESULTS-line check of P-N5-FRAME (Q undefined in the line: with Q = 0, |S| <= (n-1)(R*_S+1) + FL_S would be required)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, core_probe as CP
g = RE.parse(sys.argv[1]); s0 = CP.parse_start(g, sys.argv[2]) if len(sys.argv) > 2 else None
st = RE.run(g, s0); T = len(st) - 1; n = g.n
nxs = [[x["s"][v] if g.owner[v] == 0 else x["t"][v] for v in range(n)] for x in st]
W = [[RE.play_value(g, nx, v) for v in range(n)] for nx in nxs]; lamW = [tuple(v[0] for v in w) for w in W]
tk = [tuple(x["t"][v] for v in range(n) if g.owner[v] == 1) for x in st]
i = 0
while i <= T:
    j = i
    while j < T and tk[j + 1] == tk[i]: j += 1
    L = j - i
    if L:
        Q = sum(1 for t in range(i, j) if st[t]["fb"] or lamW[t + 1] != lamW[t]); fb = sum(1 for t in range(i, j) if st[t]["fb"])
        FL = sum(1 for t in range(i, j) if st[t + 1]["s"] != st[t]["s"] and W[t + 1] == W[t])
        print("STRETCH", i, j, "len", L, "Q", Q, "fb", fb, "FL", FL, "n", n, "n-1", n - 1)
    i = j + 1
print("T", T)
