#!/usr/bin/env python3
"""Box 48 DATA (docs/new/N5-NCONF-box48.md): LEV_C at the returns to a configuration. For each phase and each configuration C visited in
more than one epoch, with s_1 < s_2 < ... the first states of C's epochs: STALL = returns i -> i+1 with LEV_C(s_{i+1}) = LEV_C(s_i) < n - 1
(LEV_C as box47/fbconf.py: the level of Xi in H_C, lambda's cycle nodes). CONJECTURE VIS-RISE says STALL = 0. Also XI_EQ = returns with
Xi(s_{i+1}) = Xi(s_i) (must be 0 if Xi strictly rises in a phase between distinct states, RESULTS R15), UNSAT_VIS_max = the most unsaturated
epochs of one configuration in one phase, SAT_VIS_max = the most epochs of one configuration at LEV_C = n - 1.
Usage: vislev.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files) [--nmax N] [--budget B] [--start F]; VERB=1 prints each STALL."""
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
    n = g.n; lam = rows[a]["lam"]; starts = {}
    for k in range(a, b + 1):
        if k == a or rows[k]["conf"] != rows[k - 1]["conf"]: starts.setdefault(rows[k]["conf"], []).append(k)
    for cf, ss in starts.items():
        if len(ss) < 2: continue
        inc("confs_returning"); inc("returns", len(ss) - 1)
        sb = rows[ss[0]]["sb"]; frame = [[sb[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
        lev = [wlev(E, g, frame, rows[k]["xi"], lam, budget) for k in ss]
        uns = sum(1 for l in lev if l < n - 1); sat = len(lev) - uns
        mx("UNSAT_VIS_max", uns, (nm, n)); mx("SAT_VIS_max", sat, (nm, n))
        for i in range(len(ss) - 1):
            if lev[i + 1] < lev[i]: inc("LEV_DROP_V")
            if tuple(rows[ss[i]]["xi"]) == tuple(rows[ss[i + 1]]["xi"]): inc("XI_EQ")
            if lev[i + 1] == lev[i] < n - 1:
                inc("STALL")
                fbb = any(rows[k]["fb"] for k in range(ss[i], ss[i + 1]))
                inc("STALL_with_fb_between" if fbb else "STALL_no_fb_between")
                if VERB: print(f"STALL {nm} n={n} {'S3' if start is None else 'start'} phase [{a},{b}] C-epochs at {ss[i]} -> {ss[i+1]} LEV_C {lev[i]} fb_between={fbb}", flush=True)
            elif lev[i + 1] > lev[i]: inc("RISE")
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
