#!/usr/bin/env python3
"""Box 21: per-iteration analysis of an N5 run (n5x.trace): which player moves, fallback, honest Ξσ/Ξτ change (value-changing),
W = play values against the current tau change. Usage: anal.py game.pg [tstar]"""
import sys
from n5x import *
def main(path, mode=""):
    g = load(path); E, Ed = Engine(g), Engine(dual(g))
    states, fb = trace(g)
    if mode == "tstar":
        s0, ts = states[0][0], states[-1][1]
        st = ({v: s0[v] for v in range(g.n) if g.owner[v] == 0}, {v: ts[v] for v in range(g.n) if g.owner[v] == 1})
        states, fb = trace(g, st)
    rows = []
    for k in range(len(states) - 1):
        (s, t), (s2, t2) = states[k], states[k + 1]
        vs, _ = E.evaluate(s); vs2, _ = E.evaluate(s2); vt, _ = Ed.evaluate(t); vt2, _ = Ed.evaluate(t2)
        ev = [v for v in range(g.n) if s[v] != s2[v]]; od = [v for v in range(g.n) if t[v] != t2[v]]
        Is = E.improving(s, vs)
        rows.append((k, ev, od, vs != vs2, vt != vt2, len(Is)))
        print(f"it {k+1}: Even moves {ev} Odd moves {od} |Iσ|={len(Is)} Ξσ-chg={int(vs != vs2)} Ξτ-chg={int(vt != vt2)}")
    print(f"total {len(states)-1} fb {fb} Ξσ-changing {sum(r[3] for r in rows)} Ξτ-changing {sum(r[4] for r in rows)}")
if __name__ == "__main__": main(*sys.argv[1:])
