#!/usr/bin/env python3
"""L-LOWER 6: READ PATHS. For each doubling level J (1..JMAX) and each J-window with two staggered pair-J moves (f at u1, q at u2),
the chain of q's moving option (the option q moves to, under s_(u2-1)) as a mover sequence, cut at the first member of pair J (f) if
it occurs. Tally the mover sequences from q to f ('no f' if q's chain does not pass f). Usage: readpath.py genome.txt JMAX"""
import sys
from collections import Counter
from sim6 import rd, run
D = rd(sys.argv[1]); JM = int(sys.argv[2]); S, O = run(D); T = len(S) - 1
for J in range(1, JM + 1):
    bst = [t for t in range(1, T + 1) if O[t][J-1] != O[t-1][J-1]]; cuts = [1] + bst + [T + 1]; tal = Counter()
    for a, b in zip(cuts, cuts[1:]):
        mv = [(t, x) for t in range(a, b) for x in (2*J, 2*J+1) if S[t][x] != S[t-1][x]]
        if len(mv) != 2 or mv[0][0] == mv[1][0]: continue
        (u1, f), (u2, q) = mv; s = S[u2 - 1]; k = S[u2][q]; path = [q]; x = q
        while True:
            y = D['xt'][2 * x + k]
            if y < 0: path.append('X'); break
            path.append(y)
            if y == f or len(path) > 12: break
            x, k = y, s[y]
        tal[(q, f, tuple(path) if f in path else 'no f')] += 1
    print('J', J, ' '.join(f"{n}x q{q}->f{f}:{p}" for (q, f, p), n in tal.most_common(4)))
