#!/usr/bin/env python3
"""REFEREE-2 succ. 31: every «…» quote of P-TOWER-FUEL §1 (and L-1's premise words) against trunk docs/RESULTS.md, byte for byte.
Usage: r2quotes.py PACKET.md RESULTS.md"""
import sys, re
P = open(sys.argv[1], encoding='utf-8').read(); R = open(sys.argv[2], encoding='utf-8').read()
def entry(tag):
    i = R.index('### ' + tag + ' '); j = R.find('\n### ', i + 1); return R[i:j if j > 0 else len(R)]
sec1 = P[P.index('## 1.'):P.index('## 2.')]
src = {'R105': entry('R105'), 'R113': entry('R113')}
for q in re.findall(r'«(.*?)»', sec1, re.S):
    q1 = ' '.join(q.split())
    parts = [p.strip() for p in q1.split('…')]
    for name, E in src.items():
        E1 = ' '.join(E.split()); pos = 0; ok = True
        for p in parts:
            k = E1.find(p, pos)
            if k < 0: ok = False; break
            pos = k + len(p)
        if ok: print('QUOTE OK in', name, ':', q1[:90], '...' if len(q1) > 90 else ''); break
    else: print('QUOTE NOT FOUND:', q1)
# definitional phrases the packet restates (not quoted)
for name, s in [('R110', 'option k of a mover of level l ≥ 1 W-pointing to mover 2(l − 1) + k'),
                ('R110', 'movers 2l and 2l + 1 on level l, all of degree 2, no other movers'),
                ('R113', 'c_l(s) the option index k for which mover 2(l − 1) + k has the smaller current key under s'),
                ('R113', 'γ_l(j) := [g(2l, j) < g(2l + 1, j)] with g(x, k) the gate index of option (x, k)'),
                ('R113', 'on 𝓛^R_d F(l) the number of steps at which the pair (2l, 2l + 1) flips'),
                ('R113', 'a flip of (u, w) at step t a change between s_(t−1) and s_t of the order of the keys of their current options'),
                ('R113', 'cv_s(z) the integer value of z\'s current option (R105 ENC)'),
                ('R113', 'on acyclic Ξ-graphs'), ('R105', 'at any degree: (ENC)'), ('R104', 'and the run stops when nothing is available or nothing changes')]:
    print(name, 'phrase', 'OK' if s in entry(name) else 'MISSING', ':', s)
