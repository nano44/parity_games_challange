#!/usr/bin/env python3
"""L-RED successor 23: intrinsic per-phase quantities (Lead 2026-10-28 21:27Z): PL = longest phase (tau and both cycle-node maps constant;
transitions inside it), SW = max over Even vertices of switches inside one phase. Usage: phsw.py GAME.pg START|S3 [...pairs]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace as T

def measure(g, start, cap=10 ** 5):
    states = []; T.run(g, start, cap=cap, log=lambda *a: None, states=states)
    E, Ed = T.Engine(g), T.Engine(T.dual(g)); n = g.n
    lam = [(t, tuple(x[0] for x in E.evaluate(s)[0]), tuple(x[0] for x in Ed.evaluate(t)[0])) for s, t in states]
    PL = SW = 0; arg = None; a = 0
    for k in range(1, len(states) + 1):
        if k == len(states) or lam[k] != lam[k - 1]:
            PL = max(PL, k - 1 - a)
            for v in range(n):
                if g.owner[v] != 0: continue
                c = sum(1 for t in range(a, k - 1) if states[t][0][v] != states[t + 1][0][v])
                if c > SW: SW, arg = c, (v, a, k - 1)
            a = k
    return PL, SW, arg, len(states) - 1

if __name__ == "__main__":
    a = sys.argv[1:]
    for i in range(0, len(a), 2):
        g = T.pg.parse("".join(l for l in open(a[i]) if not l.lstrip().startswith("%")))
        PL, SW, arg, it = measure(g, ({}, {}) if a[i + 1] == "S3" else T.readstart(a[i + 1]))
        print("%s n=%d iterations=%d PL=%d (%.2fn) SW=%d (vertex, phase)=%s" % (os.path.basename(a[i]), g.n, it, PL, PL / g.n, SW, arg))
