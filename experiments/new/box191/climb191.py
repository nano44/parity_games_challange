#!/usr/bin/env python3
"""Box 191: hill-climb IDEAL-CYC(G) (Howard at movers of Gamma(G), cycles allowed). Score: 'T' = run length, 'run' = longest run
of consecutive PATH steps (no VJ cycle node changes), 'C' = number of cycle steps. Resumable: keeps the best genome in OUT.json and
restarts from it if present. Usage: climb191.py SCORE d w D seed iters OUT"""
import sys, os, json, random, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import idealcyc, rand191
sc_kind, d, w, D, seed, iters, out = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
rng = random.Random(seed)

def score(G):
    st, k = idealcyc.run(G, cap=5000, want_kinds=True); T = len(st) - 1; mr = max(len(r) for r in k.split("C")) if k else 0; C = k.count("C")
    main = {"T": T, "run": mr, "C": C}[sc_kind]
    return (main, T), T, mr, C

def mut(G):
    G = copy.deepcopy(G); N = G["N"]; r = rng.random(); x = rng.randrange(N); k = rng.randrange(len(G["opts"][x])); M = sum(len(o) for o in G["opts"])
    if r < 0.35: G["opts"][x][k][1] = -1 if rng.random() < 0.1 else rng.choice([y for y in range(N) if y != x] or [-1])
    elif r < 0.5 and G["lev"][x]: G["opts"][x][k][0] = rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
    elif r < 0.7: i, j = rng.randrange(M), rng.randrange(M); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r < 0.8: G["bp"][rng.randrange(M)] ^= 1
    elif r < 0.92:
        a, c = rng.randrange(N), rng.randrange(N); ka, kc = rng.randrange(len(G["opts"][a])), rng.randrange(len(G["opts"][c]))
        G["gate"][a][ka], G["gate"][c][kc] = G["gate"][c][kc], G["gate"][a][ka]
    else: G["start"][x] = rng.randrange(len(G["opts"][x]))
    return G

cur = json.load(open(out + ".json")) if os.path.exists(out + ".json") else rand191.rgen(rng, d, w, D)
cs = score(cur); best = cs[0]
print(f"start score {cs[0]} N {cur['N']}", flush=True)
for it in range(iters):
    c = mut(cur)
    try: s = score(c)
    except Exception as ex: continue
    if s[0] >= cs[0]:
        cur, cs = c, s
        if s[0] > best:
            best = s[0]; json.dump(cur, open(out + ".json", "w"))
            print(f"it {it} N {cur['N']} T {s[1]} maxrun {s[2]} C {s[3]}", flush=True)
print(f"FINAL best {best} N {cur['N']}", flush=True)
