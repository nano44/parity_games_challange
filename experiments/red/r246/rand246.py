#!/usr/bin/env python3
"""L-RED 71 R246: Lemma TOP on RANDOM acyclic genomes (R104's format). For each genome G: the IDEAL key run s_0..s_L (r187 ideal.traj) against
the scheme's run from S3 on Gamma3^top(G) (g3_246 EMODE top; own engine n5s237 through tie246.census_own), in mode spec and mode xi.
Counters (sums over genomes; each «must be 0» is a clause of Lemma TOP):
  mism      genomes whose mover states 0..L of the game run differ from s_0..s_L, or whose run has fewer than L + 1 iterations   (must be 0)
  earlyfb   genomes with a fallback before iteration L + 1, or none at iteration L + 1 when the IDEAL run ends «stuck»            (must be 0)
  tie_pre   S4a ties met at iterations 1..L+1 (S4b ties added)                                                                   (must be 0)
  tie_post  S4a + S4b ties met after iteration L + 1 (DATA: Lemma TOP says nothing there)
  xidiff    genomes on which mode xi's state sequence differs from mode spec's at states 0..L+1                                   (must be 0)
  r104tie   the same tie_pre count on Gamma3(G) with R104's priorities (positive control: must be > 0 overall)
  r104mism  mism on Gamma3(G) with R104's priorities (R117 REACH3; must be 0)
RAND246_CTRL=1: EMODE «top» replaced by a WRONG order inside a level (larger gate index outranks): mism must fire.
Usage: rand246.py SEED COUNT NMAX DMAX DEGMAX [LMIN]   (only genomes with L >= LMIN, default 1, are counted)
       rand246.py files G.json ...                      (the same counters on given acyclic genomes)
       rand246.py perm SEED COUNT LMIN G.json           (random variants of one genome: gate indices and beta ranks re-drawn as random
                                                         bijections with probability 1/2 each, start re-drawn with probability 1/4)"""
import sys, os, random, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237"), os.path.join(HERE, "..", "r187"), os.path.join(HERE, "..", "r178")]
import g3_246, tie246, ideal
CTRL = os.environ.get("RAND246_CTRL", "0")

def genome(rng, nmax, dmax, degmax):
    d = rng.randint(1, dmax); N = rng.randint(d, max(d, nmax))
    lev = list(range(d)) + [rng.randrange(d) for _ in range(N - d)]; rng.shuffle(lev)
    topo = list(range(N)); rng.shuffle(topo); pos = {x: i for i, x in enumerate(topo)}
    opts = []; b = 0
    for x in range(N):
        row = []
        for k in range(rng.randint(1, degmax)):
            wt = -1 if lev[x] == 0 else rng.choice([y for y in range(N) if lev[y] == lev[x] - 1])
            cand = [y for y in range(N) if pos[y] < pos[x]]
            xt = rng.choice(cand) if cand and rng.random() < 0.8 else -1
            row.append([wt, xt, b]); b += 1
        opts.append(row)
    M = b; perm = list(range(M)); rng.shuffle(perm); gate = []; i = 0
    for x in range(N):
        gate.append([perm[i + k] for k in range(len(opts[x]))]); i += len(opts[x])
    br = list(range(M)); rng.shuffle(br); bp = [rng.randint(0, 1) for _ in range(M)]
    return dict(N=N, lev=lev, deg=[len(o) for o in opts], opts=opts, gate=gate, br=br, bp=bp, start=[rng.randrange(len(o)) for o in opts])

def game_run(G, emode, mode):
    prio, own, succ, V = g3_246.build(G, emode)
    if CTRL == "1" and emode == "top":                       # wrong order inside a level: reverse the e-priorities level by level
        O = [(x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))]
        for L in set(G["lev"]):
            es = [V[("e", q)] for q in O if G["lev"][q[0]] == L]; ps = sorted(prio[e] for e in es)
            for e, p in zip(sorted(es, key=lambda e: -prio[e]), ps): prio[e] = p
    rows, states = [], []
    C = tie246.census_own(prio, own, succ, mode, G["N"], rows=rows, states=states)
    return C, rows, [g3_246.mover_state(G, V, s) for s in states]

def source():
    a = sys.argv
    if a[1] == "files":
        for fn in a[2:]: yield json.load(open(fn))
    elif a[1] == "perm":
        rng = random.Random(int(a[2])); G0 = json.load(open(a[5])); M = sum(len(o) for o in G0["opts"])
        while True:
            G = json.loads(json.dumps(G0))
            if rng.random() < 0.5:
                perm = list(range(M)); rng.shuffle(perm); G["gate"] = [[perm[g] for g in row] for row in G0["gate"]]
            if rng.random() < 0.5:
                perm = list(range(M)); rng.shuffle(perm); G["br"] = [perm[r] for r in G0["br"]]
            if rng.random() < 0.25: G["start"] = [rng.randrange(len(o)) for o in G0["opts"]]
            yield G
    else:
        rng = random.Random(int(a[1]))
        while True: yield genome(rng, int(a[3]), int(a[4]), int(a[5]))

if __name__ == "__main__":
    a = sys.argv
    if a[1] == "files": seed, count, nmax, dmax, degmax, lmin = "files", len(a) - 2, 0, 0, 0, 0
    elif a[1] == "perm": seed, count, nmax, dmax, degmax, lmin = "perm" + a[2], int(a[3]), 0, 0, 0, int(a[4])
    else:
        seed, count, nmax, dmax, degmax = map(int, sys.argv[1:6]); lmin = int(sys.argv[6]) if len(sys.argv) > 6 else 1
    src = source(); T = dict(genomes=0, tried=0, sumL=0, maxL=0, mism=0, earlyfb=0, tie_pre=0, tie_post=0, xidiff=0, r104tie=0, r104mism=0, its_top=0, its_r104=0)
    while T["genomes"] < count:
        G = next(src, None)
        if G is None: break
        T["tried"] += 1
        S, why = ideal.traj(G); L = len(S) - 1
        if L < lmin: continue
        T["genomes"] += 1; T["sumL"] += L; T["maxL"] = max(T["maxL"], L)
        C, rows, ms = game_run(G, "top", "spec"); T["its_top"] += C["its"]
        bad = int(len(ms) < L + 1 or [tuple(x) for x in ms[:L + 1]] != [tuple(x) for x in S]); T["mism"] += bad
        fbs = [r["it"] for r in rows if r["fb"]]
        if (fbs and fbs[0] <= L) or (why == "stuck" and (not fbs or fbs[0] != L + 1)): T["earlyfb"] += 1
        T["tie_pre"] += sum(r["ptie"] + r["ctie"] + r["btie"] for r in rows if r["it"] <= L + 1)
        T["tie_post"] += sum(r["ptie"] + r["ctie"] + r["btie"] for r in rows if r["it"] > L + 1)
        C2, rows2, ms2 = game_run(G, "top", "xi"); T["xidiff"] += int(ms2[:L + 2] != ms[:L + 2])
        C3, rows3, ms3 = game_run(G, "r104", "spec"); T["its_r104"] += C3["its"]
        T["r104tie"] += sum(r["ptie"] + r["ctie"] + r["btie"] for r in rows3 if r["it"] <= L + 1)
        T["r104mism"] += int(len(ms3) < L + 1 or [tuple(x) for x in ms3[:L + 1]] != [tuple(x) for x in S])
        if bad and os.environ.get("RAND246_DUMP"): json.dump(G, open(os.path.join(os.environ["RAND246_DUMP"], f"mism_s{seed}_{T['genomes']}.json"), "w"))
    print("RAND246 seed", seed, "nmax", nmax, "dmax", dmax, "degmax", degmax, "lmin", lmin, "ctrl", CTRL, " ".join(f"{k} {v}" for k, v in T.items()), flush=True)
