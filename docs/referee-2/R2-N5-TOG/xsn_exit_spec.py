#!/usr/bin/env python3
"""REFEREE-2 succ. 7 (Lead request 10:06Z): find S4a crossings at the transition leaving an SN prefix on the SPEC trace. The STATE SEQUENCE
comes from experiments/new/n5.py via my lane's R2-N5-RE/re_check.n5_spec (read-only, SPEC tie-breaks, S3 start). Everything else (Xi, W,
H1-H3, R, phase) is my own analysis (R2-N5-FRZ/frz_check.analyse). Usage: xsn_exit_spec.py file.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC
tot = 0
for path in sys.argv[1:]:
    g = RC.parse(open(path).read()); o = FC.odd_vertex(g)
    s, t = FC.s3_start(g)
    states, fbs = RC.n5_spec(g, o, s, t)
    A = [FC.analyse(g, o, sg, tu) for sg, tu in states]
    for k in range(len(fbs)):
        a, b = A[k], A[k + 1]
        if a.lamX == b.lamX and a.tu[o] == b.tu[o] and fbs[k] == 0 and a.H3 and not b.H3 and a.Rr != b.Rr:
            tot += 1
            print(f"{os.path.relpath(path, os.path.join(HERE, '..', '..', '..'))}: SPEC trace ({len(fbs)} it / {sum(fbs)} fb), S4a {k}->{k+1}: "
                  f"H1,H2,H3 {a.H1},{a.H2},{a.H3} -> {b.H1},{b.H2},{b.H3}; entered {sorted(b.Rr - a.Rr)} left {sorted(a.Rr - b.Rr)}")
print("SPEC exit crossings", tot)
