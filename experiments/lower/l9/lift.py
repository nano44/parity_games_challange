#!/usr/bin/env python3
"""L-LOWER 9: lift a text genome from d to d2 > d with inert top pairs: each new mover x has both options to the exit, ranks
above all old ranks, option 1 positive and option 0 negative (constant preference 1), start 1: never moves; gates 4l+1000.. as sched.py.
Old movers never read new ones, so the old trajectory (and F(0..d-1)) is unchanged. Usage: lift.py IN.txt d2 OUT.txt"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, wr
D = rd(sys.argv[1]); d = D['d']; d2 = int(sys.argv[2]); E = {k: list(v) if isinstance(v, list) else v for k, v in D.items()}
E['d'] = d2; r = 4 * d
for x in range(2 * d, 2 * d2):
    for k in (0, 1):
        E['xt'].append(-1); E['br'].append(r); E['bp'].append(0 if k == 1 else 1); r += 1
    E['start'].append(1)
for l in range(d, d2): E['gate'] += [4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003]
wr(E, sys.argv[3])
