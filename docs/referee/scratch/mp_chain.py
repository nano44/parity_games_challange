#!/usr/bin/env python3
"""REFEREE succ. 17: longest all-MATCHED chain (NM = 0) of subsets of K all-even ranks, Phi rising by 1 per step: attains W = K(K+1)/2,
so the Corollary's W is tight for abstract sequences and the mutation W := K is false. Own code (matchphi_probe.matched)."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import matchphi_probe as M
for K in range(1, 9):
    par = [0] * K
    subs = [frozenset(c) for k in range(K + 1) for c in itertools.combinations(range(K), k)]
    byphi = {}
    for s in subs: byphi.setdefault(M.phi(s, par), []).append(s)
    W = K * (K + 1) // 2; best = {s: 0 for s in byphi[0]}
    for p in range(1, W + 1):
        nb = {s: max(best[a] for a in best if M.matched(a, s, par)) + 1 for s in byphi.get(p, []) if any(M.matched(a, s, par) for a in best)}
        if not nb: break
        best = nb
    L = max(best.values()); print("K", K, "W", W, "longest all-matched chain", L, "attains W", L == W, "violates W:=K", L > K)
