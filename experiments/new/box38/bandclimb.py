#!/usr/bin/env python3
"""Box 38 (c): hill climb against CONJECTURE BAND (docs/new/P-N5-NEB-box38.md §8). At every case-A HN in-phase fallback base a with
c_w(a) ≠ o, follow the θ-constant HN run; count R̄-rises (z ∈ R̄_t ∩ R̄_{t+1}) at levels ≥ rank(c_w(a)) (BAND violations, V), high rises
in the band (H), and such bases (L). Score (V, H, L). Canonical start; mutations from nebclimb.py (MODE TAUW keeps o's self-loop optional).
One Odd choice vertex asserted. Usage: bandclimb.py seed.pg rseed minutes outdir"""
import sys, os, random, time
os.environ.setdefault("MODE", "TAUW")
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from nebclimb import mutate, ok, cw_of
from neb_run import *
from mono import lev
import pg

def score(g):
    rows, o, E = trace(g, None, cap=400); N = len(rows); V = H = L = 0; ro = E.rank[o]
    HN = [r["h1"] and not r["h2"] for r in rows]
    for a in range(N - 1):
        r = rows[a]
        if not (HN[a] and r["fb"] and rows[a + 1]["ph"] == r["ph"]) or ro < E.rank[r["Xi"][o][0]]: continue
        cw = max(cw_of(g, r, o), key=lambda v: E.rank[v])
        if cw == o: continue
        L += 1; rc = E.rank[cw]; k = a
        while k + 1 < N and HN[k + 1] and rows[k + 1]["ph"] == r["ph"] and rows[k + 1]["th"] == r["th"]:
            Rb0, Rb1 = set(rows[k]["R"]) | {o}, set(rows[k + 1]["R"]) | {o}
            for z in (Rb0 & Rb1) - {o}:
                x, y = rows[k]["Xi"][z], rows[k + 1]["Xi"][z]
                if x != y:
                    lv = lev(x, y)
                    if lv >= rc: V += 1
                    elif lv >= ro: H += 1
            k += 1
    return (V, H, L)

if __name__ == "__main__":
    f, seed, mins, outdir = sys.argv[1], int(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    os.makedirs(outdir, exist_ok=True); rng = random.Random(seed); g = load(f); assert ok(g)
    best = score(g); t0 = time.time(); it = 0; print("START", best, flush=True)
    while time.time() - t0 < 60 * mins:
        it += 1; g2, _ = mutate(rng, g, [-1] * g.n)
        if not ok(g2): continue
        try: sc = score(g2)
        except Exception: continue
        if sc >= best:
            if sc > best:
                print("IMPROVE", it, sc, flush=True)
                with open(os.path.join(outdir, f"band_{seed}.pg"), "w") as h:
                    h.write(f"parity {g2.n - 1};\n")
                    for v in range(g2.n): h.write(f"{v} {g2.prio[v]} {g2.owner[v]} {','.join(map(str, g2.succ[v]))};\n")
            best, g = sc, g2
    print("FINAL", best, "after", it, flush=True)
