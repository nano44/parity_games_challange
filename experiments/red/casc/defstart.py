#!/usr/bin/env python3
"""L-RED R148: write n5b's DEFAULT start (SPEC A2: best-reward sigma0 on G, tau0 on G^d) as a start file. Usage: defstart.py GAME.pg OUT.start"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "xcn"))
import xcn
n5b = xcn.n5b; g = xcn.pg.read(sys.argv[1]); N = n5b.N5(g)
s = N.SG.initial_strategy_by_best_reward(); t = N.SD.initial_strategy_by_best_reward()
with open(sys.argv[2], "w") as f:
    f.write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == 0) + "\n")
    f.write("TAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
