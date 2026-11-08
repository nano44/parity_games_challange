#!/usr/bin/env python3
"""L-RED 56 R221 (i) BREAK ENDGAME-3: structured genome families aimed at the core mechanism, run through post221.post; tally of
(#fallbacks, post-fallback iterations, post mover changes) and tau changes; saves any run with fb != 1 or post != 3 or tau changes.
Modes: esc (most Xi-targets X: many gates feed K), noesc (no X targets at levels >= 1), deep (d 6-9, width 1-2), dense (degree 3-4),
late (start = the option of LEAST own.py final value: movers converge late), lvl0 (many level-0 movers, all degree 3).
Usage: spost221.py MODE SEED COUNT"""
import sys, os, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post221, own
mode, seed, cnt = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]); rng = random.Random(seed); tally = collections.Counter(); hits = 0
def gen():
    d = rng.randint(6, 9) if mode == "deep" else rng.randint(1, 5); w = rng.randint(1, 2) if mode == "deep" else rng.randint(1, 3)
    D = rng.randint(3, 4) if mode in ("dense", "lvl0") else rng.choice([2, 3])
    lev = [x // w for x in range(d * w)]
    if mode == "lvl0": lev = [0] * rng.randint(2, 4) + lev
    N = len(lev); opts = []
    for x in range(N):
        oo = []
        for _ in range(D):
            wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            if mode == "esc": xt = -1 if rng.random() < 0.7 else rng.randrange(N)
            elif mode == "noesc": xt = rng.randrange(N)
            else: xt = rng.choice(list(range(N)) + [-1])
            oo.append([wt, xt, 0])
        opts.append(oo)
    M = sum(len(o) for o in opts); perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([])
        for o in opts[x]: o[2] = i; gate[x].append(perm[i]); i += 1
    br = list(range(M)); rng.shuffle(br)
    G = {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)], "start": [rng.randrange(len(o)) for o in opts]}
    if mode == "late":
        out, V, O, _ = own.run(G); vals = out[-1][1]; vj = own.VJ(own.build(G)[1])
        import functools; key = functools.cmp_to_key(vj.cmp)
        G["start"] = [min(range(len(opts[x])), key=lambda k: key(vals[V[("g", (x, k))]])) for x in range(N)]
    return G
for i in range(cnt):
    G = gen(); r = post221.post(G); post = sum(r["phases"][1:]) + r["fb"]
    tally[(r["fb"], post, r["Mpost"], r["tpost"])] += 1
    if r["fb"] != 1 or post != 3 or r["tpost"]:
        hits += 1; json.dump(G, open(f"out/spost_{mode}_{seed}_{i}.json", "w")); print("HIT", i, r, flush=True)
print(f"mode {mode} seed {seed} genomes {cnt} hits {hits} tally (fb, post, Mpost, tau-post): {sorted(tally.items())}", flush=True)
