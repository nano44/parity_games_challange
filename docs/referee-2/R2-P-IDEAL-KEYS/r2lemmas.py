#!/usr/bin/env python3
"""REFEREE-2 succ. 28: independent checks of P-IDEAL-KEYS LOCAL-KP, PAIR-KF, PAIR-MOVES, CASCADE, F<=T, LADDER, RENEW, MERGE, RETURN,
RETURN-COUNT on random IDEAL-ACYC genomes and random 2-wide ladders (L^R_d), with r2sim.py (own simulator from R104's text).
Usage: r2lemmas.py SEED NGEN"""
import random, sys, itertools, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2sim import run, key, xiset, better, par, val, X
def rand_genome(R, ladder=False):
    if ladder:
        d = R.randint(2, 6); lev = [l for l in range(d) for _ in (0, 1)]; N = 2 * d
    else:
        L = R.randint(1, 5); lev = []
        for l in range(L): lev += [l] * R.randint(1, 3)
        N = len(lev)
    pi = list(range(N)); R.shuffle(pi)  # Xi-target must have larger pi: acyclic
    nopt = 0; O = []
    gates = list(range(4 * N)); R.shuffle(gates); ranks = list(range(4 * N)); R.shuffle(ranks)
    deg2only = ladder or R.random() < 0.5
    for x in range(N):
        dg = 2 if ladder else (R.choice([1, 2, 2]) if deg2only else R.choice([1, 2, 3, 3]))
        ox = []
        for k in range(dg):
            if lev[x] == 0: w = -1
            elif ladder: w = 2 * (lev[x] - 1) + k
            else: w = R.choice([y for y in range(N) if lev[y] == lev[x] - 1])
            cand = [y for y in range(N) if pi[y] > pi[x]]
            xt = R.choice(cand + [X]) if cand and R.random() < 0.8 else X
            ox.append((w, xt, gates[nopt], ranks[nopt], R.randint(0, 1))); nopt += 1
        O.append(ox)
    return N, lev, O
def W(O, x):
    S = set(); st = [x]
    while st:
        u = st.pop()
        for o in O[u]:
            if o[0] != -1 and o[0] not in S: S.add(o[0]); st.append(o[0])
    return S
def D(O, x):
    S = set(); st = [x]
    while st:
        u = st.pop()
        for o in O[u]:
            if o[1] != X and o[1] not in S: S.add(o[1]); st.append(o[1])
    return S
def KP(O, s, x): return min(range(len(O[x])), key=lambda k: key(O, s, x, k))
def ordk(O, s, p, q): return key(O, s, p, s[p]) < key(O, s, q, s[q])
def chain(O, s, x, k):
    out = []; y = O[x][k][1]
    while y != X: out.append(y); y = O[y][s[y]][1]
    return out
def A(O, s, x, PR):
    cur = xiset(O, s, x, s[x])[0]
    return {s[x]} | {k for k in range(len(O[x])) if better(xiset(O, s, x, k)[0], cur, PR)}
V = {k: 0 for k in 'LOCALKPa LOCALCTL KFWE PAIRKF PAIRMOVES CASCADE FLET LADDER1 LADDER2 LADDER3 RENEW RENEWext RENEWB MERGE MERGECTL RETURN RETCNT'.split()}
C = {k: 0 for k in V}
C['BELOW'] = 0; C['RENEWCTL'] = 0; NG = [0, 0]
CORPUS = os.environ.get('CORPUS')
def main(seed, ngen):
    R = random.Random(seed); runs = 0; steps = 0
    def gen():
        if CORPUS:
            import glob, json
            from r2sim import load, wellformed
            for f in sorted(glob.glob(CORPUS + '/box1[5-7][0-9]/**/*.json', recursive=True)):
                b = int(f.split('/box')[1][:3])
                if not 150 <= b <= 172: continue
                try:
                    N, lev, O, s0 = load(f); wellformed(N, lev, O)
                except Exception: continue
                if N > 30 or len(s0) != N: continue
                lad = N % 2 == 0 and lev == [l for l in range(N // 2) for _ in (0, 1)] and all(len(O[x]) == 2 for x in range(N)) and \
                      all(O[x][k][0] == (2 * (lev[x] - 1) + k if lev[x] else -1) for x in range(N) for k in (0, 1))
                yield N, lev, O, [tuple(s0)], lad
            return
        for gi in range(ngen):
            lad = gi % 4 == 0
            N, lev, O = rand_genome(R, lad); degs = [len(O[x]) for x in range(N)]
            sp = [range(d) for d in degs]; tot = 1
            for d in degs: tot *= d
            starts = list(itertools.product(*sp)) if tot <= 32 else [tuple(R.randrange(d) for d in degs) for _ in range(32)]
            yield N, lev, O, starts, lad
    for N, lev, O, starts, lad in gen():
        PR = par(O); tau = max(lev); degs = [len(O[x]) for x in range(N)]; NG[0] += 1; NG[1] += lad
        Ws = [W(O, x) for x in range(N)]; Ds = [D(O, x) for x in range(N)]
        # LOCAL-KP (a) and MERGE (b) on random state pairs
        for _ in range(20):
            s = [R.randrange(d) for d in degs]; x = R.randrange(N)
            s2 = [s[y] if (y in Ws[x] or R.random() < 0.5) else R.randrange(degs[y]) for y in range(N)]
            C['LOCALKPa'] += 1
            if any(key(O, s, x, k) != key(O, s2, x, k) for k in range(degs[x])): V['LOCALKPa'] += 1
            ys = [y for y in Ws[x] if degs[y] > 1]
            if ys:
                s3 = list(s); y = R.choice(ys); s3[y] = (s3[y] + 1) % degs[y]
                if any(key(O, s, x, k) != key(O, s3, x, k) for k in range(degs[x])): C['LOCALCTL'] += 1
            if degs[x] >= 2:
                a, b = R.sample(range(degs[x]), 2)
                ca, cb = chain(O, s, x, a), chain(O, s, x, b)
                i = next((ii for ii, y in enumerate(ca) if y in cb), len(ca)); j = cb.index(ca[i]) if i < len(ca) else len(cb)
                pre = set(ca[:i]) | set(cb[:j])
                s4 = [s[y] if y in pre else R.randrange(degs[y]) for y in range(N)]
                C['MERGE'] += 1
                if val(O, s, x, a) - val(O, s, x, b) != val(O, s4, x, a) - val(O, s4, x, b): V['MERGE'] += 1
                if pre:
                    s5 = list(s); y = R.choice(sorted(pre))
                    if degs[y] > 1:
                        s5[y] = (s5[y] + 1) % degs[y]
                        if val(O, s, x, a) - val(O, s, x, b) != val(O, s5, x, a) - val(O, s5, x, b): C['MERGECTL'] += 1
        for s0 in starts:
            S = run(N, lev, O, list(s0)); T = len(S) - 1; runs += 1; steps += T
            Mv = [None] + [{x for x in range(N) if S[t][x] != S[t - 1][x]} for t in range(1, T + 1)]
            moves = [sum(1 for t in range(1, T + 1) if x in Mv[t]) for x in range(N)]
            kp = [[KP(O, s, x) for x in range(N)] for s in S]
            for x in range(N):
                KF = sum(kp[t][x] != kp[t - 1][x] for t in range(1, T + 1))
                WE = sum(1 for t in range(1, T + 1) if Mv[t] & Ws[x])
                C['KFWE'] += 1; V['KFWE'] += KF > WE
                if degs[x] == 2 and lev[x] >= 1:
                    a, b = O[x][0][0], O[x][1][0]; C['PAIRKF'] += 1
                    if a == b: V['PAIRKF'] += KF != 0
                    else:
                        fl = sum(ordk(O, S[t], a, b) != ordk(O, S[t - 1], a, b) for t in range(1, T + 1))
                        V['PAIRKF'] += KF != fl
                        if all(d <= 2 for d in degs): C['PAIRMOVES'] += 1; V['PAIRMOVES'] += moves[x] > 1 + fl
                elif all(d <= 2 for d in degs): C['PAIRMOVES'] += 1; V['PAIRMOVES'] += moves[x] > 1
            # CASCADE + F<=T
            F = {}
            for p in range(N):
                for q in range(p + 1, N):
                    if lev[p] != lev[q]: continue
                    o = [ordk(O, s, p, q) for s in S]; f = 0
                    for t in range(1, T + 1):
                        if o[t] == o[t - 1]: continue
                        f += 1; C['CASCADE'] += 1
                        if p in Mv[t] or q in Mv[t]: continue
                        if lev[p] == 0: V['CASCADE'] += 1; continue
                        wp, wq = O[p][S[t][p]][0], O[q][S[t][q]][0]
                        if wp == wq or ordk(O, S[t], wp, wq) == ordk(O, S[t - 1], wp, wq): V['CASCADE'] += 1
                        else: C['BELOW'] += 1
                    F[(p, q)] = f; C['FLET'] += 1; V['FLET'] += f > T
            if lad:
                d = N // 2; Fl = [F[(2 * l, 2 * l + 1)] for l in range(d)]
                C['LADDER1'] += 1
                if Fl[0] > moves[0] + moves[1] or Fl[0] > 2: V['LADDER1'] += 1
                for l in range(1, d):
                    if Fl[l] > moves[2 * l] + moves[2 * l + 1] + Fl[l - 1]: V['LADDER1'] += 1
                    for x in (2 * l, 2 * l + 1):
                        C['LADDER2'] += 1; V['LADDER2'] += moves[x] > 1 + Fl[l - 1]
                for l in range(d): C['LADDER3'] += 1; V['LADDER3'] += Fl[l] > 3 ** (l + 1) - 1
            # RENEW
            top = [None] + [all(lev[x] == tau for x in Mv[t]) for t in range(1, T + 1)]
            t = 1
            while t <= T:
                if not top[t]: t += 1; continue
                a = t
                while t + 1 <= T and top[t + 1]: t += 1
                b = t; C['RENEWB'] += 1
                for h in range(N):
                    if lev[h] != tau: continue
                    for u in range(max(a - 1, 0), b + 1):
                        if any(key(O, S[u], h, k) != key(O, S[max(a - 1, 0)], h, k) for k in range(degs[h])): V['RENEWB'] += 1; break
                for tt in range(max(a, 2), b + 1):
                    if tt == a and top[a - 1]: V['RENEW'] += 1
                    for h in Mv[tt]:
                        w = S[tt][h]; key_ = 'RENEW' if tt == a else 'RENEWext'; C[key_] += 1
                        bad = w in A(O, S[tt - 2], h, PR)
                        C['RENEWCTL'] += w in A(O, S[tt - 1], h, PR)  # control: w IS in A under s_(t-1) (F2)
                        bad |= not (val(O, S[tt - 1], h, w) > val(O, S[tt - 2], h, w))
                        Z = [z for z in chain(O, S[tt - 2], h, w) if z != h and z in Mv[tt - 1]]
                        bad |= not Z or any(z not in Ds[h] for z in Z)
                        V[key_] += bad
                t = b + 1
            # RETURN, RETURN-COUNT (degree-2 movers)
            for x in range(N):
                if degs[x] != 2: continue
                ts = [t for t in range(1, T + 1) if x in Mv[t]]
                for t1, t2 in zip(ts, ts[1:]):
                    C['RETURN'] += 1; o = S[t1][x]; z = O[x][1 - o][1]
                    if z == X or not (val(O, S[t2 - 1], z, S[t2 - 1][z]) > val(O, S[t1 - 1], z, S[t1 - 1][z])): V['RETURN'] += 1
                Rk = 0
                for k in (0, 1):
                    z = O[x][k][1]
                    if z != X: Rk += sum(val(O, S[u], z, S[u][z]) > val(O, S[u - 1], z, S[u - 1][z]) for u in range(1, T + 1))
                C['RETCNT'] += 1; V['RETCNT'] += moves[x] > 1 + Rk
    print('SEED', seed, 'CORPUS' if CORPUS else 'random', 'genomes', NG[0], 'ladders', NG[1], 'runs', runs, 'steps', steps)
    print('CHECKS', ' '.join(f'{k} {C[k]}' for k in C))
    print('VIOL', ' '.join(f'{k} {V[k]}' for k in V))
if __name__ == '__main__': main(int(sys.argv[1]), int(sys.argv[2]))
