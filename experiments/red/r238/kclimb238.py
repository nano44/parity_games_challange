#!/usr/bin/env python3
"""L-RED 68 R238: adversarial hill-climb against box 105's Lemma KEY-MODEL on free genomes. Random genomes give short runs (max L* 6 on
7,300, out/key238.out), so the equivalence «N5 from S3 on Gamma3*(G*) = KEY(G*) state for state» is tested on few transitions; this
climb lengthens KEY's run (and any nonzero counter wins at once).
Score = (s3fail + keyfail + endfail + wrong + keymono of key238.validate, L*). Neutral moves accepted.
Genome mutations (structure of box 104's rand_free kept: levels, option count per mover, b ids): swap two carrier priorities (pb / pe
values, so they stay distinct and >= 6); re-draw an option's W-target (a mover one level down); re-draw an option's Xi-target (a mover
or X); swap two gate indices; change a mover's start; with probability 0.02 restart from a fresh random genome (rand_free).
Every candidate (counter sum > 0) is written to OUT/kcand_TAG_EVAL.json and re-run on the second simulator (box 105's key105.validate:
key105's KEY run vs box 190 n5v spec) and on key105.key_run's states.
Env: as key238.py; CTRL (key238's controls: «best» unchanged, the counters fire); RESUME=1 (OUT/kck_TAG.json, with the rng state); TLIMIT.
Usage: kclimb238.py TAG SEED EVALS DMAX WMAX DEGMAX"""
import sys, os, json, random, time, copy
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import key238 as K
OUT = os.environ.get("OUT", os.path.join(HERE, "out")); TLIMIT = float(os.environ.get("TLIMIT", "1e18"))

def enc(G, pb, pe): return dict(G=G, pb=[[x, k, v] for (x, k), v in pb.items()], pe=[[x, k, v] for (x, k), v in pe.items()])
def dec(d): return d["G"], {(x, k): v for x, k, v in d["pb"]}, {(x, k): v for x, k, v in d["pe"]}

def mutate(G, pb, pe, rng, dm, wm, dg):
    if rng.random() < 0.02: return K.FR.rand_free(rng, dm, wm, dg)
    G = copy.deepcopy(G); pb = dict(pb); pe = dict(pe); N = G["N"]; O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    r = rng.random(); by = {}
    for x in range(N): by.setdefault(G["lev"][x], []).append(x)
    if r < 0.35:
        car = [("b", q) for q in O] + [("e", q) for q in O]; (a, qa), (b, qb) = rng.sample(car, 2)
        da = pb if a == "b" else pe; db = pb if b == "b" else pe; da[qa], db[qb] = db[qb], da[qa]
    elif r < 0.5:
        x, k = rng.choice(O)
        if G["lev"][x] > 0: G["opts"][x][k][0] = rng.choice(by[G["lev"][x] - 1])
    elif r < 0.7:
        x, k = rng.choice(O); G["opts"][x][k][1] = -1 if rng.random() < 0.15 else rng.randrange(N)
    elif r < 0.85:
        (x1, k1), (x2, k2) = rng.sample(O, 2) if len(O) > 1 else (O[0], O[0]); G["gate"][x1][k1], G["gate"][x2][k2] = G["gate"][x2][k2], G["gate"][x1][k1]
    else:
        x = rng.randrange(N); G["start"][x] = rng.randrange(len(G["opts"][x]))
    return G, pb, pe

def ev(G, pb, pe):
    c, L, n, states, its, F1, fbs = K.validate(G, pb, pe); return c, L, n

if __name__ == "__main__":
    tag, seed, evals, dm, wm, dg = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    os.makedirs(OUT, exist_ok=True); ck = os.path.join(OUT, f"kck_{tag}.json"); rng = random.Random(seed); t0 = time.time()
    if os.environ.get("RESUME") == "1" and os.path.exists(ck):
        S = json.load(open(ck)); st = S["rng"]; rng.setstate((st[0], tuple(st[1]), st[2]))
    else:
        G, pb, pe = K.FR.rand_free(rng, dm, wm, dg); c, L, n = ev(G, pb, pe)
        S = dict(tag=tag, seed=seed, cur=enc(G, pb, pe), cur_score=[sum(c.values()), L], best=enc(G, pb, pe), best_score=[sum(c.values()), L],
                 evals=1, tot={k: c[k] for k in K.KEYS}, sumL=L, maxN=n, cands=0, sec=0, seckill=0, hist={}, ctrl=K.CTRL)
    def save():
        st = rng.getstate(); S["rng"] = [st[0], list(st[1]), st[2]]; tmp = ck + ".tmp"; json.dump(S, open(tmp, "w")); os.replace(tmp, ck)
    def line(w):
        print(f"KCLIMB238 {tag} {w}: evals {S['evals']} cur {S['cur_score']} best {S['best_score']} | " + " ".join(f"{k} {S['tot'][k]}" for k in K.KEYS)
              + f" | sum L* {S['sumL']} max |V| {S['maxN']} L* histogram {dict(sorted(S['hist'].items(), key=lambda t: int(t[0])))} | cands {S['cands']} second-simulator kills {S['seckill']} of {S['sec']} | ctrl {S['ctrl']} | {time.time() - t0:.0f} s", flush=True)
    while S["evals"] < evals and time.time() - t0 < TLIMIT:
        G, pb, pe = mutate(*dec(S["cur"]), rng, dm, wm, dg)
        try: c, L, n = ev(G, pb, pe)
        except AssertionError: continue
        S["evals"] += 1; kill = sum(c.values()); S["sumL"] += L; S["maxN"] = max(S["maxN"], n); S["hist"][str(L)] = S["hist"].get(str(L), 0) + 1
        for k in K.KEYS: S["tot"][k] += c[k]
        if kill:
            S["cands"] += 1
            if S["cands"] <= 20:
                json.dump(enc(G, pb, pe), open(os.path.join(OUT, f"kcand_{tag}_{S['evals']}.json"), "w"))
                if not K.CTRL and os.environ.get("BOX105"):
                    sys.path.insert(0, os.environ["BOX105"]); import key105
                    c2, L2, _ = key105.validate(G, pb, pe); S["sec"] += 1; S["seckill"] += int(c2["keyfail"] + c2["endfail"] + c2["s3fail"] + c2["wrong"] > 0)
                    print(f"KCLIMB238 CANDIDATE {tag} eval {S['evals']}: own {c} L* {L} | second simulator (key105 + n5v) {c2} L* {L2}", flush=True)
        sc = [kill, L]
        if sc >= S["cur_score"]: S["cur"] = enc(G, pb, pe); S["cur_score"] = sc
        if sc > S["best_score"]: S["best"] = enc(G, pb, pe); S["best_score"] = sc; json.dump(S["best"], open(os.path.join(OUT, f"kbest_{tag}.json"), "w"))
        if S["evals"] % 500 == 0: save(); line("at")
    save(); line("END" if S["evals"] >= evals else "PAUSED (TLIMIT)")
