#!/usr/bin/env python3
"""REFEREE-2 independent implementations for task R2-TA1 (written from the primary sources only, not from
experiments/attr/).  Max-parity games as in TARGET.md section 1: owner 0 = Even, 1 = Odd; Even wins a play iff the
highest priority seen infinitely often is even.

  zielonka(g)                 winning regions (reference solver)
  psolB_hkp(g, order=None)    HKP arXiv 1405.0386v2 Fig. 3, run LITERALLY in min-parity colours c = M - pr (M even)
  psolB_max(g)                the same algorithm translated line by line to max-parity (cross-check of the translation)
  psolQ_hkp(g)                HKP Fig. 5 (layeredAttr with Def. 6, permissive monotone attractor), min-parity colours
  peelable(g, R, d, p)        PA** of docs/attr/TA1-proof.md section 1, exhaustive search over all X and all S
  pa2(g, WE, WO)              PA**(G) = W_E (E,d_E)-peelable and W_O (O,d_O)-peelable
  pastar(g, R, d, p)          PA* (A1-results.md section 3 / peeling.py docstring), restricted search, for Prop. 3 only
All fixpoints are naive iterate-until-stable loops (slow, simple, easy to audit)."""
import re, random
from functools import lru_cache


class Game:
    def __init__(self, pr, owner, succ):
        self.pr, self.owner, self.succ = list(pr), list(owner), [sorted(set(s)) for s in succ]
        self.n = len(self.pr)
        assert all(self.succ[v] for v in range(self.n)), "every vertex needs a successor"
        assert all(0 <= w < self.n for s in self.succ for w in s)

    def key(self):
        return (tuple(self.pr), tuple(self.owner), tuple(tuple(s) for s in self.succ))

    def pg(self):
        return "parity %d;\n" % (self.n - 1) + "".join("%d %d %d %s;\n" % (v, self.pr[v], self.owner[v], ",".join(map(str, self.succ[v]))) for v in range(self.n))

    def oneline(self):
        return " | ".join("%d %d %d %s" % (v, self.pr[v], self.owner[v], ",".join(map(str, self.succ[v]))) for v in range(self.n))


def parse_pg(text):
    rows = {}
    for line in text.replace(";", "\n").splitlines():
        line = line.strip()
        if not line or line.startswith("parity") or line.startswith("start"):
            continue
        m = re.match(r"(\d+)\s+(\d+)\s+([01])\s+([\d,]+)", line)
        rows[int(m.group(1))] = (int(m.group(2)), int(m.group(3)), [int(x) for x in m.group(4).split(",")])
    n = len(rows)
    assert sorted(rows) == list(range(n))
    return Game([rows[v][0] for v in range(n)], [rows[v][1] for v in range(n)], [rows[v][2] for v in range(n)])


# ---------------------------------------------------------------- generic attractor inside a vertex set R (edges inside R)
def attr(g, R, X, p):
    """Standard attractor of player p to X inside R (HKP Def. 1 restricted to the subgame R); X ∩ R included."""
    A = set(X) & R
    while True:
        new = {v for v in R - A if (g.owner[v] == p and any(w in A for w in g.succ[v] if w in R))
               or (g.owner[v] != p and all(w in A for w in g.succ[v] if w in R))}
        if not new:
            return frozenset(A)
        A |= new


def is_subgame(g, R):
    return all(any(w in R for w in g.succ[v]) for v in R)


def is_trap(g, S, R, q):
    """S is a trap for player q inside R (HKP Def. 2 / DJT): q's vertices of S keep all R-successors in S, the other
    player's vertices of S keep at least one R-successor in S."""
    for v in S:
        rs = [w for w in g.succ[v] if w in R]
        if g.owner[v] == q:
            if not all(w in S for w in rs):
                return False
        else:
            if not any(w in S for w in rs):
                return False
    return True


# ---------------------------------------------------------------- Zielonka (max-parity)
def zielonka(g):
    def solve(R):
        if not R:
            return frozenset(), frozenset()
        d = max(g.pr[v] for v in R)
        p = d % 2
        U = {v for v in R if g.pr[v] == d}
        A = attr(g, R, U, p)
        W0, W1 = solve(R - A)
        Wp, Wq = (W0, W1) if p == 0 else (W1, W0)
        if not Wq:
            return (R, frozenset()) if p == 0 else (frozenset(), R)
        B = attr(g, R, Wq, 1 - p)
        W0b, W1b = solve(R - B)
        return (W0b, W1b | B) if p == 0 else (W0b | B, W1b)
    return solve(frozenset(range(g.n)))


# ---------------------------------------------------------------- HKP, literal, min-parity colours
def colours(g):
    """c(v) = M - pr(v) with M even, M >= max pr: order reversed, parity kept (HKP use min-parity, tex:366-367)."""
    M = max(g.pr)
    M = M if M % 2 == 0 else M + 1
    return [M - q for q in g.pr]


def mattr_hkp(g, c, V, X, col, p):
    """HKP Def. 3: MAttr_p(X, col) = mu Z. MPred_p(Z, X, col) in the current game with node set V, target X external:
    MPred = {v in V_p : c(v) >= col, v.E ∩ (Z ∪ X) != {}} ∪ {v in V_{1-p} : c(v) >= col, v.E ⊆ Z ∪ X}."""
    Z = set()
    while True:
        ZX = Z | X
        new = set()
        for v in V:
            if v in Z or c[v] < col:
                continue
            E = [w for w in g.succ[v] if w in V]
            if (g.owner[v] == p and any(w in ZX for w in E)) or (g.owner[v] != p and all(w in ZX for w in E)):
                new.add(v)
        if not new:
            return frozenset(Z)
        Z |= new


def pmattr_hkp(g, c, V, X, col, p):
    """HKP Def. 6: permissive: eligibility is c(v) >= col OR v in X."""
    Z = set()
    while True:
        ZX = Z | X
        new = set()
        for v in V:
            if v in Z or not (c[v] >= col or v in X):
                continue
            E = [w for w in g.succ[v] if w in V]
            if (g.owner[v] == p and any(w in ZX for w in E)) or (g.owner[v] != p and all(w in ZX for w in E)):
                new.add(v)
        if not new:
            return frozenset(Z)
        Z |= new


def psolB_hkp(g, order=None, log=None):
    """HKP Fig. 3 (tex:728-747). order: None = 'colors d in descending ordering' of the current game; a callable
    cols -> list gives another order (for the order-independence check, HKP Thm 6). Returns (win, residual)."""
    c = colours(g)
    win = [None] * g.n
    V = frozenset(range(g.n))

    def psolB(V):                                   # one recursive call = one iteration of the colour loop from the top
        cols = sorted({c[v] for v in V}, reverse=True)
        if order is not None:
            cols = order(cols)
        for d in cols:
            X = frozenset(v for v in V if c[v] == d)
            cache = frozenset()
            while X and X != cache:
                cache = X
                MA = mattr_hkp(g, c, V, X, d, d % 2)
                if X <= MA:
                    D = attr(g, V, MA, d % 2)
                    for v in D:
                        win[v] = d % 2
                    if log is not None:
                        log.append((d, d % 2, sorted(MA), sorted(D)))
                    return psolB(V - D)
                X = X & MA
        return V
    res = psolB(V)
    return win, res


def psolB_max(g):
    """The same algorithm written directly in max-parity: 'colour >= d' is 'priority <= d', descending colours is
    ascending priorities, player = parity of the priority.  Must agree with psolB_hkp on every game."""
    win = [None] * g.n

    def mattr(V, X, d, p):
        Z = set()
        while True:
            ZX = Z | X
            new = set()
            for v in V - Z:
                if g.pr[v] > d:
                    continue
                E = [w for w in g.succ[v] if w in V]
                if (g.owner[v] == p and any(w in ZX for w in E)) or (g.owner[v] != p and all(w in ZX for w in E)):
                    new.add(v)
            if not new:
                return frozenset(Z)
            Z |= new

    def run(V):
        for d in sorted({g.pr[v] for v in V}):
            X = frozenset(v for v in V if g.pr[v] == d)
            cache = frozenset()
            while X and X != cache:
                cache = X
                MA = mattr(V, X, d, d % 2)
                if X <= MA:
                    D = attr(g, V, MA, d % 2)
                    for v in D:
                        win[v] = d % 2
                    return run(V - D)
                X = X & MA
        return V
    return win, run(frozenset(range(g.n)))


def layered_attr_hkp(g, c, V, p, X):
    """HKP Fig. 5 layeredAttr(G, p, X); PRE-CONDITION: all nodes of X have parity p."""
    assert all(c[v] % 2 == p for v in X)
    A = frozenset()
    b = max(c[v] for v in X)
    d = p
    while d <= b:
        Y = frozenset(v for v in X if c[v] <= d)
        A = pmattr_hkp(g, c, V, A | Y, d, p)
        d += 2
    return A


def psolQ_hkp(g, log=None):
    """HKP Fig. 5 psolQ, 'for colors b in ascending order' over the colours of the current game."""
    c = colours(g)
    win = [None] * g.n

    def psolQ(V):
        for b in sorted({c[v] for v in V}):
            X = frozenset(v for v in V if c[v] <= b and c[v] % 2 == b % 2)
            cache = frozenset()
            while X and X != cache:
                cache = X
                W = layered_attr_hkp(g, c, V, b % 2, X)
                if X <= W:
                    D = attr(g, V, W, b % 2)
                    for v in D:
                        win[v] = b % 2
                    if log is not None:
                        log.append((b, b % 2, sorted(W), sorted(D)))
                    return psolQ(V - D)
                X = X & W
        return V
    return win, psolQ(frozenset(range(g.n)))


# ---------------------------------------------------------------- PA** (TA1-proof.md section 1), max-parity
def mattr_max(g, R, X, d, p):
    """MAttr_p^R(X, d) of TA1-proof.md: least Z ⊆ R, vertices of priority <= d, p-vertex with an R-successor in Z ∪ X
    or q-vertex with all R-successors in Z ∪ X; X external."""
    Z = set()
    while True:
        ZX = Z | X
        new = set()
        for v in R - Z:
            if g.pr[v] > d:
                continue
            E = [w for w in g.succ[v] if w in R]
            if (g.owner[v] == p and any(w in ZX for w in E)) or (g.owner[v] != p and all(w in ZX for w in E)):
                new.add(v)
        if not new:
            return frozenset(Z)
        Z |= new


def subsets(items):
    items = sorted(items)
    for mask in range(1, 1 << len(items)):
        yield frozenset(items[i] for i in range(len(items)) if mask >> i & 1)


def make_peelable(g, star=False):
    """Returns ok(R, d, p): R (frozenset, a subgame of G with pr(R) <= d, d ≡ p mod 2) is (p,d)-peelable.
    star=False: PA** (options (a) and (b) in any order).  star=True: PA* (only (b)-steps, then the whole remainder must be
    the attractor of its top-priority vertices)."""
    @lru_cache(maxsize=None)
    def ok(R, d, p):
        assert d % 2 == p and all(g.pr[v] <= d for v in R)
        if not R:
            return True
        cands = []
        top = frozenset(v for v in R if g.pr[v] == d)
        if not star:
            for X in subsets(top):                                   # option (a)
                W = mattr_max(g, R, X, d, p)
                if X <= W:
                    cands.append(attr(g, R, W, p))
        elif attr(g, R, top, p) == R:
            return True
        if d >= 2:
            low = [v for v in R if g.pr[v] <= d - 2]
            for S in subsets(low):                                   # option (b)
                if is_trap(g, S, R, 1 - p) and ok(S, d - 2, p):
                    cands.append(attr(g, R, S, p))
        return any(ok(R - F, d, p) for F in cands)
    return ok


def d_p(g, p):
    M = max(g.pr)
    return M if M % 2 == p else M + 1


def pa2(g, WE, WO, star=False):
    ok = make_peelable(g, star)
    return ok(frozenset(WE), d_p(g, 0), 0) and ok(frozenset(WO), d_p(g, 1), 1)


# ---------------------------------------------------------------- enumeration and sampling
def all_games(n, prios=None):
    """Every game on n vertices with priorities in prios (default TARGET: 0..n), every owner vector, every non-empty
    successor set.  No canonicalisation at all."""
    import itertools
    prios = list(range(n + 1)) if prios is None else prios
    succsets = [list(s) for r in range(1, n + 1) for s in itertools.combinations(range(n), r)]
    for pr in itertools.product(prios, repeat=n):
        for ow in itertools.product((0, 1), repeat=n):
            for sc in itertools.product(succsets, repeat=n):
                yield Game(pr, ow, sc)


def random_game(rnd, n, maxpr=None, deg=None):
    maxpr = n if maxpr is None else maxpr
    pr = [rnd.randint(0, maxpr) for _ in range(n)]
    ow = [rnd.randint(0, 1) for _ in range(n)]
    sc = []
    for v in range(n):
        k = rnd.choice(deg) if deg else rnd.randint(1, n)
        sc.append(rnd.sample(range(n), min(k, n)))
    return Game(pr, ow, sc)
