#!/usr/bin/env python3
"""L-LOWER 8 (BOX L8 item 0): dissect a 6-capped genome against references. Per genome: (E5) the second mover of pair 5 in EVERY
5-window with two pair-5 moves (and windows with one move / simultaneous moves); 5-window types (opening mover, new state); the failing
6-windows (not exactly one move of each of 12, 13): length, profile, the type of the enclosing 5-window, PULSE_5 of that 5-window;
the MERGE chain of 11:1 (does it pass 9:1 and 54?). Diff vs a reference genome: per field and per mover block 0-11 / 12-13 / >= 14.
Usage: kill_dissect.py REF.txt GENOME.txt ..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run, chain, Fprof
def wins(S, O, j):
    T = len(S) - 1; b = [t for t in range(1, T + 1) if O[t][j - 1] != O[t - 1][j - 1]]; cuts = [1] + b + [T + 1]
    return list(zip(cuts, [c - 1 for c in cuts[1:]]))
def moves(S, a, e, xs): return [(t, x) for t in range(a, e + 1) for x in xs if S[t][x] != S[t - 1][x]]
def dissect(p):
    D = rd(p); S, O = run(D); T = len(S) - 1; F = Fprof(D, O); nm = os.path.basename(p)
    print(f'== {nm} T {T} F(5..7) {F[5:8]}')
    sec = Counter(); kinds = Counter(); W5 = wins(S, O, 5); typ5 = {}
    for a, e in W5:
        mv = moves(S, a, e, (10, 11)); op = tuple((x, S[a][x]) for x in (8, 9) if a > 1 and S[a][x] != S[a - 1][x])
        typ5[(a, e)] = (op, mv[1][0] - mv[0][0] if len(mv) == 2 else None)
        if len(mv) == 2 and mv[0][0] != mv[1][0]: sec[mv[1][1]] += 1; kinds['two staggered'] += 1
        else: kinds[f'{len(mv)} moves' + (' same step' if len(mv) == 2 else '')] += 1
    print('  E5: second mover of pair 5 over 5-windows with two staggered moves:', dict(sec), '| window kinds:', dict(kinds))
    fail = Counter(); det = []
    for a, e in wins(S, O, 6):
        mv = moves(S, a, e, (12, 13)); prof = tuple(sorted(x for _, x in mv))
        if prof == (12, 13): continue
        par = [k for k in typ5 if k[0] <= a <= k[1]][0]; op, pulse = typ5[par]
        fail[(prof, e - a + 1, op, pulse)] += 1
    print('  failing 6-windows by (profile, length, parent 5-window opener, parent PULSE_5): count')
    for k, v in sorted(fail.items(), key=lambda kv: -kv[1]): print('   ', k, v)
    s = S[0]; c = chain(D, s, 11, 1); print('  chain 11:1 at s_0 (first 8):', [(r, x, k) for r, _, x, k in c[:8]])
    return D
if __name__ == '__main__':
    R = rd(sys.argv[1]); print('reference', os.path.basename(sys.argv[1]))
    for p in sys.argv[2:]:
        D = dissect(p); N = 2 * D['d']
        blk = lambda x: '0-11' if x < 12 else '12-13' if x < 14 else '>=14'
        for f in ('xt', 'br', 'bp'):
            dif = [m for m in range(2 * N) if D[f][m] != R[f][m]]; c = Counter(blk(m // 2) for m in dif)
            print(f'  diff {f}: {len(dif)} options', dict(c), (' movers 0-11: ' + str([(m // 2, m % 2, R[f][m], D[f][m]) for m in dif if m < 24])) if c['0-11'] else '')
        dg = [x for x in range(N) if D['gate'][2 * x:2 * x + 2] != R['gate'][2 * x:2 * x + 2]]; ds = [x for x in range(N) if D['start'][x] != R['start'][x]]
        print('  diff gate movers', Counter(blk(x) for x in dg), 'start movers', Counter(blk(x) for x in ds), [x for x in ds if x < 12])
