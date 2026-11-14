#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): CONJECTURE RECUR data (doc Addendum 1). In CS(M, A), a LEVEL is a stretch of a run on which every
item's tail top tau(x) := max(chain(x) - {x}) (0 if empty) and the hub's top are all constant. These are monotone (lex-monotone
chains), so a run has at most M(M+1) + 1 levels. Prints the exact maximum of distinct hub chains inside one level (maximum over levels).
RECUR predicts f_(A-1)(M-1) (f_(-1) := 1). Usage: taulin193.py M A"""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import chain193
import numpy as np

top = lambda k: k.bit_length() - 1
if __name__ == "__main__":
    M, A = int(sys.argv[1]), int(sys.argv[2]); groups = collections.defaultdict(set)
    for k in chain193.forests(M, A):
        tau = tuple(top(k[x - 1] & ~(1 << x)) if k[x - 1] & ~(1 << x) else 0 for x in range(1, M + 1))
        for h in range(M + 1):
            c = k[h - 1] if h else 0
            groups[tau + (top(c) if c else 0,)].add(k + (c,))
    best = 0
    for st in groups.values():
        S = np.array(sorted(st, key=lambda s: s[-1]), dtype=np.int64); b = np.ones(len(S), dtype=np.int64)
        for j in range(len(S)):
            m = (S[:j, -1] < S[j, -1]) & np.all(S[:j] <= S[j], axis=1)
            if m.any(): b[j] = b[:j][m].max() + 1
        best = max(best, int(b.max()))
    print(f"RECUR CS(M {M}, A {A}): level keys {len(groups)}; max distinct hub chains inside one level {best}")
