#!/usr/bin/env python3
"""REFEREE-2 succ. 28: independent exact re-verification of a P-IDEAL-RISE §5 certificate (classes PHX, PBG), written from the packet's §5
definitions and R104's step (my r2sim.py); no lane code. Rows: dec (genome, s, next), lo (genome, s), hi (genome, s).
Unknowns y_i >= 0 (dec), a_j >= 0 (lo), b_j >= 0 (hi); equations, for EVERY feature f of class PHX:
  sum_i y_i (f(s_i) - f(step s_i)) + sum_j a_j f(lo_j) - sum_j b_j f(hi_j) = 0,   sum_j a_j = 1,   sum_j b_j = 1.
Solved over the rationals (Fraction, own Gaussian elimination); reports rank / free variables / signs and the bound sum_i y_i.
Usage: r2cert.py CERT.json"""
import sys, os, json
from fractions import Fraction as Fr
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'R2-P-IDEAL-KEYS'))
from r2sim import run, key, xiset, better, par, X
def genome(G):
    N = G['N']; O = []
    for x in range(N):
        O.append([(o[0], o[1], G['gate'][x][k], G['br'][o[2]], G['bp'][o[2]]) for k, o in enumerate(G['opts'][x])])
    return N, G['lev'], O
def isLR(N, lev, O):
    return N % 2 == 0 and lev == [x // 2 for x in range(N)] and all(len(O[x]) == 2 for x in range(N)) and \
        all(O[x][k][0] == (2 * (lev[x] - 1) + k if lev[x] else -1) for x in range(N) for k in (0, 1))
def acyclic(N, O):
    col = [0] * N
    def dfs(u):
        col[u] = 1
        for o in O[u]:
            v = o[1]
            if v != X:
                if col[v] == 1: return False
                if col[v] == 0 and not dfs(v): return False
        col[u] = 2; return True
    return all(col[u] or dfs(u) for u in range(N))
def step(N, lev, O, s):
    S = run(N, lev, O, list(s), cap=1); return tuple(S[1]) if len(S) > 1 else None
def height(N, O):
    memo = {}
    def h(x):
        if x not in memo: memo[x] = 1 + max((h(o[1]) if o[1] != X else 0) for o in O[x])
        return memo[x]
    return [h(x) for x in range(N)]
def paths(O, x):  # beta-rank sets of all maximal Xi-paths from x
    out = []
    for k, o in enumerate(O[x]):
        if o[1] == X: out.append(frozenset([o[3]]))
        else: out += [frozenset([o[3]]) | t for t in paths(O, o[1])]
    return out
def ival(O, S):
    PR = par(O); return sum((1 if PR[r] == 0 else -1) * 2 ** r for r in S)
def feats(N, lev, O, s):
    F = feats_base(N, lev, O, s)
    if CLS == 'PHX': F.update(feats_hx(N, lev, O, s, F))
    else: F.update(feats_bg(N, lev, O, s, F))
    return F
def feats_bg(N, lev, O, s, F0):
    F = {}; d = N // 2
    for x in range(N):
        PV = sorted(set(ival(O, t) for t in paths(O, x))); P = len(PV)
        ic = PV.index(ival(O, xiset(O, s, x, s[x])[0])); io = PV.index(ival(O, xiset(O, s, x, 1 - s[x])[0]))
        F[('B1', x)] = Fr(P - 1 - ic); F[('B2', x)] = Fr(P - 1 - ic, max(1, P - 1))
        F[('Bl', lev[x])] = F.get(('Bl', lev[x]), 0) + Fr(P - 1 - ic)
        g = io - ic; F[('G1', x)] = Fr(g); F[('G2', x)] = Fr(max(0, g)); F[('G3', x)] = Fr(max(0, g), max(1, P - 1))
        F[('G4', x)] = F0[('k', x)] * Fr(max(0, g))
    return F
def feats_base(N, lev, O, s):
    PR = par(O); d = N // 2; F = {}
    z = [int(better(xiset(O, s, x, 1 - s[x])[0], xiset(O, s, x, s[x])[0], PR)) for x in range(N)]
    kp = [min((0, 1), key=lambda k: key(O, s, x, k)) for x in range(N)]
    k = [int(s[x] != kp[x]) for x in range(N)]; u = [z[x] * k[x] for x in range(N)]
    for x in range(N): F[('z', x)] = z[x]; F[('k', x)] = k[x]; F[('u', x)] = u[x]
    for l in range(d):
        p, q = 2 * l, 2 * l + 1
        for v in range(16):
            F[('P', l, v)] = int((k[p], k[q], z[p], z[q]) == ((v >> 3) & 1, (v >> 2) & 1, (v >> 1) & 1, v & 1))
        F[('ord', l)] = int(key(O, s, p, s[p]) < key(O, s, q, s[q]))
    return F
def feats_hx(N, lev, O, s, F0):
    d = N // 2; F = {}; z = [F0[('z', x)] for x in range(N)]; k = [F0[('k', x)] for x in range(N)]; u = [F0[('u', x)] for x in range(N)]
    h = height(N, O)
    for l in range(d):
        for x in (2 * l, 2 * l + 1):
            F[('Hz', l, h[x])] = F.get(('Hz', l, h[x]), 0) + z[x]; F[('Hu', l, h[x])] = F.get(('Hu', l, h[x]), 0) + u[x]
    for l in range(d - 1):
        for a in (2 * l, 2 * l + 1):
            for b in (2 * l + 2, 2 * l + 3):
                F[('Xzk', a, b)] = z[a] * k[b]; F[('Xkz', a, b)] = k[a] * z[b]
    return F
def solve(A, rhs, n):  # A: list of dict col->Fr rows; returns (solution or None, rank, inconsistent)
    rows = [(dict(r), Fr(b)) for r, b in zip(A, rhs)]; piv = []; R = []
    for r, b in rows:
        r = {c: v for c, v in r.items() if v != 0}
        for (pc, pr, pb) in R:
            if pc in r:
                f = r[pc]
                for c, v in pr.items(): r[c] = r.get(c, 0) - f * v
                b -= f * pb; r = {c: v for c, v in r.items() if v != 0}
        if not r:
            if b != 0: return None, len(R), True
            continue
        pc = min(r); f = r[pc]; r = {c: v / f for c, v in r.items()}; b = b / f
        newR = []
        for (qc, qr, qb) in R:
            if pc in qr:
                g = qr[pc]
                for c, v in r.items(): qr[c] = qr.get(c, 0) - g * v
                qb -= g * b; qr = {c: v for c, v in qr.items() if v != 0}
            newR.append((qc, qr, qb))
        R = newR + [(pc, r, b)]
    sol = [None] * n
    for pc, r, b in R:
        if len(r) != 1: return None, len(R), False  # free variables remain
        sol[pc] = b
    return sol, len(R), False
if __name__ == '__main__':
    c = json.load(open(sys.argv[1])); d = c['d']; rows = []; bad = 0; CLS = c['cls']
    for tag in ('dec', 'lo', 'hi'):
        for r in c[tag]:
            N, lev, O = genome(r['genome'])
            if not (isLR(N, lev, O) and acyclic(N, O) and N == 2 * d): bad += 1
            s = tuple(r['s'])
            if tag == 'dec':
                n = step(N, lev, O, s)
                if n is None or list(n) != r['next']: bad += 1; print('STEP MISMATCH', s, n, r['next'])
                f0, f1 = feats(N, lev, O, s), feats(N, lev, O, n)
                rows.append(('dec', {kk: f0.get(kk, 0) - f1.get(kk, 0) for kk in set(f0) | set(f1)}))
            else:
                rows.append((tag, feats(N, lev, O, s)))
    n = len(rows); names = sorted(set().union(*[set(v) for _, v in rows]), key=str)
    A = []; rhs = []
    for f in names:
        A.append({j: Fr(rows[j][1].get(f, 0) * (1 if rows[j][0] != 'hi' else -1)) for j in range(n)}); rhs.append(0)
    A.append({j: Fr(1) for j in range(n) if rows[j][0] == 'lo'}); rhs.append(1)
    A.append({j: Fr(1) for j in range(n) if rows[j][0] == 'hi'}); rhs.append(1)
    sol, rank, inc = solve(A, rhs, n)
    print('rows', n, 'features', len(names), 'bad rows', bad, 'rank', rank, 'inconsistent', inc, 'unique', sol is not None)
    if sol is not None:
        neg = sum(1 for v in sol if v < 0); bound = sum(sol[j] for j in range(n) if rows[j][0] == 'dec')
        print('negative', neg, 'bound', bound, float(bound), 'VERIFIED' if neg == 0 and not bad else 'NOT VERIFIED')
        print('max |y_float - y_exact|', max(abs(float(sol[j]) - r['y']) for j, r in enumerate(c['dec'] + c['lo'] + c['hi'])))
