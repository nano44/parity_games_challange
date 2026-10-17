#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): (NT-f) fitness (l-alg 4841576, docs/alg/STEP5.md §5; Lead 08:42Z): the FINAL
pruning round of a -1 call accepts no stored tangle in its region loop. Uses L-ALG's dtl_ntfclimb.fitness UNMODIFIED
(imported read-only from LALG9_DIR >= 4841576): the largest r/f over -1 calls such that round r's region loop accepts a
tangle none of whose p-priority vertices is in V_r; 1.0 = an (NT-f) violation, 2.0 = an incomplete run.
Score: 1e12 incomplete + 1e11 violation + int(1e9 * r/f). Order from DTL_ORDER. Usage: ntf.py G.pg ..."""
import sys, os
ld = os.path.join(os.environ["LALG9_DIR"], "experiments", "alg")
sys.path.insert(0, ld); sys.path.insert(0, os.path.join(ld, "..", "harness"))
import pg, dtl_ntfclimb as NC

def measure(path): return NC.fitness(pg.read(path))

def score(path):
    f = measure(path)
    if f < 0: return -1
    return 10 ** 12 * (f >= 2.0) + 10 ** 11 * (1.0 <= f < 2.0) + int(10 ** 9 * min(f, 1.0))

if __name__ == "__main__":
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
