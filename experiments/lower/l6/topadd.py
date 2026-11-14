#!/usr/bin/env python3
"""L-LOWER 6: TOP-ADD clock test. Adds K levels on top of a text genome (new movers 2d..2d+2K-1, options random targets among all
movers / X, ranks inserted at random positions above R0, random parities/gates/starts), re-points R random existing options to new
movers, and records the max number of moves of any new mover. Usage: topadd.py genome.txt K R0 trials seed"""
import sys, random, copy
from sim6 import rd, run, Fprof, caps
def insert_ranks(D, newm, R0, rng):
    # give new options ranks; existing ranks >= chosen slot shift up (order of old ranks preserved)
    br = D['br']
    for m in newm:
        r = rng.randint(R0, max(br) + 1)
        for i in range(len(br)):
            if br[i] >= r: br[i] += 1
        br[m] = r
def topadd(D0, K, R0, R, rng):
    D = copy.deepcopy(D0); d = D['d']; N = 2 * d; N2 = 2 * (d + K)
    D['d'] = d + K
    for x in range(N, N2):
        for k in (0, 1):
            D['xt'].append(rng.choice(list(range(N2)) + [-1])); D['br'].append(-1); D['bp'].append(rng.randint(0, 1))
    for l in range(d, d + K):
        g = rng.sample(range(5000, 5100), 4); D['gate'] += g
    D['start'] += [rng.randint(0, 1) for _ in range(2 * K)]
    newm = list(range(2 * N, 2 * N2)); 
    for m in newm: D['br'][m] = -10**6
    insert_ranks(D, newm, R0, rng)
    for _ in range(R):
        m = rng.randrange(2 * N); D['xt'][m] = rng.randrange(N, N2)
    return D
if __name__ == '__main__':
    D0 = rd(sys.argv[1]); K, R0, tr, seed = map(int, sys.argv[2:6]); rng = random.Random(seed); best = 0; hist = {}
    R = 2
    for i in range(tr):
        D = topadd(D0, K, R0, R, rng); S, O = run(D)
        if S is None: continue
        d0 = D0['d']; mv = max(sum(1 for t in range(1, len(S)) if S[t][x] != S[t-1][x]) for x in range(2 * d0, 2 * D['d']))
        hist[mv] = hist.get(mv, 0) + 1
    print('max moves of a new mover: histogram', sorted(hist.items()))
