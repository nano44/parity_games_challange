#!/usr/bin/env python3
"""Write the FULL start pair (every vertex) that n5x.start_pair uses for GAME + partial START. Usage: fullstart.py GAME START OUT"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x
g = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2])
E, Ed = n3x.Engine(g), n3x.Engine(n3x.dual(g)); s, t = n3x.start_pair(g, E, Ed, st)
open(sys.argv[3], "w").write("SIGMA0 " + " ".join(f"{v}:{s[v]}" for v in range(g.n) if g.owner[v] == 0) + "\nTAU0 " + " ".join(f"{v}:{t[v]}" for v in range(g.n) if g.owner[v] == 1) + "\n")
