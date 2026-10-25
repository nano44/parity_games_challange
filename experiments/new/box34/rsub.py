#!/usr/bin/env python3
"""Box 34: r-constant sub-runs of SN prefixes (docs/new/N5-REL-box34.md). Fallback-free run of a phase -> SN prefix (c_w = c_θ) -> split
into maximal r-SUBRUNS: consecutive transitions k -> k+1 with (h) at k, w_{k+1} = w_k and r_k = ρ constant. Checks, per subrun with
ρ >= -1 (throttled): (CV) COARSE_ρ(W) on U = λ^{-1}(c_θ) changes only at the first |U| - 1 transitions of the subrun; (XA') a vertex that
leaves R at an S4a step of the subrun and rejoins later in it has a strict COARSE_ρ increase of Ξ in between (ρ = -1: a strict Ξ increase);
counts leaves per vertex. Per subrun with ρ = ⊥ (θ = w): (PH) W changes on U at <= |U| - 1 transitions. Also counts per SN prefix:
w-changes, subruns, crossings. Usage: rsub.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *
from mono import coarse

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def check(g, acc, name):
    rows, o = rows_w(g); E = Engine(g); n = g.n
    hh = [r["h1"] and h2(r["nxt"], o) and r["Xi"][o][0] == r["W"][o][0] for r in rows]
    runs = []; cur = []
    for k in range(len(rows) - 1):
        if rows[k]["ph"] != rows[k + 1]["ph"] or rows[k]["fb"]:
            if cur: runs.append(cur); cur = []
            continue
        cur.append(k)
    if cur: runs.append(cur)
    for run in runs:
        pre = []
        for k in run:
            if rows[k]["Xi"][o][0] != rows[k]["W"][o][0]: break
            pre.append(k)
        if not pre: continue
        c = rows[pre[0]]["Xi"][o][0]; U = [v for v in range(n) if rows[pre[0]]["Xi"][v][0] == c]
        subs = []; cs = []; key = None; wch = 0; nonh = 0
        for k in pre:
            a, b = rows[k], rows[k + 1]
            if a["w"] != b["w"]: wch += 1
            if not hh[k]: nonh += 1
            kk = (a["w"], lev(a["Xi"][o], a["W"][o])) if hh[k] and a["w"] == b["w"] else None
            if kk != key or kk is None:
                if cs: subs.append((key, cs))
                cs = []; key = kk
            if kk is not None: cs.append(k)
        if cs: subs.append((key, cs))
        bump(acc, "prefixes"); mx(acc, "max_wchg_per_prefix", wch, n, name, pre[0]); mx(acc, "max_subruns_per_prefix", len(subs), n, name, pre[0])
        bump(acc, "prefix_nonh_steps", nonh)
        for (wv, rho), ks in subs:
            if rho >= -1:
                bump(acc, "thr_subruns"); chg = [i for i, k in enumerate(ks) if any(coarse(rows[k]["W"][v], rho) != coarse(rows[k + 1]["W"][v], rho) for v in U)]
                if chg and chg[-1] > len(U) - 2: bump(acc, "CV_FAIL"); acc.setdefault("ex_cv", (name, ks[0], chg, len(U)))
                mx(acc, "max_thr_subrun_len", len(ks), n, name, ks[0])
                left = {}; nleave = {}
                for k in ks:
                    a, b = rows[k], rows[k + 1]; R0, R1 = set(a["R"]), set(b["R"]) | {o}
                    for v in R1 - {o}:
                        if v not in R0 and v in left:   # rejoin after a leave at step left[v]
                            s = left[v]; x0, x1 = rows[s + 1]["Xi"][v], b["Xi"][v]
                            ok = (coarse(x1, rho) != coarse(x0, rho)) if rho >= 0 else (x1 != x0)
                            if not ok: bump(acc, "XA_FAIL"); acc.setdefault("ex_xa", (name, s, k, v, rho))
                            bump(acc, "rejoins_checked"); del left[v]
                    for v in R0:
                        if v != o and v not in R1: left[v] = k; nleave[v] = nleave.get(v, 0) + 1; bump(acc, "thr_leaves")
                mx(acc, "max_leaves_one_vertex_thr_subrun", max(nleave.values(), default=0), n, name, ks[0])
            else:
                bump(acc, "unthr_subruns")
                chg = sum(1 for k in ks if any(E.key(rows[k]["W"][v]) != E.key(rows[k + 1]["W"][v]) for v in U))
                xg = sum(1 for k in ks if set(rows[k]["R"]) != set(rows[k + 1]["R"]))
                if chg > len(U) - 1: bump(acc, "PH_FAIL"); acc.setdefault("ex_ph", (name, ks[0], chg, len(U)))
                mx(acc, "max_unthr_Wchg", chg, len(U), name, ks[0]); mx(acc, "max_unthr_xing", xg, chg, len(U), name, ks[0])
                mx(acc, "max_unthr_len", len(ks), len(U), name, ks[0])

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
