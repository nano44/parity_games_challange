#!/usr/bin/env python3
"""L-SI box 30: the abstract GATE problem for |D| = 1 with c1 = c2 = c (N5-TORD-box30 §4). Even-only graph on 0..n-1; sinks: o = n (the gate)
and c = n + 1 (the common cycle node, rank th). A play into c directly has value (P(path), len); a play into o has, in frame i, the value
(P(pre) ∪ A_i, len(pre) + L_i): the tail of o in the Ξ frame (i = 1, pessimistic) and in the W frame (i = 2, optimistic), with A_i sets of
VIRTUAL tail vertices (ranks disjoint from the graph's) and frame-2 tail ▷ frame-1 tail. Order: VJ for cycle node c (P-set by top
differing vertex parity, then length: c even -> shorter better, c odd -> longer). Step: arena H = ρ ∪ frame-1-improving edges; ρ' = a
pointwise frame-2-optimal strategy of H (exhaustive; cycles avoiding the sinks are EXIT if better than c, else worst). Counts: W-changing
steps (frame-2 value of some vertex changes), steps, trap changes (set of vertices whose play enters o)."""
import itertools
def rew(p): return p if p % 2 == 0 else -p

def better(a, b, pp, cpar):
    (A, la), (B, lb) = a, b
    if A != B:
        r = max(A ^ B, key=lambda v: pp[v]); return (r in A) == (pp[r] % 2 == 0)
    if la == lb: return False
    return la < lb if cpar == 0 else la > lb

def vals(rho, n, pp, th, tail):
    """frame value of every vertex: ("T", (P, len)) into c or o, ("C", m) for a cycle with top vertex m."""
    o, c = n, n + 1; out = []
    for x in range(n):
        p, y, pos = [], x, {}
        while y < n:
            if y in pos: out.append(("C", max(p[pos[y]:], key=lambda v: pp[v]))); break
            pos[y] = len(p); p.append(y); y = rho[y]
        else:
            P = frozenset(v for v in p if pp[v] > th)
            out.append(("T", (P | tail[0], len(p) + tail[1])) if y == o else ("T", (P, len(p))))
    return out

def sval(v, n, pp, th, tail, which):          # value of a successor vertex v in a frame (sinks included)
    return which[v] if v < n else (("T", (tail[0], tail[1])) if v == n else ("T", (frozenset(), 0)))

def b2(a, b, pp, th, cpar):
    ra = rew(th) if a[0] == "T" else rew(pp[a[1]]); rb = rew(th) if b[0] == "T" else rew(pp[b[1]])
    if ra != rb: return ra > rb
    if a[0] == "C": return False
    return better(a[1], b[1], pp, cpar)

def step(G, rho, pp, th, t1, t2):
    n = len(G); cpar = th % 2; v1 = vals(rho, n, pp, th, t1)
    H = []
    for x in range(n):
        cur = rho[x]
        H.append([cur] + [z for z in G[x] if z != cur and b2(sval(z, n, pp, th, t1, v1), sval(cur, n, pp, th, t1, v1), pp, th, cpar)])
    if all(len(h) == 1 for h in H): return None
    cands = [(list(ch), vals(list(ch), n, pp, th, t2)) for ch in itertools.product(*H)]
    for ch, k in cands:
        if all(not b2(k2[x], k[x], pp, th, cpar) for _, k2 in cands for x in range(n)):
            if any(v[0] == "C" and rew(pp[v[1]]) > rew(th) for v in k): return "EXIT"
            return ch
    return "NOOPT"

def trapped(rho, n):
    out = set()
    for x in range(n):
        y, seen = x, set()
        while y < n and y not in seen: seen.add(y); y = rho[y]
        if y == n: out.add(x)
    return frozenset(out)

def run(G, rho, pp, th, t1, t2, cap=300):
    n = len(G); w = s = tc = 0; cpar = th % 2
    while s < cap:
        nr = step(G, rho, pp, th, t1, t2)
        if nr is None: return w, s, tc, "STOP"
        if nr in ("EXIT", "NOOPT"): return w, s, tc, nr
        if nr == rho: return w, s, tc, "STALL"
        if vals(nr, n, pp, th, t2) != vals(rho, n, pp, th, t2): w += 1
        if trapped(nr, n) != trapped(rho, n): tc += 1
        rho = nr; s += 1
    return w, s, tc, "CAP"
