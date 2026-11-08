#!/usr/bin/env python3
"""L-LOWER 11: per-(step, mover) violations of gsolve's decision list on a genome's clamped full trajectory (core = the tight target
file's movers). Usage: viol.py TARGET GENOME"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
for p in ('.', '../l6', '../l7', '../l10'): sys.path.insert(0, os.path.join(here, p))
from sim6 import rd
from clamp import runclamp
from ranksolve import constraints
from gsolve import gsolve
from tsat import rdtarget
LS, cg = rdtarget(sys.argv[1]); D = rd(sys.argv[2]); K = len(LS[0]); N = 2 * D['d']
tg = [list(r) + [None] * (N - K) for r in LS]
for x in range(K, N): tg[0][x] = D['start'][x]
S = runclamp(D, [tuple(r) for r in tg], set(range(K))); cons = constraints(D, S); v, br, bp = gsolve(cons, 2 * N)
bad = []
for t, x, p, A, B in cons:
    top = max(A ^ B, key=lambda m: br[m]); pos = bp[top] == 0
    if ((top in B) == pos) != (p == 1): bad.append((t, x, p))
print('score', v, 'constraints', len(cons), 'violated (step, mover, required pref):', bad)
