#!/usr/bin/env python3
"""Longest downstream-first run versus longest unrestricted run on FHZ's one-player graph G_{n,r,s,t} (fhz.py build),
exact over all trees (memoised DFS on the acyclic improvement graph).  Usage: df_fhz.py n r s t"""
import sys, os, itertools
sys.setrecursionlimit(1 << 20)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import fhz
n, r, s, t = map(int, sys.argv[1:5]); G, P, B0, B0P, names, ename, pid = fhz.build(n, r, s, t)
N = G.N; out = G.out
choices = [out[v] for v in range(N - 1)]
trees = list(itertools.product(*choices))
df_next = {}; all_next = {}
for B in trees:
    dist = [None] * N; dist[N - 1] = 0
    def d(v):
        if dist[v] is None:
            sv, w, c = G.edges[B[v]]; dist[v] = c + d(w)
        return dist[v]
    for v in range(N - 1): d(v)
    imp = [(v, e) for v in range(N - 1) for e in out[v] if e != B[v] and G.edges[e][2] + dist[G.edges[e][1]] < dist[v]]
    impv = {v for v, _ in imp}; alls = []; dfs = []
    for v, e in imp:
        T = list(B); T[v] = e; T = tuple(T); alls.append(T)
        x = G.edges[B[v]][1]; ok = True
        while x != N - 1:
            if x in impv: ok = False; break
            x = G.edges[B[x]][1]
        if ok: dfs.append(T)
    df_next[B] = dfs; all_next[B] = alls
memo = {}
def longest(B, nxt):
    if B in memo: return memo[B]
    memo[B] = 0; memo[B] = max([longest(T, nxt) + 1 for T in nxt[B]] + [0]); return memo[B]
ldf = max(longest(B, df_next) for B in trees); memo.clear(); lall = max(longest(B, all_next) for B in trees)
print(f"FHZ G_({n},{r},{s},{t}): |V|={N} |E|={len(G.edges)} trees={len(trees)}: longest DF run {ldf}, longest unrestricted run {lall}")
