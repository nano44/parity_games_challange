#!/usr/bin/env python3
"""Box 10: along gen(n) (CDAG chain, p_strict/cdag.py), at each state list the CDAG-improving edges and the executed one, and test the
local rule R: for y < n, (y,w) executes iff tau(y+1) = w (and (y,w) improving); for the top n: (n,w) executes iff w = z-1 where z is the
largest z <= n-1 with tau(z) != z-1 (the counter rule). Also reports the masking load (improving edges not executed)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "p_strict"))
def gen(m):
    if m <= 1: return []
    out = [(m, m - 1)]
    for x, u in gen(m - 1):
        out += [(m, u), (m - 1, u), (m, m - 1)] if x == m - 1 else [(x, u)]
    return out
def pset(tau, v):
    P = set()
    while v != 0: P.add(v); v = tau[v]
    return P
def better(P, Q):  # P better than Q for the improver (Even-CDAG convention: smaller index more relevant, even = good)
    d = P ^ Q
    return bool(d) and min(d) in P
n = int(sys.argv[1]); tau = [0] * (n + 1); ok = True; load = []
for k, (x, u) in enumerate(gen(n)):
    imp = [(y, w) for y in range(1, n + 1) for w in range(y) if w != tau[y] and better(pset(tau, w) | {w} if w else set(), pset(tau, tau[y]) | ({tau[y]} if tau[y] else set()))]
    assert (x, u) in imp, (k, x, u, imp)
    load.append(len(imp) - 1)
    # rule R prediction
    pred = []
    for y in range(1, n):
        for w in range(y):
            if (y, w) in imp and tau[y + 1] == w: pred.append((y, w))
    z = max([z for z in range(1, n) if tau[z] != z - 1], default=None)
    if tau[n] != n - 1: pred.append((n, n - 1))
    elif z is not None and (n, z - 1) in imp: pred.append((n, z - 1))
    if pred != [(x, u)]:
        ok = False; print(f"step {k}: state {tau[1:]} executed {(x,u)} rule predicts {pred}; improving {imp}")
    tau[x] = u
print(f"n={n} steps={len(gen(n))} rule R + top counter rule exact at every step: {ok}; masking load mean {sum(load)/len(load):.2f} max {max(load)}")
