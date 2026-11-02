#!/usr/bin/env python3
"""L-NEW box 140: hill-climb inside the LADDERBF-up shape of the IDEAL-ACYC model (box 139 §3 recipe). 2-wide complete W-ladder, levels
0..d-1, movers 2l, 2l+1 at level l; every mover has deg 2: option 0 has W-target mover 2(l-1), option 1 has W-target 2(l-1)+1 (c_W at
level 0); every Xi-target is a mover of a STRICTLY HIGHER level or T (so the Xi-graph is acyclic). Free: Xi-targets, beta ranks and
parities, gate indices, start. Simulator = box139/paths.py run() (R178 §1 rule). SCORE = steps of the run (FL length; a stuck step ends
it). Prints improvements and the best genome (JSON). Usage: upclimb.py d iters seed out.json"""
import sys, os, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box139"))
import importlib.util
spec = importlib.util.spec_from_file_location("paths", os.path.join(HERE, "..", "box139", "paths.py"))
src = open(os.path.join(HERE, "..", "box139", "paths.py")).read().split("for path in sys.argv[1:]:")[0]
ns = {"__file__": os.path.join(HERE, "..", "box139", "paths.py")}; exec(src, ns); run = ns["run"]
def rand(d, rng):
    N = 2 * d; lev = [i // 2 for i in range(N)]; opts = []; b = 0
    for v in range(N):
        l = lev[v]; hi = [u for u in range(N) if lev[u] > l] + [-1]; o = []
        for k in range(2):
            o.append([-1 if l == 0 else 2 * (l - 1) + k, rng.choice(hi), b]); b += 1
        opts.append(o)
    br = list(range(b)); rng.shuffle(br); gates = list(range(b)); rng.shuffle(gates)
    return dict(N=N, lev=lev, opts=opts, gate=[gates[2 * v:2 * v + 2] for v in range(N)], br=br, bp=[rng.randint(0, 1) for _ in range(b)],
                start=[rng.randrange(2) for _ in range(N)], deg=2)
def mut(G, rng):
    H = json.loads(json.dumps(G)); N = H["N"]; r = rng.random(); v = rng.randrange(N); k = rng.randrange(2); l = H["lev"][v]
    if r < 0.3: H["opts"][v][k][1] = rng.choice([u for u in range(N) if H["lev"][u] > l] + [-1])
    elif r < 0.5: i, j = rng.randrange(len(H["br"])), rng.randrange(len(H["br"])); H["br"][i], H["br"][j] = H["br"][j], H["br"][i]
    elif r < 0.6: i = rng.randrange(len(H["bp"])); H["bp"][i] ^= 1
    elif r < 0.85:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(2), rng.randrange(2)
        H["gate"][a][ka], H["gate"][b][kb] = H["gate"][b][kb], H["gate"][a][ka]
    else: H["start"][v] ^= 1
    return H
def score(G):
    S, CUR, KEY, why = run(G, cap=5000); return len(S) - 1
if __name__ == "__main__":
    d, iters, seed, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    G = rand(d, rng); bs = score(G); restarts = 0
    best = (bs, G)
    for it in range(iters):
        H = mut(G, rng); hs = score(H)
        if hs >= bs:
            G, bs = H, hs
            if bs > best[0]: best = (bs, G); print("IT", it, "SCORE", bs, flush=True); json.dump(G, open(out, "w"))
        if it % 5000 == 4999 and bs < best[0]: G, bs = json.loads(json.dumps(best[1])), best[0]
    print("BEST", best[0], "LADDERBF", 2 * (2 ** (d + 1) - d - 2), flush=True)
