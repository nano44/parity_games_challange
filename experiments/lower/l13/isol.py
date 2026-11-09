#!/usr/bin/env python3
"""L-LOWER 13: static reach check. For a genome and a mover X, list the movers that do NOT reach X through the genome's (fixed)
option edges (x reaches X iff some option of x points to X or to a mover that reaches X). Usage: isol.py GENOME X"""
import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'l12'))
import enc32_lcomp as e
D = e.rdgen(sys.argv[1]); X = int(sys.argv[2]); xt = D['xt']; N = 2 * D['d']
reach = {X}; ch = True
while ch:
    ch = False
    for m in range(2 * N):
        if xt[m] in reach and m // 2 not in reach: reach.add(m // 2); ch = True
print('genome', sys.argv[1].split('/')[-1], 'X', X, 'movers not reaching X:', sorted(set(range(N)) - reach), '| f5 options ->', xt[2 * X], xt[2 * X + 1])
