#!/usr/bin/env python3
"""targeted PM kill: diamond Xi-structure (n layers, 2n movers, keyless max moves 2^(desc/2+1) - 1) inside an IDEAL genome with C extra
'clock' movers (their Xi-targets are other clocks or the exit, so no diamond mover gains Xi-descendants). Levels random (L levels),
W-targets any mover one level down, degree 2 everywhere. Climb ranks / parities / gates / starts / W-targets to maximize
max over diamond movers of moves(x) - 1 - desc(x) (PM excess), tie T. Usage: embed.py n C L iters restarts seed"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__)); exec(open(os.path.join(H, "permover.py")).read().split("\nif __name__")[0])
n, C, L, iters, restarts, seed = map(int, sys.argv[1:7]); rng = random.Random(seed); N = 2 * n + C; DIA = list(range(2 * n))

def build():
    while True:
        lev = [rng.randrange(L) for _ in range(N)]
        if all(any(l == j for l in lev) for j in range(L)): break
    opts = []; M = 0
    for x in range(N):
        o = []
        for k in range(2):
            if x < 2 * n: xt = 2 * (x // 2 + 1) + k if x // 2 + 1 < n else -1
            else: xt = rng.choice([v for v in range(2 * n, N) if v > x] + [-1])
            wt = rng.choice([v for v in range(N) if lev[v] == lev[x] - 1]) if lev[x] > 0 else -1
            o.append([wt, xt, M]); M += 1
        opts.append(o)
    br = list(range(M)); rng.shuffle(br); gt = list(range(M)); rng.shuffle(gt)
    return {"N": N, "lev": lev, "opts": opts, "gate": [[gt[2 * x], gt[2 * x + 1]] for x in range(N)], "br": br,
            "bp": [rng.randint(0, 1) for _ in range(M)], "start": [rng.randint(0, 1) for _ in range(N)], "deg": [2] * N}

def mut(G):
    G = copy.deepcopy(G); M = 2 * N; r = rng.random()
    if r < 0.3: i, j = rng.sample(range(M), 2); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.45: G["bp"][rng.randrange(M)] ^= 1
    elif r < 0.7:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(2), rng.randrange(2)
        G["gate"][a][ka], G["gate"][b][kb] = G["gate"][b][kb], G["gate"][a][ka]
    elif r < 0.8: G["start"][rng.randrange(N)] ^= 1
    else:
        x = rng.randrange(N)
        if G["lev"][x] > 0: G["opts"][x][rng.randrange(2)][0] = rng.choice([v for v in range(N) if G["lev"][v] == G["lev"][x] - 1])
    return G

def sc(G):
    r = measure(G); return (max(r["mv"][x] - 1 - r["desc"][x] for x in DIA), max(r["mv"][x] for x in DIA), r["T"])

best = None
for rs in range(restarts):
    G = build(); s = sc(G)
    for it in range(iters):
        G2 = mut(G); s2 = sc(G2)
        if s2 >= s: G, s = G2, s2
        if s[0] > 0: break
    if best is None or s > best: best = s; json.dump(G, open(os.path.join(H, "out", "embed_n%d_C%d_L%d_s%d.json" % (n, C, L, seed)), "w"))
    print("restart %d %s best %s%s" % (rs, s, best, "  KILL" if s[0] > 0 else ""), flush=True)
    if s[0] > 0: json.dump(G, open(os.path.join(H, "out", "KILL_PM_embed_n%d_C%d_L%d_s%d.json" % (n, C, L, seed)), "w")); break
