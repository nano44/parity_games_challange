#!/usr/bin/env python3
"""L-LOWER 10 (item 2): the level-8 target at d 32 and the exact clamp + ranksolve test.
core8(D28, H=8): the stretched core target of pairs 0..6 (stmap.target) with ONE idle step prepended and the last tail step cut,
so o(6) changes at 3, 5, ..., 509 and T = 510; plus pair 7: f7 = 15 moves to c7 = o(6) at the first step of every 7-window
(step 1 for the first window), q7 = 14 at the second step. Start of pair 7: joined at 1 - c7(0).
test(D, CT): helpers (movers >= 16) follow D's rules with movers 0..15 clamped to CT (l7/clamp.runclamp); the full trajectory's
constraints (l7/ranksolve.constraints) are solved for ranks/signs; returns (feasible, genome or core)."""
import sys, os
from collections import Counter
here = os.path.dirname(os.path.abspath(__file__))
for p in ('.', '../l6', '../l7'): sys.path.insert(0, os.path.join(here, p))
from sim6 import rd, wr, run, Fprof, caps, okeys
from stmap import target
from clamp import runclamp
from ranksolve import constraints, solve
def core8(D28, H=8):
    Sc, Oc, idle = target(D28, H)
    Sc = [Sc[0]] + Sc[:-1]; Oc = [Oc[0]] + Oc[:-1]; T = len(Sc) - 1
    c7 = [o[6] for o in Oc]; out = []; f = q = 1 - c7[0]; last = 0
    pend = None
    for t in range(T + 1):
        if t >= 1:
            if t == 1 or c7[t] != c7[t - 1]:
                f = c7[t]; pend = t + 1
            elif pend == t:
                q = c7[t]; pend = None
        out.append(tuple(Sc[t]) + (q, f))
    return out
def fixgates(D):
    g = list(D['gate']); g[28:32] = [1028, 1029, 1030, 1031]; E = dict(D); E['gate'] = g; return E
def fulltraj(D, CT):
    tg = [list(CT[t]) + [None] * (2 * D['d'] - 16) for t in range(len(CT))]
    for x in range(16, 2 * D['d']): tg[0][x] = D['start'][x]
    st = list(tg[0]); E = dict(D); E['start'] = st
    return runclamp(E, [tuple(r) for r in tg], set(range(16))), E
def test(D, CT):
    S, E = fulltraj(D, CT); cons = constraints(E, S); res, core = solve(cons, 4 * E['d'])
    if res is None: return False, core, S, E
    G = dict(E); G['br'], G['bp'] = res; return True, G, S, E
if __name__ == '__main__':
    D28 = rd(sys.argv[1]); D = fixgates(rd(sys.argv[2])); CT = core8(D28)
    O = [okeys(D, s + (0,) * (2 * D['d'] - 16)) for s in CT]
    print('target T', len(CT) - 1, 'F(0..7)', [sum(1 for t in range(1, len(O)) if O[t][l] != O[t - 1][l]) for l in range(8)])
    ok, r, S, E = test(D, CT)
    if ok:
        S2, O2 = run(r); print('FEASIBLE; rebuilt run T', len(S2) - 1, 'caps', caps(Fprof(r, O2)), 'F', Fprof(r, O2))
        if len(sys.argv) > 3: wr(r, sys.argv[3])
    else:
        C = Counter(x for t, x, p in r); print('INFEASIBLE core', len(r), 'by mover', sorted(C.items())[:40])
