#!/usr/bin/env python3
"""L-COMP box 34 (b'), Lead 23:34Z: the INVERSE FRONTIER = the minimum N + M at which C >= c (c = 2..9) or maxm >= m occurs, engine own34
(box 198 / L-SI box 90 counters, [E-LEV], N5'-xi from S3 on Gamma3 up to the first fallback).
Method: greedy DELETION from a seed genome. Moves: (1) delete one option of a mover with >= 2 options; (2) delete one mover y (its options go;
an option whose W-target is y is re-pointed to another mover of y's level, else the move is not allowed; an option whose Xi-target is y gets
Xi-target X = -1). After a move the genome is normalised: movers renumbered, option global indices b = option order, gate indices and
beta ranks re-ranked 0..M-1 in their old order, bp kept per option, start re-indexed (a deleted start option -> option 0).
A move is kept iff the target still holds (C >= c, resp. maxm >= m). Passes in random order (seeded) until a full pass keeps nothing.
Then (optional, --polish P) P random rounds of: 1 non-size mutation (xt := X, start change) + one more deletion pass.
Resumable: OUT.state holds the current genome; each kept move rewrites it. The final genome is frozen to out/frontier/<KEY>_NM<N+M>.json.
Usage: shrink34.py SEED.json KEY(C<c>|m<m>) SEED_RNG OUT [--polish P]
The result is an UPPER bound on the frontier (a local minimum of greedy deletion), not the exact minimum."""
import sys, os, json, random, hashlib, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import own34
a = [x for x in sys.argv[1:] if not x.startswith('--')]
SEEDF, KEY, RS, OUT = a[0], a[1], int(a[2]), a[3]
POLISH = int(sys.argv[sys.argv.index('--polish') + 1]) if '--polish' in sys.argv else 0
what, tgt = ('C', int(KEY[1:])) if KEY[0] == 'C' else ('maxm', int(KEY[1:]))
FR = os.path.join(H, "out", "frontier"); os.makedirs(FR, exist_ok=True)

def size(G): return G["N"] + sum(len(o) for o in G["opts"])

def normalise(N, lev, opts, gate, br, bp, start):
    """opts[x] = list of [wt, xt, oldb]; gate[x][k] old gate value; br, bp dicts oldb -> value."""
    O = [(x, k) for x in range(N) for k in range(len(opts[x]))]
    gr = {q: r for r, q in enumerate(sorted(O, key=lambda q: gate[q[0]][q[1]]))}
    brr = {q: r for r, q in enumerate(sorted(O, key=lambda q: br[opts[q[0]][q[1]][2]]))}
    newopts = []; newgate = []; nbr = []; nbp = []; b = 0
    for x in range(N):
        oo = []; gg = []
        for k in range(len(opts[x])):
            wt, xt, ob = opts[x][k]; oo.append([wt, xt, b]); gg.append(gr[(x, k)]); nbr.append(brr[(x, k)]); nbp.append(bp[ob]); b += 1
        newopts.append(oo); newgate.append(gg)
    return {"N": N, "lev": lev, "opts": newopts, "gate": newgate, "br": nbr, "bp": nbp, "start": start}

def unpack(G):
    br = {o[2]: G["br"][o[2]] for oo in G["opts"] for o in oo}; bp = {o[2]: G["bp"][o[2]] for oo in G["opts"] for o in oo}
    return [list(map(list, oo)) for oo in G["opts"]], [list(g) for g in G["gate"]], br, bp

def del_option(G, x, k):
    if len(G["opts"][x]) < 2: return None
    opts, gate, br, bp = unpack(G); del opts[x][k]; del gate[x][k]
    st = list(G["start"]); s = st[x]; st[x] = 0 if s == k else (s - 1 if s > k else s)
    return normalise(G["N"], list(G["lev"]), opts, gate, br, bp, st)

def del_mover(G, y, rng):
    N, lev = G["N"], G["lev"]; same = [z for z in range(N) if z != y and lev[z] == lev[y]]
    opts, gate, br, bp = unpack(G)
    for x in range(N):
        if x == y: continue
        for o in opts[x]:
            if o[0] == y:
                if not same: return None
                o[0] = rng.choice(same)
            if o[1] == y: o[1] = -1
    ren = lambda z: z if z < 0 else (z - 1 if z > y else z)
    opts2 = []; gate2 = []
    for x in range(N):
        if x == y: continue
        opts2.append([[ren(o[0]), ren(o[1]), o[2]] for o in opts[x]]); gate2.append(gate[x])
    lev2 = [lev[x] for x in range(N) if x != y]; st2 = [G["start"][x] for x in range(N) if x != y]
    if not lev2: return None
    return normalise(N - 1, lev2, opts2, gate2, br, bp, st2)

def ok(G):
    try: m = own34.measure(G, True, extra=True)
    except Exception: return False, None
    return m[what] >= tgt and m["fallback"], m

stf = OUT + ".state"
if os.path.exists(stf): st = json.load(open(stf)); G = st["G"]; rnd = st["round"]
else:
    G = json.load(open(SEEDF)); rnd = 0; good, m = ok(G); assert good, f"seed fails target {KEY}: {m}"
    st = {"G": G, "round": 0}
log = lambda s: open(OUT, "a").write(s + "\n")
log(f"# shrink34 seed {SEEDF} key {KEY} rng {RS} start N+M {size(G)} round {rnd}")
def save(): st["G"] = G; st["round"] = rnd; json.dump(st, open(stf + ".tmp", "w")); os.replace(stf + ".tmp", stf)
def deletion_pass(rng):
    global G
    kept = 0; t0 = time.time()
    moves = [("m", y) for y in range(G["N"])] + [("o", x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
    rng.shuffle(moves)
    # moves refer to the genome at pass start: re-derive targets by name-free index; skip stale indices
    tried = set()
    while True:
        moves = [("m", y) for y in range(G["N"])] + [("o", x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
        rng.shuffle(moves); progress = False
        for mv in moves:
            H2 = del_mover(G, mv[1], rng) if mv[0] == "m" else del_option(G, mv[1], mv[2])
            if H2 is None: continue
            key = hashlib.sha1(json.dumps(H2, sort_keys=True).encode()).hexdigest()
            if key in tried: continue
            tried.add(key); good, m = ok(H2)
            if good:
                G = H2; kept += 1; save(); log(f"kept {mv[0]} N+M {size(G)} {what} {m[what]} C {m['C']} maxm {m['maxm']} T3 {m['T3']} {time.time() - t0:.0f}s")
                progress = True; break
        if not progress: return kept
while rnd <= POLISH:
    rng = random.Random(RS * 1009 + rnd)
    if rnd > 0:                                   # polish: one non-size mutation, kept only if the target still holds
        for _ in range(20):
            H2 = json.loads(json.dumps(G)); x = rng.randrange(H2["N"]); k = rng.randrange(len(H2["opts"][x]))
            if rng.random() < 0.5: H2["opts"][x][k][1] = -1
            else: H2["start"][x] = rng.randrange(len(H2["opts"][x]))
            if ok(H2)[0]: G = H2; break
    deletion_pass(rng); rnd += 1; save()
good, m = ok(G); h = hashlib.sha1(json.dumps(G, sort_keys=True).encode()).hexdigest()
fn = os.path.join(FR, f"{KEY}_NM{size(G)}_{h[:8]}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
log(f"FINAL {KEY} N {G['N']} M {size(G) - G['N']} N+M {size(G)} measure {m} frozen {fn}")
