#!/usr/bin/env python3
"""L-COMP box 37 item (2) (Lead 09:25Z): size-penalised CLIMB on the mover class height of L-NEW box 204 (claude/l-new 3a492186).
SCORE (lexicographic): (D_mov / (N + M), D_mov, T3). The PENALTY is the division by N + M (D_mov per unit of size); no other term.
D_mov = 1 + max over movers of #class changes, from fast37 (Gamma3 N5'-xi run to the first fallback; validated against ideal37 =
IDEAL-CYC text engine: 0 mismatches on 43 pinned genomes, 7 / 2,000 random genomes differ where the Gamma3 run itself differs from
IDEAL-CYC; both IDEAL-CYC engines (mine, L-NEW's) agree on those 7). Every new global best is RE-RUN in ideal37 (the definition) and
frozen as out/climb37/BEST_<TAG>_D<Dmov>_NM<N+M>_<sha8>.json with both values in the log (freezer37.sh logs sha1s in FROZEN.txt).
Constraint: Xi-feedback number k = 1 (own36.kfvs), as in BOX 36. Moves, sideways acceptance (0.3) and restarts: climb36.py (copied
functions canon/rerank/NM/flat/unflat/low/mutate, unchanged). CHECKPOINT: OUT.state after every accepted move and every 25 evals
(restart index, step, current genome, global best); resume continues the current restart from the saved genome and step.
Usage: climb37.py TAG CAP RESTARTS STEPS SEED OUT seed1.json [seed2.json ...]"""
import sys, os, json, random, hashlib, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box36")]
import fast37, ideal37, own36
TAG, CAP, RESTARTS, STEPS, SEED, OUT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
SEEDS = sys.argv[7:]; CL = os.path.join(H, "out", "climb37"); os.makedirs(CL, exist_ok=True)


def canon(G):
    """b := option order; br/bp re-indexed accordingly; gate kept (a permutation over options)."""
    G = json.loads(json.dumps(G)); br, bp = [], []; i = 0
    for x in range(G["N"]):
        for o in G["opts"][x]:
            br.append(G["br"][o[2]]); bp.append(G["bp"][o[2]]); o[2] = i; i += 1
    G["br"], G["bp"] = br, bp; return G


def rerank(vals):
    order = sorted(range(len(vals)), key=lambda i: vals[i]); r = [0] * len(vals)
    for j, i in enumerate(order): r[i] = j
    return r


def NM(G): return G["N"] + sum(len(o) for o in G["opts"])


def flat(G):
    """options as dicts in option order (x, wt, xt, gate, br, bp), plus mover data."""
    O = []
    for x in range(G["N"]):
        for k, (wt, xt, b) in enumerate(G["opts"][x]):
            O.append(dict(x=x, wt=wt, xt=xt, gate=G["gate"][x][k], br=G["br"][b], bp=G["bp"][b], st=(G["start"][x] == k)))
    return O


def unflat(N, lev, O):
    gr = rerank([o["gate"] for o in O]); brr = rerank([o["br"] for o in O])
    G = {"N": N, "lev": list(lev), "opts": [[] for _ in range(N)], "gate": [[] for _ in range(N)], "br": [], "bp": [], "start": [0] * N}
    for i, o in enumerate(sorted(range(len(O)), key=lambda i: (O[i]["x"], i))):
        q = O[o]; x = q["x"]; k = len(G["opts"][x])
        G["opts"][x].append([q["wt"], q["xt"], i]); G["gate"][x].append(gr[o]); G["br"].append(brr[o]); G["bp"].append(q["bp"])
        if q["st"]: G["start"][x] = k
    return G


def low(G, lev, x): return [y for y in range(G["N"]) if lev[y] == lev[x] - 1]


def mutate(G, rng):
    N, lev = G["N"], G["lev"]; O = flat(G); M = len(O); r = rng.randrange(9)
    if r == 0:
        rng.choice(O)["xt"] = rng.randrange(-1, N)
    elif r == 1:
        c = [o for o in O if lev[o["x"]] >= 1]
        if not c: return None
        o = rng.choice(c); o["wt"] = rng.choice(low(G, lev, o["x"]))
    elif r == 2:
        a, b = rng.sample(O, 2); a["gate"], b["gate"] = b["gate"], a["gate"]
    elif r == 3:
        a, b = rng.sample(O, 2); a["br"], b["br"] = b["br"], a["br"]
    elif r == 4:
        rng.choice(O)["bp"] ^= 1
    elif r == 5:
        x = rng.randrange(N); mine = [o for o in O if o["x"] == x]
        if len(mine) < 2: return None
        for o in mine: o["st"] = False
        rng.choice(mine)["st"] = True
    elif r == 6:
        if NM(G) + 1 > CAP: return None
        x = rng.randrange(N)
        O.append(dict(x=x, wt=(rng.choice(low(G, lev, x)) if lev[x] else -1), xt=rng.randrange(-1, N), gate=rng.uniform(-1, M), br=rng.uniform(-1, M),
                      bp=rng.randrange(2), st=False))
    elif r == 7:
        x = rng.randrange(N); mine = [i for i, o in enumerate(O) if o["x"] == x]
        if len(mine) < 2: return None
        i = rng.choice(mine); was = O[i]["st"]; del O[i]
        if was: rng.choice([o for o in O if o["x"] == x])["st"] = True
    else:
        if NM(G) + 2 > CAP: return None
        l = rng.choice(sorted(set(lev)) + [max(lev) + 1]); p = max([y + 1 for y in range(N) if lev[y] <= l], default=0)
        sh = lambda y: y + (y >= p) if y >= 0 else y
        for o in O: o["x"] = sh(o["x"]); o["wt"] = sh(o["wt"]); o["xt"] = sh(o["xt"])
        lev = lev[:p] + [l] + lev[p:]; N += 1
        G2 = {"N": N}; lw = [y for y in range(N) if lev[y] == l - 1]
        O.append(dict(x=p, wt=(rng.choice(lw) if l else -1), xt=rng.randrange(-1, N), gate=rng.uniform(-1, M), br=rng.uniform(-1, M), bp=rng.randrange(2), st=True))
        if rng.random() < 0.5:   # let an existing option point at the new mover (else it is unreachable by Xi)
            rng.choice(O[:-1])["xt"] = p
    return unflat(N, lev, O)


def evaluate(G):
    r = fast37.one(G); nm = NM(G)
    return (round(r["Dmov"] / nm, 6), r["Dmov"], r["T3"]), dict(T3=r["T3"], fb=r["fb"], C=r["C"], Dmov=r["Dmov"], Dmov_x=r["Dmov_x"], NM=nm,
                maxflip=max([f for q, f, l in r["rows"]] or [0]))


def sha(G): return hashlib.sha1(json.dumps(G, sort_keys=True).encode()).hexdigest()


def log(s):
    with open(OUT, "a") as f: f.write(s + "\n")


stf = OUT + ".state"
def save(st):
    tmp = stf + ".tmp"; json.dump(st, open(tmp, "w")); os.replace(tmp, stf)
st = json.load(open(stf)) if os.path.exists(stf) else dict(r=0, step=0, cur=None, best=None, bestfile=None, evals=0)
seeds = [canon(json.load(open(f))) for f in SEEDS]
while st["r"] < RESTARTS:
    si = st["r"] % len(seeds)
    if st["cur"] is None: st["cur"] = seeds[si]; st["step"] = 0
    G = st["cur"]; assert own36.kfvs(G, 1) == 1, "not k = 1"; s, m = evaluate(G); t0 = time.time()
    while st["step"] < STEPS:
        rng = random.Random(f"{SEED}-{st['r']}-{st['step']}"); st["step"] += 1
        H2 = mutate(G, rng)
        if H2 is None or NM(H2) > CAP or own36.kfvs(H2, 1) != 1: continue
        try: s2, m2 = evaluate(H2)
        except Exception as e: log(f"ERROR {type(e).__name__} {e}"); continue
        st["evals"] += 1
        if s2 > s or (s2 == s and rng.random() < 0.3):
            G, s, m = H2, s2, m2; st["cur"] = G
            if st["best"] is None or list(s) > st["best"]:
                st["best"] = list(s); fn = os.path.join(CL, f"BEST_{TAG}_D{m['Dmov']}_NM{m['NM']}_{sha(G)[:8]}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
                st["bestfile"] = os.path.basename(fn); hi = ideal37.heights(G); hi.pop("Dall")
                log(f"BEST {os.path.basename(fn)} score {list(s)} {json.dumps(m)} ideal37 {json.dumps(hi)} agree {hi['Dmov'] == m['Dmov']} t {time.strftime('%H:%M:%SZ', time.gmtime())}")
            save(st)
        elif st["evals"] % 25 == 0: save(st)
    log(f"restart {st['r']} seed {os.path.basename(SEEDS[si])} end {list(s)} {json.dumps(m)} global {st['best']} evals {st['evals']} {time.time() - t0:.0f}s")
    st["r"] += 1; st["cur"] = None; st["step"] = 0; save(st)
log("DONE")
