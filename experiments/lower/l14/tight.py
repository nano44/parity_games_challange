#!/usr/bin/env python3
"""L-LOWER 14: tight required changes (consecutive free pre-states c-1, c with different required values; l13/reqpref.py) of the
movers 8, 11, 12, 13 on core8 rows 0..18, and which of them are core-timed (a core mover of closure(x) moves at step c).
Usage: tight.py GENOME [GENOME ...]   (run from experiments/lower)"""
import sys, subprocess, ast, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l12'))
import enc32_lcomp as e
tp = os.path.join(here, '..', 'l10', 'out', 'core8_HIT7.txt')
T = open(tp).read().split(); S = [T[2 + i] for i in range(int(T[0]))]
mv = lambda u: [x for x in range(16) if S[u][x] != S[u - 1][x]]
def clo(xt, x):
    s = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            w = xt[2 * z + k]
            if w >= 0 and w not in s: s.add(w); st.append(w)
    return s
tot = ct = 0
for g in sys.argv[1:]:
    xt = e.rdgen(g)['xt']
    for x in (8, 11, 12, 13):
        l = subprocess.run([sys.executable, os.path.join(here, '..', 'l13', 'reqpref.py'), g, tp, str(x), '18'], capture_output=True, text=True).stdout
        sq = ast.literal_eval(l[l.index('['):l.index('] |') + 1])
        tight = [sq[k][0] for k in range(1, len(sq)) if sq[k][1] != sq[k - 1][1] and sq[k][0] == sq[k - 1][0] + 1]
        c = clo(xt, x); cts = [u for u in tight if [z for z in mv(u) if z in c]]
        tot += len(tight); ct += len(cts); print(os.path.basename(g), x, 'tight', tight, 'core-timed', cts)
print('total tight', tot, 'core-timed', ct)
