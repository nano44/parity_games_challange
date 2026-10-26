#!/usr/bin/env python3
"""REFEREE-2 succ. 7: print every in-phase S4c fallback s -> s+1 with H1 and not-H2 at s and H2 at s+1 (P-N5-L2 §8 open item (2)), with
the switched edges, tau(o), R membership, and whether the state after has (h). Same runs as l2_check.py inst (seed 7, starts S3 + random).
Usage: restart_probe.py game.pg runs [--rand]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC
args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
g = RC.parse(open(args[0]).read()); o = FC.odd_vertex(g); rng = random.Random(7)
for r in range(int(args[1])):
    s0, t0 = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
    A, fbs = FC.run_n5(g, o, s0, t0, rng, rand)
    for s in range(len(fbs)):
        a, b = A[s], A[s + 1]
        if a.lamX == b.lamX and a.tu[o] == b.tu[o] and fbs[s] and a.H1 and not a.H2 and b.H2:
            sw = [(y, a.sg[y], b.sg[y]) for y in range(g.n) if a.sg[y] != b.sg[y]]
            print(f"run {r} ({'S3' if r == 0 else 'random'} start, {'--rand' if rand else 'det'}) fallback {s}->{s+1}: o={o} tau(o)={a.tu[o]}"
                  f" tau(o) in R_s={a.tu[o] in a.Rr} in R_s+1={a.tu[o] in b.Rr}; H1,H2,H3 at s+1 = {b.H1},{b.H2},{b.H3};"
                  f" switched (y, old, new) {sw}; theta_s={a.theta[0]},{sorted(a.theta[1])},{a.theta[2]} w_s={a.w[0]},{sorted(a.w[1])},{a.w[2]}"
                  f" ; w_s+1={b.w[0]},{sorted(b.w[1])},{b.w[2]}; |R| {len(a.Rr)} -> {len(b.Rr)}")
