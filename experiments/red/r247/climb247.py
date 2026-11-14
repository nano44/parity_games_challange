#!/usr/bin/env python3
"""L-RED 71 R247: hill-climb for LONG runs of a one-sided strategy-improvement rule (default: candidate RF) on small parity games.
Instance = (game, start): n vertices, owners, DISTINCT priorities 0..n-1 (a permutation: no priority ties), successor sets (each nonempty,
out-degree <= DMAX), a start choice sigma0 for every Even vertex. Score = (iterations of RULE, total switches). Moves: toggle an edge, swap
two priorities, flip an owner, change a start choice, add a vertex (n < NMAX), delete a vertex (n > 2). A move is kept if the score does not
decrease (plateau moves allowed); after STALL moves without a strict gain the climb restarts from a fresh random instance (the best is kept).
Every new best is written to OUT/best_<TAG>.pg (PGSolver format with a '% start v:w ...' line, as gens_red.py writes) with a line in the
log: evals, n, edges, iterations of RULE, iterations of Howard on the same instance, switches.
Usage: climb247.py TAG SEED EVALS NMAX DMAX [RULE=rf] [STALL=3000]    env: OUT (default out), START=file.pg (seed instance), TLIMIT (seconds),
ONEP=1 (every vertex Even: one-player games)"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [HERE, os.path.join(HERE, "..", "r237")]
import si247, rf247
ONEP = os.environ.get("ONEP") == "1"                 # one-player instances only (every vertex Even)
SCORE = os.environ.get("SCORE", "its")               # its: (iterations, switches); ret: (most RETURNS of one vertex to an edge it used
                                                     # before, total returns, iterations)

def rand_inst(rng, n, dmax):
    prio = list(range(n)); rng.shuffle(prio); owner = [0 if ONEP else rng.randint(0, 1) for _ in range(n)]
    succ = [sorted(rng.sample(range(n), rng.randint(1, min(dmax, n)))) for _ in range(n)]
    start = {v: rng.choice(succ[v]) for v in range(n) if owner[v] == 0}
    return dict(prio=prio, owner=owner, succ=succ, start=start)

def fix(I, rng):
    n = len(I["prio"]); st = {}
    for v in range(n):
        if I["owner"][v] == 0:
            w = I["start"].get(v); st[v] = w if w in I["succ"][v] else rng.choice(I["succ"][v])
    I["start"] = st; return I

def mutate(I, rng, nmax, dmax):
    J = dict(prio=list(I["prio"]), owner=list(I["owner"]), succ=[list(s) for s in I["succ"]], start=dict(I["start"])); n = len(J["prio"])
    r = rng.random()
    if r < 0.40:
        v, w = rng.randrange(n), rng.randrange(n)
        if w in J["succ"][v]:
            if len(J["succ"][v]) > 1: J["succ"][v].remove(w)
        elif len(J["succ"][v]) < dmax: J["succ"][v] = sorted(J["succ"][v] + [w])
    elif r < 0.60:
        a, b = rng.randrange(n), rng.randrange(n); J["prio"][a], J["prio"][b] = J["prio"][b], J["prio"][a]
    elif r < 0.70:
        v = rng.randrange(n)
        if not ONEP: J["owner"][v] ^= 1
    elif r < 0.85:
        ev = [v for v in range(n) if J["owner"][v] == 0 and len(J["succ"][v]) > 1]
        if ev: v = rng.choice(ev); J["start"][v] = rng.choice(J["succ"][v])
    elif r < 0.95:
        if n < nmax:
            p = rng.randint(0, n); J["prio"] = [q + 1 if q >= p else q for q in J["prio"]] + [p]; J["owner"].append(0 if ONEP else rng.randint(0, 1))
            J["succ"].append(sorted(rng.sample(range(n + 1), rng.randint(1, min(dmax, n + 1)))))
            for _ in range(rng.randint(1, 2)):
                v = rng.randrange(n)
                if len(J["succ"][v]) < dmax: J["succ"][v] = sorted(set(J["succ"][v]) | {n})
                else: J["succ"][v][rng.randrange(len(J["succ"][v]))] = n; J["succ"][v] = sorted(set(J["succ"][v]))
    else:
        if n > 2:
            x = rng.randrange(n); p = J["prio"][x]; ren = lambda v: v if v < x else v - 1
            succ = []
            for v in range(n):
                if v == x: continue
                s = sorted({ren(w) for w in J["succ"][v] if w != x})
                if not s: s = [ren(rng.choice([w for w in range(n) if w != x]))]
                succ.append(s)
            J["succ"] = succ; J["prio"] = [q - 1 if q > p else q for i, q in enumerate(J["prio"]) if i != x]
            J["owner"] = [o for i, o in enumerate(J["owner"]) if i != x]
            J["start"] = {ren(v): ren(w) for v, w in J["start"].items() if v != x and w != x}
    return fix(J, rng)

def score(I, rule, cap=2000):
    e = si247.SI(I["prio"], I["owner"], I["succ"])
    if SCORE == "ret":                                   # counter-like behaviour: a vertex RETURNS to an edge it used before
        used = {v: {w} for v, w in I["start"].items()}; ret = {}
        def hook(it, sigma, val, sbar, Im, ch):
            for v, w in ch.items():
                if w in used[v]: ret[v] = ret.get(v, 0) + 1
                used[v].add(w)
        r = e.run(rule, dict(I["start"]), cap=cap, hook=hook)
        return (max(ret.values(), default=0), sum(ret.values()), r["its"]), r
    r = e.run(rule, dict(I["start"]), cap=cap)
    return (r["its"], r["switches"]), r

def dumps(I):
    n = len(I["prio"])
    return (f"parity {n - 1};\n" + "".join(f"{v} {I['prio'][v]} {I['owner'][v]} {','.join(map(str, I['succ'][v]))};\n" for v in range(n))
            + "% start " + " ".join(f"{v}:{w}" for v, w in sorted(I["start"].items())) + "\n")

def load(fn):
    prio, owner, succ = si247.parse(fn); st = si247.read_start(fn) or {}
    return dict(prio=prio, owner=owner, succ=succ, start=st)

if __name__ == "__main__":
    tag, seed, evals, nmax, dmax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    rule = sys.argv[6] if len(sys.argv) > 6 else "rf"; stall = int(sys.argv[7]) if len(sys.argv) > 7 else 3000
    out = os.environ.get("OUT", os.path.join(HERE, "out")); os.makedirs(out, exist_ok=True)
    tlimit = float(os.environ.get("TLIMIT", "1e18")); t0 = time.time()
    rng = random.Random(seed); log = open(os.path.join(out, f"climb_{tag}.log"), "a")
    cur = fix(load(os.environ["START"]), rng) if os.environ.get("START") else rand_inst(rng, min(nmax, 6), dmax)
    cs, _ = score(cur, rule); best = (cs, cur); since = 0
    for ev in range(1, evals + 1):
        if time.time() - t0 > tlimit: break
        J = mutate(cur, rng, nmax, dmax); js, r = score(J, rule)
        if r["capped"]:
            log.write(f"CAPPED evals {ev} n {len(J['prio'])} (run longer than the cap; instance saved)\n"); log.flush()
            open(os.path.join(out, f"capped_{tag}_{ev}.pg"), "w").write(dumps(J))
        if js >= cs:
            if js > cs: since = 0
            cur, cs = J, js
        since += 1
        if cs > best[0]:
            best = (cs, cur); h, _ = score(cur, "howard")
            open(os.path.join(out, f"best_{tag}.pg"), "w").write(dumps(cur))
            log.write(f"BEST evals {ev} n {len(cur['prio'])} m {sum(len(s) for s in cur['succ'])} score {SCORE} {rule} {cs} howard {h} secs {time.time() - t0:.0f}\n"); log.flush()
        if since > stall:
            cur = rand_inst(rng, rng.randint(4, nmax), dmax); cs, _ = score(cur, rule); since = 0
    log.write(f"END evals {ev} best {best[0]} n {len(best[1]['prio'])} secs {time.time() - t0:.0f}\n"); log.close()
    print("CLIMB247", tag, "seed", seed, "evals", ev, "nmax", nmax, "dmax", dmax, "rule", rule, "score", SCORE, "best", best[0], "n", len(best[1]["prio"]), flush=True)
