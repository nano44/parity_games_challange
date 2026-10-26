#!/usr/bin/env python3
"""Box 47 DATA for Theorem FB-C (docs/new/N5-FB-box47.md): for an in-phase S4c fallback t -> t+1 whose source t has configuration C = sigma-bar_t|Q,
LEV_C := the level of Xi in the honest frame H_C (G with every Odd v cut to sigma-bar_C(v)), cycle nodes of the phase's lambda.
Checks FBC_V: LEV_C(t+1) < min(LEV_C(t)+1, n-1) (must be 0); per phase and configuration: NS_C = fallbacks with LEV_C(t) < n-1 (<= n-1, must
hold: NSC_V), S_C = fallbacks with LEV_C(t) = n-1. Also LEVC_MONO_V: LEV_C not monotone between two fallbacks of the same C in one phase.
Reports per phase f, the distinct configurations at fallback sources (NCONF), epochs, rho-transitions, and max ratios.
Usage: fbconf.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files) [--nmax N] [--budget B] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box46", "../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from fbwlev import wlev
from levels import load, step, start_pair, Engine, dual, rand_ckO, Unknown
from n5x import readstart
C = {}; M = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v, tag=None):
    if v > M.get(k, (-1,))[0]: M[k] = (v, tag)
VERB = os.environ.get("VERB") == "1"
def run(g, start, budget, nm, cap=3000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), xi=vs, sb=tuple(sb), fb=r[4] if r else 0, conf=tuple(sb[q] for q in Q)))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        if any(rows[k]["fb"] for k in range(i, j)):
            try: phase(g, E, rows, i, j, Q, budget, nm, start)
            except Unknown: inc("UNK_phases")
        i = j + 1
def phase(g, E, rows, a, b, Q, budget, nm, start):
    n = g.n; lam = rows[a]["lam"]; per = {}; lastlev = {}; f = 0
    for t in range(a, b):
        if not rows[t]["fb"]: continue
        f += 1; cf = rows[t]["conf"]; sb = rows[t]["sb"]
        frame = [[sb[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
        l0 = wlev(E, g, frame, rows[t]["xi"], lam, budget); l1 = wlev(E, g, frame, rows[t + 1]["xi"], lam, budget)
        if l1 < min(l0 + 1, n - 1):
            inc("FBC_V")
            if VERB: print(f"FBC_V {nm} {'S3' if start is None else 'rand'} phase [{a},{b}] fallback {t} LEV_C {l0} -> {l1}", flush=True)
        if cf in lastlev and l0 < lastlev[cf]: inc("LEVC_MONO_V")
        lastlev[cf] = l1
        d = per.setdefault(cf, [0, 0]); d[0 if l0 < n - 1 else 1] += 1
    inc("phases_with_fb"); inc("f", f)
    nconf = len(per); ep = 1 + sum(1 for k in range(a, b) if rows[k]["conf"] != rows[k + 1]["conf"])
    rho = sum(1 for k in range(a, b) if any(rows[k]["xi"][q] != rows[k + 1]["xi"][q] for q in Q))
    for cf, (ns, sa) in per.items():
        if ns > n - 1: inc("NSC_V")
        mx("S_C_max", sa, (nm, n)); mx("NS_C_max", ns, (nm, n))
    mx("f_max", f, (nm, n)); mx("NCONF_max", nconf, (nm, n)); mx("f_per_conf_max", round(f / nconf, 2), (nm, n))
    mx("rho_minus_nconf", rho - nconf, (nm, n)); mx("ep_minus_nconf", ep - nconf, (nm, n))
    inc("sum_nconf", nconf); inc("sum_rho", rho); inc("sum_epochs", ep)
if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 34, 1000000; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
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
    print(" ".join(f"{k} {v[0]} {v[1]}" for k, v in sorted(M.items())))
