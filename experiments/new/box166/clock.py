#!/usr/bin/env python3
"""L-NEW box 166: candidate PM kill. Fixed Xi-part V = a key-free PM violator (default out/keyless_pmviol_N5_d4_m7.json: mover 2 has
desc 4, key-free max 7 moves; its options, Xi-targets, ranks, parities are kept). Added: C clock movers (degree 2, Xi-targets only
among clocks or the exit, so no V-mover gains descendants), all movers on random levels 0..L-1, W-targets any mover one level down.
Climb clock ranks / parities / Xi-targets, all gates, all starts, all W-targets, to maximize moves(x0) on the real IDEAL run.
KILL iff moves(x0) > 1 + desc(x0) = 5. Usage: clock.py C L iters restarts seed [vfile x0]"""
import os, sys, json, random, copy
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box165", "permover.py")).read().split("\nif __name__")[0])
C, L, iters, restarts, seed = map(int, sys.argv[1:6]); rng = random.Random(seed)
vfile = sys.argv[6] if len(sys.argv) > 6 else os.path.join(H, "out", "keyless_pmviol_N5_d4_m7.json"); x0 = int(sys.argv[7]) if len(sys.argv) > 7 else 2
V = json.load(open(vfile)); NV = V["N"]; N = NV + C; MV = 2 * NV

def build():
    while True:
        lev = [rng.randrange(L) for _ in range(N)]
        if all(j in lev for j in range(L)): break
    opts = []
    for x in range(N):
        o = []
        for k in range(2):
            wt = rng.choice([v for v in range(N) if lev[v] == lev[x] - 1]) if lev[x] > 0 else -1
            if x < NV: xt = V["opts"][x][k][1]
            else: xt = rng.choice([v for v in range(x + 1, N)] + [-1])
            o.append([wt, xt, 2 * x + k])
        opts.append(o)
    # ranks: V keeps its relative order on the top; clocks below (clock beta never meets a V chain)
    br = [0] * (2 * N); vr = sorted(range(MV), key=lambda m: V["br"][m])
    for i, m in enumerate(vr): br[m] = 2 * C + i
    cr = list(range(MV, 2 * N)); rng.shuffle(cr)
    for i, m in enumerate(cr): br[m] = i
    gt = list(range(2 * N)); rng.shuffle(gt)
    return {"N": N, "lev": lev, "opts": opts, "gate": [[gt[2 * x], gt[2 * x + 1]] for x in range(N)], "br": br,
            "bp": V["bp"][:MV] + [rng.randint(0, 1) for _ in range(2 * C)], "start": [rng.randint(0, 1) for _ in range(N)], "deg": [2] * N}

def mut(G):
    G = copy.deepcopy(G); r = rng.random()
    if r < 0.15 and C > 1:
        i, j = rng.sample(range(MV, 2 * N), 2); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.25 and C > 0: G["bp"][rng.randrange(MV, 2 * N)] ^= 1
    elif r < 0.5:
        a, b = rng.randrange(N), rng.randrange(N); ka, kb = rng.randrange(2), rng.randrange(2)
        G["gate"][a][ka], G["gate"][b][kb] = G["gate"][b][kb], G["gate"][a][ka]
    elif r < 0.6: G["start"][rng.randrange(N)] ^= 1
    elif r < 0.85:
        x = rng.randrange(N)
        if G["lev"][x] > 0: G["opts"][x][rng.randrange(2)][0] = rng.choice([v for v in range(N) if G["lev"][v] == G["lev"][x] - 1])
    elif C > 0:
        x = rng.randrange(NV, N); G["opts"][x][rng.randrange(2)][1] = rng.choice([v for v in range(x + 1, N)] + [-1])
    return G

def sc(G):
    r = measure(G); return (r["mv"][x0], r["T"])

best = None
for rs in range(restarts):
    G = build(); s = sc(G)
    for it in range(iters):
        G2 = mut(G); s2 = sc(G2)
        if s2 >= s: G, s = G2, s2
    if best is None or s > best: best = s; json.dump(G, open(os.path.join(H, "out", "clock_C%d_L%d_s%d.json" % (C, L, seed)), "w"))
    kill = s[0] > 5
    print("restart %d moves(x0) %d T %d best %s%s" % (rs, s[0], s[1], best, "  KILL" if kill else ""), flush=True)
    if kill: json.dump(G, open(os.path.join(H, "out", "KILL_PM_clock_C%d_L%d_s%d.json" % (C, L, seed)), "w")); break
