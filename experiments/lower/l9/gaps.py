#!/usr/bin/env python3
"""L-LOWER 9: o(l)-change gaps of a genome. A level l+1 can be capped only if every (l+1)-window (run of constant o(l)) has
length >= 2 (two pair-(l+1) moves at distinct steps), i.e. every gap between consecutive o(l) changes (and the first, from step 1)
is >= 2. Prints per level l: number of o(l) changes, histogram of gaps, number of gaps of length 1, and the lower bound
T >= 2 * (F(l) + 1) - 1 needed for level l+1 capped. Usage: gaps.py GENOME.txt [lmax]"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
D = rd(sys.argv[1]); lm = int(sys.argv[2]) if len(sys.argv) > 2 else 8
S, O = run(D); T = len(S) - 1; print('T', T)
for l in range(lm):
    ch = [t for t in range(1, T + 1) if O[t][l] != O[t - 1][l]]
    cuts = [1] + ch + [T + 1]; g = [b - a for a, b in zip(cuts, cuts[1:])]
    print(f'o({l}): F {len(ch)} windows of level {l+1}: {len(g)} gaps hist {sorted(Counter(g).items())} len<2: {sum(1 for x in g if x < 2)}')
