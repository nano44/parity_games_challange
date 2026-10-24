#!/usr/bin/env python3
"""L-SI box 1 (N5 through the OR lens): per-state trace of an N5 run (SPEC S1-S5, same loop as experiments/new/n5.py, which is
imported read-only for dual() and checked against n5.run's iteration/fallback counts) plus the gap-level / action-elimination
measures of docs/si/N5-OR-lens.md.
Valuation = (cycle node, path bitmask over ranks, length) as in experiments/si/si.py.
lev(a, b): ultrametric level of the first difference: -1 equal, 0 length only, 1 + r top rank r of the path-set difference,
n + 1 different cycle nodes.  Joint lambda-phase = maximal run of states with the same honest cycle-node map on G and on G^d.
Target T of a phase = honest valuation Xi at the LAST state of the phase.  g_k(v) = lev(T(v), Xi_k(v))."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..")); sys.path.insert(0, os.path.join(HERE, "..", "..", "harness"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "new"))
import pg
from si import Engine
import n5 as N5

def load(path, startpath=None):
    g = pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    st = None
    if startpath and os.path.exists(startpath):
        lines = [l.strip() for l in open(startpath) if l.strip()]
        st = tuple(dict(map(int, t.split(":")) for t in lines[j].split()[1:]) for j in (0, 1))
    return g, st

def run_states(g, start=None, cap=10 ** 5, mode="n5"):
    """mode n5: same loop as n5.run; mode switchall: classical switch-all SI for Even (CONTROL; tau unused). Returns list of states (sigma, tau, vs, sbar, vt, tbar, Is, It) and (it, fb)."""
    n = g.n
    E, Ed = Engine(g), Engine(N5.dual(g))
    sigma, tau = list(E.initial("best")), list(Ed.initial("best"))
    if start:
        for v, w in start[0].items(): sigma[v] = w
        for v, w in start[1].items(): tau[v] = w
    it = fb = 0; states = []; fbflag = []
    while it < cap:
        vs, sbar = E.evaluate(tuple(sigma)); Is = E.improving(tuple(sigma), vs)
        vt, tbar = Ed.evaluate(tuple(tau)); It = Ed.improving(tuple(tau), vt)
        states.append((tuple(sigma), tuple(tau), vs, sbar, vt, tbar, Is, It))
        if not Is and not It: break
        if mode == "switchall":
            if not Is: break
            it += 1
            for v in {v for v, _ in Is}: sigma[v] = E.best_succ(v, vs, [w for x, w in Is if x == v])
            fbflag.append(0); continue
        it += 1
        ns, nt = list(sigma), list(tau)
        if Is:
            opt = {v: {sigma[v]} for v in range(n) if g.owner[v] == 0}
            for v, w in Is: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
            Er = Engine(N5.dual(pg.Game(list(g.prio), list(g.owner), succ)))
            _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 0: ns[v] = best[v]
        if It:
            opt = {v: {tau[v]} for v in range(n) if g.owner[v] == 1}
            for v, w in It: opt[v].add(w)
            succ = [sorted(opt[v]) if g.owner[v] == 1 else [sigma[v]] for v in range(n)]
            Er = Engine(pg.Game(list(g.prio), list(g.owner), succ))
            _, best = Er.evaluate(tuple(sigma[v] if g.owner[v] == 0 else -1 for v in range(n)))
            for v in range(n):
                if g.owner[v] == 1: nt[v] = best[v]
        f = 0
        if ns == sigma and nt == tau:
            fb += 1; f = 1
            if Is:
                for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (E.key(vs[w]), w))
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        fbflag.append(f)
        sigma, tau = ns, nt
    return E, Ed, states, fbflag, (it, fb)

class Lex:
    def __init__(self, E):
        self.E = E; self.n = E.n
    def lev(self, a, b):
        if a[0] != b[0]: return self.n + 1
        if a[1] != b[1]: return 1 + ((a[1] ^ b[1]).bit_length() - 1)
        if a[2] != b[2]: return 0
        return -1
    def pre(self, x, a):
        E = self.E
        c, P, l = a
        if E.rank[x] > E.rank[c]: P = P | E.bit[x]
        return (c, P, l + 1)
    def le(self, a, b):   # a <= b in Even's order
        return self.E.key(a) <= self.E.key(b)

def phases(E, Ed, states):
    """joint lambda-phases as lists of state indices"""
    out = []; cur = []; last = None
    for k, st in enumerate(states):
        lam = (tuple(v[0] for v in st[2]), tuple(v[0] for v in st[4]))
        if lam != last and cur: out.append(cur); cur = []
        cur.append(k); last = lam
    if cur: out.append(cur)
    return out
