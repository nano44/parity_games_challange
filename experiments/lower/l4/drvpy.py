#!/usr/bin/env python3
"""L-LOWER 4: second implementation of the DRIVEN BLOCK (independent of drv.c): exact longest moving path over all starts and all
exogenous key sequences e(t) (c of the block's bottom level). GEN format as drv.c. Prints LP and one optimal path.
Usage: drvpy.py file.gen"""
import sys
from functools import lru_cache
sys.setrecursionlimit(100000)
w = open(sys.argv[1]).read().split()
it = iter(w); m = int(next(it)); N = 2 * m
xt = []; rk = []; par = []
for x in range(N):
    a = [int(next(it)) for _ in range(6)]; xt.append(a[0:2]); rk.append(a[2:4]); par.append(a[4:6])
kap = [[int(next(it)), int(next(it))] for _ in range(m)]
ordr = [int(next(it)) for _ in range(N)]
beta = [[(-1 if par[x][k] else 1) * (1 << rk[x][k]) for k in range(2)] for x in range(N)]
def vals(s):
    v = [0] * N
    for x in ordr:
        k = s[x]; v[x] = beta[x][k] + (v[xt[x][k]] if xt[x][k] >= 0 else 0)
    return v
def ov(v, x, k): return beta[x][k] + (v[xt[x][k]] if xt[x][k] >= 0 else 0)
def step(s, e):
    v = vals(s); ns = list(s); c = e
    for j in range(m):
        for x in (2 * j, 2 * j + 1):
            if s[x] != c and ov(v, x, 1 - s[x]) > v[x]: ns[x] = c
        a, b = ns[2 * j], ns[2 * j + 1]
        c = (1 if a != c else 0) if a != b else kap[j][a]
    return tuple(ns)
@lru_cache(None)
def lp(s):
    best = (0, None)
    for e in (0, 1):
        ns = step(s, e)
        if ns != s:
            r = 1 + lp(ns)[0]
            if r > best[0]: best = (r, (e, ns))
    return best
from itertools import product
starts = list(product((0, 1), repeat=N))
bs = max(starts, key=lambda s: lp(s)[0])
print("LP", lp(bs)[0])
s = bs; t = 0
print(f"{t:3d} {' '.join(f'{s[2*j]}{s[2*j+1]}' for j in range(m))}")
while lp(s)[1]:
    e, ns = lp(s)[1]; t += 1
    mv = ' '.join(''.join('*' if ns[x] != s[x] else '.' for x in (2*j, 2*j+1)) for j in range(m))
    print(f"{t:3d} {' '.join(f'{ns[2*j]}{ns[2*j+1]}' for j in range(m))}  e={e}  mv={mv}"); s = ns
