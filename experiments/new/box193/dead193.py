#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): instances for the two DEAD proof routes of ASC-POLY(1) in CS(M, 1) (doc Addendum 1).
  ptr M      PTR-MON-HI: «if the part of tail(x) above x is unchanged, next(x) does not decrease». Over all dominance pairs F <= F' of
             CS(M, 1) forests: counts pointer changes with unchanged high part, and how many decrease; prints the first witness at M.
  fixtop M   FIXTOP-QUAD: «with the hub's top fixed, at most quadratically many hub chains». Exact maximum per fixed top T.
Usage: dead193.py ptr M | dead193.py fixtop M"""
import sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import chain193


def forests_full(M, A=1):
    items = range(1, M + 1); out = []
    for par in itertools.product(range(M + 1), repeat=M):
        nx = dict(zip(items, par)); ch = {}; ok = True
        for i in items:
            seen = []; x = i
            while x and x not in seen: seen.append(x); x = nx[x]
            if x or sum(1 for p, q in zip(seen, seen[1:]) if q > p) > A: ok = False; break
            ch[i] = seen
        if ok: out.append((nx, {i: sum(1 << j for j in ch[i]) for i in items}, ch))
    return out


def ptr(M):
    F = forests_full(M); tot = bad = 0; wit = None
    for (n1, k1, c1), (n2, k2, c2) in itertools.product(F, F):
        if not all(k1[i] <= k2[i] for i in k1): continue
        for x in k1:
            if k1[x] >> (x + 1) == k2[x] >> (x + 1) and n1[x] != n2[x]:
                tot += 1
                if n2[x] < n1[x]:
                    bad += 1
                    if wit is None: wit = (x, c1, c2)
    print(f"PTR-MON-HI M {M}: pointer changes with unchanged high part {tot}, decreasing {bad}")
    if wit: print(f"  witness: x {wit[0]}; chains before {wit[1]}; after {wit[2]}")


def fixtop(M):
    import numpy as np
    F = chain193.forests(M, 1); res = {}
    for T in range(1, M + 1):
        st = {k + (k[h - 1],) for k in F for h in range(1, M + 1) if k[h - 1].bit_length() - 1 == T}
        S = np.array(sorted(st, key=lambda s: s[-1]), dtype=np.int64); b = np.ones(len(S), dtype=np.int64)
        for j in range(len(S)):
            m = (S[:j, -1] < S[j, -1]) & np.all(S[:j] <= S[j], axis=1)
            if m.any(): b[j] = b[:j][m].max() + 1
        res[T] = int(b.max())
    print(f"FIXTOP M {M} A 1: max distinct hub chains with hub top fixed at T: " + " ".join(f"T{T} {v}" for T, v in res.items()))


if __name__ == "__main__":
    {"ptr": ptr, "fixtop": fixtop}[sys.argv[1]](int(sys.argv[2]))
