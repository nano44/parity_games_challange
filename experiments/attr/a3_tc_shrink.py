#!/usr/bin/env python3
"""Shrink the Two Counters game tc N (Oink generator) under the predicate "psolC decides nothing", to find the smallest
tc-type obstruction. Usage: a3_tc_shrink.py N  -> instances/tc{N}_psolc_nothing_n*_m*.pg and a trace on stdout."""
import sys, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "harness"))
import pg, a1lib, zielonka
from psolc import PsolC
N = int(sys.argv[1])
gen = os.path.join(HERE, "..", "..", "tools", "oink", "build", "tc")
g = pg.parse(subprocess.run([gen, str(N)], capture_output=True, text=True, check=True).stdout)
def nothing(h):
    w, _, res, _ = PsolC(h, strat=None).run()
    return len(res) == h.n
print(f"tc {N}: n={g.n} m={g.m}, psolC decides nothing: {nothing(g)}", flush=True)
h = a1lib.shrink(g, nothing)
ref = zielonka.solve(h)
name = f"tc{N}_psolc_nothing_n{h.n}_m{h.m}"
pg.write(h, os.path.join(HERE, "instances", name + ".pg"))
print(f"shrunk to n={h.n} m={h.m}: {pg.dumps(h).replace(chr(10), ' | ')} ref={ref}")
