#!/usr/bin/env python3
"""L-SI box 51b §7 (Lead 14:09Z, «is S1 a known anti-stalling rule in disguise»): per W-constant interval I (W fixed, tau fixed, no
fallback; as const.py), REV := returns of an Even vertex v to an edge it held at an earlier state of I and left inside I. A FIXED-ORDER rule
(sigma_{k+1}(v) = the min of a fixed order <_v on the tight arena edges OPT(v) cap H_k(v); sigma_k(v) is always in H_k(v)) only moves down
<_v, so it has REV = 0 and at most |OPT(v)| - 1 switches of v per interval. BRANCH: parity of W's cycle node(s) in I (SPEC A5: original
odd cycle node -> longest path, ties to the smallest index; even -> BFS first discovery). Prints per interval: [p, q], flat, REV, max
switches of one vertex SWV, its |OPT(v)|, BRANCH. Usage: revisit.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
a = sys.argv[1:]; g = load(a[0]); n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, readstart(a[1]) if len(a) > 1 else None); s, t = tuple(s), tuple(t)
def W(s, t): return Engine(pg.Game(list(g.prio), list(own), [[t[v]] if own[v] == 1 else list(g.succ[v]) for v in range(n)])).evaluate(s)[0]
def opt(w, v): return [e for e in g.succ[v] if (E.extend(v, w[e]) == w[v] if w[v][0] != v else (w[e][0] == v and w[e][1] == 0))]
k = 0; I = [s]; w0 = W(s, t)
def flush():
    if len(I) < 2: return
    rev = 0; sw = {}
    for v in range(n):
        if own[v] != 0: continue
        held, left = {I[0][v]}, set()
        for j in range(1, len(I)):
            if I[j][v] != I[j - 1][v]:
                sw[v] = sw.get(v, 0) + 1; left.add(I[j - 1][v])
                if I[j][v] in left: rev += 1
    v = max(sw, key=sw.get)
    br = sorted({'odd' if g.prio[w0[x][0]] % 2 else 'even' for x in range(n)})
    print(f"REVISIT {os.path.basename(a[0])} interval [{k - len(I) + 1}, {k}] flat {len(I) - 1} REV {rev} SWV {sw[v]} OPT {len(opt(w0, v))} BRANCH {'/'.join(br)}")
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, _, _, fb, _, _ = r; ns, nt = tuple(ns), tuple(nt); k += 1
    w1 = W(ns, nt)
    if nt == t and not fb and [E.key(x) for x in w1] == [E.key(x) for x in w0]: I.append(ns)
    else: flush(); I = [ns]; w0 = w1
    s, t = ns, nt
flush()
