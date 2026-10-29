#!/usr/bin/env python3
"""L-NEW box 51: DELAY-LINE COUNTER family DLC_d (one-player: every vertex Even; no Odd vertex, so tau is empty and Xi = W).
s: Omega 2, self-loop (the only cycle). Gadget i (0 <= i < d), T = 2^d: x_i -> {hA_i, hB_i}; hA_i -> {s} + the heads of A_i's lines.
Event k = 1 .. T/2^i - 1 owns a private DELAY LINE l_0 .. l_{p-1}, p = 2k*2^i (spacing 2: the arena optimum sees one hop ahead), l_j -> {l_{j+1}, s}, l_{p-1} -> {r_k, s}, r_k -> s with
Omega(r_k) even, rising in k; the line hangs below hA_i if k is odd, below hB_i if k is even. Every other vertex has Omega 0.
Intended run (to be MEASURED, not assumed): l_{p-2}, ..., l_0 switch to the line one hop per N5 iteration (each link becomes improving
only when its successor's W rises), so hA_i / hB_i learn r_k at iteration p and x_i at p + 1: x_i sits on hA_i exactly when bit i of
(t - 1) is 1, and the d edges (x_i, hA_i) are shattered inside one phase. n = O(4^d), so the phase VC would be about (log2 n) / 2.
Usage: vcgad.py d > game.pg"""
import sys
d = int(sys.argv[1]); T = 1 << d
V = []                                             # [prio, succ list]
def new(p, succ=None): V.append([p, list(succ or [])]); return len(V) - 1
s = new(2, []); V[s][1] = [s]; base = 4
for i in range(d):
    x = new(0); hA = new(0, [s]); hB = new(0, [s]); V[x][1] = [hA, hB]
    for k in range(1, T >> i):
        p = 2 * (k << i); r = new(base + 2 * k, [s]); line = [new(0) for _ in range(p)]
        for j in range(p): V[line[j]][1] = [line[j + 1] if j + 1 < p else r, s]
        V[hA if k % 2 else hB][1].append(line[0])
    base += 2 * (T >> i)
print("parity %d;" % (len(V) - 1))
for v, (p, sc) in enumerate(V): print("%d %d 0 %s;" % (v, p, ",".join(map(str, sorted(set(sc))))))
