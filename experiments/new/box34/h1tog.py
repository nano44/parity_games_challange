#!/usr/bin/env python3
"""Box 34 §11: Lemma R-CONST (at ¬H1 states of a phase, R̄ = U := λ^{-1}(c_θ)); Lemma H1-INT (the states with P(θ) = ∅ form an interval
of the phase, and every H1 -> ¬H1 transition starts in it, R30 H1-DROP); H1-toggles per phase. Usage: h1tog.py game.pg ... | --rand"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def check(g, acc, name):
    rows, o = rows_w(g); n = g.n; i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        c = rows[i]["Xi"][o][0]; U = {v for v in range(n) if rows[i]["Xi"][v][0] == c}
        for k in range(i, j + 1):
            if not rows[k]["h1"]:
                bump(acc, "nH1_states")
                if set(rows[k]["R"]) | {o} != U: bump(acc, "RCONST_FAIL"); acc.setdefault("ex_rc", (name, k))
        emp = [k for k in range(i, j + 1) if rows[k]["Xi"][o][1] == 0]
        if emp and emp != list(range(emp[0], emp[-1] + 1)): bump(acc, "H1INT_interval_FAIL"); acc.setdefault("ex_hi", (name, i, emp))
        tog = 0; drops = 0
        for k in range(i, j):
            if rows[k]["h1"] != rows[k + 1]["h1"]: tog += 1
            if rows[k]["h1"] and not rows[k + 1]["h1"]:
                drops += 1
                if rows[k]["Xi"][o][1] != 0: bump(acc, "H1DROP_FAIL")
        mx(acc, "max_H1_toggles_per_phase", tog, n, name, i); mx(acc, "max_H1_drops_per_phase", drops, n, name, i)
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
