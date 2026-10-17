#!/usr/bin/env python3
"""For every finished cell (out/cells/*.json): LRAT proof of the UNSAT at value-1 (CaDiCaL 1.7.3 -> lrat_check.py)
plus CryptoMiniSat on the same CNF; writes results/cells.md (table). Value-1 = 0 needs no proof.
Usage: prove.py [cell-glob]"""
import sys, os, json, glob, subprocess, hashlib
H = os.path.dirname(os.path.abspath(__file__))
rows = []
for f in sorted(glob.glob(os.path.join(H, "out", "cells", (sys.argv[1] if len(sys.argv) > 1 else "*") + ".json"))):
    c = json.load(open(f))
    cnf = c["unsat_cnf"]
    if cnf is None:
        ev = "value 1 (k=0 impossible): no proof needed" if c["value"] == 1 else f"NO LOWER-BOUND PROOF (search started at k={c['klo']})"
    else:
        pr = cnf + ".lrat"
        r = subprocess.run(["cadical", "-q", "--lrat=true", "--binary=false", cnf, pr], capture_output=True, text=True)
        chk = subprocess.run([sys.executable, os.path.join(H, "lrat_check.py"), cnf, pr], capture_output=True, text=True)
        cms = subprocess.run(["cryptominisat5", "--verb", "0", cnf], capture_output=True, text=True)
        cmsr = "UNSAT" if "s UNSATISFIABLE" in cms.stdout else "??"
        sha = hashlib.sha256(open(cnf, "rb").read()).hexdigest()[:16]
        ev = f"k={c['value']-1} UNSAT: cadical exit {r.returncode}, {chk.stdout.strip()}, CryptoMiniSat {cmsr}, CNF sha256 {sha}"
        os.remove(pr)
    rows.append((c["cell"], c["value"], ev, json.dumps(c["witness"]["delta"])))
    print(c["cell"], c["value"], ev, flush=True)
with open(os.path.join(H, "results", "cells.md"), "a") as out:
    for r in rows:
        out.write(f"| {r[0]} | {r[1]} | {r[2]} | `{r[3]}` |\n")
