#!/usr/bin/env python3
"""L-COMP box 27: Glucose 4 DRUP proof for a given DIMACS file (optionally with cube units), for drup.c.
Usage: dimproof.py F.cnf OUT.proof [CUBE]   CUBE = comma list of signed variables added as unit clauses (the cube formula is
F + those units; written to OUT.proof.cnf so drup.c checks exactly that file). Prints sha1s, sizes, result, time."""
import sys, hashlib, time
from pysat.formula import CNF
from pysat.solvers import Solver
F, out = sys.argv[1], sys.argv[2]; cube = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 and sys.argv[3] else []
cnf = CNF(from_file=F); cls = cnf.clauses + [[l] for l in cube]
fin = F
if cube:
    fin = out + ".cnf"
    with open(fin, "w") as fo:
        fo.write("p cnf %d %d\n" % (cnf.nv, len(cls)))
        for c in cls: fo.write(" ".join(map(str, c)) + " 0\n")
h = hashlib.sha1(open(fin, "rb").read()).hexdigest()
s = Solver(name="glucose4", bootstrap_with=cls, with_proof=True); t = time.time(); r = s.solve(); dt = time.time() - t
# stream pysat's proof temp file line by line (same text as get_proof(): each line rstripped + "\n"); get_proof() would load the
# whole proof into memory (cube 0 of query 2: ~10.5 GB RSS, killed at 2026-11-06 10:13Z)
pr = s.solver.prfile; pr.flush(); pr.seek(0)
with open(out, "w") as fo:
    for line in pr: fo.write(line.rstrip().decode("ascii") + "\n")
ph = hashlib.sha1(open(out, "rb").read()).hexdigest()
import os
print(f"input {fin} sha1 {h} vars {cnf.nv} clauses {len(cls)} cube {sys.argv[3] if len(sys.argv) > 3 else ''} glucose4 {'SAT' if r else 'UNSAT'} {dt:.1f} s proof {out} sha1 {ph} bytes {os.path.getsize(out)}", flush=True)
