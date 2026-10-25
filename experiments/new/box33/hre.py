#!/usr/bin/env python3
"""Box 33: CONJECTURE H-RE (docs/new/N5-K-box33.md §10). Inside a scope run (L-SI: (h) at j, H2 at j+1, w constant), if an exit x is
absorbed (σ̄(o) changes from x and x moves F -> R) at j1 < j2, then r_{j2} < r_{j1}, r := lev(θ, w). Also reports the same question at
phase level (between two absorptions of the same exit in a phase: θ changes at a level above the absorption level?).
Usage: hre.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from scopecov import h2
from dormant import *

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); sb = [E.evaluate(tuple(r["s"]))[1][o] for r in rows]
    H2 = [h2(r["nxt"], o) for r in rows]
    hh = [r["h1"] and H2[i] and r["Xi"][o][0] == r["W"][o][0] for i, r in enumerate(rows)]
    insc = [rows[j]["ph"] == rows[j + 1]["ph"] and hh[j] and H2[j + 1] and rows[j]["w"] == rows[j + 1]["w"] for j in range(len(rows) - 1)]
    sid = 0; last = {}; lastp = {}; p = 0
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        if a["ph"] != b["ph"]: p += 1; lastp = {}
        if not insc[k]: sid += 1; last = {}
        if a["ph"] != b["ph"]: continue
        x = sb[k]
        if sb[k] != sb[k + 1] and x != o and x not in a["R"] and x in b["R"]:
            lv = lev(a["Xi"][o], b["Xi"][o]); acc["absorb"] = acc.get("absorb", 0) + 1
            if x in lastp:
                j1, l1 = lastp[x]; acc["re_absorb_phase"] = acc.get("re_absorb_phase", 0) + 1
                hi = any(lev(rows[t]["Xi"][o], rows[t + 1]["Xi"][o]) > l1 for t in range(j1 + 1, k) if rows[t]["Xi"][o] != rows[t + 1]["Xi"][o])
                if not hi: acc["PHASE_NOHIGHER_FAIL"] = acc.get("PHASE_NOHIGHER_FAIL", 0) + 1; acc.setdefault("ex_PH", (name, j1, k, x))
            lastp[x] = (k, lv)
            if insc[k]:
                r = lev(a["Xi"][o], a["W"][o])
                if x in last:
                    acc["re_absorb_scope"] = acc.get("re_absorb_scope", 0) + 1
                    if not r < last[x]: acc["HRE_FAIL"] = acc.get("HRE_FAIL", 0) + 1; acc.setdefault("ex_HRE", (name, k, x, last[x], r))
                last[x] = r

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
