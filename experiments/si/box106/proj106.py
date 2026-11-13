#!/usr/bin/env python3
"""L-SI box 106 §3d (SEARCH tool): the REALISABLE availability patterns of a set of states: every assignment of the 4·|states| AV bits
that some genome realises (cnf106.build(None, states, run=False), cadical195, enumeration with blocking clauses on the AV bits).
Usage: proj106.py STATE... (4-bit words); prints one line «PROJ106 states …: realisable K of 2^n | list» and writes out/proj/<states>.json"""
import sys, os, json, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cnf106 as C
from pysat.solvers import Solver

def proj(states):
    states = sorted(set(tuple(s) for s in states)); E = C.build(None, states=states, run=False)
    V = [E.names[("AV", S, x)] for S in states for x in range(4)]; s = Solver(name="cadical195", bootstrap_with=E.cl); out = []
    while s.solve():
        m = set(l for l in s.get_model() if l > 0); a = [int(v in m) for v in V]; out.append(a)
        s.add_clause([(-v if b else v) for v, b in zip(V, a)])
    return states, out

if __name__ == "__main__":
    t0 = time.time(); st, out = proj([tuple(int(c) for c in w) for w in sys.argv[1:]])
    os.makedirs("out/proj", exist_ok=True); name = "-".join("".join(map(str, S)) for S in st)
    json.dump({"states": st, "realisable": out}, open("out/proj/%s.json" % name, "w"))
    print("PROJ106 states %s: realisable %d of %d | %.1f s" % (name, len(out), 2 ** (4 * len(st)), time.time() - t0), flush=True)
