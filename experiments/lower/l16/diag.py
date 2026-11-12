#!/usr/bin/env python3
"""L-LOWER 16: hand-design diagnostic. Runs GENOME free (sim6) and reports the first row where the core (movers 0..15) leaves the
TARGET, and for each core mover that deviates there: its level, whether it was free at that step (key), its better value at the
pre-state, the target value, and its current closure (Xi-reach set). Usage: diag.py GENOME TARGET"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6'))
import sim6
D = sim6.rd(sys.argv[1]); L = open(sys.argv[2]).read().split(); S = [[int(c) for c in L[2 + i]] for i in range(int(L[0]))]
R, O = sim6.run(D, cap=4000); xt = D['xt']
def closure(x):
    out = set(); st = [x]
    while st:
        y = st.pop()
        for k in (0, 1):
            z = xt[2 * y + k]
            if z >= 0 and z not in out: out.add(z); st.append(z)
    return sorted(out)
t = 0
while t < len(R) and t < len(S) and list(R[t][:16]) == S[t]: t += 1
print('rows followed', t, '(run T %d)' % (len(R) - 1))
if t < len(S) and t >= 1:
    s = list(R[t - 1]); order = sim6.topo(D); v = sim6.values(D, s, order)
    for x in range(16):
        got = R[t][x] if t < len(R) else s[x]
        if got == S[t][x]: continue
        m = 2 * x + 1 - s[x]; y = xt[m]; ov = sim6.bv(D, m) + (v[y] if y >= 0 else 0); av = ov > v[x]
        l = x // 2; key = sim6.okeys(D, S[t] + list(R[t][16:]) if t < len(R) else s)[l - 1] if l else None
        print(' mover', x, 'level', l, 'pre', s[x], 'target', S[t][x], 'run', got, 'av(wants to flip)', av, 'key o(l-1) of target row', key, 'closure', closure(x))
