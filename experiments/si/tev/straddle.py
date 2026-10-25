#!/usr/bin/env python3
"""L-SI succ. 6, box 11: DATA for the straddling interval of a block (docs/si/N5-TEV-box11.md §5). For consecutive fallbacks k0 < k of a
scope run with M_k0 = M_k = L >= 0, r > L at k0+1 and r <= L at some state of (k0+1, k]: counts them, the rises (COARSE_L(θ) changes)
inside, and the length of the r = L stretch before k. Usage: straddle.py game.pg ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "coarse"))
from reltrace import *

def scan(g, name):
    o = odd_choice(g); assert o is not None
    assert sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) == 1
    runs, d_o, exits, out = runs_of(g, name); C = Counter(); ex = []
    for S in runs:
        fbs = [p for p, e in enumerate(S) if e["k"] == "F"]
        for p, p2 in zip(fbs, fbs[1:]):
            L = S[p]["M"]
            if L < 0 or S[p2]["M"] != L: continue
            C["block_int"] += 1
            if p + 1 > p2 or S[p + 1]["r"] <= L or all(S[u]["r"] > L for u in range(p + 1, p2 + 1)): continue
            C["straddle"] += 1; t1 = min(u for u in range(p + 1, p2 + 1) if S[u]["r"] <= L)
            rise = any(S[u]["lt"] > L for u in range(p + 1, p2))
            if rise: C["straddle_rise"] += 1; ex.append((name, S[p]["i"], S[p2]["i"], L, S[t1]["i"]))
            C["stretch_len_sum"] += p2 - t1 + 1
    return C, ex

if __name__ == "__main__":
    T = Counter(); X = []
    for p in sys.argv[1:]:
        c, e = scan(load(p), os.path.basename(p)); T.update(c); X += e
    print("TOTAL", dict(T))
    for e in X[:30]: print("  ", e)
