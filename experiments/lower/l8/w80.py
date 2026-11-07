#!/usr/bin/env python3
"""L-LOWER 8 item 0: 5-windows of a 6-capped genome by opener; per window: u1, u2, PULSE_5, the movers of closure(q5 = 10) moving at
u2 - 1 (with level), and the key vector o(0..9) at a. Usage: w80.py GENOME.txt OPENER(e.g. 8,0)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
D = rd(sys.argv[1]); S, O = run(D); T = len(S) - 1; opx, opv = map(int, sys.argv[2].split(','))
def clos(x):
    seen = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            y = D['xt'][2 * z + k]
            if y >= 0 and y not in seen: seen.add(y); st.append(y)
    return seen
C = clos(10); b = [t for t in range(1, T + 1) if O[t][4] != O[t - 1][4]]; cuts = [1] + b + [T + 1]
for a, e in zip(cuts, [c - 1 for c in cuts[1:]]):
    if not (a > 1 and S[a][opx] != S[a - 1][opx] and S[a][opx] == opv): continue
    mv = [(t, x) for t in range(a, e + 1) for x in (10, 11) if S[t][x] != S[t - 1][x]]
    u1, u2 = mv[0][0], mv[1][0]; trig = sorted((y // 2, y) for y in C if S[u2 - 1][y] != S[u2 - 2][y])
    print(f'[{a},{e}] u1 {u1} u2 {u2} PULSE {u2 - u1} trig(level,mover) {trig[:4]} keys o0-9 {"".join(map(str, O[a][:10]))} o6-14 {"".join(map(str, O[a][6:15]))}')
