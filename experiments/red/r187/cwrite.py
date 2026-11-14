#!/usr/bin/env python3
"""L-RED R187: write a CROOT state (json from cclimb.py) as G.pg + G.start. Usage: cwrite.py state.json out_prefix"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H]
import croot, stab
s = json.load(open(sys.argv[1])); g, sig, tau, c = croot.build(s["G"], s["copt"], s["cstart"]); stab.write(g, sig, tau, sys.argv[2])
print("n", g.n, "c", c, croot.measure(g, sig, tau, c))
