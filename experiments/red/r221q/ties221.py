#!/usr/bin/env python3
"""L-RED 56 R221: search random genomes (Xi-cycles allowed; bias: Xi-target = W-target with prob P) for VJ ties in own.py's IDEAL-CYC runs:
GATE ties (Omega(e_g) == Omega(beta_g)) and MOVER ties (two options of a mover with equal gate values, one of them the max). Writes the first
genomes with gate ties to out/tie_*.json. Usage: ties221.py SEED COUNT P"""
import sys, json, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import own
seed, cnt, P = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]); rng = random.Random(seed)
def rgen(d, w, D):
    N = d * w; lev = [x // w for x in range(N)]; opts = []
    for x in range(N):
        oo = []
        for _ in range(D):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            xt = wt if (wt >= 0 and rng.random() < P) else rng.choice(list(range(N)) + [-1]); oo.append([wt, xt, 0])
        opts.append(oo)
    M = N * D; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(D) for _ in range(N)]}
gt = mt = gg = mg = 0; saved = 0
for i in range(cnt):
    d = rng.randint(2, 5); w = rng.randint(1, 3); G = rgen(d, w, rng.choice([2, 2, 3]))
    out, V, O, o_ = own.run(G, 2000); N = G["N"]; a = b = 0
    for s, vals, tau in out:
        for q in O:
            if vals[V[("e", q)]] == vals[V[("b", q)]]: a += 1
        for x in range(N):
            gv = [vals[V[("g", (x, k))]] for k in range(len(G["opts"][x]))]
            if len(gv) != len(set(gv)): b += 1
    gt += a; mt += b; gg += a > 0; mg += b > 0
    if a and saved < 5: json.dump(G, open(f"out/tie_{seed}_{i}.json", "w")); saved += 1
print(f"seed {seed} genomes {cnt} P {P}: gate-tie (state, gate) pairs {gt} in {gg} genomes; mover-tie (state, mover) pairs {mt} in {mg} genomes", flush=True)
