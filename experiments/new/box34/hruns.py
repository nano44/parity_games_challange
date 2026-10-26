#!/usr/bin/env python3
"""Box 34 (L2): maximal (h)-runs per phase and what interrupts them (¬H1 = σ̄(o) ∈ R, ¬H2 = τ(o) ∈ R, ¬H3 = c_w ≠ c_θ), split by
whether a FREEZE window (n consecutive (h) states) has occurred earlier in the phase. Also checks RATCHET (a): after a freeze, every H2
state has H3. Usage: hruns.py game.pg ... | --rand N lo hi seed"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def check(g, acc, name):
    rows, o = rows_w(g); n = g.n
    H1 = [r["h1"] for r in rows]; H2 = [h2(r["nxt"], o) for r in rows]; H3 = [r["Xi"][o][0] == r["W"][o][0] for r in rows]
    hh = [H1[i] and H2[i] and H3[i] for i in range(len(rows))]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        frozen = False; runs = 0; runlen = 0; nruns_after = 0; prev = False
        for k in range(i, j + 1):
            if hh[k]:
                runlen += 1
                if not prev: runs += 1; nruns_after += frozen
                if runlen >= n: frozen = True
            else:
                if prev:
                    why = ("nH1" if not H1[k] else "") + ("nH2" if not H2[k] else "") + ("nH3" if not H3[k] else "")
                    bump(acc, ("after_freeze_" if frozen else "pre_freeze_") + "interrupt_" + why)
                runlen = 0
                if frozen and H2[k] and not H3[k]: bump(acc, "RATCHET_a_FAIL"); acc.setdefault("ex_ra", (name, k))
            prev = hh[k]
        mx(acc, "max_hruns_per_phase", runs, n, name, i); mx(acc, "max_hruns_after_freeze", nruns_after, n, name, i)
        if frozen: bump(acc, "phases_with_freeze")
        bump(acc, "phases")
        i = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        import random
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); d = 0
        while d < N:
            g = rand_c1o(rng, lo, hi, forced=0.0)
            if g is None: continue
            check(g, acc, f"rand{seed}_{d}"); d += 1
        a = []
    for f in a:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
