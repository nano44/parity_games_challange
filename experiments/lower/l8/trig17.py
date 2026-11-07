#!/usr/bin/env python3
"""L-LOWER 8: per (8,0) 5-window of a genome, mover 17 (level 8; q5 = 10 reads it via 10:0 -> 17) at steps u1, u1+1: its state, its key
c = o(7) at the new state, free?, preference (dec_s(17) = deciding option rank, mover, option, side) at pre-states s_(u1-1), s_u1.
Also the closure(17) movers whose state differs between s_(u1-1) and s_u1. Usage: trig17.py GENOME.txt [mover]"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run, dec
D = rd(sys.argv[1]); S, O = run(D); T = len(S) - 1; y = int(sys.argv[2]) if len(sys.argv) > 2 else 17; ly = y // 2
def clos(x):
    seen = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            w = D['xt'][2 * z + k]
            if w >= 0 and w not in seen: seen.add(w); st.append(w)
    return seen
C = clos(y); b = [t for t in range(1, T + 1) if O[t][4] != O[t - 1][4]]; cuts = [1] + b + [T + 1]
for a, e in zip(cuts, [c - 1 for c in cuts[1:]]):
    if not (a > 1 and S[a][8] != S[a - 1][8] and S[a][8] == 0): continue
    mv = [t for t in range(a, e + 1) for x in (10, 11) if S[t][x] != S[t - 1][x]]; u1, u2 = mv
    row = []
    for t in (u1, u1 + 1):
        c = O[t][ly - 1]; s = S[t - 1]; d = dec(D, s, y); pref = d[3] if d[1] != y or True else None
        row.append(f't{t}: s{y}={s[y]} c={c} free={s[y] != c} dec={d[:3]} moved={S[t][y] != s[y]}')
    dif = sorted(z for z in C if S[u1][z] != S[u1 - 1][z])
    print(f'[{a},{e}] PULSE {u2 - u1} |', ' | '.join(row), '| closure diff s_(u1-1)->s_u1:', dif[:10])
