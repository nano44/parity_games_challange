#!/usr/bin/env python3
"""REFEREE-2 successor 27: own IDEAL simulator written from RESULTS R104's text (sets of beta, no ENC),
plus checks of every P-IDEAL-M2 statement. Lane code is not imported.
Usage: m2_check.py json FILE...      (genome JSON, box 139-150 format; runs from its start)
       m2_check.py rand SEED COUNT NMAX DMAX [ALLSTARTS]
       NEG=1 env: keys under the OLD state (negative control)."""
import json, sys, random, itertools, os
NEG = os.environ.get('NEG') == '1'

class G:
    def __init__(s, d):
        s.N = d['N']; s.lev = d['lev']; s.opts = d['opts']; s.gate = d['gate']
        s.br = d['br']; s.bp = d['bp']; s.start = list(d['start'])
        s.deg = [len(o) for o in s.opts]
    def chain(s, st, x, k):
        """list of (mover, option) from (x,k) under st up to first option with Xi-target X"""
        out = [(x, k)]; y = s.opts[x][k][1]; seen = {x}
        while y != -1:
            assert y not in seen, 'Xi-cycle'
            seen.add(y); out.append((y, st[y])); y = s.opts[y][st[y]][1]
        return out
    def val(s, st, x, k):
        return frozenset(s.opts[y][o][2] for (y, o) in s.chain(st, x, k))
    def better(s, P, Q):  # P strictly better than Q
        if P == Q: return False
        b = max(P ^ Q, key=lambda i: s.br[i])
        return (b in P) == (s.bp[b] == 0)
    def key(s, st, x, k):
        w = s.opts[x][k][0]
        pre = () if s.lev[x] == 0 else s.key(st, w, st[w])
        return pre + (s.gate[x][k],)
    def avail(s, st, x):
        cur = st[x]; V = s.val(st, x, cur)
        return [cur] + [k for k in range(s.deg[x]) if k != cur and s.better(s.val(st, x, k), V)]
    def step(s, st):
        A = [s.avail(st, x) for x in range(s.N)]
        if all(len(a) == 1 for a in A): return None
        new = list(st)
        for L in sorted(set(s.lev)):
            for x in range(s.N):
                if s.lev[x] == L:
                    ref = st if NEG else new
                    new[x] = min(A[x], key=lambda k: s.key(ref, x, k))
        if new == list(st): return None
        return new
    def run(s, start, cap=100000):
        sts = [list(start)]
        while len(sts) <= cap:
            n = s.step(sts[-1])
            if n is None: break
            sts.append(n)
        return sts

def acyclic(g):
    col = [0]*g.N
    def dfs(x):
        col[x] = 1
        for o in g.opts[x]:
            y = o[1]
            if y != -1:
                if col[y] == 1: return False
                if col[y] == 0 and not dfs(y): return False
        col[x] = 2; return True
    return all(col[x] or dfs(x) for x in range(g.N))

def desc(g, x):
    seen = set(); stack = [o[1] for o in g.opts[x] if o[1] != -1]
    while stack:
        y = stack.pop()
        if y not in seen: seen.add(y); stack += [o[1] for o in g.opts[y] if o[1] != -1]
    return seen

C = dict()
def inc(k, v=1): C[k] = C.get(k, 0) + v

def check(g, start):
    sts = g.run(start); T = len(sts) - 1
    inc('runs'); inc('steps', T)
    Mv = [None] + [{x for x in range(g.N) if sts[t][x] != sts[t-1][x]} for t in range(1, T+1)]
    for t in range(1, T+1):
        if not Mv[t]: inc('VIOL_emptyMv')
    h = [None] + [min(Mv[t], key=lambda x: (g.lev[x], x)) for t in range(1, T+1)]
    U = 0
    for t in range(2, T+1):
        ch = g.chain(sts[t-2], h[t], sts[t][h[t]])
        chained = any(y == h[t-1] for (y, _) in ch[1:])
        if h[t-1] == h[t]: inc('h_equal')
        if not chained:
            U += 1
            if len(Mv[t-1]) < 2: inc('VIOL_MULTI')
    M2 = sum(1 for t in range(1, T) if len(Mv[t]) >= 2)
    inc('U', U); inc('M2', M2)
    if U > M2: inc('VIOL_U<=M2')
    if T > g.N*(1+M2): inc('VIOL_T<=N(1+M2)')
    if T > g.N*(1+U): inc('VIOL_CHAINBACK')
    if M2 > max(T-1, 0): inc('VIOL_M2EQ')
    if M2 == 0:
        inc('single_runs')
        if T > g.N: inc('VIOL_SINGLE')
    if max(g.deg) <= 2:
        inc('d2_runs')
        D = [desc(g, x) for x in range(g.N)]
        for t in range(2, T+1):
            for z in Mv[t]:
                o = sts[t-1][z]; op = 1 - o
                xi = lambda s: g.better(g.val(s, z, op), g.val(s, z, o))
                ky = lambda s: g.key(s, z, op) < g.key(s, z, o)
                XiT = xi(sts[t-2]) != xi(sts[t-1]); WT = ky(sts[t-1]) != ky(sts[t])
                inc('moves_t>=2'); inc('XiT', XiT); inc('WT', WT)
                if not (XiT or WT): inc('VIOL_TRIG_a')
                if XiT:
                    ys = {y for (y, _) in g.chain(sts[t-2], z, o)[1:] + g.chain(sts[t-2], z, op)[1:]} & Mv[t-1]
                    if not ys: inc('VIOL_TRIG_b')
                    if any(y not in D[z] for y in ys): inc('VIOL_TRIG_b_desc')
                if WT and not any(g.lev[y] < g.lev[z] for y in Mv[t]): inc('VIOL_TRIG_c')
                if WT and len(Mv[t]) < 2: inc('VIOL_TRIG_note')
        for x in range(g.N):
            mv = sum(1 for t in range(1, T+1) if x in Mv[t])
            if g.deg[x] == 1:
                if mv: inc('VIOL_deg1moves')
                continue
            sig = lambda s: g.better(g.val(s, x, 1), g.val(s, x, 0))
            kp = lambda s: min(range(2), key=lambda k: g.key(s, x, k))
            XF = sum(1 for j in range(1, T+1) if sig(sts[j]) != sig(sts[j-1]))
            KF = sum(1 for j in range(1, T+1) if kp(sts[j]) != kp(sts[j-1]))
            dmv = sum(1 for j in range(1, T+1) if Mv[j] & D[x])
            lmv = sum(1 for j in range(1, T+1) if any(g.lev[y] < g.lev[x] for y in Mv[j]))
            if mv > 1 + XF: inc('VIOL_XIFLIP')
            if mv > 1 + KF: inc('VIOL_KEYFLIP')
            if XF > dmv: inc('VIOL_XF<=desc')
            if KF > lmv: inc('VIOL_KF<=low')
    return T, M2, U, [len(Mv[t]) for t in range(1, T+1)]

LADDER = os.environ.get('LADDER') == '1'   # every mover of full degree Dmax, width 1-3 per level, Xi-target X w.p. 0.15
def rand_genome(rng, Nmax, Dmax):
    N = rng.randint(1, Nmax)
    nl = rng.randint(1, N) if not LADDER else max(1, N // rng.randint(1, 3))
    lev = sorted([rng.randrange(nl) for _ in range(N)])
    # make levels contiguous from 0
    m = {l: i for i, l in enumerate(sorted(set(lev)))}; lev = [m[l] for l in lev]
    perm = list(range(N)); rng.shuffle(perm)  # random topological order pi
    pos = {x: i for i, x in enumerate(perm)}
    opts = []; nb = 0
    for x in range(N):
        d = Dmax if LADDER else rng.randint(1, Dmax); ox = []
        for k in range(d):
            w = -1
            if lev[x] > 0: w = rng.choice([y for y in range(N) if lev[y] == lev[x]-1])
            later = [y for y in range(N) if pos[y] > pos[x]]
            xt = -1 if (not later or rng.random() < (0.15 if LADDER else 0.3)) else rng.choice(later)
            ox.append([w, xt, nb]); nb += 1
        opts.append(ox)
    br = list(range(nb)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(nb)]
    gs = list(range(nb)); rng.shuffle(gs); it = iter(gs)
    gate = [[next(it) for _ in o] for o in opts]
    start = [rng.randrange(len(o)) for o in opts]
    return dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start)

if __name__ == '__main__':
    if sys.argv[1] == 'json':
        ALLN = int(os.environ.get('ALLN', '0'))   # ALLN=n: every start of genomes with N <= n
        for f in sys.argv[2:]:
            d = json.load(open(f)); g = G(d); assert acyclic(g)
            T, M2, U, mv = check(g, g.start)
            if not ALLN: print(f, 'N', g.N, 'T', T, 'M2', M2, 'U', U, 'Mv', mv)
            elif g.N <= ALLN:
                for st in itertools.product(*[range(x) for x in g.deg]):
                    if list(st) != g.start: check(g, list(st))
    elif sys.argv[1] == 'mut':   # mut SEED ITERS FILE...: hill-climb T by mutating gates / ranks / parities / start
        seed, iters = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); best = 0
        for f in sys.argv[4:]:
            d = json.load(open(f)); g = G(d); T0 = len(g.run(g.start)) - 1
            for _ in range(iters):
                e = json.loads(json.dumps(d)); r = rng.randrange(4); nb = len(e['br'])
                if r == 0:
                    i, j = rng.randrange(nb), rng.randrange(nb); e['br'][i], e['br'][j] = e['br'][j], e['br'][i]
                elif r == 1: e['bp'][rng.randrange(nb)] ^= 1
                elif r == 2:
                    fl = sum(e['gate'], []); i, j = rng.randrange(nb), rng.randrange(nb); fl[i], fl[j] = fl[j], fl[i]
                    it = iter(fl); e['gate'] = [[next(it) for _ in o] for o in e['opts']]
                else:
                    x = rng.randrange(e['N']); e['start'][x] = rng.randrange(len(e['opts'][x]))
                ge = G(e); T, *_ = check(ge, ge.start)
                if T >= T0: d, T0 = e, T
            best = max(best, T0); print(f, 'climbed T', T0, 'N', d['N'])
        print('best', best)
    else:
        seed, cnt, Nmax, Dmax = map(int, sys.argv[2:6]); allst = len(sys.argv) > 6 and sys.argv[6] == '1'
        rng = random.Random(seed); best = (0, None)
        for _ in range(cnt):
            d = rand_genome(rng, Nmax, Dmax); g = G(d); assert acyclic(g)
            starts = itertools.product(*[range(x) for x in g.deg]) if allst else [g.start]
            for st in starts:
                T, *_ = check(g, list(st))
                if T > best[0]: best = (T, (g.N, list(st)))
        print('max T', best)
    print(' '.join(f'{k}={v}' for k, v in sorted(C.items())))
