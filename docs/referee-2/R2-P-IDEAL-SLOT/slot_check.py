#!/usr/bin/env python3
"""REFEREE-2 successor 27: own checks of P-IDEAL-SLOT on my own IDEAL simulator (R2-P-IDEAL-M2/m2_check.py, from R104's text).
SHIFT, LIFT and the SEG-CAP proof chain (freeze level 0 -> H, shift -> H-down in L_(d-1), same run) are built here; lane code not imported.
Usage: slot_check.py inst LIFTED ORIG      instance checks for the DEAD (and own lift of ORIG compared with LIFTED's run)
       slot_check.py rand SEED COUNT NMAX DMAX      SHIFT (level 0 forced to degree 1) and LIFT on random genomes (+ controls)
       slot_check.py lad SEED COUNT DMAX EXTRA [1]  random L_d genomes (two degree-2 movers per level + up to EXTRA degree-1 movers):
                                                    SEG-CAP chain per segment, T decomposition, level-0 steps <= 2; '1' = every start"""
import sys, os, json, random, itertools, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('m2', os.path.join(H, '..', 'R2-P-IDEAL-M2', 'm2_check.py'))
m2 = importlib.util.module_from_spec(sp); sp.loader.exec_module(m2)
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
cp = lambda d: json.loads(json.dumps(d))
def run(d, start=None):
    g = m2.G(d); assert m2.acyclic(g); return g.run(list(d['start'] if start is None else start))
def shift(d, scale=True):
    """G-down: requires every level-0 mover to have degree 1."""
    e = cp(d); N = d['N']; Gam = max(sum(d['gate'], [])) + 1
    assert all(len(d['opts'][x]) == 1 for x in range(N) if d['lev'][x] == 0)
    for x in range(N):
        if d['lev'][x] == 1:
            for k, o in enumerate(d['opts'][x]):
                w = o[0]; gw = d['gate'][w][0]
                e['gate'][x][k] = (gw * Gam + d['gate'][x][k]) if scale else (gw + d['gate'][x][k] + Gam * 0)
                e['opts'][x][k] = [-1, o[1], o[2]]
    e['lev'] = [max(0, l - 1) for l in d['lev']]
    return e
def lift(d, split=False, swapAB=False):
    """G^: new movers A = N, B = N + 1 at level 0; four new ranks above all (even), larger on option 0; new gates above all.
    split=True (control): old level-0 movers alternate W-target A / B instead of all A."""
    e = cp(d); N = d['N']; nb = len(d['br']); R = max(d['br']) + 1; Gg = max(sum(d['gate'], [])) + 1
    A, B = N, N + 1
    e['lev'] = [l + 1 for l in d['lev']] + [0, 0]
    zero = [x for x in range(N) if d['lev'][x] == 0]
    for i, x in enumerate(zero):
        tgt = (B if (split and i % 2) else A)
        e['opts'][x] = [[tgt, o[1], o[2]] for o in d['opts'][x]]
    e['opts'] += [[[-1, -1, nb], [-1, -1, nb + 1]], [[-1, -1, nb + 2], [-1, -1, nb + 3]]]
    e['br'] = d['br'] + [R + 1, R, R + 3, R + 2]; e['bp'] = d['bp'] + [0, 0, 0, 0]
    ga, gb = ([Gg + 2, Gg + 3], [Gg, Gg + 1]) if swapAB else ([Gg, Gg + 1], [Gg + 2, Gg + 3])
    e['gate'] = d['gate'] + [ga, gb]
    e['start'] = list(d['start']) + [0, 0]; e['N'] = N + 2
    return e
def freeze0(d, st):
    e = cp(d)
    for x in range(d['N']):
        if d['lev'][x] == 0:
            k = st[x]; e['opts'][x] = [d['opts'][x][k]]; e['gate'][x] = [d['gate'][x][k]]
    e['start'] = [0 if d['lev'][x] == 0 else st[x] for x in range(d['N'])]
    return e
def in_L(d, dd):
    deg = [len(o) for o in d['opts']]
    return (sorted(set(d['lev'])) == list(range(dd)) and max(deg) <= 2 and
            all(sum(1 for x in range(d['N']) if d['lev'][x] == l and deg[x] == 2) == 2 for l in range(dd)))
def rand_L(rng, dd, extra):
    """L_d genome: two degree-2 movers per level plus up to `extra` degree-1 movers at random levels."""
    lev = [l for l in range(dd) for _ in range(2)]; deg = [2] * len(lev)
    for _ in range(rng.randint(0, extra)): lev.append(rng.randrange(dd)); deg.append(1)
    N = len(lev); perm = list(range(N)); rng.shuffle(perm); pos = {x: i for i, x in enumerate(perm)}
    opts = []; nb = 0
    for x in range(N):
        ox = []
        for k in range(deg[x]):
            w = -1 if lev[x] == 0 else rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
            later = [y for y in range(N) if pos[y] > pos[x]]
            xt = -1 if (not later or rng.random() < 0.15) else rng.choice(later)
            ox.append([w, xt, nb]); nb += 1
        opts.append(ox)
    br = list(range(nb)); rng.shuffle(br); bp = [rng.randrange(2) for _ in range(nb)]
    gs = list(range(nb)); rng.shuffle(gs); it = iter(gs)
    return dict(N=N, lev=lev, opts=opts, gate=[[next(it) for _ in o] for o in opts], br=br, bp=bp, start=[rng.randrange(len(o)) for o in opts])
def segcap(d, st):
    dd = max(d['lev']) + 1; sts = run(d, st); T = len(sts) - 1; inc('L_runs'); inc('L_steps', T)
    l0 = [t for t in range(1, T + 1) if any(d['lev'][x] == 0 and sts[t][x] != sts[t-1][x] for x in range(d['N']))]
    if len(l0) > 2: inc('VIOL_L0>2')
    if not l0: segs = [(1, T)]
    else: segs = [(1, l0[0] - 1), (l0[0] + 1, l0[-1] - 1), (l0[-1] + 1, T)]
    tot = sum(max(0, b - a + 1) for a, b in segs) + len(l0)
    if tot != T: inc('VIOL_decomp')
    seg1 = T if not l0 else l0[0] - 1
    inc('seg1_max_d%d' % dd, 0); C['seg1_max_d%d' % dd] = max(C['seg1_max_d%d' % dd], seg1)
    C['T_max_d%d' % dd] = max(C.get('T_max_d%d' % dd, 0), T)
    if dd < 2: return T
    for a, b in segs:
        if b < a: continue
        inc('segments')
        Hd = shift(freeze0(d, sts[a-1]))
        if not in_L(Hd, dd - 1): inc('VIOL_notL')
        SH = run(Hd)   # frozen level-0 movers have option index 0 in H-down: map back to s_(a-1)'s option
        back = [[sts[a-1][x] if d['lev'][x] == 0 else s[x] for x in range(d['N'])] for s in SH]
        if back[:b - a + 2] != [list(s) for s in sts[a-1:b+1]] or len(SH) - 1 < b - a + 1: inc('VIOL_SEGCAP_chain')
        C['HdownT_minus_seg_max'] = max(C.get('HdownT_minus_seg_max', 0), len(SH) - 1 - (b - a + 1))
        C['seglen_max_d%d' % dd] = max(C.get('seglen_max_d%d' % dd, 0), b - a + 1)
    return T
if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'inst':
        L = json.load(open(sys.argv[2])); O = json.load(open(sys.argv[3]))
        deg = [len(o) for o in L['opts']]; dd = max(L['lev']) + 1
        lad = all(sorted(L['lev']).count(l) == 2 for l in range(dd)) and set(deg) == {2}
        sL = run(L); T = len(sL) - 1; sO = run(O)
        l0 = [t for t in range(1, T + 1) if any(L['lev'][x] == 0 and sL[t][x] != sL[t-1][x] for x in range(L['N']))]
        print('lifted: N', L['N'], 'd', dd, '2-wide degree-2 ladder (no degree-1):', lad, 'in L_d:', in_L(L, dd), 'T', T, 'level-0 steps', l0,
              'seg1', T if not l0 else l0[0] - 1, '> 2d-1 =', 2 * dd - 1)
        old = [x for x in range(L['N']) if L['lev'][x] >= 1]; new = [x for x in range(L['N']) if L['lev'][x] == 0]
        # match old movers of L with O's movers by position (lift keeps indices or appends); report both
        print('orig T', len(sO) - 1, 'old movers of L', old, 'new', new)
        same_idx = len(old) == O['N'] and all([s[x] for x in range(O['N'])] == list(o) for s, o in zip(sL, sO)) and len(sL) == len(sO)
        print('run on movers 0..N_orig-1 equals orig run:', same_idx)
        own = lift(O); sown = run(own)
        print('own lift of ORIG: T', len(sown) - 1, 'same run on old movers:', [s[:O['N']] for s in sown] == [list(s) for s in sO],
              'A,B fixed:', all(s[O['N']:] == [0, 0] for s in sown))
    elif mode == 'rand':
        seed, cnt, Nmax, Dmax = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for _ in range(cnt):
            d = m2.rand_genome(rng, Nmax, Dmax); g = m2.G(d)
            starts = [d['start']] + [[rng.randrange(len(o)) for o in d['opts']] for _ in range(3)]
            for st in starts:
                d['start'] = st; s0 = run(d); inc('lift_runs')
                e = lift(d); se = run(e)
                if [s[:d['N']] for s in se] != [list(s) for s in s0] or any(s[d['N']:] != [0, 0] for s in se): inc('VIOL_LIFT')
                for sw in (False, True):
                    c = lift(d, split=True, swapAB=sw); sc = run(c)
                    if [s[:d['N']] for s in sc] != [list(s) for s in s0]: inc('CTRL_lift_split_differs')
                if max(d['lev']) >= 1:
                    f = freeze0(d, st); sf = run(f); sh = run(shift(f)); inc('shift_runs')
                    if [list(s) for s in sh] != [list(s) for s in sf]: inc('VIOL_SHIFT')
                    if [list(s) for s in run(shift(f, scale=False))] != [list(s) for s in sf]: inc('CTRL_shift_noscale_differs')
    elif mode == 'lad':
        seed, cnt, Dmax, extra = map(int, sys.argv[2:6]); allst = len(sys.argv) > 6 and sys.argv[6] == '1'; rng = random.Random(seed)
        for _ in range(cnt):
            dd = rng.randint(1, Dmax); d = rand_L(rng, dd, extra); assert in_L(d, dd)
            sts = itertools.product(*[range(len(o)) for o in d['opts']]) if allst else [d['start']]
            for st in sts: segcap(d, list(st))
    elif mode in ('json', 'mut'):   # json FILE... (L_d genomes only; ALLN=n every start for N <= n) | mut SEED ITERS FILE... (climb T)
        sp2 = importlib.util.spec_from_file_location('sg', os.path.join(H, '..', 'R2-P-IDEAL-SEG', 'seg_check.py'))
        sg = importlib.util.module_from_spec(sp2); sp2.loader.exec_module(sg)
        files = sys.argv[2:] if mode == 'json' else sys.argv[4:]
        if mode == 'mut': rng = random.Random(int(sys.argv[2])); iters = int(sys.argv[3])
        ALLN = int(os.environ.get('ALLN', '0'))
        for f in files:
            d = json.load(open(f)); dd = max(d['lev']) + 1
            if not in_L(d, dd): inc('skipped_not_L'); continue
            inc('L_files')
            if mode == 'json':
                sts = [d['start']] + ([list(t) for t in itertools.product(*[range(len(o)) for o in d['opts']]) if list(t) != d['start']] if d['N'] <= ALLN else [])
                for st in sts: segcap(d, st)
            else:
                T0 = segcap(d, d['start'])
                for _ in range(iters):
                    e = sg.mutate(rng, d); T = segcap(e, e['start'])
                    if T >= T0: d, T0 = e, T
    print(' '.join(f'{k}={v}' for k, v in sorted(C.items())))
