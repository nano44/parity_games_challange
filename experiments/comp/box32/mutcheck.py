#!/usr/bin/env python3
"""L-COMP box 32: validation of enc32.py in checker mode (--fix all). For a base genome G and its own core target (H levels), make
mutants (seeded), and compare three verdicts of REALIZES(mutant, target) (definition in enc32.py docstring):
  fenc   (L-LOWER 9 l9/fenc.c, TRAJ=1: core rows t = 0..T and T),  sim6 (L-LOWER l6/sim6.py, big-integer values),
  enc32  (CNF with every parameter fixed, CaDiCaL).  replay30 (box30, my box27 simulator) is run on each mutant for T and F(0..H-1),
  and must agree with fenc's T and F.
Mutant classes: rank swap of two options, sign flip, start flip of a helper, helper gate swap, rewire one option (acyclic only).
Usage: mutcheck.py GENOME TARGET H NMUT SEED OUTDIR"""
import sys, os, random, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'box31', 'l-lower'))
import enc32, sim6
from pysat.solvers import Solver
HERE = os.path.dirname(os.path.abspath(__file__))
gp, tp, H, NM, SEED, OUT = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
os.makedirs(OUT, exist_ok=True)
D0 = enc32.rdgen(gp); S, nc = enc32.rdtarget(tp); T = len(S) - 1; NC = 2 * H; d = D0['d']; N = 2 * d
def realizes_rows(rows):
    return len(rows) - 1 == T and all(tuple(r[:NC]) == tuple(S[t]) for t, r in enumerate(rows))
def v_fenc(p, D):
    o = subprocess.run([os.path.join(HERE, 'bin', 'fenc'), p], env=dict(os.environ, TRAJ='1'), capture_output=True, text=True).stdout
    rows = [list(map(int, D['start']))]
    Tl = None; F = None
    for ln in o.split('\n'):
        w = ln.split()
        if not w: continue
        if w[0] == 'CYCLIC': return None, None, None
        if w[0] == 'T': Tl = int(w[1]); F = list(map(int, w[3:3 + d]))
        else: rows.append([int(c) for c in w[1]])
    assert Tl == len(rows) - 1
    return realizes_rows(rows), Tl, F
def v_sim6(D):
    St, O = sim6.run(D)
    return realizes_rows([list(x) for x in St]), len(St) - 1
def v_r30(p):
    o = subprocess.run([sys.executable, os.path.join(HERE, '..', 'box30', 'replay30.py'), p], capture_output=True, text=True).stdout
    w = o.split(); i = w.index('T'); Tl = int(w[i + 1]); F = list(map(int, w[w.index('F') + 1:]))
    return Tl, F
def v_enc(D):
    try:
        E, info, ctx = enc32.build(D, S, H, {'ranks', 'signs', 'gates', 'starts'})
    except SystemExit as e:
        return False, str(e)
    if E.empty: return False, "empty clause"
    sv = Solver(name='cadical195', bootstrap_with=E.cl); r = sv.solve(); sv.delete(); return bool(r), ''
rng = random.Random(SEED)
def acyc(D):
    xt = D['xt']; vis = [0] * N
    sys.setrecursionlimit(10000)
    def go(x):
        if vis[x] == 2: return True
        if vis[x] == 1: return False
        vis[x] = 1
        for k in (0, 1):
            y = xt[2 * x + k]
            if y >= 0 and not go(y): return False
        vis[x] = 2; return True
    return all(go(x) for x in range(N))
def mutate(i):
    D = {k: (list(v) if isinstance(v, list) else v) for k, v in D0.items()}
    cls = ['rank', 'sign', 'start', 'gate', 'wire'][i % 5]
    if cls == 'rank':
        a, b = rng.sample(range(2 * N), 2); D['br'][a], D['br'][b] = D['br'][b], D['br'][a]; desc = f'swap br {a} {b}'
    elif cls == 'sign':
        a = rng.randrange(2 * N); D['bp'][a] ^= 1; desc = f'flip bp {a}'
    elif cls == 'start':
        a = rng.randrange(NC, N); D['start'][a] ^= 1; desc = f'flip start {a}'
    elif cls == 'gate':
        l = rng.randrange(H, d); a = rng.randrange(2); i1, i2 = 4 * l + a, 4 * l + 2 + a
        D['gate'][i1], D['gate'][i2] = D['gate'][i2], D['gate'][i1]; desc = f'swap gate {i1} {i2}'
    else:
        while True:
            m = rng.randrange(2 * N); y = rng.choice([-1] + list(range(N)))
            if y == D0['xt'][m] or y == m // 2: continue
            D['xt'][m] = y
            if acyc(D): break
            D['xt'][m] = D0['xt'][m]
        desc = f'xt[{m}] {D0["xt"][m]} -> {y}'
    return cls, desc, D
res = []; mism = 0
for i in range(-1, NM):
    if i < 0: cls, desc, D = 'base', 'unmutated', D0
    else: cls, desc, D = mutate(i)
    p = os.path.join(OUT, f'mut{i:03d}.txt' if i >= 0 else 'base.txt'); enc32.wrgen(D, p)
    vf, Tf, Ff = v_fenc(p, D); vs, Ts = v_sim6(D); Tr, Fr = v_r30(p); ve, why = v_enc(D)
    ok = (vf == vs == ve) and Tf == Ts == Tr and Ff[:H] == Fr[:H]
    mism += (not ok)
    line = f'{i:3d} {cls:5s} {desc:28s} fenc {int(vf)} sim6 {int(vs)} enc32 {int(ve)} T {Tf}/{Ts}/{Tr} F0..{H-1} {"=" if Ff[:H] == Fr[:H] else "!="} {Ff[:H]} {"OK" if ok else "MISMATCH"} {why}'
    print(line, flush=True); res.append((cls, vf))
acc = sum(1 for c, v in res if v); print(f'SUMMARY mutants {NM} (+ base): realize {acc}, reject {len(res) - acc}, mismatches {mism}')
