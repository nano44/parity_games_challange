#!/usr/bin/env python3
"""Box 32: list every experiments/**/*.pg in 𝒞^1O (exactly one Odd vertex with out-degree > 1), n <= NMAX. Usage: c1o_list.py NMAX"""
import sys, os, glob
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments/harness"))
import pg
nmax = int(sys.argv[1])
for f in sorted(glob.glob(os.path.join(ROOT, "experiments/**/*.pg"), recursive=True)):
    try: g = pg.load(f) if hasattr(pg, "load") else pg.read(f)
    except Exception: continue
    if g.n <= nmax and sum(1 for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) > 1) == 1: print(os.path.relpath(f, ROOT), g.n)
