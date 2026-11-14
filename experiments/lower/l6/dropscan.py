#!/usr/bin/env python3
"""L-LOWER 6: for every mover y not upstream of pair J's members, the change v(y)_(b+1) - v(y)_b at each step b+1 = the step after a
move «9 -> 1» (the level-5 b-step of type (9, 1)), printed as signed bit-lengths; counts blocks where the DROP exceeds THR =
2^87 + 2^79 + 2^71 + 2^68 + 2^26 (the bound of L6 §4 (a)). Also the coupling of mover 10 to pair J's tails: deciders of 10 per state.
Usage: dropscan.py genome.txt"""
import sys
from collections import Counter
from sim6 import rd, run, topo, values, dec
D = rd(sys.argv[1]); S, O = run(D); T = len(S) - 1; N = 2 * D['d']; order = topo(D); xt = D['xt']
blocks = [t for t in range(1, T + 1) if S[t][9] != S[t-1][9] and S[t][9] == 1]
thr = (1 << 87) + (1 << 79) + (1 << 71) + (1 << 68) + (1 << 26)
pred = {y: [m // 2 for m in range(2 * N) if xt[m] == y] for y in range(N)}
U = set([12, 13]); st = [12, 13]
while st:
    y = st.pop()
    for x in pred[y]:
        if x not in U: U.add(x); st.append(x)
print("blocks (steps of 9 -> 1):", blocks); print("upstream of 12, 13:", sorted(U))
V = [values(D, s, order) for s in S]
sb = lambda z: 0 if z == 0 else (z.bit_length() if z > 0 else -(-z).bit_length())
res = []
for y in range(N):
    if y in U: continue
    ch = [V[b+1][y] - V[b][y] for b in blocks]
    res.append((sum(1 for c in ch if -c > thr), y, [sb(c) for c in ch]))
res.sort(key=lambda r: (-r[0], -max(abs(v) for v in r[2])))
print("movers with a drop > THR at step b+1, by count of blocks (signed bit-lengths of the change per block):")
for r in res[:12]: print("  ", r)
print("max count:", max(r[0] for r in res), "of", len(blocks), "blocks;", len(res), "movers scanned")
c = Counter(dec(D, s, 10)[:3] for s in S); print("mover 10: deciding element (rank, mover, option) over", len(S), "states:", c.most_common(10))
