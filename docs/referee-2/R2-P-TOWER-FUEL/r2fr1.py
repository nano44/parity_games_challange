#!/usr/bin/env python3
"""REFEREE-2 succ. 31, fix round 1: counts new in fixes entry 1 / L-2 that my first report did not measure: distinct I-ROOM 5-windows
carrying the 30 violations; I-FUEL decider = option 19 at s_(a-1) itself; at some state s_a..s_e. Own code (r2tower.py loader).
Usage: r2fr1.py ROOT"""
import sys, os
H = os.path.dirname(os.path.abspath(__file__)); ROOT = sys.argv[1]
src = open(os.path.join(H, 'r2tower.py')).read().split("# ---- §4 instances")[0]
ns = {'__name__': 'lib', '__file__': os.path.join(H, 'r2tower.py')}; sys.argv = ['x', ROOT]; exec(src, ns)
R7, RS = ns['R7'], ns['RS']
W, _ = R7.windows(5); bad = set(); units = 0
for i, (a, e, mv) in enumerate(W):
    if mv[1][0] - mv[0][0] < 2: bad.add(a); units += 1
    if i + 1 < len(W) and W[i + 1][2][0][0] - mv[1][0] < 2: bad.add(a); units += 1
print('I-ROOM level 5: (window, condition) units', units, 'on', len(bad), 'distinct 5-windows of', len(W))
print('I-ROOM j-windows at j = 1..5:', sum(len(R7.windows(j)[0]) for j in range(1, 6)), '| I-FUEL:', sum(len(RS.windows(j)[0]) for j in range(1, 6)))
W6, _ = RS.windows(6); res = {}
for a, e, mv in W6:
    f = sorted(x for _, x in mv) != [12, 13]
    is19 = lambda t: any(RS.dec(RS.S[t], x)[0] == 19 for x in (12, 13))
    for name, ok in (('at s_(a-1)', is19(a - 1)), ('some s_a..s_e', any(is19(t) for t in range(a, e + 1))),
                     ('some pre-state', any(is19(t) for t in range(a - 1, e))), ('every pre-state', all(is19(t) for t in range(a - 1, e)))):
        res.setdefault((name, 'fail' if f else 'good'), 0); res[(name, 'fail' if f else 'good')] += ok
for k in sorted(res): print('I-FUEL decider = option 19 (12 or 13)', k, res[k])
