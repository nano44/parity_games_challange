#!/usr/bin/env python3
"""Box 21: brute-force check of Lemma R / Lemma S (a) on small random games: for random (sigma, tau),
  L_sigma(v) = min over all Odd strategies tau' of V_{sigma,tau'}(v)   (Even's key order),
  U_tau(v) (dual valuation of tau, read in G's order) = max over all Even strategies sigma' of V_{sigma',tau}(v),
and the dual triple equals the G triple of the same play. Usage: sandwich_check.py N nmax seed"""
import sys, random, itertools
from n5x import *
from h1 import wvals
N, nmax, seed = map(int, sys.argv[1:]); rng = random.Random(seed); bad = 0; checks = 0
for _ in range(N):
    n = rng.randint(2, nmax)
    g = pg.Game([rng.randrange(n) for _ in range(n)], [rng.randrange(2) for _ in range(n)], [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2))))) for _ in range(n)])
    E, Ed = Engine(g), Engine(dual(g))
    ev = [v for v in range(n) if g.owner[v] == 0]; od = [v for v in range(n) if g.owner[v] == 1]
    S = [dict(zip(ev, c)) for c in itertools.product(*[g.succ[v] for v in ev])]
    T = [dict(zip(od, c)) for c in itertools.product(*[g.succ[v] for v in od])]
    if len(S) * len(T) > 4000: continue
    s = rng.choice(S); t = rng.choice(T)
    sig = tuple(s.get(v, -1) for v in range(n)); tau = tuple(t.get(v, -1) for v in range(n))
    L, _ = E.evaluate(sig); U, _ = Ed.evaluate(tau)
    for v in range(n):
        vals = [wvals(g, sig, [t2.get(u, -1) for u in range(n)]) for t2 in T]
        mn = min(Eg.key(W[v]) for Eg, W in vals)
        vals2 = [wvals(g, [s2.get(u, -1) for u in range(n)], tau) for s2 in S]
        mx = max(Eg.key(W[v]) for Eg, W in vals2)
        Eg0 = vals[0][0]
        checks += 1
        if Eg0.key(L[v]) != mn or E.key(U[v]) != mx: bad += 1   # U[v] is a (c, P, l) triple of a play: read it with G's key
print(f"checks {checks} mismatches {bad}")
