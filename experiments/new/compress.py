#!/usr/bin/env python3
"""Priority compression used by anneal.py (merge consecutive distinct priorities of equal parity). Usage: compress.py in.pg > out.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
cp = {}; cur = None; prev = None
for p in sorted(set(g.prio)):
    cur = p % 2 if prev is None else (cur + 1 if p % 2 != prev % 2 else cur)
    cp[p] = cur; prev = p
print(pg.dumps(pg.Game([cp[p] for p in g.prio], g.owner, g.succ)), end="")
