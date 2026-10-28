#!/usr/bin/env python3
"""Replay offmono_check.py's 'random N nmin nmax seed k ns' generator and save game i with start r as <out>.pg / <out>.start."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND")); import rund_check as R
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
DC = R.DC
nmin, nmax, seed, k, ns, I, RR, out = map(str, sys.argv[1:9]); nmin, nmax, seed, k, ns, I, RR = map(int, (nmin, nmax, seed, k, ns, I, RR))
srng = random.Random(seed)
for i in range(I + 1):
    nn = srng.randint(nmin, nmax)
    gp = DC.rand_game(srng, nn, "kO") if k == 0 else H3.rand_kO(srng, nn, k)
    for r in range(ns):
        s, t = R.starts(gp, r, srng)
        if i == I and r == RR:
            with open(out + ".pg", "w") as fh:
                fh.write(f"parity {gp.n - 1};\n")
                for v in range(gp.n): fh.write(f"{v} {gp.prio[v]} {gp.owner[v]} {','.join(map(str, gp.succ[v]))};\n")
            with open(out + ".start", "w") as fh:
                fh.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(gp.n) if gp.owner[v] == 0) + "\n")
                fh.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(gp.n) if gp.owner[v] == 1) + "\n")
            sys.exit(0)
