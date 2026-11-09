#!/usr/bin/env python3
"""L-COMP box 36 (Lead 05:18Z): CLIMB at Xi-feedback number k = 1 with the C engine fast36 (validated, bin/k build = same code + face
counters). Score (lexicographic): (ratio, C, T3), ratio = max over gates of flips(g) / (lamch(g) + 1). Every evaluated genome is also
checked against L-SI box 93 (d) (claude/l-si f723957b): flips(g) <= 2*lamch(g) + 2*min_f nl_f + 1 and flips(g) <= 2*min_f ch_f + 1
(f in {pe_g, pB_g}; ch_f = #t with a value change at f, nl_f = ch_f - lam_f); a violation is frozen at once (out/climb/LSIFAIL_*.json).
Genome space: eg195 schema; b indices canonical (= option order; br/bp carried with their option). Moves: xt of an option; wt of an option
(level >= 1); swap two gate ranks; swap two br ranks; flip bp; start; ADD option (N + M < CAP); DELETE option (mover with >= 2 options);
ADD mover (1 option, inserted after its level; indices shifted). Constraint: k(G) = 1 (own FVS, own36.kfvs); else the move is rejected.
Search: first-improvement hill climbing, sideways moves accepted with prob. 0.3; restarts cycle over the SEEDS (each restart = STEPS
proposals from the seed itself). Every new global best is frozen (out/climb/BEST_<TAG>_r<ratio>_<sha8>.json) and re-run in own36 (Python
engine) before the log line is written (agree flag). Resumable: OUT.state (restart index, global best) after every restart.
Usage: climb36.py TAG CAP RESTARTS STEPS SEED OUT seed1.json [seed2.json ...]"""
import sys, os, json, random, hashlib, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
import fast36, own36
TAG, CAP, RESTARTS, STEPS, SEED, OUT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
SEEDS = sys.argv[7:]; CL = os.path.join(H, "out", "climb"); os.makedirs(CL, exist_ok=True)
BIN = "bin/k"


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
    T, fb, rows = fast36.one(G, bindir=BIN); C = fast36.LASTC; best = None; lsi = []
    for q, f, l in rows:
        chpe, lpe, chpb, lpb = fast36.FACE[q]; nl = min(chpe - lpe, chpb - lpb)
        if f > 2 * l + 2 * nl + 1 or f > 2 * min(chpe, chpb) + 1: lsi.append((q, f, l, fast36.FACE[q]))
        key = (f / (l + 1), f)
        if best is None or key > best[0]: best = (key, q, f, l, fast36.FACE[q])
    (ratio, _), q, f, l, face = best
    return (round(ratio, 6), C, T), dict(T3=T, fb=fb, C=C, gate=list(q), flips=f, lamch=l, face=list(face), lsifail=lsi)


def sha(G): return hashlib.sha1(json.dumps(G, sort_keys=True).encode()).hexdigest()


def log(s):
    with open(OUT, "a") as f: f.write(s + "\n")


stf = OUT + ".state"
st = json.load(open(stf)) if os.path.exists(stf) else dict(r=0, best=None, bestfile=None, evals=0, lsifail=0)
seeds = [canon(json.load(open(f))) for f in SEEDS]
while st["r"] < RESTARTS:
    si = st["r"] % len(seeds); rng = random.Random(SEED * 100003 + st["r"]); t0 = time.time()
    G = seeds[si]; assert own36.kfvs(G, 1) == 1, "seed not k = 1"; s, m = evaluate(G); rbest = (s, m)
    for step in range(STEPS):
        H2 = mutate(G, rng)
        if H2 is None or NM(H2) > CAP or own36.kfvs(H2, 1) != 1: continue
        try: s2, m2 = evaluate(H2)
        except Exception as e: log(f"ERROR {type(e).__name__} {e}"); continue
        st["evals"] += 1
        if m2["lsifail"]:
            st["lsifail"] += 1; fn = os.path.join(CL, f"LSIFAIL_{TAG}_{sha(H2)[:8]}.json"); json.dump(H2, open(fn, "w"), sort_keys=True)
            log(f"LSIFAIL {fn} {json.dumps(m2)}")
        if s2 > s or (s2 == s and rng.random() < 0.3):
            G, s, m = H2, s2, m2
            if s > rbest[0]: rbest = (s, m)
            if st["best"] is None or list(s) > st["best"]:
                st["best"] = list(s); fn = os.path.join(CL, f"BEST_{TAG}_r{s[0]:g}_C{s[1]}_{sha(G)[:8]}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
                st["bestfile"] = os.path.basename(fn); o, rows = own36.census(G, True, True)
                py = [z for z in rows if list(z[0]) == m["gate"]][0]; face = own36.FACE[tuple(m["gate"])]
                agree = (o["T3"], py[1], py[2], o["C"], list(face)) == (m["T3"], m["flips"], m["lamch"], m["C"], m["face"])
                log(f"BEST {os.path.basename(fn)} N+M {NM(G)} k 1 score {list(s)} {json.dumps(m)} own36_agree {agree} t {time.strftime('%H:%M:%SZ', time.gmtime())}")
    st["r"] += 1
    log(f"restart {st['r'] - 1} seed {os.path.basename(SEEDS[si])} best {list(rbest[0])} {json.dumps(rbest[1])} global {st['best']} evals {st['evals']} {time.time() - t0:.0f}s")
    json.dump(st, open(stf + ".tmp", "w")); os.replace(stf + ".tmp", stf)
log(f"SUMMARY {TAG} cap {CAP} restarts {RESTARTS} steps {STEPS} seed {SEED} best {st['best']} {st['bestfile']} evals {st['evals']} lsifail {st['lsifail']}")
