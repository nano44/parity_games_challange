#!/usr/bin/env python3
"""Dual game: owners swapped, priorities +1 (W_E of the dual = W_O of the input). Usage: dual.py game.pg > out.pg"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%")))
print(pg.dumps(pg.Game([p + 1 for p in g.prio], [1 - o for o in g.owner], g.succ)), end="")
