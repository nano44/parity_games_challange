#!/usr/bin/env python3
"""Box 33: Lemma R-STICK and Corollary SN-PREFIX (docs/new/N5-K-box33.md §8). Inside a phase, at an S4a transition (no fallback) s -> s+1
with c_w(s) != c_θ (c_w = λ_W(o), c_θ = λ_Ξ(o)), R_s ⊆ R_{s+1}. In a fallback-free segment the states with c_w = c_θ form a prefix.
Counts per fallback-free segment: crossings in the SN prefix, crossings after it, and checks both claims.
Usage: sn.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box32"))
from dormant import *

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g)
    segs = []; cur = []
    for k in range(len(rows) - 1):
        if rows[k]["ph"] != rows[k + 1]["ph"]:
            if cur: segs.append(cur)
            cur = []; continue
        cur.append(k)
        if rows[k]["fb"]: segs.append(cur); cur = []
    if cur: segs.append(cur)
    for seg in segs:
        sn = xs = xo = 0; left = False
        for k in seg:
            a, b = rows[k], rows[k + 1]; ct = a["Xi"][o][0]; same = a["cw"] == ct
            if E.rew[a["cw"]] < E.rew[ct]: acc["XW_rew_FAIL"] = acc.get("XW_rew_FAIL", 0) + 1
            if a["fb"]: continue
            if same and left: acc["PREFIX_FAIL"] = acc.get("PREFIX_FAIL", 0) + 1; acc.setdefault("ex_PREFIX", (name, k))
            if not same: left = True
            R0, R1 = set(a["R"]) | {o}, set(b["R"]) | {o}
            if R0 != R1:
                if same: xs += 1
                else:
                    xo += 1
                    if not R0 <= R1: acc["RSTICK_FAIL"] = acc.get("RSTICK_FAIL", 0) + 1; acc.setdefault("ex_RSTICK", (name, k))
        acc["segs"] = acc.get("segs", 0) + 1; acc["X_SN"] = acc.get("X_SN", 0) + xs; acc["X_after"] = acc.get("X_after", 0) + xo
        for key, v in (("max_X_SN_per_seg", xs), ("max_X_after_per_seg", xo)):
            if v > acc.get(key, (0,))[0]: acc[key] = (v, g.n, name)

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
