#!/usr/bin/env python3
"""Planted-defect solver for bench self-checks: runs pinned DTL, then corrupts the solution.
Usage: plant.py region|strategy IN OUT. region: flip vertex 0's winner, keep strategies. strategy: for the first winner-owned
vertex with another successor, point the strategy at a different successor that loses (if any), else any other one."""
import sys, os, subprocess, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg, verify, solvers
kind, gin, gout = sys.argv[1:4]
g = pg.read(gin)
with tempfile.TemporaryDirectory() as td:
    o = os.path.join(td, "s")
    subprocess.run([solvers.OINK, "--dtl", "--no-single", "--no-wcwc", "--no-loops", gin, o], capture_output=True, check=True)
    text = open(o).read()
win = pg.read_sol(text, g.n); st = verify.read_strategy(text, g.n)
if kind == "region":
    win[0] = 1 - win[0]
else:
    for v in range(g.n):
        if g.owner[v] == win[v]:
            alts = [w for w in set(g.succ[v]) if w != st[v]]
            bad = [w for w in alts if verify.check(g, win, st[:v] + [w] + st[v + 1:])]
            if bad:
                st[v] = bad[0]; break
pg.write_sol(win, gout, st)
