#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) §4: the ideal pair 6 on SL41's wiring. (i) sanity: clamping SL41's movers 0-13 to SL41's own run reproduces it and
is feasible; (ii) target = SL41's pairs 0-5 + ideal pair 6 (clamp.ideal6, first mover 13 at t0 + a, second 12 at t0 + a + b), all
other movers completed by their own rules (clamp.runclamp); report the target F-profile, the movers whose trajectory changes, global
feasibility (ranksolve, all ranks free, SL41's wiring) and the movers whose OWN constraint set is infeasible. Usage: ideal.py SL41_d28.txt"""
import sys, os
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, '..', 'l6')); sys.path.insert(0, H)
from sim6 import rd, run, okeys
from clamp import runclamp, ideal6
from ranksolve import constraints, solve
from collections import defaultdict
D = rd(sys.argv[1]); S, O = run(D); M = set(range(14))
full = runclamp(D, S, M); print('(i) clamp to own run reproduces it:', full == S, '; feasible:', solve(constraints(D, full), 4 * D['d'])[0] is not None)
for a, b in ((0, 1), (1, 1), (0, 2)):
    tg = ideal6(D, S, a, b); full = runclamp(D, tg, M)
    O2 = [okeys(D, s) for s in full]; F = [sum(1 for t in range(1, len(O2)) if O2[t][l] != O2[t - 1][l]) for l in range(8)]
    ch = sorted({x for t in range(len(S)) for x in range(len(S[0])) if full[t][x] != S[t][x]})
    cons = constraints(D, full); res, core = solve(cons, 4 * D['d']); by = defaultdict(list)
    for c in cons: by[c[1]].append(c)
    own = [x for x in sorted(by) if solve(by[x], 4 * D['d'])[0] is None]
    print('(ii) a', a, 'b', b, '| target F[0:8]', F, '| movers with changed trajectory:', len(ch), '(levels', sorted({x // 2 for x in ch}), ')',
          '| feasible on SL41 wiring:', res is not None, '| movers whose own constraints are infeasible:', own)
