#!/usr/bin/env python3
"""Check a solution: regions equal Zielonka and strategies pass harness/verify.py. Usage: check_sol.py game.pg sol -> 'zielonka OK strategies verified' or the failure."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg, zielonka, verify
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); text = open(sys.argv[2]).read()
win = pg.read_sol(text, g.n); e = verify.check(g, win, verify.read_strategy(text, g.n))
print("zielonka " + ("OK" if win == zielonka.solve(g) else "MISMATCH") + (" strategies verified" if not e else " STRATEGY FAIL " + e[0]))
