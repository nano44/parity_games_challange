#!/usr/bin/env python3
"""Box 217 (b) (L-NEW successor 76): hill-climb Xi-acyclic genomes (w movers per level, d levels, degree D) to maximise T_key of the
one-player model 1P(G) (one217.py). Mutations: one option's W-target (a mover one level down), one option's Xi-target (any mover or the
exit; rejected if the Xi-graph gets a cycle), swap two beta ranks, flip one beta parity, swap two gate numbers, flip one start option.
Accept if T_key does not decrease (plateau moves allowed). Restarts from a random genome; optional seed genome (--from G.json).
Output: one line per improvement to stdout; the best genome saved to OUTDIR/rec_w{w}_d{d}_D{D}_s{seed}.json with T_key, Howard, seq.
Usage: climb217.py W D DEG SEED ITERS OUTDIR [--from G.json [--lift K]]   (with --from, W, D, DEG are read from the genome)"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from one217 import OneP, acyclic

XTW = os.environ.get("CLIMB217_XTW") == "1"         # Xi-target = W-target on every option (a «self-fuelling» shape: Xi-edges parallel
                                                    # to W-edges, so a switch below moves the key and the Xi value of the same option)
LADDER = os.environ.get("CLIMB217_LADDER") == "1"   # W-graph fixed to the ladder shape (option j of a level-l mover -> the j-th mover of
                                                    # level l - 1; needs D = w), as the towers (box 215's L^R_d shape); wt is not mutated
def rand_genome(rng, w, d, D):
    lev = [x // w for x in range(w * d)]; N = len(lev); M = N * D; opts = []; i = 0
    perm = list(range(N)); rng.shuffle(perm); pos = {x: p for p, x in enumerate(perm)}
    for x in range(N):
        oo = []
        for j in range(D):
            if LADDER: wt = [y for y in range(N) if lev[y] == lev[x] - 1][j] if lev[x] else -1
            else: wt = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1]) if lev[x] else -1
            if XTW: oo.append([wt, wt, i]); i += 1; continue
            lower = [y for y in range(N) if pos[y] < pos[x]]
            xt = rng.choice(lower + [-1]) if lower and rng.random() < 0.8 else -1
            oo.append([wt, xt, i]); i += 1
        opts.append(oo)
    g = list(range(M)); rng.shuffle(g); gate = [[g[x * D + k] for k in range(D)] for x in range(N)]
    br = list(range(M)); rng.shuffle(br)
    return {"N": N, "lev": lev, "opts": opts, "gate": gate, "br": br, "bp": [rng.randrange(2) for _ in range(M)],
            "start": [rng.randrange(D) for _ in range(N)]}

def mutate(rng, G):
    H = json.loads(json.dumps(G)); N, lev, D = H["N"], H["lev"], len(H["opts"][0]); M = N * D
    r = rng.random(); x = rng.randrange(N); k = rng.randrange(D)
    if r < 0.2 and lev[x] > 0 and not LADDER: H["opts"][x][k][0] = rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
    elif r < 0.45 and not XTW: H["opts"][x][k][1] = rng.choice(list(range(N)) + [-1])
    elif r < 0.6: a, b = rng.randrange(M), rng.randrange(M); H["br"][a], H["br"][b] = H["br"][b], H["br"][a]
    elif r < 0.7: b = rng.randrange(M); H["bp"][b] ^= 1
    elif r < 0.9:
        y, l = rng.randrange(N), rng.randrange(D); H["gate"][x][k], H["gate"][y][l] = H["gate"][y][l], H["gate"][x][k]
    else: H["start"][x] = rng.randrange(D)
    return H if acyclic(H) else None

def lift(G, k):
    """TOP-ADD (L-LOWER's l3/lift.py recipe, claude/l-lower experiments/lower/l3/lift.py, re-implemented for JSON genomes): add k levels of
    w movers on top; each option of a new mover has W-target the matching mover of the level below (option j -> the j-th mover there,
    degree = w), Xi-target the exit, a beta rank above every old one (the new top highest), parity even, fresh gate numbers, start 0."""
    H = json.loads(json.dumps(G)); w = sum(1 for l in H["lev"] if l == 0); D = len(H["opts"][0]); assert D == w, "TOP-ADD needs degree = w"
    for j in range(k):
        top = max(H["lev"]); below = [x for x in range(H["N"]) if H["lev"][x] == top]
        for p in range(w):
            x = H["N"]; H["N"] += 1; H["lev"].append(top + 1); oo = []; gg = []
            for kk in range(D):
                b = len(H["br"]); H["br"].append(len(H["br"])); H["bp"].append(0); oo.append([below[kk], -1, b])
                gg.append(max(v for row in H["gate"] for v in row) + 1 + kk)
            H["opts"].append(oo); H["gate"].append(gg); H["start"].append(0)
    return H

def tkey(G): return len(OneP(G).run("key")) - 1

def enum_depth(G, S=None):
    """k(G) of box 217 §5 A6: the largest k such that some mover of W-level k - 1 switches |K(x)| - 1 times (every key), 0 if none"""
    if S is None: S = OneP(G).run("key")
    N, lev = G["N"], G["lev"]; K = {}
    for x in sorted(range(N), key=lambda x: lev[x]): K[x] = sum((K[w] if w >= 0 else 1) for (w, _, _) in G["opts"][x])
    sw = [sum(1 for t in range(1, len(S)) if S[t][x] != S[t - 1][x]) for x in range(N)]
    return max([lev[x] + 1 for x in range(N) if K[x] > 1 and sw[x] == K[x] - 1] + [0])

OBJ = os.environ.get("CLIMB217_OBJ", "T")      # T: maximise T_key; enum: maximise (k(G), T_key) lexicographically
def score(G):
    S = OneP(G).run("key"); t = len(S) - 1
    return (enum_depth(G, S), t) if OBJ == "enum" else (t,)

if __name__ == "__main__":
    w, d, D, seed, iters, outdir = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
    rng = random.Random(seed)
    if "--from" in sys.argv:
        G = json.load(open(sys.argv[sys.argv.index("--from") + 1])); G = G.get("genome", G)
        if "--lift" in sys.argv: G = lift(G, int(sys.argv[sys.argv.index("--lift") + 1]))
        w = sum(1 for l in G["lev"] if l == 0); d = max(G["lev"]) + 1; D = len(G["opts"][0])
    else:
        G = rand_genome(rng, w, d, D)
    best = score(G); t0 = time.time(); last = 0
    for it in range(iters):
        H = mutate(rng, G)
        if H is None: continue
        t = score(H)
        if t >= best:
            if t > best: print(f"w {w} d {d} D {D} seed {seed} it {it} score {t}", flush=True); last = it
            G, best = H, t
    P = OneP(G); kG = enum_depth(G); best = len(P.run("key")) - 1; rec = {"genome": G, "T_key": best, "enum_depth": kG, "obj": OBJ, "howard": len(P.run("howard")) - 1, "seq": len(P.run("seq")) - 1,
                        "w": w, "d": d, "D": D, "seed": seed, "iters": iters}
    os.makedirs(outdir, exist_ok=True); fn = os.path.join(outdir, f"rec_w{w}_d{d}_D{D}_s{seed}" + ("_enum" if OBJ == "enum" else "") + ("_lad" if LADDER else "") + ("_xtw" if XTW else "") + ".json")
    json.dump(rec, open(fn, "w"), sort_keys=True)
    print(f"FINAL w {w} d {d} D {D} seed {seed} N {G['N']} T_key {best} k {kG} obj {OBJ} howard {rec['howard']} seq {rec['seq']} lastimp {last} "
          f"secs {time.time() - t0:.0f} file {os.path.basename(fn)}", flush=True)
