#!/usr/bin/env python3
"""L-COMP box 36: the exhaustive genome space of box 33 (enum33.py), re-written without the asc197 import.
Space (eg195.gen schema): lev = every nondecreasing level vector from 0 with steps 0/1 (N <= 2: (0) | (0,0) | (0,1), = enum33; N >= 3 = exact35); option split D (>= 1 per mover, sum M); xt in {-1} + movers
per option; gate = permutation of 0..M-1 over options (option order); br = permutation; bp in {0,1}^M; start = one option per mover.
wt = -1 at level 0, else the FIRST mover of level lev - 1 (enum33/exact35 convention). Index i = position in this fixed enumeration order (identical to enum33's order).
xi_filter(xts, D, N): the Xi-graph depends only on (D, xts), so k is computed once per (lev, D, xts) block."""
import itertools


def levvecs(N):
    """every nondecreasing level vector from 0 with steps 0 or 1 (exact35.py's order; for N <= 2 = enum33's (0), (0,0), (0,1))."""
    out = []
    def rec(v):
        if len(v) == N: out.append(tuple(v)); return
        for l in (v[-1], v[-1] + 1): rec(v + [l])
    rec([0]); return out


def structures(N, M):
    levs = levvecs(N)
    for lev in levs:
        for D in itertools.product(range(1, M + 1), repeat=N):
            if sum(D) == M: yield lev, D


def blocks(N, M):
    """(lev, D, xts) blocks in enumeration order, with the block size."""
    for lev, D in structures(N, M):
        for xts in itertools.product(range(-1, N), repeat=M):
            yield lev, D, xts


def inner(D, M):
    for gate in itertools.permutations(range(M)):
        for br in itertools.permutations(range(M)):
            for bp in itertools.product((0, 1), repeat=M):
                for st in itertools.product(*[range(d) for d in D]):
                    yield gate, br, bp, st


def blocksize(D, M):
    import math
    s = 1
    for d in D: s *= d
    return math.factorial(M) ** 2 * 2 ** M * s


def make(N, lev, D, xts, gate, br, bp, st):
    opts = []; g = []; b = 0
    for x in range(N):
        oo = []; gg = []
        for _ in range(D[x]):
            wt = -1 if lev[x] == 0 else [y for y in range(N) if lev[y] == lev[x] - 1][0]
            oo.append([wt, xts[b], b]); gg.append(gate[b]); b += 1
        opts.append(oo); g.append(gg)
    return {"N": N, "lev": list(lev), "opts": opts, "gate": g, "br": list(br), "bp": list(bp), "start": list(st)}


def xi_k(N, D, xts):
    """Xi feedback number of the block: minimum number of movers whose removal leaves no Xi-cycle (self-loops count); brute force."""
    owner = [x for x in range(N) for _ in range(D[x])]
    adj = [set() for _ in range(N)]
    for b, xt in enumerate(xts):
        if xt >= 0: adj[owner[b]].add(xt)
    def acyc(rem):
        col = {}
        def dfs(v):
            col[v] = 1
            for w in adj[v]:
                if w in rem: continue
                if col.get(w) == 1: return False
                if w not in col and not dfs(w): return False
            col[v] = 2; return True
        return all(dfs(v) for v in range(N) if v not in rem and v not in col)
    for k in range(N + 1):
        for S in itertools.combinations(range(N), k):
            if acyc(set(S)): return k
