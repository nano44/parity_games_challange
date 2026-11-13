#!/usr/bin/env python3
"""L-RED 69 R241: adversarial hill climb over genomes G (N5 = n5s237 mode spec from S3 on Γ3(G)) against box 213 KEY-TAU and box 215
KEYSIDE-ALL, every eval checked with kt241.analyse (all must-0 counters). Objective (OBJ):
  T     non-fallback steps before the first fallback (long key runs)
  nlk   moves to an option that is NOT the global least key under the new state (the value side restricting A_t: «non-least-key choice»)
  slack Σ over degree-2 movers of moves(x) - KF_x (KEYFLIP′ says <= 1 each; the climb pushes towards «moves > 1 + KF»)
  cyc   (mover, state) pairs whose option has a Ξ-edge on a Ξ-cycle of G (L-COMP box 46's cycopt), plus T
  mu    Σ over movers of the number of states whose μ is NOT the least key of x's τ-paths in the W-graph (room for μ to fall)
Fitness = (must-0 sum, objective, -(N + M)); any must-0 > 0 is saved at once (out/CAND_*.json) and re-run on n5v (box 190) by kt241.
Mutations: start, W-target, Ξ-target (mover, -1 or self), gate swap, β-rank swap, β parity, add / remove an option, add a mover.
Resumable: checkpoint OUT/ck_TAG.json (genome, fitness, evals, rng state) every 200 evals; RESUME=1 continues; TLIMIT seconds per call.
Usage: climb241.py TAG SEED EVALS NMAX OBJ [START.json]   (env LNEW; OUT default experiments/red/r241/out; LRED unset)"""
import sys, os, json, random, time, copy, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kt241 as K
OUT = os.environ.get("OUT", os.path.join(HERE, "out")); TLIMIT = float(os.environ.get("TLIMIT", "6600")); RESUME = os.environ.get("RESUME") == "1"

def normalize(G):
    N = G["N"]; flat = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    rk = {q: i for i, q in enumerate(sorted(flat, key=lambda q: G["gate"][q[0]][q[1]]))}
    br_old = {q: G["br"][G["opts"][q[0]][q[1]][2]] for q in flat}; bp_old = {q: G["bp"][G["opts"][q[0]][q[1]][2]] for q in flat}
    brk = {q: i for i, q in enumerate(sorted(flat, key=lambda q: br_old[q]))}
    br = [0] * len(flat); bp = [0] * len(flat)
    for i, q in enumerate(flat):
        G["opts"][q[0]][q[1]][2] = i; br[i] = brk[q]; bp[i] = bp_old[q]
    G["gate"] = [[rk[(x, k)] for k in range(len(G["opts"][x]))] for x in range(N)]; G["br"] = br; G["bp"] = bp
    for x in range(N): G["start"][x] = min(G["start"][x], len(G["opts"][x]) - 1)
    return G

def mutate(G, rng, nmax):
    G = copy.deepcopy(G); N = G["N"]; lev = G["lev"]; by = {}
    for x in range(N): by.setdefault(lev[x], []).append(x)
    for _ in range(rng.choice([1, 1, 1, 2, 3])):
        r = rng.random(); x = rng.randrange(N); k = rng.randrange(len(G["opts"][x])); o = G["opts"][x][k]
        if r < 0.15: G["start"][x] = rng.randrange(len(G["opts"][x]))
        elif r < 0.30:
            if lev[x]: o[0] = rng.choice(by[lev[x] - 1])
        elif r < 0.50: o[1] = rng.choice([-1, x] + list(range(N)))
        elif r < 0.60:
            y = rng.randrange(N); j = rng.randrange(len(G["opts"][y])); G["gate"][x][k], G["gate"][y][j] = G["gate"][y][j], G["gate"][x][k]
        elif r < 0.70:
            j = rng.randrange(len(G["br"])); G["br"][o[2]], G["br"][j] = G["br"][j], G["br"][o[2]]
        elif r < 0.78: G["bp"][o[2]] ^= 1
        elif r < 0.88:
            M = len(G["br"]); G["opts"][x].append([rng.choice(by[lev[x] - 1]) if lev[x] else -1, rng.choice([-1] + list(range(N))), M])
            G["gate"][x].append(rng.random() * M); G["br"].append(rng.random() * M); G["bp"].append(rng.randrange(2))
        elif r < 0.95:
            if len(G["opts"][x]) > 1:
                G["opts"][x].pop(k); G["gate"][x].pop(k)
                if G["start"][x] >= k and G["start"][x] > 0: G["start"][x] -= 1
        else:
            if N < nmax:
                l = rng.choice(sorted(by)); M = len(G["br"]); G["lev"].append(l); G["N"] = N + 1
                G["opts"].append([[rng.choice(by[l - 1]) if l else -1, rng.choice([-1] + list(range(N + 1))), M]])
                G["gate"].append([rng.random() * M]); G["br"].append(rng.random() * M); G["bp"].append(rng.randrange(2)); G["start"].append(0)
                N += 1; by.setdefault(l, []).append(N - 1)
    # rebuild br / bp indexed by option (drop orphans), then rank everything
    flat = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    br = [G["br"][G["opts"][q[0]][q[1]][2]] for q in flat]; bp = [G["bp"][G["opts"][q[0]][q[1]][2]] for q in flat]
    for i, q in enumerate(flat): G["opts"][q[0]][q[1]][2] = i
    G["br"], G["bp"] = br, bp
    return normalize(G)

def fitness(G, obj):
    c, d, info = K.analyse(G)
    m0 = sum(c.values()); M = sum(len(o) for o in G["opts"])
    if obj == "T": v = d["T"]
    elif obj == "nlk": v = d["nlk"] * 1000 + d["T"]
    elif obj == "slack": v = info["slack"] * 1000 + d["T"]
    elif obj == "cyc": v = info["cyc"] * 1000 + d["T"]
    elif obj == "mu": v = info["muroom"] * 1000 + d["T"]
    return (m0, v, -(G["N"] + M)), c, d, info

def main():
    tag, seed, evals, nmax, obj = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
    os.makedirs(OUT, exist_ok=True); ck = os.path.join(OUT, f"ck_{tag}.json"); t0 = time.time()
    if RESUME and os.path.exists(ck):
        S = json.load(open(ck)); rng = random.Random(); rng.setstate((S["rng"][0], tuple(S["rng"][1]), S["rng"][2]))
        best, bf, ev, tot = S["best"], tuple(S["fit"]), S["evals"], S["tot"]
    else:
        rng = random.Random(seed)
        if len(sys.argv) > 6: best = normalize(K.load(sys.argv[6]))
        else: best = K.rand_genome(rng, min(nmax, 10), 4, 3)
        bf = fitness(best, obj)[0]; ev = 0; tot = {k: 0 for k in K.KEYS}
    def save():
        st = rng.getstate()
        json.dump(dict(best=best, fit=list(bf), evals=ev, tot=tot, rng=[st[0], list(st[1]), st[2]], tag=tag, obj=obj, seed=seed), open(ck + ".tmp", "w"))
        os.replace(ck + ".tmp", ck)
    while ev < evals and time.time() - t0 < TLIMIT:
        cand = mutate(best, rng, nmax); ev += 1
        try: f, c, d, info = fitness(cand, obj)
        except AssertionError as e:
            print(f"CLIMB241 {tag} eval {ev} ASSERT {e}", flush=True); continue
        for k in K.KEYS: tot[k] += c[k]
        if f[0] > 0:
            h = hashlib.sha1(json.dumps(cand, sort_keys=True).encode()).hexdigest()[:8]; fn = os.path.join(OUT, f"CAND_{tag}_{h}.json")
            json.dump(cand, open(fn, "w")); print(f"CLIMB241 {tag} eval {ev} CANDIDATE {fn} " + " ".join(f"{k} {v}" for k, v in c.items() if v), flush=True)
            continue                                                  # candidates are kept, never climbed on
        if f >= bf: best, bf = cand, f
        if ev % 200 == 0:
            save(); print(f"CLIMB241 {tag} eval {ev} best {bf} N {best['N']} | must0 so far {sum(tot.values())} | {time.time() - t0:.0f} s", flush=True)
    save(); h = hashlib.sha1(json.dumps(best, sort_keys=True).encode()).hexdigest()[:8]
    fn = os.path.join(OUT, f"BEST_{tag}_{obj}_{bf[1]}_{h}.json"); json.dump(best, open(fn, "w"))
    print(f"CLIMB241 {tag} END evals {ev} best {bf} file {fn} | must0 totals " + " ".join(f"{k} {v}" for k, v in tot.items()) + f" | {time.time() - t0:.0f} s", flush=True)

if __name__ == "__main__": main()
