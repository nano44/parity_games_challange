#!/usr/bin/env python3
"""L-LOWER 9: re-solve a DIMACS CNF with a second solver (pysat Glucose4) and write its DRUP proof, for a cross-check of hsat.py's
CaDiCaL results. Usage: resolve2.py F.cnf P.proof"""
import sys, time
from pysat.formula import CNF
from pysat.solvers import Glucose4
F = CNF(from_file=sys.argv[1]); t0 = time.time()
with Glucose4(bootstrap_with=F.clauses, with_proof=True) as s:
    r = s.solve(); print('RESULT', 'SAT' if r else 'UNSAT', f'{time.time() - t0:.1f}s', flush=True)
    if not r:
        P = s.get_proof()
        with open(sys.argv[2], 'w') as f: f.writelines(l + '\n' for l in P)
        print('proof lines', len(P), 'last', P[-1] if P else None)
