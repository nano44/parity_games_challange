#!/usr/bin/env python3
"""REFEREE-2 succ. 28: R110's c-step written from R110's text (A-sets under the old state by beta-SET comparison, keys under the new
state, lowest level first; a level-1 option W-pointing to mover w keyed (kappa^c_w, its own gate), kappa^c_0 = 1 - c, kappa^c_1 = c;
movers 0 and 1 kept), using my r2sim.py. Exhaustive T_k for one ISO genome of L^R_(m+1), k in {0, 1}: max over all starts u_0 and bit
sequences with <= k changes of #{t : u_t != u_(t-1) on the levels >= 1}. Usage: r2cstep.py genome.json"""
import sys, os, itertools
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'R2-P-IDEAL-KEYS'))
from r2sim import load, wellformed, xiset, better, par, X
def ckey(O, lev, s, x, k, c):
    w = O[x][k][0]
    if lev[x] == 1: return ((1 - c) if w == 0 else c, O[x][k][2])
    return ckey(O, lev, s, w, s[w], c) + (O[x][k][2],)
def cstep(N, lev, O, u, c, PR):
    n = list(u)
    for l in range(1, max(lev) + 1):
        for x in [x for x in range(N) if lev[x] == l]:
            cur = xiset(O, u, x, u[x])[0]
            A = [u[x]] + [k for k in range(len(O[x])) if k != u[x] and better(xiset(O, u, x, k)[0], cur, PR)]
            n[x] = min(A, key=lambda k: ckey(O, lev, n, x, k, c))
    return tuple(n)
def Tk(N, lev, O, k, L=200):
    PR = par(O); best = (0, None, None); memo = {}
    def stepm(u, c):
        if (u, c) not in memo: memo[(u, c)] = cstep(N, lev, O, u, c, PR)
        return memo[(u, c)]
    def runc(u, c):  # constant-c sequence: the states while they change (constant c: once fixed, fixed for good)
        out = [u]
        for _ in range(L):
            v = stepm(out[-1], c)
            if v == out[-1]: break
            out.append(v)
        return out
    ups = [x for x in range(N) if lev[x] >= 1]
    for bits in itertools.product((0, 1), repeat=len(ups)):
        u0 = [0] * N
        for x, b in zip(ups, bits): u0[x] = b
        u0 = tuple(u0)
        for c0 in (0, 1):
            seg = runc(u0, c0)
            if len(seg) - 1 > best[0]: best = (len(seg) - 1, u0, (c0,) * (len(seg) - 1))
            if k >= 1:
                for j in range(len(seg)):
                    tail = runc(seg[j], 1 - c0); tot = j + len(tail) - 1
                    if tot > best[0]: best = (tot, u0, (c0,) * j + (1 - c0,) * (len(tail) - 1))
    return best
if __name__ == '__main__':
    N, lev, O, s0 = load(sys.argv[1]); wellformed(N, lev, O)
    iso = all(o[1] not in (0, 1) for ox in O for o in ox)
    LR = lev == [x // 2 for x in range(N)] and all(O[x][kk][0] == (2 * (lev[x] - 1) + kk if lev[x] else -1) for x in range(N) for kk in (0, 1))
    for k in (0, 1):
        T, u0, bits = Tk(N, lev, O, k)
        print('ISO', iso, 'L^R', LR, 'k', k, 'T_k of this genome', T, 'start (upper)', ''.join(str(u0[x]) for x in range(2, N)), 'bits', ''.join(map(str, bits)))

def checks(seed, ng):
    """Own checks on random ISO genomes of L^R_(m+1), m = 1..3, every upper state, both c: Lemma IM (a), (b), (c); BIT-CHAIN (i) on the
    c-step's new state; KEY-DIR; VALUE-MONO; frame step (C table from values, BIT-CHAIN recursion from the new states) = my c-step."""
    import random
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'R2-P-IDEAL-ALIGN'))
    from r2align import ladder
    from r2sim import val
    R = random.Random(seed); V = dict(IMa=0, IMb=0, IMc=0, BIT=0, KEYDIR=0, VMONO=0, FRAME=0); Cn = dict(V)
    for gi in range(ng):
        m = R.randint(1, 3); d = m + 1
        while True:
            N, lev, O = ladder(R, d)
            if all(o[1] not in (0, 1) for ox in O for o in ox): break
            # redraw targets 0/1 to X to keep ISO cheaply
            O = [[(o[0], X if o[1] in (0, 1) else o[1], o[2], o[3], o[4]) for o in ox] for ox in O]; break
        PR = par(O); ups = [x for x in range(N) if lev[x] >= 1]
        def C(z, s): return 0 if val(O, s, z, 0) > val(O, s, z, 1) else 1
        def chain(z, k, s):
            out = set(); y = O[z][k][1]
            while y != X: out.add(y); y = O[y][s[y]][1]
            return out
        for bits in itertools.product((0, 1), repeat=len(ups)):
            s = [0, 0] + list(bits); s = tuple(s)
            for z in ups:
                for y in ups:
                    if y == z or s[y] == C(y, s): continue
                    s2 = list(s); s2[y] ^= 1; s2 = tuple(s2); c0, c1 = chain(z, 0, s), chain(z, 1, s); a, b = C(z, s), C(z, s2)
                    if y not in c0 and y not in c1: Cn['IMa'] += 1; V['IMa'] += a != b
                    elif y in c0 and y in c1: Cn['IMb'] += 1; V['IMb'] += a != b
                    else:
                        k = 0 if y in c0 else 1; Cn['IMc'] += 1; V['IMc'] += b not in (a, k)
            for c in (0, 1):
                n = cstep(N, lev, O, s, c, PR)
                bl = [c]
                for l in range(1, m + 1):
                    A, B = 2 * l, 2 * l + 1
                    if (n[A], n[B]) == (0, 1): bl.append(bl[-1])
                    elif (n[A], n[B]) == (1, 0): bl.append(1 - bl[-1])
                    else: k = n[A]; bl.append(int(O[A][k][2] < O[B][k][2]))
                    Cn['BIT'] += 1; V['BIT'] += bl[l] != int(ckey(O, lev, n, A, n[A], c) < ckey(O, lev, n, B, n[B], c))
                for x in ups:
                    l = lev[x]; mv = n[x] != s[x]
                    Cn['KEYDIR'] += 1; V['KEYDIR'] += mv != (s[x] == bl[l - 1] and C(x, s) != bl[l - 1])
                    Cn['VMONO'] += 1; V['VMONO'] += not (val(O, n, x, n[x]) >= val(O, s, x, s[x]) and (not mv or val(O, n, x, n[x]) > val(O, s, x, s[x])))
                f = list(s); b = c
                for l in range(1, m + 1):
                    for x in (2 * l, 2 * l + 1):
                        if C(x, s) != s[x] and C(x, s) == 1 - b: f[x] = 1 - s[x]
                    A, B = 2 * l, 2 * l + 1
                    if f[A] != f[B]: b = (1 - b) if f[A] == 1 else b
                    else: b = int(O[A][f[A]][2] < O[B][f[A]][2])
                Cn['FRAME'] += 1; V['FRAME'] += tuple(f) != n
    print('SEED', seed, 'ISO genomes', ng); print('CHECKS', ' '.join(f'{k} {Cn[k]}' for k in Cn)); print('VIOL', ' '.join(f'{k} {V[k]}' for k in V))
