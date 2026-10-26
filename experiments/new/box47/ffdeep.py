#!/usr/bin/env python3
"""Box 47 DATA for CONJECTURE HON-FF (docs/new/N5-XDIR-box47.md §8, docs/new/N5-REC1-box46.md §1a): the W-CARRY of the honest level.
Per phase, for the latest W-honest state h before t whose transition h -> h+1 is an in-phase non-fallback, L := LEV(h) (exact, G_tau frame,
the phase's lambda cycle nodes; box46 fbwlev.wlev). Lemma P's step (HON step 1) gives WLEV(h+1) >= min(L+1, n-1) (STEP_V must be 0).
At every in-phase S4c fallback t -> t+1 at a NON-honest state t after h+1 it records
  CARRY0   WLEV(t) >= min(L+1, n-1) (the bound carried to t)
  DEEP     WLEV(t) >= min(L+1, n-1) > WLEV(t+1): the fallback breaks the carried bound (Lemma FF-LOC: every HON-FF failure has one)
  DEEP_REC for a DEEP fallback with a later W-honest state h' in the phase: LEV(h') >= min(L+1, n-1) anyway (HON-FF survives)
  XI_AT    LEV(t) (the Xi-level itself, permanent) >= min(L+1, n-1) already at t
  FBRISE_V LEV(t+1) < min(L+1, n-1): Lemma FB-RISE (the Xi-level is >= L+1 right after the fallback) fails
  CTRL_T   control at EVERY non-honest in-phase fallback t (honest state before it or not): LEV(t+1) < min(LEV(t)+1, n-1), i.e. the rise
           measured from t's own level instead of an honest state's; FB-RISE does not claim this (its Odd part needs the honest state)
  GEN_V    Lemma FB-RISE, general form, at every non-honest in-phase fallback: LEV(t+1) < min(LEV(t)+1, LEVodd(t), n-1), LEVodd(t) := the
           level counted at Odd start vertices only (must be 0); GEN_ODDBIND: LEVodd(t) <= LEV(t) (the Odd part is what stops the rise)
UNK = level computation over budget. Usage: ffdeep.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files) [--nmax N] [--budget B] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box46", "../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
import hon
from fbwlev import wlev
from levels import load, step, start_pair, Engine, dual, rand_ckO, Unknown
C = {}; EX = []
def levsub(E, g, frame, w, lam, budget, own):
    """as fbwlev.wlev, but a violation counts only at a start vertex x with g.owner[x] == own (paths run through every vertex)."""
    n = g.n; pred = [[] for _ in range(n)]
    for v in range(n):
        for z in frame[v]: pred[z].append(v)
    best = n; cnt = 0
    for c in [c for c in range(n) if lam[c] == c]:
        rc = E.rank[c]; stack = [(c, 0, 0, 1 << c)]
        while stack:
            x, mask, ln, vis = stack.pop(); cnt += 1
            if cnt > budget: raise Unknown()
            if ln >= best: continue
            if g.owner[x] == own and E.key((c, mask, ln)) > E.key(w[x]): best = ln; continue
            if ln == n - 1: continue
            for p in pred[x]:
                if vis >> p & 1: continue
                stack.append((p, mask | (E.bit[p] if E.rank[p] > rc else 0), ln + 1, vis | 1 << p))
    return min(best - 1, n - 1)
def inc(k, v=1): C[k] = C.get(k, 0) + v
VERB = os.environ.get("VERB") == "1"

def run(g, start, budget, nm, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = hon.wvals(g, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), xi=vs, w=w, hon=(tuple(vs) == tuple(w)), fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        try: phase(g, E, rows, i, j, budget, nm, start)
        except Unknown: inc("UNK")
        i = j + 1

def phase(g, E, rows, a, b, budget, nm, start):
    if not any(rows[k]["fb"] and not rows[k]["hon"] for k in range(a, b)): return
    inc("phases_with_nonhon_fb"); n = g.n; lam = rows[a]["lam"]; tau = rows[a]["t"]
    frame = [[tau[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
    lev = {}
    def LV(k, key):
        if (k, key) not in lev: lev[(k, key)] = wlev(E, g, frame, rows[k][key], lam, budget)
        return lev[(k, key)]
    h = None
    for t in range(a, b):
        if rows[t]["hon"] and not rows[t]["fb"]:
            h = t; L = LV(h, "xi"); tgt = min(L + 1, n - 1); inc("honest_steps")
            if LV(h + 1, "w") < tgt: inc("STEP_V")
            continue
        if rows[t]["fb"] and not rows[t]["hon"]:
            inc("nonhon_fb")
            if LV(t + 1, "xi") < min(LV(t, "xi") + 1, n - 1): inc("CTRL_T")   # control: the rise WITHOUT the honest hypothesis (may fail)
            lo = levsub(E, g, frame, rows[t]["xi"], lam, budget, 1)
            if LV(t + 1, "xi") < min(LV(t, "xi") + 1, lo, n - 1):
                inc("GEN_V")
                if VERB: print(f"GEN_V {nm} {'S3' if start is None else 'rand'} phase [{a},{b}] fallback {t} LEV {LV(t, 'xi')} -> {LV(t + 1, 'xi')} LEVodd(t) {lo}", flush=True)
            if lo <= LV(t, "xi"): inc("GEN_ODDBIND")
        if h is None or t <= h or not rows[t]["fb"] or rows[t]["hon"]: continue
        inc("nonhon_fb_after_honest")
        c0 = LV(t, "w") >= tgt; inc("CARRY0", c0)
        if LV(t, "xi") >= tgt: inc("XI_AT")
        if LV(t + 1, "xi") < tgt:
            inc("FBRISE_V")
            if VERB: print(f"FBRISE_V {nm} {'S3' if start is None else 'rand'} phase [{a},{b}] h {h} L {L} fallback {t} LEV(t) {LV(t, 'xi')} LEV(t+1) {LV(t + 1, 'xi')}", flush=True)
        if c0 and LV(t + 1, "w") < tgt:
            inc("DEEP"); hp = next((k for k in range(t + 1, b + 1) if rows[k]["hon"]), None)
            if hp is not None:
                inc("DEEP_NEXTHON"); ok = LV(hp, "xi") >= tgt; inc("DEEP_REC", ok)
                if not ok: inc("HONFF_V")
            if VERB: print(f"DEEP {nm} {'S3' if start is None else 'rand'} phase [{a},{b}] h {h} L {L} fallback {t} WLEV {LV(t, 'w')}->{LV(t + 1, 'w')} "
                           f"LEV(t) {LV(t, 'xi')} next honest {hp} " + ("" if hp is None else f"LEV {LV(hp, 'xi')}"), flush=True)

if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 34, 1000000
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    fixed = None
    if "--start" in a:
        i = a.index("--start"); sys.path.insert(0, os.path.join(HERE, "../box21")); from n5x import readstart; fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [(f"rand{i}", g) for i, g in enumerate(rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, budget, nm)
            except RecursionError: inc("RECERR")
    print(" ".join(f"{k} {v}" for k, v in sorted(C.items())))
