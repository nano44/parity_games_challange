#!/usr/bin/env python3
"""L-LOWER 14: check Lemma CAUSE / KEY-DELAY (L14 §2) on a genome's free run (sim6, R104 degree 2).
For every move of a mover y of level L >= 1 at step u (S_(u-1) -> S_u), let a = the least row such that y's state is constant and
av_y (the other option strictly better) holds on all rows a..u-1. Lemma CAUSE: (i) if a >= 1, some mover of closure(y) moves at step a
(the av switch); (ii) if a <= u-3 and L >= 9 and o(7) alternates on rows u-2, u-1, u, some mover of pairs 8..L-1 moves at step u-1
or u (KEY-DELAY); (iii) if a <= u-3 and L = 8 with o(7) alternating there: impossible. Prints counts and every violation.
Usage: cause.py GENOME"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6'))
from sim6 import rd, run, okeys, topo, bv
D = rd(sys.argv[1]); d = D['d']; N = 2 * d; xt = D['xt']
S, O = run(D); T = len(S) - 1; order = topo(D)
def clo(x):
    s = set(); st = [x]
    while st:
        z = st.pop()
        for k in (0, 1):
            w = xt[2 * z + k]
            if w >= 0 and w not in s: s.add(w); st.append(w)
    return s
C = [clo(x) for x in range(N)]
def avs(s):
    v = {}
    for x in order:
        m = 2 * x + s[x]; y = xt[m]; v[x] = bv(D, m) + (v[y] if y >= 0 else 0)
    out = []
    for x in range(N):
        m = 2 * x + 1 - s[x]; y = xt[m]; out.append(bv(D, m) + (v[y] if y >= 0 else 0) > v[x])
    return out
AV = [avs(S[t]) for t in range(T + 1)]
mv = lambda u: [x for x in range(N) if S[u][x] != S[u - 1][x]]
MV = [None] + [set(mv(u)) for u in range(1, T + 1)]
cnt = {'moves': 0, 'i': 0, 'ii': 0, 'iii_or_other': 0, 'start': 0}; bad = []
for u in range(1, T + 1):
    for y in MV[u]:
        L = y // 2
        if L == 0: continue
        cnt['moves'] += 1
        a = u - 1
        while a - 1 >= 0 and AV[a - 1][y] and S[a - 1][y] == S[u - 1][y]: a -= 1
        if a >= 1:
            if not (C[y] & MV[a]): bad.append(('i', y, u, a))
            else: cnt['i'] += 1
        else: cnt['start'] += 1
        if a <= u - 3:
            alt = O[u - 2][7] != O[u - 1][7] != O[u][7]
            if L >= 9 and alt:
                if not any(z // 2 in range(8, L) for z in MV[u - 1] | MV[u]): bad.append(('ii', y, u, a))
                else: cnt['ii'] += 1
            elif L == 8 and alt: bad.append(('iii', y, u, a))
            else: cnt['iii_or_other'] += 1
print('genome', os.path.basename(sys.argv[1]), 'T', T, cnt, 'violations', len(bad), bad[:10])
