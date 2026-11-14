#!/usr/bin/env python3
"""REFEREE-2 succ. 28: own-simulator checks of P-IDEAL-RISE PHIK-DESCENT (from EVERY state, d <= 4), Corollary PHIK-T,
RISE-EQUIV (a) both halves, (b), (c), MOVE-RISE, MOVE-RISE-R on random 2-wide R197 ladders (r2align.ladder) and on random
IDEAL-ACYC genomes of any degree / width (r2lemmas.rand_genome) for the §4 items. Usage: r2rise.py SEED NGEN"""
import sys, os, random, itertools
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.insert(0, os.path.join(B, 'R2-P-IDEAL-KEYS')); sys.path.insert(0, os.path.join(B, 'R2-P-IDEAL-ALIGN'))
from r2sim import run, key, val, X
from r2align import ladder
from r2lemmas import rand_genome
def kbits(O, s, N): return [int(s[x] != min(range(len(O[x])), key=lambda k: key(O, s, x, k))) for x in range(N)]
def phik(O, s, N, d): return sum((2 ** (d - x // 2) - 1) * b for x, b in enumerate(kbits(O, s, N)))
V = dict(PHIK=0, PHIKT=0, RA1=0, RA2=0, RB=0, RC=0, MR=0, MRR=0); C = dict(V); tight = [0]
def rise_checks(N, O, S):
    T = len(S) - 1; opts = [(x, k) for x in range(N) for k in range(len(O[x]))]
    Vv = [[val(O, s, x, k) for (x, k) in opts] for s in S]; R = [0] * len(opts); rs = 0
    for t in range(1, T + 1):
        anyr = False
        for i in range(len(opts)):
            C['RA1'] += 1
            if Vv[t][i] > Vv[t - 1][i]: R[i] += 1; anyr = True
            elif Vv[t][i] < Vv[t - 1][i]: V['RA1'] += 1
        if t <= T - 1: rs += anyr
        for z in range(N):
            if S[t][z] != S[t - 1][z]:
                C['MR'] += 1; V['MR'] += not (val(O, S[t], z, S[t][z]) > val(O, S[t - 1], z, S[t - 1][z]))
    for i, (x, k) in enumerate(opts):
        z = O[x][k][1]; C['RA2'] += 1; C['RB'] += 1
        cvr = 0 if z == X else sum(val(O, S[t], z, S[t][z]) > val(O, S[t - 1], z, S[t - 1][z]) for t in range(1, T + 1))
        V['RA2'] += R[i] != cvr; V['RB'] += R[i] > T
        if z != X:
            C['MRR'] += 1; V['MRR'] += R[i] < sum(S[t][z] != S[t - 1][z] for t in range(1, T + 1))
    C['RC'] += 1; V['RC'] += T >= 1 and not (T <= 1 + rs <= 1 + sum(R))
if __name__ == '__main__':
    seed, ng = int(sys.argv[1]), int(sys.argv[2]); R = random.Random(seed)
    for gi in range(ng):
        d = R.randint(1, 4); N, lev, O = ladder(R, d)
        for s in itertools.product((0, 1), repeat=N):
            S = run(N, lev, O, list(s), cap=1)
            if len(S) > 1:
                a, b = phik(O, S[0], N, d), phik(O, S[1], N, d); C['PHIK'] += 1; V['PHIK'] += a - b < 1; tight[0] += a - b == 1
        for s in [tuple(R.randint(0, 1) for _ in range(N)) for _ in range(8)]:
            S = run(N, lev, O, list(s)); C['PHIKT'] += 1; V['PHIKT'] += len(S) - 1 > phik(O, S[0], N, d) or phik(O, S[0], N, d) > 2 ** (d + 2) - 2 * d - 4
            rise_checks(N, O, S)
        N2, lev2, O2 = rand_genome(R)
        for s in [tuple(R.randrange(len(O2[x])) for x in range(N2)) for _ in range(8)]:
            rise_checks(N2, O2, run(N2, lev2, O2, list(s)))
    print('SEED', seed, 'ladders', ng, 'any-degree genomes', ng, 'PHIK drop exactly 1:', tight[0])
    print('CHECKS', ' '.join(f'{k} {C[k]}' for k in C)); print('VIOL', ' '.join(f'{k} {V[k]}' for k in V))

def tau_check(d, l, p, R):
    """Build tau(l, p) from packet §3's text with my own choices (random options below l and above l + 1, random distinct gates
    elsewhere), and check the forcing-step Lemma with my simulator."""
    N = 2 * d; q = p ^ 1; lev = [x // 2 for x in range(N)]
    gates = R.sample(range(1000), 2 * N); s = [R.randint(0, 1) for _ in range(N)]
    G = [[gates[2 * x], gates[2 * x + 1]] for x in range(N)]
    def O_of(G, best):
        return [[(2 * (lev[x] - 1) + k if lev[x] else -1, X, G[x][k], 2 * x + (1 if k == best[x] else 0), 0) for k in (0, 1)] for x in range(N)]
    def keyl(G, s, x, k): return key(O_of(G, [0] * N), s, x, k)
    def cl(G, s, l): return 0 if keyl(G, s, 2 * l - 2, s[2 * l - 2]) < keyl(G, s, 2 * l - 1, s[2 * l - 1]) else 1
    if l == 0:
        a, m, b, e = sorted(R.sample(range(1000, 2000), 4)); sp = R.randint(0, 1); sq = R.randint(0, 1)
        s[p], s[q] = sp, sq; G[p][sp], G[p][1 - sp] = b, a; G[q][sq], G[q][1 - sq] = m, e
    else:
        c = cl(G, s, l); s[q] = c; s[p] = 1 - c; before = int(s[2 * l] == c)
        g1, g2 = sorted(R.sample(range(1000, 2000), 2))
        lo, hi = (g1, g2) if before == 0 else (g2, g1)   # gamma_l(c) = [g(2l, c) < g(2l+1, c)] = 1 - before
        G[2 * l][c], G[2 * l + 1][c] = lo, hi
    if l + 1 < d:
        c1 = cl(G, s, l + 1); s[2 * l + 2] = s[2 * l + 3] = c1
    best = [(1 - s[x]) if x == p else s[x] for x in range(N)]; O = O_of(G, best)
    assert len(set(g for gx in G for g in gx)) == 2 * N
    S = run(N, lev, O, list(s), cap=1)
    if len(S) < 2: return False
    k0, k1 = kbits(O, S[0], N), kbits(O, S[1], N); mv = [x for x in range(N) if S[1][x] != S[0][x]]
    ok = mv == [p]
    for x in range(N):
        if x == p: ok &= (k0[x], k1[x]) == (1, 0)
        elif l + 1 < d and lev[x] == l + 1: ok &= (k0[x], k1[x]) == (0, 1)
        else: ok &= k0[x] == k1[x]
    return ok
def tau_main(seed, reps):
    R = random.Random(seed); n = bad = 0
    for d in range(1, 9):
        for l in range(d):
            for p in (2 * l, 2 * l + 1):
                for _ in range(reps): n += 1; bad += not tau_check(d, l, p, R)
    print('TAU', 'transitions', n, 'failures', bad)
