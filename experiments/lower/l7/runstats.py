#!/usr/bin/env python3
"""L-LOWER 7 (BOX L7), §1-§2: per genome (text format, l6/sim6.py): T, caps, F(6); guard data (does closure(q5) meet levels >= 6);
6-windows of length 1 and the WINDOW-CAP bound 2·#6-windows − #length-1; 5-windows split into INNER (no move of pairs 0-4 strictly
inside) / OUTER and by PULSE_5 = 1 / ≥ 2, and for PULSE_5 ≥ 2 the levels of the closure(q5) movers that move at step u2 − 1
(PULSE-TRIGGER). q5 = the member of pair 5 moving second (checked per window). Usage: runstats.py GENOME.txt ..."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
from sim6 import rd, run, Fprof, caps
from collections import Counter
def clos(D, x):
    xt = D['xt']; seen = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            y = xt[2 * z + k]
            if y >= 0 and y not in seen: seen.add(y); st.append(y)
    return seen
for p in sys.argv[1:]:
    D = rd(p); S, O = run(D); F = Fprof(D, O); T = len(S) - 1
    mv5 = [t for t in range(1, T + 1) if S[t][10:12] != S[t - 1][10:12]]
    w6 = list(zip([1] + mv5, mv5 + [T + 1])); L1 = sum(1 for a, b in w6 if b - a == 1)
    k4 = [t for t in range(1, T + 1) if O[t][4] != O[t - 1][4]]
    c = Counter(); trig = Counter(); qs = Counter()
    for a, b in zip([1] + k4, k4 + [T + 1]):
        inner = not any(S[t][x] != S[t - 1][x] for t in range(a + 1, b) for x in range(10))
        ms = [(t, x) for t in range(a, b) for x in (10, 11) if S[t][x] != S[t - 1][x]]
        if len(ms) != 2 or ms[0][0] == ms[1][0]: c['other'] += 1; continue
        (u1, f), (u2, q) = ms; qs[q] += 1; kind = 'inner' if inner else 'outer'
        if u2 - u1 == 1: c[(kind, 'PULSE1')] += 1; continue
        who = sorted(y // 2 for y in clos(D, q) if S[u2 - 1][y] != S[u2 - 2][y])
        hi = [l for l in who if l >= 6]; lo = [l for l in who if l <= 4]
        c[(kind, 'PULSE>=2', 'trigger level>=6' if hi else ('lower-only' if lo else 'NONE'))] += 1
        trig['min trigger level %d' % min(hi)] += 1 if hi else 0
    print(os.path.basename(p), '| T', T, 'caps', caps(F), 'F(6)', F[6], '| closure(q5=10) meets levels >= 6:', any(y >= 12 for y in clos(D, 10)),
          '| q5 movers', dict(qs))
    print('   6-windows', len(w6), 'of length 1:', L1, '-> WINDOW-CAP bound', 2 * len(w6) - L1)
    print('   5-windows:', dict(sorted(c.items(), key=str)), '| PULSE>=2 windows by lowest trigger level:', dict(sorted(trig.items())))
