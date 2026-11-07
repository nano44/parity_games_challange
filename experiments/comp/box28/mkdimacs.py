#!/usr/bin/env python3
"""L-COMP box 28: write the DIMACS of one root cube (SYM=1, CUBE = start bits of movers 2..2d-1 from the cube id), exactly the clause
list box27/cnf.py builds (same text as box27/mkproof.py writes), and print its sha1. Usage: mkdimacs.py d L cube_id OUTDIR"""
import os, sys, hashlib
d, L, cid, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
os.environ["SYM"] = "1"; os.environ["CUBE"] = ",".join(f"{x}:{(cid >> i) & 1}" for i, x in enumerate(range(2, 2 * d)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box27")); import cnf
C, I = cnf.build(d, L, None, "R"); os.makedirs(out, exist_ok=True); fn = os.path.join(out, f"d{d}_L{L}_c{cid}.cnf")
with open(fn, "w") as f:
    f.write(f"p cnf {C.n} {len(C.cl)}\n")
    for c in C.cl: f.write(" ".join(map(str, c)) + " 0\n")
print(f"cube {cid} CUBE {os.environ['CUBE']} cnf {fn} sha1 {hashlib.sha1(open(fn, 'rb').read()).hexdigest()} vars {C.n} clauses {len(C.cl)}", flush=True)
