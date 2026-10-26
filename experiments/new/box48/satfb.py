#!/usr/bin/env python3
"""Box 48 DATA for FB-C's saturated term (docs/new/N5-NCONF-box48.md §5): at every in-phase S4c fallback t -> t+1 whose source t is a C-state with
LEV_C(t) = n - 1 (Xi_t = B_C), record: FLAT (Xi_{t+1} = Xi_t), LAST (t+1 is the phase's last state), T1C (t+1 is a C-state), and for every switched
Even x: OWNCN (lambda(x) = x), THRU (z* = sigma_{t+1}(x) has its honest play at t through x). Per phase: SATFB (count), SATFB_max per phase.
CONJECTURE SAT-FB: every saturated fallback is FLAT and LAST (so at most one per phase). Usage as box48/vislev.py."""
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
VERB = os.environ.get("VERB") == "1"
def run(g, start, budget, nm, cap=5000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), s=tuple(s), xi=tuple(vs), sb=tuple(sb), fb=r[4] if r else 0, conf=tuple(sb[q] for q in Q)))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        try: phase(g, E, rows, i, j, budget, nm, start)
        except Unknown: inc("UNK_phases")
        i = j + 1
def thru(g, row, z, x):
    seen = set(); y = z
    while y not in seen:
        if y == x: return True
        seen.add(y); y = row["s"][y] if g.owner[y] == 0 else row["sb"][y]
    return False
def phase(g, E, rows, a, b, budget, nm, start):
    n = g.n; lam = rows[a]["lam"]; cnt = 0
    for t in range(a, b):
        if not rows[t]["fb"]: continue
        sb = rows[t]["sb"]; frame = [[sb[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)]
        if wlev(E, g, frame, rows[t]["xi"], lam, budget) < n - 1: continue
        cnt += 1; inc("SATFB")
        flat = rows[t + 1]["xi"] == rows[t]["xi"]; last = (t + 1 == b); t1c = rows[t + 1]["conf"] == rows[t]["conf"]
        inc("FLAT" if flat else "NONFLAT"); inc("LAST" if last else "NOTLAST"); inc("T1C" if t1c else "T1_NOT_C")
        sw = [x for x in range(n) if g.owner[x] == 0 and rows[t]["s"][x] != rows[t + 1]["s"][x]]
        for x in sw:
            inc("SW"); inc("SW_OWNCN" if lam[x] == x else "SW_NOTCN"); inc("SW_THRU" if thru(g, rows[t], rows[t + 1]["s"][x], x) else "SW_NOTTHRU")
        if VERB and not (flat and last):
            print(f"SATFB {nm} n={n} {'S3' if start is None else 'start'} phase [{a},{b}] t={t} flat={flat} last={last} t1c={t1c} sw={sw} owncn={[lam[x]==x for x in sw]}", flush=True)
    if cnt: mx("SATFB_per_phase_max", cnt, (nm, n))
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
        from levels import rand_ckO
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
