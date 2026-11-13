#!/usr/bin/env python3
"""L-COMP box 46 item 3: a climb on W_key / (N + M) over Ξ-CYCLIC genomes in a size band (copy of box44/climb44.py: moves, resumability
and band unchanged; the score, the Ξ-cyclic constraint and the best re-measurement differ).
climb46e.py = climb46.py with the objective of the Lead's 03:30Z second B3 climb: W_ess / (N + M), W_ess = the longest window with wess >= 2
(wess = steps inside the window at which a mover enters or leaves a cycle option, or σ̄ moves onto or off an e-face; win46e.measure).
Columns of a BEST line: Wused there is W_ess, Wkey is Wused, run_used is wess_max (names kept from climb46). Proposals whose Ξ-graph (R104) is acyclic are rejected (counted). Every NEW GLOBAL BEST is re-run by sec46.py on
n5b --mode spec and on L-NEW's rfd212 (n5v spec): «agree» and must0 logged; a best with must0 > 0 or agree False is an ALERT line.
--- climb44's header follows ---
L-COMP box 44 item 3: a climb on T3 / (N + M) over genomes in a size band (N + M ≈ 300).
Moves: box38/climb38.py's nine move kinds (canon / rerank / flat / unflat / low / mutate copied unchanged, as climb38 copied climb37's).
Score: T3 / (N + M), compared exactly (cross-multiplication), then T3. No constraint on the Ξ-feedback number or on U(G).
Engines: every proposal is evaluated by the C engine box37/fast37 (T3 = iterations of N5'-xi from S3 on Γ3(G) before the first fallback,
[E-LEV]; validated in boxes 36-38); every NEW GLOBAL BEST is re-run on my text engine through lev44.measure (own34 builder + n5xi44, to
the end), which also evaluates box 209's must-0 counters on it: the line records T3 of both engines, «agree», and the counter sum. A
best whose counter sum is not 0, or on which the engines disagree, is logged as ALERT.
Resumable: OUT.state (restart, step, current genome, best); every proposal's RNG is seeded by (SEED, restart, step).
Usage: climb44.py TAG LO HI RESTARTS STEPS SEED OUT seed1.json [...]"""
import sys, os, json, random, hashlib, time
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box44")]
import win46e as win46, rand46, subprocess
TAG, LO, HI, RESTARTS, STEPS, SEED, OUT = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), sys.argv[7]
CAP = HI; SEEDS = sys.argv[8:]; CL = os.path.join(H, "out", "climb46e"); os.makedirs(CL, exist_ok=True)


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
        lw = [y for y in range(N) if lev[y] == l - 1]
        O.append(dict(x=p, wt=(rng.choice(lw) if l else -1), xt=rng.randrange(-1, N), gate=rng.uniform(-1, M), br=rng.uniform(-1, M), bp=rng.randrange(2), st=True))
        if rng.random() < 0.5:   # let an existing option point at the new mover (else it is unreachable by Xi)
            rng.choice(O[:-1])["xt"] = p
    return unflat(N, lev, O)


def better(a, b):
    """a, b = (Wused, NM, T_key, must0, W_key, run_used): is a's score strictly above b's? (ratio first, then T3)"""
    l, r = a[0] * b[1], b[0] * a[1]
    return l > r or (l == r and (a[0], a[2]) > (b[0], b[2]))


def evaluate(G):
    c, d, first, B = win46.measure(G); return (d["Wess"], NM(G), d["Tkey"], sum(c[k] for k in win46.PREM + win46.K + win46.LV + win46.PL + win46.END), d["Wused"], d["wess_max"])


def ok(G): return LO <= NM(G) <= HI and rand46.xcyclic(G)


def sha(G): return hashlib.sha1(json.dumps(G, sort_keys=True).encode()).hexdigest()


def log(s):
    with open(OUT, "a") as f: f.write(s + "\n")


if __name__ == "__main__":
    stf = OUT + ".state"
    def save(st):
        tmp = stf + ".tmp"; json.dump(st, open(tmp, "w")); os.replace(tmp, stf)
    st = json.load(open(stf)) if os.path.exists(stf) else dict(r=0, step=0, cur=None, best=None, bestfile=None, evals=0)
    seeds = [canon(json.load(open(f))) for f in SEEDS]
    while st["r"] < RESTARTS:
        si = st["r"] % len(seeds)
        if st["cur"] is None: st["cur"] = seeds[si]; st["step"] = 0
        G = st["cur"]; assert ok(G), "seed outside the band"; s = evaluate(G)
        if st["step"] == 0: log("START restart %d seed %s Wused %d NM %d ratio %.4f Tkey %d Wkey %d" % (st["r"], os.path.basename(SEEDS[si]), s[0], s[1], s[0] / s[1], s[2], s[4]))
        while st["step"] < STEPS:
            rng = random.Random("%d-%d-%d" % (SEED, st["r"], st["step"])); st["step"] += 1
            H2 = mutate(G, rng)
            if H2 is None: continue
            if not ok(H2): st["rej"] = st.get("rej", 0) + 1; continue
            try: s2 = evaluate(H2)
            except Exception as e: log("ERROR %s %s" % (type(e).__name__, e)); continue
            st["evals"] += 1
            if better(s2, s) or (s2[0] * s[1] == s[0] * s2[1] and rng.random() < 0.3):
                G, s = H2, s2; st["cur"] = G
                if st["best"] is None or better(s, st["best"]):
                    st["best"] = list(s); fn = os.path.join(CL, "BEST_%s_WE%d_NM%d_%s.json" % (TAG, s[0], s[1], sha(G)[:8])); json.dump(G, open(fn, "w"), sort_keys=True)
                    st["bestfile"] = os.path.basename(fn)
                    o = subprocess.run([sys.executable, os.path.join(H, "sec46.py"), fn], capture_output=True, text=True).stdout.strip()
                    bad = s[3] > 0 or "agree True" not in o
                    log("%sBEST %s Wused %d NM %d ratio %.4f Tkey %d Wkey %d run_used %d must0 %d | %s | restart %d step %d evals %d rejected %d" % ("ALERT " if bad else "", os.path.basename(fn), s[0], s[1], s[0] / s[1], s[2], s[4], s[5], s[3], o, st["r"], st["step"], st["evals"], st.get("rej", 0)))
                save(st)
            elif st["evals"] % 25 == 0: save(st)
        log("END restart %d: current Wused %d NM %d ratio %.4f; best so far %s; evals %d" % (st["r"], s[0], s[1], s[0] / s[1], st["best"], st["evals"]))
        st["r"] += 1; st["cur"] = None; st["step"] = 0; save(st)
    log("DONE %s: best %s %s evals %d" % (TAG, st["best"], st["bestfile"], st["evals"]))
