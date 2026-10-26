#!/usr/bin/env python3
"""Box 35 (c): classify every theta-change inside SCOPE RUNS (in-phase transitions k -> k+1 with (h) at k, H2 at k+1, w_{k+1} = w_k).
Kinds: ABS (sigma-bar(o) changes from x0 and x0 enters R), OVT (sigma-bar(o) changes, x0 stays in F), VAL (same sigma-bar(o)).
Also: was there a fallback earlier in the same scope run ("post"), the theta-change level vs the last fallback level Lf, and the
transition type (S4a / fallback). Usage: thcls.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box34"))
from relfr import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def scope_runs(g, rows, o):
    ins = []
    for k in range(len(rows) - 1):
        a, b = rows[k], rows[k + 1]
        hh = a["h1"] and h2(a["nxt"], o) and a["Xi"][o][0] == a["W"][o][0]
        ins.append(a["ph"] == b["ph"] and hh and h2(b["nxt"], o) and a["w"] == b["w"])
    runs, k = [], 0
    while k < len(ins):
        if ins[k]:
            j = k
            while j + 1 < len(ins) and ins[j + 1]: j += 1
            runs.append((k, j)); k = j + 1   # transitions k..j
        else: k += 1
    return runs

def check(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); E = Engine(g); sb = [E.evaluate(tuple(r["s"]))[1][o] for r in rows]
    for (k0, k1) in scope_runs(g, rows, o):
        Lf = None; post_th = 0; seq = []
        for k in range(k0, k1 + 1):
            a, b = rows[k], rows[k + 1]
            if a["th"] != b["th"]:
                L = lev(a["Xi"][o], b["Xi"][o]); x0 = sb[k]
                kind = "VAL" if sb[k + 1] == x0 else ("ABS" if x0 in set(b["R"]) else "OVT")
                tag = "pre" if Lf is None else ("post_" + ("gt" if L > Lf else ("eq" if L == Lf else "lt")))
                bump(acc, f"th_{kind}_{tag}"); bump(acc, "th_at_fb" if a["fb"] else "th_at_S4a")
                if Lf is not None: post_th += 1
                seq.append(("T", kind, L))
            if a["fb"]:
                Lf = a["M"]; seq.append(("F", Lf))
        mx(acc, "max_post_fb_theta_changes_per_scope_run", post_th, g.n, name, k0)
        nf = sum(1 for s in seq if s[0] == "F"); mx(acc, "max_fallbacks_per_scope_run", nf, g.n, name, k0)
        bump(acc, "scope_runs")
        if post_th >= acc.get("max_post_fb_theta_changes_per_scope_run", (0,))[0] and post_th > 0: acc["ex_seq"] = (name, k0, seq[:60])

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
