#!/usr/bin/env python3
"""L-RED box 6 (produced on Opus 5.5): random grafts onto base games: m = 1..MMAX new vertices (random priority <= max
base priority + 3, random owner), each with 1-3 random successors anywhere, plus 0-3 random base -> new edges. Scored with
carry/klow.py in both orders; prints (K-in) violations / incomplete runs and keeps a histogram of minprod.
Usage: rgraft.py SEED COUNT OUTDIR MMAX BASE.pg ..."""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "carry"))
import klow, pg
seed, cnt, out, mmax = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4]); bases = [pg.read(f) for f in sys.argv[5:]]
rng = random.Random(seed); os.makedirs(out, exist_ok=True); hist = {}
for i in range(cnt):
    b = rng.choice(bases); n = b.n; m = rng.randint(1, mmax); N = n + m; mp = max(b.prio) + 3
    prio = list(b.prio) + [rng.randint(0, mp) for _ in range(m)]; own = list(b.owner) + [rng.randint(0, 1) for _ in range(m)]
    succ = [list(s) for s in b.succ] + [sorted({rng.randrange(N) for _ in range(rng.randint(1, 3))}) for _ in range(m)]
    for _ in range(rng.randint(0, 3)):
        u = rng.randrange(n); succ[u] = sorted(set(succ[u]) | {rng.randrange(n, N)})
    g = pg.Game(prio, own, succ)
    for order in ("oink", "stable"):
        try: mm = klow.measure_game(g, order)
        except RecursionError: continue
        if mm["wsearch"] == 0: continue
        k = mm["minprod"]; hist[k] = hist.get(k, 0) + 1
        if mm["incomplete"] or mm["kin"]:
            fn = os.path.join(out, f"rg_{seed}_{i}_{order}.pg"); open(fn, "w").write(pg.dumps(g)); print("HIT", order, mm, fn, flush=True)
print("done", cnt, "minprod histogram", sorted(hist.items()))
