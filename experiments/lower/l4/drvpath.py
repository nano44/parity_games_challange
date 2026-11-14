#!/usr/bin/env python3
"""L-LOWER 4: second implementation (Python) of the DRIVEN BLOCK, from the stored start only. Objective: max flips of o_L
(L = OBJL, block level; = real F(L+1)) over moving paths and exogenous key sequences e; tie-break: fewest e-changes.
Prints the optimal path (states, e, movers), flips of every o_j along it, moves per mover. Usage: drvpath.py file.gen L"""
import sys
from functools import lru_cache
sys.setrecursionlimit(1000000)
w = open(sys.argv[1]).read().split(); L = int(sys.argv[2])
it = iter(w); m = int(next(it)); N = 2 * m
xt = []; rk = []; par = []
for x in range(N):
    a = [int(next(it)) for _ in range(6)]; xt.append(a[0:2]); rk.append(a[2:4]); par.append(a[4:6])
kap = [[int(next(it)), int(next(it))] for _ in range(m)]
ordr = [int(next(it)) for _ in range(N)]
s0 = tuple(int(c) for c in next(it))
beta = [[(-1 if par[x][k] else 1) * (1 << rk[x][k]) for k in range(2)] for x in range(N)]
def vals(s):
    v = [0] * N
    for x in ordr: k = s[x]; v[x] = beta[x][k] + (v[xt[x][k]] if xt[x][k] >= 0 else 0)
    return v
def ov(v, x, k): return beta[x][k] + (v[xt[x][k]] if xt[x][k] >= 0 else 0)
def step(s, e):
    v = vals(s); ns = list(s); c = e
    for j in range(m):
        for x in (2 * j, 2 * j + 1):
            if s[x] != c and ov(v, x, 1 - s[x]) > v[x]: ns[x] = c
        a, b = ns[2 * j], ns[2 * j + 1]; c = (1 if a != c else 0) if a != b else kap[j][a]
    return tuple(ns)
def os_(s, e):
    c = e; out = []
    for j in range(m):
        a, b = s[2 * j], s[2 * j + 1]; c = (1 if a != c else 0) if a != b else kap[j][a]; out.append(c)
    return out
@lru_cache(None)
def best(s, e):  # (flips, -echanges, next)
    o = os_(s, e)[L]; b = (0, 0, None)
    for f in (0, 1):
        ns = step(s, f)
        if ns == s: continue
        r = best(ns, f); cand = (r[0] + (os_(ns, f)[L] != o), r[1] - (f != e), (f, ns))
        if cand[:2] > b[:2]: b = cand
    return b
e0 = max((0, 1), key=lambda e: best(s0, e)[:2])
r = best(s0, e0); print("max flips of o_%d (real F(%d)): %d ; e-changes %d" % (L, L + 1, r[0], -r[1]))
s, e = s0, e0; path = [(s, e)]
while best(s, e)[2]: e, s = best(s, e)[2]; path.append((s, e))
F = [0] * m; mv = [0] * N; es = "".join(str(e) for _, e in path)
for (a, ea), (b, eb) in zip(path, path[1:]):
    oa, ob = os_(a, ea), os_(b, eb)
    for j in range(m): F[j] += oa[j] != ob[j]
    for x in range(N): mv[x] += a[x] != b[x]
print("T", len(path) - 1, "e", es); print("flips o_j (real F(j+1)):", F); print("moves:", mv)
if len(sys.argv) > 3:
    for t, (s, e) in enumerate(path): print(t, " ".join(f"{s[2*j]}{s[2*j+1]}" for j in range(m)), e)
