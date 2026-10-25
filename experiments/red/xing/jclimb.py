#!/usr/bin/env python3
"""Box 34 (refined, Lead 21:5xZ): climb on J = non-tame transitions per joint λ-phase (L-SI box 7, Theorem FB: fallbacks per phase
<= n_E(2n-1)(J+1) + J; open core (J-poly)). Counter = L-SI's experiments/si/coarse/tame.py scan_t at l-si 25d16cc8, imported
UNMODIFIED from $LSI (a checkout of that commit). Fitness = (max J in one phase, total J, transitions).
Usage: LSI=<l-si worktree> jclimb.py seed secs OUT seed.pg"""
import sys, os, random, time
L = os.environ.get("LSI") or sys.exit("set LSI"); sys.path.insert(0, os.path.join(L, "experiments/si/coarse"))
import tame as T
sys.path.insert(0, os.path.join(L, "experiments/new/box21")); sys.path.insert(0, os.path.join(L, "experiments/new/box25"))
from climb_fix import mutate
from pureY import split
import pg

def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return (-1, -1, -1), None
    g = pg.Game(*G)
    if not any(w in split(g, odd[0]) for w in G[2][odd[0]]): return (-1, -1, -1), None
    try: c, _ = T.scan_t(g)
    except Exception: return (-1, -1, -1), None
    return (c["maxJ_phase"], c["J"], c["tr"]), c

if __name__ == "__main__":
    seed, secs, out = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]; rng = random.Random(seed)
    g = T.load(sys.argv[4]); n = g.n; G = [list(g.prio), list(g.owner), [list(x) for x in g.succ]]; f, c = fit(G)
    t0 = time.time(); it = 0; print("start", f, flush=True)
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, ch = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh} {ch}", flush=True)
                open(out + ".pg", "w").write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it, flush=True)
