#!/usr/bin/env python3
"""L-LOWER 8 (Lead 21:36Z): can KILL238's 8 untriggered (8,0) 5-windows be given PULSE_5 = 2 by hand, decided exactly?
Target for movers 0-13: KILL238's run, except in each bad block (opener 8 at step a, u1 = a + 1, u2 = a + 2, next opener 9 at a + 3)
the pairs 5-6 pattern of the good (8,0) windows is transplanted: a: 8; a+1: 11, 13; a+2: 12; a+3: 10, 13; a+4: 12; a+5: the moves of
pairs 0-4 of the original step a+3 (9); then the original run resumes (+2 steps per block). Pairs 0-4 frozen in inserted steps. Movers
>= 14: completed by their own rules (clamp.runclamp, current ranks). Then ranksolve on the FULL trajectory (all ranks/signs free) --
exact for that (wiring, trajectory) pair. Edits: single re-points of option m (any mover >= 11 option, plus 10:1) to any target keeping
the graph acyclic, each decided the same way. Usage: mirror.py GENOME [edits]  (edits: 'none' | 'single' [from to])"""
import sys, os, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, os.path.join(H, '..', 'l7'))
from sim6 import rd, run, topo, Fprof, caps, okeys
from clamp import runclamp
from ranksolve import constraints, solve
D0 = rd(sys.argv[1]); S, O = run(D0); T = len(S) - 1; N = 2 * D0['d']
b5 = [t for t in range(1, T + 1) if O[t][4] != O[t - 1][4]]; cuts = [1] + b5 + [T + 1]; bad = []
for a, e in zip(cuts, [c - 1 for c in cuts[1:]]):
    if a > 1 and S[a][8] != S[a - 1][8] and S[a][8] == 0:
        mv = [t for t in range(a, e + 1) for x in (10, 11) if S[t][x] != S[t - 1][x]]
        if mv[1] - mv[0] == 1: bad.append(a)
assert len(bad) == 8, bad
def target():
    tg = [list(S[0][:14])]; t = 1
    while t <= T:
        if t in bad:
            a = t; s = list(S[a][:14]); tg.append(list(s))                       # a: opener 8 (as original)
            s1 = list(s); s1[11] = S[a + 1][11]; s1[13] = S[a + 1][13]; tg.append(s1)  # a+1: 11, 13
            s2 = list(s1); s2[12] = 1 - s2[12]; tg.append(s2)                       # a+2: 12
            s3 = list(s2); s3[10] = S[a + 2][10]; s3[13] = 1 - s3[13]; tg.append(s3)  # a+3: 10, 13
            s4 = list(s3); s4[12] = 1 - s4[12]; tg.append(s4)                       # a+4: 12
            s5 = list(s4); s5[:10] = S[a + 3][:10]; tg.append(s5)                   # a+5: pairs 0-4 of original a+3
            assert s5 == list(S[a + 3][:14]), (a, s5, S[a + 3][:14])
            t = a + 4
        else: tg.append(list(S[t][:14])); t += 1
    return tg
TG = target()
def decide(D):
    if topo(D) is None: return 'cyclic', None
    full = [tuple(x) + tuple(S[0][14:]) if i == 0 else tuple(x) + (None,) * (N - 14) for i, x in enumerate(TG)]
    tgt = [list(f) for f in full]
    for i in range(1, len(tgt)):
        for x in range(14, N): tgt[i][x] = tgt[i - 1][x] if tgt[i][x] is None else tgt[i][x]
    Sc = runclamp(D, [tuple(x) for x in tgt], set(range(14)))
    res, core = solve(constraints(D, Sc), 2 * N)
    if res is None:
        mv = sorted({c[1] for c in core}); return 'infeasible', (len(core), mv[:12])
    E = dict(D); E['br'], E['bp'] = res; S2, O2 = run(E); F = Fprof(E, O2)
    return 'FEASIBLE', (len(S2) - 1, caps(F), F[:8], S2[:len(Sc)] == Sc, E)
if __name__ == '__main__':
    t0 = time.time(); r = decide(D0); print('bad blocks', bad, 'target T', len(TG) - 1); print('no edit:', r[0], r[1] if r[0] != 'FEASIBLE' else r[1][:4], f'{time.time() - t0:.1f}s', flush=True)
    if len(sys.argv) > 2 and sys.argv[2] == 'single':
        lo, hi = (int(sys.argv[3]), int(sys.argv[4])) if len(sys.argv) > 4 else (0, 10 ** 9)
        opts = [21] + [m for m in range(2 * N) if m // 2 >= 14]; cnt = {}
        for i, m in enumerate(opts):
            if not lo <= i < hi: continue
            for y in [-1] + list(range(N)):
                if y == m // 2 or y == D0['xt'][m]: continue
                D = {k: (list(v) if isinstance(v, list) else v) for k, v in D0.items()}; D['xt'][m] = y
                st, info = decide(D); cnt[st] = cnt.get(st, 0) + 1
                if st == 'FEASIBLE':
                    print('HIT', m // 2, m % 2, '->', y, info[:4], flush=True)
                    from sim6 import wr; wr(info[4], os.path.join(H, 'out', f'mirror_hit_{m}_{y}.txt'))
            print('option', m // 2, m % 2, 'done', cnt, f'{time.time() - t0:.0f}s', flush=True)
