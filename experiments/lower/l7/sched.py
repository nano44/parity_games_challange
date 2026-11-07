#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §7: the SEQUENTIAL schedule of an h-capped tower (d = h + extra levels, the extra ones frozen).
Level 0: gates 0 2 1 3, start (1, 1): after the initial level-1 job, mover 1 moves (o(0) 0 -> 1), then mover 0 (o(0) -> 0).
Pairs 1..h-1 start joined at 1 (the initial keys are 0), so each also moves in its first window.
alpha[l] in {0, 1}: delay of f_l after its key change (0 = same step; the initial windows always use 1).
Level l >= 1: first mover f = 2l + 1, second q = 2l; gates with g[4l + a] < g[4l + 2 + a] (joined value 0; split value 1).
job(l, t): the key of level l changed at step t; f_l moves at t + 1; job(l + 1, t + 1) ends at e1; q_l moves at e1 + 1; job(l + 1, e1 + 1)
ends at e2; returns e2. init(l, t): init(l + 1, t), then job(l, ·) (initial windows nest). The top level h - 1: f at t + 1, q at t + 2. One move per step. Importable: schedule(h, d) -> (D_shell, S)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import okeys
def schedule(h, d=None, alpha=None):
    d = d or h; N = 2 * d; moves = {}; alpha = alpha or [1] * h
    def job(l, t):
        if l >= h: return t
        f, q = 2 * l + 1, 2 * l
        a = alpha[l] if t > 0 else 1                      # alpha[l] = 0: f moves in the step of its key change
        moves.setdefault(t + a, []).append(f); e1 = job(l + 1, t + a); moves.setdefault(e1 + 1, []).append(q); return job(l + 1, e1 + 1)
    def init(l, t):   # the initial window of level l: the initial windows above complete first
        if l >= h: return t
        t2 = init(l + 1, t); return job(l, t2)
    e0 = init(1, 0); moves.setdefault(e0 + 1, []).append(1); e1 = job(1, e0 + 1); moves.setdefault(e1 + 1, []).append(0); T = job(1, e1 + 1)
    gate = [0, 2, 1, 3] + [v for l in range(1, d) for v in (4 * l + 1000, 4 * l + 1001, 4 * l + 1002, 4 * l + 1003)]
    start = [1, 1] + [1] * (2 * h - 2) + [0] * (N - 2 * h)
    D = {'d': d, 'xt': [-1] * (2 * N), 'br': list(range(2 * N)), 'bp': [0] * (2 * N), 'gate': gate, 'start': start}
    s = list(start); S = [tuple(s)]
    for t in range(1, T + 1):
        for x in sorted(moves.get(t, [])):              # lower levels first: a mover's key uses the new lower states
            s[x] = 0 if x <= 1 else okeys(D, s)[x // 2 - 1]
        S.append(tuple(s))
    return D, S
if __name__ == '__main__':
    h = int(sys.argv[1]); D, S = schedule(h); T = len(S) - 1
    O = [okeys(D, s) for s in S]; F = [sum(1 for t in range(1, T + 1) if O[t][l] != O[t - 1][l]) for l in range(D['d'])]
    print('h', h, 'T', T, 'F', F, 'caps target', [2 ** (l + 2) - 2 for l in range(h)])
