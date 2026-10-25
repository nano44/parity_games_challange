#!/usr/bin/env python3
"""Box 37 (b) climb against ENTRY-TW (docs/new/N5-OUT-box37.md §3): in an H1 ∧ ¬H2 stretch of a phase, an entry into R after an
eviction with neither θ nor w changing in between. Fitness MODE=sep: (#such events, max epochs in one stretch, max re-entries);
MODE=ep: (max epochs in one HN stretch, -(θ-changes there)) to look for many epochs per θ-change. One Odd choice vertex asserted.
Usage: sepclimb.py seed secs out seed.pg [MODE]"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from epoch import *
from climb_fix import mutate
from cascclimb import save

def fit(G, mode):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0, 0)
    g = pg.Game(*G); acc = {}
    try: run(g, acc, "c")
    except Exception: return (-1, 0, 0)
    ep = acc.get("max_epochs", (0, 0, 0))
    if mode == "ep": return (ep[0], -ep[2] if len(ep) > 2 else 0, 0)
    return (acc.get("sep_NONE", 0) + acc.get("sep_w", 0), ep[0], acc.get("max_vertex_reentries", (0,))[0])

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; mode = sys.argv[5] if len(sys.argv) > 5 else "sep"
    rng = random.Random(seed); g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]
    f = fit(G, mode); t0 = time.time(); it = 0
    print("start", f, "n", g.n, mode, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H, mode)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
