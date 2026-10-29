#!/usr/bin/env python3
"""L-SI box 31: per-transition view of one frozen W-phase [a, b]: switched Even vertices (old -> new), their basin (gate or U) before and
after, #W-changed vertices, #Xi-changed vertices, blocked edges (W-improving, not in I_sigma) count. Usage: look.py GAME START|- a b"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "root")); sys.path.insert(0, os.path.join(HERE, "..", "tord"))
from common import rows, load, readstart
from gates import basins
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if sys.argv[2] != "-" else None; a, b = int(sys.argv[3]), int(sys.argv[4])
E, R = rows(g, st, cap=b + 2); n = g.n
D = {u for u in range(n) if g.owner[u] == 1 and R[a]["sb"][u] != R[a]["t"][u]}
print("n", n, "D", sorted(D), "ranks", {d: E.rank[d] for d in D}, "lam(d)", {d: R[a]["W"][d][0] for d in D}, "tau", {d: R[a]["t"][d] for d in D}, "sb", {d: R[a]["sb"][d] for d in D})
for k in range(a, min(b, len(R) - 1)):
    A, B = R[k], R[k + 1]; F0, F1 = basins(A["wn"], D, n), basins(B["wn"], D, n)
    sw = [(v, A["s"][v], B["s"][v], F0[v], F1[v]) for v in range(n) if g.owner[v] == 0 and A["s"][v] != B["s"][v]]
    wc = sum(1 for v in range(n) if A["W"][v] != B["W"][v]); xc = sum(1 for v in range(n) if A["vs"][v] != B["vs"][v])
    s = tuple(A["s"]); blk = set(E.improving(s, A["W"])) - set(E.improving(s, A["vs"]))
    tr = sum(1 for v in range(n) if F0[v] != -1)
    print(k, "sw", sw, "Wch", wc, "Xch", xc, "blk", len(blk), sorted(blk)[:4], "|S|", tr, "W(d)", [A["W"][d] for d in D], "X(d)", [A["vs"][d] for d in D])
