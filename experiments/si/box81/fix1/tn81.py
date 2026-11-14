#!/usr/bin/env python3
"""L-SI P-ACYC fixes entry 1, AC-2: T_CYC / N on lemma81's set A (agen 300, seed 7, the same generator stream as lemma81.py's main)
by N: number of runs, runs with T_CYC = N, max T_CYC / N. Usage: tn81.py (run from anywhere)"""
import sys, os, random
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, B)
import lemma81, census81
rng = random.Random(7); got = 0; by = {}
while got < 300:
    G = lemma81.agen(rng, rng.randint(1, 6), rng.randint(1, 3), rng.randint(2, 3))
    if not census81.xi_acyclic(G): continue
    T, N, *_ = lemma81.check(G); got += 1
    n, eq, mx = by.get(N, (0, 0, 0.0)); by[N] = (n + 1, eq + (T == N), max(mx, T / N))
for N in sorted(by): print(f"N {N} runs {by[N][0]} T=N {by[N][1]} max T/N {by[N][2]:.3f}")
ge2 = max(by[N][2] for N in by if N >= 2)
print(f"set A: runs with T = N {sum(v[1] for v in by.values())} (all at N = 1: {all(by[N][1] == 0 for N in by if N >= 2)}); max T/N over N >= 2: {ge2:.3f}")
