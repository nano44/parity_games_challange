#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §7: per step, the movers that move, each marked KEY (its key o(l-1) changed in that step) or pref, with the
movers of its closure that moved at the step before (its possible triggers). Usage (from experiments/lower/l7): fired.py GENOME.txt"""
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run, okeys
D = rd(sys.argv[1]); S, O = run(D); T = len(S) - 1; N = 2 * D['d']
def clos(x):
    seen = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            y = D['xt'][2 * z + k]
            if y >= 0 and y not in seen: seen.add(y); st.append(y)
    return seen
print('T', T, 'xt pairs 0-2:', [(x, D['xt'][2*x], D['xt'][2*x+1]) for x in range(6)])
for t in range(1, T + 1):
    mv = [x for x in range(N) if S[t][x] != S[t-1][x]]
    row = []
    for x in mv:
        l = x // 2
        if l == 0: row.append('%d(L0)' % x); continue
        keych = O[t][l-1] != O[t-1][l-1]
        trig = sorted(y for y in clos(x) if S[t-1][y] != S[t-2][y]) if t >= 2 else []
        row.append('%d(%s%s)' % (x, 'KEY' if keych else 'pref', ' trig=' + ','.join(map(str, trig)) if not keych or True else ''))
    print(t, ' '.join(row))
