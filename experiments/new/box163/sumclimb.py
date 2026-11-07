#!/usr/bin/env python3
"""L-NEW box 163 (DATA, lower bounds only): hill-climb over ISO R197 ladders with m + 1 levels to maximise an objective of the
per-genome exact values V_k(G) := max over U-starts (level 0 at (0, 0)) of the box 162 V_k (k flips). Objective (env OBJ):
  SUM  = V_0 + V_1   (CONJECTURE SUM: <= 2 T^R(m) + 1)      V1 = V_1      V2 = V_2
(env START=genome.json: every restart starts from that genome)
Usage: sumclimb.py m seed iters restarts  -> prints the best value and writes out/climb_<OBJ>_m<m>_s<seed>.json"""
import os, sys, json, random
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box162", "flipcheck.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read(), ns); Gen, Vk, rand_lr, allstates = ns["Gen"], ns["Vk"], ns["rand_lr"], ns["allstates"]
OBJ = os.environ.get("OBJ", "SUM")
def vals(G):
    g = Gen(G); N = G["N"]; v = [0, 0, 0]
    for s in allstates(N):
        if s[:2] != (0, 0): continue
        for k in range(3 if OBJ in ("V2", "SUM2") else 2): v[k] = max(v[k], Vk(g, s, k))
    return v
def score(v): return {"SUM": v[0] + v[1], "SUM2": v[0] + v[2], "V1": v[1], "V2": v[2]}[OBJ]
def mutate(G, rng):
    G = json.loads(json.dumps(G)); N = G["N"]; G.setdefault("xorder", ns["ns"]["topo"](G)); pos = {v: i for i, v in enumerate(G["xorder"])}; r = rng.random()
    if r < 0.4:
        x = rng.randrange(N); k = rng.randrange(2); later = [v for v in range(N) if pos[v] > pos[x] and G["lev"][v] > 0]
        G["opts"][x][k][1] = rng.choice(later + [-1]) if later else -1
    elif r < 0.7:
        i, j = rng.sample(range(2 * N), 2); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.85: i = rng.randrange(2 * N); G["bp"][i] ^= 1
    else:
        x, y = rng.sample(range(2, N), 2); k = rng.randrange(2); G["gate"][x][k], G["gate"][y][k] = G["gate"][y][k], G["gate"][x][k]
    return G
m, seed, iters, rest = map(int, sys.argv[1:5]); rng = random.Random(seed); best = (-1, None, None)
for r in range(rest):
    G = json.load(open(os.environ["START"])) if os.environ.get("START") else rand_lr(m + 1, rng, True); v = vals(G); sc = score(v)
    for it in range(iters):
        G2 = mutate(G, rng); v2 = vals(G2); s2 = score(v2)
        if s2 >= sc: G, v, sc = G2, v2, s2
    if sc > best[0]: best = (sc, v, G)
os.makedirs(os.path.join(H, "out"), exist_ok=True)
json.dump(best[2], open(os.path.join(H, "out", f"climb_{OBJ}_m{m}_s{seed}.json"), "w"))
print(f"CLIMB OBJ {OBJ} m {m} seed {seed} best {best[0]} V {best[1]}", flush=True)
