#!/usr/bin/env python3
"""REFEREE successor 35: the family G_k (k >= 3) rebuilt from the TEXT of the rule relayed by the Lead (message of 12:41Z,
2026-11-13) only. No file of claude/l-red-b, claude/l-red, claude/l-new, claude/l-comp or docs/referee-2 was read for it.
raw(k)   -> the dict in the lanes' JSON form (keys N, lev, deg, opts, gate, br, bp, start; gate = 100*level + eps, as generated)
genome(k)-> my own genome dict (gk_ideal.py) with the ORDER-PRESERVING renumbering of the gate values onto 0..M-1
names(k) -> mover names in file order
usage: gk_build.py sha k...   prints sha1 of json.dumps(raw(k)) ; gk_build.py dump k path"""
import hashlib
import json
import sys


def movers(k):
    """file order: u0 v0; u1 v1 ... u(k-1) v(k-1); e2 ... e(k-2); wv1 ... wv(k-2); wu2 ... wu(k-2);
    y1 yb1 ... y(k-1) yb(k-1); yp2 ypb2 ... yp(k-2) ypb(k-2)"""
    names = []
    for j in range(0, k): names += [('u', j), ('v', j)]
    for j in range(2, k - 1): names.append(('e', j))
    for j in range(1, k - 1): names.append(('wv', j))
    for j in range(2, k - 1): names.append(('wu', j))
    for j in range(1, k): names += [('y', j), ('yb', j)]
    for j in range(2, k - 1): names += [('yp', j), ('ypb', j)]
    return names


def raw(k):
    assert k >= 3
    names = movers(k)
    ix = {nm: i for i, nm in enumerate(names)}
    N = len(names)
    assert N == 9 * k - 16
    X = -1; NONE = -1

    def E(j):                      # E(j) := e_j for j <= k-2, u_(k-1) for j = k-1
        return ('e', j) if j <= k - 2 else ('u', k - 1)
    lev = [None] * N; opts = [None] * N; eps = [None] * N; dl = [None] * N; start = [None] * N; dep = [None] * N
    for nm, i in ix.items():
        t, j = nm
        if t in ('u', 'v') and j == 0:
            lev[i] = 0
            W = (NONE, NONE); XI = (X, X)
            if t == 'u': eps[i] = (2, 5); dl[i] = (2, 0)
            else: eps[i] = (3, 1); dl[i] = (1, 3)
            start[i] = 0; dep[i] = 0
        elif t in ('u', 'v'):
            lev[i] = j
            W = (ix[('u', j - 1)], ix[('v', j - 1)])              # option o: W -> member o of (u_(j-1), v_(j-1))
            if t == 'u': XI = (ix[('yb', j)], ix[('y', j)]); eps[i] = (2, 3); dl[i] = (1, 0)
            else: XI = (ix[('y', j)], ix[('yb', j)]); eps[i] = (4, 5); dl[i] = (3, 2)
            start[i] = 0; dep[i] = 2 * j
        elif t == 'e':
            lev[i] = j
            W = (ix[('u', j - 1)], ix[('v', j - 1)])
            XI = (ix[('ypb', j)], ix[('yp', j)]); eps[i] = (0, 1); dl[i] = (4, 5)
            start[i] = 0; dep[i] = 2 * j + 1
        elif t == 'wv':
            lev[i] = j + 1
            W = (ix[('v', j)], ix[('v', j)]); XI = (X, X); eps[i] = (6, 7); dl[i] = (1, 0)
            start[i] = 0; dep[i] = 2 * k + 5
        elif t == 'wu':
            lev[i] = j + 1
            W = (ix[('u', j)], ix[('u', j)]); XI = (X, X); eps[i] = (8, 9); dl[i] = (3, 2)
            start[i] = 0; dep[i] = 2 * k + 5
        elif t in ('y', 'yb'):
            top = (j == k - 1)
            lev[i] = k if top else j + 2
            if top: W = (ix[('u', k - 1)], ix[('v', k - 1)])
            else: W = (ix[('wv', j)], ix[E(j + 1)])
            if t == 'y':
                XI = (ix[('u', j - 1)], ix[('v', j - 1)]); eps[i] = (20, 21) if top else (10, 11); dl[i] = (1, 3); start[i] = 0
            else:
                XI = (ix[('v', j - 1)], ix[('u', j - 1)]); eps[i] = (22, 23) if top else (12, 13); dl[i] = (0, 2); start[i] = 1
            dep[i] = 2 * j - 1
        elif t in ('yp', 'ypb'):
            lev[i] = j + 2
            W = (ix[('wu', j)], ix[E(j + 1)])
            if t == 'yp':
                XI = (ix[('yb', j)], ix[('y', j)]); eps[i] = (14, 15); dl[i] = (5, 7); start[i] = 0
            else:
                XI = (ix[('y', j)], ix[('yb', j)]); eps[i] = (16, 17); dl[i] = (4, 6); start[i] = 1
            dep[i] = 2 * j
        else:
            raise ValueError(nm)
        opts[i] = [[W[o], XI[o], 2 * i + o] for o in (0, 1)]       # beta-id of (mover i, option o) = 2i + o
    M = 2 * N
    # br = the rank order of the pair (2k + 5 - dep, dl), ties by beta-id
    keyb = {}
    for i in range(N):
        for o in (0, 1): keyb[2 * i + o] = (2 * k + 5 - dep[i], dl[i][o], 2 * i + o)
    order = sorted(range(M), key=lambda b: keyb[b])
    br = [None] * M
    for r, b in enumerate(order): br[b] = r
    gate = [[100 * lev[i] + eps[i][o] for o in (0, 1)] for i in range(N)]
    G = {'N': N, 'lev': lev, 'deg': 2, 'opts': opts, 'gate': gate, 'br': br, 'bp': [0] * M, 'start': start}
    return G


def sha(k):
    return hashlib.sha1(json.dumps(raw(k)).encode()).hexdigest()


def genome(k):
    """my genome dict; gate values renumbered order-preservingly onto 0..M-1."""
    R = raw(k)
    N = R['N']
    vals = sorted(g for row in R['gate'] for g in row)
    assert len(set(vals)) == len(vals), 'gate values not distinct'
    ren = {g: i for i, g in enumerate(vals)}
    G = {'N': N, 'lev': list(R['lev']), 'deg': [2] * N,
         'wt': [[(o[0] if o[0] >= 0 else None) for o in R['opts'][x]] for x in range(N)],
         'xt': [[(o[1] if o[1] >= 0 else 'X') for o in R['opts'][x]] for x in range(N)],
         'bid': [[o[2] for o in R['opts'][x]] for x in range(N)],
         'gate': [[ren[g] for g in row] for row in R['gate']], 'rawgate': [list(r) for r in R['gate']],
         'br': list(R['br']), 'bp': list(R['bp']), 'start': list(R['start']),
         'names': ['%s%d' % nm for nm in movers(k)]}
    return G


if __name__ == '__main__':
    if sys.argv[1] == 'sha':
        for a in sys.argv[2:]: print('G_%s sha1 %s N %d' % (a, sha(int(a)), raw(int(a))['N']))
    elif sys.argv[1] == 'dump':
        json.dump(raw(int(sys.argv[2])), open(sys.argv[3], 'w'))
