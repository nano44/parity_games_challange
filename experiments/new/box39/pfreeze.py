#!/usr/bin/env python3
"""Box 39: Theorem P-FREEZE check (docs/new/N5-RW-box39.md §11). For every maximal run of consecutive in-phase states with θ constant:
U := λ^{-1}(c_θ) (phase-constant, asserted), M(z) := signed weight of P(Ξ(z)) (all of P). Checks:
- FBF: at every fallback transition k -> k+1 of the run, for every Even v ∈ U ∖ {o, c_θ} and successor x ∈ U: M_{k+1}(v) ≥ wt(v) + M_k(x),
  wt(v) = ±2^rank(v) if rank(v) > rank(c_θ) else 0;
- PFZ: after the (|U| − 1)-th fallback of the run, P(Ξ z) is constant on U;
- counts crossings (R changes), breaks (entry after an eviction, no entry between) after the freeze, and the max number of fallbacks
  after which a P-change on U was still seen (vs |U| − 1). DATA only. Env PFZ_KEY=P: P-epochs (P(θ) constant) instead of θ-runs; then also checks θ-changes per run ≤ |U| (FAIL_THLEN).
Usage: pfreeze.py game.pg [game.state] ... | --rand N lo hi seed"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *

# PFZ_KEY=P: runs with P(θ) constant (P-epochs, §12) instead of θ constant (θ is E.key(Ξ(o)) = (reward, P-weight, ±length))
KEY = (lambda th: th[:2]) if os.environ.get("PFZ_KEY") == "P" else (lambda th: th)

def analyse(g, s0, acc, name):
    rows, o, E = trace(g, s0); N = len(rows); n = g.n; a = 0
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"] and KEY(rows[b + 1]["th"]) == KEY(rows[a]["th"]): b += 1
        if b > a:
            ct = rows[a]["Xi"][o][0]; U = [z for z in range(n) if rows[a]["Xi"][z][0] == ct]
            for k in range(a, b + 1): assert [z for z in range(n) if rows[k]["Xi"][z][0] == ct] == U
            hi = E.rank[ct]; wt = lambda v: (E.weight(E.bit[v]) if E.rank[v] > hi else 0); M = lambda val: E.weight(val[1])
            Us = set(U); fb = 0; lastP = 0; post_cross = 0; post_break = 0; ev = False
            bump(acc, "runs"); bump(acc, "transitions", b - a)
            for k in range(a, b):
                X0, X1 = rows[k]["Xi"], rows[k + 1]["Xi"]
                if rows[k]["fb"]:
                    for v in U:
                        if g.owner[v] != 0 or v in (o, ct): continue
                        for x in set(g.succ[v]):
                            if x in Us and M(X1[v]) < wt(v) + M(X0[x]): bump(acc, "FAIL_FBF"); print("FBF", name, a, k, v, x)
                pch = any(X0[z][1] != X1[z][1] for z in U)
                if pch: lastP = fb + 1 if rows[k]["fb"] else fb   # P-change seen after `fb` completed fallbacks
                if pch and fb >= len(U) - 1 + (1 if rows[k]["fb"] else 0) and fb >= len(U):
                    bump(acc, "FAIL_PFZ"); print("PFZ", name, a, k, fb, len(U))
                R0, R1 = set(rows[k]["R"]), set(rows[k + 1]["R"])
                if fb >= len(U) - 1 and R0 != R1: post_cross += 1
                if R1 - R0:
                    if ev and fb >= len(U) - 1: post_break += 1
                    ev = False
                if R0 - R1: ev = True
                if rows[k]["fb"]: fb += 1
            bump(acc, "fallbacks", fb); mx(acc, "max_fb_in_run", fb, n, name, a, b, len(U))
            mx(acc, "max_lastP_minus_U", lastP - (len(U) - 1), n, name, a, b, lastP, len(U))
            acc["_late"] = max(acc.get("_late", -10 ** 9), lastP - (len(U) - 1)); acc["_lastP"] = max(acc.get("_lastP", 0), lastP)
            if len(U) >= 3: acc["_excess"] = max(acc.get("_excess", -10 ** 9), fb - (len(U) - 1))
            thc = sum(1 for k in range(a, b) if rows[k]["th"] != rows[k + 1]["th"]); mx(acc, "max_theta_changes_in_run", thc, n, name, a, b, len(U))
            if thc > len(U): bump(acc, "FAIL_THLEN"); print("THLEN", name, a, b, thc, len(U))
            bump(acc, "post_freeze_crossings", post_cross); bump(acc, "post_freeze_breaks", post_break)
            if post_cross: mx(acc, "ex_post_cross", post_cross, n, name, a, b)
        a = b + 1

def main():
    acc = {}; args = sys.argv[1:]
    if args[:1] == ["--rand"]:
        import random; sys.path.insert(0, os.path.join(HERE, "..", "box25")); from common import rand_c1o
        N, lo, hi, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g = rand_c1o(rng, lo, hi)
            if g is not None: bump(acc, "games"); analyse(g, None, acc, f"rand{seed}_{i}")
    else:
        i = 0
        while i < len(args):
            f = args[i]; s0 = None
            if i + 1 < len(args) and args[i + 1].endswith(".state"): s0 = list(map(int, open(args[i + 1]).read().split())); i += 1
            try: g = load(f)
            except Exception: bump(acc, "load_fail"); i += 1; continue
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: analyse(g, s0, acc, f)
            else: bump(acc, "skipped_not_C1O")
            i += 1
    for key in sorted(acc):
        if not key.startswith('_'): print(key, acc[key])

if __name__ == "__main__": main()
