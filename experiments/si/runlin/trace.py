#!/usr/bin/env python3
"""L-SI box 24 (successor 20): trace the longest fallback-free run of a game (RUN-LIN, docs/si/N5-RUNLIN-box24.md).
Per transition: the Even switches (v: old -> new), sigma-bar on Odd choice vertices, and per switch whether v's honest / W play meets D.
Usage: trace.py G.pg [G.start|-]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root"))
from common import rows, phases, load, readstart, Dset

def runs(R):
    for i, j in phases(R):
        s0 = i
        for k in range(i, j + 1):
            if k == j or R[k]["fb"]:
                yield (s0, k, i, j); s0 = k + 1

def main():
    g = load(sys.argv[1]); st = None
    if len(sys.argv) > 2 and sys.argv[2] != "-": st = readstart(sys.argv[2])
    E, R = rows(g, st)
    best = max(runs(R), key=lambda r: r[1] - r[0])
    a, b, i, j = best
    print("phase", (i, j), "run", (a, b), "len", b - a, "n", g.n)
    odd = [u for u in range(g.n) if g.owner[u] == 1 and len(g.succ[u]) > 1]
    for k in range(a, b):
        A, B = R[k], R[k + 1]
        sw = [(v, A["s"][v], B["s"][v]) for v in range(g.n) if g.owner[v] == 0 and A["s"][v] != B["s"][v]]
        print(k, "sb", [A["sb"][u] for u in odd], "t", [A["t"][u] for u in odd], "sw", " ".join("%d:%d>%d" % x for x in sw))

if __name__ == "__main__":
    main()
