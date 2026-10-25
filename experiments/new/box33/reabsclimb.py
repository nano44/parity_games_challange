#!/usr/bin/env python3
"""Box 33 climb: re-absorptions. An ABSORPTION is a phase transition where σ̄(o) changes and the old exit x0 moves from F to R
(Lemma OR / ABS-L, docs/new/N5-K-box33.md). Fitness = (max absorptions of one exit inside one phase, max absorptions in one phase,
-n). A counter-like N5 run would push the first key up with n. Usage: reabsclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from dormant import *
from climb_fix import mutate
from cascclimb import save

def absorb_stats(g):
    rows, o = rows_w(g); E = Engine(g); sb = [E.evaluate(tuple(r["s"]))[1][o] for r in rows]; same = {}; ph = {}; p = 0
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["ph"] != b["ph"]: p += 1; continue
        if sb[k] != sb[k + 1] and sb[k] not in a["R"] and sb[k] != o and sb[k] in b["R"]:
            same[(p, sb[k])] = same.get((p, sb[k]), 0) + 1; ph[p] = ph.get(p, 0) + 1
    return (max(same.values()) if same else 0, max(ph.values()) if ph else 0)

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    try: a, b = absorb_stats(pg.Game(*G))
    except Exception: return (-1, 0, 0)
    return (a, b, -n)

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
