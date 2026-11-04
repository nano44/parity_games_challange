#!/usr/bin/env python3
"""box 156: DATA (lower bounds only). Simulated annealing over 2-wide degree-2 ladders with d levels (N = 2d): genome + start mutated
together, objective T of the run from the genome start (box 150 simulator). Seed: random, or a smaller genome (SEED=file) whose levels
are kept, with 2 new movers added on top (level d-1). Any xorder (Xi-targets: X or a later mover in xorder).
Usage: ladclimb.py d SEED ITERS [seedfile] -> writes wit/lad_d<d>_s<SEED>.json at every improvement"""
import sys, json, random, math, copy
from val import ns
Gen = ns["Gen"]
d, seed, iters = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); N = 2 * d; M = 2 * N; rng = random.Random(seed)
lev = [x // 2 for x in range(N)]
def rnd():
    xo = list(range(N)); rng.shuffle(xo)
    return {"xo": xo, "wt": [[rng.choice([2 * (lev[x] - 1), 2 * (lev[x] - 1) + 1]) if lev[x] else -1 for k in range(2)] for x in range(N)],
            "xt": [[-1, -1] for _ in range(N)], "rk": rng.sample(range(M), M), "sg": [rng.randint(0, 1) for _ in range(M)],
            "gt": rng.sample(range(M), M), "st": [rng.randint(0, 1) for _ in range(N)]}
def later(G, x): p = G["xo"].index(x); return G["xo"][p + 1:]
def legal(G):
    for x in range(N):
        for k in range(2):
            if G["xt"][x][k] >= 0 and G["xt"][x][k] not in later(G, x): G["xt"][x][k] = -1
def build(G):
    opts = [[[G["wt"][x][k], G["xt"][x][k], 2 * x + k] for k in range(2)] for x in range(N)]
    return {"N": N, "lev": lev, "opts": opts, "gate": [[G["gt"][2 * x], G["gt"][2 * x + 1]] for x in range(N)], "br": G["rk"],
            "bp": G["sg"], "start": G["st"], "xorder": G["xo"]}
def score(G):
    try: S, _ = Gen(build(G)).run(G["st"], cap=10000); return len(S) - 1
    except RuntimeError: return -1
def mut(G):
    G = copy.deepcopy(G); r = rng.random(); x = rng.randrange(N); k = rng.randrange(2)
    if r < 0.2: G["xt"][x][k] = rng.choice([-1] + later(G, x))
    elif r < 0.3 and lev[x]: G["wt"][x][k] ^= 1 if G["wt"][x][k] % 2 == 0 else 0; G["wt"][x][k] = 2 * (lev[x] - 1) + rng.randint(0, 1)
    elif r < 0.45: i, j = rng.sample(range(M), 2); G["rk"][i], G["rk"][j] = G["rk"][j], G["rk"][i]
    elif r < 0.55: G["sg"][rng.randrange(M)] ^= 1
    elif r < 0.7: i, j = rng.sample(range(M), 2); G["gt"][i], G["gt"][j] = G["gt"][j], G["gt"][i]
    elif r < 0.8: G["st"][x] ^= 1
    else: i, j = rng.sample(range(N), 2); G["xo"][i], G["xo"][j] = G["xo"][j], G["xo"][i]; legal(G)
    return G
cur = rnd()
if len(sys.argv) > 4:
    H = json.load(open(sys.argv[4])); n0 = H["N"]; assert H["lev"] == [x // 2 for x in range(n0)]
    cur["xo"] = list(H["xorder"]) + [x for x in cur["xo"] if x >= n0]
    for x in range(n0):
        for k in range(2): cur["wt"][x][k] = H["opts"][x][k][0]; cur["xt"][x][k] = H["opts"][x][k][1]
    rk = sorted(range(2 * n0), key=lambda m: H["br"][m]); gt = sorted(range(2 * n0), key=lambda m: H["gate"][m // 2][m % 2])
    # old options keep their relative rank / gate order; new options get the top ranks / gates
    for i, m in enumerate(rk): cur["rk"][m] = i
    for i, m in enumerate(gt): cur["gt"][m] = i
    for i, m in enumerate(range(2 * n0, M)): cur["rk"][m] = 2 * n0 + i; cur["gt"][m] = 2 * n0 + i
    cur["sg"][:2 * n0] = H["bp"]; cur["st"][:n0] = H["start"]; legal(cur)
cs = score(cur); best, bs = cur, cs; temp = 1.0
print("start", cs, flush=True)
for it in range(iters):
    temp = max(0.05, 1.0 - it / iters)
    H = mut(cur); s = score(H)
    if s >= cs or rng.random() < math.exp((s - cs) / temp): cur, cs = H, s
    if s > bs:
        best, bs = H, s; json.dump(build(best), open(f"wit/lad_d{d}_s{seed}.json", "w")); print(it, "best T", bs, flush=True)
print("FINAL d", d, "N", N, "T", bs)
