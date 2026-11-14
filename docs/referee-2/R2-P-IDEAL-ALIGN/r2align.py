#!/usr/bin/env python3
"""REFEREE-2 succ. 28: independent checks of P-IDEAL-ALIGN on 2-wide R197 ladders (R110's L^R_d) with my own simulator r2sim.py
(from R104's text; beta-SET comparison). Checks ALIGN (a)(b)(c), KP-MOVE (b), F0, PAIR-DOUBLE, MOVES, T-BOUND, PATH-RISE; counts the
equality cases of PAIR-DOUBLE and the largest T per d. Usage: r2align.py SEED NGEN [CORPUS_DIR]"""
import sys, os, random, itertools, glob
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'R2-P-IDEAL-KEYS'))
from r2sim import run, key, xiset, better, par, val, load, wellformed, X
def ladder(R, d):
    N = 2 * d; lev = [x // 2 for x in range(N)]; pi = list(range(N)); R.shuffle(pi)
    g = list(range(2 * N)); R.shuffle(g); r = list(range(2 * N)); R.shuffle(r); O = []; i = 0
    for x in range(N):
        ox = []
        for k in (0, 1):
            cand = [y for y in range(N) if pi[y] > pi[x]]
            xt = R.choice(cand + [X]) if cand and R.random() < 0.85 else X
            ox.append((2 * (lev[x] - 1) + k if lev[x] else -1, xt, g[i], r[i], R.randint(0, 1))); i += 1
        O.append(ox)
    return N, lev, O
def isLR(N, lev, O):
    return N % 2 == 0 and lev == [x // 2 for x in range(N)] and all(len(O[x]) == 2 for x in range(N)) and \
        all(O[x][k][0] == (2 * (lev[x] - 1) + k if lev[x] else -1) for x in range(N) for k in (0, 1))
def npaths(O, z, memo):
    if z in memo: return memo[z]
    v = sum(1 if o[1] == X else npaths(O, o[1], memo) for o in O[z]); memo[z] = v; return v
def KP(O, s, x): return min((0, 1), key=lambda k: key(O, s, x, k))
def ordk(O, s, u, w): return key(O, s, u, s[u]) < key(O, s, w, s[w])
V = dict.fromkeys('ALIGNa ALIGNb ALIGNc KPMOVE F0 PAIRDBL MOVESkf MOVES TBOUND1 TBOUND2 PATHRISE'.split(), 0); C = dict(V); EQ = [0]; TMAX = {}
def check(N, lev, O, starts):
    d = N // 2; PR = par(O); memo = {}; P = [npaths(O, z, memo) for z in range(N)]
    for s0 in starts:
        S = run(N, lev, O, list(s0)); T = len(S) - 1; TMAX[d] = max(TMAX.get(d, 0), T)
        Mv = [None] + [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
        mv = [sum(x in Mv[t] for t in range(1, T + 1)) for x in range(N)]
        F = [sum(ordk(O, S[t], 2 * l, 2 * l + 1) != ordk(O, S[t - 1], 2 * l, 2 * l + 1) for t in range(1, T + 1)) for l in range(d)]
        for s in S:
            for l in range(1, d):
                p, q = 2 * l, 2 * l + 1; b = ordk(O, s, 2 * l - 2, 2 * l - 1); c = 0 if b else 1
                C['ALIGNa'] += 1; V['ALIGNa'] += not (KP(O, s, p) == c == KP(O, s, q))
                ga = lambda j: O[p][j][2] < O[q][j][2]
                want = (s[p] == c) if s[p] != s[q] else ga(s[p])
                C['ALIGNc'] += 1; V['ALIGNc'] += ordk(O, s, p, q) != want
        for t in range(1, T + 1):
            for x in Mv[t]:
                if lev[x] >= 1:
                    l = lev[x]; c = 0 if ordk(O, S[t], 2 * l - 2, 2 * l - 1) else 1
                    C['ALIGNb'] += 1; V['ALIGNb'] += S[t][x] != c
        for x in range(N):
            kf = sum(KP(O, S[t], x) != KP(O, S[t - 1], x) for t in range(1, T + 1))
            C['KPMOVE'] += 1; V['KPMOVE'] += mv[x] > 1 + kf
            if lev[x] >= 1:
                C['MOVESkf'] += 1; V['MOVESkf'] += kf != F[lev[x] - 1]
                C['MOVES'] += 1; V['MOVES'] += mv[x] > 1 + F[lev[x] - 1]
            else: C['MOVES'] += 1; V['MOVES'] += mv[x] > 1
            rises = sum(val(O, S[t], x, S[t][x]) > val(O, S[t - 1], x, S[t - 1][x]) for t in range(1, T + 1))
            C['PATHRISE'] += 1; V['PATHRISE'] += rises > P[x] - 1
        C['F0'] += 1; V['F0'] += F[0] > 2 or F[0] > mv[0] + mv[1]
        for l in range(1, d):
            C['PAIRDBL'] += 1; V['PAIRDBL'] += F[l] > 2 * F[l - 1] + 2; EQ[0] += F[l] == 2 * F[l - 1] + 2
        C['TBOUND1'] += 1; V['TBOUND1'] += T > 2 * d + 2 * sum(F[:d - 1]) or any(F[l] > 2 ** (l + 2) - 2 for l in range(d))
        C['TBOUND2'] += 1; V['TBOUND2'] += T > 2 ** (d + 2) - 2 * d - 4
        yield S, F, mv, P
if __name__ == '__main__':
    seed, ng = int(sys.argv[1]), int(sys.argv[2]); R = random.Random(seed); runs = 0
    for gi in range(ng):
        d = R.randint(1, 6); N, lev, O = ladder(R, d)
        starts = list(itertools.product((0, 1), repeat=N)) if N <= 6 else [tuple(R.randint(0, 1) for _ in range(N)) for _ in range(64)]
        for _ in check(N, lev, O, starts): runs += 1
    nc = 0
    if len(sys.argv) > 3:
        for f in sorted(glob.glob(sys.argv[3] + '/box1[5-7][0-9]/**/*.json', recursive=True)):
            try: N, lev, O, s0 = load(f); wellformed(N, lev, O)
            except Exception: continue
            if len(s0) != N or not isLR(N, lev, O): continue
            nc += 1
            for _ in check(N, lev, O, [tuple(s0)]): runs += 1
    print('SEED', seed, 'random ladders', ng, 'corpus L^R files', nc, 'runs', runs, 'PAIR-DOUBLE equalities', EQ[0], 'max T by d', dict(sorted(TMAX.items())))
    print('CHECKS', ' '.join(f'{k} {C[k]}' for k in C)); print('VIOL', ' '.join(f'{k} {V[k]}' for k in V))
