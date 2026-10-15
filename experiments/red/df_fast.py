#!/usr/bin/env python3
"""Question DF, one-player acyclic sink games, fast exact search (L-RED). Vertices 1..n, successors among smaller indices
(sink 0), all Even; val(u) = signed weight of the path set (even priorities +2^rank, odd -2^rank; larger = better), no
length needed (acyclic, distinct sets). Longest DF run and longest unrestricted run by memoised DFS over all strategies.
Usage: df_fast.py --n 8 [--deg 3] [--restarts 5] [--steps 200] [--seed 0]"""
import sys, random, argparse, itertools
sys.setrecursionlimit(1 << 20)
ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=7); ap.add_argument("--deg", type=int, default=3)
ap.add_argument("--restarts", type=int, default=5); ap.add_argument("--steps", type=int, default=200); ap.add_argument("--seed", type=int, default=0)
a = ap.parse_args(); rng = random.Random(a.seed); n = a.n


def rand_game():
    prio = [1] + rng.sample(range(2, 3 * n + 2), n)
    succ = [[0]] + [sorted(rng.sample(range(0, v), min(a.deg, v))) for v in range(1, n + 1)]
    return prio, succ


def mutate(g):
    prio, succ = list(g[0]), [list(s) for s in g[1]]
    v = rng.randrange(1, n + 1)
    if rng.random() < 0.3:
        u = rng.randrange(1, n + 1); prio[v], prio[u] = prio[u], prio[v]
    else:
        pool = [x for x in range(0, v) if x not in succ[v]]
        if pool:
            i = rng.randrange(len(succ[v])); succ[v][i] = rng.choice(pool); succ[v] = sorted(set(succ[v]))
    return prio, succ


def analyse(g):
    prio, succ = g
    w = [0] + [((1 << prio[v]) if prio[v] % 2 == 0 else -(1 << prio[v])) for v in range(1, n + 1)]
    choices = [range(len(succ[v])) for v in range(1, n + 1)]
    df_next = {}; all_next = {}
    for c in itertools.product(*choices):
        s = (0,) + tuple(succ[v][c[v - 1]] for v in range(1, n + 1))      # s[v] = successor
        val = [0] * (n + 1)
        for v in range(1, n + 1): val[v] = w[v] + val[s[v]]             # successors have smaller index
        imp = [(v, x) for v in range(1, n + 1) for x in succ[v] if x != s[v] and val[x] > val[s[v]]]
        impv = {v for v, _ in imp}; alls = []; dfs = []
        for v, x in imp:
            t = list(s); t[v] = x; t = tuple(t); alls.append(t)
            y = s[v]; ok = True
            while y != 0:
                if y in impv: ok = False; break
                y = s[y]
            if ok: dfs.append(t)
        df_next[s] = dfs; all_next[s] = alls
    memo = {}
    def longest(s, nxt):
        if s in memo: return memo[s]
        memo[s] = 0; memo[s] = max([longest(t, nxt) + 1 for t in nxt[s]] + [0]); return memo[s]
    best_df = max(longest(s, df_next) for s in df_next); memo.clear()
    best_all = max(longest(s, all_next) for s in all_next)
    return best_df, best_all


best = (-1, None)
for r in range(a.restarts):
    g = rand_game(); sc = analyse(g)
    for k in range(a.steps):
        g2 = mutate(g); sc2 = analyse(g2)
        if sc2[0] >= sc[0]: g, sc = g2, sc2
    if sc[0] > best[0]: best = (sc[0], (g, sc))
    print(f"n={n} deg={a.deg} restart {r}: DF {sc[0]} unrestricted {sc[1]}", flush=True)
g, sc = best[1]
print(f"BEST n={n} deg={a.deg}: DF {sc[0]} unrestricted {sc[1]}; prio {g[0]} succ {g[1]}")
