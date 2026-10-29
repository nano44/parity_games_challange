#!/usr/bin/env python3
"""L-SI box 30: the abstract TWO-ORDER SWITCH-BEST (N5-FRZ-box29 §7, |D| = 1). Even-only graph on 0..n-1 plus the gate t = n (o).
Every prefix vertex has a distinct rank r (p' = 2r + par). Order i (i = 1: arena, Ξ frame; i = 2: choice, W frame) is the VJ prefix order
for a tail whose cycle node c_i has p'(c_i) = th_i (threshold) and parity cp_i: compare P_i = {v on path : p'(v) > th_i} by the top
vertex of the symmetric difference (better if in the new set and even, or in the old set and odd), then length (c even: shorter better;
c odd: longer better). A step: H = ρ ∪ {(x, z) : key1(z) better than key1(ρx)}; ρ' = a pointwise key2-optimal positional strategy of H
whose plays reach t (cycles avoiding t are treated as worst; exact by enumeration, small n). Counts W-changing steps until H = ρ.
STALL = ρ' = ρ while H ≠ ρ (N5 would fall back)."""
import itertools, random, sys

def pval(path, pp, th):           # path: list of vertices from x up to (not incl.) t
    return frozenset(v for v in path if pp[v] > th), len(path)

def better(a, b, pp, cpar):       # is key a strictly better than key b (for Even)?
    (A, la), (B, lb) = a, b
    if A != B:
        r = max(A ^ B, key=lambda v: pp[v])
        return (r in A) == (pp[r] % 2 == 0)
    if la == lb: return False
    return la < lb if cpar == 0 else la > lb

def paths(rho, n):
    P = {}
    for x in range(n):
        p, y, seen = [], x, set()
        while y != n:
            if y in seen: p = None; break
            seen.add(y); p.append(y); y = rho[y]
        P[x] = p
    return P

def rew(p): return p if p % 2 == 0 else -p

PP = {}
def play(rho, n, x):
    p, y, pos = [], x, {}
    while y != n:
        if y in pos: return p, max(p[pos[y]:], key=lambda v: PP[v])  # cycle avoiding t: (path, most relevant cycle vertex)
        pos[y] = len(p); p.append(y); y = rho[y]
    return p, None

def better2(a, b, pp, th, c):     # values: ("T", key) for plays into t, ("C", m) for a cycle with max vertex m
    ra = rew(th) if a[0] == "T" else rew(pp[a[1]]); rb = rew(th) if b[0] == "T" else rew(pp[b[1]])
    if ra != rb: return ra > rb
    if a[0] == "C": return False  # same cycle node: VJ ties ignored here (both are exits anyway)
    return better(a[1], b[1], pp, c)

def step(G, rho, pp, th1, c1, th2, c2):
    PP.clear(); PP.update(enumerate(pp))
    n = len(G); P = paths(rho, n)
    k1 = {x: pval(P[x], pp, th1) for x in range(n)}; k1[n] = (frozenset(), 0)
    H = []
    for x in range(n):
        cur = rho[x]
        H.append([cur] + [z for z in G[x] if z != cur and better(k1[z], k1[cur], pp, c1)])
    if all(len(o) == 1 for o in H): return None, H
    cands = []
    for choice in itertools.product(*H):
        k = []
        for x in range(n):
            p, m = play(choice, n, x)
            k.append(("T", pval(p, pp, th2)) if m is None else ("C", m))
        cands.append((list(choice), k))
    for ch, k in cands:
        if all(not better2(k2[x], k[x], pp, th2, c2) for _, k2 in cands for x in range(n)):
            if any(v[0] == "C" and rew(pp[v[1]]) > rew(th2) for v in k): return "EXIT", H
            return ch, H
    return "NOOPT", H

def run(G, rho, pp, th1, c1, th2, c2, cap=200):
    n = len(G); w = 0; steps = 0; hist = []
    while steps < cap:
        P = paths(rho, n); k2 = [pval(P[x], pp, th2) for x in range(n)]
        nr, H = step(G, rho, pp, th1, c1, th2, c2)
        if nr is None: return w, steps, "STOP", hist
        if nr in ("NOOPT", "EXIT"): return w, steps, nr, hist
        if nr == rho: return w, steps, "STALL", hist
        Q = paths(nr, n); k2n = [pval(Q[x], pp, th2) for x in range(n)]
        ch = [x for x in range(n) if k2n[x] != k2[x]]
        w += bool(ch); steps += 1; hist.append((tuple(rho), ch)); rho = nr
    return w, steps, "CAP", hist
