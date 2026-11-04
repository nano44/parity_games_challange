#!/usr/bin/env python3
"""L-RED R200 PROPCK: exact check of fixed extra-level proposals (r199 cegar2/hunt blocks: moves, start, gate bits) in the xcnf model by
assumptions; UNSAT gives a core over the proposal's literals (a generalised no-good). Usage: propck.py target.json E blocks.json i0 i1"""
import sys, os, json, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H]
import xcnf
from pysat.solvers import Solver
T = json.load(open(sys.argv[1])); E = int(sys.argv[2]); B = json.load(open(sys.argv[3])); i0, i1 = int(sys.argv[4]), int(sys.argv[5])
C, I = xcnf.build(T, E); N0, N, L = I["N0"], I["N"], I["L"]
def lits(P):
    out = []
    for v in range(N0, N):
        s = P["start"][str(v)]; mv = set(P["moves"].get(str(v), []))
        for t in range(L + 1):
            if t > 0 and t in mv: s ^= 1
            out.append(I["st"][(t, v)] if s else -I["st"][(t, v)])
    for (l, k), var in I["Gb"].items(): out.append(var if P["G"][f"{l},{k}"] else -var)
    return out
with Solver(name=os.environ.get("SOLVER", "cadical195"), bootstrap_with=C.cl) as S:
    for i in range(i0, min(i1, len(B))):
        a = lits(B[i]); t0 = time.time(); r = S.solve(assumptions=a)
        core = S.get_core() if not r else None
        print(f"proposal {i}: {'SAT' if r else 'UNSAT'} {time.time() - t0:.1f} s core {len(core) if core else '-'} of {len(a)}", flush=True)
