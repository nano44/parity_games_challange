#!/usr/bin/env python3
"""L-SI box 20 (successor 16): shared helpers for the root probes (note §29). Read-only use of experiments/new/box21/n5x.py and si.py.
rows(g, start): the N5 run as a list of states with Xi (vs), sigma-bar (sb), sigma (s), tau (t), the honest successor map (nxt), the
W-valuation of the (sigma, tau)-play (W, computed by wplay), and the fallback flag of the transition LEAVING the state (fb).
phases(rows): maximal runs [i, j] with lambda_Xi and tau constant (RESULTS R38 (a) KEY)."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import step, start_pair, Engine, dual, load, readstart

def wplay(E, g, s, t):
    """VJ00 valuation (cycle node, path mask, length) of the (s, t)-play from every vertex: follow the play to its cycle; cycle node =
    the vertex of largest rank on the cycle; P = vertices strictly before the cycle node with rank > its rank; length = steps to it."""
    n = g.n; nx = [s[v] if g.owner[v] == 0 else t[v] for v in range(n)]; val = [None] * n
    for v in range(n):
        if val[v] is not None: continue
        path, pos, x = [], {}, v
        while x not in pos and val[x] is None: pos[x] = len(path); path.append(x); x = nx[x]
        if val[x] is None:                      # new cycle: path[pos[x]:]
            cyc = path[pos[x]:]; w = max(cyc, key=lambda u: E.rank[u]); val[w] = (w, 0, 0)
            i = cyc.index(w)
            for k in range(1, len(cyc)):        # walk the cycle backwards from w
                u = cyc[(i - k) % len(cyc)]; val[u] = E.extend(u, val[nx[u]])
            path = path[:pos[x]]
        for u in reversed(path): val[u] = E.extend(u, val[nx[u]])
    return val, nx

def rows(g, start=None, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); out = []
    while len(out) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        W, wn = wplay(E, g, s, t)
        out.append(dict(vs=vs, sb=list(sb), s=list(s), t=list(t), nxt=nxt, W=W, wn=wn, fb=(r[4] if r else 0),
                        key=(tuple(x[0] for x in vs), tuple(t))))
        if r is None: break
        s, t = list(r[0]), list(r[1])
    return E, out

def phases(R):
    i = 0
    while i < len(R):
        j = i
        while j + 1 < len(R) and R[j + 1]["key"] == R[i]["key"]: j += 1
        if j > i: yield i, j
        i = j + 1

def Dset(g, A):
    return {u for u in range(g.n) if g.owner[u] == 1 and A["sb"][u] != A["t"][u]}

def avoid(nx, D, n):
    """the vertices whose play under the successor map nx never meets D (start vertex included)."""
    res = [None] * n
    for v in range(n):
        path, x, seen = [], v, set()
        while res[x] is None and x not in seen and x not in D: seen.add(x); path.append(x); x = nx[x]
        ok = res[x] if res[x] is not None else (x not in D)
        for u in path: res[u] = ok
    return {v for v in range(n) if res[v]}

def wt(E, v, c):
    return ((1 << E.rank[v]) if E.par[v] == 0 else -(1 << E.rank[v])) if E.rank[v] > E.rank[c] else 0

def M(E, val):
    return E.weight(val[1])

def first_D(nx, z, D):
    """the first vertex of D on z's play under nx (z included), or None."""
    x, seen = z, set()
    while x not in seen and x not in D: seen.add(x); x = nx[x]
    return x if x in D else None
