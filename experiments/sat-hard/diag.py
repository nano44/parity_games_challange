#!/usr/bin/env python3
"""Least k for one cell (weak or strong, convention, alphabet {m..d}), searching k = KLO, KLO+1, ...
Writes out/cells/<tag>.json with the witness and the CNF path of the last UNSAT k (for LRAT proofs).
Usage: diag.py n d conv weak|strong [--min-letter m] [--klo K]"""
import sys, os, json, time, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import search
ap = argparse.ArgumentParser()
ap.add_argument("n", type=int); ap.add_argument("d", type=int); ap.add_argument("conv"); ap.add_argument("mode")
ap.add_argument("--min-letter", type=int, default=1); ap.add_argument("--klo", type=int, default=1)
a = ap.parse_args()
tag = f"{a.mode}_{a.conv}_n{a.n}_d{a.d}_m{a.min_letter}"
od = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "cells"); os.makedirs(od, exist_ok=True)
k, t0, last_unsat = a.klo, time.time(), None
while True:
    cnf = os.path.join(od, f"{tag}_k{k}.cnf")
    aut, used = search.run(a.n, a.d, k, cnf_out=cnf, conv=a.conv, strong=(a.mode == "strong"), min_letter=a.min_letter,
                           log=lambda s: print("  " + s[:150], flush=True))
    if aut:
        if os.path.exists(cnf): os.remove(cnf)
        break
    last_unsat = cnf; k += 1
res = {"cell": tag, "value": k, "klo": a.klo, "witness": aut, "unsat_cnf": last_unsat, "seconds": round(time.time() - t0, 1)}
json.dump(res, open(os.path.join(od, tag + ".json"), "w"), indent=1)
print(f"RESULT {tag}: {k} (lower bound needs UNSAT at k={k-1}: {last_unsat}) {res['seconds']}s", flush=True)
