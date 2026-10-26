#!/usr/bin/env python3
"""Box 39: packet data for P-N5-PFZ (docs/new/P-N5-PFZ-box39.md). Which hypotheses and proof branches occur in data.
θ-runs (maximal runs of consecutive in-phase states with θ constant), U = λ^{-1}(c_θ), M = signed weight of P(Ξ).
- FB-ROUND: per (fallback, Even v ∈ U ∖ {c_θ}, successor x ∈ U): branch 1 (Ξ_k(x) ⊴ Ξ_k(σ_k v)) / branch 2 ((v, x) improving);
  tight cases (equality); failures.
- P-FREEZE (a), checked directly where it is cheap: for every j and state t > f_j, M_t(z) ≥ BF_j(z), where BF_j is the j-round value
  iteration over SIMPLE paths, computed exactly by DFS when |U| ≤ 18 (else skipped and counted).
- (b) non-vacuous runs: #fallbacks ≥ |U| − 1; their post-freeze transitions; LEN-TAIL: post-freeze U-rises (all must be length rises);
  NO-CROSS-A: post-freeze transitions between H1 states in case A.
- RISE (re-proved in the packet): for every HN in-phase fallback state a and the first state t+1 > a with θ constant on [a, t+1] and a
  gate F -> R̄: the branch of the gate's tail y (y ∈ F_t / y ∈ R_t) and whether an R̄-rise exists at t -> t+1.
- BRK-POLY: per HN stretch: B_S, θ_S, and per break the charging branch (θ-change / early eviction (one of the first |U| − 1 fallbacks of
  its θ-run) / post-freeze rise); the bound, and the ratio.
DATA only. Usage: pfzdata.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "box38"))
from neb_run import *

# PFZ_KEY=P: runs are P-epochs (P(θ) constant; P-N5-PFZ-ext) instead of θ-runs
KEY = (lambda th: th[:2]) if os.environ.get("PFZ_KEY") == "P" else (lambda th: th)

def simple_bf(g, U, term, wt, j, start):
    """max over simple paths from start to a terminal in G_U with ≤ j edges of wt(path minus end) + term[end]; None if none."""
    best = [None]
    def dfs(z, seen, acc_w, edges):
        if z in term:
            v = acc_w + term[z]
            if best[0] is None or v > best[0]: best[0] = v
            return
        if edges == j: return
        succ = set(g.succ[z]) if g.owner[z] == 0 else {g.succ[z][0]}
        for x in succ:
            if x in U and x not in seen: dfs(x, seen | {x}, acc_w + wt(z), edges + 1)
    dfs(start, {start}, 0, 0)
    return best[0]

def analyse(g, acc, name):
    rows, o, E = trace(g, None); N = len(rows); n = g.n
    HN = [r["h1"] and not r["h2"] for r in rows]
    runs = []; a = 0
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["ph"] == rows[a]["ph"] and KEY(rows[b + 1]["th"]) == KEY(rows[a]["th"]): b += 1
        runs.append((a, b)); a = b + 1
    run_of = {}
    for (a, b) in runs:
        for k in range(a, b + 1): run_of[k] = (a, b)
    freeze_at = {}
    for (a, b) in runs:
        ct = rows[a]["Xi"][o][0]; U = [z for z in range(n) if rows[a]["Xi"][z][0] == ct]; Us = set(U)
        hi = E.rank[ct]; wt = lambda v: (E.weight(E.bit[v]) if E.rank[v] > hi else 0); M = lambda val: E.weight(val[1])
        fbs = [k for k in range(a, b) if rows[k]["fb"]]
        freeze_at[(a, b)] = (fbs[len(U) - 2] + 1) if len(U) >= 2 and len(fbs) >= len(U) - 1 else (a if len(U) == 1 else None)
        if b > a: bump(acc, "runs")
        for k in fbs:
            X0, X1 = rows[k]["Xi"], rows[k + 1]["Xi"]; s = rows[k]["s"]
            for v in U:
                if g.owner[v] != 0 or v == ct: continue
                for x in set(g.succ[v]):
                    if x not in Us: continue
                    br = 1 if E.key(X0[x]) <= E.key(X0[s[v]]) else 2
                    lhs, rhs = M(X1[v]), wt(v) + M(X0[x])
                    bump(acc, f"FBR_branch{br}"); bump(acc, f"FBR_branch{br}_tight" if lhs == rhs else f"FBR_branch{br}_strict")
                    if lhs < rhs: bump(acc, "FAIL_FBR"); print("FBR", name, k, v, x)
        if b > a:
            thc = sum(1 for q in range(a, b) if rows[q]["th"] != rows[q + 1]["th"]); bump(acc, "theta_changes_in_runs", thc)
            if thc: bump(acc, "runs_with_theta_change")
            if thc > max(len(U) - 2, 0): bump(acc, "FAIL_THLEN"); print("THLEN", name, a, b, thc, len(U))
        if len(U) <= 18 and fbs:
            term = {o: M(rows[a]["Xi"][o]), ct: 0}
            for j in range(1, len(fbs) + 1):
                if j > len(U) - 1: break
                bfj = {z: simple_bf(g, Us, term, wt, j, z) for z in U}
                for t in range(fbs[j - 1] + 1, b + 1):
                    for z in U:
                        if bfj[z] is not None:
                            bump(acc, "PFZa_checks")
                            if M(rows[t]["Xi"][z]) < bfj[z]: bump(acc, "FAIL_PFZa"); print("PFZa", name, a, j, t, z)
        elif fbs: bump(acc, "PFZa_skipped_bigU")
        fz = freeze_at[(a, b)]
        if fz is not None and b > a and fz < b:
            bump(acc, "freeze_nonvacuous_runs"); bump(acc, "post_freeze_transitions", b - fz)
            mx(acc, "ex_nonvacuous", len(U), n, name, a, b, len(fbs))
            caseA = E.rank[o] > E.rank[ct]
            for t in range(fz, b):
                X0, X1 = rows[t]["Xi"], rows[t + 1]["Xi"]
                for z in U:
                    if X0[z][1] != X1[z][1]: bump(acc, "FAIL_PFZb"); print("PFZb", name, a, t, z)
                    elif E.key(X0[z]) < E.key(X1[z]): bump(acc, "LENTAIL_length_rises")
                if caseA and rows[t]["h1"] and rows[t + 1]["h1"]:
                    bump(acc, "NOCROSSA_transitions")
                    if set(rows[t]["R"]) != set(rows[t + 1]["R"]): bump(acc, "FAIL_NOCROSSA"); print("NCA", name, a, t)
    # RISE branches and BRK-POLY per HN stretch
    k = 0
    while k < N:
        if not HN[k]: k += 1; continue
        e = k
        while e + 1 < N and HN[e + 1] and rows[e + 1]["ph"] == rows[k]["ph"]: e += 1
        B = 0; th = sum(1 for t in range(k, e) if rows[t]["th"] != rows[t + 1]["th"]); ev_at = None
        for t in range(k, e):
            R0, R1 = set(rows[t]["R"]), set(rows[t + 1]["R"])
            if R0 - R1 and ev_at is None: ev_at = t
            if R1 - R0:
                if ev_at is not None:
                    B += 1; a = ev_at
                    if any(rows[q]["th"] != rows[q + 1]["th"] for q in range(a, t + 1)): bump(acc, "BRK_charge_theta")
                    else:
                        ra, rb = run_of[a]; fbs = [q for q in range(ra, rb) if rows[q]["fb"]]
                        ct = rows[a]["Xi"][o][0]; Ul = sum(1 for z in range(n) if rows[a]["Xi"][z][0] == ct)
                        idx = fbs.index(a) if a in fbs else -1
                        if idx < 0: bump(acc, "FAIL_BRK_eviction_not_fallback"); print("EVNF", name, a)
                        elif idx < Ul - 1: bump(acc, "BRK_charge_early_eviction")
                        else: bump(acc, "BRK_charge_postfreeze")
                ev_at = None
        if e > k:
            bump(acc, "HN_stretches"); bump(acc, "breaks", B)
            if B: mx(acc, "max_breaks_per_stretch", B, n, name, k, e, th)
        k = e + 1
    for a in range(N - 1):
        r = rows[a]
        if not (HN[a] and r["fb"] and rows[a + 1]["ph"] == r["ph"]): continue
        t = a
        while t + 1 < N and HN[t + 1] and rows[t + 1]["ph"] == r["ph"] and rows[t + 1]["th"] == r["th"]:
            Rb1 = set(rows[t + 1]["R"]) | {o}
            gates = [(y, z) for y, z in E.improving(tuple(rows[t + 1]["s"]), rows[t + 1]["Xi"]) if y not in Rb1 and z in Rb1]
            if gates:
                Rbt = set(rows[t]["R"]) | {o}; y = gates[0][0]
                bump(acc, "RISE_events"); bump(acc, "RISE_tail_in_F_t" if y not in Rbt else "RISE_tail_in_R_t")
                X0, X1 = rows[t]["Xi"], rows[t + 1]["Xi"]
                if not any(E.key(X0[z]) < E.key(X1[z]) for z in (Rbt & Rb1) - {o}): bump(acc, "FAIL_RISE"); print("RISE", name, a, t)
                if rows[t]["fb"]: bump(acc, "RISE_at_fallback")
                else: bump(acc, "RISE_at_S4a")
                break
            Rbt = set(rows[t]["R"]) | {o}
            if any(y not in Rbt and z in Rbt for y, z in E.improving(tuple(rows[t]["s"]), rows[t]["Xi"])): break
            t += 1

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        try: g = load(f)
        except Exception: bump(acc, "load_fail"); continue
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) == 1: analyse(g, acc, f)
        else: bump(acc, "skipped_not_C1O")
    for key in sorted(acc): print(key, acc[key])
