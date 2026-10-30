#!/usr/bin/env python3
"""L-NEW box 82 (R2-POLY): exhaustive R2 search on the abstract Odd-gated ladder (k <= 3). Usage: r2search.py K"""
# R2 search on the Odd-gated ladder ogl_k: reader v (level j+1 vertex or T) -> Odd gates o(v,0), o(v,1); o(v,c) -> {u(j,c) [tau], u(j,1-c)}.
# Gates are less relevant than the sink cycle node (not in path sets); all paths equal length. Abstract value: ladder copy bits deep-first.
# R2 run: states (sigma, rho); X = val(sigma, rho), W = val(sigma, tau); offers {(v, o): X(o) > X(o_cur)}; sigma' = W-optimum of sigma+offers
# (each reader takes its W-best offered/current gate); then any rho' with X(sigma', rho') >= X(sigma, rho) pointwise and X' <= W'. sigma must change.
import sys, functools, itertools
k = int(sys.argv[1])
readers = [(j, b) for j in range(2, k + 1) for b in (0, 1)] + [("T",)]
def lv(r): return k if r == ("T",) else r[0] - 1
ridx = {r: i for i, r in enumerate(readers)}
NG = 2 * len(readers)
def val_ladder(sig, rho, j, b, honest):
    # value of u(j,b): bits deep-first: path u(j,b) -> (reader u(j,b) via its current gate) -> routed child ...
    bits = [b]; jj, bb = j, b
    while jj >= 2:
        i = ridx[(jj, bb)]; c = sig[i]; g = 2 * i + c
        nb = c if honest else (c if rho[g] == 0 else 1 - c)
        bits.append(nb); jj -= 1; bb = nb
    return tuple(reversed(bits))
def vals(sig, rho, honest):
    # value of every reader and every gate
    out = {}
    for i, r in enumerate(readers):
        for c in (0, 1):
            g = 2 * i + c; nb = c if honest else (c if rho[g] == 0 else 1 - c)
            out[("g", g)] = val_ladder(sig, rho, lv(r), nb, honest)
        out[("r", i)] = out[("g", 2 * i + sig[i])]
    for j in range(1, k + 1):
        for b in (0, 1): out[("u", j, b)] = val_ladder(sig, rho, j, b, honest)
    return out
ZERO = tuple([0] * NG)
@functools.lru_cache(None)
def Wv(sig): return vals(sig, ZERO, True)
@functools.lru_cache(None)
def Xv(sig, rho): return vals(sig, rho, False)
def le(A, B): return all(A[x] <= B[x] for x in A)
RHOS = list(itertools.product((0, 1), repeat=NG))
@functools.lru_cache(None)
def best(sig, rho):
    X = Xv(sig, rho); W = Wv(sig)
    ns = list(sig)
    for i in range(len(readers)):
        cur = sig[i]; alt = 1 - cur
        if X[("g", 2 * i + alt)] > X[("g", 2 * i + cur)] and W[("g", 2 * i + alt)] > W[("g", 2 * i + cur)]: ns[i] = alt
    ns = tuple(ns)
    if ns == sig: return 0
    W2 = Wv(ns); gain = W2[("r", len(readers) - 1)] != W[("r", len(readers) - 1)]
    res = 0
    for r2 in RHOS:
        X2 = Xv(ns, r2)
        if le(X, X2) and le(X2, W2): res = max(res, best(ns, r2))
    return res + gain
s0 = tuple([0] * len(readers))
cands = [r for r in RHOS if le(Xv(s0, r), Wv(s0))]
print("k", k, "readers", len(readers), "max T W-rises under R2", max(best(s0, r) for r in cands), "R0:", 2 ** k - 1)
