#!/usr/bin/env python3
"""L-RED R212 MODELCK: does a witness ladder (JSON with start) satisfy the r200 xcnf encoding? Fix every state variable st(t, v) along
the witness's r187/ideal.py run (t = 0..T) and every gate bit Gb as assumptions; one CaDiCaL call (env flags as for cubes.py, e.g.
SEGMAX=13 SYM0=1 SYMB=1). SAT = the encoding admits the witness's run (an encoding check; UNSAT would mean an encoding bug or a
violated side condition). Usage: modelck.py witness.json d t"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, "..", "r200"); sys.path[:0] = [R, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
os.environ.setdefault("TMIN", "1")
import xcnf, ideal
from pysat.solvers import Solver
G = json.load(open(sys.argv[1])); d, t = int(sys.argv[2]), int(sys.argv[3])
C, I = xcnf.build(dict(movers=[], gate=[], states=[[] for _ in range(t + 1)]), d); st, Gb = I["st"], I["Gb"]
S, _ = ideal.traj(G); assert len(S) - 1 >= t, "witness shorter than horizon"
a = []; bad = []
def lit(x, val):
    if isinstance(x, bool):
        if x != val: bad.append(1)
        return None
    return x if val else -x
for tt in range(t + 1):
    for v in range(G["N"]):
        if (tt, v) in st:
            l = lit(st[(tt, v)], bool(S[tt][v]))
            if l is not None: a.append(l)
for (l, k), var in Gb.items():
    x = lit(var, G["gate"][2 * l][k] < G["gate"][2 * l + 1][k])
    if x is not None: a.append(x)
if bad: print("MODELCK constant clash", len(bad)); sys.exit(1)
with Solver(name="cadical195", bootstrap_with=C.cl) as Sv:
    r = Sv.solve(assumptions=a); print("MODELCK", os.path.basename(sys.argv[1]), "d", d, "t", t, "assumptions", len(a), "SAT" if r else "UNSAT")
