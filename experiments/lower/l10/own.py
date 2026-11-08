#!/usr/bin/env python3
"""L-LOWER 10: own-feasibility per mover: solve only the constraints of mover x (its chains as wired, the full clamped trajectory).
Usage: own.py D28 D32 -> per mover: #constraints, own-feasible or core size."""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from build import *
def ownrep(D, CT, movers=None):
    S, E = fulltraj(D, CT); cons = constraints(E, S); out = {}
    for x in (movers or range(2 * E['d'])):
        cx = [c for c in cons if c[1] == x]
        if not cx: continue
        res, core = solve(cx, 4 * E['d']); out[x] = (len(cx), None if res else len(core))
    return out, S, E, cons
if __name__ == '__main__':
    D28 = rd(sys.argv[1]); D = fixgates(rd(sys.argv[2])); CT = core8(D28)
    out, S, E, cons = ownrep(D, CT)
    print('own-infeasible:', [(x, n, c) for x, (n, c) in out.items() if c is not None])
    print('moves per helper 16..63:', [sum(1 for t in range(1, len(S)) if S[t][x] != S[t-1][x]) for x in range(16, 64)])
