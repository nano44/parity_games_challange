#!/usr/bin/env python3
"""L-LOWER 10 (item 2): search for a d 32 genome realizing the exact level-8 target (build.core8: HIT7's minimal stretch + pair 7).
Score = gsolve violations of the full constraint set (movers 0..15 clamped to the target, helpers simulated by the genome's rules,
l7/ranksolve.constraints). Score 0 = the exact greedy succeeds: the genome with the solved ranks REPRODUCES the target (8 caps by
construction; re-checked by sim6). Moves: re-point one option (acyclic), swap two ranks, flip a sign, permute a helper level's
gates, flip a helper start bit; every 50 accepted moves the ranks are reset to gsolve's (kept if not worse). Annealing at
temperature temp. Resumable: starts from OUT if it exists. Usage: anneal.py D28 D32 OUT SEED SECONDS [temp]"""
import sys, os, random, time, math
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here)
from build import *
from gsolve import gsolve
from sim6 import topo
def score(D, CT):
    S, E = fulltraj(D, CT); cons = constraints(E, S); v, br, bp = gsolve(cons, 4 * D['d']); return v, br, bp
def mutate(D, rng):
    E = {k: (list(v) if isinstance(v, list) else v) for k, v in D.items()}; N = 2 * E['d']; r = rng.random()
    if r < 0.55:
        for _ in range(20):
            m = rng.randrange(2 * N); x = m // 2; y = rng.choice([-1] + [z for z in range(N) if z != x])
            old = E['xt'][m]; E['xt'][m] = y
            if topo(E) is not None: return E
            E['xt'][m] = old
        return E
    if r < 0.75:
        a, b = rng.randrange(2 * N), rng.randrange(2 * N); E['br'][a], E['br'][b] = E['br'][b], E['br'][a]; return E
    if r < 0.85:
        a = rng.randrange(2 * N); E['bp'][a] ^= 1; return E
    if r < 0.93:
        l = rng.randrange(8, E['d']); g = E['gate'][4 * l:4 * l + 4]; rng.shuffle(g); E['gate'][4 * l:4 * l + 4] = g; return E
    x = rng.randrange(16, N); E['start'][x] ^= 1; return E
if __name__ == '__main__':
    D28 = rd(sys.argv[1]); out = sys.argv[3]; seed = int(sys.argv[4]); secs = float(sys.argv[5]); temp = float(sys.argv[6]) if len(sys.argv) > 6 else 2.0
    D = fixgates(rd(out if os.path.exists(out) else sys.argv[2])); CT = core8(D28); rng = random.Random(seed)
    cur, br, bp = score(D, CT); best = cur; t0 = time.time(); it = acc = 0
    print(f'start score {cur}', flush=True)
    while time.time() - t0 < secs:
        it += 1; E = mutate(D, rng); v, ebr, ebp = score(E, CT)
        if v <= cur or rng.random() < math.exp((cur - v) / temp):
            D, cur = E, v; acc += 1
            if acc % 50 == 0:
                F = dict(D); F['br'], F['bp'] = ebr, ebp; v2 = score(F, CT)[0]
                if v2 <= cur: D, cur = F, v2
            if cur < best:
                best = cur; wr(D, out + '.tmp'); os.replace(out + '.tmp', out)
                if best == 0: print('HIT score 0', flush=True); break
        if it % 500 == 0: print(f'{time.strftime("%H:%M:%S", time.gmtime())} it {it} acc {acc} cur {cur} best {best}', flush=True)
    print('end best', best, 'it', it, flush=True)
