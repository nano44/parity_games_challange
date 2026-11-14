#!/usr/bin/env python3
"""REFEREE-2 succ. 27: line reading vs packet reading of R105 CHAINED.
packet: h_(t-1) on the chain of (h_t, s_t(h_t)) under s_(t-2) as a mover OTHER than h_t.
line  : h_(t-1) lies on that chain (the chain starts at (h_t, w), so h_(t-1) = h_t counts).
Counts per run: DIFF (steps chained under line only), CB_i_line (chained-line steps with NOT pi(h_t) < pi(h_(t-1))),
CB_i_pkt, CB_ii_line (T > N(1+U')), CB_ii_pkt (T > N(1+U)), UEQ_line (U' > max(T-1,0)), MC_line (unchained-line t with |Mv_(t-1)|<2).
Usage: chained_check.py json FILE... [ALLN=n env] | rand SEED COUNT NMAX DMAX [1=allstarts] (LADDER=1 env) | mut SEED ITERS FILE...
       FIRST=path: write the first DIFF instance (genome, start, step) as JSON there."""
import sys, os, json, random, itertools, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('m2', os.path.join(H, '..', 'R2-P-IDEAL-M2', 'm2_check.py'))
m2 = importlib.util.module_from_spec(sp); sp.loader.exec_module(m2)
C = {}; FIRST = os.environ.get('FIRST'); found = [None]
def inc(k, v=1): C[k] = C.get(k, 0) + v
def topo(g):  # one topological order pi of the Xi-graph (DFS postorder reversed); CHAIN-BACK (i) is for every pi
    seen, out = set(), []
    def dfs(x):
        seen.add(x)
        for o in g.opts[x]:
            if o[1] != -1 and o[1] not in seen: dfs(o[1])
        out.append(x)
    for x in range(g.N):
        if x not in seen: dfs(x)
    out.reverse(); return {x: i for i, x in enumerate(out)}
def check(g, d, start):
    sts = g.run(start); T = len(sts) - 1; pi = topo(g); inc('runs'); inc('steps', T)
    Mv = [None] + [{x for x in range(g.N) if sts[t][x] != sts[t-1][x]} for t in range(1, T+1)]
    h = [None] + [min(Mv[t], key=lambda x: (g.lev[x], x)) for t in range(1, T+1)]
    U = Ul = 0
    for t in range(2, T+1):
        ch = g.chain(sts[t-2], h[t], sts[t][h[t]])
        pk = any(y == h[t-1] for (y, _) in ch[1:]); ln = any(y == h[t-1] for (y, _) in ch)
        U += not pk; Ul += not ln
        if ln != pk:
            inc('DIFF')
            if found[0] is None:
                found[0] = dict(genome=d, start=list(start), t=t, h_t=h[t], h_tm1=h[t-1], s_tm2=sts[t-2], s_tm1=sts[t-1], s_t=sts[t],
                                Mv_tm1=sorted(Mv[t-1]), Mv_t=sorted(Mv[t]), T=T, chain=ch)
        if pk and not pi[h[t]] < pi[h[t-1]]: inc('CB_i_pkt')
        if ln and not pi[h[t]] < pi[h[t-1]]: inc('CB_i_line')
        if not ln and len(Mv[t-1]) < 2: inc('MC_line')
    inc('U', U); inc('Uline', Ul)
    if T > g.N*(1+U): inc('CB_ii_pkt')
    if T > g.N*(1+Ul): inc('CB_ii_line')
    if U > max(T-1, 0): inc('UEQ_pkt')
    if Ul > max(T-1, 0): inc('UEQ_line')
    if max(g.deg) <= 2: inc('d2runs'); inc('d2DIFF', 0)
    return T, U, Ul
def d2diff(g, before):  # DIFF at degree <= 2 is impossible by XI-NEW; count it
    if max(g.deg) <= 2 and C.get('DIFF', 0) > before: inc('DIFF_deg2', C['DIFF'] - before)
def run_one(d, start):
    g = m2.G(d); b = C.get('DIFF', 0); r = check(g, d, start); d2diff(g, b); return r
if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'json':
        ALLN = int(os.environ.get('ALLN', '0'))
        for f in sys.argv[2:]:
            d = json.load(open(f)); g = m2.G(d)
            sts = [g.start] + ([list(s) for s in itertools.product(*[range(x) for x in g.deg]) if list(s) != g.start] if g.N <= ALLN else [])
            for st in sts: run_one(d, st)
    elif mode == 'rand':
        seed, cnt, Nmax, Dmax = map(int, sys.argv[2:6]); allst = len(sys.argv) > 6 and sys.argv[6] == '1'
        rng = random.Random(seed)
        for _ in range(cnt):
            d = m2.rand_genome(rng, Nmax, Dmax); g = m2.G(d)
            for st in (itertools.product(*[range(x) for x in g.deg]) if allst else [g.start]): run_one(d, list(st))
    elif mode == 'mut':   # climb T - N(1+U') (the slack of CHAIN-BACK (ii) under the line reading)
        seed, iters = int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); best = -10**9
        for f in sys.argv[4:]:
            d = json.load(open(f)); g = m2.G(d); T, U, Ul = check(g, d, g.start); sc = T - g.N*(1+Ul)
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
                T, U, Ul = run_one(e, e['start']); s2 = T - e['N']*(1+Ul)
                if s2 >= sc: d, sc = e, s2
            best = max(best, sc)
        print('best slack T - N(1+Uline)', best)
    if FIRST and found[0]: json.dump(found[0], open(FIRST, 'w'))
    print(' '.join(f'{k}={v}' for k, v in sorted(C.items())))
