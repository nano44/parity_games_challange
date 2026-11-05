#!/usr/bin/env python3
"""hill-climb ISO R197 ladders (m+1 levels) maximizing (mu_k - bound(k), T_k), bound(k) = 1 + ceil(k/2) (CONJECTURE REC-K).
Writes out/fkclimb_k<k>_m<m>_mu<mu>_T<T>.json for every new best; prints KILL if mu_k > bound. Usage: fkclimb.py k m iters restarts seed"""
import os, sys, json, random
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "fk.py")).read().split("\nif __name__")[0])
sys.setrecursionlimit(100000)
k, m, iters, restarts, seed = map(int, sys.argv[1:6]); rng = random.Random(seed); bound = 1 + (k + 1) // 2; best = None
for rs in range(restarts):
    G = rand_lr(m + 1, rng, iso=True); T, mu, _ = muk(G, k); s = (mu, T)
    for it in range(iters):
        G2 = mutate(G, rng); T2, mu2, _ = muk(G2, k)
        if (mu2, T2) >= s: G, s = G2, (mu2, T2)
    if best is None or s > best:
        best = s; json.dump(G, open(os.path.join(H, "out", "fkclimb_k%d_m%d_mu%d_T%d.json" % (k, m, s[0], s[1])), "w"))
    print("restart %d (mu_k, T_k) %s best %s bound %d%s" % (rs, s, best, bound, "  KILL" if s[0] > bound else ""), flush=True)
