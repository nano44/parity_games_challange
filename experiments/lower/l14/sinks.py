#!/usr/bin/env python3
"""L-LOWER 14: for every core mover X (0..15), the movers that do NOT reach X by Xi-edges (isol.py for all X at once).
A global sink = a core mover reached by every other mover (or all but its own option targets). Usage: sinks.py GENOME"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l12'))
import enc32_lcomp as e
D = e.rdgen(sys.argv[1]); xt = D['xt']; N = 2 * D['d']
for X in range(16):
    reach = {X}; ch = True
    while ch:
        ch = False
        for m in range(2 * N):
            if xt[m] in reach and m // 2 not in reach: reach.add(m // 2); ch = True
    nr = sorted(set(range(N)) - reach)
    print('X', X, 'options ->', xt[2 * X], xt[2 * X + 1], '| not reaching:', len(nr), nr if len(nr) <= 12 else '')
