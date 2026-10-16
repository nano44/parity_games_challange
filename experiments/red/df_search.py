#!/usr/bin/env python3
"""Question DF (Lead 14:00Z): longest downstream-first (DF) single-switch improvement run on small sink games, exactly.
A switch (v, w) at sigma is DF if it is improving and no other vertex with an improving edge lies on v's (sigma, tau)-play.
The improvement graph on strategies is acyclic (Friedmann Thm 3.2), so the longest DF run from any start is a longest path
in the DF switch graph, computed by memoised DFS over all strategies; the unrestricted longest run is computed alongside.
Games: sink 0 (Odd, priority 1, self-loop); vertices 1..n with out-degree 2; 'acyclic' = successors have smaller index
(so every play reaches the sink); 'cyclic' = arbitrary successors with the sink reachable; owners all Even (one-player) or
random (two-player).  Hill-climb over games maximising the longest DF run.
Usage: df_search.py --n 5 [--mode one|two] [--graph acyclic|cyclic] [--restarts 10] [--steps 300] [--seed 0] [--deg 2]"""
import sys, os, random, argparse, itertools
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import vj
sys.setrecursionlimit(1 << 16)
ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=5); ap.add_argument("--mode", default="one")
ap.add_argument("--graph", default="acyclic"); ap.add_argument("--restarts", type=int, default=10); ap.add_argument("--steps", type=int, default=300)
ap.add_argument("--seed", type=int, default=0); ap.add_argument("--deg", type=int, default=2); ap.add_argument("--out", default="")
a = ap.parse_args(); rng = random.Random(a.seed); n = a.n


def rand_game():
    while True:
        prio = [1] + rng.sample(range(2, 3 * n + 2), n)
        owner = [1] + [0 if a.mode == "one" else rng.randrange(2) for _ in range(n)]
        succ = [[0]]
        for v in range(1, n + 1):
            pool = list(range(0, v)) if a.graph == "acyclic" else list(range(0, n + 1))
            k = min(a.deg, len(pool)); succ.append(sorted(rng.sample(pool, k)))
        if a.graph == "cyclic" and not sink_reachable(succ): continue
        return prio, owner, succ


def sink_reachable(succ):
    seen = {0}; st = [0]; pred = [[] for _ in succ]
    for v, s in enumerate(succ):
        for w in s: pred[w].append(v)
    while st:
        x = st.pop()
        for y in pred[x]:
            if y not in seen: seen.add(y); st.append(y)
    return len(seen) == len(succ)


def mutate(g):
    prio, owner, succ = list(g[0]), list(g[1]), [list(s) for s in g[2]]
    while True:
        v = rng.randrange(1, n + 1); k = rng.randrange(4)
        if k == 0:
            u = rng.randrange(1, n + 1); prio[v], prio[u] = prio[u], prio[v]
        elif k == 1 and a.mode == "two":
            owner[v] ^= 1
        else:
            pool = [x for x in (range(0, v) if a.graph == "acyclic" else range(0, n + 1)) if x not in succ[v]]
            if not pool: continue
            i = rng.randrange(len(succ[v])); succ[v][i] = rng.choice(pool); succ[v] = sorted(set(succ[v]))
            if len(succ[v]) < 2:
                pool = [x for x in (range(0, v) if a.graph == "acyclic" else range(0, n + 1)) if x not in succ[v]]
                if pool: succ[v] = sorted(succ[v] + [rng.choice(pool)])
        if a.graph == "cyclic" and not sink_reachable(succ): continue
        return prio, owner, succ


def analyse(g):
    """returns (longest DF run, longest unrestricted run, number of strategies)"""
    prio, owner, succ = g; e = vj.VJ(prio, owner, succ)
    evens = [v for v in range(n + 1) if owner[v] == 0]
    choices = [succ[v] for v in evens]
    strategies = []
    for c in itertools.product(*choices):
        s = [-1] * (n + 1)
        for v, w in zip(evens, c): s[v] = w
        strategies.append(tuple(s))
    df_next = {}; all_next = {}
    for s in strategies:
        val, tau = e.evaluate(s); imp = e.improving(s, val)
        impv = {v for v, _ in imp}; dfs = []; alls = []
        for v, w in imp:
            s2 = list(s); s2[v] = w; s2 = tuple(s2); alls.append(s2)
            x = v; seen = set(); ok = True
            while x not in seen:
                if x != v and x in impv: ok = False; break
                seen.add(x); x = s[x] if owner[x] == 0 else tau[x]
            if ok: dfs.append(s2)
        df_next[s] = dfs; all_next[s] = alls
    memo = {}
    def longest(s, nxt):
        if s in memo: return memo[s]
        memo[s] = 0; memo[s] = max([longest(t, nxt) + 1 for t in nxt[s]] + [0]); return memo[s]
    best_df = max(longest(s, df_next) for s in strategies)
    # reconstruct one longest DF run and count switches per vertex
    s0 = max(strategies, key=lambda s: memo[s]); run = [s0]
    while df_next[run[-1]]:
        t = max(df_next[run[-1]], key=lambda t: memo[t])
        if memo[t] + 1 != memo[run[-1]]: break
        run.append(t)
    per = {}
    for s, t in zip(run, run[1:]):
        v = [i for i in range(len(s)) if s[i] != t[i]][0]; per[v] = per.get(v, 0) + 1
    analyse.last_per_vertex = per
    memo.clear()
    best_all = max(longest(s, all_next) for s in strategies)
    return best_df, best_all, len(strategies)


best = (-1, None)
for r in range(a.restarts):
    g = rand_game(); sc = analyse(g)
    for k in range(a.steps):
        g2 = mutate(g); sc2 = analyse(g2)
        if sc2[0] >= sc[0]: g, sc = g2, sc2
    if sc[0] > best[0]: best = (sc[0], (g, sc))
    print(f"n={n} {a.mode} {a.graph} restart {r}: longest DF run {sc[0]} (unrestricted {sc[1]}, {sc[2]} strategies)", flush=True)
g, sc = best[1]
analyse(g); print(f"BEST n={n} {a.mode} {a.graph}: DF {sc[0]} unrestricted {sc[1]}; prio {g[0]} owner {g[1]} succ {g[2]}; DF switches per vertex {analyse.last_per_vertex}; out-degrees {[len(x) for x in g[2]]}")
if a.out:
    with open(a.out, "w") as f:
        f.write(f"parity {n};\n" + "".join(f"{v} {g[0][v]} {g[1][v]} {','.join(map(str, g[2][v]))};\n" for v in range(n + 1)))
