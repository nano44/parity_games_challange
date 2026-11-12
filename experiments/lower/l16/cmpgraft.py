#!/usr/bin/env python3
"""L-LOWER 16: run a grafted genome with the core (movers 0..15) clamped to the target (l7/clamp.runclamp) and print the states of
the cascade movers 16..15+2K per row, next to the stand-alone cascade run (l15 rules, o(7)(S_t) = t mod 2). Usage: cmpgraft.py GENOME CASCADE TARGET P"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(here, '..', 'l6')); sys.path.insert(0, os.path.join(here, '..', 'l7'))
import sim6, clamp
D = sim6.rd(sys.argv[1]); C = {}
for ln in open(sys.argv[2]):
    w = ln.split(); C[w[0]] = w[1:]
K = int(C['k'][0]); P = int(sys.argv[4])
T = open(sys.argv[3]).read().split(); tg = [[int(c) for c in T[2 + i]] for i in range(P + 1)]
tgt = [r + (D['start'][16:] if t == 0 else [0] * 48) for t, r in enumerate(tg)]
S = clamp.runclamp(D, tgt, set(range(16)))
# stand-alone
xt = list(map(int, C['xt'])); rank = list(map(int, C['rank'])); even = list(map(int, C['even'])); gate = list(map(int, C['gate'])); s = [int(c) for c in C['start'][0]]
H = 2 * K; eps = [(1 if even[a] else -1) * 2 ** rank[a] for a in range(2 * H)]
def value(op, s):
    v = 0
    while True:
        v += eps[op]; z = xt[op]
        if z < 0: return v
        op = 2 * z + s[z]
A = [tuple(s)]
for t in range(P):
    bet = [1 if value(2 * y + 1, s) > value(2 * y, s) else 0 for y in range(H)]
    ns = list(s); c = (t + 1) % 2
    for i in range(K):
        for y in (2 * i, 2 * i + 1):
            if bet[y] != s[y] and s[y] != c: ns[y] = c
        a, b = ns[2 * i], ns[2 * i + 1]; c = (a ^ c) if a != b else gate[2 * i + a]
    s = ns; A.append(tuple(s))
bad = 0
for t in range(P + 1):
    g = ''.join(map(str, S[t][16:16 + H])); a = ''.join(map(str, A[t]))
    bad += g != a; print(t, g, a, '' if g == a else 'DIFF')
print('CMPGRAFT rows 0..%d' % P, 'mismatches', bad)
