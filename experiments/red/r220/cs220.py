#!/usr/bin/env python3
"""L-RED 55 R220: exhaustive maximum of distinct hub values in CS(M) runs whose HUB value has <= B ascents (other chains unrestricted),
as in P-N5-ASC §4 Theorem HUB-ASC(B). Independent of L-NEW's tools. Method: states = (forest, hub); a run is a sequence of states with
every item's chain and the hub value lex-nondecreasing. Lex order of sets of items = integer order of bitmasks (item i = bit i-1, the
most relevant element of the symmetric difference is the highest differing bit). Runs are monotone paths in the product order of the
vector (chain(1), ..., chain(M), hub value); the answer is the longest path counting strict hub increases, +1.
Usage: cs220.py M"""
import sys, itertools
import numpy as np
M = int(sys.argv[1])
def forests(M):
    for nx in itertools.product(range(M + 1), repeat=M):          # nx[i] = parent item (1..M) or 0 = none
        ok = True
        for i in range(M):
            seen, x = set(), i + 1
            while x and ok:
                if x in seen: ok = False
                seen.add(x); x = nx[x - 1]
            if not ok: break
        if ok: yield nx
def chain(nx, x):
    s = []
    while x: s.append(x); x = nx[x - 1]
    return s
states = {}
for nx in forests(M):
    ch = [chain(nx, i + 1) for i in range(M)]; masks = tuple(sum(1 << (c - 1) for c in c_) for c_ in ch)
    for h in range(M + 1):
        hs = ch[h - 1] if h else []; asc = sum(1 for a, b in zip(hs, hs[1:]) if b > a); hv = sum(1 << (c - 1) for c in hs)
        key = masks + (hv,)
        states[key] = min(states.get(key, 99), asc)
keys = list(states); A = np.array(keys, dtype=np.int64); asc = np.array([states[k] for k in keys])
order = np.argsort(A.sum(axis=1), kind="stable"); A = A[order]; asc = asc[order]
for B in (0, 1, 2, 3):
    sel = np.where(asc <= B)[0]; X = A[sel]; best = np.ones(len(X), dtype=np.int64)
    for i in range(len(X)):
        dom = np.all(X[:i] <= X[i], axis=1)
        if dom.any():
            prev = np.where(dom)[0]; inc = (X[prev, -1] < X[i, -1]).astype(np.int64)
            best[i] = max(1, (best[prev] + inc).max())
    F = 1 + M * (M + 1) // 2
    for b in range(B): F = (M * M + M + 1) * (1 + M * F * F)
    print(f"M {M} B {B}: exhaustive max distinct hub values {best.max()} | packet bound F_B(M) {F} | states {len(X)}", flush=True)
