#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7) item (a): the I-FUEL decider count of P-TOWER-FUEL (p_tower_check.py's predicate) on any genome: per 6-window
[a, e], is option 19 = (mover 9, option 1) the deciding element dec_s(12) or dec_s(13) at some / the first / every pre-state
s_(a-1), …, s_(e-1)? Split by failing (not exactly one move of each of 12, 13) and good windows. Also prints option 19's rank and
the chains of 11:1 and 9:1 at the first failing pre-state. Usage: dom87.py GENOME.txt ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run, chain, dec
for p in sys.argv[1:]:
    D = rd(p); S, O = run(D); T = len(S) - 1
    mv5 = [t for t in range(1, T + 1) if S[t][10:12] != S[t - 1][10:12]]
    W = list(zip([1] + mv5, [t - 1 for t in mv5] + [T]))
    c = {'fail': [0, 0, 0, 0], 'good': [0, 0, 0, 0]}; first = None
    for a, e in W:
        mv = [(t, x) for t in range(a, e + 1) for x in (12, 13) if S[t][x] != S[t - 1][x]]
        ok = sorted(x for t, x in mv) == [12, 13]; k = 'good' if ok else 'fail'
        hit = [any(dec(D, S[t], x)[1:3] == (9, 1) for x in (12, 13)) for t in range(a - 1, e)]
        c[k][0] += 1; c[k][1] += any(hit); c[k][2] += hit[0]; c[k][3] += all(hit)
        if not ok and any(hit) and first is None: first = a - 1 + hit.index(True)
    print(os.path.basename(p), 'T', T, 'rank of option 19 (9:1):', D['br'][19], 'sign', '-' if D['bp'][19] else '+', '| 6-windows [count, (9,1) decides at some / first / every pre-state]:', c)
    if first is not None:
        s = S[first]; print('   first failing pre-state s_%d: chain 11:1 =' % first, [(r, x, k) for r, b, x, k in chain(D, s, 11, 1)][:6], '| chain 9:1 =', [(r, x, k) for r, b, x, k in chain(D, s, 9, 1)][:5])
