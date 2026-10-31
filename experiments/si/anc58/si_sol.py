#!/usr/bin/env python3
"""L-SI box 58: classical switch-all SI (si.py, best-reward start) to the end; write its solution (Engine.regions) for check_sol2.py.
Usage: si_sol.py GAME.pg OUT.sol -> prints the iteration count."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("..", "../../harness"): sys.path.insert(0, os.path.join(HERE, p))
import pg
from si import Engine
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); E = Engine(g)
st, it = E.run(E.rule_switch_all, E.initial("best")); win, ws = E.regions(st)
pg.write_sol(win, sys.argv[2], ws); print(os.path.basename(sys.argv[1]), "iterations", it)
