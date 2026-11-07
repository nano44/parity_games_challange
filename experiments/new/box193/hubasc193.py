#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): Theorem HUB-ASC data (doc Addendum 4). Exact maximum of distinct hub chains in CS(M, unlimited), where
ONLY the hub's chain must have at most B ascents at every time (other chains unconstrained). Compare F_0 = 1 + M(M+1)/2 and the
recursion bound F_B <= (M^2+M+1)(1 + M F_(B-1)^2). Usage: hubasc193.py M B"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import chain193
import numpy as np


if __name__ == "__main__":
    import itertools
    M, B = int(sys.argv[1]), int(sys.argv[2]); items = range(1, M + 1); st = set()
    for par in itertools.product(range(M + 1), repeat=M):
        nx = dict(zip(items, par)); ks = {}; asc = {}; ok = True
        for i in items:
            seen = []; x = i
            while x and x not in seen: seen.append(x); x = nx[x]
            if x: ok = False; break
            ks[i] = sum(1 << j for j in seen); asc[i] = sum(1 for p, q in zip(seen, seen[1:]) if q > p)
        if not ok: continue
        base = tuple(ks[i] for i in items)
        st.add(base + (0,))
        for h in items:
            if asc[h] <= B: st.add(base + (ks[h],))
    S = np.array(sorted(st, key=lambda s: s[-1]), dtype=np.int64); b = np.ones(len(S), dtype=np.int64)
    for j in range(len(S)):
        m = (S[:j, -1] < S[j, -1]) & np.all(S[:j] <= S[j], axis=1)
        if m.any(): b[j] = b[:j][m].max() + 1
    F = [1 + M * (M + 1) // 2]
    for _ in range(B): F.append((M * M + M + 1) * (1 + M * F[-1] ** 2))
    print(f"HUB-ASC CS(M {M}, hub <= {B} ascents): max distinct hub chains {int(b.max())}; bound F_{B} {F[B]}; 2^M {1 << M}")
