#!/usr/bin/env python3
"""L-LOWER 10: per-mover violations of gsolve's decision list on a genome's clamped full trajectory. Usage: viol.py D28 G32"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from build import *
from gsolve import gsolve
from collections import Counter
D28 = rd(sys.argv[1]); D = fixgates(rd(sys.argv[2])); CT = core8(D28)
S, E = fulltraj(D, CT); cons = constraints(E, S); v, br, bp = gsolve(cons, 4 * D['d'])
V = Counter(); Tt = Counter()
for t, x, p, A, B in cons:
    Tt[x] += 1; top = max(A ^ B, key=lambda m: br[m]); pos = bp[top] == 0
    if ((top in B) == pos) != (p == 1): V[x] += 1
print('score', v, 'constraints', len(cons)); print('violations by mover', sorted(V.items()))
print('helper moves', {x: sum(1 for t in range(1, len(S)) if S[t][x] != S[t-1][x]) for x in range(16, 64) if any(S[t][x] != S[t-1][x] for t in range(1, len(S)))})
