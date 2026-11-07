#!/usr/bin/env python3
"""REFEREE successor 24: falsification attempt for T^R(3) <= 8 with my own simulator t3r_sim.py: random restarts x hill-climb over
𝓛^R_3 (the single-field mutations and generator of t3r_pin.py, copied; accept a mutant if its max-over-starts T does not fall).
Usage: python3 -I t3r_climb.py d restarts iters seed. DATA only (a search, not a proof)."""
import itertools, json, random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import t3r_sim as R

def rgen(rng, d):
    N = 2 * d
    order = list(range(N)); rng.shuffle(order); pos = {v: i for i, v in enumerate(order)}
    ranks = list(range(2 * N)); rng.shuffle(ranks)
    gates = list(range(2 * N)); rng.shuffle(gates)
    opts = []
    for x in range(N):
        later = [y for y in range(N) if pos[y] > pos[x]]
        o = []
        for k in range(2):
            xt = rng.choice(later + [-1, -1]) if later else -1
            o.append([-1 if x < 2 else 2 * (x // 2 - 1) + k, xt, 2 * x + k])
        opts.append(o)
    return {"N": N, "lev": [x // 2 for x in range(N)], "opts": opts,
            "gate": [[gates[2 * x], gates[2 * x + 1]] for x in range(N)], "br": ranks,
            "bp": [rng.randrange(2) for _ in range(2 * N)], "start": [0] * N}

def mutate(rng, G):
    H = json.loads(json.dumps(G))
    N = H["N"]
    while True:
        kind = rng.randrange(4)
        if kind == 0:
            a, b = rng.sample(range(2 * N), 2); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
        elif kind == 1:
            a = rng.randrange(2 * N); H["bp"][a] ^= 1
        elif kind == 2:
            x, y = rng.randrange(N), rng.randrange(N); k, j = rng.randrange(2), rng.randrange(2)
            H["gate"][x][k], H["gate"][y][j] = H["gate"][y][j], H["gate"][x][k]
        else:
            x, k = rng.randrange(N), rng.randrange(2)
            H["opts"][x][k][1] = rng.choice([y for y in range(N) if y != x] + [-1])
        if R.in_LR(H) and H != G:
            return H
        H = json.loads(json.dumps(G))

def tmax(G):
    return max(len(R.run(G, st)) - 1 for st in itertools.product((0, 1), repeat=G["N"]))

def climb(rng, G, iters):
    best, bt = G, tmax(G)
    for _ in range(iters):
        H = mutate(rng, best)
        t = tmax(H)
        if t >= bt:
            best, bt = H, t
    return best, bt


if __name__ == "__main__":
    d, rs, it, seed = (int(v) for v in sys.argv[1:5])
    rng = random.Random(seed); hist = {}; best = (-1, None)
    for r in range(rs):
        G, t = climb(rng, rgen(rng, d), it)
        hist[t] = hist.get(t, 0) + 1
        if t > best[0]:
            best = (t, G)
        print("restart", r, "maxT", t, flush=True)
    print("CLIMB d", d, "restarts", rs, "iters", it, "histogram of climbed max-T", dict(sorted(hist.items())), "best", best[0], flush=True)
    json.dump(best[1], open(f"t3r_logs/climb_best_d{d}_s{seed}.json", "w"))
