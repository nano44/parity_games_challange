#!/usr/bin/env python3
"""Box 24: o-cyclic C^1O, canonical N5. Fitness = (longest run of consecutive PURE transitions (σ|X, τ fixed) inside one joint
λ-phase) - (n - 1). Positive fitness = a pure block exceeding R17's per-phase bound, i.e. a block that is not a one-player
phase. Usage: cycclimb.py n seed secs out"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from pureY import split
from climb_fix import mutate
def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return -999
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if not any(w in Y for w in G[2][o]): return -999                 # o-acyclic: excluded
    try: st, _ = trace(g, check=False)
    except Exception: return -999
    E, Ed = Engine(g), Engine(dual(g)); X = [v for v in range(n) if v not in Y and g.owner[v] == 0]
    lam = [(tuple(x[0] for x in E.evaluate(s)[0]), tuple(y[0] for y in Ed.evaluate(t)[0])) for s, t in st]
    best = cur = 0
    for k in range(len(st) - 1):
        pure = all(st[k + 1][0][v] == st[k][0][v] for v in X) and st[k + 1][1] == st[k][1] and lam[k + 1] == lam[k]
        cur = cur + 1 if pure else 0; best = max(best, cur)
    return best - (n - 1)
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    while True:
        owner = [0] * n; owner[0] = 1
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 3))))) for _ in range(n)]; succ[0] = sorted(set(rng.sample(range(n), 3)))
        G = [[rng.randrange(n + 3) for _ in range(n)], owner, succ]; f = fit(G)
        if f > -999: break
    t0 = time.time(); it = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh = fit(H)
        if fh >= f:
            if fh > f:
                print(f"{time.time()-t0:7.0f}s it {it} fit {fh}", flush=True)
                with open(out + ".pg", "w") as fo:
                    fo.write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
            G, f = H, fh
    print("FINAL", f, it)
