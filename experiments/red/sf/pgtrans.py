#!/usr/bin/env python3
"""L-RED: PGSolver's SI preprocessing (pgsolver_si.py: alternating_transformation, cheap_escape_cycles_transformation, as
solve_switchbest) applied to a game; writes GAME' and a start file with sigma_0 = PGSolver's initial_strategy_by_last_edge on G'
(Odd's tau_0 is left to the engine's S3 default: Even's distinct-sigma sequence does not depend on it, DECOUPLE).
Usage: pgtrans.py IN.pg OUT.pg OUT.start"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "hard-families"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "harness"))
import pg
from pgsolver_si import SI, alternating_transformation, cheap_escape_cycles_transformation
g = pg.read(sys.argv[1]); g2 = cheap_escape_cycles_transformation(alternating_transformation(g))
with open(sys.argv[2], "w") as f:
    f.write(f"parity {g2.n - 1};\n")
    for v in range(g2.n):
        f.write(f"{v} {g2.prio[v]} {g2.owner[v]} {','.join(map(str, g2.succ[v]))};\n")
s = SI(g2).initial_strategy_by_last_edge()
with open(sys.argv[3], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g2.n) if g2.owner[v] == 0) + "\n")
