#!/usr/bin/env python3
"""REFEREE-2 succ. 31: own replay of packet P-TOWER-FUEL (claude/l-lower 7f7ff6f5) on my R104 IDEAL simulator
(R2-P-IDEAL-MOVES/r2moves.py class G; no lane code imported). Text genomes read by my own parser from the R110 text format
(option m = 2x + k: xt[m], br[m], bp[m], gate[m]; W-target of (x, k) = 2(lev(x) - 1) + k, R110).
Usage: r2tower.py ROOT   (ROOT = a checkout / `git archive` of 7f7ff6f5)
Prints: per-genome T and F; §4 instance counts (I-ROOM, I-FUEL) with every attribution I use; §5 counters (same units as the packet)
plus my extra checks: MOVE iff (every mover of level >= 1, every step), (E1)/(E2) directly, (E5) gamma equality on EVERY doubling
level, DOMINANCE-FREEZE (a) as a pointwise parity rule at every (state, mover), CROSS-ECONOMY (iii) at every state of every crossed pair,
and the two inequalities of the packet's proof of (iii) (|D| >= 2^r*, 2^r* > 2 max|theta|) counted where they FAIL."""
import sys, os, json, glob, hashlib
H = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(H, '..', 'R2-P-IDEAL-MOVES', 'r2moves.py')).read().split("\nif __name__")[0]
ns = {'__name__': 'lib'}; a_ = sys.argv; sys.argv = ['x']; exec(src, ns); sys.argv = a_
G, X = ns['G'], ns['X']
ROOT = sys.argv[1]

def txt_genome(p):
    D = {}
    for ln in open(p):
        w = ln.split()
        if w and w[0] in ('d', 'xt', 'br', 'bp', 'gate', 'start'): D[w[0]] = list(map(int, w[1:]))
    d = D['d'][0]; N = 2 * d
    assert all(len(D[k]) == 2 * N for k in ('xt', 'br', 'bp', 'gate')) and len(D['start']) == N
    opts = [[[2 * (x // 2 - 1) + k if x // 2 else -1, D['xt'][2 * x + k], 2 * x + k] for k in (0, 1)] for x in range(N)]
    return dict(N=N, lev=[x // 2 for x in range(N)], opts=opts, gate=[[D['gate'][2 * x], D['gate'][2 * x + 1]] for x in range(N)],
                br=D['br'], bp=D['bp'], start=D['start'])

class Run:
    def __init__(s, raw):
        s.raw = raw; s.g = g = G(raw); assert g.ok_lr(), 'not L^R_d / not acyclic'
        s.N = g.N; s.d = s.N // 2; s.S = g.run(list(g.start)); s.T = len(s.S) - 1
        ck = [[g.key(st, x, st[x]) for x in range(s.N)] for st in s.S]
        s.ord = [[ck[t][2 * l] < ck[t][2 * l + 1] for l in range(s.d)] for t in range(s.T + 1)]   # True: 2l has the smaller key
        s.F = [sum(s.ord[t][l] != s.ord[t - 1][l] for t in range(1, s.T + 1)) for l in range(s.d)]
        s.dbl = [l >= 1 and s.F[l] == 2 * s.F[l - 1] + 2 for l in range(s.d)]
        s.mv = [None] + [{x for x in range(s.N) if s.S[t][x] != s.S[t - 1][x]} for t in range(1, s.T + 1)]
    def c(s, j, t): return 0 if s.ord[t][j - 1] else 1                     # c_j(s_t), R113
    def windows(s, j):
        b = [t for t in range(1, s.T + 1) if s.c(j, t) != s.c(j, t - 1)]
        starts = [1] + [t for t in b if t > 1]; ends = [x - 1 for x in starts[1:]] + [s.T]
        out = []
        for a, e in zip(starts, ends):
            mv = [(t, x) for t in range(a, e + 1) for x in (2 * j, 2 * j + 1) if x in s.mv[t]]
            out.append((a, e, mv))
        return out, b
    def chain(s, st, x, k):  # option indices m on the Xi-path of (x, k) under st
        out = []
        while True:
            m = 2 * x + k; out.append(m); y = s.g.O[x][k][1]
            if y == X: return out
            x, k = y, st[y]
    def rank(s, m): return s.raw['br'][m]
    def par(s, m): return s.raw['bp'][m]
    def eps(s, m): return (1 if s.par(m) == 0 else -1) << s.rank(m)
    def dec(s, st, x):
        A = set(s.chain(st, x, 0)); B = set(s.chain(st, x, 1)); m = max(A ^ B, key=s.rank); return m, (0 if m in A else 1)
    def pi(s, st, x):
        v0, v1 = s.g.val(st, x, 0), s.g.val(st, x, 1); assert v0 != v1; return 0 if v0 > v1 else 1
    def cv(s, st, x): return s.g.val(st, x, st[x])

def load(p): return Run(txt_genome(p) if p.endswith('.txt') else json.load(open(p)))
sha = lambda p: hashlib.sha1(open(p, 'rb').read()).hexdigest()
L = os.path.join(ROOT, 'experiments', 'lower')
G7 = os.path.join(L, 'l4', 'rec', 'G7_best_d28.txt'); SL = os.path.join(L, 'l5', 'rec', 'SL41_d28.txt')
print('sha1', sha(G7), 'G7_best_d28.txt;', sha(SL), 'SL41_d28.txt')
R7, RS = load(G7), load(SL)
print('start G7', ''.join(map(str, R7.g.start)), '| start SL41', ''.join(map(str, RS.g.start)))

# ---- §4 instances
def slack(R, j, need):
    W, _ = R.windows(j); P = []; Gp = []
    for i, (a, e, mv) in enumerate(W):
        assert len(mv) == 2 and len({t for t, _ in mv}) == 2
        opener = tuple(sorted((x, R.S[a][x]) for x in R.mv[a] if x in (2 * j - 2, 2 * j - 1))) if a > 1 else 'first'
        pu = mv[1][0] - mv[0][0]
        if pu < need: P.append((a, pu, opener))
        if i + 1 < len(W):
            gp = W[i + 1][2][0][0] - mv[1][0]
            if gp < need: Gp.append((a, gp, opener, W[i + 1][0], W[i + 1][2][0][0]))
    return W, P, Gp
for name, R in (('I-ROOM G7_best_d28', R7), ('I-FUEL SL41_d28', RS)):
    print('==', name, 'T', R.T, 'F', R.F, 'capped 0-5', all(R.F[l] == 2 ** (l + 2) - 2 for l in range(6)), 'dbl 1-5', R.dbl[1:6], 'dbl6', R.dbl[6])
    for j in range(1, 6):
        W, P, Gp = slack(R, j, 7 - j)
        from collections import Counter
        print('  level', j, 'windows', len(W), 'need', 7 - j, 'PULSE viol', len(P), 'GAP viol', len(Gp),
              'PULSE lengths', dict(Counter(p[1] for p in P)), 'GAP lengths', dict(Counter(g[1] for g in Gp)),
              'PULSE openers', dict(Counter(p[2] for p in P)), 'GAP openers (earlier window W)', dict(Counter(g[2] for g in Gp)))
        if Gp:
            inside = sum(1 for g in Gp if True)
            print('    GAP intervals [u2(W), u1(W+)-1] cross into W+ (u1(W+) > opening of W+):', sum(1 for g in Gp if g[4] > g[3]), 'of', len(Gp))
    W6, _ = R.windows(6)
    bad = [w for w in W6 if sorted(x for _, x in w[2]) != [12, 13]]
    print('  level 6 windows', len(W6), 'without exactly one move of each of 12, 13:', len(bad),
          'move-count profile', dict(Counter(tuple(sorted(x for _, x in w[2])) for w in W6)))
# I-FUEL decider
o = RS.g.O
print('SL41 xt(12,0..1)', o[12][0][1], o[12][1][1], 'xt(13,0..1)', o[13][0][1], o[13][1][1], '| option 19 = (9,1): rank', RS.rank(19), 'parity', RS.par(19),
      '| xt(11,0..1)', o[11][0][1], o[11][1][1], 'xt(22,0..1)', o[22][0][1], o[22][1][1])
W6, _ = RS.windows(6); bad = {w[0] for w in W6 if sorted(x for _, x in w[2]) != [12, 13]}
cnt = Counter()
for a, e, mv in W6:
    states = range(a - 1, e)                       # s_(a-1) .. s_(e-1): the pre-states of the window's steps
    per = {x: [RS.dec(RS.S[t], x)[0] == 19 for t in states] for x in (12, 13)}
    some = any(any(v) for v in per.values()); every12 = all(per[12]); every13 = all(per[13]); every_or = all(a1 or b1 for a1, b1 in zip(per[12], per[13]))
    cnt[('fail' if a in bad else 'good', 'some', some)] += 1
    cnt[('fail' if a in bad else 'good', 'every-state 12', every12)] += 1
    cnt[('fail' if a in bad else 'good', 'every-state 13', every13)] += 1
    cnt[('fail' if a in bad else 'good', 'every-state 12-or-13', every_or)] += 1
    # extended range including s_e (the window's last state)
    some_e = any(RS.dec(RS.S[t], x)[0] == 19 for t in range(a - 1, e + 1) for x in (12, 13))
    cnt[('fail' if a in bad else 'good', 'some incl s_e', some_e)] += 1
    p9 = all(RS.S[t][9] == 1 for t in states); cnt[('fail' if a in bad else 'good', 'mover 9 on option 1 at every pre-state', p9)] += 1
for k in sorted(cnt, key=str): print('  decider', k, cnt[k])

# ---- §5 counters on the corpus
files = sorted(glob.glob(os.path.join(L, 'l3', 'kill', '*.json')) + glob.glob(os.path.join(L, 'l4', 'rec', '*.json')))
runs = [(os.path.basename(f), load(f)) for f in files] + [('G7_best_d28', R7), ('SL41_d28', RS)]
C = Counter()
for name, R in runs:
    C['runs'] += 1; C['steps'] += R.T
    for t in range(1, R.T + 1):                        # Lemma 0 MOVE iff, every mover of level >= 1
        for x in range(2, R.N):
            l = x // 2; prev = R.S[t - 1][x]; better = R.pi(R.S[t - 1], x) != prev
            C['MOVE_units'] += 1; C['MOVE_viol'] += (x in R.mv[t]) != (better and R.c(l, t) != prev)
            if x in R.mv[t]: C['MOVE_viol'] += R.S[t][x] != R.c(l, t)
    for t in range(R.T + 1):                           # Lemma 4 (a), pointwise parity rule
        for x in range(R.N):
            m, k = R.dec(R.S[t], x); C['DFa_point'] += 1; C['DFa_point_viol'] += R.pi(R.S[t], x) != (k if R.par(m) == 0 else 1 - k)
    for t in range(1, R.T + 1):                        # Lemma 4 (a), the lane's unit
        for x in range(R.N):
            if R.dec(R.S[t - 1], x) == R.dec(R.S[t], x):
                C['DFa_pairs'] += 1; C['DFa_viol'] += R.pi(R.S[t - 1], x) != R.pi(R.S[t], x)
    for j in range(1, R.d):
        p, q = 2 * j, 2 * j + 1
        A0, A1 = R.g.O[p][0][1], R.g.O[p][1][1]
        crossed = A0 != X and A1 != X and A0 != A1 and R.g.O[q][0][1] == A1 and R.g.O[q][1][1] == A0
        if crossed:                                    # (iii) at every state of every crossed pair (doubling or not)
            C['CR_pairs'] += 1; own = max(R.rank(2 * x + k) for x in (p, q) for k in (0, 1))
            th = {p: R.eps(2 * p + 1) - R.eps(2 * p), q: R.eps(2 * q) - R.eps(2 * q + 1)}
            assert not (set(R.chain(R.S[0], A0, R.S[0][A0])) | set(R.chain(R.S[0], A1, R.S[0][A1]))) & {2 * p, 2 * p + 1, 2 * q, 2 * q + 1}
            for st in R.S:
                Dv = R.cv(st, A0) - R.cv(st, A1)
                C['CRi_units'] += 1
                C['CRi_viol'] += (R.pi(st, p) == 0) != (Dv > th[p]) or (R.pi(st, q) == 1) != (Dv > th[q])
                sd = set(R.chain(st, A0, st[A0])) ^ set(R.chain(st, A1, st[A1])); rs = max(R.rank(m) for m in sd)
                if rs > own:
                    C['RANK_states'] += 1
                    C['iii_pointwise_viol'] += not ((Dv > th[p]) == (Dv > th[q]) == (Dv > 0))
                    C['proof_ineq1_fails(|D|<2^r*)'] += abs(Dv) < (1 << rs)
                    C['proof_ineq2_fails(|D|<=2max|th|)'] += abs(Dv) <= 2 * max(abs(th[p]), abs(th[q]))
                    C['repair_fails(|D|<=max|th|)'] += abs(Dv) <= max(abs(th[p]), abs(th[q]))
        if not R.dbl[j]: continue
        C['levels'] += 1; W, B = R.windows(j)
        Phi = [(R.S[t][p] != R.c(j, t)) + (R.S[t][q] != R.c(j, t)) for t in range(R.T + 1)]
        C['E1'] += not (Phi[0] == 2 and Phi[R.T] == 0); C['E2'] += sum(Phi[t - 1] != 0 for t in B)
        for t in range(1, R.T + 1):
            mp, mq = p in R.mv[t], q in R.mv[t]; fl = R.ord[t][j] != R.ord[t - 1][j]
            C['E3_units'] += 1; C['E3'] += (mp and mq) or ((mp or mq) != fl)
        firsts = set()
        for a, e, mv in W:
            C['windows'] += 1; C['E4'] += sorted(x for _, x in mv) != [p, q] or len({t for t, _ in mv}) != 2
            if len(mv) == 2: firsts.add(min(mv)[1])
        C['E5'] += R.F[j - 1] >= 1 and len(firsts) > 1
        gam = [R.g.O[p][k][2] < R.g.O[q][k][2] for k in (0, 1)]
        C['E5_gamma_all_dbl_levels_viol'] += gam[0] != gam[1]; C['E5_F(j-1)=0_levels'] += R.F[j - 1] == 0
        k = 0
        while j + k + 1 < R.d and R.dbl[j + k + 1]: k += 1
        for i, (a, e, mv) in enumerate(W):
            pu = mv[1][0] - mv[0][0]; C['PN_units'] += 1; C['PN_viol'] += pu < k + 1; C['PN_tight'] += pu == k + 1
            if k >= 1 and i + 1 < len(W):
                gp = W[i + 1][2][0][0] - mv[1][0]; C['GN_units'] += 1; C['GN_viol'] += gp < k + 1; C['GN_tight'] += gp == k + 1
        for x in (p, q):
            ts = [t for t in range(1, R.T + 1) if x in R.mv[t]]
            for t, t2 in zip(ts, ts[1:]):
                C['DFb_pairs'] += 1; C['DFb_viol'] += len({R.dec(R.S[v], x) for v in range(t - 1, t2)}) == 1
        if crossed:
            C['CE_pairs'] += 1; C['CE_pair_names'] += 0; print('  crossed doubling pair:', name, 'level', j, 'A0, A1 =', A0, A1)
            own = max(R.rank(2 * x + kk) for x in (p, q) for kk in (0, 1))
            th = {p: R.eps(2 * p + 1) - R.eps(2 * p), q: R.eps(2 * q) - R.eps(2 * q + 1)}
            Dd = lambda st: R.cv(st, A0) - R.cv(st, A1)
            def rh(st):
                sd = set(R.chain(st, A0, st[A0])) ^ set(R.chain(st, A1, st[A1])); return max(R.rank(m) for m in sd) > own
            for a, e, mv in W:
                (u1, f), (u2, x2) = mv; C['CE_windows'] += 1
                C['CE_viol'] += (Dd(R.S[u1 - 1]) > th[f]) == (Dd(R.S[u2 - 1]) > th[x2])
                if rh(R.S[u1 - 1]) and rh(R.S[u2 - 1]):
                    C['CE3_units'] += 1; C['CE3_viol'] += (Dd(R.S[u1 - 1]) > 0) == (Dd(R.S[u2 - 1]) > 0)
print('corpus', len(runs), 'runs:', ' '.join('%s(T%d)' % (n, R.T) for n, R in runs))
for k in sorted(C): print('  %-36s %d' % (k, C[k]))
