#!/usr/bin/env python3
"""L-COMP box 34 (b) (Lead 20:18Z): structured search for genomes with large C (box 198 C-EQUIV), then A, maxm, with own34 (engine
of record for the search; every hit is re-measured with asc197 @ f98e93ee before it is reported).
Score (lexicographic): (C, maxalt, maxm, T3). Search: restarts from a random genome of (N, M) (cmp34's sampler, all level vectors), then
first-improvement hill climbing with sideways moves (equal score accepted with prob. 0.3), STEPS proposals per restart.
Moves (all keep a valid genome of the eg195 schema): xt of one option := a random value in {-1} + movers; wt of one option := a random
mover of level lev - 1 (level >= 1); swap two gate indices; swap two br ranks; flip one bp; start of one mover := another of its options;
re-level: a random nondecreasing reachable level vector (wt re-drawn where needed).
Scope [E-LEV] (gamma3 e-order (lev, gate)) unless --noelev. Freezes (out/climb/HIT_*.json) every genome with C >= 6 or maxm >= 3.
Resumable: state file OUT.state (json: restart index, best per restart, global best); one log line per restart to OUT.
Usage: climb34.py N M RESTARTS STEPS SEED OUT [--noelev]"""
import sys, os, json, random, hashlib, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import own34
a = [x for x in sys.argv[1:] if not x.startswith('--')]
N, M, RESTARTS, STEPS, SEED, OUT = int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]
ELEV = '--noelev' not in sys.argv
HITDIR = os.path.join(H, "out", "climb"); os.makedirs(HITDIR, exist_ok=True)

def levvecs(N):
    out = []
    def rec(v):
        if len(v) == N: out.append(tuple(v)); return
        for l in (v[-1], v[-1] + 1): rec(v + [l])
    rec([0]); return out
LEVS = levvecs(N)

def comps(M, N):
    if N == 1: return [(M,)]
    return [(i,) + c for i in range(1, M - N + 2) for c in comps(M - i, N - 1)]
COMPS = comps(M, N)

def fresh(rng):
    lev = rng.choice(LEVS); D = rng.choice(COMPS)
    gate = list(range(M)); rng.shuffle(gate); br = list(range(M)); rng.shuffle(br)
    opts = []; g = []; b = 0
    for x in range(N):
        oo = []; gg = []
        for _ in range(D[x]):
            low = [y for y in range(N) if lev[y] == lev[x] - 1]
            oo.append([-1 if lev[x] == 0 else rng.choice(low), rng.randrange(-1, N), b]); gg.append(gate[b]); b += 1
        opts.append(oo); g.append(gg)
    return {"N": N, "lev": list(lev), "opts": opts, "gate": g, "br": br, "bp": [rng.randrange(2) for _ in range(M)],
            "start": [rng.randrange(d) for d in D]}

def mutate(G, rng):
    G = json.loads(json.dumps(G)); O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    r = rng.randrange(7)
    if r == 0:
        x, k = rng.choice(O); G["opts"][x][k][1] = rng.randrange(-1, N)
    elif r == 1:
        cand = [(x, k) for (x, k) in O if G["lev"][x] >= 1]
        if not cand: return mutate(G, rng)
        x, k = rng.choice(cand); G["opts"][x][k][0] = rng.choice([y for y in range(N) if G["lev"][y] == G["lev"][x] - 1])
    elif r == 2:
        (x1, k1), (x2, k2) = rng.sample(O, 2); G["gate"][x1][k1], G["gate"][x2][k2] = G["gate"][x2][k2], G["gate"][x1][k1]
    elif r == 3:
        i, j = rng.sample(range(M), 2); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
    elif r == 4:
        i = rng.randrange(M); G["bp"][i] ^= 1
    elif r == 5:
        x = rng.randrange(N); d = len(G["opts"][x])
        if d == 1: return mutate(G, rng)
        G["start"][x] = rng.choice([k for k in range(d) if k != G["start"][x]])
    else:
        lev = rng.choice(LEVS); G["lev"] = list(lev)
        for x in range(N):
            for o in G["opts"][x]:
                low = [y for y in range(N) if lev[y] == lev[x] - 1]
                if lev[x] == 0: o[0] = -1
                elif o[0] not in low: o[0] = rng.choice(low)
    return G

def score(G):
    m = own34.measure(G, ELEV, extra=True)
    return (m["C"], m["maxalt"], m["maxm"], m["T3"]), m

def sha(G): return hashlib.sha1(json.dumps(G, sort_keys=True).encode()).hexdigest()

stf = OUT + ".state"
st = json.load(open(stf)) if os.path.exists(stf) else dict(r=0, best=None, bestG=None, hits=0)
while st["r"] < RESTARTS:
    rng = random.Random(SEED * 100003 + st["r"]); t0 = time.time()
    G = fresh(rng); s, m = score(G); best = (s, G)
    for _ in range(STEPS):
        H2 = mutate(G, rng)
        try: s2, m2 = score(H2)
        except AssertionError: continue
        if s2 > s or (s2 == s and rng.random() < 0.3):
            G, s, m = H2, s2, m2
            if s > best[0]: best = (s, G)
            if m["C"] >= 6 or m["maxm"] >= 3:
                h = sha(G); fn = os.path.join(HITDIR, f"HIT_N{N}M{M}_C{m['C']}_m{m['maxm']}_{h[:8]}.json")
                if not os.path.exists(fn):
                    json.dump(G, open(fn, "w"), sort_keys=True); st["hits"] += 1
                    with open(OUT, "a") as f: f.write(f"HIT {fn} {m}\n")
    if st["best"] is None or list(best[0]) > st["best"]: st["best"] = list(best[0]); st["bestG"] = best[1]
    st["r"] += 1
    with open(OUT, "a") as f:
        f.write(f"restart {st['r'] - 1} best (C, A, maxm, T3) {list(best[0])} global {st['best']} hits {st['hits']} {time.time() - t0:.0f}s\n")
    json.dump(st, open(stf + ".tmp", "w")); os.replace(stf + ".tmp", stf)
with open(OUT, "a") as f:
    f.write(f"SUMMARY N {N} M {M} restarts {RESTARTS} steps {STEPS} seed {SEED} elev {ELEV} best {st['best']} hits {st['hits']}\n")
    f.write("BEST " + json.dumps(st["bestG"], sort_keys=True) + "\n")
