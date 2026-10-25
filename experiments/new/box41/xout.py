#!/usr/bin/env python3
"""Box 41 (b): Lemma X-OUT (docs/new/N5-XOUT-box41.md) on N5 traces. OUT state: in-phase, H1, c_w ≠ c_θ. Per OUT stretch S: f_S (Even
fallbacks with both ends in S), X_S (crossings with both ends in S); check X_S ≤ (|U| − 2)(f_S + 1) + f_S, S4a crossings are entries,
fallback crossings are evictions. DATA only. Usage: xout.py game.pg ... | --rand N nlo nhi seed [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box39")); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *

def fail(acc, k, *info): bump(acc, k); print(k, *info, flush=True)

def analyse(g, acc, name, s0=None):
    rows, o, E = trace(g, s0); N = len(rows); n = g.n; bump(acc, "runs")
    cw = [wvals(g, r["s"], r["t"])[1][o][0] for r in rows]
    a = 0
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"]: b += 1
        ct = rows[a]["Xi"][o][0]; u = sum(1 for z in range(n) if rows[a]["Xi"][z][0] == ct)
        out = [rows[t]["h1"] and cw[t] != ct for t in range(N)]
        t = a
        while t <= b:
            if not out[t]: t += 1; continue
            s = t
            while t + 1 <= b and out[t + 1]: t += 1
            fS = XS = 0; bump(acc, "out_stretches")
            for k in range(s, t):
                Rk, R1 = set(rows[k]["R"]), set(rows[k + 1]["R"]); isfb = rows[k]["fb"] and rows[k]["t"] == rows[k + 1]["t"]
                if isfb: fS += 1
                if Rk != R1:
                    XS += 1
                    if isfb and not R1 <= Rk: fail(acc, "FAIL_FB_ENTERS", name, k)
                    if not isfb and not Rk <= R1: fail(acc, "FAIL_S4A_EVICTS", name, k)
            bump(acc, "X_total", XS); bump(acc, "f_total", fS)
            if XS > (u - 2) * (fS + 1) + fS: fail(acc, "FAIL_XOUT", name, s, t, XS, fS, u)
            mx(acc, "max_X_S", XS, fS, u, name)
            t += 1
        a = b + 1

if __name__ == "__main__":
    acc = {}
    if sys.argv[1] == "--rand":
        from common import rand_c1o
        N, lo, hi, seed = map(int, sys.argv[2:6]); starts = int(sys.argv[6]) if len(sys.argv) > 6 else 0; rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi)
            if g is None: bump(acc, "rejected"); continue
            analyse(g, acc, "rand%d_%d" % (seed, i))
            for _ in range(starts):
                analyse(g, acc, "rand%d_%d_s" % (seed, i), [rng.choice(g.succ[v]) if g.owner[v] == 0 else -1 for v in range(g.n)])
    else:
        for f in sys.argv[1:]:
            try: g = load(f)
            except Exception: bump(acc, "load_fail"); continue
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: bump(acc, "files"); analyse(g, acc, f)
            else: bump(acc, "skipped_not_C1O")
    for key in sorted(acc): print(key, acc[key])
