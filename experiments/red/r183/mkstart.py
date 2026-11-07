#!/usr/bin/env python3
"""L-RED R183: write the default S3 start pair (n5x.start_pair) of G.pg as a START file. Usage: mkstart.py G.pg OUT.start"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, start_pair, Engine, dual
g = load(sys.argv[1]); s, t = start_pair(g, Engine(g), Engine(dual(g)), None)
with open(sys.argv[2], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
