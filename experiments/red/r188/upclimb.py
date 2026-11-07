#!/usr/bin/env python3
"""L-RED R188 UPCLIMB: L-NEW box 139 recipe class on the 2-wide deg-2 LADDERBF ladder (option k -> vertex k one level down): every
Xi-target points UP (a mover of strictly higher level; top level -> X), beta ranks ordered by owner level (lower level = more
significant; UPDOM=1: higher level more significant) with free order inside a level, free parities, gate indices and start. Climb on run length T. Usage: upclimb.py d iters seed OUT"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal, rel
d, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
N = 2 * d; lev = [v // 2 for v in range(N)]
def ranks(order):   # order: list of faces (v,k) per level permutation -> br (higher rank = more significant), lower level first
    br = [0] * (2 * N); r = 2 * N - 1
    for l in (range(d - 1, -1, -1) if os.environ.get('UPDOM') == '1' else range(d)):
        for f in order[l]: br[f] = r; r -= 1
    return br
def rand():
    up = lambda v: [u for u in range(N) if lev[u] > lev[v]]
    G = dict(N=N, lev=lev, deg=2, opts=[[[-1 if lev[v] == 0 else 2 * (lev[v] - 1) + k, rng.choice(up(v)) if up(v) else -1, 2 * v + k] for k in (0, 1)] for v in range(N)])
    G["order"] = [rng.sample([2 * v + k for v in range(N) if lev[v] == l for k in (0, 1)], 4) for l in range(d)]
    g = list(range(2 * N)); rng.shuffle(g); G["gate"] = [g[2 * v:2 * v + 2] for v in range(N)]
    G["bp"] = [rng.randint(0, 1) for _ in range(2 * N)]; G["start"] = [rng.randint(0, 1) for _ in range(N)]; G["br"] = ranks(G["order"]); return G
def mut(G):
    H_ = json.loads(json.dumps(G)); r = rng.random(); v = rng.randrange(N); k = rng.randrange(2)
    if r < 0.3:
        up = [u for u in range(N) if lev[u] > lev[v]]
        if up: H_["opts"][v][k][1] = rng.choice(up)
    elif r < 0.5:
        o = H_["order"][lev[v]]; i, j = rng.randrange(4), rng.randrange(4); o[i], o[j] = o[j], o[i]; H_["br"] = ranks(H_["order"])
    elif r < 0.65: H_["bp"][rng.randrange(2 * N)] ^= 1
    elif r < 0.9:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(2), rng.randrange(2)
        H_["gate"][a][ka], H_["gate"][b][kb] = H_["gate"][b][kb], H_["gate"][a][ka]
    else: H_["start"][v] ^= 1
    return H_
def score(G):
    S, _ = ideal.traj(G, cap=3000); return len(S) - 1
best = None
for rs in range(10):
    G = rand(); s = score(G)
    for it in range(iters // 10):
        H_ = mut(G); t = score(H_)
        if t >= s: G, s = H_, t
    if best is None or s > best[0]: best = (s, G); json.dump(G, open(out, "w"))
S, _ = ideal.traj(best[1]); print("UP d", d, "BEST", best[0], rel.stats(best[1], S))
