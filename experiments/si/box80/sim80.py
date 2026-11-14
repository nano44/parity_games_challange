#!/usr/bin/env python3
"""L-SI box 80: compact simulator of R104's IDEAL model on L^R_d genomes (same rule as box76/tw.py Sim; cross-checked against it).
Genome dict: N, lev, opts[x][k] = [W-pointer, Xi-target (-1 = X), edge id], gate[x][k], br[e], bp[e], start."""
import json, sys
class Sim:
    def __init__(s, G):
        s.G = G; s.N = N = G["N"]; s.o = G["opts"]; s.g = G["gate"]
        s.xt = [[s.o[x][k][1] for k in range(2)] for x in range(N)]
        s.e = [[(1 << G["br"][s.o[x][k][2]]) * (1 if G["bp"][s.o[x][k][2]] == 0 else -1) for k in range(2)] for x in range(N)]
        # topological order of the Xi-DAG (targets first)
        seen = [0] * N; order = []
        def dfs(x):
            if seen[x] == 1: raise RuntimeError("Xi-cycle")
            if seen[x]: return
            seen[x] = 1
            for k in range(2):
                y = s.xt[x][k]
                if y >= 0: dfs(y)
            seen[x] = 2; order.append(x)
        for x in range(N): dfs(x)
        s.topo = order
    def cv(s, st):
        c = [0] * s.N
        for x in s.topo:
            y = s.xt[x][st[x]]; c[x] = s.e[x][st[x]] + (c[y] if y >= 0 else 0)
        return c
    def v(s, c, x, k):
        y = s.xt[x][k]; return s.e[x][k] + (c[y] if y >= 0 else 0)
    def step(s, st):
        N = s.N; c = s.cv(st)
        better = [s.v(c, x, 1 - st[x]) > c[x] for x in range(N)]
        if not any(better): return None
        ns = list(st); K = [None] * N
        for x in range(N):   # x in index order = level order on L^R_d
            ks = [st[x]] + ([1 - st[x]] if better[x] else [])
            def key(k):
                w = s.o[x][k][0]; return (s.g[x][k],) if w < 0 else K[w] + (s.g[x][k],)
            k = min(ks, key=key); ns[x] = k; K[x] = key(k)
        return tuple(ns)
    def run(s, st=None, cap=10 ** 6):
        st = tuple(s.G["start"] if st is None else st); S = [st]
        while len(S) <= cap:
            n = s.step(S[-1])
            if n is None or n == S[-1]: return S
            S.append(n)
        raise RuntimeError("cap")
def keyorder(sim, st):
    N = sim.N; K = [None] * N
    for x in range(N):
        w = sim.o[x][st[x]][0]; K[x] = (sim.g[x][st[x]],) if w < 0 else K[w] + (sim.g[x][st[x]],)
    return [int(K[2 * j] < K[2 * j + 1]) for j in range(N // 2)]
def stats(sim, S):
    d = sim.N // 2; T = len(S) - 1
    O = [keyorder(sim, s) for s in S]
    F = [sum(O[t][j] != O[t - 1][j] for t in range(1, T + 1)) for j in range(d)]
    mv = [sum(S[t][x] != S[t - 1][x] for t in range(1, T + 1)) for x in range(sim.N)]
    return T, F, mv
def capped(F):
    """number of capped levels: largest h with F(l) = 2^(l+2) - 2 for l < h"""
    h = 0
    while h < len(F) and F[h] == 2 ** (h + 2) - 2: h += 1
    return h
if __name__ == "__main__":
    for p in sys.argv[1:]:
        G = json.load(open(p)); sim = Sim(G); S = sim.run(); T, F, mv = stats(sim, S)
        print(p.split("/")[-1], "d", G["N"] // 2, "T", T, "capped", capped(F), "F", F)
