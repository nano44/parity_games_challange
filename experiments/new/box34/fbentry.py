#!/usr/bin/env python3
"""Box 34: residue (L1) of docs/new/N5-REL-box34.md §6. BLOCKS = maximal runs of consecutive (h) states of one phase with r = ρ >= 0 and
COARSE_{ρ-1}(θ), COARSE_{ρ-1}(w) constant (the r = ℓ intervals of RATCHET, without requiring a freeze). Inside a block: fallback evictions
(v in R_k, not in R̄_{k+1} at an S4c step), their gain level lev(Ξ_k v, Ξ_{k+1} v) vs ρ, re-entries after them, and re-entries after S4a
leaves (BLOCK: 0 when frozen). Per block: max re-entries of one vertex, fallbacks, levels of fallbacks. Usage: fbentry.py game.pg ... | --rand"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *
from mono import coarse

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def blocks(rows, o):
    hh = [r["h1"] and h2(r["nxt"], o) and r["Xi"][o][0] == r["W"][o][0] for r in rows]
    def key(k):
        if not hh[k]: return None
        rho = lev(rows[k]["Xi"][o], rows[k]["W"][o])
        if rho < 0: return None
        return (rows[k]["ph"], rho, coarse(rows[k]["Xi"][o], rho - 1), coarse(rows[k]["W"][o], rho - 1))
    out = []; k = 0
    while k < len(rows):
        if key(k) is None: k += 1; continue
        j = k
        while j + 1 < len(rows) and key(j + 1) == key(k): j += 1
        if j > k: out.append((key(k)[1], k, j))
        k = j + 1
    return out

def check(g, acc, name):
    rows, o = rows_w(g); n = g.n
    for rho, a, b in blocks(rows, o):
        bump(acc, "blocks"); ev = {}; re_fb = {}; re_s4a = 0; nfb = 0; lv = []
        for k in range(a, b):
            A, B = rows[k], rows[k + 1]; R0, R1 = set(A["R"]), set(B["R"])
            for v in R1 - R0:
                if v in ev:
                    kind = ev.pop(v)
                    if kind == "fb": re_fb[v] = re_fb.get(v, 0) + 1; bump(acc, "reentry_after_fb")
                    else: re_s4a += 1
            out = [v for v in R0 if v != o and v not in R1 and v != o]
            if A["fb"]:
                nfb += 1; lv.append(A["M"])
                for v in out:
                    gl = lev(A["Xi"][v], B["Xi"][v]); bump(acc, "fb_evict_" + ("eq" if gl == rho else ("lt" if gl < rho else "GT")))
                    ev[v] = "fb" if gl < rho else "fbgood"
            else:
                for v in out: ev[v] = "s4a"
        bump(acc, "reentry_after_s4a", re_s4a)
        mx(acc, "max_reentry_one_vertex_block", max(re_fb.values(), default=0), n, name, a, rho)
        mx(acc, "max_fb_per_block", nfb, n, name, a, rho)
        mx(acc, "max_total_fb_reentries_block", sum(re_fb.values()), n, name, a, rho)
        if any(lv[i] < lv[i + 1] for i in range(len(lv) - 1)): bump(acc, "fb_level_rise_in_block")

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
