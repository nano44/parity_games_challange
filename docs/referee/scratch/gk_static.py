#!/usr/bin/env python3
"""REFEREE successor 35: per-mover switch counts sw(x) of the IDEAL run on G_k, by mover name; which movers never move.
usage: gk_static.py kmin kmax"""
import sys
import gk_build as B
import gk_ideal as I
for k in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
    G = B.genome(k); nm = G['names']
    L, why, S = I.run(G, keep=True)
    sw = {nm[x]: sum(1 for j in range(1, L + 1) if S[j][x] != S[j - 1][x]) for x in range(G['N'])}
    first = {nm[x]: next((j for j in range(1, L + 1) if S[j][x] != S[j - 1][x]), None) for x in range(G['N'])}
    wires = sorted(n for n in sw if n.startswith('w'))
    print('G_%d L %d | wires that move: %d of %d | sw(u0) %d sw(v0) %d (first move of v0 at step %s)' % (k, L, sum(1 for n in wires if sw[n]), len(wires), sw['u0'], sw['v0'], first['v0']))
    for t in ('u', 'v', 'e', 'y', 'yb', 'yp', 'ypb'):
        print('   sw(%s_j): %s' % (t, ' '.join('%s=%d' % (j, sw[t + str(j)]) for j in range(0, k) if (t + str(j)) in sw)))
