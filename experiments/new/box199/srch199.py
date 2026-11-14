#!/usr/bin/env python3
"""Box 199 (L-NEW 66): random search for a failure of ROUTE-LOW (ytopB_ne) or RW-WT (rwfail) / REWIN-HI (rhfail).
Mode base: add 1-3 random options to a frozen base genome. Mode fresh: a random genome (levels 0..L, 1-3 options per mover).
Option semantics as L-RED's compose226.add_opt / check (re-implemented). Usage: srch199.py SEED SAMPLES OUTDIR BASE.json... (ROOT env)."""
import sys, os, json, random, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import split199 as rw199
seed, S, OUT = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; bases = [json.load(open(f)) for f in sys.argv[4:]]
bases = [b.get("genome", b) for b in bases]; rng = random.Random(seed)
def add_opt(G, x, wt, xt, gp, bp_, bpar):
    G = copy.deepcopy(G); M = len(G["br"])
    G["gate"] = [[r + (r >= gp) for r in g] for g in G["gate"]]; G["gate"][x].append(gp)
    G["br"] = [r + (r >= bp_) for r in G["br"]] + [bp_]; G["bp"] = G["bp"] + [bpar]; G["opts"][x].append([wt, xt, M]); return G
def check(G):
    N = G["N"]; M = sum(len(o) for o in G["opts"])
    assert sorted(r for g in G["gate"] for r in g) == list(range(M)) and sorted(G["br"]) == list(range(M)) and len(G["bp"]) == M
    for x in range(N):
        assert G["opts"][x]
        for (w, t, b) in G["opts"][x]:
            assert (w == -1) if G["lev"][x] == 0 else (w >= 0 and G["lev"][w] == G["lev"][x] - 1)
def rnd_opt(G):
    N = G["N"]; x = rng.randrange(N); M = len(G["br"]); l = G["lev"][x]
    wt = -1 if l == 0 else rng.choice([y for y in range(N) if G["lev"][y] == l - 1])
    return add_opt(G, x, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
def fresh():
    L = rng.randint(1, 3); N = rng.randint(4, 12); lev = sorted(rng.randint(0, L) for _ in range(N)); lev[0] = 0
    for l in range(1, max(lev) + 1):
        if l - 1 not in lev: lev = [min(v, l - 1) if v >= l else v for v in lev]
    G = dict(N=N, lev=lev, opts=[[] for _ in range(N)], gate=[[] for _ in range(N)], br=[], bp=[], start=[0] * N)
    for x in range(N):
        for _ in range(rng.randint(1, 3)):
            M = len(G["br"]); l = lev[x]; wt = -1 if l == 0 else rng.choice([y for y in range(N) if lev[y] == l - 1])
            G = add_opt(G, x, wt, rng.choice(list(range(N)) + [-1]), rng.randint(0, M), rng.randint(0, M), rng.randrange(2))
    G["start"] = [rng.randrange(len(G["opts"][x])) for x in range(N)]; return G
KEYS = ("Bne_t1", "Bne_t2", "ytopB_ne", "rwfail", "rhfail", "dnfail", "hwfail", "gtfail", "trfail", "kindfail", "playfail")
tot = {k: 0 for k in KEYS}; tot["runs"] = tot["rewin"] = tot["ytops"] = 0
for i in range(S):
    if bases and rng.random() < 0.6:
        G = rng.choice(bases)
        for _ in range(rng.randint(1, 3)): G = rnd_opt(G)
    else: G = fresh()
    try: check(G); T, c = rw199.run(G, cap=3000)
    except AssertionError: continue
    except Exception as e: tot["err"] = tot.get("err", 0) + 1; continue
    tot["runs"] += 1; tot["rewin"] += c["rewin"]; tot["ytops"] += sum(v for k, v in c.items() if k.startswith("ytop_"))
    for k in KEYS:
        if c[k]:
            tot[k] += 1; fn = f"{OUT}/{k}_{seed}_{i}.json"
            if len([f for f in os.listdir(OUT) if f.startswith(k)]) < 20: json.dump(G, open(fn, "w"))
            print(i, "HIT", k, c[k], "N", G["N"], "M", len(G["br"]), "T3", T, fn, flush=True)
    if i % 200 == 0: print(i, tot, flush=True)
print("FINAL", tot, flush=True)
