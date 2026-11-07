#!/usr/bin/env python3
"""box 80 DATA: delay lines. For a genome (stored start) and a doubling level j: in every j-window, the second mover x2 of the pair j,
the pulse, and the backward trigger chain x2 <- y1 <- y2 ... where y_(i+1) is a mover on y_i's option chains (under the state before
the step) that moved at the step at which pi(y_i) last became y_i's next target option, followed while it is unique, stopping at a mover
of the pairs 0..j-1 or after 8 links. Usage: delay80.py genome.json j"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'box76'))
import collections
from sim80 import Sim, stats, keyorder
from check80 import windows
def chain(sim, st, x, k):
    out = []; y = sim.xt[x][k]
    while y >= 0: out.append(y); y = sim.xt[y][st[y]]
    return out
G = json.load(open(sys.argv[1])); j = int(sys.argv[2]); sim = Sim(G); S = sim.run(); T = len(S) - 1
c = [sim.cv(s) for s in S]
P = [[0 if sim.v(c[t], x, 0) > sim.v(c[t], x, 1) else 1 for x in range(sim.N)] for t in range(T + 1)]
F, dbl, W = windows(sim, S)
def trig(x, u):
    """x moves at step u; return (v, sources): v the step at which pi(x) last became S[u][x]"""
    cc = S[u][x]; v = u - 1
    while v >= 1 and P[v - 1][x] == cc: v -= 1
    if v < 1: return v, []
    src = sorted({y for k in range(2) for y in chain(sim, S[v - 1], x, k) if S[v][y] != S[v - 1][y]})
    return v, src
pat = collections.Counter()
for (a, e, m) in W[j]:
    u1, u2 = m; x2 = [x for x in (2 * j, 2 * j + 1) if S[u2][x] != S[u2 - 1][x]][0]
    line = [x2]; x, u = x2, u2
    for _ in range(8):
        v, src = trig(x, u)
        if len(src) != 1: line.append("?" + ",".join(map(str, src))); break
        y = src[0]; line.append(y); x, u = y, v
        if y < 2 * j: break
    key = (x2, u2 - u1, tuple(line)); pat[key] += 1
for (x2, pl, line), n in sorted(pat.items(), key=lambda kv: -kv[1]):
    print("x2 %d pulse %d line %s : %d windows" % (x2, pl, " <- ".join(map(str, line)), n))
