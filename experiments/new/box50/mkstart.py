#!/usr/bin/env python3
"""L-NEW box 50: write the S3 (best-reward) start pair of a game as a .start file (SIGMA0 / TAU0 lines), for two-engine checks.
Usage: mkstart.py GAME.pg OUT.start"""
import sys, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, load
g = load(sys.argv[1]); E, R = rows(g, None, cap=0); s, t = R[0]["s"], R[0]["t"]
with open(sys.argv[2], "w") as f:
    f.write("SIGMA0 " + " ".join("%d:%d" % (v, s[v]) for v in range(g.n) if g.owner[v] == 0) + "\n")
    f.write("TAU0 " + " ".join("%d:%d" % (v, t[v]) for v in range(g.n) if g.owner[v] == 1) + "\n")
