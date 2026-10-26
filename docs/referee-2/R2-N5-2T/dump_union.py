#!/usr/bin/env python3
"""REFEREE-2 succ. 14: write tt_check.gadget(base, kind, P) unions as .pg files. Usage: dump_union.py base.pg kind P out.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tt_check as TT
base, kind, P, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4]
g = TT.gadget(TT.pg.read(os.path.join(TT.DC.ROOT, base)), kind, P)
open(out, "w").write(TT.pg.dumps(g))
