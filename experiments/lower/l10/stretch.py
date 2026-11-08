#!/usr/bin/env python3
"""L-LOWER 10: minimal pure STRETCH of a run. Keep the sequence of states of pairs 0..J-1 (J = number of core pairs) of the run S,
and give original step t a new time tau(t), strictly increasing (tau(0) = 0). Constraints (P-TOWER-FUEL Lemmas 2, 3 at H caps,
j = 1..H-2): in every j-window with two pair-j moves u1 < u2: tau(u2) - tau(u1) >= H - j (PULSE); for consecutive such windows:
tau(u1+) - tau(u2) >= H - j (GAP); and the level-(H-1) windows: consecutive changes of o(H-2) at least 2 apart in tau, first one
at tau >= 2... (we use: all o(H-2) changes >= 2 apart, first >= 2, last <= T' - 2). Minimal tau = longest path (difference
constraints, all forward). Prints T', inserted steps per original gap histogram. Usage: stretch.py GENOME.txt H"""
import sys, os
from collections import Counter, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l9'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run
from slack import windows
def stretch(S, O, H):
    T = len(S) - 1; need = defaultdict(int)   # need[(a, b)] = min tau(b) - tau(a)
    for j in range(1, H - 1):
        W = windows(S, O, j); k = H - j
        for i, (a, e, mv) in enumerate(W):
            if len(mv) == 2:
                need[(mv[0], mv[1])] = max(need[(mv[0], mv[1])], k)
                if i + 1 < len(W) and len(W[i + 1][2]) == 2:
                    b = W[i + 1][2][0]; need[(mv[1], b)] = max(need[(mv[1], b)], k)
    ch = [t for t in range(1, T + 1) if O[t][H - 2] != O[t - 1][H - 2]]
    for a, b in zip(ch, ch[1:]): need[(a, b)] = max(need[(a, b)], 2)
    if ch: need[(0, ch[0])] = max(need[(0, ch[0])], 2)
    inc = defaultdict(list)
    for (a, b), k in need.items(): inc[b].append((a, k))
    tau = [0] * (T + 1)
    for t in range(1, T + 1):
        tau[t] = max([tau[t - 1] + 1] + [tau[a] + k for a, k in inc[t]])
    Tp = tau[T] + (2 if ch and ch[-1] == T else 0)
    return tau, Tp, need
if __name__ == '__main__':
    D = rd(sys.argv[1]); H = int(sys.argv[2]); S, O = run(D); T = len(S) - 1
    J = H - 1
    # core = pairs 0..H-2 only (pair H-1 is the new one): drop steps where none of them moves (they are not core steps)
    keep = [0] + [t for t in range(1, T + 1) if S[t][:2 * J] != S[t - 1][:2 * J]]
    S2 = [S[t] for t in keep]; O2 = [O[t] for t in keep]
    tau, Tp, need = stretch(S2, O2, H)
    ins = Counter(tau[i] - tau[i - 1] - 1 for i in range(1, len(tau)))
    print('T', T, 'core steps', len(keep) - 1, 'stretched T', Tp, 'inserted', Tp - (len(keep) - 1), 'gap-insert hist', sorted(ins.items()))
