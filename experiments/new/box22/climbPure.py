#!/usr/bin/env python3
"""Box 24: hill-climb o-acyclic C^1O games for MANY pure transitions (σ|X, τ unchanged) in the canonical N5 run, and check
P-N5-1OA's lemmas L1-L3 (statcheck.check) on every improved instance; any failure is printed as FAIL and the instance saved.
Usage: climbPure.py n seed secs out"""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box21"))
from n5x import *
from pureY import split
from climb_fix import mutate
import statcheck
def evalG(G):
    n = len(G[0]); odd = [v for v in range(n) if G[1][v] == 1 and len(G[2][v]) > 1]
    if len(odd) != 1 or any(not s for s in G[2]): return -999, None
    o = odd[0]; g = pg.Game(*G); Y = split(g, o)
    if any(w in Y for w in G[2][o]): return -999, None
    try: st, _ = trace(g, check=False)
    except Exception: return -999, None
    X = [v for v in range(n) if v not in Y and g.owner[v] == 0]
    return sum(all(st[k + 1][0][v] == st[k][0][v] for v in X) and st[k + 1][1] == st[k][1] for k in range(len(st) - 1)), (g, st)
if __name__ == "__main__":
    n, seed, secs, out = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]; rng = random.Random(seed)
    while True:
        owner = [0] * n; owner[0] = 1; half = n // 3
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 3))))) for _ in range(n)]
        succ[0] = sorted(set(rng.sample(range(n - half, n), 2)))
        for v in range(n - half, n): succ[v] = sorted(set(rng.sample(range(n - half, n), rng.choice((1, 2)))))
        G = [[rng.randrange(n + 3) for _ in range(n)], owner, succ]; f, _ = evalG(G)
        if f > -999: break
    t0 = time.time(); it = 0; fails = 0
    while time.time() - t0 < secs:
        H = mutate(rng, G); it += 1; fh, gs = evalG(H)
        if fh >= f:
            if fh > f:
                cnt = {"pure": 0, "L1_fail": 0, "L2_fail": 0, "blocks": 0, "L3_fail": 0, "maxblock": 0, "games": 1}
                statcheck.check(gs[0], gs[1], cnt)
                bad = cnt["L1_fail"] + cnt["L2_fail"] + cnt["L3_fail"]
                print(f"{time.time()-t0:7.0f}s it {it} pure {fh} maxblock {cnt['maxblock']} {'FAIL ' + str(cnt) if bad else 'L1-L3 ok'}", flush=True)
                with open(out + ("_FAIL%d" % fails if bad else "") + ".pg", "w") as fo:
                    fo.write(f"parity {n-1};\n" + "".join(f"{v} {H[0][v]} {H[1][v]} {','.join(map(str, H[2][v]))};\n" for v in range(n)))
                fails += bool(bad)
            G, f = H, fh
    print("FINAL", f, it, "fails", fails)
