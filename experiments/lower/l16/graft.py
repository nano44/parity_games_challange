#!/usr/bin/env python3
"""L-LOWER 16 (BOX L16, design D1): graft a decoded private cascade (l15 ekr.py format: k / xt / rank / even / gate / start) onto a
d-32 genome at helper levels 8..7+k (movers 16..15+2k). Cascade-local mover i -> genome mover 16+i; xt -1 stays exit. Ranks: the
cascade's 4k options take the SAME set of br values the replaced options had, re-assigned in the cascade's relative rank order (br
stays a permutation). Signs bp = 1 - even (bp 1 = negative). Gates of levels 8..7+k: joined value given by the cascade's gate bit
g(i, a) (o = 1 iff gate[4l+a] > gate[4l+2+a]); the existing two numbers are re-ordered to give it. Starts of movers 16..15+2k from
the cascade. Usage: graft.py GENOME CASCADE OUT"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l6'))
import sim6
D = sim6.rd(sys.argv[1]); C = {}
for ln in open(sys.argv[2]):
    w = ln.split(); C[w[0]] = w[1:]
K = int(C['k'][0]); xt = list(map(int, C['xt'])); rk = list(map(int, C['rank'])); ev = list(map(int, C['even']))
gt = list(map(int, C['gate'])); st = [int(c) for c in C['start'][0]]
base = 32  # first option of mover 16
opts = list(range(base, base + 4 * K))
vals = sorted(D['br'][m] for m in opts)
for j, m in enumerate(opts):
    D['xt'][m] = (16 + xt[j]) if xt[j] >= 0 else -1
    D['br'][m] = vals[rk[j]]
    D['bp'][m] = 0 if ev[j] else 1
for i in range(K):
    l = 8 + i
    for a in (0, 1):
        x, y = D['gate'][4 * l + a], D['gate'][4 * l + 2 + a]
        hi, lo = max(x, y), min(x, y)
        if gt[2 * i + a]: D['gate'][4 * l + a], D['gate'][4 * l + 2 + a] = hi, lo
        else: D['gate'][4 * l + a], D['gate'][4 * l + 2 + a] = lo, hi
for i in range(2 * K): D['start'][16 + i] = st[i]
assert sim6.topo(D) is not None, 'cyclic after graft'
sim6.wr(D, sys.argv[3]); print('GRAFT', sys.argv[2], '->', sys.argv[3], 'K', K)
