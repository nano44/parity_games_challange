#!/usr/bin/env python3
"""L-LOWER 6: J-windows of a text genome with key, own type, parent type, pair-J moves, and per step the decider of pair J's members.
Usage: win.py genome.txt J [verbose]"""
import sys
from sim6 import rd, run, dec, Fprof
D = rd(sys.argv[1]); J = int(sys.argv[2]); V = len(sys.argv) > 3
S, O = run(D); T = len(S) - 1
def wins(j):
    bst = [t for t in range(1, T + 1) if O[t][j - 1] != O[t - 1][j - 1]]; cuts = [1] + bst + [T + 1]
    return [(a, b - 1, tuple((x, S[a][x]) for x in (2*j-2, 2*j-1) if a > 1 and S[a][x] != S[a-1][x])) for a, b in zip(cuts, cuts[1:])]
up = wins(J - 1); W = wins(J); bad = 0
for i, (a, e, typ) in enumerate(W):
    par = [ty for (aa, ee, ty) in up if aa <= a <= ee]; ptyp = par[0] if par else None
    mv = [(t, x, S[t][x]) for t in range(a, e + 1) for x in (2*J, 2*J+1) if S[t][x] != S[t-1][x]]
    ok = len(mv) == 2; bad += not ok
    if V or not ok:
        print(f"W{i} [{a},{e}] key {O[a][J-1]} own {typ} parent {ptyp} moves {mv} {'OK' if ok else 'FAIL'}")
        if V:
            for t in range(a - 1, e + 1):
                print("   t", t, "dec", [dec(D, S[t], x) for x in (2*J, 2*J+1)], "s", S[t][2*J], S[t][2*J+1],
                      "movers", [x for x in range(2*D['d']) if t > 0 and S[t][x] != S[t-1][x]])
print("windows", len(W), "fail", bad)
