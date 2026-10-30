#!/usr/bin/env python3
"""L-SI box 51b §8: the BFS-layer reset test. Per W-constant interval I (as revisit.py), layer(v) := the length of W(v) (fixed on I).
A RETURN of Even v at transition k2: sigma_{k2+1}(v) = e != sigma_{k2}(v), and v left e at an earlier transition k1 of I (the latest
such k1). RET: all returns; RETL2: returns of vertices with layer <= 2; UNX: returns with no switch of another Even vertex of layer(v) - 1
at a transition in (k1, k2]. CONJECTURE LAYER-RESET: UNX = 0. DEPTH: largest layer of a switched vertex. Control MUT=1: ask for the
switch at layer(v) - 2 instead (it must give UNX > 0 somewhere).
Usage: layer.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
OFF = 2 if os.environ.get('MUT') == '1' else 1
a = sys.argv[1:]; g = load(a[0]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, readstart(a[1]) if len(a) > 1 else None); s, t = tuple(s), tuple(t)
def W(s, t): return Engine(pg.Game(list(g.prio), list(own), [[t[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)])).evaluate(s)[0]
c = dict(RET=0, UNX=0, RETL2=0, DEPTH=0, FLAT=0)
k = 0; I = [s]; w0 = W(s, t)
def flush():
    if len(I) < 2: return
    c['FLAT'] += len(I) - 1
    L = [w0[v][2] for v in range(n)]
    sw = [[v for v in range(n) if own[v] == 0 and I[j + 1][v] != I[j][v]] for j in range(len(I) - 1)]
    c['DEPTH'] = max([c['DEPTH']] + [L[v] for x in sw for v in x])
    for v in range(n):
        if own[v] != 0: continue
        lastleave = {}
        for j in range(len(I) - 1):
            if I[j + 1][v] == I[j][v]: continue
            e = I[j + 1][v]
            if e in lastleave:
                c['RET'] += 1; c['RETL2'] += L[v] <= 2
                if not any(L[u] == L[v] - OFF for jj in range(lastleave[e] + 1, j) for u in sw[jj]) and not any(L[u] == L[v] - OFF for u in sw[j] if u != v):
                    c['UNX'] += 1
            lastleave[I[j][v]] = j
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt); k += 1
    w1 = W(ns, nt)
    if nt == t and not fb and [E.key(x) for x in w1] == [E.key(x) for x in w0]: I.append(ns)
    else: flush(); I = [ns]; w0 = w1
    s, t = ns, nt
flush()
print(f"LAYER {os.path.basename(a[0])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
