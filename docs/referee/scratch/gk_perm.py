#!/usr/bin/env python3
"""REFEREE successor 35: two robustness checks of the rebuild.
RENUM (must be 0): states of the IDEAL run with the raw gate values 100*level + eps differ from the run with the order-preserving
       renumbering onto 0..M-1 (unit: states).
PERM  : N5 from S3 on Gamma3 of G_k with the movers renumbered by a random permutation (the option order of the beta-vertices and
       all vertex indices of movers change with it); counters of gk_reach.py must be 0 and the iteration count must stay 2^k + 1.
usage: gk_perm.py kmin kmax nperm seed"""
import copy
import random
import sys
import rl_engine as eng
import gk_ideal as ideal
import gk_gamma3 as g3
import gk_build as B
import gk_reach as R


def permute(G, p):
    """mover x -> index p[x]"""
    N = G['N']
    H = copy.deepcopy(G)
    inv = [0] * N
    for x in range(N): inv[p[x]] = x
    for key in ('lev', 'deg', 'start'): H[key] = [G[key][inv[y]] for y in range(N)]
    H['wt'] = [[(None if w is None else p[w]) for w in G['wt'][inv[y]]] for y in range(N)]
    H['xt'] = [[('X' if t == 'X' else p[t]) for t in G['xt'][inv[y]]] for y in range(N)]
    for key in ('bid', 'gate'): H[key] = [list(G[key][inv[y]]) for y in range(N)]
    if 'names' in G: H['names'] = [G['names'][inv[y]] for y in range(N)]
    return H


kmin, kmax, nperm, seed = (int(a) for a in sys.argv[1:5])
rnd = random.Random(seed)
for k in range(kmin, kmax + 1):
    G = B.genome(k)
    Graw = copy.deepcopy(G); Graw['gate'] = [list(r) for r in G['rawgate']]
    L, why, S = ideal.run(G, keep=True)
    L2, why2, S2 = ideal.run(Graw, keep=True)
    renum = (0 if (L, why) == (L2, why2) else 1) + sum(1 for a, b in zip(S, S2) if a != b)
    res = []
    for i in range(nperm):
        p = list(range(G['N'])); rnd.shuffle(p)
        H = permute(G, p)
        assert all(o for _, o, _ in ideal.check_def(H)) and ideal.xi_acyclic(H)
        r = R.replay(H, eng, ideal, g3)
        res.append((r['L'], r['iters'], tuple(r['fallbacks']), sum(r['counters'].values())))
    print('G_%d: RENUM %d (L raw %d = L renumbered %d) | PERM %d permutations: (L, iterations, fallback transitions, sum of counters) = %s' % (
        k, renum, L2, L, nperm, sorted(set(res))))
    sys.stdout.flush()
