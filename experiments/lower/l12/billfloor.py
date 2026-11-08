#!/usr/bin/env python3
"""L-LOWER 12: independent check of slackt.py's bill floor. (1) every gap's bill b(i) >= 1 (the lowest-level mover at a step is
free at its pre-state); (2) the hard intervals (constraints tau(b) - tau(a) > b - a, each needs >= 1 inserted idle step in gaps
a+1..b) admit at most m pairwise disjoint ones, found by the right-endpoint greedy, so any re-timing inserts idle steps in >= m
distinct gaps and pays >= sum over those of b >= m. Usage: billfloor.py GENOME H"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
for p in ('../l10', '../l6', '../l9'): sys.path.insert(0, os.path.join(here, p))
from sim6 import rd, run
from stretch import stretch
D = rd(sys.argv[1]); H = int(sys.argv[2]); S, O = run(D); T = len(S) - 1; J = H - 1; g = D['gate']
keep = [0] + [t for t in range(1, T + 1) if S[t][:2 * J] != S[t - 1][:2 * J]]
S2 = [S[t][:2 * J] for t in keep]; O2 = [O[t][:J] for t in keep]; n = len(S2) - 1
tau0, Tp0, need = stretch(S2, O2, H)
def b(i):
    pre, post, o = S2[i - 1], S2[i], O2[i - 1]
    return sum(1 for x in range(2 * J) if post[x] != pre[x] and ((g[2 * x + 1 - pre[x]] < g[2 * x + pre[x]]) if x < 2 else (pre[x] != o[x // 2 - 1])))
bs = [b(i) for i in range(1, n + 1)]
hard = sorted({(a, bb) for (a, bb), k in need.items() if k > bb - a}, key=lambda x: x[1])
last = -1; m = 0; cost_lb = 0
for a, bb in hard:
    if a + 1 > last: m += 1; last = bb; cost_lb += min(bs[i - 1] for i in range(a + 1, bb + 1))
print('gaps', n, 'min bill per gap', min(bs), 'gaps with bill 0', bs.count(0), '| hard intervals', len(hard), 'disjoint', m, 'bill lower bound', cost_lb)
