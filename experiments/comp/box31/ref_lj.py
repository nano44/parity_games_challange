#!/usr/bin/env python3
"""L-COMP 12 box 31: Python reference for rclimb31's LJ score, built ONLY from L-LOWER's guard_l6.py / sim6.py (copies in l-lower/):
(min(caps, J), [F(J) >= gate], -npaths(q_{J-1}, {2J, 2J+1}), -n1_J, T, F(J)) with q_{J-1} = roles(D,S,O,J-1)[1] (none -> 2J-2) and
n1_J = #windows(S, O, J) of length 1 (e == a). Also the guard (LJGUARD m:y). Env LJSLACK=H [LJSLACKJ=4,5]: the slack term -sv after -npaths (as rclimb31). Usage: ref_lj.py J GATE GUARD genome.txt..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "l-lower"))
from sim6 import rd, run, Fprof, caps
from guard_l6 import windows, roles, npaths
def ref(D, J, gate, guard):
    for m, y in guard:
        if D['xt'][m] != y: return None
    S, O = run(D, cap=5000)
    if S is None: return None
    T = len(S) - 1; F = Fprof(D, O); r = roles(D, S, O, J - 1); q = r[1] if r else 2 * J - 2
    n1 = sum(1 for a, e, _ in windows(S, O, J) if e == a)
    tup = (min(caps(F), J), int(F[J] >= gate), -npaths(D, q, {2 * J, 2 * J + 1}), -n1, T, F[J])
    if os.environ.get('LJSLACK'):
        H = int(os.environ['LJSLACK']); js = [int(x) for x in os.environ.get('LJSLACKJ', '4,5').split(',')]
        sv = sum(slack(S, O, j, H - j) for j in js); tup = tup[:3] + (-sv,) + tup[3:]
    return tup, caps(F), q
def slack(S, O, j, need):
    """L-LOWER l5/slack.py's per-level count (PULSE u2 - u1 < need, GAP u1(next) - u2 < need), on sim6's (S, O); a window with < 2 moves
    (slack.py would raise) counts 1 and breaks the GAP of the window before it into 1 violation if the next window has no move."""
    T = len(S) - 1; p, q = 2 * j, 2 * j + 1; cuts = [1] + [t for t in range(1, T + 1) if O[t][j-1] != O[t-1][j-1]] + [T + 1]
    W = [[t for t in range(a, b) for x in (p, q) if S[t][x] != S[t-1][x]] for a, b in zip(cuts, cuts[1:])]
    v = 0
    for i, mv in enumerate(W):
        if len(mv) < 2: v += 1; continue
        v += mv[1] - mv[0] < need
        if i + 1 < len(W): v += (W[i+1][0] - mv[1] if W[i+1] else -1) < need
    return v
if __name__ == '__main__':
    J, gate = int(sys.argv[1]), int(sys.argv[2]); guard = [tuple(map(int, t.split(':'))) for t in sys.argv[3].split(',') if t]
    for p in sys.argv[4:]: print(p, ref(rd(p), J, gate, guard))
