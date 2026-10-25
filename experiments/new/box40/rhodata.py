#!/usr/bin/env python3
"""Box 40: data for packet P-N5-RHO (docs/new/P-N5-RHO-box40.md): how often each hypothesis of each statement occurs, with checks.
Per phase: U = λ^{-1}(c_θ), Û = U ∖ {o}, M = signed weight of the path set, wt as in P-N5-PFZ §0, g_j = j-th in-phase fallback.
- YF: Y-FORM at EVERY H1 state (M(o) = wt(o) + min_{y∈Y} M(y), σ̄(o) ∈ Y); at ¬H1 states P(θ) = ∅. FAIL_YF, FAIL_YF0.
- HFa: HAT-FREEZE (a) directly: for j ≤ |U| − 2, states t > g_j, z ∈ Û: M_t(z) ≥ best simple path of G_Û with ≤ j edges (|U| ≤ 14).
- HFc: HAT-FREEZE (c) at states t > g_{|U|−2} (|U| ≥ 3 counted apart from |U| ≤ 2), y ∈ F_t ∩ U: M_t(y) = MoptÛ(y) (|U| ≤ 18).
- RT: RHO-TAIL. P(θ)-changes after g_{|U|−2} ≤ deg(o); counted by |U| ≥ 3 / ≤ 2 and by whether an H1 state follows the freeze.
- BFF: BF-F at S4a HN→HN transitions; branch counts: case 1, case 2 with x ∈ R̄_k / x ∈ F_k passing v / x ∈ F_k avoiding v.
- FFa: FREEZE-F (a) directly (|U| ≤ 14); FFb: number of states where (b)'s hypothesis t ≥ s + |U| − 2 holds; FFc: (c).
- RHO: RHO-HN bound per phase.
DATA only. Usage: rhodata.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "box39")); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *

def fail(acc, k, *info): bump(acc, k); print(k, *info, flush=True)

def best_paths(g, nodes, ct, wt, jmax):
    """best[j][z] = max wt(p ∖ {ct}) over simple paths p from z to ct in the graph on `nodes` (Even: all edges into nodes, Odd: forced
    edge if in nodes, ct a sink) with ≤ j edges; None if none."""
    best = [dict() for _ in range(jmax + 1)]
    def dfs(u, seen, w, d, z):
        if u == ct:
            for j in range(d, jmax + 1):
                if best[j].get(z) is None or w > best[j][z]: best[j][z] = w
            return
        if d == jmax: return
        succ = set(g.succ[u]) if g.owner[u] == 0 else {g.succ[u][0]}
        for x in succ:
            if x in nodes and x not in seen: dfs(x, seen | {x}, w + wt(u), d + 1, z)
    for z in nodes: dfs(z, {z}, 0, 0, z)
    return best

def analyse(g, acc, name):
    rows, o, E = trace(g, None); N = len(rows); n = g.n; dego = len(set(g.succ[o]))
    HN = [r["h1"] and not r["h2"] for r in rows]; a = 0
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"]: b += 1
        ct = rows[a]["Xi"][o][0]; U = {z for z in range(n) if rows[a]["Xi"][z][0] == ct}; Uh = U - {o}; u = len(U)
        hi = E.rank[ct]; wt = lambda v: (E.weight(E.bit[v]) if E.rank[v] > hi else 0)
        M = lambda t, z: E.weight(rows[t]["Xi"][z][1]); F = lambda t: set(range(n)) - set(rows[t]["R"]) - {o}
        Pth = lambda t: rows[t]["Xi"][o][1]
        fbs = [k for k in range(a, b) if rows[k]["fb"]]; bump(acc, "phases")
        # YF at every state
        for t in range(a, b + 1):
            if rows[t]["h1"]:
                Y = [y for y in set(g.succ[o]) if y in F(t) & U]; bump(acc, "YF_checks")
                if not Y or M(t, o) != wt(o) + min(M(t, y) for y in Y): fail(acc, "FAIL_YF", name, t)
            else:
                bump(acc, "YF0_checks")
                if Pth(t) != 0: fail(acc, "FAIL_YF0", name, t)
        # HFa direct
        if 3 <= u <= 14 and fbs:
            jm = min(u - 2, len(fbs)); bp = best_paths(g, Uh, ct, wt, jm)
            for j in range(1, jm + 1):
                for t in range(fbs[j - 1] + 1, b + 1):
                    for z in Uh:
                        if bp[j].get(z) is None: continue
                        bump(acc, "HFa_checks")
                        if M(t, z) < bp[j][z]: fail(acc, "FAIL_HFa", name, a, j, t, z)
        elif u > 14 and fbs: bump(acc, "HFa_phases_skipped_U>14")
        # HFc, RT
        if u >= 2 and (u == 2 or len(fbs) >= u - 2):
            start = a if u == 2 else fbs[u - 3] + 1; tag = "U3+" if u >= 3 else "U2"
            bump(acc, f"phases_past_hat_{tag}")
            h1after = [t for t in range(start, b + 1) if rows[t]["h1"]]
            if h1after: bump(acc, f"phases_past_hat_with_H1_{tag}")
            if u <= 18:
                bp = best_paths(g, Uh, ct, wt, max(u - 2, 0))[max(u - 2, 0)]
                for t in h1after:
                    for y in F(t) & U:
                        bump(acc, f"HFc_checks_{tag}")
                        if bp.get(y) is None or M(t, y) != bp[y]: fail(acc, "FAIL_HFc", name, a, t, y)
            rt = sum(1 for t in range(start, b) if Pth(t) != Pth(t + 1))
            mx(acc, f"max_RT_{tag}", rt, n, name, a, dego)
            if rt > dego: fail(acc, "FAIL_RT", name, a, rt, dego)
        # BFF
        for k in range(a, b):
            if rows[k]["fb"] or not (HN[k] and HN[k + 1]): continue
            F0, F1 = F(k), F(k + 1); R0bar = set(rows[k]["R"]) | {o}
            for v in U:
                if g.owner[v] != 0 or v == ct or v not in F1: continue
                for x in set(g.succ[v]):
                    if x not in U: continue
                    if M(k, x) <= M(k, rows[k]["s"][v]): br = "case1"
                    elif x in R0bar: br = "case2_xRbar"
                    else:
                        y, seen = x, set()
                        while y not in seen and y != v:
                            seen.add(y); y = rows[k]["s"][y] if g.owner[y] == 0 else (rows[k]["t"][y])
                        br = "case2_passes_v" if y == v else "case2_avoids_v"
                    bump(acc, "BFF_" + br)
                    if M(k + 1, v) < wt(v) + M(k, x): fail(acc, "FAIL_BFF", name, k, v, x, br)
        # FREEZE-F on maximal fallback-free HN runs
        s = a
        while s <= b:
            if not HN[s]: s += 1; continue
            e = s
            while e + 1 <= b and HN[e + 1] and not rows[e]["fb"]: e += 1
            if e > s:
                bump(acc, "FF_runs"); mx(acc, "max_FF_run_len_minus_(U-2)", e - s - max(u - 2, 0), n, name, s, e, u)
                if u <= 14:
                    for t in range(s + 1, e + 1):
                        nodes = F(t) & U; jm = min(t - s, max(u - 2, 0)); bpt = best_paths(g, nodes, ct, wt, jm)[jm]
                        for z in nodes:
                            if bpt.get(z) is None: continue
                            bump(acc, "FFa_checks")
                            if M(t, z) < bpt[z]: fail(acc, "FAIL_FFa", name, s, t, z)
                bump(acc, "FFb_states_with_hypothesis", max(0, e - (s + max(u - 2, 0))))
                ch = sum(1 for t in range(s, e) if Pth(t) != Pth(t + 1)); mx(acc, "max_FFc", ch, n, name, s, e, u, dego)
                if ch > max(u - 2, 0) + dego - 1: fail(acc, "FAIL_FFc", name, s, e, ch)
            s = e + 1
        rho = sum(1 for t in range(a, b) if HN[t] and HN[t + 1] and Pth(t) != Pth(t + 1))
        nhn = sum(1 for t in range(a, b + 1) if HN[t] and (t == a or not HN[t - 1]))
        if nhn:
            bump(acc, "phases_with_HN"); bound = (nhn + max(u - 2, 0)) * (max(u - 2, 0) + dego - 1) + dego
            bump(acc, "rho_HN_total", rho); mx(acc, "max_rho_HN", rho, n, name, a, nhn, u, dego, bound)
            if rho > bound: fail(acc, "FAIL_RHO", name, a, rho, bound)
        a = b + 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        try: g = load(f)
        except Exception: bump(acc, "load_fail"); continue
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: bump(acc, "files"); analyse(g, acc, f)
        else: bump(acc, "skipped_not_C1O")
    for key in sorted(acc): print(key, acc[key])
