#!/usr/bin/env python3
"""L-SI box 17 (successor 13): DATA for (R4), stretch_D boundaries (note §19). Runs as sched.py (one phase, no fallback, lambda_W constant).
A BOUNDARY is a transition k -> k+1 of a run at which the stretch key (D, and (Xi(u), W(u)) for u in D) changes. Causes (not exclusive):
  DCH  D_k != D_{k+1};  XI  some u in both D's with Xi(u) changed;  WG  some u in both with W(u) changed.
Per run: transitions, boundaries, and per gate u the number of Xi(u) / W(u) changes (max over u). Per vertex u in some D: COARSE_{-1}
changes of W(u) vs Xi(u). Usage: bnd.py --one GAME [START] | --list FILE [KMIN] | --rand COUNT NLO NHI SEED (env RS, K, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sched
from sched import Engine, dual, load, readstart, start_pair, step, wval, lasso
C = sched.C; VIOL = sched.VIOL

def run(g, E, name, rows, i, j):
    C["runs"] += 1; C["trans"] += j - i; nb = 0; xi, wg = Counter(), Counter()
    for k in range(i, j):
        A, B = rows[k], rows[k + 1]; dch = A["D"] != B["D"]
        x = [u for u in A["D"] & B["D"] if tuple(A["vs"][u]) != tuple(B["vs"][u])]
        w = [u for u in A["D"] & B["D"] if tuple(A["W"][u]) != tuple(B["W"][u])]
        for u in x:
            xi[u] += 1; b0, b1 = A["sb"][u], B["sb"][u]
            if b0 != b1: C["xi_sbar_changed"] += 1; continue
            g0, g1 = sched.gate(A, b0), sched.gate(B, b0)
            if g0 is None and g1 is None:
                cw = sched.ck(E, A["W"][b0]) != sched.ck(E, B["W"][b0])
                C["xi_b_inF_Wchanged" if cw else "xi_b_inF_Wsame"] += 1
                if not cw: print("  XI_B_SAME", name, k, u, b0, A["vs"][u], B["vs"][u], A["W"][b0], B["W"][b0])
            else: C["xi_b_gated"] += 1
        for u in w: wg[u] += 1
        if dch or x or w:
            nb += 1; C["bd"] += 1; C["bd_DCH"] += dch; C["bd_XI"] += bool(x); C["bd_WG"] += bool(w)
            C["bd_XI_only"] += bool(x) and not w and not dch; C["bd_WG_only"] += bool(w) and not x and not dch
    C["max_bd_run"] = max(C["max_bd_run"], nb); C["max_trans_run"] = max(C["max_trans_run"], j - i)
    if xi: C["max_xi_changes_gate"] = max(C["max_xi_changes_gate"], max(xi.values()))
    if wg: C["max_w_changes_gate"] = max(C["max_w_changes_gate"], max(wg.values()))
    if nb > g.n - 1: C["BD_GT_N1"] += 1; VIOL.append(("BD_GT_N1", name, i, j - i, nb, g.n))
    if os.environ.get("V") == "1": print(f"  RUN {name} k0={i} trans={j - i} n={g.n} boundaries={nb} xi={dict(xi)} w={dict(wg)}")

sched.run = run
if __name__ == "__main__":
    os.environ["NOGEN"] = "1"
    sched.main()
