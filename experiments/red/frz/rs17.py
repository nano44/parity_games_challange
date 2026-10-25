#!/usr/bin/env python3
"""Box 41: random 𝒞^1O games, fast score (shrink17.score: best f − (|U| − 1) per θ-run, KIND=pf, or g − (|U| − 2) per phase,
KIND=hat, over |U| ≥ UMIN). Histogram of the best excess; games with excess ≥ 0 saved (then checked exactly with pfz17.py for
FAIL and nontriviality). Usage: rs17.py seed secs nmin nmax OUTPREFIX"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import shrink17 as S
from soclimb import dump
seed, secs, nmin, nmax, out = int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
rng = random.Random(seed); t0 = time.time(); hist = {}; cnt = 0; saved = 0
while time.time() - t0 < secs:
    n = rng.randint(nmin, nmax); p = rng.random()
    prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.7 else 1 for _ in range(n)]
    succ = [sorted(set(rng.sample(range(n), 1 if owner[v] else rng.choice((1, 2, 2, 3, 3, 4))))) for v in range(n)]
    o = rng.randrange(n); owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 3)))))
    sc = S.score([prio, owner, succ]); cnt += 1
    if sc == S.BAD: continue
    e = sc[0]; hist[e] = hist.get(e, 0) + 1
    if e >= 0 and saved < 50: saved += 1; dump([prio, owner, succ], f"{out}_{saved}.pg"); print("SAVE", saved, sc, flush=True)
print("games", cnt, "hist", sorted(hist.items())[-8:], flush=True)
