#!/usr/bin/env python3
"""Box 22: hill-climb o-acyclic C^1O games (canonical N5 run) for long pure-Y blocks (σ|X frozen; pureY.py).
Fitness = longest pure-Y block - |Y| (-999 outside the class). Usage: climbY.py n seed secs out"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from pureY import split, blocks
from climb_fix import mutate
def fit(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return -999
    g = pg.Game(*G); o = odd[0]; Y = split(g, o)
    if any(w in Y for w in G[2][o]): return -999
    try: st, _ = trace(g, check=False)
    except Exception: return -999
    b, ny, _ = blocks(g, st, o); return b - ny
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    while True:
        owner = [0] * n; o = 0; owner[o] = 1; half = n // 2
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 3))))) for _ in range(n)]
        succ[o] = sorted(set(rng.sample(range(half, n), 2)))
        for v in range(half, n): succ[v] = sorted(set(rng.sample(range(half, n), rng.choice((1, 2, 3)))))   # X = upper half
        G = [[rng.randrange(n + 3) for _ in range(n)], owner, succ]
        f = fit(G)
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
