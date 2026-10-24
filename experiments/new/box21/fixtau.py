#!/usr/bin/env python3
"""Box 21 probe E1: N5 with Odd frozen at an honest-optimal tau* (Iτ* = ∅, so Odd never moves; N5's own loop, unmodified).
tau* = the final tau of the plain N5 run. sigma_0 = the plain run's sigma_0. Prints plain N5 iterations, frozen-tau* iterations,
and Even switch-all SI (si.py rule_switch_all) from the same sigma_0, for comparison.
Usage: fixtau.py game.pg [--start file]"""
import sys
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))  # box21 -I: find sibling modules
from n5x import *
def main(path, startf=None):
    g = load(path); st = readstart(startf) if startf else None
    states, fb = trace(g, st)
    E, Ed = Engine(g), Engine(dual(g))
    s0 = states[0][0]; tstar = states[-1][1]
    vt, _ = Ed.evaluate(tstar); assert not Ed.improving(tstar, vt)
    fst = ({v: s0[v] for v in range(g.n) if g.owner[v] == 0}, {v: tstar[v] for v in range(g.n) if g.owner[v] == 1})
    fstates, ffb = trace(g, fst)
    assert all(t == tstar for _, t in fstates)
    _, sa = E.run(E.rule_switch_all, s0)
    print(f"{path.split('/')[-1]} n={g.n} plain={len(states)-1} (fb {fb}) frozen_tau*={len(fstates)-1} (fb {ffb}) evenSA_from_s0={sa}", flush=True)
if __name__ == "__main__":
    a = sys.argv[1:]; sf = a[a.index("--start") + 1] if "--start" in a else None
    main(a[0], sf)
