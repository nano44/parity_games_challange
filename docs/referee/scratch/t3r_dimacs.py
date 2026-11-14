#!/usr/bin/env python3
"""REFEREE successor 24: build the 16 d = 3, T >= 9 cube CNFs of L-COMP box 27 cnf.py (6f19564f) exactly as cubes.sh does and print
vars, clauses, empty/unit clause counts and the DIMACS sha1 of each (no solving). Usage: CNFDIR=<dir> python3 -I t3r_dimacs.py"""
import hashlib, os, sys
sys.path.insert(0, os.environ["CNFDIR"])
for v in ("FREE0", "ISO", "KF", "P"):
    os.environ.pop(v, None)
import cnf
for c in range(16):
    os.environ["SYM"] = "1"
    os.environ["CUBE"] = "".join(f"{i + 2}:{(c >> i) & 1}," for i in range(4))
    C, I = cnf.build(3, 9, None, "R")
    txt = f"p cnf {C.n} {len(C.cl)}\n" + "".join(" ".join(map(str, cl)) + " 0\n" for cl in C.cl)
    print(c, os.environ["CUBE"], "vars", C.n, "clauses", len(C.cl), "empty", sum(1 for x in C.cl if not x),
          "units", sum(1 for x in C.cl if len(x) == 1), "sha1", hashlib.sha1(txt.encode()).hexdigest(), flush=True)
