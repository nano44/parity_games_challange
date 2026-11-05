#!/usr/bin/env python3
"""REFEREE-2 successor 27: semantic check of L-COMP box 27 cnf.py (the artifact under audit, passed as CNFPY) against MY simulator
(R2-P-IDEAL-M2/m2_check.py, written from R104's text; no lane simulator). For each (genome of L^R_d, start): T := my simulator's run
length; cnf.build(d, L) with the whole genome and start pinned by unit clauses must be SAT at L = T and UNSAT at L = T + 1.
Usage: CNFPY=path/cnf.py pin_mine.py json FILE... (ALLST=1: every start)  |  CNFPY=... pin_mine.py rand SEED COUNT D [ISOFRAC]"""
import sys, os, json, random, itertools, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
def load(name, path):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
m2 = load('m2', os.path.join(H, '..', 'R2-P-IDEAL-M2', 'm2_check.py'))
fc = load('fc', os.path.join(H, '..', 'R2-P-IDEAL-FLIP', 'flip_check.py'))
cnf = load('cnf', os.environ['CNFPY'])
from pysat.solvers import Solver
C_ = {}
def inc(k, v=1): C_[k] = C_.get(k, 0) + v
def pinned_sat(d, G, start, L):
    for k in ('ISO', 'FREE0', 'P', 'W', 'SYM', 'CUBE', 'KF'): os.environ.pop(k, None)
    C, I = cnf.build(d, L)
    lit = lambda b, v: v if b else -v
    def req(l, b):
        if isinstance(l, bool):
            if l != b: C.add([])
        else: C.add([lit(b, l)])
    opts = I['opts']
    beta = {(x, k): G['opts'][x][k][2] for (x, k) in opts}
    for o in opts:
        for o2 in opts:
            if o != o2: req(I['rk'][(o, o2)], G['br'][beta[o]] < G['br'][beta[o2]])
        req(I['par'][o], G['bp'][beta[o]] == 1)
        xt = G['opts'][o[0]][o[1]][1]
        for y, v in I['Xv'][o].items(): req(v, y == xt)
    for l, V in I['gord'].items():
        for (o, o2), v in V.items():
            if v > 0: req(v, G['gate'][o[0]][o[1]] < G['gate'][o2[0]][o2[1]])
    for x in I['movers']: req(I['S'][0][x], start[x] == 1)
    s = Solver(name='cadical195', bootstrap_with=C.cl); r = s.solve(); s.delete(); return r
def check(G, start):
    d = G['N'] // 2; assert fc.in_LR(G)
    g = m2.G(G); T = len(g.run(list(start))) - 1
    a = pinned_sat(d, G, start, T); b = pinned_sat(d, G, start, T + 1)
    inc('pairs'); inc('T=%d' % T)
    if not a or b: inc('DISAGREE'); print('DISAGREE', T, a, b, json.dumps(G), start, flush=True)
if __name__ == '__main__':
    if sys.argv[1] == 'json':
        for f in sys.argv[2:]:
            G = json.load(open(f))
            if not fc.in_LR(G): inc('skip_notLR'); continue
            sts = [list(s) for s in itertools.product(range(2), repeat=G['N'])] if os.environ.get('ALLST') == '1' else [G['start']]
            for st in sts: check(G, st)
    else:
        seed, cnt, d = map(int, sys.argv[2:5]); isofrac = float(sys.argv[5]) if len(sys.argv) > 5 else 0.5; rng = random.Random(seed)
        for _ in range(cnt):
            G = fc.rand_W(rng, d, rng.random() < isofrac, LR=True); check(G, G['start'])
    print(' '.join(f'{k}={v}' for k, v in sorted(C_.items())))
