#!/usr/bin/env python3
"""L-COMP box 39 item 2: Q_(>c) CLIMB at k = 1 inside a fixed N + M band (Lead brief: «k = 1, score Q_(>1) (raw, not divided by size),
bands N + M [280, 320] and [580, 620], 2 seed streams x 1 restart x 200 proposals per band»).
Engine: depth39.measure (MY IDEAL-CYC engine ideal37 + box 206's loud-depth definitions, scope all). SCORE (lexicographic):
(Q_(>C), Q, T) with C = argument (1 by default). Constraints: LO <= N + M <= HI; Xi-feedback number k = 1 (own36.kfvs, as BOX 36-38);
must-0 counters (elfall, ufail) are logged, never optimised. Moves: mut39.mutate (= box38 climb38's move set, unchanged); sideways
acceptance 0.3 as climb36-38. Every new global best is frozen (out/climb39/BEST_<TAG>_Q<..>_NM<..>_<sha8>.json, sha1 in the log) and
RE-RUN on the second engine: L-NEW's depth206.py (read-only worktree in env LNEW, DEP_ALL=1 = scope all); its L-histogram is parsed
and the agreement logged (agree = same loud-depth histogram and T).
CHECKPOINT: OUT.state after every accepted move and every 10 evals; resume continues from the saved genome and step.
GROW mode (STEPS < 0 is not used; separate entry): grow39 TAG LO HI SEED OUT seed.json: growth-only moves (6 add option, 8 add mover),
k = 1 kept, accept iff Q_(>C) does not fall, until N + M >= LO (must stay <= HI); the end genome is frozen.
Usage: climb39.py TAG LO HI RESTARTS STEPS SEED OUT C seed1.json [...] | climb39.py grow TAG LO HI SEED OUT C seed.json"""
import sys, os, json, random, hashlib, time, subprocess, re
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box37"), os.path.join(H, "..", "box36")]
import mut39, depth39, own36
from mut39 import canon, NM, mutate
GROW = sys.argv[1] == "grow"; A = sys.argv[2:] if GROW else sys.argv[1:]
if GROW: TAG, LO, HI, SEED, OUT, C = A[0], int(A[1]), int(A[2]), int(A[3]), A[4], int(A[5]); SEEDS = A[6:]; RESTARTS, STEPS = 1, 10 ** 6
else: TAG, LO, HI, RESTARTS, STEPS, SEED, OUT, C = A[0], int(A[1]), int(A[2]), int(A[3]), int(A[4]), int(A[5]), A[6], int(A[7]); SEEDS = A[8:]
mut39.CAP = HI; CL = os.path.join(H, "out", "climb39"); os.makedirs(CL, exist_ok=True)
QK = lambda r: sum(n for k, n in r["hist"].items() if k > C)


def evaluate(G):
    r = depth39.measure(G); return (QK(r), r["Q"], r["T"]), dict(QC=QK(r), Q=r["Q"], T=r["T"], maxdepth=r["maxdepth"], maxloud=r["maxloud"],
                                                                 hist=r["hist"], elfall=r["elfall"], ufail=r["ufail"], NM=NM(G))


def lnew(fn):
    """second engine: L-NEW depth206.py, scope all; returns (T, histogram) or None."""
    L = os.environ.get("LNEW")
    if not L: return None
    p = subprocess.run([sys.executable, os.path.join(L, "experiments/new/box206/depth206.py"), fn], capture_output=True, text=True,
                       env=dict(os.environ, DEP_ALL="1", ROOT=L), timeout=7200)
    line = [l for l in p.stdout.splitlines() if " T " in l]
    if not line: return dict(error=p.stderr[-300:])
    s = line[-1]; T = int(re.search(r" T (\d+)", s).group(1))
    hist = {int(a): int(b) for a, b in re.findall(r"L(-?\d+) (\d+)", s.split("|")[-1])}
    return dict(T=T, hist=hist)


def ok(G):
    n = NM(G); return n <= HI and (GROW or n >= LO) and own36.kfvs(G, 1) == 1


def sha(G): return hashlib.sha1(json.dumps(G, sort_keys=True).encode()).hexdigest()


def log(s):
    with open(OUT, "a") as f: f.write(s + "\n")


def freeze(G, m, s):
    fn = os.path.join(CL, f"BEST_{TAG}_Q{m['QC']}_T{m['T']}_NM{m['NM']}_{sha(G)[:8]}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
    sh = hashlib.sha1(open(fn, "rb").read()).hexdigest(); l2 = lnew(fn)
    cap = {}                                                   # depth206 prints loud depths >= 8 as L8 (its l. 72: min(d + 1, 9))
    for k, v in m["hist"].items(): cap[min(int(k), 8)] = cap.get(min(int(k), 8), 0) + v
    agree = None if l2 is None or "hist" not in l2 else (l2["T"] == m["T"] and l2["hist"] == cap)
    log(f"BEST {os.path.basename(fn)} sha1 {sh} score {list(s)} {json.dumps(m)} lnew206 {json.dumps(l2)} agree {agree} "
        f"t {time.strftime('%H:%M:%SZ', time.gmtime())}")
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
        acc = (s2[0] >= s[0]) if GROW else (s2 > s or (s2 == s and rng.random() < 0.3))
        if acc:
            G, s, m = H2, s2, m2; st["cur"] = G
            if not GROW and list(s) > st["best"]:
                st["best"] = list(s); st["bestfile"] = freeze(G, m, s)
            save(st)
        elif st["evals"] % 10 == 0: save(st)
    if GROW:
        fn = os.path.join(CL, f"GROWN_{TAG}_Q{m['QC']}_T{m['T']}_NM{m['NM']}_{sha(G)[:8]}.json"); json.dump(G, open(fn, "w"), sort_keys=True)
        log(f"GROWN {os.path.basename(fn)} sha1 {hashlib.sha1(open(fn, 'rb').read()).hexdigest()} {json.dumps(m)} evals {st['evals']}")
    log(f"restart {st['r']} seed {os.path.basename(SEEDS[si])} end {list(s)} {json.dumps(m)} global {st['best']} evals {st['evals']} "
        f"{time.time() - t0:.0f}s")
    st["r"] += 1; st["cur"] = None; st["step"] = 0; save(st)
log("DONE")
