#!/usr/bin/env python3
"""Box 35 (c): level -1 states. (CN-LAST) at an Even fallback whose gates are all level -1 gates at own cycle nodes: Xi unchanged and
I_sigma empty next. (LEN-STAY) after a state with M = -1 inside a phase, M <= -1 and COARSE_{-1}(Xi) = (cycle node, P) stay constant for
the rest of the phase. Usage: lenrun.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box34"))
from relfr import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def cp(x): return (x[0], x[1])

def check(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); E = Engine(g); n = g.n
    for k in range(len(rows) - 1):
        r, b = rows[k], rows[k + 1]
        if r["fb"] and r["M"] == -1 and r["s"] != b["s"]:
            I = E.improving(tuple(r["s"]), r["Xi"]); own = all(r["Xi"][y][0] == y for y, _ in I)
            bump(acc, "lev-1_even_fb_" + ("allown" if own else "notown"))
            if own:
                if any(r["Xi"][v] != b["Xi"][v] for v in range(n)): bump(acc, "CNLAST_XI_FAIL"); acc.setdefault("ex_cx", (name, k))
                if E.improving(tuple(b["s"]), b["Xi"]): bump(acc, "CNLAST_I_FAIL"); acc.setdefault("ex_ci", (name, k))
                if k + 2 < len(rows) and rows[k + 2]["ph"] == r["ph"]: bump(acc, "CNLAST_PHASE_CONT")
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and rows[j + 1]["ph"] == rows[i]["ph"]: j += 1
        f = next((k for k in range(i, j + 1) if rows[k]["M"] == -1), None)
        if f is not None:
            bump(acc, "phases_with_M-1")
            for k in range(f + 1, j + 1):
                if rows[k]["M"] > -1: bump(acc, "LENSTAY_M_FAIL"); acc.setdefault("ex_lm", (name, f, k)); break
            for k in range(f, j):
                if any(cp(rows[k]["Xi"][v]) != cp(rows[k + 1]["Xi"][v]) for v in range(n)):
                    bump(acc, "LENSTAY_COARSE_FAIL"); acc.setdefault("ex_lc", (name, f, k)); break
            acc["max_trans_after_M-1"] = max(acc.get("max_trans_after_M-1", 0), j - f)
        i = j + 1

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
