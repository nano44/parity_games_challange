#!/usr/bin/env python3
"""L-LOWER 8 item 0: the failing 6-windows of a 6-capped genome in detail: window [a, e], length, pair-5 moves of the parent 5-window
(u1, u2, PULSE_5), c6, states of 12, 13 at a - 1, and for the member(s) that do not move: dec_s at every pre-state (rank, mover, option,
side) -- what blocks it. Also the same for the good windows of the same parent type, as a contrast (first 3). Usage: fail16.py GENOME.txt"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run, dec
D = rd(sys.argv[1]); S, O = run(D); T = len(S) - 1
def wins(j):
    b = [t for t in range(1, T + 1) if O[t][j - 1] != O[t - 1][j - 1]]; cuts = [1] + b + [T + 1]; return list(zip(cuts, [c - 1 for c in cuts[1:]]))
W5 = wins(5); dc = Counter(); shown = Counter()
for a, e in wins(6):
    mv = [(t, x) for t in range(a, e + 1) for x in (12, 13) if S[t][x] != S[t - 1][x]]
    good = sorted(x for _, x in mv) == [12, 13]
    pa = [w for w in W5 if w[0] <= a <= w[1]][0]; op = tuple((x, S[pa[0]][x]) for x in (8, 9) if pa[0] > 1 and S[pa[0]][x] != S[pa[0] - 1][x])
    m5 = [(t, x) for t in range(pa[0], pa[1] + 1) for x in (10, 11) if S[t][x] != S[t - 1][x]]
    key = ('good' if good else 'fail', op)
    if good and shown[key] >= 2: continue
    shown[key] += 1; c6 = O[a][5]
    stuck = [x for x in (12, 13) if x not in [y for _, y in mv]]
    ds = {x: [dec(D, S[t], x) for t in range(a - 1, e)] for x in (12, 13)}
    print(key, f'[{a},{e}] len {e - a + 1} pair5 {m5} c6 {c6} s12,13 {S[a - 1][12]},{S[a - 1][13]} moved {mv}')
    for x in (12, 13): print('    dec', x, ds[x])
    if not good:
        for x in stuck: dc[(x, tuple(sorted({(r, y, k) for r, y, k, _ in ds[x]})))] += 1
print('stuck member -> set of deciders over pre-states : #failing windows')
for k, v in dc.most_common(): print('  ', k, v)
