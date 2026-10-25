#!/usr/bin/env python3
"""Box 38 (a): fallback accounting on HN stretches (docs/new/P-N5-OUT-box37.md §2, §6). An HN stretch is a maximal run of consecutive
H1 ∧ ¬H2 states of one phase. Per stretch S (transitions with both ends in S): X_S crossings, evictions (fallback crossings), entries,
fallbacks f_S split into crossing fallbacks and non-crossing ones, max fallbacks in one crossing-free run of S, breaks B, θ-changes θ_S,
and the exit transition (last state of S -> next state of the phase) if it is a fallback. Checks: (SPLIT') every crossing of S is an
S4a entry or a fallback eviction; (EPOCH') X_S <= 2(n-1)(B+1) and f_S <= n_E(2n-1)(X_S+1)+X_S; (BRK) in case A with τ(o) = o, each
break has a θ-change at a transition in (a, k] (a = its eviction, k = its entry); (PH) per τ(o) = o phase of case A:
f_HN <= (n_E(2n-1)+1)(2(n-1)θ_ph + (2n-1)N_HN) and N_HN <= T_ph//2 + 1. One Odd choice vertex asserted.
Usage: fbsplit.py game.pg ... | --rand N lo hi seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); B37 = os.path.join(HERE, "..", "box37")
sys.path.insert(0, B37); sys.path.insert(0, os.path.join(HERE, "..", "..", "si", "coarse"))
from outsn import *

def run(g, acc, name):
    assert sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1
    rows, o = rows_w(g); N = len(rows); H2 = [h2(r["nxt"], o) for r in rows]; E = Engine(g)
    n = g.n; nE = sum(1 for u in range(n) if g.owner[u] == 0); K = nE * (2 * n - 1)
    HN = [rows[k]["h1"] and not H2[k] for k in range(N)]
    ph = {}
    k = 0
    while k < N:
        if not HN[k]: k += 1; continue
        j = k
        while j + 1 < N and HN[j + 1] and rows[j + 1]["ph"] == rows[k]["ph"]: j += 1
        too = rows[k]["nxt"][o] == o; case = "A" if E.rank[o] > E.rank[rows[k]["Xi"][o][0]] else "B"
        X = ev = en = fcr = fnc = th = brk = 0; run_fb = 0; max_run = 0; lastev = None; firstev = None
        for i in range(k, j):
            R0, R1 = set(rows[i]["R"]), set(rows[i + 1]["R"]); fb = rows[i]["fb"]
            if rows[i]["th"] != rows[i + 1]["th"]: th += 1
            if R0 != R1:
                X += 1; run_fb = 0
                if fb: fcr += 1
                if fb and (R1 - R0 or not (R0 - R1)): bump(acc, "FAIL_SPLIT_fb_entry"); print("SPLIT", name, i)
                if not fb and (R0 - R1 or not (R1 - R0)): bump(acc, "FAIL_SPLIT_s4a_exit"); print("SPLIT", name, i)
                if fb:
                    ev += 1
                    if firstev is None: firstev = i
                else:
                    en += 1
                    if firstev is not None:
                        brk += 1; a = firstev
                        sep = any(rows[t]["th"] != rows[t + 1]["th"] for t in range(a + 1, i + 1))
                        bump(acc, f"breaks_{case}_tauo{'=o' if too else '!=o'}_" + ("theta_sep" if sep else "NO_theta_sep"))
                        if too and case == "A" and not sep: bump(acc, "FAIL_BRK"); print("BRK", name, a, i)
                    firstev = None
            elif fb:
                fnc += 1; run_fb += 1; max_run = max(max_run, run_fb)
        f = fcr + fnc
        exitfb = int(j + 1 < N and rows[j + 1]["ph"] == rows[k]["ph"] and rows[j]["fb"])
        bump(acc, "HN_stretches"); bump(acc, "f_crossing", fcr); bump(acc, "f_noncrossing", fnc); bump(acc, "f_exit", exitfb)
        mx(acc, "max_fb_per_crossing_free_run", max_run, n, name, k)
        mx(acc, "max_f_S", f, n, X, fcr, name, k); mx(acc, "max_X_S", X, n, brk, th, name, k)
        if X > 2 * (n - 1) * (brk + 1): bump(acc, "FAIL_EPOCH_X"); print("EPOCHX", name, k)
        if f > K * (X + 1) + X: bump(acc, "FAIL_EPOCH_f"); print("EPOCHf", name, k)
        if f > K * (X + 1): bump(acc, "exceeds_old_form_KX1")
        if too:
            p = ph.setdefault(rows[k]["ph"], dict(case=case, N=0, f=0, first=k))
            p["N"] += 1; p["f"] += f + exitfb
        k = j + 1
    for pid, p in ph.items():
        ks = [t for t in range(N) if rows[t]["ph"] == pid]
        T = sum(1 for t in ks[:-1] if rows[t]["h1"] != rows[t + 1]["h1"])
        thp = sum(1 for t in ks[:-1] if rows[t]["th"] != rows[t + 1]["th"])
        bump(acc, "phases_tauo_o_" + p["case"])
        if p["N"] > T // 2 + 1: bump(acc, "FAIL_NHN"); print("NHN", name, pid)
        if p["case"] == "A" and p["f"] > (K + 1) * (2 * (n - 1) * thp + (2 * n - 1) * p["N"]): bump(acc, "FAIL_PH"); print("PH", name, pid)
        mx(acc, "max_f_HN_phase_" + p["case"], p["f"], n, p["N"], T, thp, name)

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    if a and a[0] == "--rand":
        Nn, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed)
        for d in range(Nn):
            g = rand_c1o(rng, lo, hi)
            if g is not None: run(g, acc, f"rand{seed}_{d}")
    else:
        for f in a:
            g = load(f)
            if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: bump(acc, "skipped_not_C1O"); continue
            run(g, acc, f)
    for key in sorted(acc): print(key, acc[key])
