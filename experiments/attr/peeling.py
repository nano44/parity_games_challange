#!/usr/bin/env python3
"""Peeling decompositions (predicate PA*, docs/attr/A1-results.md section 3; proof in docs/attr/TA1-proof.md).
A p-peeling d-decomposition of a subgame R (a trap for 1-p, pr(R) <= d, d of p's parity) is a sequence
(S_1, H_1, A_1), ..., (S_l, H_l, A_l) with R_0 = R and, for i = 1..l: S_i a non-empty trap for 1-p in R_{i-1} with
pr(S_i) <= d-2, H_i a p-peeling (d-2)-decomposition of S_i, A_i = Attr_p^{R_{i-1}}(S_i), R_i = R_{i-1} \\ A_i; and finally
R_l = Attr_p^{R_l}(pr^{-1}(d) ∩ R_l). (DJT's decomposition removes the top attractor FIRST and asks S_i to be a trap only in
the remainder; peeling removes it LAST, so S_i may escape only into earlier pieces A_1..A_{i-1}.)
PA*(G): both W_E and W_O have peeling decompositions (d = least number of the player's parity >= max priority).
peeling(): exact, by search over all sequences (memoised).  greedy(): canonical polynomial-time candidate: at each stage take
the LARGEST trap for 1-p avoiding priorities > d-2 (complement of the opponent's attractor to them), recurse, remove its
attractor, repeat until no such trap is left, then check the final attractor condition.
Usage: peeling.py n [--sample K --seed S] : table psolQ/psolB status x PA x PA* x greedy, containment of HKP classes."""
import sys, os, random, itertools
from functools import lru_cache
from itertools import combinations
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a1lib, pg, hypotheses
from strahler import Strahler


def peeling(g, R, d, p):
    S = Strahler(g)

    @lru_cache(maxsize=None)
    def ok(R, d):
        if not R:
            return True
        if d < 0:
            return False
        top = frozenset(v for v in R if g.prio[v] == d)

        @lru_cache(maxsize=None)
        def rec(Rc):
            if S.attr(Rc, top & Rc, p) == Rc:
                return True
            elems = sorted(v for v in Rc if g.prio[v] <= d - 2)
            for r in range(1, len(elems) + 1):
                for Sset in combinations(elems, r):
                    Sset = frozenset(Sset)
                    if not S.is_trap_for_opponent(Sset, Rc, p) or not ok(Sset, d - 2):
                        continue
                    if rec(Rc - S.attr(Rc, Sset, p)):
                        return True
            return False
        return rec(R)
    return ok(frozenset(R), d)


def greedy(g, R, d, p):
    S = Strahler(g)

    def ok(R, d):
        if not R:
            return True
        if d < 0:
            return False
        Rc = R
        while True:
            high = frozenset(v for v in Rc if g.prio[v] > d - 2)
            Z = Rc - S.attr(Rc, high, 1 - p)          # largest trap for 1-p in Rc avoiding priorities > d-2
            if not Z:
                break
            if not ok(Z, d - 2):
                return False
            Rc = Rc - S.attr(Rc, Z, p)
        top = frozenset(v for v in Rc if g.prio[v] == d)
        return S.attr(Rc, top, p) == Rc
    return ok(frozenset(R), d)


def both(g, ref, fn):
    WE = frozenset(v for v in range(g.n) if ref[v] == 0)
    WO = frozenset(v for v in range(g.n) if ref[v] == 1)
    P = max(g.prio)
    dE = P if P % 2 == 0 else P + 1
    dO = P if P % 2 == 1 else P + 1
    return fn(g, WE, dE, 0) and fn(g, WO, dO, 1)


def sccs(g):
    import verify
    return verify.sccs(range(g.n), lambda v: list(set(g.succ[v])))


def classes(g):
    """HKP's complete classes in max-parity: Buchi (at most two priority values, of different parity, or one value),
    SCC-constant priority (HKP Thm 8), deterministic (Lemma 5)."""
    vals = sorted(set(g.prio))
    buchi = len(vals) == 1 or (len(vals) == 2 and vals[0] % 2 != vals[1] % 2)
    scc_const = all(len({g.prio[v] for v in c}) == 1 for c in sccs(g))
    det = all(len(set(s)) == 1 for s in g.succ)
    return dict(buchi=buchi, scc=scc_const, det=det)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    n = int(args[0])
    opt = lambda k, d: int(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
    sample, seed = opt("--sample", 0), opt("--seed", 1)
    if sample:
        rnd = random.Random(seed)
        pats = list(a1lib.priority_patterns(n))
        succsets = [list(s) for r in range(1, n + 1) for s in combinations(range(n), r)]
        games = (pg.Game(rnd.choice(pats), [rnd.randint(0, 1) for _ in range(n)], [rnd.choice(succsets) for _ in range(n)])
                 for _ in range(sample))
    else:
        games = (g for cfg, m in a1lib.succ_orbits(n) for g in a1lib.games_on(cfg, n))
    conf, first, total = {}, {}, 0
    for g in games:
        total += 1
        r = a1lib.classify(g, others=True)
        pa = hypotheses.predicates(g, r["ref"])["A"]
        ps = both(g, r["ref"], peeling)
        gr = both(g, r["ref"], greedy)
        cl = classes(g)
        keys = [("psolq", r["psolq"], "PA*", ps), ("psolb", r["psolb"], "PA*", ps), ("psol", r["psol"], "PA*", ps),
                ("PA", pa, "PA*", ps), ("greedy", gr, "PA*", ps)]
        keys += [(c, True, "PA*", ps) for c, v in cl.items() if v]
        for k in keys:
            conf[k] = conf.get(k, 0) + 1
            if k not in first:
                first[k] = pg.dumps(g).replace("\n", " | ")
    print(f"n={n}, {total} games")
    for k in sorted(conf, key=str):
        print(f"  {k[0]:7s} {str(k[1]):10s} {k[2]} = {str(k[3]):5s} : {conf[k]:8d}   e.g. {first[k]}")
    def imp(a, av, b, bv):
        c = conf.get((a, av, b, bv), 0)
        return "HOLDS" if c == 0 else f"FAILS ({c})"
    print("PA* => psolQ solves:", imp("psolq", "undecided", "PA*", True), "; PA* => psolB solves:", imp("psolb", "undecided", "PA*", True),
          "; PA* => psol solves:", imp("psol", "undecided", "PA*", True))
    print("PA => PA*:", imp("PA", True, "PA*", False), "; greedy => PA*:", imp("greedy", True, "PA*", False), "; PA* => greedy:", imp("greedy", False, "PA*", True))
    for c in ("buchi", "scc", "det"):
        print(f"{c} => PA*:", imp(c, True, "PA*", False), f"(class size {conf.get((c, True, 'PA*', True), 0) + conf.get((c, True, 'PA*', False), 0)})")
    print("psolQ solves => PA*:", imp("psolq", "solved", "PA*", False))


if __name__ == "__main__" and "--pa2" not in sys.argv:
    main()


# ---- PA**: mixed-order peeling -----------------------------------------------------------------------------------
def mattr(g, S, R, X, d, p):
    """HKP Def. 3 in max-parity: vertices of R with priority <= d from which p forces reaching X in >= 1 move through
    vertices of priority <= d; X is external (a vertex of X is in the result only if attracted in >= 1 move)."""
    Z = set()
    changed = True
    while changed:
        changed = False
        for v in R:
            if v in Z or g.prio[v] > d:
                continue
            s = S.succ[v] & R
            if (g.owner[v] == p and (s & (Z | X))) or (g.owner[v] != p and s <= (Z | X)):
                Z.add(v); changed = True
    return frozenset(Z)


def largest_fatal(g, S, R, T, d, p):
    """Greatest fixpoint X ⊆ T with X ⊆ MAttr(X) (psolB's loop at one colour)."""
    X = frozenset(T)
    while X:
        W = mattr(g, S, R, X, d, p)
        if X <= W:
            return X, W
        X = X & W
    return frozenset(), frozenset()


def peelable(g, R, d, p, exact=True):
    """PA** on the subgame R (a trap for 1-p, pr(R) <= d, d of p's parity): R is empty, or some non-empty piece F can be
    decided now and R \\ F is again peelable, where F is
      (a) Attr_p^R(MAttr_p^R(X, d)) for a non-empty X ⊆ pr^{-1}(d) ∩ R with X ⊆ MAttr_p^R(X, d)  [self-returning top set], or
      (b) Attr_p^R(S) for a non-empty trap S for 1-p in R with pr(S) <= d-2 that is itself peelable at d-2 [closed sub-trap].
    exact=True searches every X and every S; exact=False is the canonical rule: the largest X (gfp), else the bottom SCCs
    of the largest admissible trap (tried in turn)."""
    S = Strahler(g)

    @lru_cache(maxsize=None)
    def ok(R, d):
        if not R:
            return True
        if d < 0:
            return False
        T = frozenset(v for v in R if g.prio[v] == d)
        if exact:
            cands = []
            Ts = sorted(T)
            for r in range(1, len(Ts) + 1):
                for X in combinations(Ts, r):
                    X = frozenset(X)
                    W = mattr(g, S, R, X, d, p)
                    if X <= W:
                        cands.append(S.attr(R, W, p))
            elems = sorted(v for v in R if g.prio[v] <= d - 2)
            for r in range(1, len(elems) + 1):
                for Sset in combinations(elems, r):
                    Sset = frozenset(Sset)
                    if S.is_trap_for_opponent(Sset, R, p) and ok(Sset, d - 2):
                        cands.append(S.attr(R, Sset, p))
            return any(ok(R - F, d) for F in cands)
        X, W = largest_fatal(g, S, R, T, d, p)
        if X:
            return ok(R - S.attr(R, W, p), d)
        high = frozenset(v for v in R if g.prio[v] > d - 2)
        Z = R - S.attr(R, high, 1 - p)
        if not Z:
            return False
        import verify
        for C in verify.sccs(sorted(Z), lambda v: [w for w in S.succ[v] if w in Z]):
            C = frozenset(C)
            if not all((S.succ[v] & Z) <= C for v in C):   # bottom SCC of the subgame Z
                continue
            if ok(C, d - 2):
                return ok(R - S.attr(R, C, p), d)
        return False
    return ok(frozenset(R), d)


def pa2(g, R, d, p):
    return peelable(g, R, d, p, exact=True)


def pa2_greedy(g, R, d, p):
    return peelable(g, R, d, p, exact=False)


def main2():
    """peeling.py --pa2 n [--sample K --seed S]: PA** table."""
    args = [a for a in sys.argv[1:] if not a.startswith("--") and a != "--pa2"]
    n = int(args[0])
    opt = lambda k, d: int(sys.argv[sys.argv.index(k) + 1]) if k in sys.argv else d
    sample, seed = opt("--sample", 0), opt("--seed", 1)
    if sample:
        rnd = random.Random(seed)
        pats = list(a1lib.priority_patterns(n))
        succsets = [list(s) for r in range(1, n + 1) for s in combinations(range(n), r)]
        games = (pg.Game(rnd.choice(pats), [rnd.randint(0, 1) for _ in range(n)], [rnd.choice(succsets) for _ in range(n)])
                 for _ in range(sample))
    else:
        games = (g for cfg, m in a1lib.succ_orbits(n) for g in a1lib.games_on(cfg, n))
    conf, first, total = {}, {}, 0
    for g in games:
        total += 1
        r = a1lib.classify(g, others=True)
        ps = both(g, r["ref"], peeling)
        p2 = both(g, r["ref"], pa2)
        g2 = both(g, r["ref"], pa2_greedy)
        cl = classes(g)
        keys = [("psolq", r["psolq"], p2), ("psolb", r["psolb"], p2), ("psol", r["psol"], p2), ("PA*", ps, p2), ("greedy2", g2, p2)]
        keys += [(c, True, p2) for c, v in cl.items() if v]
        for k in keys:
            conf[k] = conf.get(k, 0) + 1
            if k not in first:
                first[k] = pg.dumps(g).replace("\n", " | ")
    print(f"n={n}, {total} games")
    for k in sorted(conf, key=str):
        print(f"  {k[0]:7s} {str(k[1]):10s} PA** = {str(k[2]):5s} : {conf[k]:8d}   e.g. {first[k]}")
    def imp(a, av, bv):
        c = conf.get((a, av, bv), 0)
        return "HOLDS" if c == 0 else f"FAILS ({c})"
    print("PA** => psolQ solves:", imp("psolq", "undecided", True), "; PA** => psolB solves:", imp("psolb", "undecided", True),
          "; psolB solves => PA**:", imp("psolb", "solved", False), "; psolQ solves => PA**:", imp("psolq", "solved", False))
    print("PA* => PA**:", imp("PA*", True, False), "; greedy2 => PA**:", imp("greedy2", True, False), "; PA** => greedy2:", imp("greedy2", False, True))
    for c in ("buchi", "scc", "det"):
        print(f"{c} => PA**:", imp(c, True, False))


if __name__ == "__main__" and "--pa2" in sys.argv:
    main2()
