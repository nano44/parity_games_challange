#!/usr/bin/env python3
"""L-LOWER 18: f6 pair (helpers 16, 17; level 8, key o(7)) in a genome's CLAMPED run: its state, o(7) and whether each pair mover is
free, at every row; prints the last row where the pair changes and the change rows. Usage: pairtraj.py GENOME TARGET"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
G, tp = sys.argv[1], sys.argv[2]
D = sim6.rd(G); T = open(tp).read().split(); n = int(T[0]); tg = [[int(c) for c in T[2 + i]] for i in range(n)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
S = clamp.runclamp(D, tgt, set(range(16)))
ch = [t for t in range(1, len(S)) if S[t][16:18] != S[t - 1][16:18]]
print(os.path.basename(G), 'pair changes', len(ch), 'first', ch[:12], 'last', ch[-6:] if ch else None, 'rows', len(S) - 1)
