#!/usr/bin/env python3
"""REFEREE-2 succ. 7: print in-phase S4a crossings k -> k+1 with H3 (c_w = c_theta) at k and not at k+1, i.e. the transition leaving an
SN prefix: counted in X_SN (R30 (c)) but not among X-RUN'''s crossings "with both ends in P". Same runs as tog_check.py inst (seed 7).
Usage: xsn_exit_probe.py game.pg runs [--rand]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC
args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
g = RC.parse(open(args[0]).read()); o = FC.odd_vertex(g); rng = random.Random(7)
for r in range(int(args[1])):
    s0, t0 = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
    A, fbs = FC.run_n5(g, o, s0, t0, rng, rand)
    for k in range(len(fbs)):
        a, b = A[k], A[k + 1]
        if a.lamX == b.lamX and a.tu[o] == b.tu[o] and fbs[k] == 0 and a.H3 and not b.H3 and a.Rr != b.Rr:
            print(f"run {r}: S4a {k}->{k+1} in phase; H1,H2,H3 at k = {a.H1},{a.H2},{a.H3}; at k+1 = {b.H1},{b.H2},{b.H3};"
                  f" entered R {sorted(b.Rr - a.Rr)} left R {sorted(a.Rr - b.Rr)}; c_theta={a.theta[0]} c_w(k+1)={b.w[0]}")
