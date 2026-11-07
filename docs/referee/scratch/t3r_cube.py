#!/usr/bin/env python3
"""REFEREE successor 24: re-solve one d = 3, T >= 9 cube of L-COMP box 27 cnf.py (claude/l-comp 6f19564f) with a chosen pysat
solver, and record the DIMACS sha1 of the exact CNF (so any solver can re-check it).
Cube c (0..15) = cubes.sh's: SYM=1 and CUBE = '2:b0,3:b1,4:b2,5:b3,' with b_i = (c >> i) & 1.
Usage: CNFDIR=<dir> python3 -I t3r_cube.py c SOLVER [DIMACS_OUT]"""
import hashlib, os, sys, time
c, solver = int(sys.argv[1]), sys.argv[2]
os.environ["SYM"] = "1"
os.environ["CUBE"] = "".join(f"{i + 2}:{(c >> i) & 1}," for i in range(4))
for v in ("FREE0", "ISO", "KF", "P"):
    os.environ.pop(v, None)
sys.path.insert(0, os.environ["CNFDIR"])
import cnf
from pysat.solvers import Solver
C, I = cnf.build(3, 9, None, "R")
txt = f"p cnf {C.n} {len(C.cl)}\n" + "".join(" ".join(map(str, cl)) + " 0\n" for cl in C.cl)
h = hashlib.sha1(txt.encode()).hexdigest()
empty = sum(1 for cl in C.cl if len(cl) == 0)
units = sum(1 for cl in C.cl if len(cl) == 1)
if len(sys.argv) > 3:
    open(sys.argv[3], "w").write(txt)
t = time.time()
s = Solver(name=solver, bootstrap_with=C.cl)
r = s.solve()
print(f"CUBE {c} {os.environ['CUBE']} vars {C.n} clauses {len(C.cl)} dimacs-sha1 {h} empty-clauses {empty} unit-clauses {units} solver {solver} "
      f"result {'SAT' if r else 'UNSAT'} {time.time() - t:.1f} s", flush=True)
