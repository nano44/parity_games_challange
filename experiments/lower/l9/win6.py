#!/usr/bin/env python3
"""L-LOWER 9: 6-window profile of a genome: per 6-window [t0, t1) (o(5) constant), the movers moving at each step (all movers),
u1/u2 of pair 6. Usage: win6.py GENOME.txt [j=6]"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
D = rd(sys.argv[1]); j = int(sys.argv[2]) if len(sys.argv) > 2 else 6
S, O = run(D); T = len(S) - 1
b = [t for t in range(1, T + 1) if O[t][j - 1] != O[t - 1][j - 1]]; cuts = [1] + b + [T + 1]
for w, (a, e) in enumerate(zip(cuts, cuts[1:])):
    rows = []
    for t in range(a, e):
        mv = [x for x in range(len(S[0])) if S[t][x] != S[t - 1][x]]
        rows.append(f'{t}:' + ','.join(map(str, mv)))
    print(f'W{w} [{a},{e}) c={O[a][j-1]}', ' | '.join(rows))
