#!/usr/bin/env python3
"""Box 46 DATA for Lemma HON (docs/new/N5-REC1-box46.md §1): per phase of N5, H := the states with Xi_k = W_k (W-HONEST), H0 := the
D = empty states (a subset), f := in-phase fallbacks. Checks |H| <= f + 4n^2 - 3n (HON_V), no in-phase fallback at a W-honest state
(FBH_V), and, per pair of consecutive W-honest states with a fallback-free gap, that W at the later one dominates W one step after the
earlier one (WM chain; WMC_V). Lemma HON-FB: an in-phase fallback at a W-honest state k is value-flat in W (FBH_FLAT_V), its
target is W-honest (FBH_HON_V) and is the last state of the phase (FBH_LAST_V); all three must be 0.
FBIN / FBIN_GAPS: fallbacks at non-honest states strictly inside a gap between consecutive W-honest states (HON's remaining f term). Reports max |H|, max |H0|, max |H| - |H0| (honest states with D != empty), max |H| / (f + n).
Usage: hon.py STARTS SEED (--list FILE | --rand C LO HI GSEED | files)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box43")); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from multi import rand_ckO
from n5x import load, step, start_pair, Engine, dual, pg
C = {}
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
def wvals(g, s, t):
    succ = [[t[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
    return Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(s))[0]
def check(g, start, cap=4000):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []; inc("runs")
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= cap:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t); w = wvals(g, s, t)
        rows.append(dict(lam=tuple(x[0] for x in vs), t=tuple(t), hon=(tuple(vs) == tuple(w)), d0=all(sb[q] == t[q] for q in Q),
                         w=w, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        phase(g, E, rows, i, j); i = j + 1
def ge(E, a, b): return all(E.key(x) >= E.key(y) for x, y in zip(a, b))
def phase(g, E, rows, a, b):
    inc("phases"); n = g.n
    f = sum(rows[k]["fb"] for k in range(a, b))
    H = [k for k in range(a, b + 1) if rows[k]["hon"]]; H0 = [k for k in H if rows[k]["d0"]]
    if any(rows[k]["d0"] and not rows[k]["hon"] for k in range(a, b + 1)): inc("D0NOTHON_V")
    if len(H) > f + 4 * n * n - 3 * n: inc("HON_V")
    for k in H:
        if k < b and rows[k]["fb"]:
            inc("FBH_V")
            if k + 1 != b: inc("FBH_LAST_V")
            if not rows[k + 1]["hon"]: inc("FBH_HON_V")
            if rows[k + 1]["w"] != rows[k]["w"]: inc("FBH_FLAT_V")
    for h0, h1 in zip(H, H[1:]):
        fin = sum(rows[k]["fb"] for k in range(h0 + 1, h1))
        if fin: inc("FBIN_GAPS"); inc("FBIN", fin)
        if not any(rows[k]["fb"] for k in range(h0, h1)):
            inc("ffpairs")
            if not ge(E, rows[h1]["w"], rows[h0 + 1]["w"]): inc("WMC_V")
    mx("HMAX", len(H)); mx("H0MAX", len(H0)); mx("HNOT0MAX", len(H) - len(H0)); mx("H_OVER_FN", round(len(H) / (f + n), 2))
if __name__ == "__main__":
    a = sys.argv[1:]; K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
        gs = [load(os.path.join(R0, l.split()[0])) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    elif a[0] == "--rand":
        cnt, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        gs = [g for g in (rand_ckO(rng, lo, hi, rng.randint(2, 4)) for _ in range(cnt)) if g is not None]
    else: gs = [load(f) for f in a]
    for g in gs:
        if g.n > 64: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: check(g, st)
            except RecursionError: inc("recursion")
    print(", ".join(f"{k} {v}" for k, v in sorted(C.items())))
