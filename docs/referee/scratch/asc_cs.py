#!/usr/bin/env python3
"""REFEREE successor 27: P-N5-ASC abstract DATA with my own code (no L-NEW code imported).
CS(M): items 1..M, forests = acyclic next maps; a chain is a set, encoded as the bitmask sum 2^(x-1); lex order on sets (the top of the
symmetric difference lies in the larger) = integer order of the masks. A run: every chain mask non-decreasing. A hub: an item (or none,
mask 0) whose chain mask is non-decreasing. Max distinct hub values = 1 + longest chain of (forest, hub) nodes with componentwise <= masks
and strictly larger hub mask (transitivity of <= makes consecutive steps enough; equal-value steps are not needed).
Nodes in a valid topological order: by (sum of masks, hub mask). Usage: asc_cs.py max M B | rmon"""
import sys, itertools
import numpy as np

def forests(M):
    for par in itertools.product(range(M + 1), repeat=M):   # par[x-1] = next(x), 0 = bottom
        chains = []; ok = True
        for x in range(1, M + 1):
            seq = [x]; y = par[x - 1]
            while y:
                if y in seq: ok = False; break
                seq.append(y); y = par[y - 1]
            if not ok: break
            chains.append(seq)
        if ok: yield chains

def asc(seq): return sum(1 for p, q in zip(seq, seq[1:]) if q > p)
def mask(seq): return sum(1 << (x - 1) for x in seq)

def maxhub(M, B):
    rows = []
    for ch in forests(M):
        ms = [mask(c) for c in ch]
        rows.append(ms + [0])
        for h in range(M):
            if asc(ch[h]) <= B: rows.append(ms + [ms[h]])
    A = np.array(rows, dtype=np.int64)
    order = np.lexsort((A[:, -1], A[:, :-1].sum(axis=1))); A = A[order]
    best = np.ones(len(A), dtype=np.int64)
    for j in range(len(A)):
        pred = np.all(A[:j, :-1] <= A[j, :-1], axis=1) & (A[:j, -1] < A[j, -1])
        if pred.any(): best[j] = best[:j][pred].max() + 1
    return int(best.max()), len(A)

def F(B, M):
    f = 1 + M * (M + 1) // 2
    for _ in range(B): f = (M * M + M + 1) * (1 + M * f * f)
    return f

def rmon():
    before = {1: [1, 2, 5, 4], 2: [2, 5, 4], 3: [3, 4], 4: [4], 5: [5, 4]}
    after = {1: [1, 5, 3, 4], 2: [2, 1, 5, 3, 4], 3: [3, 4], 4: [4], 5: [5, 3, 4]}
    def forest_ok(C):   # chains must come from one next map: chain(x) = x + chain(next(x))
        return all(C[x][1:] == (C[C[x][1]] if len(C[x]) > 1 else []) for x in C)
    tau = lambda C: tuple(max(C[x][1:], default=0) for x in sorted(C))
    print("RMON-2 witness CS(5, 2): forests valid", forest_ok(before), forest_ok(after),
          "| every chain lex-nondecreasing", all(mask(before[x]) <= mask(after[x]) for x in before),
          "| max ascents", max(asc(c) for c in list(before.values()) + list(after.values())),
          "| tau before", tau(before), "after", tau(after))
    part = lambda C, w: C[w][:C[w].index(max(C[w][1:]))]
    print("  part of chain(1) before tau(1) = 5: before", part(before, 1), "after", part(after, 1),
          "| decreases:", mask(part(after, 1)) < mask(part(before, 1)),
          "| chain(5) =", before[5], "->", after[5], "(changed: P-N5-ASC (ii) conditions on chain(y) = C, so this step is outside it)")

if __name__ == "__main__":
    if sys.argv[1] == "rmon": rmon()
    else:
        M, B = int(sys.argv[2]), int(sys.argv[3]); m, n = maxhub(M, B)
        print(f"CS(M {M}), hub <= {B} ascents: max distinct hub values {m} (nodes {n}); F_{B}(M) = {F(B, M)}; F_0(M) = {F(0, M)}")
