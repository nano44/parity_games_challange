#!/usr/bin/env python3
"""L-RED R189 LAGCLIMB: hill-climb on the 2-wide deg-2 LADDER (option k of a level-l mover has W-target 2(l-1)+k; c_W at level 0),
acyclic Xi-graph (forward in a permutation pi), scoring LAG EVENTS: a flip of L_(l-1) (the key-smaller level-(l-1) mover) at step t
after which BOTH level-l movers move, at DIFFERENT steps, before the next flip of L_(l-1) (box 140 TOWARD-L: each moves at most once
there). Score = (sum over levels of 4^l * lag events at level l, run length). Usage: lagclimb.py d iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "..", "r187"), os.path.join(H, "..", "..", "r178")]
import ideal
def lagstats(G):
    S, why = ideal.traj(G, cap=5000); N = G["N"]; lev = G["lev"]; d = max(lev) + 1; O = G["opts"]
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return key
    Ls = [[min((2 * l, 2 * l + 1), key=lambda v: K[v]) for l in range(d)] for K in (keys(s) for s in S)]
    lag = [0] * d
    for l in range(1, d):
        fl = [t for t in range(1, len(S)) if Ls[t][l - 1] != Ls[t - 1][l - 1]] + [len(S)]
        for a, b in zip(fl, fl[1:]):
            mu = [t for t in range(a, b) if S[t][2 * l] != S[t - 1][2 * l]]; mv = [t for t in range(a, b) if S[t][2 * l + 1] != S[t - 1][2 * l + 1]]
            if mu and mv and mu[0] != mv[0]: lag[l] += 1
    return len(S) - 1, lag
def rand(d, rng):
    N = 2 * d; lev = [v // 2 for v in range(N)]; pi = list(range(N)); rng.shuffle(pi)
    opts = [[[-1 if lev[v] == 0 else 2 * (lev[v] - 1) + k, -1, 2 * v + k] for k in (0, 1)] for v in range(N)]
    G = dict(N=N, lev=lev, opts=opts, deg=2, pi=pi, gate=None, br=None, bp=[rng.randint(0, 1) for _ in range(2 * N)], start=[rng.randint(0, 1) for _ in range(N)])
    g = list(range(2 * N)); rng.shuffle(g); G["gate"] = [g[2 * v:2 * v + 2] for v in range(N)]; b = list(range(2 * N)); rng.shuffle(b); G["br"] = b
    for v in range(N):
        for k in (0, 1): G["opts"][v][k][1] = rng.choice([u for u in range(N) if pi[u] > pi[v]] + [-1])
    return G
def mutate(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; pi = H["pi"]; r = rng.random(); v = rng.randrange(N); k = rng.randrange(2)
    if r < 0.35: H["opts"][v][k][1] = rng.choice([u for u in range(N) if pi[u] > pi[v]] + [-1])
    elif r < 0.45:
        a, b = rng.randrange(N), rng.randrange(N); pi[a], pi[b] = pi[b], pi[a]
        if any(xt >= 0 and pi[xt] <= pi[u] for u in range(N) for (_, xt, _) in H["opts"][u]): return G
    elif r < 0.6: a, b = rng.randrange(2 * N), rng.randrange(2 * N); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.7: H["bp"][rng.randrange(2 * N)] ^= 1
    elif r < 0.9:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(2), rng.randrange(2); H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    else: H["start"][v] ^= 1
    return H
def score(G):
    L, lag = lagstats(G); return (sum(4 ** l * x for l, x in enumerate(lag)), L), lag
if __name__ == "__main__":
    d, it, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    G = rand(d, rng); sc, lag = score(G); best = (sc, G, lag)
    for i in range(it):
        if i % 20000 == 0 and i: G = json.loads(json.dumps(best[1]))
        H = mutate(G, rng); s2, l2 = score(H)
        if s2 >= sc: G, sc, lag = H, s2, l2
        if sc > best[0]: best = (sc, json.loads(json.dumps(G)), lag); json.dump(G, open(out, "w"))
    print(f"LAGCLIMB d {d} seed {seed} best score {best[0][0]} L {best[0][1]} lag events per level {best[2]}")
