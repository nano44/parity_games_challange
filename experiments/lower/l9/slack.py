#!/usr/bin/env python3
"""L-LOWER 9: room conditions of P-TOWER-FUEL Lemmas 2, 3 (PULSE-NEST, GAP-NEST) for H capped levels: every j-window
(1 <= j <= H-2) in which both pair-j members move needs PULSE = u2 - u1 >= H - j and, for consecutive windows W, W+, GAP = u1(W+) - u2(W)
>= H - j. Prints per j: windows, PULSE violations, GAP violations, histogram of PULSE and GAP. Usage: slack.py GENOME.txt H"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
def windows(S, O, j):
    T = len(S) - 1; b = [t for t in range(1, T + 1) if O[t][j - 1] != O[t - 1][j - 1]]; cuts = [1] + b + [T + 1]; W = []
    for a, e in zip(cuts, cuts[1:]):
        mv = sorted(t for t in range(a, e) for x in (2 * j, 2 * j + 1) if S[t][x] != S[t - 1][x])
        W.append((a, e, mv))
    return W
def slack(D, H, S=None, O=None):
    if S is None: S, O = run(D)
    res = {}
    for j in range(1, H - 1):
        W = windows(S, O, j); need = H - j; P = []; G = []
        for i, (a, e, mv) in enumerate(W):
            if len(mv) == 2:
                P.append(mv[1] - mv[0])
                if i + 1 < len(W) and len(W[i + 1][2]) == 2: G.append(W[i + 1][2][0] - mv[1])
        res[j] = (len(W), sum(1 for p in P if p < need), sum(1 for g in G if g < need), Counter(P), Counter(G), sum(1 for w in W if len(w[2]) != 2))
    return res
if __name__ == '__main__':
    D = rd(sys.argv[1]); H = int(sys.argv[2]); S, O = run(D); print('T', len(S) - 1)
    for j, (nw, pv, gv, P, G, bad) in slack(D, H, S, O).items():
        print(f'j {j} need {H - j}: windows {nw} not-two-moves {bad} PULSE<need {pv} GAP<need {gv} | PULSE {sorted(P.items())} GAP {sorted(G.items())}')
