#!/usr/bin/env python3
"""Run L-SI's frame.py (read-only copy lsi/frame.py) only up to its DIMACS dump (no solve). Usage: DUMP=dir [K=..] lsi_dimacs.py m MODE T [T2]"""
import sys, os
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lsi", "frame.py")).read()
cut = src.index("t0 = time.time()\nfrom pysat.solvers import Solver")
sys.argv = ["frame.py"] + sys.argv[1:]
exec(compile(src[:cut], "lsi/frame.py", "exec"), {"__name__": "__main__"})
