#!/usr/bin/env python3
"""REFEREE-2 succ. 29: own check of packet P-IDEAL-MOVES (l-new d86adc86). Own IDEAL simulator written from RESULTS R104's text
(beta-SETS compared by the largest-rank beta of the symmetric difference; A-sets under the old state; keys = gate indices of the
W-chain under the NEW state, lowest level first, then the option's own gate). No lane code imported.
Usage: r2moves.py ROOT [--random K] [--neg]
  ROOT   = an experiments/new directory (corpus: every L^R_d genome JSON under box150..box187; every start for N <= 10, else stored)
  --random K: also K random acyclic L^R_d genomes per d = 2..6 (seed 29), every start for N <= 10, else 64 random starts
  --neg  : negative control, keys read under the OLD state (counters must fire)
Prints violation counters (all must be 0 without --neg), info counts, a sha1 of all runs, and the DEAD instances."""
import os, sys, json, glob, itertools, random, hashlib
X = -1
NEG = '--neg' in sys.argv

class G:
    def __init__(s, g):
        s.N = g['N']; s.lev = g['lev']; s.O = []
        for x in range(s.N):
            s.O.append([(o[0], o[1], g['gate'][x][k], g['br'][o[2]], g['bp'][o[2]]) for k, o in enumerate(g['opts'][x])])
        s.PR = {o[3]: o[4] for ox in s.O for o in ox}
        s.order = sorted(range(s.N), key=lambda x: s.lev[x])
        s.start = list(g.get('start', [0] * s.N))
    def ok_lr(s):  # R110: movers 2l, 2l+1 on level l, deg 2, option k of level l >= 1 W-points to 2(l-1)+k; distinct gates/ranks; acyclic
        N = s.N
        if N % 2 or s.lev != [v // 2 for v in range(N)]: return False
        if any(len(s.O[x]) != 2 for x in range(N)): return False
        for x in range(N):
            for k in range(2):
                if s.O[x][k][0] != (2 * (s.lev[x] - 1) + k if s.lev[x] else -1): return False
        gates = [o[2] for ox in s.O for o in ox]; ranks = [o[3] for ox in s.O for o in ox]
        if len(set(gates)) != len(gates) or len(set(ranks)) != len(ranks): return False
        return s.acyclic()
    def acyclic(s):
        col = [0] * s.N
        def dfs(u):
            col[u] = 1
            for o in s.O[u]:
                v = o[1]
                if v != X:
                    if col[v] == 1 or (col[v] == 0 and not dfs(v)): return False
            col[u] = 2; return True
        return all(col[u] or dfs(u) for u in range(s.N))
    def chain(s, st, x, k):  # list of (mover, option) on the chain of (x, k) under st
        out = [(x, k)]
        while s.O[out[-1][0]][out[-1][1]][1] != X:
            y = s.O[out[-1][0]][out[-1][1]][1]; out.append((y, st[y]))
        return out
    def bset(s, st, x, k): return frozenset(s.O[y][j][3] for y, j in s.chain(st, x, k))
    def better(s, P, Q):
        D = P ^ Q
        if not D: return False
        r = max(D); return (r in P) == (s.PR[r] == 0)
    def val(s, st, x, k): return sum((1 if s.PR[r] == 0 else -1) << r for r in s.bset(st, x, k))
    def key(s, st, x, k):
        t = [s.O[x][k][2]]; y = s.O[x][k][0]
        while y != -1: t.append(s.O[y][st[y]][2]); y = s.O[y][st[y]][0]
        return tuple(reversed(t))
    def run(s, s0, cap=10 ** 5):
        S = [list(s0)]
        while len(S) <= cap:
            st = S[-1]; A = {}
            for x in range(s.N):
                cur = s.bset(st, x, st[x])
                A[x] = [st[x]] + [k for k in range(len(s.O[x])) if k != st[x] and s.better(s.bset(st, x, k), cur)]
            if all(len(a) == 1 for a in A.values()): break
            n = list(st)
            for x in s.order:
                n[x] = min(A[x], key=lambda k: s.key(st if NEG else n, x, k))
            if n == st: break
            S.append(n)
        return S

C = {k: 0 for k in 'RX1 RX2 RX3 MEQ F0 AGA AGB AGBm AGC WDA WDB WB2 SWA SWB1 SWB2 SWC SWD SWE1 SWE2 SWE3'.split()}
I = dict(files=0, runs=0, steps=0, segments=0, windows=0, maxD=0, flipsNoMove=0)
H = hashlib.sha1()

def check(g, s0):
    S = g.run(s0); T = len(S) - 1; N = g.N; d = N // 2; lev = g.lev
    H.update((''.join(map(str, s0)) + ':' + ' '.join(''.join(map(str, s)) for s in S) + ';').encode())
    I['runs'] += 1; I['steps'] += T
    Z = {o[1] for ox in g.O for o in ox if o[1] != X}
    Mv = [None] + [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
    mv = {x: sum(1 for t in range(1, T + 1) if x in Mv[t]) for x in range(N)}
    # REDUCE-XI
    if any(not (Mv[t - 1] & Z) for t in range(2, T + 1)): C['RX1'] += 1
    zst = sum(1 for t in range(1, T) if Mv[t] & Z)
    if T > 1 + zst: C['RX2'] += 1
    if T > 1 + sum(mv[z] for z in Z): C['RX3'] += 1
    # MOVES-EQUIV, per run: T <= 3 + (2d-2) * max moves of a level >= 1 Xi-target; F0
    mu = max([mv[z] for z in Z if lev[z] >= 1], default=0)
    if T > 3 + (2 * d - 2) * mu: C['MEQ'] += 1
    # current keys and flips
    ck = [[g.key(s, x, s[x]) for x in range(N)] for s in S]
    order = [[ck[t][2 * j] < ck[t][2 * j + 1] for j in range(d)] for t in range(T + 1)]
    flip = [None] + [[order[t][j] != order[t - 1][j] for j in range(d)] for t in range(1, T + 1)]
    if mv[0] > 1 or mv[1] > 1 or sum(flip[t][0] for t in range(1, T + 1)) > 2: C['F0'] += 1
    # pi (by sets), v (integers), KP
    pi = [[None] * N for _ in S]; V = [[None] * N for _ in S]; KP = [[None] * N for _ in S]
    for t, s in enumerate(S):
        for x in range(N):
            P0, P1 = g.bset(s, x, 0), g.bset(s, x, 1)
            pi[t][x] = 0 if g.better(P0, P1) else 1
            V[t][x] = (g.val(s, x, 0), g.val(s, x, 1))
            KP[t][x] = 0 if g.key(s, x, 0) < g.key(s, x, 1) else 1
    for x in range(N):
        mt = [t for t in range(1, T + 1) if x in Mv[t]]
        for t in range(1, T + 1):
            if (x in Mv[t]) != (S[t - 1][x] != pi[t - 1][x] and pi[t - 1][x] == KP[t][x]): C['AGA'] += 1
            if x in Mv[t] and not (S[t][x] == pi[t - 1][x] == KP[t][x]): C['AGA'] += 1
            if pi[t][x] != pi[t - 1][x]:
                b = pi[t][x]
                if not V[t][x][b] > V[t - 1][x][b]: C['AGC'] += 1
        for t, t2 in zip(mt, mt[1:]):
            if not any(pi[r][x] != pi[r - 1][x] for r in range(t, t2)): C['AGB'] += 1
            if not any(KP[r][x] != KP[r - 1][x] for r in range(t + 1, t2 + 1)): C['AGB'] += 1
        KF = sum(KP[t][x] != KP[t - 1][x] for t in range(1, T + 1)); PF = sum(pi[t][x] != pi[t - 1][x] for t in range(1, T + 1))
        if mv[x] > 1 + min(KF, PF): C['AGBm'] += 1
    # WINDOW-DOUBLE
    for j in range(1, d):
        p, q = 2 * j, 2 * j + 1
        c = [0 if order[t][j - 1] else 1 for t in range(T + 1)]   # c_j(s_t): option k with mover 2(j-1)+k of smaller key
        Phi = [(S[t][p] != c[t]) + (S[t][q] != c[t]) for t in range(T + 1)]
        for t in range(1, T + 1):
            if flip[t][j] and not (Mv[t] & {p, q}):
                I['flipsNoMove'] += 1
                if not (flip[t][j - 1] and S[t - 1][p] != S[t - 1][q] and Phi[t - 1] == 1): C['WDA'] += 1
        for a in range(0, T):
            fj = fj1 = 0
            for b in range(a + 1, T + 1):
                fj += flip[b][j]; fj1 += flip[b][j - 1]; I['windows'] += 1
                if fj > 2 + 2 * fj1: C['WDB'] += 1
                if fj1 == 0 and fj > 2: C['WB2'] += 1
    # SEG-WINDOW on every metronome segment
    for x in range(N):
        l = lev[x]
        if l == 0: continue
        u, w = 2 * l - 2, 2 * l - 1
        for a in range(1, T + 1):
            if x not in Mv[a]: continue
            for b in range(a, T + 1):
                if x not in Mv[b]: break
                I['segments'] += 1; D = b - a + 1; I['maxD'] = max(I['maxD'], D); inner = list(range(a + 1, b + 1))
                if any(not flip[t][l - 1] for t in inner): C['SWA'] += 1
                LS = sum(1 for t in inner if Mv[t] & {u, w}); PT = sum(1 for t in inner if flip[t][l - 1] and not (Mv[t] & {u, w}))
                if D > 1 + LS + PT: C['SWB1'] += 1
                if any(not any(lev[y] < l for y in Mv[t]) for t in inner): C['SWB2'] += 1
                if D > (3 + 2 * sum(flip[t][l - 2] for t in inner) if l >= 2 else 3): C['SWC'] += 1
                if l >= 2:   # (d): every sub-window W of [a+1, b] with F_W(l-2) = 0 has |W| <= 2
                    for i in range(len(inner)):
                        for k in range(i, len(inner)):
                            if any(flip[t][l - 2] for t in inner[i:k + 1]): break
                            if k - i + 1 > 2: C['SWD'] += 1
                for t in range(a, b):
                    bb = S[t + 1][x]
                    if pi[t][x] == pi[t - 1][x] or pi[t][x] != bb: C['SWE1'] += 1
                    if not V[t][x][bb] > V[t - 1][x][bb]: C['SWE2'] += 1
                    if not any(y != x and y in Mv[t] for y, _ in g.chain(S[t - 1], x, bb)): C['SWE3'] += 1

def dead(root):
    out = []
    for f, z, st in [('box186/out/pass_d3_D3.json', 5, '110100'), ('box186/out/pass_d4_D4.json', 7, '01010111'),
                     ('box186/out/pass_d5_D5.json', 9, '0101010110'), ('box187/inst/m4_z4_r7.json', 4, None)]:
        raw = open(os.path.join(root, f), 'rb').read(); g = G(json.loads(raw))
        s0 = [int(c) for c in st] if st else g.start
        S = g.run(s0); T = len(S) - 1; l = g.lev[z]
        mvz = [t for t in range(1, T + 1) if S[t][z] != S[t - 1][z]]
        LM = sum((S[t][2 * l - 2] != S[t - 1][2 * l - 2]) + (S[t][2 * l - 1] != S[t - 1][2 * l - 1]) for t in mvz)
        Z = {o[1] for ox in g.O for o in ox if o[1] != X}
        contig = mvz == list(range(mvz[0], mvz[-1] + 1)) if mvz else False
        out.append('DEAD %s sha1 %s LR %s d %d start %s z %d level %d Xi-target %s T %d moves %d at %s contiguous %s LM %d 2(l+1) %d'
                   % (f, hashlib.sha1(raw).hexdigest()[:8], g.ok_lr(), g.N // 2, ''.join(map(str, s0)), z, l, z in Z, T, len(mvz), mvz,
                      contig, LM, 2 * (l + 1)))
    return out

def rand_lr(d, rng):
    N = 2 * d; perm = list(range(N)); rng.shuffle(perm); pos = {v: i for i, v in enumerate(perm)}
    ranks = list(range(2 * N)); rng.shuffle(ranks); gates = list(range(2 * N)); rng.shuffle(gates)
    opts = []; gate = []; br = []; bp = []
    for x in range(N):
        ox = []
        for k in range(2):
            wt = 2 * (x // 2 - 1) + k if x // 2 else -1
            cand = [y for y in range(N) if pos[y] < pos[x]] + [-1] * rng.randint(1, 3)
            ox.append([wt, rng.choice(cand), len(br)]); br.append(ranks[len(br)]); bp.append(rng.randint(0, 1))
        opts.append(ox); gate.append([gates[2 * x], gates[2 * x + 1]])
    return dict(N=N, lev=[v // 2 for v in range(N)], opts=opts, gate=gate, br=br, bp=bp, start=[rng.randint(0, 1) for _ in range(N)])

def main():
    root = sys.argv[1]
    files = sorted(f for f in glob.glob(os.path.join(root, 'box1[5-8][0-9]/**/*.json'), recursive=True)
                   if 150 <= int(os.path.relpath(f, root)[3:6]) <= 187)
    for f in files:
        try: raw = json.load(open(f))
        except Exception: continue
        if not isinstance(raw, dict) or 'opts' not in raw: continue
        try: g = G(raw)
        except Exception: continue
        if not g.ok_lr(): continue
        I['files'] += 1
        starts = list(itertools.product((0, 1), repeat=g.N)) if g.N <= 10 else [tuple(g.start)]
        for st in starts: check(g, list(st))
    print('CORPUS ' + ' '.join('%s %d' % kv for kv in C.items()))
    print('INFO ' + ' '.join('%s %d' % kv for kv in I.items()) + ' runsha1 ' + H.hexdigest()[:12])
    if '--random' in sys.argv:
        K = int(sys.argv[sys.argv.index('--random') + 1]); rng = random.Random(29)
        for k in C: C[k] = 0
        for k in I: I[k] = 0
        for d in range(2, 7):
            for _ in range(K):
                g = G(rand_lr(d, rng)); assert g.ok_lr()
                I['files'] += 1
                starts = list(itertools.product((0, 1), repeat=g.N)) if g.N <= 10 else [[rng.randint(0, 1) for _ in range(g.N)] for _ in range(64)]
                for st in starts: check(g, list(st))
        print('RANDOM ' + ' '.join('%s %d' % kv for kv in C.items()))
        print('RINFO ' + ' '.join('%s %d' % kv for kv in I.items()))
    for line in dead(root): print(line)

if __name__ == '__main__':
    main()
