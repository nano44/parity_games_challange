#!/usr/bin/env python3
"""REFEREE-2 succ. 31: own exhaustive counter-search for Theorem HUB-ASC(B) of P-N5-ASC §4, written from the packet's §2 / §4
definitions only (no L-NEW code read or imported).
CS(M): items 1..M (rank = number); a forest is next: items -> items ∪ {⊥} without cycles; chain(x) = x, next(x), ...; the lex order on
sets (S ≤ S′ iff S = S′ or max(S Δ S′) ∈ S′) is the integer order of Σ_{x∈S} 2^x. A run is a sequence of forests with every chain
lex-nondecreasing (pairwise = consecutive, by transitivity); a hub picks h_t ∈ items ∪ {⊥} with chain_t(h_t) nondecreasing.
Exact maximum of the number of distinct hub values over ALL runs and hubs whose value has ≤ B ascents at every time: longest path on
states (forest, hub item), weight 1 when the hub value strictly increases (forests are partially ordered by componentwise chain
integers; equal chain vectors give equal forests). Also SKELETON (a)-(c) on every forest.
Usage: r2hub.py MMAX BMAX"""
import sys, itertools
import numpy as np
MMAX, BMAX = int(sys.argv[1]), int(sys.argv[2])
def forests(M):
    for nx in itertools.product(range(M + 1), repeat=M):          # nx[x-1] = next(x), 0 = ⊥
        if any(nx[x - 1] == x for x in range(1, M + 1)): continue
        ok = True
        for x in range(1, M + 1):
            seen = set(); y = x
            while y:
                if y in seen: ok = False; break
                seen.add(y); y = nx[y - 1]
            if not ok: break
        if ok: yield nx
def chain(nx, x):
    out = []
    while x: out.append(x); x = nx[x - 1]
    return out
def asc(seq): return sum(1 for a, b in zip(seq, seq[1:]) if b > a)
def F(B, M): return 1 + M * (M + 1) // 2 if B == 0 else (M * M + M + 1) * (1 + M * F(B - 1, M) ** 2)
def skeleton(M, FS):
    bad = 0; units = 0
    for nx in FS:
        tau = {x: max([0] + chain(nx, x)[1:]) for x in range(1, M + 1)}
        for x in range(1, M + 1):
            c = chain(nx, x); P = [x]
            while tau[P[-1]]: P.append(tau[P[-1]])
            pos = [c.index(p) if p in c else -1 for p in P]; units += 1
            if -1 in pos or pos != sorted(pos): bad += 1; continue                                   # (a)
            for i in range(len(P) - 1):
                seg = c[pos[i] + 1:pos[i + 1]]
                if any(not (z < P[i + 1] and tau[z] == P[i + 1]) for z in seg): bad += 1             # (b) first half
                if i + 2 < len(P) and not P[i + 2] < P[i + 1]: bad += 1                              # (b) second half
                if seg and not P[i + 1] > seg[-1]: bad += 1                                           # (c)
    return units, bad
for M in range(1, MMAX + 1):
    FS = list(forests(M)); nF = len(FS)
    V = np.array([[sum(1 << x for x in chain(nx, x)) for x in range(1, M + 1)] for nx in FS], dtype=np.int64)
    H = np.concatenate([np.zeros((nF, 1), dtype=np.int64), V], axis=1)                              # hub value per (forest, h), h=0 is ⊥
    A = np.array([[0] + [asc(chain(nx, x)) for x in range(1, M + 1)] for nx in FS])
    order = np.argsort(V.sum(axis=1), kind='stable')
    u, b = skeleton(M, FS)
    row = ['M %d forests %d SKELETON units %d violations %d |' % (M, nF, u, b)]
    for B in range(BMAX + 1):
        best = np.full((nF, M + 1), -1, dtype=np.int64); done = np.zeros(nF, dtype=bool)
        for f in order:
            pred = np.where(done & np.all(V <= V[f], axis=1))[0]
            hs = sorted(range(M + 1), key=lambda h: H[f, h])
            for h in hs:
                if A[f, h] > B: continue
                val = H[f, h]; c = 1
                if len(pred):
                    hv = H[pred]; bv = best[pred]; ok = (hv <= val) & (bv >= 1)
                    if ok.any(): c = max(c, int((bv + (hv < val))[ok].max()))
                same = [best[f, h0] + 1 for h0 in hs if H[f, h0] < val and best[f, h0] >= 1]
                if same: c = max(c, max(same))
                best[f, h] = c
            done[f] = True
        mx = int(best.max()); row.append('B %d: max %d, F_B %d, %s' % (B, mx, F(B, M), 'OK' if mx <= F(B, M) else 'VIOLATION'))
    print(' '.join(row), flush=True)
