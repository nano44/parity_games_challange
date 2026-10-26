#!/usr/bin/env python3
"""Hill climb for a LONG PHASE of N5 (maximal run with (lambda_Xi, tau) constant), fitness = longest phase length T (ties: fewer
phases broken toward more iterations). n is held fixed (mutations keep the vertex set). Optional KMAX caps the number of Odd choice
vertices (|Q| <= KMAX). Usage: phclimb.py SEED SECONDS SEEDGAME OUTDIR [KMAX]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x, pg
from n3climb import mutate, rstart

def fit(g, st, kmax):
    if sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) > kmax: return None
    try: E, rows = n3x.trace(g, st)
    except Exception: return None
    keys = [(r["lam"], r["tau"]) for r in rows]; best = 0; i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and keys[j + 1] == keys[i]: j += 1
        best = max(best, j - i); i = j + 1
    return (best, len(rows))

def save(g, st, p):
    pg.write(g, p)
    open(p[:-3] + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{w}" for v, w in st[0].items()) + "\nTAU0 " + " ".join(f"{v}:{w}" for v, w in st[1].items()) + "\n")

def main():
    seed, secs, src, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4]
    kmax = int(sys.argv[5]) if len(sys.argv) > 5 else 10 ** 9
    os.makedirs(out, exist_ok=True); rng = random.Random(seed)
    g = n3x.load(src); st = n3x.readstart(src[:-3] + ".start") if os.path.exists(src[:-3] + ".start") else rstart(rng, g)
    f = fit(g, st, kmax) or (0, 0); t0 = time.time(); it = 0; last = -1
    while time.time() - t0 < secs:
        it += 1; h = mutate(rng, g)
        s2 = rstart(rng, h) if rng.random() < 0.1 else ({v: w for v, w in st[0].items() if w in h.succ[v]}, {v: w for v, w in st[1].items() if w in h.succ[v]})
        f2 = fit(h, s2, kmax)
        if f2 is not None and f2 >= f:
            g, st, f = h, s2, f2
            if f[0] > last: last = f[0]; save(g, st, os.path.join(out, f"best_{seed}.pg")); print(f"{time.time()-t0:.0f}s it {it} T {f[0]} iters {f[1]} n {g.n}", flush=True)
    print("done", it, f)

if __name__ == "__main__":
    main()
