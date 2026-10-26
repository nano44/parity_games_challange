#!/usr/bin/env python3
"""REFEREE succ. 16: the INTERVAL-LEVEL reading of P-N5-GCX §1 "every Delta_t(u), u in DD_t, is constant" on one run: an interval [s, e]
qualifies iff every transition keeps A non-increasing (every class) and D constant, and for every gate u the values Delta_t(u) over the
states t in [s, e] with u in DD_t are all equal. Prints the maximal qualifying intervals, K_lit (transitions in none) and the count
check len(maximal) <= K_lit + 1 used by Corollary UL-RED (a). Usage: gcx_literal.py game.pg (start-file | S3) a b"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, epr_probe as E
from root_probe import firstD
g = RE.parse(sys.argv[1]); a, b = int(sys.argv[3]), int(sys.argv[4]); n = g.n
from gcx_probe import load_start
st = RE.run(g, load_start(g, sys.argv[2]) if sys.argv[2].endswith(".start") else RE.best_reward_start(g)); Q = {v for v in range(n) if g.owner[v] == 1}
for x in st:
    x["D"] = frozenset(u for u in Q if x["sb"][u] != x["t"][u]); x["fu"] = [firstD(g, x["s"], x["t"], x["D"], v) for v in range(n)]
lam = tuple(v[0] for v in st[a]["Xi"]); tau = st[a]["t"]
assert all(tuple(v[0] for v in st[t]["Xi"]) == lam and st[t]["t"] == tau for t in range(a, b + 1)) and not any(st[t]["fb"] for t in range(a, b))
M = lambda t, z: g.weight(st[t]["Xi"][z][1])
cls = sorted(set(lam)); U = {c: {v for v in range(n) if lam[v] == c} for c in cls}
A = {(c, t): {v for v in U[c] if st[t]["fu"][v] is None} for c in cls for t in range(a, b + 1)}
DD = {t: {u: M(t, tau[u]) - M(t, st[t]["sb"][u]) for c in cls for u in st[t]["D"] if u in U[c] and st[t]["sb"][u] in A[c, t] and tau[u] in A[c, t]} for t in range(a, b + 1)}
def ok(s, e):
    for t in range(s, e):
        if st[t]["D"] != st[t + 1]["D"] or any(not A[c, t + 1] <= A[c, t] for c in cls): return False
    vals = {}
    for t in range(s, e + 1):
        for u, d in DD[t].items():
            if vals.setdefault(u, d) != d: return False
    return True
good = [(s, e) for s in range(a, b + 1) for e in range(s + 1, b + 1) if ok(s, e)]
maxi = [(s, e) for (s, e) in good if not any((s2 <= s and e <= e2 and (s2, e2) != (s, e)) for (s2, e2) in good)]
covered = {t for (s, e) in maxi for t in range(s, e)}
K = sum(1 for t in range(a, b) if t not in covered)
print("states", a, b, "maximal intervals", maxi, "K_lit", K, "count <= K_lit + 1:", len(maxi) <= K + 1)
for t in range(a, b + 1): print(" t", t, "DD", sorted(DD[t].items()))
