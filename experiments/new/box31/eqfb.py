#!/usr/bin/env python3
"""Box 31 fixes §7.5: at every Even fallback whose state is EQ (Ξ = W everywhere), check W_{k+1} ⊵ W_k pointwise (W = value of the
(σ, τ_k)-play). Any game (not only C^1O). Usage: eqfb.py N nmin nmax seed [--c1o]"""
import sys, random
from tbcheck import *
N, lo, hi, seed = map(int, sys.argv[1:5]); rng = random.Random(seed); c1o = "--c1o" in sys.argv; st = dict(eqfb=0, viol=0, fb=0); d = 0
while d < N:
    g = rand_c1o(rng, lo, hi) if c1o else rgame(rng, lo, hi)
    if g is None: continue
    d += 1; E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, None); k = 0
    while k < 500:
        r = step(g, E, Ed, s, t)
        if r is None: break
        ns, nt, Is, It, fb, _, _ = r
        if fb and Is:
            st["fb"] += 1; Xi, _ = E.evaluate(tuple(s)); Eg0, W0 = wvals(g, s, t)
            if all(E.key(Xi[v]) == Eg0.key(W0[v]) for v in range(g.n)):
                st["eqfb"] += 1; Eg1, W1 = wvals(g, ns, t)
                if any(Eg1.key(W1[v]) < Eg0.key(W0[v]) for v in range(g.n)): st["viol"] += 1
        s, t = ns, nt; k += 1
print("EQFB", st)
