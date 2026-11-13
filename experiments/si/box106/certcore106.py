#!/usr/bin/env python3
"""L-SI box 106 §3d, step 2: the CNF of one CORE, solved with Glucose 4 DRUP (the certificate; checked by run106.sh with both checkers).
CNF = cnf106.build(None, states = the core's states, run = False) (the AV-CNF of those states: free data, values, AV; a SUBSET of the
clauses of the full query's CNF up to variable numbering, the AV variables named in the DIMACS comments) + one unit clause per core
literal. UNSAT = no genome realises the core. Usage: certcore106.py LEN INDEX TAG (the core is out/cores106_L<LEN>.json[INDEX])."""
import sys, os, json, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cnf106 as C
from pysat.solvers import Solver
import pysat

def main():
    LEN, i, tag = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    core = json.load(open(os.path.join(HERE, "out/cores106_L%d.json" % LEN)))[i]
    states = sorted(set(tuple(S) for S, x, b in core)); E = C.build(None, states=states, run=False)
    for S, x, b in core: E.add([E.names[("AV", tuple(S), x)] * (1 if b else -1)])
    txt = " ".join("%sAV[%s][%d]" % ("" if b else "-", "".join(map(str, S)), x) for S, x, b in core)
    os.makedirs("dump", exist_ok=True); path = "dump/%s.cnf" % tag
    C.dimacs(E, path, ["L-SI box 106 certcore106.py: core %d of L* >= %d: %s" % (i, LEN, txt)], avmap=True)
    sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    t0 = time.time(); s = Solver(name="glucose4", with_proof=True, bootstrap_with=E.cl); r = s.solve(); dt = time.time() - t0
    out = "CERTCORE106 %s core %d of L* >= %d: %s | states %d | %s | vars %d clauses %d | cnf sha1 %s | solver glucose4 (python-sat %s) | %.1f s" % (
        tag, i, LEN, txt, len(states), "SAT" if r else "UNSAT", E.n, len(E.cl), sha, pysat.__version__, dt)
    if not r:
        pf = s.get_proof() or []
        with open("dump/%s.drup" % tag, "w") as f:
            for line in pf: f.write(line + "\n")
        out += " | proof lines %d sha1 %s" % (len(pf), hashlib.sha1(open("dump/%s.drup" % tag, "rb").read()).hexdigest())
    print(out, flush=True)

if __name__ == "__main__":
    main()
