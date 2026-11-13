#!/usr/bin/env python3
"""L-SI box 106 §3e: the COVERAGE certificate: cnf106.build_run(LEN, cores) — the level-0 gate order, the KEY run with L* >= LEN, the
availability bits AV[σ][x] as FREE variables (named in the DIMACS comments), and one clause per core of out/cores106_L<LEN>.json
forbidding it — solved with Glucose 4 DRUP. UNSAT = every KEY run of length >= LEN needs some core. With every core certified UNSAT on its
own AV-CNF (certcore106.py; the AV-CNF of a core's states is a clause subset of §3a's CNF up to the naming of the AV variables), the
query «some G* has L* >= LEN» is UNSAT. Usage: covercert106.py LEN TAG"""
import sys, os, json, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cnf106 as C
from pysat.solvers import Solver
import pysat
LEN, tag = int(sys.argv[1]), sys.argv[2]
cores = json.load(open(os.path.join(HERE, "out/cores106_L%d.json" % LEN)))
E = C.build_run(LEN, cores); os.makedirs("dump", exist_ok=True); path = "dump/%s.cnf" % tag
C.dimacs(E, path, ["L-SI box 106 covercert106.py: the KEY run with L* >= %d, AV free, %d cores forbidden (out/cores106_L%d.json, sha1 %s)" % (
    LEN, len(cores), LEN, hashlib.sha1(open(os.path.join(HERE, "out/cores106_L%d.json" % LEN), "rb").read()).hexdigest())], avmap=True)
sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
t0 = time.time(); s = Solver(name="glucose4", with_proof=True, bootstrap_with=E.cl); r = s.solve(); dt = time.time() - t0
out = "COVERCERT106 %s L* >= %d with %d cores forbidden: %s | vars %d clauses %d | cnf sha1 %s | solver glucose4 (python-sat %s) | %.1f s" % (
    tag, LEN, len(cores), "SAT" if r else "UNSAT", E.n, len(E.cl), sha, pysat.__version__, dt)
if not r:
    pf = s.get_proof() or []
    with open("dump/%s.drup" % tag, "w") as f:
        for line in pf: f.write(line + "\n")
    out += " | proof lines %d sha1 %s" % (len(pf), hashlib.sha1(open("dump/%s.drup" % tag, "rb").read()).hexdigest())
print(out, flush=True)
