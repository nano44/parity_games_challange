#!/usr/bin/env python3
"""Box 21: λ-phases of an N5 run (honest cycle-node maps of Ξσ and Ξτ), iterations per joint phase, best-reply (σ̄) changes.
Usage: phases.py game.pg [tstar]"""
import sys
import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__)))  # box21 -I: find sibling modules
from n5x import *
def main(path, mode=""):
    g = load(path); E, Ed = Engine(g), Engine(dual(g))
    states, fb = trace(g)
    if mode == "tstar":
        s0, ts = states[0][0], states[-1][1]
        st = ({v: s0[v] for v in range(g.n) if g.owner[v] == 0}, {v: ts[v] for v in range(g.n) if g.owner[v] == 1})
        states, fb = trace(g, st)
    lam, sb = [], []
    for s, t in states:
        vs, sbar = E.evaluate(s); vt, _ = Ed.evaluate(t)
        lam.append((tuple(x[0] for x in vs), tuple(x[0] for x in vt))); sb.append(tuple(sbar))
    ph = [0]
    for k in range(1, len(states)):
        ph.append(ph[-1] + (lam[k] != lam[k - 1]))
    from collections import Counter
    c = Counter(ph[1:]); print("iterations per joint λ-phase:", [c[i] for i in sorted(c)])
    print("σ̄ changes:", sum(sb[k] != sb[k - 1] for k in range(1, len(sb))), "of", len(states) - 1)
    seg = [0]
    for k in range(1, len(states)): seg.append(seg[-1] + (sb[k] != sb[k - 1] or lam[k] != lam[k - 1]))
    c2 = Counter(seg[1:]); print("iterations per (σ̄-segment ∩ λ-phase):", [c2[i] for i in sorted(c2)])
    print("raw val[0] of Ξσ at start:", E.evaluate(states[0][0])[0][:3])
if __name__ == "__main__": main(*sys.argv[1:])
