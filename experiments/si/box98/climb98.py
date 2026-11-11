#!/usr/bin/env python3
"""L-SI box 98: hill-climb for long N5'-xi mover phases (T3 on Gamma3 from S3; L-NEW gamma3 / n5v / n5x / eg195 at the pins of
box91/pins.txt) at fixed genome shape (d levels, width w, degree D). Mutations of rand191.rgen genomes: one option's Xi-target (a mover
or X), one option's W-target (a mover one level down), the start of one mover, a swap of two beta ranks, a flip of one beta parity, a swap
of two gate indices. Score = (T3, U, ascents) lexicographic: longer runs first. Accept if not worse (sideways moves allowed).
Prints, per shape, the best T3, its U, N, M and the best genome as JSON (one line, «BEST …»).
Usage: climb98.py SEED ITERS d w D [d w D ...]   (ROOT = archive of l-new fcba92fc)"""
import sys, os, json, random, copy
R = os.environ["ROOT"]; os.environ.setdefault("EG195_ROOT", R)
sys.path[:0] = [os.path.join(R, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import eg195, gamma3, n5v, n5x, rand191

def T3(G, cap=5000):
    g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0)
    E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
    for j in range(cap):
        res = n5v.step(g, E, Ed, sigma, tau, "xi")
        if res is None or res[4]: return j
        sigma, tau = list(res[0]), list(res[1])
    return cap

def Uof(G):
    lev = G["lev"]; return sum(1 for x in range(G["N"]) for (wt, xt, b) in G["opts"][x] if xt >= 0 and lev[xt] > lev[x])

def mutate(G, rng):
    G = copy.deepcopy(G); N = G["N"]; lev = G["lev"]; opts = G["opts"]
    x = rng.randrange(N); k = rng.randrange(len(opts[x])); r = rng.randrange(6)
    if r == 0: opts[x][k][1] = -1 if rng.random() < 0.15 else rng.choice([y for y in range(N) if y != x] or [-1])
    elif r == 1 and lev[x] > 0: opts[x][k][0] = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
    elif r == 2: G["start"][x] = rng.randrange(len(opts[x]))
    elif r == 3:
        M = len(G["br"]); i, j = rng.randrange(M), rng.randrange(M); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r == 4: i = rng.randrange(len(G["bp"])); G["bp"][i] ^= 1
    else:
        y = rng.randrange(N); l = rng.randrange(len(opts[y])); G["gate"][x][k], G["gate"][y][l] = G["gate"][y][l], G["gate"][x][k]
    return G

if __name__ == "__main__":
    seed, iters = int(sys.argv[1]), int(sys.argv[2]); a = list(map(int, sys.argv[3:]))
    print("shape d w D N M bestT3 U", flush=True)
    for i in range(0, len(a), 3):
        d, w, D = a[i:i + 3]; rng = random.Random(seed * 1000 + i)
        G = rand191.rgen(rng, d, w, D); s = T3(G)
        for _ in range(iters):
            H = mutate(G, rng); t = T3(H)
            if t >= s: G, s = H, t
        M = sum(len(o) for o in G["opts"])
        print("shape", d, w, D, G["N"], M, s, Uof(G), flush=True)
        print("BEST", d, w, D, json.dumps(G, separators=(",", ":")), flush=True)
