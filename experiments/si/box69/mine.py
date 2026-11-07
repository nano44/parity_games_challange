#!/usr/bin/env python3
"""L-SI box 69: abstract m = 2 dynamics (abs2.c rule, BIT-CHAIN + C-table) on (a) the realisable improvement tables of the exact m = 2
enumeration (tabs_m2.txt) and (b) the abstract counterexamples (T_1 >= 6); property mining. Table format: bit (s*4 + i) = C_i(s)."""
import sys, itertools
def step(C, c1, s, b0):
    ns = s; kp1 = 0 if b0 else 1
    for z in (0, 1):
        cz = (C >> (s * 4 + z)) & 1
        if cz != (s >> z) & 1 and cz == kp1: ns ^= 1 << z
    a, b = ns & 1, (ns >> 1) & 1
    b1 = b0 if (a, b) == (0, 1) else (1 - b0) if (a, b) == (1, 0) else c1[a]
    kp2 = 0 if b1 else 1
    for z in (2, 3):
        cz = (C >> (s * 4 + z)) & 1
        if cz != (s >> z) & 1 and cz == kp2: ns ^= 1 << z
    return ns
def t01(C, c1):
    nx = {(s, b): step(C, c1, s, b) for s in range(16) for b in (0, 1)}; L = {}
    for s in range(16):
        for b in (0, 1):
            u, n, seq = s, 0, [s]
            while nx[(u, b)] != u: u = nx[(u, b)]; n += 1; seq.append(u)
            L[(s, b)] = seq
    T0 = max(len(v) - 1 for v in L.values()); T1 = 0
    for (s, b), seq in L.items():
        for t, u in enumerate(seq): T1 = max(T1, t + len(L[(u, 1 - b)]) - 1)
    return T0, T1
if __name__ == "__main__":
    tabs = [int(l.split()[1], 16) for l in open("tabs_m2.txt")]
    best = {}
    for C in tabs:
        for c1 in ((0, 0), (0, 1), (1, 0), (1, 1)):
            T0, T1 = t01(C, c1); best[T0] = max(best.get(T0, -1), T1)
    print("realisable tables", len(tabs), "D(2, tau) from tables x c1:", dict(sorted(best.items())))
