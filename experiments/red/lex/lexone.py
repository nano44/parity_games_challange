#!/usr/bin/env python3
"""L-RED R153: T54's abstract LEX-ARENA model (l-lit 0ee955c7 docs/lit/T54-lexarena.py, same step rule), scored by the number of strict
key decreases of ONE top vertex (layer L, first vertex) instead of the run length. Exhaustive DP over states. Usage: lexone.py L [W]"""
import sys, itertools, functools
L = int(sys.argv[1]); W = int(sys.argv[2]) if len(sys.argv) > 2 else 2
lay = [[0]] + [[1 + (j - 1) * W + i for i in range(W)] for j in range(1, L + 1)]
movers = [x for j in range(2, L + 1) for x in lay[j]]; TOP = lay[L][0]
def keys(sig):
    key = {0: ()}
    for j in range(1, L + 1):
        for x in lay[j]: key[x] = (x,) if j == 1 else key[sig[x]] + (x,)
    return key
def newsig(sig, full):
    key = {0: ()}; s = dict(sig)
    for j in range(1, L + 1):
        for x in lay[j]:
            if j == 1: key[x] = (x,); continue
            opts = lay[j - 1] if x in full else [sig[x]]
            y = min(opts, key=lambda y: key[y]); s[x] = y; key[x] = key[y] + (x,)
    return s
start = {x: lay[j - 1][-1] for j in range(2, L + 1) for x in lay[j]}
@functools.lru_cache(None)
def best(st):
    sig = dict(st); k0 = keys(sig)[TOP]; b = 0
    for r in range(1, len(movers) + 1):
        for full in itertools.combinations(movers, r):
            s2 = newsig(sig, set(full))
            if s2 != sig: b = max(b, (keys(s2)[TOP] < k0) + best(tuple(sorted(s2.items()))))
    return b
print("L", L, "W", W, "n", 1 + L * W, "max key decreases of one top vertex", best(tuple(sorted(start.items()))), "distinct keys", W ** (L - 1))
