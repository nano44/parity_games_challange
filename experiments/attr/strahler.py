#!/usr/bin/env python3
"""Exact Strahler number of a small parity game (Daviaud, Jurdzinski, Thejaswini, arXiv 2003.08627v2, section 2;
definitions fixed in docs/attr/A1-statement.md D1-D2, convention D2a). Max-parity, TARGET.md vocabulary.

Str(G) = max(Str_E(W_E), Str_O(W_O)); Str_p(W) = minimum over all p d-attractor decompositions H of G ∩ W of Str(T_H),
with d the least number of p's parity >= max pr(V) (D2a; `shift` adds 2 to d for the sensitivity check).
Exact by dynamic programming over vertex subsets (notebook "Strahler DP"); brute force over all decompositions for the
cross-check (`strahler_bruteforce`). Regions come from harness zielonka.py unless `win` is given.

API: strahler(g, win=None, shift=0) -> (Str, info) with info = dict(E=(str, tree), O=(str, tree), d_E, d_O).
Trees are nested tuples: () is the trivial tree <>, (T1, T2, ...) = <T1, T2, ...>.
CLI: strahler.py game.pg [--shift 2] [--brute]"""
import sys, os
from functools import lru_cache
from itertools import combinations
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "harness"))
import pg, zielonka

INF = float("inf")


def tree_strahler(T):
    """DJT section 2: Str(<>) = 1; Str(<T_1..T_l>) = m if a unique child attains m = max Str(T_i), else m+1."""
    if not T:
        return 1
    vals = [tree_strahler(t) for t in T]
    m = max(vals)
    return m if vals.count(m) == 1 else m + 1


def tree_height(T):
    return 1 if not T else 1 + max(tree_height(t) for t in T)


def tree_leaves(T):
    return 1 if not T else sum(tree_leaves(t) for t in T)


def fold(children):
    """Strahler number of <children> from the children's Strahler numbers."""
    if not children:
        return 1
    m = max(children)
    return m if children.count(m) == 1 else m + 1


class Strahler:
    def __init__(self, g):
        self.g = g
        self.succ = [frozenset(s) for s in g.succ]

    def attr(self, R, X, p):
        """Standard attractor of player p to X inside the subgame R (frozenset); X included."""
        A = set(X) & R
        changed = True
        while changed:
            changed = False
            for v in R:
                if v in A:
                    continue
                s = self.succ[v] & R
                if (self.g.owner[v] == p and s & A) or (self.g.owner[v] != p and s <= A):
                    A.add(v); changed = True
        return frozenset(A)

    def is_trap_for_opponent(self, S, R, p):
        """S is a trap for player 1-p in the subgame R: p's vertices keep an edge inside S, (1-p)'s vertices have all
        their R-edges inside S (DJT section 2: a p-strategy traps the opponent in S). Implies S is a subgame."""
        for v in S:
            s = self.succ[v] & R
            if self.g.owner[v] == p:
                if not (s & S):
                    return False
            elif not (s <= S):
                return False
        return True

    def min_strahler(self, R, d, p):
        """(minimal Strahler number, witness tree) over all p d-attractor decompositions of the subgame R
        (a trap for 1-p with pr(R) <= d, d of p's parity); (INF, None) if none exists."""
        @lru_cache(maxsize=None)
        def f(R, d):
            if not R:
                return 1, ()
            if d < 0:
                return INF, None
            top = frozenset(v for v in R if self.g.prio[v] == d)
            A = self.attr(R, top, p)
            rem = R - A
            if d == 0 or (d == 1 and p == 1):            # l = 0 forced (DJT: if d = 0 then l = 0; dual for Odd)
                return (1, ()) if not rem else (INF, None)
            return chain(rem, d - 2, 0, 0)

        @lru_cache(maxsize=None)
        def chain(rem, dc, m, c):
            """Minimal final Strahler number of the children sequence, given children so far have max m attained
            c times (c in {0,1,2}); returns (value, tuple of child trees)."""
            if not rem:
                return (1 if c == 0 else (m if c == 1 else m + 1)), ()
            best = (INF, None)
            elems = sorted(v for v in rem if self.g.prio[v] <= dc)
            for r in range(1, len(elems) + 1):
                for S in combinations(elems, r):
                    S = frozenset(S)
                    if not self.is_trap_for_opponent(S, rem, p):
                        continue
                    s, T = f(S, dc)
                    if s == INF:
                        continue
                    m2, c2 = (s, 1) if s > m else ((m, 2) if s == m else (m, c))
                    rest = rem - self.attr(rem, S, p)
                    val, kids = chain(rest, dc, m2, c2)
                    if val < best[0]:
                        best = (val, (T,) + kids)
                        if val == 1:
                            return best
            return best

        v, T = f(frozenset(R), d)
        f.cache_clear(); chain.cache_clear()
        return v, T


def regions(g):
    win = zielonka.solve(g)
    return frozenset(v for v in range(g.n) if win[v] == 0), frozenset(v for v in range(g.n) if win[v] == 1)


def strahler(g, win=None, shift=0):
    WE, WO = regions(g) if win is None else (frozenset(v for v in range(g.n) if win[v] == 0),
                                              frozenset(v for v in range(g.n) if win[v] == 1))
    P = max(g.prio)
    dE = (P if P % 2 == 0 else P + 1) + shift
    dO = (P if P % 2 == 1 else P + 1) + shift
    S = Strahler(g)
    sE, TE = S.min_strahler(WE, dE, 0)
    sO, TO = S.min_strahler(WO, dO, 1)
    assert sE < INF and sO < INF, "no attractor decomposition found: regions or code wrong"
    return max(sE, sO), dict(E=(sE, TE), O=(sO, TO), d_E=dE, d_O=dO)


def all_decompositions(S, R, d, p):
    """Brute force: yield every tree of a p d-attractor decomposition of R (no DP, no pruning). Cross-check only."""
    if not R:
        yield (); return
    if d < 0:
        return
    top = frozenset(v for v in R if S.g.prio[v] == d)
    rem = R - S.attr(R, top, p)
    if d == 0 or (d == 1 and p == 1):
        if not rem:
            yield ()
        return

    def chains(rem):
        if not rem:
            yield (); return
        elems = sorted(v for v in rem if S.g.prio[v] <= d - 2)
        for r in range(1, len(elems) + 1):
            for Sset in combinations(elems, r):
                Sset = frozenset(Sset)
                if not S.is_trap_for_opponent(Sset, rem, p):
                    continue
                rest = rem - S.attr(rem, Sset, p)
                for T in all_decompositions(S, Sset, d - 2, p):
                    for kids in chains(rest):
                        yield (T,) + kids
    yield from chains(rem)


def strahler_bruteforce(g, shift=0):
    WE, WO = regions(g)
    P = max(g.prio)
    dE = (P if P % 2 == 0 else P + 1) + shift
    dO = (P if P % 2 == 1 else P + 1) + shift
    S = Strahler(g)
    sE = min(tree_strahler(T) for T in all_decompositions(S, WE, dE, 0))
    sO = min(tree_strahler(T) for T in all_decompositions(S, WO, dO, 1))
    return max(sE, sO)


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    shift = int(sys.argv[sys.argv.index("--shift") + 1]) if "--shift" in sys.argv else 0
    g = pg.read(args[0])
    s, info = strahler(g, shift=shift)
    print(f"Strahler number {s}  (Even: {info['E'][0]} tree {info['E'][1]} d={info['d_E']}; "
          f"Odd: {info['O'][0]} tree {info['O'][1]} d={info['d_O']})")
    if "--brute" in sys.argv:
        print(f"brute force: {strahler_bruteforce(g, shift)}")
