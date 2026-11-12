#!/usr/bin/env python3
"""L-COMP box 40 item 3: SCC-LIN CLIMB inside a fixed N + M band (Lead 08:42Z: «score loc(C_max)/M_C on the largest SCC, raw H(C) − M_C
as tiebreak, bands N + M [140, 160] and [280, 320], 2 streams x 200 proposals»). Copy of box39/climb39.py; changes: the engine and score.
Engine: scc40.census (MY Γ3 engine own34: N5'-xi from S3 to the first fallback, [E-LEV]; box 99's D(G), f, e, loc, M_C).
SCORE (lexicographic): (locbig / Mbig, locbig − Mbig, T3) on the largest SCC (most movers, then most options). No k constraint (box 99's
SCC-LIN is for every genome; READING of the brief, stated); argument C unused (kept for the command line). Moves: mut39.mutate (= box38 climb38's move set, unchanged); sideways
acceptance 0.3 as climb36-38. Every new global best is frozen (out/climb39/BEST_<TAG>_Q<..>_NM<..>_<sha8>.json, sha1 in the log) and
RE-RUN on the second engine: L-NEW's depth206.py (read-only worktree in env LNEW, DEP_ALL=1 = scope all); its L-histogram is parsed
and the agreement logged (agree = same loud-depth histogram and T).
CHECKPOINT: OUT.state after every accepted move and every 10 evals; resume continues from the saved genome and step.
GROW mode (STEPS < 0 is not used; separate entry): grow39 TAG LO HI SEED OUT seed.json: growth-only moves (6 add option, 8 add mover),
k = 1 kept, accept iff Q_(>C) does not fall, until N + M >= LO (must stay <= HI); the end genome is frozen.
Usage: climb40.py TAG LO HI RESTARTS STEPS SEED OUT C seed1.json [...] | climb40.py grow TAG LO HI SEED OUT C seed.json"""
import sys, os, json, random, hashlib, time, subprocess, re
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box39"), os.path.join(H, "..", "box34"), os.path.join(H, "..", "box36")]
import mut39, scc40, own36
from mut39 import canon, NM, mutate
GROW = sys.argv[1] == "grow"; A = sys.argv[2:] if GROW else sys.argv[1:]
if GROW: TAG, LO, HI, SEED, OUT, C = A[0], int(A[1]), int(A[2]), int(A[3]), A[4], int(A[5]); SEEDS = A[6:]; RESTARTS, STEPS = 1, 10 ** 6
else: TAG, LO, HI, RESTARTS, STEPS, SEED, OUT, C = A[0], int(A[1]), int(A[2]), int(A[3]), int(A[4]), int(A[5]), A[6], int(A[7]); SEEDS = A[8:]
mut39.CAP = HI; CL = os.path.join(H, "out", "climb40"); os.makedirs(CL, exist_ok=True)
def evaluate(G):
    r = scc40.census(G); rb = r["locbig"] / r["Mbig"]
    return (round(rb, 6), r["locbig"] - r["Mbig"], r["T3"]), dict(rbig=round(rb, 4), NM=NM(G), **r)


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
    fn = os.path.join(CL, f"BEST_{TAG}_R{m['rbig']}_L{m['locbig']}_M{m['Mbig']}_NM{m['NM']}_{sha(G)[:8]}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
    sh = hashlib.sha1(open(fn, "rb").read()).hexdigest(); l2 = lsi(fn)
    agree = None if l2 is None or "T3" not in l2 else all(l2[k] == m[k] for k in ("T3", "nscc", "big", "maxloc", "ratio", "locfail"))
    log(f"BEST {os.path.basename(fn)} sha1 {sh} score {list(s)} {json.dumps(m)} lsi99 {json.dumps(l2)} agree {agree} "
        f"t {time.strftime('%H:%M:%SZ', time.gmtime())}")
    if m["HM"] > 0 or m["ratio"] > 1: log(f"ALERT H>M or ratio>1 {os.path.basename(fn)}")
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
        fn = os.path.join(CL, f"GROWN_{TAG}_R{m['rbig']}_NM{m['NM']}_{sha(G)[:8]}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
        log(f"GROWN {os.path.basename(fn)} sha1 {hashlib.sha1(open(fn, 'rb').read()).hexdigest()} {json.dumps(m)} evals {st['evals']}")
    log(f"restart {st['r']} seed {os.path.basename(SEEDS[si])} end {list(s)} {json.dumps(m)} global {st['best']} evals {st['evals']} "
        f"{time.time() - t0:.0f}s")
    st["r"] += 1; st["cur"] = None; st["step"] = 0; save(st)
log("DONE")
