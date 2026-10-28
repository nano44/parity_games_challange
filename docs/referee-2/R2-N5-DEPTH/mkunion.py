#!/usr/bin/env python3
"""Disjoint union of a game with a start file and a small 2-vertex Even-only class {p, q} (p: Even, priority 2, self-loop;
q: Even, priority 0, edge to p). Usage: mkunion.py game.pg game.start out_stem"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND")); import rund_check as R
g = R.pg.read(sys.argv[1]); s, t = R.read_start(g, sys.argv[2]); out = sys.argv[3]; n = g.n
p, q = n, n + 1
with open(out + ".pg", "w") as fh:
    fh.write(f"parity {n + 1};\n")
    for v in range(n): fh.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, g.succ[v]))};\n")
    fh.write(f"{p} 2 0 {p};\n{q} 0 0 {p};\n")
with open(out + ".start", "w") as fh:
    fh.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(n) if g.owner[v] == 0) + f" {p}:{p} {q}:{p}\n")
    fh.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(n) if g.owner[v] == 1) + "\n")
