#!/usr/bin/env python3
"""Box 37 (b) climb against ROUTE-FROZEN (docs/new/N5-OUT-box37.md §3): in an H1 ∧ ¬H2 stretch, after a fallback with θ unchanged,
an entry into R or a rise of Ξ at a vertex staying in R (MODE=ent: entries only, NO-ENTRY; MODE=ent2: entries, then R-rises after / at a fallback as the guide). Fitness = (#such transitions, #S4a transitions after a fallback, n-free tiebreak).
One Odd choice vertex asserted (rfrozen.run). Usage: rfclimb.py seed secs out seed.pg"""
import sys, os, random, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "box21")); sys.path.insert(0, os.path.join(HERE, "..", "box31"))
from rfrozen import *
from climb_fix import mutate
from cascclimb import save

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(set(G[2][v])) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, 0)
    acc = {}
    try: run(pg.Game(*G), acc, "c")
    except Exception: return (-1, 0)
    keys = ("S4A_afterfb_entry", "FB_afterfb_entry") if os.environ.get("MODE") == "ent" else ("S4A_afterfb_entry", "S4A_afterfb_Rrise", "FB_afterfb_Rrise", "FB_afterfb_entry")
    v = sum(acc.get(k, 0) for k in keys)
    if os.environ.get("MODE") == "ent2":
        v = acc.get("S4A_afterfb_entry", 0) + acc.get("FB_afterfb_entry", 0)
        return (v, acc.get("S4A_afterfb_Rrise", 0) + acc.get("FB_afterfb_Rrise", 0) + acc.get("FB_before_Rrise", 0))
    return (v, acc.get("S4A_afterfb", 0) + acc.get("FB_afterfb", 0))

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = load(sys.argv[4]); G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f = fit(G); t0 = time.time(); it = 0
    print("start", f, "n", g.n, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f: print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True); save(out + ".pg", H)
            G, f = H, fh
    print("FINAL", f, it, flush=True)
