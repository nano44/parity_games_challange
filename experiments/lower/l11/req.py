#!/usr/bin/env python3
"""L-LOWER 11: required preferences of the core movers of a clamped target (free pre-state -> required pref) and, between two
consecutive free pre-states of a mover with different requirements, the core movers that changed in between (the trigger
candidates in the core; any helper may also be one). Usage: req.py TARGET"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '../l6')); sys.path.insert(0, here)
from sim6 import okeys
from tsat import rdtarget
LS, g = rdtarget(sys.argv[1]); h = len(g) // 4; K = 2 * h; T = len(LS) - 1
O = [okeys({'d': h, 'gate': g}, list(s)) for s in LS]
for x in range(K):
    l = x // 2; req = []
    for t in range(1, T + 1):
        s = LS[t - 1]
        free = (g[2 * x + 1 - s[x]] < g[2 * x + s[x]]) if l == 0 else (s[x] != O[t][l - 1])
        if free: req.append((t - 1, LS[t][x]))
    line = ' '.join(f'{a}:{p}' for a, p in req); trig = []
    for (a, p), (b, q) in zip(req, req[1:]):
        if p != q: trig.append(f'{a}->{b}:' + ','.join(str(y) for y in range(K) if y != x and any(LS[u][y] != LS[u - 1][y] for u in range(a + 1, b + 1))))
    print(f'mover {x} (pair {l}) pre-state:req  {line}\n   pref changes need a closure mover changing in (a, b]: {" ".join(trig)}')
