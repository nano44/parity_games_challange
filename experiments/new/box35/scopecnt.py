#!/usr/bin/env python3
"""Box 36: cross-scope-run counts per phase (docs/new/N5-SCOPE-box36.md). Per phase: scope runs (maximal runs of in-phase transitions
with (h) at k, H2 at k+1, w unchanged), (h)-runs, w-changes between H2 states (WCH), crossings X, toggles T, fallbacks f. Checks
(SCOPE-COUNT) #scope runs <= #(h)-runs + WCH, (WCH-X) WCH <= (n - 2)(X + 1) + X, (RESTARTS) #(h)-runs <= 1 + T + f.
Classifies every in-phase fallback: IN (in a scope run), NH1 (¬H1 at k), H1nH2 (H1 ∧ ¬H2), OTH (H1 ∧ H2 ∧ ¬H3), END ((h) at k, transition
not in scope: ¬H2 at k+1 or w changes). Also checks lambda_U constant whenever tau is. Usage: scopecnt.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from thcls import *

def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def check(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); n = g.n
    hh = [r["h1"] and h2(r["nxt"], o) and r["Xi"][o][0] == r["W"][o][0] for r in rows]
    H2 = [h2(r["nxt"], o) for r in rows]
    for k in range(len(rows) - 1):
        if rows[k]["ph"][2] == rows[k + 1]["ph"][2] and rows[k]["ph"][1] != rows[k + 1]["ph"][1]: bump(acc, "LAMBDA_U_FAIL")
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        ins = [hh[k] and H2[k + 1] and rows[k]["w"] == rows[k + 1]["w"] for k in range(i, j)]
        sr = sum(1 for t in range(len(ins)) if ins[t] and (t == 0 or not ins[t - 1]))
        hr = sum(1 for k in range(i, j + 1) if hh[k] and (k == i or not hh[k - 1]))
        wch = sum(1 for k in range(i, j) if H2[k] and H2[k + 1] and rows[k]["w"] != rows[k + 1]["w"])
        X = sum(1 for k in range(i, j) if set(rows[k]["R"]) != set(rows[k + 1]["R"]))
        T = sum(1 for k in range(i, j) if rows[k]["h1"] != rows[k + 1]["h1"])
        f = sum(1 for k in range(i, j) if rows[k]["fb"])
        if sr > hr + wch: bump(acc, "SCOPECOUNT_FAIL"); acc.setdefault("ex_sc", (name, i))
        if wch > (n - 2) * (X + 1) + X: bump(acc, "WCHX_FAIL"); acc.setdefault("ex_wx", (name, i))
        if hr > 1 + T + f: bump(acc, "RESTARTS_FAIL"); acc.setdefault("ex_rs", (name, i))
        mx(acc, "max_scope_runs_phase", sr, n, name, i); mx(acc, "max_wch_phase", wch, n, X, name, i); mx(acc, "max_hruns_phase", hr, n, name, i)
        for t, k in enumerate(range(i, j)):
            if not rows[k]["fb"]: continue
            r = rows[k]
            if ins[t]: c = "IN"
            elif not r["h1"]: c = "NH1"
            elif not H2[k]: c = "H1nH2"
            elif not hh[k]: c = "OTH"
            else: c = "END_" + ("nH2next" if not H2[k + 1] else "wchg")
            bump(acc, "fb_" + c)
        fo = sum(1 for t, k in enumerate(range(i, j)) if rows[k]["fb"] and not ins[t])
        mx(acc, "max_out_of_scope_fb_phase", fo, n, X, T, name, i)
        bump(acc, "phases"); i = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
            check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
