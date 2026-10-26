#!/usr/bin/env python3
"""REFEREE successor 8: an own N5 engine, written from the SPEC text (docs/new/N5-ssi-global.md S1-S5, FIX 1-4, Q1-Q4) only.
No lane code is imported (no si.py, n5.py, pg.py). Values are triples (c, mask, d): c = cycle node, mask = path set as a bitmask
over RANKS, d = steps to reach c. key() is the Even order of S1. Used by rl_probe.py (packet P-N5-RL)."""
from collections import deque


class Game:
    def __init__(self, prio, owner, succ):
        self.n = len(prio); self.prio = list(prio); self.owner = list(owner); self.succ = [sorted(set(s)) for s in succ]
        order = sorted(range(self.n), key=lambda v: (self.prio[v], v))
        self.rank = [0] * self.n
        for i, v in enumerate(order): self.rank[v] = i
        self.byrank = order
        self.pp = [2 * self.rank[v] + (self.prio[v] % 2) for v in range(self.n)]
        self.rew = [self.pp[v] if self.prio[v] % 2 == 0 else -self.pp[v] for v in range(self.n)]
        self.pred = [[] for _ in range(self.n)]
        for v in range(self.n):
            for w in self.succ[v]: self.pred[w].append(v)

    def dual(self):
        return Game([p + 1 for p in self.prio], [1 - o for o in self.owner], self.succ)

    def restrict(self, keep):
        """same vertex ids; keep[v] = allowed successor list of v"""
        return Game(self.prio, self.owner, keep)

    def weight(self, mask):
        s, r = 0, 0
        while mask:
            if mask & 1: s += (1 << r) if self.prio[self.byrank[r]] % 2 == 0 else -(1 << r)
            mask >>= 1; r += 1
        return s

    def key(self, x):
        c, m, d = x
        return (self.rew[c], self.weight(m), d if self.prio[c] % 2 else -d)

    def ext(self, u, x):
        """u (+) x : u put in front of a play of value x"""
        c, m, d = x
        return (c, m | (1 << self.rank[u]) if self.rank[u] > self.rank[c] else m, d + 1)


def parse(path):
    prio, owner, succ = {}, {}, {}
    txt = "".join(l for l in open(path) if not l.lstrip().startswith("%"))
    stmts = [s.strip() for s in txt.split(";")]
    for s in stmts:
        if not s or s.startswith("parity") or s.startswith("start"): continue
        if '"' in s: s = s[:s.index('"')].strip()
        parts = s.split()
        v, p, o = int(parts[0]), int(parts[1]), int(parts[2])
        prio[v], owner[v], succ[v] = p, o, [int(x) for x in parts[3].split(",")]
    n = max(prio) + 1
    assert sorted(prio) == list(range(n)), "non-contiguous ids"
    return Game([prio[v] for v in range(n)], [owner[v] for v in range(n)], [succ[v] for v in range(n)])


def evaluate(g, strat):
    """S1: owner-0 vertices fixed by strat (dict/list), owner-1 = optimiser (Odd). Returns (val, choice) with choice[x] for
    owner-1 x. Written from SPEC S1 (i)-(vi), FIX 2, FIX 4, Q2, Q4."""
    n, rank = g.n, g.rank
    gs = [[strat[v]] if g.owner[v] == 0 else g.succ[v] for v in range(n)]
    gp = [[] for _ in range(n)]
    for v in range(n):
        for w in gs[v]: gp[w].append(v)
    for v in range(n): gp[v].sort()
    alive = [True] * n; val = [None] * n; choice = [None] * n
    for v in sorted(range(n), key=lambda u: g.rew[u]):
        if not alive[v]: continue
        # (i) cycle test
        seen = {v}; stack = [v]; found = False
        while stack and not found:
            x = stack.pop()
            for y in gs[x]:
                if y == v: found = True; break
                if alive[y] and rank[y] < rank[v] and y not in seen: seen.add(y); stack.append(y)
        if not found: continue
        # (ii) R = alive vertices reaching v in G_sigma (through alive vertices)
        R = {v}; dq = deque([v])
        while dq:
            y = dq.popleft()
            for p in gp[y]:
                if alive[p] and p not in R: R.add(p); dq.append(p)
        # (iii) restricted graph on R
        rs = {x: [y for y in gs[x] if y in R] for x in R}
        path = {x: 0 for x in R}

        def reach_to(target, avoid):
            rp = {x: [] for x in R}
            for x in R:
                for y in rs[x]: rp[y].append(x)
            M = {target}; dq = deque([target])
            while dq:
                y = dq.popleft()
                for p in rp[y]:
                    if p != avoid and p not in M: M.add(p); dq.append(p)
            return M
        for u in sorted((u for u in R if rank[u] > rank[v]), key=lambda u: -rank[u]):
            if g.prio[u] % 2 == 0:
                M = reach_to(v, u)
                for q in R:
                    if q not in M: path[q] |= 1 << rank[u]
                for q in list(M) + [u]: rs[q] = [y for y in rs[q] if y in M]
            else:
                M = reach_to(u, v)
                for q in M: path[q] |= 1 << rank[u]
                for q in M:
                    if q != u: rs[q] = [y for y in rs[q] if y in M]
        # (iv) lengths
        length = {v: 0}
        if g.prio[v] % 2 == 0:
            import sys
            sys.setrecursionlimit(100000)
            onstack = set()

            def L(x):
                if x in length: return length[x]
                assert x not in onstack, "cycle in restricted graph"
                onstack.add(x)
                best, bc = None, None
                for y in sorted(rs[x]):
                    ly = L(y)
                    if best is None or ly > best: best, bc = ly, y
                onstack.discard(x)
                length[x] = best + 1
                if g.owner[x] == 1: choice[x] = bc
                return length[x]
            for x in R: L(x)
        else:
            rp = {x: [] for x in R}
            for x in R:
                for y in rs[x]: rp[y].append(x)
            for x in R: rp[x].sort()
            dq = deque([v])
            while dq:
                y = dq.popleft()
                for p in rp[y]:
                    if p not in length:
                        length[p] = length[y] + 1
                        if g.owner[p] == 1: choice[p] = y
                        dq.append(p)
            assert len(length) == len(R), "BFS did not reach all of R"
        # (v) the cycle node's own choice (FIX 2, Q2)
        if g.owner[v] == 1:
            par = {v: None}; stack = [v]; hit = None
            while stack and hit is None:
                x = stack.pop()
                for y in gs[x]:
                    if y == v: hit = x; break
                    if alive[y] and rank[y] < rank[v] and y not in par: par[y] = x; stack.append(y)
            if hit == v: choice[v] = v
            else:
                x = hit
                while par[x] != v: x = par[x]
                choice[v] = x
        # (vi)
        for x in R: val[x] = (v, path[x], length[x]); alive[x] = False
    assert all(x is not None for x in val)
    return val, choice


def best_reward_start(g):
    def pick(h, v):
        def r(w): return h.prio[w] if h.prio[w] % 2 == 0 else -h.prio[w]
        return max(h.succ[v], key=lambda w: (r(w), w if r(w) % 2 == 0 else -w))
    gd = g.dual()
    s = [pick(g, v) if g.owner[v] == 0 else None for v in range(g.n)]
    t = [pick(gd, v) if g.owner[v] == 1 else None for v in range(g.n)]
    return s, t


def improving(g, val, strat, own):
    I = []
    for v in range(g.n):
        if g.owner[v] != own: continue
        kv = g.key(val[strat[v]])
        for w in g.succ[v]:
            if w != strat[v] and g.key(val[w]) > kv: I.append((v, w))
    return I


def run(g, start=None, maxit=100000):
    """N5 (S2-S5). Returns the list of states: dict(s, t, Is, It, Xi, sb, Ut, fb, kind) for k = 0..T (the last has Is = It = [])."""
    gd = g.dual()
    s, t = start if start else best_reward_start(g)
    s, t = list(s), list(t)
    out = []
    for _ in range(maxit):
        Xi, sb = evaluate(g, s)
        tt = [t[v] if g.owner[v] == 1 else None for v in range(g.n)]
        Ut, tb = evaluate(gd, tt)             # dual: owner swapped, tau is the fixed (dual-Even) strategy
        Is = improving(g, Xi, s, 0)
        It = improving(gd, Ut, t, 1 - 0) if False else [(v, w) for v in range(g.n) if g.owner[v] == 1
                                                         for w in g.succ[v] if w != t[v] and gd.key(Ut[w]) > gd.key(Ut[t[v]])]
        st = dict(s=list(s), t=list(t), Is=Is, It=It, Xi=Xi, sb=sb, Ut=Ut, fb=False)
        out.append(st)
        if not Is and not It: return out
        # S4a
        if Is:
            A = {v: {s[v]} for v in range(g.n) if g.owner[v] == 0}
            for v, w in Is: A[v].add(w)
            keep = [sorted(A[v]) if g.owner[v] == 0 else [t[v]] for v in range(g.n)]
            Hd = g.restrict(keep).dual()
            _, ch = evaluate(Hd, [t[v] if g.owner[v] == 1 else None for v in range(g.n)])
            sn = [ch[v] if g.owner[v] == 0 else None for v in range(g.n)]
        else: sn = list(s)
        # S4b
        if It:
            A = {v: {t[v]} for v in range(g.n) if g.owner[v] == 1}
            for v, w in It: A[v].add(w)
            keep = [sorted(A[v]) if g.owner[v] == 1 else [s[v]] for v in range(g.n)]
            _, ch = evaluate(g.restrict(keep), s)
            tn = [ch[v] if g.owner[v] == 1 else None for v in range(g.n)]
        else: tn = list(t)
        # S4c
        if sn == s and tn == t:
            st["fb"] = True
            if Is:
                for v in range(g.n):
                    cand = [w for (x, w) in Is if x == v]
                    if cand: sn[v] = max(cand, key=lambda w: (g.key(Xi[w]), w))
            else:
                for v in range(g.n):
                    cand = [w for (x, w) in It if x == v]
                    if cand: tn[v] = max(cand, key=lambda w: (gd.key(Ut[w]), w))
        s, t = sn, tn
    raise RuntimeError("maxit")


def play_value(g, nx, v):
    seq, pos = [], {}
    x = v
    while x not in pos: pos[x] = len(seq); seq.append(x); x = nx[x]
    cyc = seq[pos[x]:]; c = max(cyc, key=lambda u: g.rank[u]); pre = seq[:seq.index(c)]
    m = 0
    for u in pre:
        if g.rank[u] > g.rank[c]: m |= 1 << g.rank[u]
    return (c, m, len(pre))


def lasso(nx, v):
    """(prefix list, cycle list) of v's play in the functional graph nx"""
    seq, pos = [], {}
    x = v
    while x not in pos: pos[x] = len(seq); seq.append(x); x = nx[x]
    return seq[:pos[x]], seq[pos[x]:]
