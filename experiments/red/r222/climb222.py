#!/usr/bin/env python3
"""L-RED 57 R222 PRIV-FREE: adversarial climb against the PRIV-free flip bound (R222-lockup.md §4). Genome = priv222.rgen_ret start;
mutations: retarget one option's Xi-target (biased to movers whose plays return), its W-target, a beta rank / parity (SET's beta kept
even), a gate index swap, a start entry, add / drop an option. Score = (- min slack over non-PRIV units, max flips of a non-PRIV unit, T).
A unit with slack < 0 is a counterexample: saved to out/climb222_viol_<seed>.json. Usage: climb222.py SEED ITERS OUT.txt"""
import sys, os, json, random, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import priv222
seed, iters, outf = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
def score(G):
    try: r = priv222.check(G)
    except Exception: return None
    if not r.get("np"): return (-99, 0, 0), r
    return (-r.get("npslack", 99), r["maxnopriv"], r["T"]), r
def renum(G):
    M = sum(len(o) for o in G["opts"]); i = 0
    for x in range(G["N"]):
        for o in G["opts"][x]: o[2] = i; i += 1
    G["gate"] = [[0] * len(o) for o in G["opts"]]; perm = list(range(M)); rng.shuffle(perm); i = 0
    for x in range(G["N"]):
        for k in range(len(G["opts"][x])): G["gate"][x][k] = perm[i]; i += 1
    if len(G["br"]) != M: G["br"] = list(range(M)); rng.shuffle(G["br"]); G["bp"] = [rng.randrange(2) for _ in range(M)]
    for x in range(G["N"]):
        for o in G["opts"][x]:
            if o[1] == x: G["bp"][o[2]] = 0
    G["start"] = [min(s, len(G["opts"][x]) - 1) for x, s in enumerate(G["start"])]
def mutate(G):
    G = copy.deepcopy(G); N, lev = G["N"], G["lev"]; x = rng.randrange(N); k = rng.randrange(len(G["opts"][x])); o = G["opts"][x][k]
    m = rng.randrange(7)
    if m == 0 and o[1] != x: o[1] = rng.choice(list(range(N)) + [-1])
    elif m == 1 and lev[x]: o[0] = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
    elif m == 2: b = o[2]; G["br"][b], G["br"][rng.randrange(len(G["br"]))] = G["br"][rng.randrange(len(G["br"]))], G["br"][b]
    elif m == 3: G["bp"][o[2]] ^= (o[1] != x)
    elif m == 4: G["start"][x] = rng.randrange(len(G["opts"][x]))
    elif m == 5 and len(G["opts"][x]) < 5:
        G["opts"][x].append([rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1, rng.choice(list(range(N)) + [-1]), 0]); renum(G); return G
    elif m == 6 and len(G["opts"][x]) > 2 and o[1] != x: del G["opts"][x][k]; renum(G); return G
    else: G["gate"][x][k], G["gate"][rng.randrange(N)][0] = G["gate"][rng.randrange(N)][0], G["gate"][x][k]
    renum(G) if m == 7 else None
    return G
G = priv222.rgen_ret(rng); best = score(G)
while best is None: G = priv222.rgen_ret(rng); best = score(G)
fo = open(outf, "a")
for it in range(iters):
    H = mutate(G); s = score(H)
    if s is None: continue
    if s[0] >= best[0]:
        G, best = H, s
        if s[0][0] > 0:
            json.dump(G, open(f"out/climb222_viol_{seed}.json", "w")); fo.write(f"VIOL it {it} {s[0]} {s[1]['violnp']}\n"); fo.flush(); break
    if it % 200 == 0: fo.write(f"it {it} best {best[0]} N {G['N']}\n"); fo.flush()
json.dump(G, open(f"out/climb222_best_{seed}.json", "w"))
fo.write(f"FINAL seed {seed} best (−min slack, max non-PRIV flips, T) {best[0]} np {best[1].get('np')} violnp {len(best[1]['violnp'])}\n")
