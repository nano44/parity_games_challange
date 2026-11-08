#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): the abstract chain system CS(M, A) of the box 193 doc §2.
Items 1..M (rank = number). A forest = a parent map next: item -> item or 0 (none), acyclic; chain(x) = the set of items on the path
from x (x included). A <= the most ascents (consecutive p, q on a chain with q > p) allowed on every item's chain; A = 99: no limit.
Sets are compared lexicographically by the most relevant element of the symmetric difference (= the binary number sum 2^i).
A run is a sequence of forests in which every item's chain is lex-nondecreasing, plus a hub whose chain is chain(h_t) for some item
h_t (or empty), also lex-nondecreasing. Output: the maximum number of distinct hub chains over all runs (exact, exhaustive).
Usage: chain193.py M A            exact value by a numpy dominance DP (fine for M <= 5)
       chain193.py M A --emit     print the forests (count, M, then one line of M chain keys each) for dp193.c (M = 6, 7)"""
import itertools, sys


def forests(M, A):
    items = range(1, M + 1); out = set()
    for par in itertools.product(range(M + 1), repeat=M):
        nx = dict(zip(items, par)); ks = []; ok = True
        for i in items:
            seen = []; x = i
            while x and x not in seen: seen.append(x); x = nx[x]
            if x or sum(1 for p, q in zip(seen, seen[1:]) if q > p) > A: ok = False; break
            ks.append(sum(1 << j for j in seen))
        if ok: out.add(tuple(ks))
    return sorted(out, key=sum)


def best(M, A):
    import numpy as np
    st = set()
    for k in forests(M, A):
        for h in range(M + 1): st.add(k + ((k[h - 1] if h else 0),))
    S = np.array(sorted(st, key=lambda s: s[-1]), dtype=np.int64); b = np.ones(len(S), dtype=np.int64)
    for j in range(len(S)):
        m = (S[:j, -1] < S[j, -1]) & np.all(S[:j] <= S[j], axis=1)
        if m.any(): b[j] = b[:j][m].max() + 1
    return int(b.max())


if __name__ == "__main__":
    M, A = int(sys.argv[1]), int(sys.argv[2])
    if len(sys.argv) > 3 and sys.argv[3] == "--emit":
        F = forests(M, A); print(len(F), M)
        for k in F: print(*k)
    else:
        print(f"CS(M {M}, A {A}): max distinct hub chains {best(M, A)}; 2^M {1 << M}; 1 + M(M+1)/2 {1 + M * (M + 1) // 2}")
