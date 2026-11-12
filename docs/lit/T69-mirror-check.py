#!/usr/bin/env python3
"""T69 Addendum A (L-LIT): Howard on shortest-path games with weights >= 0, in both orientations. No code of another lane.
Game: vertices 0..n-1, a target, every vertex owned by Max or Min, integer weights >= 0, no cycle of total weight 0
(random games: zero-weight edges only from a lower to a higher index).
MIRROR: Howard for MIN (every Min vertex moves to an edge of least w + V(y), keeps its edge if it is one of them); Max answers
        exactly (INF if Max can avoid the target). Values fall.
ABS:    Howard for MAX (every Max vertex moves to an edge of largest w + d(y), keeps its edge if it is one of them); Min answers
        with shortest paths. Values rise. (L-NEW box 208 section 10, orientation of Statement ABS.)
Usage (from anywhere; python3 -I):
  T69-mirror-check.py rand SEED GAMES NMAX BRUTE   random games with 3..NMAX vertices; brute-force optimum when n <= BRUTE
  T69-mirror-check.py ctrl M                       the designed instance: Min vertex v, Max chain a_1..a_M, target
Counters of rand (all must be 0):
  mono_m / mono_a  a value rises in a MIRROR run / falls in an ABS run          (unit: consecutive states)
  bound_m          a MIRROR run has more than n - 1 steps                        (unit: games)
  order_m          MIRROR: at state j a vertex whose optimal value is below the (j+1)-th smallest finite optimal value is not
                   yet at its optimal value (Dijkstra-order settling)           (unit: (state, vertex))
  opt_m / opt_a    the final values differ from the brute-force optimum         (unit: games with n <= BRUTE)
Descriptive: gt_n_a = ABS runs with more than n steps; the longest runs.
Control for order_m: `ctrl M` applies the same test to the ABS run of the designed instance, where it must fire (M >= 4).
Random games give short runs (a few steps): the rand sets test the logic state by state, not any growth.
"""
import sys, random, itertools
INF = float('inf')

def gen(rng, n, wts):
    owner = [rng.random() < 0.5 for _ in range(n)]          # True = Max
    E = [[] for _ in range(n)]
    t = n - 1
    for v in range(n - 1):
        k = min(rng.randint(1, 3), n - 1)
        succ = set()
        while len(succ) < k:
            y = rng.randrange(n)
            if y != v: succ.add(y)
        for y in sorted(succ):
            w = rng.choice(wts)
            if w == 0 and y < v: w = rng.choice([x for x in wts if x > 0])
            E[v].append((y, w))
    return owner, E, t

def best_response_max(n, t, owner, E, mu):
    """Min plays mu; Max maximises cost to t (INF if Max can avoid t forever)."""
    G = [[] if v == t else (E[v] if owner[v] else [E[v][mu[v]]]) for v in range(n)]
    # INF iff v can reach a cycle or cannot reach t. Compute by DFS-based longest path with cycle detection.
    state = [0] * n; val = [None] * n
    sys.setrecursionlimit(10000)
    def go(v):
        if v == t: return 0
        if state[v] == 2: return val[v]
        if state[v] == 1: return INF            # cycle
        state[v] = 1
        best = -1
        for (y, w) in G[v]:
            r = go(y)
            c = INF if r == INF else w + r
            if c > best: best = c
        state[v] = 2; val[v] = best
        return best
    # a vertex found on a cycle gets INF; vertices finished earlier with a path into the cycle also INF (max over succ) - but
    # a vertex 'in progress' revisited returns INF to its predecessor, and the in-progress vertex itself then gets INF: fine.
    return [go(v) for v in range(n)]

def best_response_min(n, t, owner, E, s):
    """Max plays s; Min minimises cost to t: Bellman-Ford on nonneg weights (n rounds)."""
    d = [INF] * n; d[t] = 0
    for _ in range(n):
        ch = False
        for v in range(n):
            if v == t: continue
            es = [E[v][s[v]]] if owner[v] else E[v]
            b = min((w + d[y] for (y, w) in es), default=INF)
            if b < d[v]: d[v] = b; ch = True
        if not ch: break
    return d

def howard(n, t, owner, E, improver_is_max, start):
    strat = list(start); hist = []
    while True:
        V = best_response_min(n, t, owner, E, strat) if improver_is_max else best_response_max(n, t, owner, E, strat)
        hist.append(V)
        new = list(strat); changed = False
        for v in range(n):
            if v == t or owner[v] != improver_is_max: continue
            cur = E[v][strat[v]]; curv = cur[1] + V[cur[0]]
            vals = [w + V[y] for (y, w) in E[v]]
            b = max(vals) if improver_is_max else min(vals)
            if (b > curv) if improver_is_max else (b < curv):
                new[v] = vals.index(b); changed = True
        if not changed: return hist
        strat = new
        if len(hist) > 10000: raise RuntimeError("no termination")

def order_violations(n, hist):
    """Dijkstra-order settling: at state j every vertex whose final value is strictly below the (j+1)-th smallest finite
    final value must already have its final value. Returns the number of (state, vertex) pairs violating this."""
    fin_val = hist[-1]
    fin = sorted([v for v in range(n) if fin_val[v] < INF], key=lambda v: fin_val[v])
    bad = 0
    for j in range(min(len(hist), len(fin))):
        thr = fin_val[fin[j]]
        for v in fin:
            if fin_val[v] < thr and hist[j][v] != fin_val[v]: bad += 1
    return bad

def brute(n, t, owner, E):
    """optimal values = max over Max strategies of Min's best response (pointwise max exists)."""
    mx = [v for v in range(n) if v != t and owner[v]]
    best = None
    for choice in itertools.product(*[range(len(E[v])) for v in mx]):
        s = [0] * n
        for v, c in zip(mx, choice): s[v] = c
        d = best_response_min(n, t, owner, E, s)
        best = d if best is None else [max(a, b) for a, b in zip(best, d)]
    return best

def rand(seed, games, nmax, bl):
    rng = random.Random(seed); wts = [0, 1, 2, 4, 8, 16, 32]
    cnt = dict(mono_m=0, bound_m=0, order_m=0, opt_m=0, mono_a=0, opt_a=0, gt_n_a=0)
    maxit_m = 0; maxit_a = 0; maxratio_a = 0.0; worst = None
    for g in range(games):
        n = rng.randint(3, nmax)
        owner, E, t = gen(rng, n, wts)
        start = [rng.randrange(len(E[v])) if v != t else 0 for v in range(n)]
        hm = howard(n, t, owner, E, False, start)       # MIRROR
        ha = howard(n, t, owner, E, True, start)        # ABS
        steps_m = len(hm) - 1; steps_a = len(ha) - 1
        maxit_m = max(maxit_m, steps_m)
        if steps_a > maxit_a: maxit_a = steps_a
        if steps_a / n > maxratio_a: maxratio_a = steps_a / n; worst = (n, steps_a)
        for a, b in zip(hm, hm[1:]):
            if any(y > x for x, y in zip(a, b)): cnt['mono_m'] += 1
        for a, b in zip(ha, ha[1:]):
            if any(y < x for x, y in zip(a, b)): cnt['mono_a'] += 1
        if steps_m > n - 1: cnt['bound_m'] += 1
        if steps_a > n: cnt['gt_n_a'] += 1
        cnt['order_m'] += order_violations(n, hm)
        if n <= bl:
            b = brute(n, t, owner, E)
            if b != hm[-1]: cnt['opt_m'] += 1
            if b != ha[-1]: cnt['opt_a'] += 1
    print(f"seed {seed} games {games} nmax {nmax}: {cnt} max steps MIRROR {maxit_m}, ABS {maxit_a}, ABS worst steps/n {maxratio_a:.2f} at (n, steps) {worst}")

def ctrl(m):
    """v = 0 (Min): v -> t (10), v -> a_1 (0). a_i = i (Max), i < m: a_i -> t (m - i + 1), a_i -> a_(i+1) (0). a_m -> t (100)."""
    n = m + 2; t = m + 1
    owner = [False] + [True] * m + [False]
    E = [[] for _ in range(n)]
    E[0] = [(t, 10), (1, 0)]
    for i in range(1, m): E[i] = [(t, m - i + 1), (i + 1, 0)]
    E[m] = [(t, 100)]
    start = [0] * n
    ha = howard(n, t, owner, E, True, start); hm = howard(n, t, owner, E, False, start)
    opt = ha[-1]
    first = next(j for j, h in enumerate(ha) if h[0] == opt[0])
    print(f"ctrl m {m} n {n}: ABS steps {len(ha) - 1}, MIRROR steps {len(hm) - 1}, final values equal {ha[-1] == hm[-1]}")
    print(f"  optimal values: v {opt[0]}, a_1 {opt[1]}, target {opt[t]}; v has the second-smallest optimal value")
    print(f"  ABS: value of v per state {[h[0] for h in ha]}; v first at its optimal value at state {first}")
    print(f"  MIRROR: value of v per state {[h[0] for h in hm]}")
    print(f"  Dijkstra-order violations: ABS run {order_violations(n, ha)} (CONTROL: must be > 0 for m >= 4), "
          f"MIRROR run {order_violations(n, hm)} (must be 0)")

if __name__ == "__main__":
    if sys.argv[1] == "rand": rand(*map(int, sys.argv[2:6]))
    elif sys.argv[1] == "ctrl": ctrl(int(sys.argv[2]))
    else: sys.exit(__doc__)
