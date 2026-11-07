#!/usr/bin/env python3
"""BOX L7 (L-LOWER successor 7) check block, run by experiments/lower/check.sh: (1) pins of the frozen L-COMP genome copies;
(2) ranksolve on SL41_d28 reproduces its trajectory; (3) lemma checks on SL41_d28, G7_best_d28 and the four copies: WINDOW-CAP
(F(l) <= 2 W_l - W1_l for l = 1..7) and PULSE-TRIGGER (in every j-window, j = 1..6, with two staggered pair-j moves, closure(q) has a mover
moving at u2 - 1): 0 violations; (4) the F(6) values and guard data of docs/lower/L7-design.md §1-§2. Prints «L7 CHECK PASS»."""
import sys, os, hashlib
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, H)
from sim6 import rd, run, Fprof, caps
from ranksolve import constraints, solve
P = {'LCOMP_L6_TEST1_d28.txt': 'c7a32d08b84554808f9c423d92974ee0d83ec1df', 'LCOMP_L6Z_TEST1_d28.txt': 'a7cca69a8c88f92e07597b3d6e3f708f8b91e8ab',
     'LCOMP_L6_BEST_D_l6_d28.txt': '43e8b5def35e915ebae3a8e5706f367b75094d91', 'LCOMP_D_l6z_best.txt': '1ef15c3b3c2596087a9eabbc49264d6d4f5b765d',
     'LCOMP_L6G_TEST1_d28.txt': '86cf19033924662a418e1cbe6a48e93c285d3bd7'}
for f, h in P.items(): assert hashlib.sha1(open(os.path.join(H, 'rec', f), 'rb').read()).hexdigest() == h, f
print('pins OK:', len(P), 'files')
SL = os.path.join(H, '..', 'l5', 'rec', 'SL41_d28.txt'); G7 = os.path.join(H, '..', 'l4', 'rec', 'G7_best_d28.txt')
D = rd(SL); S, O = run(D); res, core = solve(constraints(D, S), 4 * D['d']); assert res
E = dict(D); E['br'], E['bp'] = res; S2, O2 = run(E); assert S2[:len(S)] == S; print('ranksolve: SL41_d28 trajectory re-solved and reproduced (6,023 conditions)')
def clos(D, x):
    seen = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            y = D['xt'][2 * z + k]
            if y >= 0 and y not in seen: seen.add(y); st.append(y)
    return seen
F6 = {'SL41_d28.txt': 222, 'G7_best_d28.txt': 222, 'LCOMP_L6_TEST1_d28.txt': 117, 'LCOMP_L6Z_TEST1_d28.txt': 160, 'LCOMP_L6_BEST_D_l6_d28.txt': 134, 'LCOMP_D_l6z_best.txt': 190, 'LCOMP_L6G_TEST1_d28.txt': 222}
nwc = npt = 0
for p in [SL, G7] + [os.path.join(H, 'rec', f) for f in P]:
    D = rd(p); S, O = run(D); F = Fprof(D, O); T = len(S) - 1; nm = os.path.basename(p)
    assert caps(F) == 6 and F[6] == F6[nm], (nm, F[6]); assert (12 in clos(D, 10) or 13 in clos(D, 10)) == (nm in ('SL41_d28.txt', 'G7_best_d28.txt')), nm
    for l in range(1, 8):
        ch = [t for t in range(1, T + 1) if O[t][l - 1] != O[t - 1][l - 1]]; W = list(zip([1] + ch, ch + [T + 1]))
        assert F[l] <= 2 * len(W) - sum(1 for a, b in W if b - a == 1), (nm, l); nwc += 1
        if l <= 6:
            for a, b in W:
                ms = [(t, x) for t in range(a, b) for x in (2 * l, 2 * l + 1) if S[t][x] != S[t - 1][x]]
                if len(ms) == 2 and ms[0][0] < ms[1][0]:
                    u2, q = ms[1]; npt += 1
                    assert any(S[u2 - 1][y] != S[u2 - 2][y] for y in clos(D, q)), (nm, l, u2)
print('WINDOW-CAP: 0 violations on', nwc, '(genome, level) pairs; PULSE-TRIGGER: 0 violations on', npt, 'windows with two staggered moves; F(6) values as in L7 §1-§2')
print('L7 CHECK PASS')
