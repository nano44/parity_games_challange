#!/usr/bin/env python3
"""L-COMP 12 box 31: Python reference for rclimb31's LJ score, built ONLY from L-LOWER's guard_l6.py / sim6.py (copies in l-lower/):
(min(caps, J), [F(J) >= gate], -npaths(q_{J-1}, {2J, 2J+1}), -n1_J, T, F(J)) with q_{J-1} = roles(D,S,O,J-1)[1] (none -> 2J-2) and
n1_J = #windows(S, O, J) of length 1 (e == a). Also the guard (LJGUARD m:y). Usage: ref_lj.py J GATE GUARD genome.txt..."""
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
    return (min(caps(F), J), int(F[J] >= gate), -npaths(D, q, {2 * J, 2 * J + 1}), -n1, T, F[J]), caps(F), q
if __name__ == '__main__':
    J, gate = int(sys.argv[1]), int(sys.argv[2]); guard = [tuple(map(int, t.split(':'))) for t in sys.argv[3].split(',') if t]
    for p in sys.argv[4:]: print(p, ref(rd(p), J, gate, guard))
