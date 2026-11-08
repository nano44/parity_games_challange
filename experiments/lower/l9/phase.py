#!/usr/bin/env python3
"""L-LOWER 9: UPPER-BLIND check on capped sched(h, alpha) targets. For every level l >= 1, member x of pair l and every two consecutive
moves of x (pre-states s, s'): which core movers differ between s and s' (pref_x must differ, Lemma 4 (b)), split into: the other
member of pair l, movers below level l, movers above level l. Prints, per (l, x), how many consecutive pairs have ANY difference above l.
Usage: phase.py h alpha"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l7'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sched import schedule
h = int(sys.argv[1]); al = list(map(int, sys.argv[2].split(','))); D, S = schedule(h, alpha=al); N = 2 * h
for x in range(2, N):
    l = x // 2; mv = [t for t in range(1, len(S)) if S[t][x] != S[t - 1][x]]
    pre = [S[t - 1][:N] for t in mv]; above = other = below = 0
    for a, b in zip(pre, pre[1:]):
        dif = [y for y in range(N) if y != x and a[y] != b[y]]
        above += any(y // 2 > l for y in dif); other += (x ^ 1) in dif; below += any(y // 2 < l for y in dif)
    print(f'h {h} l {l} mover {x}: consecutive move pairs {len(pre) - 1}: differ above {above}, other member {other}, below {below}')
