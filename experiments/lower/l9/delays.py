#!/usr/bin/env python3
"""L-LOWER 9: delay map of the capped pairs. For every move of a mover x of pairs 1..J at step t: wait w = t - (last step <= t at
which c_x changed), so w = 0 means key-fired. Per mover: histogram of w. Usage: delays.py GENOME.txt J"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
D = rd(sys.argv[1]); J = int(sys.argv[2]); S, O = run(D); T = len(S) - 1
for x in range(2, 2 * J + 2):
    l = x // 2; last = 0; H = Counter()
    for t in range(1, T + 1):
        if O[t][l - 1] != O[t - 1][l - 1]: last = t
        if S[t][x] != S[t - 1][x]: H[t - last] += 1
    print(f'mover {x:2d} level {l}: moves {sum(H.values()):3d} wait hist {sorted(H.items())}')
