#!/usr/bin/env python3
"""L-RED 70 R244: seed text for lad244 from a 2-per-level ladder genome (JSON): d; per mover: start xt0 xt1 g0 g1 (g = rank of the gate
among the 4 gates of its level); then the 4d beta ranks and the 4d beta parities in the order (mover, option).
Usage: dumpseed244.py G.json OUT.txt"""
import sys, sim244
G = sim244.load(sys.argv[1]); N = G["N"]; d = N // 2
assert G["lev"] == [x // 2 for x in range(N)] and all(G["opts"][x][c][0] == (-1 if x < 2 else 2 * (x // 2 - 1) + c) for x in range(N) for c in range(2))
with open(sys.argv[2], "w") as f:
    f.write(f"{d}\n")
    for x in range(N):
        lv = sorted(g for y in (2 * (x // 2), 2 * (x // 2) + 1) for g in G["gate"][y])
        f.write(f"{G['start'][x]} {G['opts'][x][0][1]} {G['opts'][x][1][1]} {lv.index(G['gate'][x][0])} {lv.index(G['gate'][x][1])}\n")
    f.write(" ".join(str(G["br"][G["opts"][x][c][2]]) for x in range(N) for c in range(2)) + "\n")
    f.write(" ".join(str(G["bp"][G["opts"][x][c][2]]) for x in range(N) for c in range(2)) + "\n")
