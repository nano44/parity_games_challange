#!/usr/bin/env python3
"""Box 48 DATA for Lemma RET-FB and Corollary VIS (docs/new/N5-NCONF-box48.md).
RET-FB: for an in-phase fallback t -> t+1 and a later C-state s of the same phase, LEV_C(s) >= min(LEV_C(t) + 1, n - 1) (LEV_C in the frame H_C of
s's configuration, lambda's cycle nodes; box47 fbconf). Checked at every epoch start s against the last in-phase fallback source t < s (enough:
LEV_C is non-decreasing): RETFB_V must be 0. MUT=1 control: use t := s - 1 whether or not it is a fallback (must bite, i.e. RETFB_V > 0 somewhere).
VIS: per phase and configuration, V_C (epochs) <= 2n^2 - n + R0_C, R0_C := returns i -> i+1 with no fallback source in [s_i, s_{i+1}) and
LEV_C(s_i) < n - 1. VIS_V must be 0. Also R0 (sum of R0_C) against REV = N_ep - NCONF per phase.
Usage: retfb.py STARTS SEED (--list FILE | files) [--nmax N] [--budget B] [--start F]; VERB=1 prints violations."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
for p in ("../box46", "../box43", "../box21"): sys.path.insert(0, os.path.join(HERE, p))
from fbwlev import wlev
from levels import load, step, start_pair, Engine, dual, Unknown
from n5x import readstart
C = {}; M = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v, tag=None):
    if v > M.get(k, (-1,))[0]: M[k] = (v, tag)
VERB = os.environ.get("VERB") == "1"; MUT = os.environ.get("MUT") == "1"
def run(g, start, budget, nm, cap=5000):
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
        try: phase(g, E, rows, i, j, budget, nm, start)
        except Unknown: inc("UNK_phases")
        i = j + 1
def phase(g, E, rows, a, b, budget, nm, start):
    n = g.n; lam = rows[a]["lam"]; frames = {}; cache = {}
    def lev(k, cf):
        if (k, cf) not in cache:
            if cf not in frames:
                sb = rows[k]["sb"] if rows[k]["conf"] == cf else None
                frames[cf] = [[sb[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
            cache[(k, cf)] = wlev(E, g, frames[cf], rows[k]["xi"], lam, budget)
        return cache[(k, cf)]
    starts = [k for k in range(a, b + 1) if k == a or rows[k]["conf"] != rows[k - 1]["conf"]]
    for k in starts: lev(k, rows[k]["conf"])          # fix each configuration's frame at a C-state first
    lastfb = None; si = 0
    for k in range(a, b + 1):
        if k in starts and k > a:
            t = (k - 1) if MUT else lastfb
            if t is not None:
                cf = rows[k]["conf"]; l0, l1 = lev(t, cf), lev(k, cf); inc("checked")
                if l1 < min(l0 + 1, n - 1):
                    inc("RETFB_V")
                    if VERB: print(f"RETFB_V {nm} n={n} phase [{a},{b}] t={t} s={k} LEV_C {l0} -> {l1}", flush=True)
        if k < b and rows[k]["fb"]: lastfb = k
    ss = {}
    for k in starts: ss.setdefault(rows[k]["conf"], []).append(k)
    fbs = [k for k in range(a, b) if rows[k]["fb"]]; R0 = 0
    for cf, st in ss.items():
        r0 = 0
        for i in range(len(st) - 1):
            if not any(st[i] <= x < st[i + 1] for x in fbs) and lev(st[i], cf) < n - 1: r0 += 1
        if len(st) > 2 * n * n - n + r0: inc("VIS_V")
        R0 += r0
    rev = len(starts) - len(ss)
    inc("sum_R0", R0); inc("sum_REV", rev); mx("R0_max", R0, (nm, n)); mx("REV_max", rev, (nm, n)); mx("REV_minus_R0_max", rev - R0, (nm, n))
if __name__ == "__main__":
    a = sys.argv[1:]; nmax, budget = 34, 1000000; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--budget" in a: i = a.index("--budget"); budget = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [(l.split()[0], load(os.path.join(R0, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
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
