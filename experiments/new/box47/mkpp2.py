#!/usr/bin/env python3
"""Box 47: cut a game to G^U at a state of its S3 run (every Odd v outside U fixed to tau_k(v)); write the 2-Odd-choice game and the
start pair (sigma_k, tau_k) as a .start file. Usage: mkpp2.py GAME.pg K u u2 OUT.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from n5x import load, step, start_pair, Engine, dual, pg
g = load(sys.argv[1]); K = int(sys.argv[2]); U = {int(sys.argv[3]), int(sys.argv[4])}; out = sys.argv[5]
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None)
for _ in range(K): r = step(g, E, Ed, s, t); s, t = r[0], r[1]
succ = [list(g.succ[v]) if (g.owner[v] == 0 or v in U) else [t[v]] for v in range(g.n)]
with open(out, "w") as f:
    f.write(f"parity {g.n - 1};\n")
    for v in range(g.n): f.write(f"{v} {g.prio[v]} {g.owner[v]} {','.join(map(str, succ[v]))};\n")
with open(out[:-3] + ".start", "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
