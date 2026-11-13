#!/usr/bin/env python3
"""REFEREE successor 35: membership of G_k in R104's class (docs/red/P-N5-REALIZE.md §2, clause by clause; IDEAL-ACYC) and
L(G_k) on my own IDEAL simulator. usage: gk_member.py kmin kmax [-v]"""
import sys
import time
from collections import Counter
import gk_build as B
import gk_ideal as I

kmin, kmax = int(sys.argv[1]), int(sys.argv[2])
verbose = '-v' in sys.argv
for k in range(kmin, kmax + 1):
    G = B.genome(k)
    N = G['N']; M = sum(G['deg'])
    defs = I.check_def(G)
    acyc = I.xi_acyclic(G)
    # the order-preserving renumbering: same order as the raw values 100*level + eps
    flat = [(G['rawgate'][x][o], G['gate'][x][o]) for x in range(N) for o in range(2)]
    ren_ok = all((a < c) == (b < d) for (a, b) in flat for (c, d) in flat)
    perlev = Counter(G['lev'])
    wires = [x for x in range(N) if G['wt'][x][0] is not None and G['wt'][x][0] == G['wt'][x][1] and G['xt'][x] == ['X', 'X']]
    lev0exit = [x for x in range(N) if G['lev'][x] == 0 and G['xt'][x] == ['X', 'X']]
    t0 = time.time()
    L, why, S = I.run(G, keep=True)
    sw = [sum(1 for j in range(1, L + 1) if S[j][x] != S[j - 1][x]) for x in range(N)]
    dt = time.time() - t0
    print('G_%d: N %d (9k-16 = %d) M %d d %d (k+1 = %d) | DEF clauses %d/%d ok | Xi-acyclic %s | renumbering order-preserving %s | max movers per level %d | wires %d | level-0 movers with both Xi-targets X %d | parities %s | L %d (2^k-2 = %d) stop %s | max sw %d (2^(k-2) = %d) | n3 %d (135k-230 = %d) | %.1fs' % (
        k, N, 9 * k - 16, M, max(G['lev']) + 1, k + 1, sum(1 for _, o, _ in defs if o), len(defs), acyc, ren_ok, max(perlev.values()), len(wires), len(lev0exit),
        sorted(set(G['bp'])), L, 2 ** k - 2, why, max(sw), 2 ** (k - 2), N + 7 * M + 10, 135 * k - 230, dt))
    if verbose:
        for c, o, det in defs: print('   [%s] %s %s' % ('ok' if o else 'FAIL', c, det))
        print('   movers per level:', dict(sorted(perlev.items())))
    sys.stdout.flush()
