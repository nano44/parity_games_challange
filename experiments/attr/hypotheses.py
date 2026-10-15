#!/usr/bin/env python3
"""Hypothesis tests for the A1 judgement: which structural predicate separates psolQ-solved from psolQ-undecided games?
Predicates on the two dominions (max-parity, DJT decompositions with D2a's d):
  PA: there is a decomposition in which every S_i (at every level, inside the level's subgame R) is a trap for the
      opponent in R itself (so the opponent can never leave S_i, not even into the level's attractors);
  PB: the same with "trap for the opponent in R \\ A" (may escape only into the top attractor A of the level);
  PC: the definition itself (trap in G_i): always true by DJT Thm 2;
  PD: a decomposition (recursively) whose piece-escape graph is acyclic at every level: pieces A, A_1..A_l of the level,
      escape P -> Q when an opponent vertex of P has an edge into Q (escapes of inner pieces to outside their S_i are the
      parent level's business).
Usage: hypotheses.py n [--sample K --seed S]   (n <= 3: all canonical games; else K random games on random orbits)
Prints the confusion matrix psolQ status x predicate, and the first counterexample to each implication."""
import sys, os, random, itertools
from functools import lru_cache
from itertools import combinations
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a1lib, pg, zielonka
from strahler import Strahler


def closed_decomposition(g, W, d, p, mode):
    S = Strahler(g)

    @lru_cache(maxsize=None)
    def ok(R, d):
        if not R:
            return True
        if d < 0:
            return False
        top = frozenset(v for v in R if g.prio[v] == d)
        A = S.attr(R, top, p)
        rem = R - A
        if d == 0 or (d == 1 and p == 1):
            return not rem
        base = R if mode == "A" else rem
        if mode == "D":
            # pieces A, A_1, ..., A_l; escape P -> Q if a (1-p)-vertex of P has an edge (in R) into Q; need acyclic.
            def acyclic(pieces):
                k = len(pieces)
                adj = {i: set() for i in range(k)}
                for i, P in enumerate(pieces):
                    for u in P:
                        if g.owner[u] == p:
                            continue
                        for w in S.succ[u] & R:
                            for j, Q in enumerate(pieces):
                                if j != i and w in Q:
                                    adj[i].add(j)
                state = {}
                def dfs(i):
                    state[i] = 1
                    for j in adj[i]:
                        if state.get(j) == 1 or (state.get(j) is None and not dfs(j)):
                            return False
                    state[i] = 2
                    return True
                return all(state.get(i) == 2 or dfs(i) for i in range(k))

            def chainD(rest, pieces):
                if not rest:
                    return acyclic(pieces)
                elems = sorted(v for v in rest if g.prio[v] <= d - 2)
                for r in range(1, len(elems) + 1):
                    for Sset in combinations(elems, r):
                        Sset = frozenset(Sset)
                        if not S.is_trap_for_opponent(Sset, rest, p):
                            continue
                        if not ok(Sset, d - 2):
                            continue
                        Ai = S.attr(rest, Sset, p)
                        if chainD(rest - Ai, pieces + [Ai]):
                            return True
                return False
            return chainD(rem, [A])

        @lru_cache(maxsize=None)
        def chain(rest):
            if not rest:
                return True
            elems = sorted(v for v in rest if g.prio[v] <= d - 2)
            for r in range(1, len(elems) + 1):
                for Sset in combinations(elems, r):
                    Sset = frozenset(Sset)
                    if not S.is_trap_for_opponent(Sset, base, p):
                        continue
                    if not ok(Sset, d - 2):
                        continue
                    if chain(rest - S.attr(rest, Sset, p)):
                        return True
            return False
        return chain(rem)
    return ok(frozenset(W), d)


def predicates(g, ref):
    WE = [v for v in range(g.n) if ref[v] == 0]
    WO = [v for v in range(g.n) if ref[v] == 1]
    P = max(g.prio)
    dE = P if P % 2 == 0 else P + 1
    dO = P if P % 2 == 1 else P + 1
    out = {}
    for mode in ("A", "B", "D"):
        out[mode] = closed_decomposition(g, WE, dE, 0, mode) and closed_decomposition(g, WO, dO, 1, mode)
    return out


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n = int(args[0])
    opt = lambda k, d: int(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
    sample, seed = opt("--sample", 0), opt("--seed", 1)
    if sample:
        rnd = random.Random(seed)
        orbits = [cfg for cfg, m in a1lib.succ_orbits(n)]
        pats = list(a1lib.priority_patterns(n))
        def games():
            for _ in range(sample):
                cfg = rnd.choice(orbits)
                yield pg.Game(rnd.choice(pats), [rnd.randint(0, 1) for _ in range(n)], [list(s) for s in cfg])
    else:
        def games():
            for cfg, m in a1lib.succ_orbits(n):
                yield from a1lib.games_on(cfg, n)
    conf, first = {}, {}
    total = 0
    for g in games():
        total += 1
        r = a1lib.classify(g, others=True)
        pr = predicates(g, r["ref"])
        for mode in ("A", "B", "D"):
            for solver in ("psolq", "psolb", "psol"):
                key = (mode, solver + " " + r[solver], pr[mode])
                conf[key] = conf.get(key, 0) + 1
                if key not in first:
                    first[key] = pg.dumps(g).replace("\n", " | ")
    print(f"n={n}, {total} games")
    for key in sorted(conf):
        print(f"  P{key[0]} = {key[2]!s:5s}  psolQ {key[1]:9s} : {conf[key]:7d}   e.g. {first[key]}")
    for mode in ("A", "B", "D"):
        for solver in ("psolq", "psolb", "psol"):
            imp1 = conf.get((mode, solver + " undecided", True), 0)
            imp2 = conf.get((mode, solver + " solved", False), 0)
            print(f"P{mode} => {solver} solved: {'HOLDS' if imp1 == 0 else f'FAILS ({imp1})'};  {solver} solved => P{mode}: {'HOLDS' if imp2 == 0 else f'FAILS ({imp2})'}")


if __name__ == "__main__":
    main()
