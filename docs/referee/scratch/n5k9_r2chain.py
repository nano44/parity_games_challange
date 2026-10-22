#!/usr/bin/env python3
"""R-N5K9 §C: re-derive REFEREE-2's n = 10 one-player chain (R2-N5K9/chain_n10.txt: start only) with my VJ00-only oracle
(n5t_probe). Longest SINGLE-switch improvement chain from the given start (memoised DFS on the acyclic strategy graph), the number
of flat steps on it, and the longest ANY-subset-free check is not attempted. Run from the repo root."""
import sys, os
sys.setrecursionlimit(100000)
sys.path.insert(0, os.path.join(os.getcwd(), "docs/referee/scratch"))
from n5t_probe import omega, improvements, from_pg
prio = [4, 5, 3, 5, 7, 4, 6, 8, 5, 1]; owner = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
succ = [[4], [7, 6, 5], [0, 2, 8], [4, 6, 3], [7, 9, 6], [7, 8, 9], [0, 2, 1], [1, 2, 3], [6, 3, 7], [2, 1, 9]]
start = {1: 6, 2: 0, 3: 4, 4: 6, 5: 8, 6: 0, 7: 3, 8: 3, 9: 2}
o, s, p, r = from_pg(prio, owner, succ)
n = len(prio); inv = {b: a for a, b in r.items()}
memo = {}; Om = {}
def om(t):
    if t not in Om: Om[t] = omega(n, o, s, p, list(t))
    return Om[t]
def best(t):                     # (length, flats) of a longest single-switch chain from t
    if t in memo: return memo[t]
    imp = improvements(n, o, s, p, list(t), om(t)); res = (0, 0)
    for v, ws in imp.items():
        for w in ws:
            u = list(t); u[v] = w; u = tuple(u)
            L, F = best(u); cand = (L + 1, F + (om(u) == om(t)))
            if cand > res: res = cand
    memo[t] = res; return res
t0 = [None] * n
for v, w in start.items(): t0[r[v]] = r[w]
L, F = best(tuple(t0))
print(f"longest single-switch chain from R2's start: {L} steps (flat steps on the chosen longest chain: {F}); strategies visited {len(memo)}")
