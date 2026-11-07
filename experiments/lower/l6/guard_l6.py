#!/usr/bin/env python3
"""L-LOWER 6: GUARD predicates for a climb toward a seventh capped level from SL41 (BOX L6 §2, §4; text genome, R104 model).
Importable, pure functions of (genome dict D, run S, O) as given by sim6.run; no global state.
  pair6_cross(D)      -> (A0, A1) if pair 6 is crossed (xt(12,k) = A_k = xt(13,1-k)) else None.
  merge_count(D,S,O)  -> number of PRE-STATES s_(a-1) .. s_(e-1) of 6-windows [a, e] at which the chain of A1's current option
                         passes A0 or the chain of A0's current option passes A1 (the MERGE of §2: then everything after the merge
                         point cancels in pair 6's comparison). On SL41: > 0 exactly in the windows under parent (9, 1).
  merge91_count(D,S,O)-> the same, restricted to 6-windows whose enclosing 5-window is of type (9, 1) (opened by mover 9 moving to 1).
  pulse5_91(D,S,O)    -> min over 5-windows of type (9, 1) of PULSE_5 = u2 - u1 of pair 5 (None if no such window or no two moves).
  guard(D, mode)      -> (ok, info). mode 'nomerge91': merge91_count == 0; mode 'pulse3': pulse5_91 >= 3; mode 'either': one of them.
                         Caps (levels 0-5 capped) are NOT part of this predicate: combine with the climb's own GUARD 0-5.
CLI: guard_l6.py genome.txt [mode]  -> prints the counts and ok."""
import sys
from sim6 import rd, run, chain, Fprof, caps
def pair6_cross(D):
    xt = D['xt']; a0, a1 = xt[24], xt[25]
    return (a0, a1) if (xt[26], xt[27]) == (a1, a0) and a0 != a1 and min(a0, a1) >= 0 and not {a0, a1} & {12, 13} else None
def windows(S, O, j):
    T = len(S) - 1; b = [t for t in range(1, T + 1) if O[t][j-1] != O[t-1][j-1]]; cuts = [1] + b + [T + 1]
    return [(a, e - 1, tuple((x, S[a][x]) for x in (2*j-2, 2*j-1) if a > 1 and S[a][x] != S[a-1][x])) for a, e in zip(cuts, cuts[1:])]
def _merged(D, s, A0, A1):
    m0 = {x for _, _, x, _ in chain(D, s, A0, s[A0])}; m1 = {x for _, _, x, _ in chain(D, s, A1, s[A1])}
    return A0 in m1 or A1 in m0
def _count(D, S, O, only91):
    c = pair6_cross(D)
    if c is None: return None
    A0, A1 = c; W5 = windows(S, O, 5); n = 0
    for a, e, typ in windows(S, O, 6):
        if only91:
            par = [ty for (aa, ee, ty) in W5 if aa <= a <= ee]
            if not par or par[0] != ((9, 1),): continue
        n += sum(_merged(D, S[t], A0, A1) for t in range(a - 1, e))
    return n
def merge_count(D, S, O): return _count(D, S, O, False)
def merge91_count(D, S, O): return _count(D, S, O, True)
def pulse5_91(D, S, O):
    p = []
    for a, e, typ in windows(S, O, 5):
        if typ != ((9, 1),): continue
        mv = [t for t in range(a, e + 1) for x in (10, 11) if S[t][x] != S[t-1][x]]
        if len(mv) == 2: p.append(mv[1] - mv[0])
    return min(p) if p else None
def guard(D, mode='either'):
    S, O = run(D)
    if S is None: return False, {'cyclic': True}
    m91 = merge91_count(D, S, O); p = pulse5_91(D, S, O); F = Fprof(D, O)
    info = {'caps': caps(F), 'F6': F[6], 'merge_all': merge_count(D, S, O), 'merge91': m91, 'pulse5_91_min': p}
    nm = m91 == 0; p3 = p is not None and p >= 3
    ok = nm if mode == 'nomerge91' else p3 if mode == 'pulse3' else (nm or p3)
    return ok, info
if __name__ == '__main__':
    D = rd(sys.argv[1]); mode = sys.argv[2] if len(sys.argv) > 2 else 'either'
    ok, info = guard(D, mode); print(sys.argv[1], 'mode', mode, 'ok', ok, info)
