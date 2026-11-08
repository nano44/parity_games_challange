#!/usr/bin/env python3
"""L-RED 60 R226: A score (max(1, maxalt), #tops, T) on own.py; shared by tower226.py / tower2_226.py."""
import sys, os
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r225"), os.path.join(H, "..", "r221")]
import own
from asc226 import alt
def ascore(G, cap=3000):
    out, V, O, ow = own.run(G, cap); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    T = len(out) - 1; best = (0, 0)
    for v in range(n):
        t = 0
        while t <= T:
            u = t
            while u + 1 <= T and out[u + 1][1][v][0] == out[t][1][v][0]: u += 1
            prev = None; tops = []
            for i in range(t, u + 1):
                E = frozenset(e for e in out[i][1][v][1] if e in evs)
                if prev is not None and E != prev: tops.append(max(E ^ prev, key=lambda e: rk[e]))
                prev = E
            if tops: best = max(best, (max(1, alt(tops)), len(tops)))
            t = u + 1
    return best[0], best[1], T
