#!/usr/bin/env python3
"""Compose two copies of a core game: A (upper, ranks just above the sink) and B (lower = near the sink, ranks above A's).
A's edges into its TAIL vertices (A-vertices with rank >= TR) are redirected to MAP[t] in B; A's tail vertices are dropped (made
unreachable: they keep their edges but nothing points to them). A's sink edges go to B's sink. Priorities rebuilt with parity kept:
order low -> high: B below-sink, A below-sink, sink(B), A above-sink, B above-sink.
Usage: compose.py CORE START TR MAPSPEC OUT   (MAPSPEC: 't1:b1,t2:b2,...' vertex ids of the core; b = 'B'-copy vertex)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x, pg
from phclimb import save
core = n3x.load(sys.argv[1]); st = n3x.readstart(sys.argv[2]); TR = int(sys.argv[3]); out = sys.argv[5]
MAP = {int(a): int(b) for a, b in (x.split(":") for x in sys.argv[4].split(","))} if sys.argv[4] else {}
E = n3x.Engine(core); n = core.n; sink = [v for v in range(n) if core.succ[v] == [v]][0]
rs = E.rank[sink]
A = lambda v: v; B = lambda v: n + v
N = 2 * n; owner = [0] * N; succ = [None] * N; par = [0] * N
for v in range(n):
    for f in (A, B):
        owner[f(v)] = core.owner[v]; par[f(v)] = core.prio[v] % 2
for v in range(n):
    succ[B(v)] = [B(w) for w in core.succ[v]]
    ss = []
    for w in core.succ[v]:
        if w == sink: ss.append(B(sink))
        elif E.rank[w] >= TR and w in MAP: ss.append(B(MAP[w]))
        elif E.rank[w] >= TR: ss.append(B(w))
        else: ss.append(A(w))
    succ[A(v)] = sorted(set(ss))
succ[A(sink)] = [A(sink)]
key = lambda v: E.rank[v]
order = ([B(v) for v in sorted(range(n), key=key) if E.rank[v] < rs] + [A(v) for v in sorted(range(n), key=key) if E.rank[v] < rs] +
         [B(sink)] + [A(v) for v in sorted(range(n), key=key) if E.rank[v] > rs] + [B(v) for v in sorted(range(n), key=key) if E.rank[v] > rs] + [A(sink)])
prio = [0] * N; p = -1
for v in order:
    p += 1
    if p % 2 != par[v]: p += 1
    prio[v] = p
g = pg.Game(prio, owner, succ)
def img(v, w):
    if w == sink: return B(sink)
    if E.rank[w] >= TR: return B(MAP.get(w, w))
    return A(w)
s0 = {}; t0 = {}
for v, w in st[0].items(): s0[B(v)] = B(w); s0[A(v)] = img(v, w)
for v, w in st[1].items(): t0[B(v)] = B(w); t0[A(v)] = img(v, w)
save(g, (s0, t0), out)
