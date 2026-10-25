#!/usr/bin/env python3
"""Box 40 (2): HN stretches per phase for τ(o) ≠ o (docs/new/N5-NHN-box40.md). Per phase with t0 := τ(o) ≠ o and an HN state:
- T0U: t0 ∈ U = λ^{-1}(c_θ) (FAIL_T0U).
- stretch ends inside the phase: DROP (H1 at k, ¬H1 at k+1) or EV2 (HN at k, H1 ∧ H2 at k+1).
- every EV2 end is an Even S4c fallback evicting t0 (FAIL_SPLIT), with a strict rise Ξ_k(t0) ◁ Ξ_{k+1}(t0) (FAIL_SG).
- EV2 ends that are the j-th in-phase fallback with j ≥ |U| − 1 ("post"): M_k(t0) = M_{k+1}(t0) (FAIL_PIN), = MoptÛ(t0) (exact
  DFS, |U| ≤ 18; FAIL_MOPT), the rise is length-only (FAIL_LEN); post EV2 ends per phase ≤ |U| − 2 (FAIL_POST).
- N_HN ≤ 1 + #DROP + #EV2 (FAIL_NHN1); N_HN ≤ ⌈T/2⌉ + 2|U| − 3, T = |U|(n + 1) + n − 1 (FAIL_NHN).
DATA only. Usage: nhn.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box39")); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *
from rho import mopt_hat

def fail(acc, k, *info): bump(acc, k); print(k, *info, flush=True)

def analyse(g, acc, name):
    rows, o, E = trace(g, None); N = len(rows); n = g.n; a = 0
    HN = [r["h1"] and not r["h2"] for r in rows]
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"]: b += 1
        t0 = rows[a]["t"][o]
        if t0 == o or not any(HN[a:b + 1]): a = b + 1; continue
        bump(acc, "phases_tau_ne_o_with_HN")
        ct = rows[a]["Xi"][o][0]; U = {z for z in range(n) if rows[a]["Xi"][z][0] == ct}; u = len(U)
        if t0 not in U: fail(acc, "FAIL_T0U", name, a)
        hi = E.rank[ct]; wt = lambda v: (E.weight(E.bit[v]) if E.rank[v] > hi else 0); M = lambda t: E.weight(rows[t]["Xi"][t0][1])
        fbs = [k for k in range(a, b) if rows[k]["fb"]]; fbi = {k: j + 1 for j, k in enumerate(fbs)}
        drops = ev2 = post = 0; mo = None
        for k in range(a, b):
            if rows[k]["h1"] and not rows[k + 1]["h1"]: drops += 1
            if HN[k] and rows[k + 1]["h1"] and rows[k + 1]["h2"]:
                ev2 += 1; bump(acc, "EV2_ends")
                if not rows[k]["fb"] or t0 not in rows[k]["R"] or t0 in rows[k + 1]["R"]: fail(acc, "FAIL_SPLIT", name, k)
                if not E.key(rows[k + 1]["Xi"][t0]) > E.key(rows[k]["Xi"][t0]): fail(acc, "FAIL_SG", name, k)
                if rows[k]["fb"] and fbi[k] >= u - 1:
                    post += 1; bump(acc, "EV2_post")
                    if M(k) != M(k + 1): fail(acc, "FAIL_PIN", name, k)
                    if rows[k]["Xi"][t0][1] != rows[k + 1]["Xi"][t0][1]: fail(acc, "FAIL_LEN", name, k)
                    if u <= 18:
                        if mo is None: mo = mopt_hat(g, U - {o}, ct, wt, t0)
                        bump(acc, "MOPT_checks")
                        if mo is None or M(k + 1) != mo: fail(acc, "FAIL_MOPT", name, k)
        if post > u - 2: fail(acc, "FAIL_POST", name, a, post, u)
        nhn = sum(1 for t in range(a, b + 1) if HN[t] and (t == a or not HN[t - 1]))
        T = u * (n + 1) + n - 1
        if nhn > 1 + drops + ev2: fail(acc, "FAIL_NHN1", name, a)
        if nhn > (T + 1) // 2 + 2 * u - 3: fail(acc, "FAIL_NHN", name, a)
        bump(acc, "N_HN_total", nhn); bump(acc, "drops_total", drops)
        mx(acc, "max_N_HN", nhn, n, name, a, u, drops, ev2, post)
        mx(acc, "max_EV2_phase", ev2, n, name, a, u)
        mx(acc, "max_EV2_post_phase", post, n, name, a, u)
        a = b + 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        try: g = load(f)
        except Exception: bump(acc, "load_fail"); continue
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1:
            bump(acc, "files"); analyse(g, acc, f)
        else: bump(acc, "skipped_not_C1O")
    for key in sorted(acc): print(key, acc[key])
