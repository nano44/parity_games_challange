#!/usr/bin/env python3
"""Climb for GATE-LAG re-arming: fitness = (max re-raises of one D-direct gate's offset inside one fallback-free run, longest phase).
Usage: lagclimb.py SEED SECONDS SEEDGAME OUTDIR"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import n3x
from lag import analyse
from n3climb import mutate, rstart
from phclimb import save, readany
def fit(g, st):
    try: return (analyse(g, st, out=lambda *a: None),)
    except Exception: return None
seed, secs, src, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3], sys.argv[4]
os.makedirs(out, exist_ok=True); rng = random.Random(seed)
g = n3x.load(src); st = readany(src, g) or rstart(rng, g); f = fit(g, st) or (0,); t0 = time.time(); it = 0; last = -1
while time.time() - t0 < secs:
    it += 1; h = mutate(rng, g)
    s2 = rstart(rng, h) if rng.random() < 0.1 else ({v: w for v, w in st[0].items() if w in h.succ[v]}, {v: w for v, w in st[1].items() if w in h.succ[v]})
    f2 = fit(h, s2)
    if f2 is not None and f2 >= f:
        g, st, f = h, s2, f2
        if f[0] > last: last = f[0]; save(g, st, os.path.join(out, f"best_{seed}.pg")); print(f"{time.time()-t0:.0f}s it {it} fit {f} n {g.n}", flush=True)
print("done", it, f)
