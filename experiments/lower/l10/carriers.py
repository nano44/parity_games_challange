#!/usr/bin/env python3
"""L-LOWER 10: signal carriers. For a genome's clamped full trajectory and a core mover X: every mover y whose state (or negation)
equals X's required preference at all (or most) of X's free pre-states. Usage: carriers.py D28 G32 X [X ...]"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from build import *
D28 = rd(sys.argv[1]); D = fixgates(rd(sys.argv[2])); CT = core8(D28); S, E = fulltraj(D, CT)
for X in map(int, sys.argv[3:]):
    rows = []
    for t in range(2, len(S)):
        o = okeys(E, S[t]); l = X // 2
        if S[t - 1][X] != o[l - 1]: rows.append((S[t - 1], S[t][X]))
    n = len(rows); res = []
    for y in range(2 * E['d']):
        if y == X: continue
        a = sum(1 for s, p in rows if s[y] == p); res.append((max(a, n - a), y, '+' if a >= n - a else '-'))
    res.sort(reverse=True); print(f'X {X}: free pre-states {n}; best carriers (agree, mover, sign):', res[:8])
