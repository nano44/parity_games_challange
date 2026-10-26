#!/usr/bin/env python3
"""Box 37 (b): epochs of H1 ∧ ¬H2 stretches (docs/new/N5-OUT-box37.md §2-§3). Inside a phase, an HN stretch is a maximal run of
consecutive states with H1 ∧ ¬H2. Checks per transition k -> k+1 with H1 ∧ ¬H2 at k:
  (SPLIT) S4a: R_k ⊆ R_{k+1}; Even S4c fallback: R̄_{k+1} ⊆ R̄_k.
  (ENTRY-TW) every S4a transition with an entry, preceded in the same HN stretch by an evicting fallback at k0 < k with no entry in
             between, has θ or w changed somewhere in (k0, k] (θ_j != θ_{j+1} or w_j != w_{j+1} for some k0 < j+1 <= k ... as states).
Records which of θ / w / route-only (neither) separates each eviction from the next entry, the number of θ-changes, w-changes and
epochs per HN stretch, and the max re-entries of one vertex in one phase. Usage: epoch.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from outsn import *

def run(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); N = len(rows); H2 = [h2(r["nxt"], o) for r in rows]
    HN = [rows[k]["h1"] and not H2[k] for k in range(N)]
    for k in range(N - 1):
        if rows[k]["ph"] != rows[k + 1]["ph"] or not HN[k]: continue
        R0, R1 = set(rows[k]["R"]), set(rows[k + 1]["R"])
        if rows[k]["fb"] and R1 - R0: bump(acc, "SPLIT_FAIL_fb_entry"); print("SPLIT fb", name, k)
        if not rows[k]["fb"] and R0 - R1: bump(acc, "SPLIT_FAIL_s4a_exit"); print("SPLIT s4a", name, k)
    k = 0
    while k < N:
        if not HN[k]: k += 1; continue
        j = k
        while j + 1 < N and HN[j + 1] and rows[j + 1]["ph"] == rows[k]["ph"]: j += 1
        # HN stretch k..j (transitions k..j-1 inside; transition j -> j+1 leaves or ends)
        lastev = None; ep = 1; th = sum(rows[i]["th"] != rows[i + 1]["th"] for i in range(k, j))
        wc = sum(rows[i]["w"] != rows[i + 1]["w"] for i in range(k, j)); left = {}; remax = 0; cnt = {}
        for i in range(k, j):
            R0, R1 = set(rows[i]["R"]), set(rows[i + 1]["R"])
            if R0 - R1: lastev = i
            for v in R0 - R1: left[v] = i
            if R1 - R0:
                for v in R1 - R0:
                    if v in left: cnt[v] = cnt.get(v, 0) + 1; remax = max(remax, cnt[v])
                if lastev is not None:
                    ep += 1
                    tc = any(rows[a]["th"] != rows[a + 1]["th"] for a in range(lastev, i + 1))
                    wch = any(rows[a]["w"] != rows[a + 1]["w"] for a in range(lastev, i + 1))
                    key = "sep_theta" if tc and not wch else ("sep_w" if wch and not tc else ("sep_both" if tc else "sep_NONE"))
                    bump(acc, key)
                    if key == "sep_NONE": mx(acc, "ex_sep_NONE", 1, g.n, name, lastev, i)
                    lastev = None
        too = rows[k]["nxt"][o] == o
        bump(acc, "HN_stretches"); bump(acc, "HN_tauo_o" if too else "HN_tauo_other")
        mx(acc, "max_epochs", ep, g.n, th, wc, too, name, k)
        mx(acc, "max_theta_changes_HN", th, g.n, ep, too, name, k)
        mx(acc, "max_w_changes_HN", wc, g.n, ep, too, name, k)
        mx(acc, "max_vertex_reentries", remax, g.n, ep, too, name, k)
        k = j + 1

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for d in range(N):
            g = rand_c1o(rng, lo, hi)
            if g is not None: run(g, acc, f"rand{seed}_{d}")
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: bump(acc, "skipped_not_C1O"); continue
            run(g, acc, f)
    for key in sorted(acc): print(key, acc[key])
