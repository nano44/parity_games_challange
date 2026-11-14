#!/usr/bin/env python3
"""REFEREE-2 successor 27: own checks of P-IDEAL-FLIP on my own IDEAL simulator (R2-P-IDEAL-M2/m2_check.py, from R104's text).
The c-step, forced runs, H_q, G^swap and the exact FLIP-1 maximum are written here from the packet's §1 text; lane code not imported.
Usage: flip_check.py rand SEED COUNT DMAX   random W_d genomes (any degrees, widths 1-3; half ISO) and random L^R_d genomes (3/4 ISO)
       flip_check.py inst FILE              replay a genome (L^R / ISO / T / level-0 steps / seg1 / tail)
       flip_check.py forced FILE C1,C2,...  forced run of FILE from its start under the given bits (moves, flips, states on U)
       flip_check.py flip1 SEED COUNT       exact max moves over forced runs (k = 0..6) on random ISO L^R_2 genomes, all starts
       flip_check.py climb SEED ITERS FILE...  hill-climb T on L^R_d genomes (mutating ranks, parities, gates, Xi-targets, start)
       FNEG=1: c-step ignoring c (control)."""
import sys, os, json, random, itertools, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('m2', os.path.join(H, '..', 'R2-P-IDEAL-M2', 'm2_check.py'))
m2 = importlib.util.module_from_spec(sp); sp.loader.exec_module(m2)
NEG = os.environ.get('FNEG') == '1'   # FNEG (not NEG: m2_check reads NEG for its own control)
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
cp = lambda d: json.loads(json.dumps(d))
def b0(d, s): return 1 if d['gate'][0][s[0]] < d['gate'][1][s[1]] else 0
def kappa(c, w): return (1 - c) if w == 0 else c
def keyc(d, s2, x, k, c):
    w = d['opts'][x][k][0]
    if d['lev'][x] == 1: return ((0 if NEG else kappa(c, w)), d['gate'][x][k])
    return keyc(d, s2, w, s2[w], c) + (d['gate'][x][k],)
def cstep(d, g, s, c):
    U = [x for x in range(d['N']) if d['lev'][x] >= 1]
    A = {x: g.avail(s, x) for x in U}; s2 = list(s)
    for l in range(1, max(d['lev']) + 1):
        for x in U:
            if d['lev'][x] == l: s2[x] = min(A[x], key=lambda k: keyc(d, s2, x, k, c))
    return s2
def onU(d, s): return tuple(s[x] for x in range(d['N']) if d['lev'][x] >= 1)
def iso(d): return all(o[1] not in (0, 1) for oo in d['opts'] for o in oo)
def in_LR(d):
    N = d['N']; dd = N // 2
    return (N % 2 == 0 and d['lev'] == [x // 2 for x in range(N)] and all(len(o) == 2 for o in d['opts']) and
            all(d['opts'][x][k][0] == (2 * (d['lev'][x] - 1) + k if d['lev'][x] >= 1 else -1) for x in range(N) for k in range(2)))
def freeze01(d, q):
    e = cp(d)
    for y in (0, 1):
        e['opts'][y] = [d['opts'][y][q[y]]]; e['gate'][y] = [d['gate'][y][q[y]]]
    return e
def swap(d):
    e = cp(d)
    for x in range(d['N']):
        if d['lev'][x] == 1:
            e['opts'][x] = [[d['opts'][x][1 - k][0], d['opts'][x][k][1], d['opts'][x][k][2]] for k in range(2)]
    return e
def rand_W(rng, dd, isoflag, LR=False):
    if LR:
        lev = [x // 2 for x in range(2 * dd)]; deg = [2] * (2 * dd)
    else:
        lev = [0, 0]; deg = [rng.randint(1, 3), rng.randint(1, 3)]
        for l in range(1, dd):
            for _ in range(rng.randint(1, 3)): lev.append(l); deg.append(rng.randint(1, 3))
    N = len(lev); perm = list(range(N)); rng.shuffle(perm); pos = {x: i for i, x in enumerate(perm)}
    opts = []; nb = 0
    for x in range(N):
        ox = []
        for k in range(deg[x]):
            if lev[x] == 0: w = -1
            elif LR: w = 2 * (lev[x] - 1) + k
            else: w = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
            later = [y for y in range(N) if pos[y] > pos[x] and not (isoflag and y in (0, 1))]
            xt = -1 if (not later or rng.random() < 0.2) else rng.choice(later)
            ox.append([w, xt, nb]); nb += 1
        opts.append(ox)
    br = list(range(nb)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(nb)]
    gs = list(range(nb)); rng.shuffle(gs); it = iter(gs)
    return dict(N=N, lev=lev, opts=opts, gate=[[next(it) for _ in o] for o in opts], br=br, bp=bp,
                start=[rng.randrange(len(o)) for o in opts])
def check_genome(d, rng, nstarts=6):
    g = m2.G(d); assert m2.acyclic(g); ISO = iso(d); LR = in_LR(d)
    starts = [d['start']] + [[rng.randrange(len(o)) for o in d['opts']] for _ in range(nstarts)]
    for st in starts:
        sts = g.run(st); T = len(sts) - 1; inc('runs'); inc('steps', T)
        for t in range(1, T + 1):   # W-ONLY (a), any W_d genome
            inc('WONLY_steps')
            if onU(d, cstep(d, g, sts[t-1], b0(d, sts[t]))) != onU(d, sts[t]): inc('VIOL_WONLY_a')
        if ISO:
            # (d) as forced run: u_t|U = s_t|U, flips <= 2 (L^R only: degree 2)
            u = list(st); cs = [b0(d, sts[t]) for t in range(1, T + 1)]
            for t in range(1, T + 1):
                u = cstep(d, g, u, cs[t-1])
                if onU(d, u) != onU(d, sts[t]): inc('VIOL_WONLY_d_forced')
            if LR:
                inc('LR_iso_runs'); fl = sum(1 for t in range(1, T) if cs[t] != cs[t-1])
                l0 = sum(1 for t in range(1, T + 1) if sts[t][0] != sts[t-1][0] or sts[t][1] != sts[t-1][1])
                if fl > 2 or l0 > 2: inc('VIOL_WONLY_d_flips')
        # NOW-ONCE (a), L^R real runs: intervals with b0 constant
        if LR:
            for x in range(d['N']):
                if d['lev'][x] != 1: continue
                mv = [t for t in range(1, T + 1) if sts[t][x] != sts[t-1][x]]
                for a, b in zip(mv, mv[1:]):
                    inc('NOW_pairs')
                    if b0(d, sts[a]) == b0(d, sts[b]): inc('VIOL_NOWONCE_a')
    if ISO:
        for _ in range(8):   # (b) A-sets on U independent of options of 0, 1
            s = [rng.randrange(len(o)) for o in d['opts']]; s2 = list(s); s2[0] = rng.randrange(len(d['opts'][0])); s2[1] = rng.randrange(len(d['opts'][1]))
            inc('ISOB_pairs')
            if any(g.avail(s, x) != g.avail(s2, x) for x in range(2, d['N'])): inc('VIOL_WONLY_b')
        for q in itertools.product(range(len(d['opts'][0])), range(len(d['opts'][1]))):   # (c) frozen form
            h = freeze01(d, q); gh = m2.G(h); c = b0(d, q)
            for _ in range(2):
                s = [rng.randrange(len(o)) for o in d['opts']]; s[0], s[1] = q
                hs = [0, 0] + s[2:]; runh = gh.run(hs); inc('FROZ_runs')
                cur = list(s); it = [onU(d, cur)]
                for _ in range(10 * d['N'] + 50):
                    nx = cstep(d, g, cur, c)
                    if onU(d, nx) == onU(d, cur): break
                    cur = nx; it.append(onU(d, cur))
                if [onU(h, r) for r in runh] != it: inc('VIOL_WONLY_c')
    if LR and ISO:   # SWAP
        gs = m2.G(swap(d))
        for _ in range(8):
            s = [rng.randrange(2) for _ in range(d['N'])]
            for c in (0, 1):
                inc('SWAP_pairs')
                if onU(d, cstep(d, g, s, 1 - c)) != onU(d, cstep(swap(d), gs, s, c)): inc('VIOL_SWAP')
                if onU(d, cstep(d, g, s, c)) != onU(d, cstep(swap(d), gs, s, c)): inc('CTRL_swap_samec_differs')
        # NOW-ONCE (b): forced runs with random bits, constant-c stretches
        for _ in range(6):
            u = [rng.randrange(2) for _ in range(d['N'])]; L = rng.randint(1, 12); cs = [rng.randrange(2) for _ in range(L)]
            prev = list(u); hist = [list(u)]
            for t in range(L): hist.append(cstep(d, g, hist[-1], cs[t]))
            for x in range(d['N']):
                if d['lev'][x] != 1: continue
                ch = [t for t in range(1, L + 1) if hist[t][x] != hist[t-1][x]]
                for a, b in zip(ch, ch[1:]):
                    inc('NOWB_pairs')
                    if all(cs[t-1] == cs[a-1] for t in range(a, b + 1)): inc('VIOL_NOWONCE_b')
def maxmoves(d, u0, k, Lmax=14):
    g = m2.G(d); best = 0; memo = {}
    def rec(u, lastc, flips, depth):
        key = (onU(d, u), lastc, flips, depth)
        if key in memo: return memo[key]
        r = 0
        if depth < Lmax:
            for c in (0, 1):
                f = flips + (1 if (lastc is not None and c != lastc) else 0)
                if f > k: continue
                nx = cstep(d, g, u, c); mv = 1 if onU(d, nx) != onU(d, u) else 0
                if mv or c != lastc: r = max(r, mv + rec(nx, c, f, depth + 1))
        memo[key] = r; return r
    return rec(list(u0), None, 0, 0)
if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'rand':
        seed, cnt, Dmax = map(int, sys.argv[2:5]); rng = random.Random(seed)
        for i in range(cnt):
            dd = rng.randint(2, Dmax)
            check_genome(rand_W(rng, dd, rng.random() < 0.5, LR=False), rng)
            check_genome(rand_W(rng, dd, rng.random() < 0.75, LR=True), rng)
    elif mode == 'json':   # json FILE...: every start (N <= 8; else 40 random starts) through check_genome; also max T over starts
        rng = random.Random(0); mx = {}
        for f in sys.argv[2:]:
            d = json.load(open(f)); g = m2.G(d); N = d['N']
            sts = [list(s) for s in itertools.product(*[range(len(o)) for o in d['opts']])] if N <= 8 else [[rng.randrange(len(o)) for o in d['opts']] for _ in range(40)]
            for st in sts:
                e = dict(d); e['start'] = st; check_genome(e, rng, nstarts=0)
                if in_LR(d): mx[N // 2] = max(mx.get(N // 2, 0), len(g.run(st)) - 1)
        print('max T over starts by d (L^R files)', mx)
    elif mode == 'inst':
        d = json.load(open(sys.argv[2])); g = m2.G(d); sts = g.run(d['start']); T = len(sts) - 1
        l0 = [t for t in range(1, T + 1) if sts[t][0] != sts[t-1][0] or sts[t][1] != sts[t-1][1]]
        print('L^R', in_LR(d), 'ISO', iso(d), 'acyclic', m2.acyclic(g), 'd', d['N'] // 2, 'T', T, 'level-0 steps', l0,
              'seg1', (l0[0] - 1) if l0 else T, 'tail', (T - l0[-1]) if l0 else 0)
        print('states', [''.join(map(str, s)) for s in sts])
    elif mode == 'forced':
        d = json.load(open(sys.argv[2])); g = m2.G(d); cs = [int(c) for c in sys.argv[3].split(',')]
        u = list(d['start']); hist = [u]
        for c in cs: hist.append(cstep(d, g, hist[-1], c))
        mv = sum(1 for t in range(1, len(hist)) if onU(d, hist[t]) != onU(d, hist[t-1]))
        print('L^R', in_LR(d), 'ISO', iso(d), 'moves', mv, 'flips', sum(1 for a, b in zip(cs, cs[1:]) if a != b), 'U-states', [onU(d, h) for h in hist])
        for k in range(4): print(' exact max moves from this start, k =', k, ':', maxmoves(d, d['start'], k))
    elif mode == 'flip1':
        seed, cnt = map(int, sys.argv[2:4]); rng = random.Random(seed); mx = {}
        for _ in range(cnt):
            d = rand_W(rng, 2, True, LR=True)
            for st in itertools.product(range(2), repeat=4):
                inc('flip1_pairs')
                for k in range(7):
                    v = maxmoves(d, list(st), k); mx[k] = max(mx.get(k, 0), v)
                    if v > (2 if k == 0 else 3): inc('VIOL_FLIP1')
        print('max moves by k', mx)
    elif mode == 'climb':
        sp2 = importlib.util.spec_from_file_location('sg', os.path.join(H, '..', 'R2-P-IDEAL-SEG', 'seg_check.py'))
        sg = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(sg)
        seed, iters = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); best = 0
        for f in sys.argv[4:]:
            d = json.load(open(f)) if f != 'RAND' else rand_W(rng, 3, rng.random() < 0.5, LR=True)
            T0 = len(m2.G(d).run(d['start'])) - 1
            for _ in range(iters):
                if rng.random() < 0.2:   # re-draw one Xi-target (kept acyclic, R197 W-targets fixed)
                    e = cp(d); x = rng.randrange(e['N']); k = rng.randrange(2); e['opts'][x][k][1] = rng.choice([-1] + [y for y in range(e['N']) if y != x])
                    if not m2.acyclic(m2.G(e)): continue
                else: e = sg.mutate(rng, d)
                T = len(m2.G(e).run(e['start'])) - 1; inc('climb_runs')
                if T >= T0: d, T0 = e, T
            best = max(best, T0)
            if T0 >= 9: inc('T>=9_FOUND'); json.dump(d, open(os.environ.get('OUT', '/dev/null'), 'w'))
        print('best T', best)
    print(' '.join(f'{k}={v}' for k, v in sorted(C.items())))
