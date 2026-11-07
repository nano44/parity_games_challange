#!/usr/bin/env python3
"""REFEREE-2 successor 27: own checks of P-IDEAL-SEG on my own IDEAL simulator (R2-P-IDEAL-M2/m2_check.py, written from R104's text).
Lane code (box150 restrict(), segcheck.py) is not imported; H is built here.
Per run, for every l in [-1, top-1] and EVERY sub-interval [a', b'] of every maximal interval without a level-<=l move (SUB=0: maximal only):
 SEG   H (movers of level <= l keep only s_(a'-1)'s option) run from s_(a'-1) starts with s_(a'-1), ..., s_b' (any degree);
 ONCE  (deg <= 2) every level-(l+1) mover moves at most once in the interval; BADLEV=k tests level l+k instead (control);
 COUNT (deg <= 2) C_(l+1) + 1 <= (C_l + 1)(n_(l+1) + 1);  PROD (deg <= 2) T + 1 <= prod (n_l + 1); LADDER T <= 3^d - 1.
Usage: seg_check.py json FILE... (ALLN=n: every start for N <= n) | rand SEED COUNT NMAX DMAX [1] (LADDER=1) | mut SEED ITERS FILE...
       states FILE: print the run and the REPLAY test."""
import sys, os, json, random, itertools, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('m2', os.path.join(H, '..', 'R2-P-IDEAL-M2', 'm2_check.py'))
m2 = importlib.util.module_from_spec(sp); sp.loader.exec_module(m2)
SUB = os.environ.get('SUB', '1') == '1'; BADLEV = int(os.environ.get('BADLEV', '1'))
C = {}; RATIO = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def freeze(d, keep, st):
    e = json.loads(json.dumps(d))
    for x in keep:
        k = st[x]; e['opts'][x] = [d['opts'][x][k]]; e['gate'][x] = [d['gate'][x][k]]
    e['start'] = [0 if x in keep else st[x] for x in range(d['N'])]
    return e
def is_ladder(g):
    top = max(g.lev); return all(sum(1 for x in range(g.N) if g.lev[x] == l) == 2 for l in range(top + 1)) and all(v == 2 for v in g.deg), top + 1
def check(d, start, cap=None):
    g = m2.G(d); sts = g.run(start); T = len(sts) - 1; N = g.N; top = max(g.lev); D = max(g.deg)
    inc('runs'); inc('steps', T)
    Mv = [None] + [{x for x in range(N) if sts[t][x] != sts[t-1][x]} for t in range(1, T+1)]
    n = [sum(1 for x in range(N) if g.lev[x] == l and g.deg[x] == 2) for l in range(top + 1)]
    Cl = {-1: 0}
    for l in range(top + 1): Cl[l] = sum(1 for t in range(1, T+1) if any(g.lev[y] <= l for y in Mv[t]))
    if Cl[top] != T: inc('VIOL_T=Ctop')
    for l in range(-1, top):
        free = [t for t in range(1, T+1) if not any(g.lev[y] <= l for y in Mv[t])]
        ivs = []
        for t in free:
            if ivs and t == ivs[-1][1] + 1: ivs[-1][1] = t
            else: ivs.append([t, t])
        if len(ivs) > Cl[l] + 1: inc('VIOL_nintervals')
        for (A, B) in ivs:
            inc('intervals')
            subs = [(a, b) for a in range(A, B+1) for b in range(a, B+1)] if SUB else [(A, B)]
            for (a, b) in subs:
                inc('subintervals')
                keep = [x for x in range(N) if g.lev[x] <= l]
                e = freeze(d, keep, sts[a-1]); h = m2.G(e)
                SH = h.run(e['start'], cap=(b - a + 3))
                back = [[sts[a-1][x] if x in keep else s[x] for x in range(N)] for s in SH]
                if back[:b-a+2] != [list(s) for s in sts[a-1:b+1]]: inc('VIOL_SEG')
            if D <= 2:
                for x in range(N):
                    if g.lev[x] == l + BADLEV and sum(1 for t in range(A, B+1) if x in Mv[t]) > 1: inc('VIOL_ONCE')
        if D <= 2 and Cl[l+1] + 1 > (Cl[l] + 1) * (n[l+1] + 1): inc('VIOL_COUNT')
    if D <= 2:
        inc('d2runs'); pr = 1
        for v in n: pr *= v + 1
        if T + 1 > pr: inc('VIOL_PROD')
        r = (T + 1) / pr; nd2 = sum(n)
        RATIO[nd2] = max(RATIO.get(nd2, 0), r)
        lad, dd = is_ladder(g)
        if lad:
            inc('ladder_runs')
            if T > 3**dd - 1: inc('VIOL_LADDER')
    return T
def mutate(rng, d):
    e = json.loads(json.dumps(d)); r = rng.randrange(4); nb = len(e['br'])
    if r == 0:
        i, j = rng.randrange(nb), rng.randrange(nb); e['br'][i], e['br'][j] = e['br'][j], e['br'][i]
    elif r == 1: e['bp'][rng.randrange(nb)] ^= 1
    elif r == 2:
        fl = sum(e['gate'], []); i, j = rng.randrange(nb), rng.randrange(nb); fl[i], fl[j] = fl[j], fl[i]
        it = iter(fl); e['gate'] = [[next(it) for _ in o] for o in e['opts']]
    else:
        x = rng.randrange(e['N']); e['start'][x] = rng.randrange(len(e['opts'][x]))
    return e
if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'states':
        d = json.load(open(sys.argv[2])); g = m2.G(d); assert m2.acyclic(g); sts = g.run(d['start']); T = len(sts) - 1
        Mv = [None] + [sorted(x for x in range(g.N) if sts[t][x] != sts[t-1][x]) for t in range(1, T+1)]
        print('N', g.N, 'lev', g.lev, 'deg', g.deg, 'T', T)
        for t, s in enumerate(sts): print(' s_%d' % t, ' '.join(map(str, s)), 'Mv', Mv[t] if t else '-')
        hi = [x for x in range(g.N) if g.lev[x] >= 1]
        l0 = [t for t in range(1, T+1) if any(g.lev[y] == 0 for y in Mv[t])]
        print('level-0 move steps', l0)
        free = [t for t in range(1, T+1) if t not in l0]; ivs = []
        for t in free:
            if ivs and t == ivs[-1][1] + 1: ivs[-1][1] = t
            else: ivs.append([t, t])
        for (a, b) in ivs:
            if a < 2: print(' interval', [a, b], '(a = 1: outside REPLAY)'); continue
            prev = {tuple(sts[j][x] for x in hi) for j in range(a)}
            new = [t for t in range(a, b+1) if tuple(sts[t][x] for x in hi) not in prev]
            print(' interval', [a, b], 'new above level 0 at t =', new, 'REPLAY', 'FAILS' if new else 'holds')
        sys.exit(0)
    if mode == 'json':
        ALLN = int(os.environ.get('ALLN', '0'))
        for f in sys.argv[2:]:
            d = json.load(open(f)); g = m2.G(d); assert m2.acyclic(g)
            starts = [d['start']] + ([list(s) for s in itertools.product(*[range(x) for x in g.deg]) if list(s) != d['start']] if g.N <= ALLN else [])
            for st in starts: check(d, st)
    elif mode == 'rand':
        seed, cnt, Nmax, Dmax = map(int, sys.argv[2:6]); allst = len(sys.argv) > 6 and sys.argv[6] == '1'; rng = random.Random(seed)
        for _ in range(cnt):
            d = m2.rand_genome(rng, Nmax, Dmax); g = m2.G(d)
            for st in (itertools.product(*[range(x) for x in g.deg]) if allst else [d['start']]): check(d, list(st))
    elif mode == 'mut':   # climb T on each file (stresses LEVEL-PRODUCT / ladder bound)
        seed, iters = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); best = []
        for f in sys.argv[4:]:
            d = json.load(open(f)); T0 = check(d, d['start'])
            for _ in range(iters):
                e = mutate(rng, d); T = check(e, e['start'])
                if T >= T0: d, T0 = e, T
            best.append(T0)
        print('climbed T', best)
    print(' '.join(f'{k}={v}' for k, v in sorted(C.items())))
    print('max (T+1)/prod by #degree-2 movers', {k: round(v, 4) for k, v in sorted(RATIO.items())})
