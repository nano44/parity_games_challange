#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): (YZ)/(ACYC) fitness (l-alg c2e80e9, STEP5.md §6; Lead 09:04Z) using L-ALG's
dtl_yzclimb.fitness UNMODIFIED (imported read-only from LALG11_DIR >= c2e80e9): (max |Y_0 \\ Z_f| over P pieces, number of
Dom acceptances of a stored tangle using a vertex of old X or of an earlier top's part); (99, 0) = incomplete run.
Score: 1e12 incomplete + 1e11 excess + 1e8 min(straddles, 999). Order from DTL_ORDER. Usage: yzc.py G.pg ..."""
import sys, os
ld = os.path.join(os.environ["LALG11_DIR"], "experiments", "alg")
sys.path.insert(0, ld); sys.path.insert(0, os.path.join(ld, "..", "harness"))
import pg, dtl_yzclimb as YC

def measure(path): return YC.fitness(pg.read(path))

def score(path):
    ex, st = measure(path)
    if ex < 0: return -1
    if ex >= 99: return 10 ** 12
    return 10 ** 11 * ex + 10 ** 8 * min(st, 999)

if __name__ == "__main__":
    for f in sys.argv[1:]:
        print(os.path.basename(f), os.environ.get("DTL_ORDER", "stable"), measure(f))
