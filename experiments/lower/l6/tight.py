#!/usr/bin/env python3
"""L-LOWER 6: fuel of the second mover in doubling J-windows, classified by mechanism. For every J-window with exactly two pair-J moves
(first f at u1, second q at u2 > u1): the element that turned q's comparison = the decider of q under s_(u2-1); its mover z; whether z
moved at step u2-1 (the last step before q's move) and, if so, whether z was KEY-gated there (its key c changed at that step and z's
preference was already set one state earlier) or Xi (z's preference flipped at the previous state). Tally by window length (u2 - u1 + 1
small = tight) and mechanism. Usage: tight.py genome.txt J"""
import sys
from collections import Counter
from sim6 import rd, run, dec, topo, values
D = rd(sys.argv[1]); J = int(sys.argv[2]); S, O = run(D); T = len(S) - 1; order = topo(D)
V = [values(D, s, order) for s in S]
def pref(t, z):
    m = 2 * z + 1 - S[t][z]; y = D['xt'][m]; bvz = -(1 << D['br'][m]) if D['bp'][m] else (1 << D['br'][m])
    return bvz + (V[t][y] if y >= 0 else 0) > V[t][z]
def key(t, z): l = z // 2; return None if l == 0 else O[t][l - 1]
bst = [t for t in range(1, T + 1) if O[t][J-1] != O[t-1][J-1]]; cuts = [1] + bst + [T + 1]
tal = Counter(); ex = {}
for a, b in zip(cuts, cuts[1:]):
    mv = [(t, x) for t in range(a, b) for x in (2*J, 2*J+1) if S[t][x] != S[t-1][x]]
    if len(mv) != 2 or mv[0][0] == mv[1][0]: continue
    (u1, f), (u2, q) = mv; L = b - a
    r, z, k, side = dec(D, S[u2 - 1], q)
    zm = [t for t in range(u1, u2) if S[t][z] != S[t-1][z]]
    if not zm: mech = 'decider-not-moved'
    else:
        t = zm[-1]
        mech = 'KEY' if (t >= 2 and pref(t - 1, z) and pref(t - 2, z) and key(t, z) != key(t - 1, z)) else ('XI' if t >= 2 and pref(t - 1, z) and not pref(t - 2, z) else 'other')
        mech += f'@u1+{t - u1} lev{z // 2}'
    tal[(f'pulse{u2 - u1}', mech)] += 1; ex.setdefault((f'pulse{u2 - u1}', mech), (a, u1, u2, f, q, z, r))
print(sys.argv[1], 'J', J)
for k, n in sorted(tal.items()): print('  ', n, k, 'e.g. (window start, u1, u2, f, q, supplier, rank)', ex[k])
