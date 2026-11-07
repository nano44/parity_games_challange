#!/usr/bin/env python3
"""L-SI box 78: annealing toward a tower of consecutive doubling levels, allowing RE-ENTRANT fuel (any Xi-target that keeps the Xi-graph
acyclic). Seed: an L^R_d genome; EXTRA=k appends k frozen top pairs (box76/append77.py construction) to give fuel room. Scalar score (SMOOTH=1: sum_(l<=4) min(F(l), 2^(l+2)-2) + T/100; else)
1000*h + 10*F(h+1) + T/10 (h = consecutive doubling levels from level 1). Moves as box76/climb77.py. Simulated annealing with
temperature TEMP0 decaying linearly to 0; the best genome is written to OUT every 500 iterations (resumable: re-run with OUT as seed).
Usage: climb78.py SEED.json RNGSEED ITERS OUT.json"""
import sys, os, json, random, copy, math
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "box76"))
from tw import Sim, analyse, is_lr
from climb77 import acyclic
def score(G):
    try: S = Sim(G).run(tuple(G["start"]), cap=4000)
    except RuntimeError: return None
    a = analyse(Sim(G), S); T = a["T"]; d = G["N"] // 2
    F = [sum(1 for t in range(1, T + 1) if a["flip"][t][j]) for j in range(d)]
    h = 0
    while h + 1 < d and F[h + 1] == 2 * F[h] + 2: h += 1
    nxt = F[h + 1] if h + 1 < d else 0
    if os.environ.get("SMOOTH"):   # sum over levels 0..4 of min(F(l), 2^(l+2) - 2) (height-5 tower target) + T/100
        return sum(min(F[l], 2 ** (l + 2) - 2) for l in range(min(5, d))) + T / 100.0, F, T
    return 1000 * h + 10 * nxt + T / 10.0, F, T
def append_frozen(G):
    N = G["N"]; d = N // 2; G = copy.deepcopy(G); M = len(G["br"]); r0 = max(G["br"]) + 1; g0 = max(max(g) for g in G["gate"]) + 1
    G["N"] = N + 2; G["lev"] = G["lev"] + [d, d]; G["start"] = list(G["start"]) + [0, 1]
    for i, x in enumerate((N, N + 1)):
        G["opts"].append([[2 * (d - 1) + k, -1, M + 2 * i + k] for k in range(2)]); G["gate"].append([g0 + 2 * i, g0 + 2 * i + 1])
        for k in range(2): G["br"].append(r0 + 2 * i + k); G["bp"].append(0 if k == G["start"][x] else 1)
    return G
def mutate(G, rnd):
    N = G["N"]; H2 = copy.deepcopy(G); r = rnd.random()
    if r < 0.45:
        x = rnd.randrange(N); k = rnd.randrange(2); H2["opts"][x][k][1] = rnd.choice([-1] + [y for y in range(N) if y != x])
        if not acyclic(H2): return None
    elif r < 0.62:
        i, j = rnd.sample(range(len(H2["br"])), 2); H2["br"][i], H2["br"][j] = H2["br"][j], H2["br"][i]
    elif r < 0.77:
        x, y = rnd.randrange(N), rnd.randrange(N); k, l = rnd.randrange(2), rnd.randrange(2)
        H2["gate"][x][k], H2["gate"][y][l] = H2["gate"][y][l], H2["gate"][x][k]
    elif r < 0.9:
        i = rnd.randrange(len(H2["bp"])); H2["bp"][i] ^= 1
    else:
        x = rnd.randrange(N); H2["start"][x] ^= 1
    return H2
def main():
    G = json.load(open(sys.argv[1])); rnd = random.Random(int(sys.argv[2])); iters = int(sys.argv[3]); out = sys.argv[4]
    for _ in range(int(os.environ.get("EXTRA", "0"))): G = append_frozen(G)
    assert is_lr(G) and acyclic(G)
    T0 = float(os.environ.get("TEMP0", "30"))
    cur = score(G); best = (cur[0], G); print("seed", cur, flush=True)
    for it in range(iters):
        H2 = mutate(G, rnd)
        if H2 is None: continue
        sc = score(H2)
        if sc is None: continue
        temp = T0 * (1 - it / iters) + 1e-9
        if sc[0] >= cur[0] or rnd.random() < math.exp((sc[0] - cur[0]) / temp):
            G, cur = H2, sc
            if sc[0] > best[0]:
                best = (sc[0], copy.deepcopy(H2)); print("it", it, "best", sc, flush=True)
        if it % 500 == 0: json.dump(best[1], open(out, "w"))
    json.dump(best[1], open(out, "w")); print("final", score(best[1]))
if __name__ == "__main__":
    main()
