#!/usr/bin/env python3
"""L-SI box 106 §3d: COVERAGE of the cube split. Writes dump/cover6.cnf = cnf106.build(6) (the whole query «L* >= 6») plus, for each of
the 16 x 24 cubes of cube106.py (start, level-0 gate order), one clause that negates the cube's unit clauses; solves it with Glucose 4
(DRUP to dump/cover6.drup). UNSAT means: every model of the query lies in some cube; with every cube UNSAT, the query is UNSAT.
The cube literals are produced by the same code as cube106.py (cube_units)."""
import sys, os, time, hashlib, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cnf106 as C
from pysat.solvers import Solver
import pysat

def cube_units(E, start, perm):
    rank = {q: i for i, q in enumerate(perm)}; u = [E.names[("R", 0, x)] * (1 if start[x] == "1" else -1) for x in range(4)]
    for q in range(4):
        for r in range(q + 1, 4): u.append(E.names[("GO", q, r)] * (1 if rank[q] < rank[r] else -1))
    return u

def path_units(E, path):
    """unit literals fixing R[1..len(path)] to the given 4-bit words"""
    return [E.names[("R", j + 1, x)] * (1 if w[x] == "1" else -1) for j, w in enumerate(path) for x in range(4)]

def cubes():
    for s in itertools.product("01", repeat=4):
        for p in itertools.permutations(range(4)): yield "".join(s), list(p)

if __name__ == "__main__":
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    E = C.build(L); n = 0
    for s, p in cubes(): E.add([-l for l in cube_units(E, s, p)]); n += 1
    os.makedirs("dump", exist_ok=True); path = "dump/cover%d.cnf" % L
    C.dimacs(E, path, ["L-SI box 106 cover106.py: cnf106.build(%d) + the negations of the %d cubes (start x level-0 gate order)" % (L, n)])
    sha = hashlib.sha1(open(path, "rb").read()).hexdigest()
    t0 = time.time(); s = Solver(name="glucose4", with_proof=True, bootstrap_with=E.cl); r = s.solve(); dt = time.time() - t0
    out = "COVER106 cover%d: query L* >= %d with %d cube negations: %s | vars %d clauses %d | cnf sha1 %s | solver glucose4 (python-sat %s) | %.1f s" % (
        L, L, n, "SAT" if r else "UNSAT", E.n, len(E.cl), sha, pysat.__version__, dt)
    if not r:
        pf = s.get_proof() or []
        with open("dump/cover%d.drup" % L, "w") as f:
            for line in pf: f.write(line + "\n")
        out += " | proof lines %d sha1 %s" % (len(pf), hashlib.sha1(open("dump/cover%d.drup" % L, "rb").read()).hexdigest())
    print(out, flush=True)
