#!/usr/bin/env python3
"""Box 39 (2): P(θ)-changes per phase (ρ). docs/new/N5-RHO-box39.md. Per phase: U = λ^{-1}(c_θ), Û = U ∖ {o}, M = signed P-weight.
Checks:
- BFF: at every S4a transition k -> k+1 between HN states, for every Even v ∈ U ∩ F_{k+1}, v ≠ c_θ, and successor x ∈ U:
  M_{k+1}(v) ≥ wt(v) + M_k(x) (FAIL_BFF).
- FREEZE-F: in every maximal run of consecutive HN states of the phase with no fallback transition: #transitions with a P(θ)-change
  ≤ |U| − 2 + deg(o) − 1 (FAIL_FRF); and M constant on F_t ∩ U from index |U| − 2 on (FAIL_FRF_M).
- THETA-FORM: at H1 states t after the phase's (|U| − 2)-th fallback: M_t(o) = wt(o) + min_{y ∈ Y_t} M_t(y), Y_t = succ(o) ∩ U ∩ F_t
  (FAIL_TF), and for y ∈ F_t ∩ U, M_t(y) = MoptÛ(y) (exact DFS, |U| ≤ 18; FAIL_TFM).
- RHO-TAIL: P(θ)-changes after the phase's (|U| − 2)-th fallback ≤ deg(o) (FAIL_RT).
- ρ_HN per phase (transitions with both ends HN) against (N_HN + |U| − 2)(|U| + deg(o) − 3) + deg(o) (FAIL_RHO).
DATA only. Usage: rho.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *

def mopt_hat(g, Uh, ct, wt, z):
    best = [None]
    def dfs(u, seen, w):
        if u == ct:
            if best[0] is None or w > best[0]: best[0] = w
            return
        succ = set(g.succ[u]) if g.owner[u] == 0 else {g.succ[u][0]}
        for x in succ:
            if x in Uh and x not in seen: dfs(x, seen | {x}, w + wt(u))
    dfs(z, {z}, 0); return best[0]

def analyse(g, acc, name):
    rows, o, E = trace(g, None); N = len(rows); n = g.n; dego = len(set(g.succ[o]))
    HN = [r["h1"] and not r["h2"] for r in rows]; a = 0
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"]: b += 1
        ct = rows[a]["Xi"][o][0]; U = [z for z in range(n) if rows[a]["Xi"][z][0] == ct]; Us = set(U); Uh = Us - {o}
        hi = E.rank[ct]; wt = lambda v: (E.weight(E.bit[v]) if E.rank[v] > hi else 0); M = lambda val: E.weight(val[1])
        Pth = lambda t: rows[t]["Xi"][o][1]
        bump(acc, "phases")
        fbs = [k for k in range(a, b) if rows[k]["fb"]]
        # BFF
        for k in range(a, b):
            if rows[k]["fb"] or not (HN[k] and HN[k + 1]): continue
            X0, X1 = rows[k]["Xi"], rows[k + 1]["Xi"]; F1 = set(range(n)) - set(rows[k + 1]["R"]) - {o}
            for v in U:
                if g.owner[v] != 0 or v == ct or v not in F1: continue
                for x in set(g.succ[v]):
                    if x in Us:
                        bump(acc, "BFF_checks")
                        if M(X1[v]) < wt(v) + M(X0[x]): bump(acc, "FAIL_BFF"); print("BFF", name, k, v, x)
        # FREEZE-F on fallback-free HN runs
        s = a
        while s <= b:
            if not HN[s]: s += 1; continue
            e = s
            while e + 1 <= b and HN[e + 1] and not rows[e]["fb"]: e += 1
            if e > s:
                if e - s > max(len(U) - 2, 0): bump(acc, "ffHN_runs_longer_than_U-2")
                bump(acc, "ffHN_runs"); ch = sum(1 for t in range(s, e) if Pth(t) != Pth(t + 1))
                mx(acc, "max_Pth_changes_ffHN_run", ch, n, name, s, e, len(U), dego)
                if ch > max(len(U) - 2, 0) + dego - 1: bump(acc, "FAIL_FRF"); print("FRF", name, s, e, ch, len(U), dego)
                for t in range(s + max(len(U) - 2, 0), e):
                    Ft1 = (set(range(n)) - set(rows[t + 1]["R"]) - {o}) & Us
                    for y in Ft1:
                        bump(acc, "FRF_M_checks")
                        if M(rows[t]["Xi"][y]) != M(rows[t + 1]["Xi"][y]): bump(acc, "FAIL_FRF_M"); print("FRFM", name, s, t, y)
            s = e + 1
        # THETA-FORM and RHO-TAIL
        if len(U) >= 2:
            start = (fbs[len(U) - 3] + 1) if len(U) >= 3 and len(fbs) >= len(U) - 2 else (a if len(U) <= 2 else None)
            if start is not None:
                bump(acc, "phases_past_hat_freeze"); mopt = {}
                for t in range(start, b + 1):
                    if not rows[t]["h1"]: continue
                    Ft = (set(range(n)) - set(rows[t]["R"]) - {o}) & Us; Y = [y for y in set(g.succ[o]) if y in Ft]
                    bump(acc, "TF_checks")
                    if not Y or M(rows[t]["Xi"][o]) != wt(o) + min(M(rows[t]["Xi"][y]) for y in Y):
                        bump(acc, "FAIL_TF"); print("TF", name, a, t)
                    if len(U) <= 18:
                        for y in Ft:
                            if y not in mopt: mopt[y] = mopt_hat(g, Uh, ct, wt, y)
                            bump(acc, "TFM_checks")
                            if mopt[y] is None or M(rows[t]["Xi"][y]) != mopt[y]: bump(acc, "FAIL_TFM"); print("TFM", name, a, t, y)
                rt = sum(1 for t in range(start, b) if Pth(t) != Pth(t + 1))
                if rt > dego: bump(acc, "FAIL_RT"); print("RT", name, a, rt, dego)
                mx(acc, "max_rho_tail", rt, n, name, a, b, dego)
        # ρ_HN per phase
        rho = sum(1 for t in range(a, b) if HN[t] and HN[t + 1] and Pth(t) != Pth(t + 1))
        nhn = sum(1 for t in range(a, b + 1) if HN[t] and (t == a or not HN[t - 1]))
        bound = (nhn + max(len(U) - 2, 0)) * (max(len(U) - 2, 0) + dego - 1) + dego
        if nhn: bump(acc, "phases_with_HN"); bump(acc, "rho_HN_total", rho); mx(acc, "max_rho_HN", rho, n, name, a, b, nhn, len(U), dego, bound)
        if rho > bound: bump(acc, "FAIL_RHO"); print("RHO", name, a, rho, bound)
        a = b + 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        try: g = load(f)
        except Exception: bump(acc, "load_fail"); continue
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: analyse(g, acc, f)
        else: bump(acc, "skipped_not_C1O")
    for key in sorted(acc): print(key, acc[key])
