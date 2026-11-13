#!/usr/bin/env python3
"""L-SI box 106 §3c: one CUBE of the query «some G* in 𝓛*_2 has L* >= LEN»: cnf106.build(LEN) plus unit clauses fixing the start R[0]
and the order of the four level-0 gates (GO). The 16 starts x 24 orders cover every genome (each genome has one start and one GO order),
so the query is UNSAT iff every cube is. Writes dump/TAG.cnf and, on UNSAT, dump/TAG.drup (Glucose 4); on SAT, best/TAG.json.
Usage: cube106.py LEN START(4 bits, e.g. 0101) GOPERM(4 digits: the level-0 options q = 0..3 listed from the lowest gate up) [TAG [PATH]]
PATH (optional, a PATH CUBE, §3d): the states R[1..LEN] as 4-bit words joined by «-»; they are fixed by unit clauses as well."""
import sys, os, time, hashlib, json, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box105"))
import cnf106 as C
from pysat.solvers import Solver
import pysat

def main():
    L, start, perm = int(sys.argv[1]), sys.argv[2], [int(c) for c in sys.argv[3]]
    assert len(start) == 4 and sorted(perm) == [0, 1, 2, 3]
    tag = sys.argv[4] if len(sys.argv) > 4 else "q%d_s%s_g%s" % (L, start, sys.argv[3])
    import cover106
    E = C.build(L)
    for u in cover106.cube_units(E, start, perm): E.add([u])
    path = sys.argv[5].split("-") if len(sys.argv) > 5 else []
    for u in cover106.path_units(E, path): E.add([u])
    os.makedirs("dump", exist_ok=True); os.makedirs("best", exist_ok=True); path = "dump/%s.cnf" % tag
    C.dimacs(E, path, ["L-SI box 106 cube106.py: some G* in L*_2 has L* >= %d with start %s and level-0 gate order %s%s" % (L, start, sys.argv[3], (" and states R[1..] " + "-".join(path)) if path else "")])
    sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    t0 = time.time(); s = Solver(name="glucose4", with_proof=True, bootstrap_with=E.cl); r = s.solve(); dt = time.time() - t0
    out = "CUBE106 %s L* >= %d start %s go %s: %s | vars %d clauses %d | cnf sha1 %s | solver glucose4 (python-sat %s) | %.1f s" % (
        tag, L, start, sys.argv[3], "SAT" if r else "UNSAT", E.n, len(E.cl), sha, pysat.__version__, dt)
    if not r:
        pf = s.get_proof() or []
        with open("dump/%s.drup" % tag, "w") as f:
            for line in pf: f.write(line + "\n")
        out += " | proof lines %d sha1 %s" % (len(pf), hashlib.sha1(open("dump/%s.drup" % tag, "rb").read()).hexdigest())
    else:
        import solve106
        st = solve106.decode(E, s.get_model()); json.dump({"mode": "free", "d": 2, "state": st, "L": None}, open("best/%s.json" % tag, "w"))
    print(out, flush=True)

if __name__ == "__main__":
    main()
