#!/usr/bin/env python3
"""L-LOWER 18: at f6's free pre-states in a genome's CLAMPED run, the decisive option of f6's preference (top rank in chain(13,0) xor
chain(13,1)) and the movers whose state on those chains differs from row-earlier pattern. Usage: drift.py GENOME TARGET ROWS(list)"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
G, tp = sys.argv[1], sys.argv[2]; rows = [int(v) for v in sys.argv[3].split(',')]
D = sim6.rd(G); T = open(tp).read().split(); n = int(T[0]); tg = [[int(c) for c in T[2 + i]] for i in range(n)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
S = clamp.runclamp(D, tgt, set(range(16)))
for t in rows:
    s = S[t]; a = [2 * x + k for _, _, x, k in sim6.chain(D, s, 13, 0)]; b = [2 * x + k for _, _, x, k in sim6.chain(D, s, 13, 1)]
    A, B = set(a), set(b); dif = (A ^ B); top = max(dif, key=lambda m: D['br'][m]) if dif else None
    movers = sorted(set(m // 2 for m in list(A | B)))
    print('row', t, 'chain0 movers', [m // 2 for m in a], 'chain1 movers', [m // 2 for m in b], 'top opt', top, 'of mover', None if top is None else top // 2,
          'in', 'B' if top in B else 'A', '| helper states', ''.join(str(s[x]) for x in movers if x >= 16), [x for x in movers if x >= 16])
