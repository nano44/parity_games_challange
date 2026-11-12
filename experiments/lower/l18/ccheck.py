#!/usr/bin/env python3
"""L-LOWER 18: checker mode of enc32c: GENOME fully fixed, free run on rows 0..PREFIX, clamped run (only CLAMP_KEEP core constraints)
on transitions PREFIX..R-1. Prints SAT / UNSAT. Usage: ccheck.py GENOME TARGET PREFIX R [KEEP=13]"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
import enc32c as enc32
from pysat.solvers import Solver
G, tp, P, R = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
D = enc32.rdgen(G); S, nc = enc32.rdtarget(tp); S = S[:max(P, R) + 1]
if R > P: enc32.CLAMP_FROM = P; enc32.CLAMP_KEEP = set(int(v) for v in (sys.argv[5] if len(sys.argv) > 5 else '13').split(','))
sv = Solver(name='cadical195')
try:
    E, info, _ = enc32.build(D, S, nc // 2, {'ranks', 'signs', 'gates', 'starts'}, sink=sv.add_clause, fixpoint=False)
    ok = (not E.empty) and sv.solve()
except SystemExit as e:
    ok = False; print('build exit:', e)
print('CCHECK', os.path.basename(G), 'prefix', P, 'R', R, 'SAT' if ok else 'UNSAT', 'clauses', info['clauses'] if ok or 'info' in dir() else '')
