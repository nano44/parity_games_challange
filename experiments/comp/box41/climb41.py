#!/usr/bin/env python3
"""L-COMP box 41 item 2 (and item 3 with SCORE=sccfloor): DEEP3 CLIMB inside a fixed N + M band (Lead 10:23Z: «score Deep_3 raw
(tiebreak dmax), bands N + M [140, 160] and [280, 320], 2 streams x 200»). Copy of box40/climb40.py (move set box39/mut39.py, sideways
acceptance 0.3, checkpoint OUT.state, GROW mode); changes: engine, score, second engine.
SCORE=deep (default): deep41.census (MY Γ3 engine own34): (DeepInt = Σ_C Deep_3(C) [internal-gate flips after t0(C) charged to depth > 3],
dmaxInt [max charged depth at internal gates after t0], deep [whole-run, every gate: box 100 §5.2's upper bound]).
SCORE=sccfloor (item 3): scc40.census: (locbig / Mbig if big >= FLOOR (env, default 40) else -1, locbig − Mbig, T3).
Second engine on every new best: L-SI cross100.py (worktree of claude/l-si 23d39400 in env LSI100; its engine L-RED how3_232 at
59daaef2 in env RED; LNEW = archive of l-new fcba92fc), CMAX=3: whole-run deep / dmax / qflip / qint / gates must equal mine. For
SCORE=sccfloor the second engine is L-SI scc99.py as in box 40 (env LSI, LSIROOT).
Usage: climb41.py TAG LO HI RESTARTS STEPS SEED OUT C seed1.json [...] | climb41.py grow TAG LO HI SEED OUT C seed.json"""
import sys, os, json, random, hashlib, time, subprocess, re
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box39"), os.path.join(H, "..", "box34"), os.path.join(H, "..", "box36"), os.path.join(H, "..", "box40")]
import mut39, scc40, own36, deep41, ast
from mut39 import canon, NM, mutate
GROW = sys.argv[1] == "grow"; A = sys.argv[2:] if GROW else sys.argv[1:]
if GROW: TAG, LO, HI, SEED, OUT, C = A[0], int(A[1]), int(A[2]), int(A[3]), A[4], int(A[5]); SEEDS = A[6:]; RESTARTS, STEPS = 1, 10 ** 6
else: TAG, LO, HI, RESTARTS, STEPS, SEED, OUT, C = A[0], int(A[1]), int(A[2]), int(A[3]), int(A[4]), int(A[5]), A[6], int(A[7]); SEEDS = A[8:]
mut39.CAP = HI; CL = os.path.join(H, "out", "climb41"); SCORE = os.environ.get("SCORE", "deep"); FLOOR = int(os.environ.get("FLOOR", "40")); os.makedirs(CL, exist_ok=True)
def evaluate(G):
    if SCORE == "sccfloor":
        r = scc40.census(G); rb = r["locbig"] / r["Mbig"] if r["big"] >= FLOOR else -1.0
        return (round(rb, 6), r["locbig"] - r["Mbig"], r["T3"]), dict(rbig=round(rb, 4), NM=NM(G), **r)
    r = deep41.census(G); return (r["DeepInt"], r["dmaxInt"], r["deep"]), dict(NM=NM(G), **r)


def cross(fn):
    """second engine for SCORE=deep: L-SI cross100.py inst fn, CMAX=3; returns its dict (T3 added) or None."""
    L, RED, LN = os.environ.get("LSI100"), os.environ.get("RED"), os.environ.get("LNEW")
    if not (L and RED and LN): return None
    p = subprocess.run([sys.executable, "-I", os.path.join(L, "experiments/si/box100/cross100.py"), "inst", fn], capture_output=True,
                       text=True, env=dict(os.environ, CMAX="3"), timeout=7200)
    w = [l for l in p.stdout.splitlines() if l.split() and l.split()[0].endswith(".json")]
    if not w: return dict(error=p.stderr[-300:])
    d = ast.literal_eval(w[-1][w[-1].index("{"):]); d["T3"] = int(w[-1].split()[2]); return d


def lsi(fn):
    """second engine: L-SI scc99.py (claude/l-si f65e0fb9 worktree in env LSI; ROOT = archive of l-new fcba92fc in env LSIROOT)."""
    L, RT = os.environ.get("LSI"), os.environ.get("LSIROOT")
    if not (L and RT): return None
    p = subprocess.run([sys.executable, os.path.join(L, "experiments/si/box99/scc99.py"), "inst", fn], capture_output=True, text=True,
                       env=dict(os.environ, ROOT=RT), timeout=7200)
    w = [l.split() for l in p.stdout.splitlines() if l.split() and l.split()[0].endswith(".json")]
    if not w: return dict(error=p.stderr[-300:])
    w = w[-1]; return dict(T3=int(w[3]), nscc=int(w[4]), big=int(w[5]), maxloc=int(w[6]), ratio=float(w[7]), locfail=int(w[8]), chainfail=int(w[9]))


def ok(G):
    n = NM(G); return n <= HI and (GROW or n >= LO)


def sha(G): return hashlib.sha1(json.dumps(G, sort_keys=True).encode()).hexdigest()


def log(s):
    with open(OUT, "a") as f: f.write(s + "\n")


def freeze(G, m, s):
    if SCORE == "sccfloor":
        fn = os.path.join(CL, f"BEST_{TAG}_R{m['rbig']}_L{m['locbig']}_M{m['Mbig']}_B{m['big']}_NM{m['NM']}_{sha(G)[:8]}.json")
    else:
        fn = os.path.join(CL, f"BEST_{TAG}_D{m['DeepInt']}_dm{m['dmaxInt']}_W{m['deep']}_NM{m['NM']}_{sha(G)[:8]}.json")
    json.dump(G, open(fn, "w"), sort_keys=True); sh = hashlib.sha1(open(fn, "rb").read()).hexdigest()
    if SCORE == "sccfloor":
        l2 = lsi(fn); agree = None if l2 is None or "T3" not in l2 else all(l2[k] == m[k] for k in ("T3", "nscc", "big", "maxloc", "ratio", "locfail"))
        alert = m["HM"] > 0 or m["ratio"] > 1
    else:
        l2 = cross(fn); agree = None if l2 is None or "T3" not in l2 else all(l2[k] == m[k] for k in ("T3", "deep", "dmax", "qflip", "qint", "gates", "unm"))
        alert = False
    log(f"BEST {os.path.basename(fn)} sha1 {sh} score {list(s)} {json.dumps(m)} engine2 {json.dumps(l2)} agree {agree} "
        f"t {time.strftime('%H:%M:%SZ', time.gmtime())}")
    if alert: log(f"ALERT {os.path.basename(fn)}")
    return os.path.basename(fn)


stf = OUT + ".state"
def save(st):
    tmp = stf + ".tmp"; json.dump(st, open(tmp, "w")); os.replace(tmp, stf)
st = json.load(open(stf)) if os.path.exists(stf) else dict(r=0, step=0, cur=None, best=None, bestfile=None, evals=0)
seeds = [canon(json.load(open(f))) for f in SEEDS]
while st["r"] < RESTARTS:
    si = st["r"] % len(seeds)
    if st["cur"] is None:
        st["cur"] = seeds[si]; st["step"] = 0
    G = st["cur"]; assert ok(G), "seed outside the constraints"; s, m = evaluate(G); t0 = time.time()
    if st["best"] is None:
        st["best"] = list(s); st["bestfile"] = freeze(G, m, s) if not GROW else None; save(st)
    log(f"START r {st['r']} step {st['step']} {list(s)} {json.dumps(m)}")
    while st["step"] < STEPS:
        if GROW and NM(G) >= LO: break
        rng = random.Random(f"{SEED}-{st['r']}-{st['step']}"); st["step"] += 1
        H2 = mutate(G, rng, [6, 8] if GROW else None)
        if H2 is None or not ok(H2): continue
        try: s2, m2 = evaluate(H2)
        except Exception as e: log(f"ERROR {type(e).__name__} {e}"); continue
        st["evals"] += 1
        acc = (s2 >= s) if GROW else (s2 > s or (s2 == s and rng.random() < 0.3))
        if acc:
            G, s, m = H2, s2, m2; st["cur"] = G
            if not GROW and list(s) > st["best"]:
                st["best"] = list(s); st["bestfile"] = freeze(G, m, s)
            save(st)
        elif st["evals"] % 10 == 0: save(st)
    if GROW:
        fn = os.path.join(CL, f"GROWN_{TAG}_S{s[0]}_{s[1]}_{s[2]}_NM{m['NM']}_{sha(G)[:8]}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
        log(f"GROWN {os.path.basename(fn)} sha1 {hashlib.sha1(open(fn, 'rb').read()).hexdigest()} {json.dumps(m)} evals {st['evals']}")
    log(f"restart {st['r']} seed {os.path.basename(SEEDS[si])} end {list(s)} {json.dumps(m)} global {st['best']} evals {st['evals']} "
        f"{time.time() - t0:.0f}s")
    st["r"] += 1; st["cur"] = None; st["step"] = 0; save(st)
log("DONE")
