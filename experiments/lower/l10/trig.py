#!/usr/bin/env python3
"""L-LOWER 10: trigger map. For every move of a mover x of pairs 1..J at step t with wait w >= 1 (x free and holding at t - 1):
the triggers = movers y that changed between S[t-2] and S[t-1] and lie on chain(x,0) or chain(x,1) at S[t-1] or S[t-2];
the decider = the top-rank option of chain(x,0) xor chain(x,1) at S[t-1] (mover, option). For key-fired moves (w = 0): the
decider at S[t-1] only. Per mover: Counter of (wait, triggers, decider mover). Usage: trig.py GENOME.txt J"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run, chain, dec
def cmovers(D, s, x):
    return {e[2] for k in (0, 1) for e in chain(D, s, x, k)}
def trig(D, S, O, J):
    T = len(S) - 1; res = {}
    for x in range(2, 2 * J + 2):
        l = x // 2; last = 0; C = Counter()
        for t in range(1, T + 1):
            if O[t][l - 1] != O[t - 1][l - 1]: last = t
            if S[t][x] != S[t - 1][x]:
                w = t - last; dm = dec(D, S[t - 1], x)[1]
                if w >= 1 and t >= 2:
                    ch = {y for y in range(len(S[0])) if S[t - 1][y] != S[t - 2][y]}
                    tr = tuple(sorted(ch & (cmovers(D, S[t - 1], x) | cmovers(D, S[t - 2], x))))
                else: tr = ()
                C[(min(w, 9), tr, dm)] += 1
        res[x] = C
    return res
if __name__ == '__main__':
    D = rd(sys.argv[1]); J = int(sys.argv[2]); S, O = run(D)
    for x, C in trig(D, S, O, J).items():
        print(f'mover {x} level {x // 2}:', ' | '.join(f'w{w} trig{list(tr)} dec{dm} x{n}' for (w, tr, dm), n in sorted(C.items(), key=lambda a: -a[1])))
