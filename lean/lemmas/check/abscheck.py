#!/usr/bin/env python3
"""Numerical reading check of PGLemmas/AbsStatement.lean (box 208 section 10, Statement ABS).

This is a Python transcription of the Lean definitions (SPGame, edge, PathW, d, HowardAt,
NoZeroCycle) and of the hypotheses and the two conclusions of `AbsStatement`.  It is NOT the Lean
code and proves nothing.  It answers two questions the Lean proof cannot:
  * are the hypotheses satisfiable with T >= 1 (is the statement about something)?
  * does the statement, read by a second implementation, hold on random games (is the reading
    of the statement the intended one)?

Usage:  python3 -I lean/lemmas/check/abscheck.py SEED GAMES NMAX
Control: ABS_CTRL=1 moves every Max vertex to a SMALLEST edge.  Then the Howard hypothesis fails
(hypfail), and the conclusions are checked all the same: c2fail must fire.

d is computed twice: by Bellman-Ford, and (n <= 7) by enumerating all simple paths to the
target, which is the definition `Nat.find` of the least weight of a path (weights are >= 0, so a
least-weight path can be taken simple).  A disagreement is counted in `dfail`.

Counters (all must be 0 except in the control):
  dfail      Bellman-Ford and path enumeration disagree               (unit: vertex of a state)
  hypfail    a hypothesis of AbsStatement fails on the generated run  (unit: run)
  boundfail  T > (sum over Max z of |E z|) * |V|                      (unit: run)
  c2fail     clause (2) fails at a step t < T                         (unit: step)
  lastfail   clause (2) fails at the LAST step t = T - 1              (unit: run with T >= 1)
"""
import itertools
import os
import random
import sys

INF = float("inf")
CTRL = os.environ.get("ABS_CTRL") == "1"


def zero_cycle(n, E, w):
    """NoZeroCycle fails: a closed walk along edges b in E[a] with w[a][b] == 0."""
    color = [0] * n

    def dfs(a):
        color[a] = 1
        for b in E[a]:
            if w[a][b] == 0:
                if color[b] == 1 or (color[b] == 0 and dfs(b)):
                    return True
        color[a] = 2
        return False

    return any(color[a] == 0 and dfs(a) for a in range(n))


def edges(n, E, Max, s):
    """SPGame.edge: u in E[v], and u == s[v] if v is a Max vertex."""
    return [[u for u in E[v] if (v not in Max or u == s[v])] for v in range(n)]


def d_bf(n, E, w, Max, tgt, s):
    """SPGame.d by Bellman-Ford: least weight of a path (edge-list) from v to tgt."""
    G = edges(n, E, Max, s)
    d = [INF] * n
    d[tgt] = 0
    for _ in range(n + 1):
        for v in range(n):
            for u in G[v]:
                if w[v][u] + d[u] < d[v]:
                    d[v] = w[v][u] + d[u]
    return d


def d_enum(n, E, w, Max, tgt, s):
    """SPGame.d by the definition: the least weight over all simple paths to tgt.
    PathW.nil is the empty path at tgt (weight 0); PathW.cons prepends an edge."""
    G = edges(n, E, Max, s)
    best = [INF] * n

    def walk(v, seen, acc, start):
        if v == tgt:
            best[start] = min(best[start], acc)
            # a path may pass through tgt and return to it, but that only adds weight >= 0
            return
        for u in G[v]:
            if u not in seen:
                walk(u, seen | {u}, acc + w[v][u], start)

    for v in range(n):
        walk(v, {v}, 0, v)
    return best


def howard(n, E, w, Max, d, s, rng):
    """One step: every Max z moves to an edge of largest w + d, keeping its edge if that is one
    of them (SPGame.HowardAt); ties among the best are broken at random."""
    s2 = list(s)
    for z in Max:
        val = lambda y: w[z][y] + d[y]
        best = (min if CTRL else max)(val(y) for y in E[z])
        if val(s[z]) != best:
            s2[z] = rng.choice([y for y in E[z] if val(y) == best])
    return s2


def howard_at(E, w, d, s, s2, z):
    """SPGame.HowardAt, clause by clause."""
    val = lambda y: w[z][y] + d[y]
    c1 = s2[z] in E[z]
    c2 = all(val(y) <= val(s2[z]) for y in E[z])
    keep = s[z] in E[z] and all(val(y) <= val(s[z]) for y in E[z])
    c3 = (not keep) or s2[z] == s[z]
    return c1 and c2 and c3


def gen(rng, nmax):
    n = rng.randint(2, nmax)
    tgt = 0
    Max = {v for v in range(1, n) if rng.random() < 0.5}  # tgt is not a Max vertex
    upward = rng.random() < 0.5
    wts = [0, 0, 1, 1, 2, 3, 5]
    while True:
        E = []
        for v in range(n):
            k = rng.randint(1 if v in Max else 0, min(n, 4))
            E.append(sorted(rng.sample(range(n), k)))
        w = [[0] * n for _ in range(n)]
        for v in range(n):
            for u in E[v]:
                x = rng.choice(wts)
                if x == 0 and upward and not u > v:
                    x = 1
                w[v][u] = x
        if not zero_cycle(n, E, w):
            return n, E, w, Max, tgt


def main():
    seed, games, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = random.Random(seed)
    cnt = dict(dfail=0, hypfail=0, boundfail=0, c2fail=0, lastfail=0)
    vertices = steps = runs1 = maxT = 0
    hist = {}
    for _ in range(games):
        n, E, w, Max, tgt = gen(rng, nmax)
        s = [rng.choice(E[v]) if v in Max else v for v in range(n)]
        run, ds = [s], []
        while True:
            d = d_bf(n, E, w, Max, tgt, run[-1])
            if n <= 7:
                de = d_enum(n, E, w, Max, tgt, run[-1])
                cnt["dfail"] += sum(1 for v in range(n) if d[v] != de[v])
            vertices += n
            ds.append(d)
            nxt = howard(n, E, w, Max, d, run[-1], rng)
            if nxt == run[-1] or len(run) > 10 * n * n * n:
                break
            run.append(nxt)
        T = len(run) - 1
        hist[T] = hist.get(T, 0) + 1
        maxT = max(maxT, T)
        runs1 += T >= 1
        # hypotheses of AbsStatement
        ok = not zero_cycle(n, E, w) and tgt not in Max
        ok = ok and all(run[t][z] in E[z] for t in range(T + 1) for z in Max)
        ok = ok and all(run[t][v] == run[0][v] for t in range(T + 1) for v in range(n) if v not in Max)
        ok = ok and all(howard_at(E, w, ds[t], run[t], run[t + 1], z) for t in range(T) for z in Max)
        ok = ok and all(run[t + 1] != run[t] for t in range(T))
        if not ok:
            cnt["hypfail"] += 1
            if not CTRL:
                continue  # the control goes on: it shows that the conclusions can fail
        # conclusion (1)
        if T > sum(len(E[z]) for z in Max) * n:
            cnt["boundfail"] += 1
        # conclusion (2), for every t < T
        for t in range(T):
            steps += 1
            lag = [u for u in range(n) if ds[t][u] != ds[T][u]]
            good = any(
                ds[t][v] != ds[T][v]
                and all(ds[t][v] <= ds[t][u] for u in lag)
                and ds[t][v] < ds[t + 1][v]
                for v in range(n)
            )
            if not good:
                cnt["c2fail"] += 1
                if t == T - 1:
                    cnt["lastfail"] += 1
    print(
        f"abscheck seed {seed} games {games} nmax {nmax} ctrl {int(CTRL)}: "
        f"states-vertices {vertices} steps {steps} runs with T>=1 {runs1} maxT {maxT} "
        + " ".join(f"{k} {v}" for k, v in cnt.items())
    )
    print("T histogram: " + " ".join(f"{k}:{hist[k]}" for k in sorted(hist)))


if __name__ == "__main__":
    main()
