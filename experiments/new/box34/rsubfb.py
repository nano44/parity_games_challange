#!/usr/bin/env python3
"""Box 34: (w, r)-SUBRUNS over whole phases, fallbacks included: maximal runs of states k0..k1 of one phase with (h) at every state, w and
r = lev(θ, w) constant (θ may change). For ρ >= -1: (CV) COARSE_ρ(W) changes only at the first n - 1 transitions; (XA') re-entry after an
S4a leave needs a strict COARSE_ρ(Ξ) increase (ρ = -1: strict Ξ increase); (FBF') entries into R after the subrun's first fallback;
non-flat fallbacks (some value changes) per subrun; θ-changes per subrun. Usage: rsubfb.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *
from mono import coarse

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def subruns(rows, o):
    hh = [r["h1"] and h2(r["nxt"], o) and r["Xi"][o][0] == r["W"][o][0] for r in rows]
    key = lambda k: (rows[k]["ph"], rows[k]["w"], lev(rows[k]["Xi"][o], rows[k]["W"][o])) if hh[k] else None
    out = []; k = 0
    while k < len(rows):
        if key(k) is None: k += 1; continue
        j = k
        while j + 1 < len(rows) and key(j + 1) == key(k): j += 1
        if j > k: out.append((key(k)[2], list(range(k, j + 1))))   # states k..j, transitions k..j-1
        k = j + 1
    return out

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); n = g.n
    for rho, st in subruns(rows, o):
        tr = st[:-1]; c = rows[st[0]]["Xi"][o][0]; U = [v for v in range(n) if rows[st[0]]["Xi"][v][0] == c]
        kind = "thr" if rho >= -1 else "unthr"; bump(acc, kind + "_subruns")
        th = sum(1 for k in tr if rows[k]["th"] != rows[k + 1]["th"]); mx(acc, f"max_{kind}_theta_changes", th, n, name, st[0])
        fbs = [k for k in tr if rows[k]["fb"]]; nfb = 0
        for k in fbs:
            if any(E.key(rows[k]["W"][v]) != E.key(rows[k + 1]["W"][v]) or rows[k]["Xi"][v] != rows[k + 1]["Xi"][v] for v in range(n)): nfb += 1
        mx(acc, f"max_{kind}_nonflat_fb", nfb, n, name, st[0]); bump(acc, f"{kind}_fallbacks", len(fbs))
        if fbs:
            ent = sum(len(set(rows[k + 1]["R"]) - set(rows[k]["R"])) for k in tr if k > fbs[0])
            bump(acc, f"{kind}_entries_after_fb", ent)
            if ent: acc.setdefault(f"ex_{kind}_entry_after_fb", (name, st[0], fbs[0], ent))
        if rho >= -1:
            chg = [i for i, k in enumerate(tr) if any(coarse(rows[k]["W"][v], rho) != coarse(rows[k + 1]["W"][v], rho) for v in range(n))]
            if chg and chg[-1] > n - 2: bump(acc, "CV_FAIL"); acc.setdefault("ex_cv", (name, st[0], chg))
            left = {}
            for k in tr:
                a, b = rows[k], rows[k + 1]; R0, R1 = set(a["R"]), set(b["R"]) | {o}
                for v in R1 - {o}:
                    if v not in R0 and v in left:
                        s = left.pop(v); x0, x1 = rows[s + 1]["Xi"][v], b["Xi"][v]
                        ok = (coarse(x1, rho) != coarse(x0, rho)) if rho >= 0 else (E.key(x1) > E.key(x0))
                        if not ok: bump(acc, "XA_FAIL"); acc.setdefault("ex_xa", (name, s, k, v, rho))
                        bump(acc, "rejoins_checked")
                if not a["fb"]:
                    for v in R0:
                        if v != o and v not in R1: left[v] = k
            xg = sum(1 for k in tr if set(rows[k]["R"]) != set(rows[k + 1]["R"])); mx(acc, "max_thr_xing", xg, n, name, st[0])

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
