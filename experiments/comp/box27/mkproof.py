#!/usr/bin/env python3
"""L-COMP box 27: write one d 3 cube's CNF as DIMACS (exactly the clause list cnf.py builds for it) and a solver proof, for drup.c.
Usage: mkproof.py d L cube_id OUTDIR [solver]   (cube_id = index of the start-bit cube as in cubes.sh / acube.py roots; SYM=1)
Env W/P as cnf.py. Prints the sha1 of the DIMACS file and the solver result."""
import os, sys, hashlib, time
d, L, cid, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; name = sys.argv[5] if len(sys.argv) > 5 else "glucose4"
os.environ["SYM"] = "1"; os.environ["CUBE"] = ",".join(f"{x}:{(cid >> i) & 1}" for i, x in enumerate(range(2, 2 * d)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import cnf
from pysat.solvers import Solver
C, I = cnf.build(d, L, None, os.environ.get("W", "R")); os.makedirs(out, exist_ok=True)
fn = os.path.join(out, f"d{d}_L{L}_c{cid}.cnf")
with open(fn, "w") as f:
    f.write(f"p cnf {C.n} {len(C.cl)}\n")
    for c in C.cl: f.write(" ".join(map(str, c)) + " 0\n")
h = hashlib.sha1(open(fn, "rb").read()).hexdigest()
s = Solver(name=name, bootstrap_with=C.cl, with_proof=True); t = time.time(); r = s.solve(); dt = time.time() - t
pf = os.path.join(out, f"d{d}_L{L}_c{cid}.{name}.proof")
with open(pf, "w") as f:
    for line in s.get_proof() or []: f.write(line + "\n")
print(f"cube {cid} CUBE {os.environ['CUBE']} cnf {fn} sha1 {h} vars {C.n} clauses {len(C.cl)} solver {name} {'SAT' if r else 'UNSAT'} {dt:.1f} s proof {pf}", flush=True)
