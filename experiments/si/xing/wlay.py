#!/usr/bin/env python3
"""L-SI box 4: W (the trusted (σ, τ)-play valuation, Engine key) along a joint λ-phase.
Checks: (WM) W_{k+1} ⊵ W_k pointwise at every ARENA transition (PROVED as Lemma WM, docs/si/N5-X-box4.md §8);
(W-LAY) CONJECTURE: between consecutive W-lowering transitions (some vertex's W decreases), at most n − 1 transitions change W.
Reports per longest phase: W-lowering transitions (and whether they are fallbacks), max W-changing run between them, Z.
Usage: wlay.py game.pg ... | wlay.py --rand N lo hi seed [--randstart]"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from zcount import *

def scan_rows(g, rows, ph):
    res = []
    for (x, y) in ph:
        low = []; wm_viol = 0; run = 0; mrun = 0; wch = 0
        for k in range(x, y):
            a, b = rows[k]["Wk"], rows[k + 1]["Wk"]
            dec = any(b[v] < a[v] for v in range(g.n)); ch = a != b
            if dec and not rows[k]["fb"]: wm_viol += 1
            if dec: low.append(k); run = 0
            elif ch: run += 1; wch += 1; mrun = max(mrun, run)
        Z, _ = zsigns(rows, x, y)
        res.append(dict(phase=(x, y), T=y - x, Wlow=len(low), Wlow_fb=sum(1 for k in low if rows[k]["fb"]), WM_viol=wm_viol, maxrun=mrun, Wch=wch, Z=Z))
    return res

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "--rand":
        sys.path.insert(0, os.path.join(ROOT, "experiments/new/box25")); from common import rand_c1o
        RS = "--randstart" in a; N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); agg = dict(games=0, WM_viol=0, Wlow=0, layviol=0, maxrun=0)
        for i in range(N):
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            st = ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0}, {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) if RS else None
            rows, ph = profile(g, st); annotate(g, rows); agg["games"] += 1
            for r in scan_rows(g, rows, ph):
                agg["WM_viol"] += r["WM_viol"]; agg["Wlow"] += r["Wlow"]; agg["layviol"] += r["maxrun"] > g.n - 1; agg["maxrun"] = max(agg["maxrun"], r["maxrun"])
        print(agg); sys.exit()
    for p in a:
        g = load(p); rows, ph = profile(g); assert_run(g, rows); annotate(g, rows)
        r = max(scan_rows(g, rows, ph), key=lambda s: (s["T"]))
        allv = sum(s["WM_viol"] for s in scan_rows(g, rows, ph))
        print(f"{os.path.basename(p):22s} n {g.n:3d}", r, "WM violations (all phases)", allv)
