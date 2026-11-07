#!/usr/bin/env python3
"""L-LOWER 4: field-by-field diff of two text genomes of equal d (xt, bp, gate, start: changed entries; br: length of the longest
common subsequence of the two rank orders). Usage: diffg.py a.txt b.txt"""
import sys, bisect
def rd(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] in ("xt", "br", "bp", "gate", "start"): D[w[0]] = list(map(int, w[1:]))
    return D
A, B = rd(sys.argv[1]), rd(sys.argv[2])
for k in ("xt", "bp", "gate", "start"):
    print(k, "changed", sum(a != b for a, b in zip(A[k], B[k])), "of", len(A[k]))
ia = sorted(range(len(A["br"])), key=lambda i: A["br"][i]); pos = {v: i for i, v in enumerate(sorted(range(len(B["br"])), key=lambda i: B["br"][i]))}
L = []
for x in (pos[v] for v in ia):
    j = bisect.bisect_left(L, x)
    if j == len(L): L.append(x)
    else: L[j] = x
print("br rank-order LCS", len(L), "of", len(ia))
