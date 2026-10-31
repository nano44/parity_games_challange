#!/usr/bin/env python3
"""L-RED successor 38 (R164): N5 started from (best-reward sigma, tau*), where tau* = n5b SPEC's final tau from the best-reward start.
tau* has no Odd improving edge, so tau never moves: the whole run is S4a against tau* (one W-world) plus fallbacks. A legitimate N5
run (any start pair). Writes OUT.start (validated with startck) and prints both runs' iterations / fallbacks.
Usage: taustar.py G.pg OUT.start"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "n5-second")); sys.path.insert(0, os.path.join(HERE, "..", "startck"))
import n5b, startck
g = n5b.pg.read(sys.argv[1]); N = n5b.N5(g); N.mode = "spec"; tr, fb = [], []; N.run(None, None, trace=tr, fbtrace=fb)
s0, _ = tr[0]; _, tfin = tr[-1]
with open(sys.argv[2], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{tfin[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
bad = startck.check(sys.argv[1], sys.argv[2])
s1, t1 = n5b.read_start(sys.argv[2], g); M = n5b.N5(g); M.mode = "spec"; tr2, fb2 = [], []; M.run(s1, t1, trace=tr2, fbtrace=fb2)
moved = sum(1 for a, b in zip(tr2, tr2[1:]) if a[1] != b[1])
print(f"TAUSTAR {os.path.basename(sys.argv[1])} n {g.n} best-reward: iters {len(tr) - 1} fb {sum(fb)} | (sigma0, tau*): iters {len(tr2) - 1} fb {sum(fb2)} tau-moves {moved} start {'OK' if not bad else bad[:2]}")
