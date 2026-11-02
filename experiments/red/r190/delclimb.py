#!/usr/bin/env python3
"""L-RED R190 DELCLIMB: hill-climb IDEAL-ACYC W-ladders of width w, degree D (option k of a level-l >= 1 mover has W-target
w(l-1) + (k mod w)), acyclic Xi (forward in a mutable pi), scored by DELSTEPS (L-NEW box 143): steps whose LEAST-level mover is
DELAYED, i.e. moves at a step where the key order of the level below (the ranking of its w movers) did not change; level-0 movers are
never delayed. Score (DELSTEPS, L). Usage: delclimb.py d w D iters seed out.json"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
def stats(G, w):
    S, why = ideal.traj(G, cap=5000); N = G["N"]; lev = G["lev"]; d = max(lev) + 1; O = G["opts"]
    def keys(s):
        key = [None] * N
        for v in sorted(range(N), key=lambda v: lev[v]):
            wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
        return key
    R = [[tuple(sorted(range(w * l, w * l + w), key=lambda v: K[v])) for l in range(d)] for K in (keys(s) for s in S)]
    dels = 0; per = [0] * d
    for t in range(1, len(S)):
        mv = [v for v in range(N) if S[t][v] != S[t - 1][v]]; l = min(lev[v] for v in mv)
        if l >= 1 and R[t][l - 1] == R[t - 1][l - 1]: dels += 1; per[l] += 1
    return len(S) - 1, dels, per
def rand(d, w, D, rng):
    N = w * d; lev = [v // w for v in range(N)]; pi = list(range(N)); rng.shuffle(pi); M = N * D
    opts = [[[-1 if lev[v] == 0 else w * (lev[v] - 1) + (k % w), rng.choice([u for u in range(N) if pi[u] > pi[v]] + [-1]), D * v + k] for k in range(D)] for v in range(N)]
    g = list(range(M)); rng.shuffle(g); b = list(range(M)); rng.shuffle(b)
    return dict(N=N, lev=lev, opts=opts, deg=D, pi=pi, gate=[g[D * v:D * v + D] for v in range(N)], br=b,
                bp=[rng.randint(0, 1) for _ in range(M)], start=[rng.randrange(D) for _ in range(N)])
def mutate(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; D = H["deg"]; M = N * D; pi = H["pi"]; r = rng.random(); v = rng.randrange(N); k = rng.randrange(D)
    if r < 0.35: H["opts"][v][k][1] = rng.choice([u for u in range(N) if pi[u] > pi[v]] + [-1])
    elif r < 0.45:
        a, b = rng.randrange(N), rng.randrange(N); pi[a], pi[b] = pi[b], pi[a]
        if any(xt >= 0 and pi[xt] <= pi[u] for u in range(N) for (_, xt, _) in H["opts"][u]): return G
    elif r < 0.6: a, b = rng.randrange(M), rng.randrange(M); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.7: H["bp"][rng.randrange(M)] ^= 1
    elif r < 0.9:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(D), rng.randrange(D); H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    else: H["start"][v] = rng.randrange(D)
    return H
if __name__ == "__main__":
    d, w, D, it, seed = map(int, sys.argv[1:6]); out = sys.argv[6]; rng = random.Random(seed)
    G = rand(d, w, D, rng); L, ds, per = stats(G, w); sc = (ds, L); best = (sc, G, per)
    for i in range(it):
        if i % 20000 == 0 and i: G = json.loads(json.dumps(best[1])); sc = best[0]
        H2 = mutate(G, rng); L, ds, per = stats(H2, w)
        if (ds, L) >= sc: G, sc = H2, (ds, L)
        if sc > best[0]: best = (sc, json.loads(json.dumps(G)), per); json.dump(G, open(out, "w"))
    print(f"DELCLIMB d {d} w {w} D {D} seed {seed} DELSTEPS {best[0][0]} L {best[0][1]} per level {best[2]}")
