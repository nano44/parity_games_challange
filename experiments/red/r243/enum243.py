#!/usr/bin/env python3
"""L-RED 69 R243: full key enumeration depth on Ξ-acyclic ladder genomes (𝓛^R_d: movers 2l, 2l+1 at level l, two options each with
W-targets 2l-2, 2l-1; level 0 to c_W). Simulator: L-RED's r187 ideal.traj (the IDEAL / KEY model of R104; equals N5's key run from S3
on Γ3(G) before the first fallback on Ξ-acyclic genomes: R117 / box 105 KEY-MODEL; T equal to N5's T_key on the five towers, checked).
k(G) := the largest k such that for some base level b every level b + j, j < k, has a mover with sw = 2^(j+1) - 1 (= |K| - 1: full enumeration, box 217 A5).
Score (lexicographic): (k, best sw at level k / (2^(k+1) - 1), T).
Climb: mutations keep the ladder W-structure and Ξ-acyclicity (Ξ-target of (x, k) is -1 or a mover; a cycle is rejected), and change
Ξ-targets, β ranks (swap), β parities, gate indices (swap), starts. Resumable checkpoint (RESUME=1), TLIMIT seconds.
START.json with D > its depth: lifted to depth D first (helper levels appended on top).
Usage: enum243.py climb TAG SEED EVALS D [START.json] | enum243.py score G.json ...   (OUT dir env, default experiments/red/r243/out)"""
import sys, os, json, random, time, copy, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "r187"))
import ideal
OUT = os.environ.get("OUT", os.path.join(HERE, "out")); RESUME = os.environ.get("RESUME") == "1"; TLIMIT = float(os.environ.get("TLIMIT", "3000"))
XLOC = int(os.environ.get("XLOC", "0"))   # >0: Ξ-targets restricted to movers within XLOC levels of x (locality), 0 = any

def ladder(rng, d):
    N = 2 * d; lev = [x // 2 for x in range(N)]; opts = []; i = 0
    for x in range(N):
        l = lev[x]; o = []
        for k in range(2):
            o.append([-1 if l == 0 else 2 * l - 2 + k, -1, i]); i += 1
        opts.append(o)
    M = i; gp = list(range(M)); rng.shuffle(gp); it = iter(gp)
    G = dict(N=N, lev=lev, opts=opts, gate=[[next(it), next(it)] for _ in range(N)], br=rng.sample(range(M), M), bp=[rng.randint(0, 1) for _ in range(M)],
             start=[rng.randint(0, 1) for _ in range(N)])
    for x in range(N):
        for o in G["opts"][x]: o[1] = rand_xt(rng, G, x)
    if not acyclic(G): return ladder(rng, d)
    return G

def rand_xt(rng, G, x):
    N, lev = G["N"], G["lev"]
    cand = [y for y in range(N) if y != x and (XLOC == 0 or abs(lev[y] - lev[x]) <= XLOC)]
    return -1 if rng.random() < 0.15 or not cand else rng.choice(cand)

def acyclic(G):
    N = G["N"]; adj = [[o[1] for o in G["opts"][x] if o[1] >= 0] for x in range(N)]; col = [0] * N
    for s in range(N):
        if col[s]: continue
        st = [(s, 0)]; col[s] = 1
        while st:
            v, i = st[-1]
            if i < len(adj[v]):
                st[-1] = (v, i + 1); w = adj[v][i]
                if col[w] == 1: return False
                if col[w] == 0: col[w] = 1; st.append((w, 0))
            else: col[v] = 2; st.pop()
    return True

def score(G):
    S, why = ideal.traj(G, cap=200000); N = G["N"]; T = len(S) - 1
    sw = [0] * N
    for i in range(1, len(S)):
        a, b = S[i - 1], S[i]
        for x in range(N):
            if a[x] != b[x]: sw[x] += 1
    L = max(G["lev"]) + 1
    best = [max(sw[x] for x in range(N) if G["lev"][x] == l) for l in range(L)]
    K = (0, 0.0)
    for b in range(L):                                   # a full block may start at any base level b (DBL4: b = 1)
        k = 0
        while b + k < L and best[b + k] == 2 ** (k + 1) - 1: k += 1
        frac = best[b + k] / (2 ** (k + 1) - 1) if b + k < L else 1.0
        K = max(K, (k, round(frac, 4)))
    return (K[0], K[1], T), best, why

FOCUS = int(os.environ.get("FOCUS", "-1"))   # >= 0: only movers of level >= FOCUS mutate (their Ξ-target, β, gate, start)

def mutate(G, rng):
    G = copy.deepcopy(G); N = G["N"]; M = len(G["br"])
    pool = [x for x in range(N) if G["lev"][x] >= FOCUS] if FOCUS >= 0 else list(range(N))
    for _ in range(rng.choice([1, 1, 2, 3])):
        x = rng.choice(pool); k = rng.randrange(2); o = G["opts"][x][k]; r = rng.random()
        if r < 0.35: o[1] = rand_xt(rng, G, x)
        elif r < 0.55: j = rng.randrange(M); G["br"][o[2]], G["br"][j] = G["br"][j], G["br"][o[2]]
        elif r < 0.70: G["bp"][o[2]] ^= 1
        elif r < 0.85:
            y = rng.choice(pool); j = rng.randrange(2); G["gate"][x][k], G["gate"][y][j] = G["gate"][y][j], G["gate"][x][k]
        else: G["start"][x] ^= 1
    return G if acyclic(G) else None

def lift(G, D, rng):
    """append ladder levels on top up to depth D (helpers): random Ξ-targets (acyclic), gates above every old gate, β ranks inserted at random"""
    G = copy.deepcopy(G); d0 = max(G["lev"]) + 1; M0 = len(G["br"]); ranks = [(r, i) for i, r in enumerate(G["br"])]
    for l in range(d0, D):
        for j in range(2):
            x = G["N"]; G["N"] += 1; G["lev"].append(l); o = []
            for k in range(2):
                b = len(G["bp"]); G["bp"].append(rng.randint(0, 1)); ranks.append((rng.random() * (len(ranks) + 1) - 0.5, b))
                o.append([2 * l - 2 + k, -1, b])
            G["opts"].append(o); G["gate"].append([max(max(g) for g in G["gate"]) + 1, max(max(g) for g in G["gate"]) + 2]); G["start"].append(rng.randint(0, 1))
    br = [0] * len(ranks)
    for r, (_, b) in enumerate(sorted(ranks)): br[b] = r
    G["br"] = br
    for x in range(2 * d0, G["N"]):
        for o in G["opts"][x]:
            for _ in range(20):
                o[1] = rand_xt(rng, G, x)
                if acyclic(G): break
                o[1] = -1
    return G

def climb(tag, seed, evals, d, start=None):
    os.makedirs(OUT, exist_ok=True); ck = os.path.join(OUT, f"ck_{tag}.json"); t0 = time.time()
    if RESUME and os.path.exists(ck):
        C = json.load(open(ck)); rng = random.Random(); st = C["rng"]; rng.setstate((st[0], tuple(st[1]), st[2])); best, bf, ev = C["best"], tuple(C["fit"]), C["evals"]
    else:
        rng = random.Random(seed); best = json.load(open(start)) if start else ladder(rng, d); best = best.get("genome", best)
        if start and d > max(best["lev"]) + 1: best = lift(best, d, rng)
        bf = score(best)[0]; ev = 0
    def save():
        st = rng.getstate(); json.dump(dict(best=best, fit=list(bf), evals=ev, rng=[st[0], list(st[1]), st[2]], d=d), open(ck + ".tmp", "w")); os.replace(ck + ".tmp", ck)
    while ev < evals and time.time() - t0 < TLIMIT:
        c = mutate(best, rng); ev += 1
        if c is None: continue
        f, b, why = score(c)
        if f >= bf:
            if f[:2] > bf[:2]: print(f"ENUM243 {tag} eval {ev} new best {f} levels {b[:f[0] + 2]} | {time.time() - t0:.0f} s", flush=True)
            best, bf = c, f
        if ev % 500 == 0: save()
    save(); h = hashlib.sha1(json.dumps(best, sort_keys=True).encode()).hexdigest()[:8]
    fn = os.path.join(OUT, f"ENUM_{tag}_d{d}_k{bf[0]}_{h}.json"); json.dump(best, open(fn, "w"))
    print(f"ENUM243 {tag} END evals {ev} d {d} best {bf} file {os.path.basename(fn)} | {time.time() - t0:.0f} s", flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "climb":
        climb(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6] if len(sys.argv) > 6 else None)
    else:
        for f in sys.argv[2:]:
            G = json.load(open(f)); G = G.get("genome", G); sc, best, why = score(G)
            print(f"ENUM243 score {os.path.basename(f)}: k {sc[0]} frac {sc[1]} T {sc[2]} ({why}) per-level best sw {best}", flush=True)
