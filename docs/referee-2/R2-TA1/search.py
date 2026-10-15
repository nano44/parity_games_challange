#!/usr/bin/env python3
"""Counterexample search for T-A1 / T-A1' / the psolQ 'iff' claim with the REFEREE-2 implementations only.
Usage: search.py exhaustive n            every game on n vertices, priorities 0..n (TARGET), all owners, all successor sets
       search.py random n K seed [maxpr] [deglist]   K random games
Per game: Zielonka regions; psolB (HKP literal); psolB_max (translation check); psolB with reversed and shuffled colour
orders (HKP Thm 6); psolQ; PA**.  Counts every combination and prints the first witness of each violated implication."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r2lib import *

def run(games, label):
    t0 = time.time()
    cnt, first, total = {}, {}, 0
    rnd = random.Random(7)
    for g in games:
        total += 1
        WE, WO = zielonka(g)
        wB, rB = psolB_hkp(g)
        wBm, rBm = psolB_max(g)
        wBr, rBr = psolB_hkp(g, order=lambda cols: list(reversed(cols)))
        wBs, rBs = psolB_hkp(g, order=lambda cols: rnd.sample(cols, len(cols)))
        wQ, rQ = psolQ_hkp(g)
        p2 = pa2(g, WE, WO)
        sound = all(w is None or (w == 0) == (v in WE) for v, w in enumerate(wB)) and all(w is None or (w == 0) == (v in WE) for v, w in enumerate(wQ))
        rec = {
            "psolB sound": sound,
            "psolB_max == psolB_hkp": (rBm == rB),
            "psolB order-independent (reversed)": (rBr == rB),
            "psolB order-independent (shuffled)": (rBs == rB),
            "psolB complete": not rB,
            "psolQ complete": not rQ,
            "PA**": p2,
            "psolQ ⊇ psolB (complete)": (not rB) <= (not rQ),
        }
        key = (not rB, not rQ, p2)
        cnt[key] = cnt.get(key, 0) + 1
        for k in ("psolB sound", "psolB_max == psolB_hkp", "psolB order-independent (reversed)", "psolB order-independent (shuffled)", "psolQ ⊇ psolB (complete)"):
            if not rec[k] and k not in first:
                first[k] = g.oneline()
        if key not in first:
            first[key] = g.oneline()
    print(f"== {label}: {total} games in {time.time()-t0:.0f}s")
    print("   (psolB complete, psolQ complete, PA**) : count : first example")
    for k in sorted(cnt):
        print(f"   {str(k):24s} : {cnt[k]:8d} : {first[k]}")
    def c(f):
        return sum(v for k, v in cnt.items() if f(*k))
    print("   T-A1  'if'   PA** => psolB complete :", "HOLDS" if c(lambda b, q, p: p and not b) == 0 else f"FAILS ({c(lambda b,q,p: p and not b)})")
    print("   T-A1 'only if' psolB complete => PA** :", "HOLDS" if c(lambda b, q, p: b and not p) == 0 else f"FAILS ({c(lambda b,q,p: b and not p)})")
    print("   T-A1' PA** => psolQ complete :", "HOLDS" if c(lambda b, q, p: p and not q) == 0 else f"FAILS ({c(lambda b,q,p: p and not q)})")
    print("   'psolQ complete => PA**' (the routed iff) :", "HOLDS" if c(lambda b, q, p: q and not p) == 0 else f"FAILS ({c(lambda b,q,p: q and not p)})")
    for k in ("psolB sound", "psolB_max == psolB_hkp", "psolB order-independent (reversed)", "psolB order-independent (shuffled)", "psolQ ⊇ psolB (complete)"):
        print(f"   {k}: " + ("HOLDS" if k not in first else "FAILS, e.g. " + first[k]))

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "exhaustive":
        n = int(sys.argv[2])
        run(all_games(n), f"exhaustive n={n}, priorities 0..{n}")
    else:
        n, K, seed = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
        maxpr = int(sys.argv[5]) if len(sys.argv) > 5 else n
        deg = [int(x) for x in sys.argv[6].split(",")] if len(sys.argv) > 6 else None
        rnd = random.Random(seed)
        run((random_game(rnd, n, maxpr, deg) for _ in range(K)), f"random n={n} K={K} seed={seed} maxpr={maxpr} deg={deg}")
