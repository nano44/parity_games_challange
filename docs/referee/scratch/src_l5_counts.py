#!/usr/bin/env python3
"""REFEREE successor 21: per-W-run counts for SRC line L-5's DATA clause (own engine rl_engine; W-run split as in src_probe.py).
Per W-run F: XCN(o) = transitions at which sbar(o) changes, Odd o its own Xi-cycle node (at k or k+1); CN(c) = switches of Even c in C;
SB(o) = all sbar(o) changes. Usage: src_l5_counts.py GAME.pg (uses GAME.start if present)."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, core_probe as CP


def nxs(g, s, t): return [s[v] if g.owner[v] == 0 else t[v] for v in range(g.n)]


for p in sys.argv[1:]:
    g = RE.parse(p); sp = p[:-3] + ".start"
    start = CP.parse_start(g, sp) if os.path.exists(sp) else None
    st = RE.run(g, start); n = g.n; T = len(st) - 1
    W = [[RE.play_value(g, nxs(g, s["s"], s["t"]), v) for v in range(n)] for s in st]
    Xi = [s["Xi"] for s in st]
    runs, a = [], 0
    for k in range(T):
        if st[k]["t"] != st[k + 1]["t"] or st[k]["fb"] or [x[0] for x in W[k]] != [x[0] for x in W[k + 1]]: runs.append((a, k)); a = k + 1
    runs.append((a, T))
    print(os.path.basename(p), "n", n, "T", T, "start", "file" if start else "best-reward")
    for (a, b) in runs:
        if b == a: continue
        C = {v for v in range(n) if W[a][v][0] == v}
        XCN, CN, SB = Counter(), Counter(), Counter()
        for k in range(a, b):
            for o in range(n):
                if g.owner[o] == 1 and st[k]["sb"][o] != st[k + 1]["sb"][o]:
                    SB[o] += 1
                    if Xi[k][o][0] == o or Xi[k + 1][o][0] == o: XCN[o] += 1
            for c in C:
                if g.owner[c] == 0 and st[k]["s"][c] != st[k + 1]["s"][c]: CN[c] += 1
        print("  W-run", (a, b), "|F|", b - a, "C", sorted(C), "XCN", dict(XCN), "CN", dict(CN), "SB", dict(SB))
