#!/usr/bin/env python3
"""L-LOWER 6: insert one level at position P into a text genome (old levels P..d-1 shift up by one; movers >= 2P renumbered +2).
New movers Z = 2P, W = 2P + 1 get options (target in OLD numbering or 'Z'/'W'/-1, rank tier = real number among old ranks, parity),
start bits, and the level's four gate values. Importable: insert(D, P, opts, starts, gates) -> new genome dict."""
import copy
def insert(D0, P, opts, starts, gates):
    d0 = D0['d']; N0 = 2 * d0; d = d0 + 1; N = 2 * d; Z = 2 * P
    nid = lambda x: x if x < 0 else (x + 2 if x >= 2 * P else x)
    D = {'d': d, 'xt': [0] * (2 * N), 'br': [0] * (2 * N), 'bp': [0] * (2 * N), 'gate': [0] * (2 * N), 'start': [0] * N}
    key = [0.0] * (2 * N)
    for x in range(N0):
        y = nid(x)
        for k in (0, 1):
            D['xt'][2*y+k] = nid(D0['xt'][2*x+k]); D['bp'][2*y+k] = D0['bp'][2*x+k]; D['gate'][2*y+k] = D0['gate'][2*x+k]
            key[2*y+k] = D0['br'][2*x+k]
        D['start'][y] = D0['start'][x]
    for i, (t, tier, par) in enumerate(opts):
        D['xt'][2*Z+i] = Z if t == 'Z' else (Z + 1 if t == 'W' else nid(t)); D['bp'][2*Z+i] = par; key[2*Z+i] = tier + 1e-3 * (i + 1)
    D['start'][Z], D['start'][Z+1] = starts
    D['gate'][4*P:4*P+4] = gates
    for r, m in enumerate(sorted(range(2 * N), key=lambda m: key[m])): D['br'][m] = r
    return D
