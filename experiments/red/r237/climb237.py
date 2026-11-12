#!/usr/bin/env python3
"""L-RED 67 R237 (2): adversarial hill-climb on Lemma WRAP's step (W4) (L-SI 52 box 104, claude/l-si 26704e01 docs/si/box104-map.md §3).
Goal: a parity game H and a positional Even strategy s0 for which N5'-xi from SPEC S3 on the wrapper W(H, s0) is NOT a Howard run
of H until its first fallback. Base: experiments/red/r236/wr237.py check(H, s0) = WRAP's six must-0 counters (s3fail, nonstd, nohoward,
fbwrong, endwrong, wrong), run on BOTH own engines (w237.py: n5x236 and the SPEC-exact n5s237) and summed. Score = (sum of the six counters, T): any nonzero counter wins at once,
otherwise the climb lengthens Howard's run on H (more states and (step, vertex) pairs under test). Neutral moves are accepted.
A genome is (prio, owner, succ, s0): a parity game with natural priorities in 0..2n+2 (TARGET.md section 1 before its compression
step; random and mutated priorities are drawn from 0..n, a START family keeps its order and parities), every vertex with a successor,
self-loops allowed.
Mutations: owner flip, priority (random / copy another vertex's / +-1), add edge (self-loops included), remove edge, s0 change,
add vertex, delete vertex, swap two indices (index tie-breaks), swap two priorities.
Every candidate (counter sum > 0) is written to OUT/cand_TAG_EVAL.json and re-run on the second engine (box 104's wrap104.check =
box 190 n5v xi on si.Engine). Every XEVERY-th evaluation is cross-checked on the second engine as a sample (xdiff = rows whose
(T, iterations) differ; xkill = second-engine counter sums > 0).
Env: BOX104, LNEW, LRED, LLIT (as wr237.py); CTRL=1 (wr237's control: «best» := worst, nohoward must fire); OUT (default HERE/out);
RESUME=1 (continue from OUT/ck_TAG.json: genome, counts and the rng state, so the stream is the same as an uninterrupted run);
TLIMIT seconds (stop cleanly at a checkpoint); XEVERY (default 50); START=lmcs1|fried2|FILE.json (default: a random game).
Usage: climb237.py TAG SEED EVALS NMAX"""
import sys, os, json, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "r236"))
import w237 as Wm
R = Wm.R
import pg
OUT = os.environ.get("OUT", os.path.join(HERE, "out")); XEVERY = int(os.environ.get("XEVERY", "50")); TLIMIT = float(os.environ.get("TLIMIT", "1e18"))
KEYS = ("s3fail", "nonstd", "nohoward", "fbwrong", "endwrong", "wrong")

def valid(g):
    n = len(g["prio"])
    return (n >= 1 and all(g["succ"][v] and all(0 <= w < n for w in g["succ"][v]) and len(set(g["succ"][v])) == len(g["succ"][v]) for v in range(n))
            and all(0 <= p <= 2 * n + 2 for p in g["prio"]) and all((g["s0"][v] in g["succ"][v]) if g["owner"][v] == 0 else g["s0"][v] == -1 for v in range(n)))

def rand_genome(rng, nmax):
    n = rng.randint(2, min(nmax, 8)); prio = [rng.randint(0, n) for _ in range(n)]; owner = [rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(rng.sample(range(n), rng.randint(1, min(n, 3)))) for _ in range(n)]
    return dict(prio=prio, owner=owner, succ=succ, s0=[rng.choice(succ[v]) if owner[v] == 0 else -1 for v in range(n)])

def fix(g, rng):
    """repair s0 and the priority range after a mutation"""
    n = len(g["prio"])
    for v in range(n):
        g["succ"][v] = sorted(set(g["succ"][v])); g["prio"][v] = min(g["prio"][v], 2 * n + 2)
        if g["owner"][v] == 1: g["s0"][v] = -1
        elif g["s0"][v] not in g["succ"][v]: g["s0"][v] = rng.choice(g["succ"][v])
    return g

def mutate(g, rng, nmax):
    g = json.loads(json.dumps(g)); n = len(g["prio"]); k = rng.randrange(10); v = rng.randrange(n)
    if k == 0: g["owner"][v] ^= 1
    elif k == 1:
        j = rng.randrange(3)
        g["prio"][v] = rng.randint(0, n) if j == 0 else (g["prio"][rng.randrange(n)] if j == 1 else max(0, min(n, g["prio"][v] + rng.choice((-1, 1)))))
    elif k == 2: g["succ"][v].append(rng.randrange(n))
    elif k == 3:
        if len(g["succ"][v]) > 1: g["succ"][v].remove(rng.choice(g["succ"][v]))
    elif k in (4, 5):
        ev = [u for u in range(n) if g["owner"][u] == 0 and len(g["succ"][u]) > 1]
        if ev: u = rng.choice(ev); g["s0"][u] = rng.choice(g["succ"][u])
    elif k == 6:
        if n < nmax:
            g["prio"].append(rng.randint(0, n + 1)); g["owner"].append(rng.randint(0, 1)); g["s0"].append(-1)
            g["succ"].append(rng.sample(range(n + 1), rng.randint(1, min(n + 1, 3))))
            for u in rng.sample(range(n), rng.randint(1, min(n, 2))): g["succ"][u].append(n)
    elif k == 7:
        if n > 2:
            ren = lambda w: w - (w > v)
            for key in ("prio", "owner", "s0"): del g[key][v]
            del g["succ"][v]
            for u in range(n - 1):
                s = [ren(w) for w in g["succ"][u] if w != v]; g["succ"][u] = s if s else [u]
                g["s0"][u] = ren(g["s0"][u]) if g["s0"][u] not in (-1, v) else -1
    elif k == 8:
        w = rng.randrange(n); p = list(range(n)); p[v], p[w] = p[w], p[v]
        g = dict(prio=[g["prio"][p[u]] for u in range(n)], owner=[g["owner"][p[u]] for u in range(n)],
                 succ=[[p[x] for x in g["succ"][p[u]]] for u in range(n)], s0=[(p[g["s0"][p[u]]] if g["s0"][p[u]] != -1 else -1) for u in range(n)])
    else:
        w = rng.randrange(n); g["prio"][v], g["prio"][w] = g["prio"][w], g["prio"][v]
    return fix(g, rng)

def evaluate(g):
    """both own engines (w237): counters summed over the two; T, iterations of the primary engine s (n5s237; Lead 18:33Z), engine x
    (n5x236) second; tiediff = the engines' (T, iterations) differ"""
    H = pg.Game(g["prio"], g["owner"], g["succ"]); c, T, its, wn = Wm.check(H, g["s0"], "s"); c2, T2, its2, _ = Wm.check(H, g["s0"], "x")
    cv, F, itv, _ = Wm.check_spec(H, g["s0"])
    evaluate.tiediff = int((T, its) != (T2, its2)); evaluate.parts = (c, c2, T2, its2, cv, F, itv); evaluate.spec = cv; evaluate.F = F
    cw, w1, _ = Wm.check_w4(H, g["s0"]); evaluate.w4 = cw; evaluate.w1 = w1
    tot = {k: c[k] + c2[k] for k in c}; tot["spec"] = sum(cv.values()); tot["w4"] = sum(cw.values())
    return tot, T, its, wn

def second(g):
    H = pg.Game(g["prio"], g["owner"], g["succ"]); c, T, its, wn = R.WR.check(H, g["s0"])
    return c, T, its, wn

def start_genome(rng, nmax):
    st = os.environ.get("START", "")
    if st.startswith("lmcs"): H, s0 = R.WR.lmcs_game(int(st[4:]), "fig4")
    elif st.startswith("fried"): H, s0, _ = R.WR.fried_game(int(st[5:]))
    elif st: return json.load(open(st))
    else: return rand_genome(rng, nmax)
    # compress priorities to 0..n (order and parity kept: TARGET.md section 1) so that the genome is valid
    order = sorted(set(H.prio)); mp = {}; cur = -1
    for p in order:
        cur += 1
        if cur % 2 != p % 2: cur += 1
        mp[p] = cur
    g = dict(prio=[mp[p] for p in H.prio], owner=list(H.owner), succ=[sorted(set(s)) for s in H.succ], s0=[s0[v] if H.owner[v] == 0 else -1 for v in range(H.n)])
    assert max(g["prio"]) <= 2 * H.n + 2, "priorities do not fit 0..2n+2"
    return g

if __name__ == "__main__":
    tag, seed, evals, nmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    os.makedirs(OUT, exist_ok=True); ck = os.path.join(OUT, f"ck_{tag}.json"); rng = random.Random(seed); t0 = time.time()
    if os.environ.get("RESUME") == "1" and os.path.exists(ck):
        S = json.load(open(ck)); st = S["rng"]; rng.setstate((st[0], tuple(st[1]), st[2]))
        assert (S["seed"], S["nmax"]) == (seed, nmax), "checkpoint belongs to another stream"
    else:
        g = start_genome(rng, nmax); assert valid(g); c, T, its, wn = evaluate(g)
        S = dict(tag=tag, seed=seed, nmax=nmax, ctrl=R.CTRL, evals=1, cur=g, cur_score=[sum(c.values()), T], best=g, best_score=[sum(c.values()), T],
                 tot={k: c[k] for k in KEYS}, pairs=T * sum(1 for o in g["owner"] if o == 0), states=T + 1, sumT=T, maxT=T, maxW=wn, cands=0,
                 x=0, xdiff=0, xkill=0, accepted=0, nhist={}, tiediff=evaluate.tiediff, spec=dict(evaluate.spec), maxF=evaluate.F, sumF=evaluate.F, w4=dict(evaluate.w4), w1=evaluate.w1)
    def save():
        st = rng.getstate(); S["rng"] = [st[0], list(st[1]), st[2]]; tmp = ck + ".tmp"
        json.dump(S, open(tmp, "w")); os.replace(tmp, ck)
    def line(what):
        print(f"CLIMB237 {tag} {what}: evals {S['evals']} cur {S['cur_score']} n {len(S['cur']['prio'])} best {S['best_score']} n_best {len(S['best']['prio'])} | "
              + " ".join(f"{k} {S['tot'][k]}" for k in KEYS) + f" | states {S['states']} pairs {S['pairs']} sumT {S['sumT']} maxT {S['maxT']} max|W| {S['maxW']} "
              f"cands {S['cands']} tiediff(x,s) {S['tiediff']} | N5 (spec, WRAP (v) + Remark 3): " + " ".join(f"{k} {S['spec'][k]}" for k in Wm.SKEYS) + f" maxF {S['maxF']} sumF {S['sumF']} | (W4)-(W6): " + " ".join(f"{k} {S['w4'][k]}" for k in Wm.WKEYS) + f" (W-1 starts {S['w1']}) | second engine: sampled {S['x']} xdiff {S['xdiff']} xkill {S['xkill']} | accepted {S['accepted']} ctrl {S['ctrl']}", flush=True)
    while S["evals"] < evals and time.time() - t0 < TLIMIT:
        g = S["cur"]
        for _ in range(1 + (rng.random() < 0.3) + (rng.random() < 0.1)): g = mutate(g, rng, nmax)
        if not valid(g) or g == S["cur"]: continue
        c, T, its, wn = evaluate(g); S["evals"] += 1; kill = sum(c.values()); sc = [kill, T]; nE = sum(1 for o in g["owner"] if o == 0)
        for k in KEYS: S["tot"][k] += c[k]
        S["tiediff"] += evaluate.tiediff; S["maxF"] = max(S["maxF"], evaluate.F); S["sumF"] += evaluate.F
        for k in Wm.SKEYS: S["spec"][k] += evaluate.spec[k]
        for k in Wm.WKEYS: S["w4"][k] += evaluate.w4[k]
        S["w1"] += evaluate.w1
        S["pairs"] += T * nE; S["states"] += T + 1; S["sumT"] += T; S["maxT"] = max(S["maxT"], T); S["maxW"] = max(S["maxW"], wn)
        S["nhist"][str(len(g["prio"]))] = S["nhist"].get(str(len(g["prio"])), 0) + 1
        if kill:
            S["cands"] += 1; c2, T2, its2, _ = second(g)
            json.dump(dict(genome=g, own=dict(c=c, T=T, iterations=its, parts=evaluate.parts), second=dict(c=c2, T=T2, iterations=its2)), open(os.path.join(OUT, f"cand_{tag}_{S['evals']}.json"), "w"))
            print(f"CLIMB237 {tag} CANDIDATE at eval {S['evals']}: own {c} T {T} its {its} | second engine {c2} T {T2} its {its2}", flush=True)
        elif S["evals"] % XEVERY == 0:
            c2, T2, its2, _ = second(g); S["x"] += 1; S["xdiff"] += int((T2, its2) != (T, its)); S["xkill"] += int(sum(c2.values()) > 0)
            if sum(c2.values()) > 0:
                json.dump(dict(genome=g, own=dict(c=c, T=T, iterations=its), second=dict(c=c2, T=T2, iterations=its2)), open(os.path.join(OUT, f"xcand_{tag}_{S['evals']}.json"), "w"))
                print(f"CLIMB237 {tag} SECOND-ENGINE CANDIDATE at eval {S['evals']}: own {c} T {T} | second {c2} T {T2} its {its2}", flush=True)
        if sc >= S["cur_score"]:
            S["cur"], S["cur_score"] = g, sc; S["accepted"] += 1
            if sc > S["best_score"]: S["best"], S["best_score"] = g, sc; json.dump(g, open(os.path.join(OUT, f"best_{tag}.json"), "w"))
        if S["evals"] % 200 == 0: save(); line("at")
    save(); line("END" if S["evals"] >= evals else "PAUSED (TLIMIT)")
