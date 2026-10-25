#!/usr/bin/env python3
"""Box 41 (L-RED successor 17): exact checker of P-N5-PFZ (docs/new/P-N5-PFZ-box39.md, sha1 3c617e06) §2 P-FREEZE (a)-(c), §3 LEN-TAIL,
§4 NO-CROSS-A, and P-N5-RHO (docs/new/P-N5-RHO-box40.md, sha1 cd5df65c) §1 Y-FORM, §2 HAT-FREEZE (a)-(c), §3 RHO-TAIL, written from the
frozen texts. Trace = sox.trace (own copy of n5.run, SPEC S1-S5, canonical start). 𝒞^1O asserted (one Odd vertex of out-degree > 1).
Per state k: Ξ_k, σ̄_k (si.Engine.evaluate), R_k (vertices ≠ o whose (σ_k, τ_k)-play reaches o), H1 (o not on its honest cycle), H2
(o not on its (σ, τ) cycle). PHASE = maximal run with λ_Ξ and τ constant. θ-RUN = maximal run of one phase with θ = Ξ(o) constant.
f_j / g_j = j-th Even S4c fallback transition with both ends in the θ-run / phase.
Counters FAIL_* are violations (each printed). Regime stats (the point of box 41):
  PF_post[u]  = # states t > f_{u-1} in θ-runs with |U| = u;  PF_tr[u] = # transitions t -> t+1 of Θ with t > f_{u-1}.
  HF_post[u]  = # states t > g_{u-2} in phases with |U| = u;  HF_postH1[u] = those with H1.
Usage: pfz17.py game.pg ...      (env PFZ_CAP: simple-path DFS budget per graph, default 2e6 path steps)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "so"))
import sox
CAP = int(float(os.environ.get("PFZ_CAP", "2e6")))

class Budget(Exception): pass

def paths_best(g, nodes, sinks, start_w, wt, jmax):
    """best[z][j] = max over simple paths p from z (in nodes) to a sink with <= j edges of wt(p minus end) + start_w[end].
    Graph: Even v in nodes \\ sinks keeps its edges into nodes; Odd v in nodes \\ sinks keeps its forced edge if in nodes."""
    steps = [0]; best = {}
    def succ(u):
        if g.owner[u] == 0: return sorted(x for x in set(g.succ[u]) if x in nodes)
        x = g.succ[u][0]; return [x] if x in nodes else []
    for z in nodes:
        b = [None] * (jmax + 1)
        def dfs(u, seen, w, d):
            steps[0] += 1
            if steps[0] > CAP: raise Budget()
            if u in sinks:
                v = w + start_w[u]
                for j in range(d, jmax + 1):
                    if b[j] is None or v > b[j]: b[j] = v
                return
            if d == jmax: return
            for x in succ(u):
                if x not in seen: dfs(x, seen | {x}, w + wt(u), d + 1)
        dfs(z, {z}, 0, 0); best[z] = b
    return best

def bump(acc, k, v=1): acc[k] = acc.get(k, 0) + v
def mx(acc, k, v, *ex):
    if k not in acc or v > acc[k][0]: acc[k] = (v,) + ex

def states(g, cap=3000, tr=None):
    S, FB, E = sox.trace(g, cap=cap) if tr is None else tr; o = sox.oddchoice(g)[0]; n = g.n; rows = []
    for k, (s, t) in enumerate(S):
        Xi, sb = E.evaluate(tuple(s))
        def cyc(nxt):
            seen = []; v = o
            while v not in seen: seen.append(v); v = nxt(v)
            return o in seen[seen.index(v):]
        h1 = not cyc(lambda v: s[v] if g.owner[v] == 0 else sb[v]); h2 = not cyc(lambda v: s[v] if g.owner[v] == 0 else t[v])
        R = set()
        for v in range(n):
            if v == o: continue
            seen = set(); x = v
            while x not in seen and x != o: seen.add(x); x = s[x] if g.owner[x] == 0 else t[x]
            if x == o: R.add(v)
        rows.append(dict(s=s, t=t, Xi=Xi, sb=sb, h1=h1, h2=h2, R=R, fb=FB[k] if k < len(FB) else None,
                         lam=tuple(x[0] for x in Xi)))
    return rows, o, E

def analyse(g, acc, name, rows=None):
    if rows is None: rows, o, E = states(g)
    else: rows, o, E = rows
    n = g.n; N = len(rows); dego = len(set(g.succ[o])); bump(acc, "files")
    a = 0
    while a < N:
        b = a
        while b + 1 < N and rows[b + 1]["lam"] == rows[a]["lam"] and rows[b + 1]["t"] == rows[a]["t"]: b += 1
        bump(acc, "phases")
        ct = rows[a]["Xi"][o][0]; U = {z for z in range(n) if rows[a]["Xi"][z][0] == ct}; u = len(U); Uh = U - {o}
        hi = E.rank[ct]; wt = lambda v: (E.weight(E.bit[v]) if E.rank[v] > hi else 0)
        M = lambda t, z: E.weight(rows[t]["Xi"][z][1]); L = lambda t, z: rows[t]["Xi"][z][2]
        F = lambda t: set(range(n)) - rows[t]["R"] - {o}
        caseA = E.rank[o] > hi
        # ---------- P-N5-RHO: Y-FORM at every state
        for t in range(a, b + 1):
            if rows[t]["h1"]:
                Y = [y for y in set(g.succ[o]) if y in U and y in F(t)]; bump(acc, "YF_checks")
                if rows[t]["sb"][o] not in Y or M(t, o) != wt(o) + min(M(t, y) for y in Y):
                    bump(acc, "FAIL_YF"); print("FAIL_YF", name, t, flush=True)
            else:
                bump(acc, "YF0_checks")
                if rows[t]["Xi"][o][1] != 0: bump(acc, "FAIL_YF0"); print("FAIL_YF0", name, t, flush=True)
        # ---------- HAT-FREEZE (a)-(c), RHO-TAIL on the phase
        g_fb = [k for k in range(a, b) if rows[k]["fb"]]
        try:
            jm = max(u - 2, 0); bh = paths_best(g, Uh, {ct}, {ct: 0}, wt, jm) if u >= 2 else {}
            for j in range(1, min(jm, len(g_fb)) + 1):
                for t in range(g_fb[j - 1] + 1, b + 1):
                    for z in Uh:
                        if bh[z][j] is None: continue
                        bump(acc, "HFa_checks")
                        if M(t, z) < bh[z][j]: bump(acc, "FAIL_HFa"); print("FAIL_HFa", name, a, j, t, z, flush=True)
            for t in range(a, b + 1):
                for z in F(t) & U:
                    bump(acc, "HFb_checks")
                    if u < 2 or bh[z][jm] is None or M(t, z) > bh[z][jm]: bump(acc, "FAIL_HFb"); print("FAIL_HFb", name, t, z, flush=True)
            if u >= 2 and len(g_fb) >= u - 2:
                st = a if u == 2 else g_fb[u - 3] + 1
                bump(acc, f"HF_post_U{u}", b - st + 1); bump(acc, f"HF_postH1_U{u}", sum(rows[t]["h1"] for t in range(st, b + 1)))
                if any(M(a, y) != bh[y][jm] for y in F(a) & U):   # NONTRIVIAL: some F ∩ U vertex below MoptÛ at the phase start
                    bump(acc, f"HF_post_nontriv_U{u}", b - st + 1); mx(acc, "max_HF_nontriv_U", u, name, a, b - st + 1)
                for t in range(st, b + 1):
                    for y in F(t) & U:
                        bump(acc, f"HFc_checks_U{min(u, 9)}")
                        if bh[y][jm] is None or M(t, y) != bh[y][jm]: bump(acc, "FAIL_HFc"); print("FAIL_HFc", name, a, t, y, flush=True)
                rt = sum(1 for t in range(st, b) if rows[t]["Xi"][o][1] != rows[t + 1]["Xi"][o][1])
                mx(acc, f"max_RT_U{min(u, 9)}", rt, name, a, dego)
                if rt > dego: bump(acc, "FAIL_RT"); print("FAIL_RT", name, a, rt, dego, flush=True)
            mx(acc, f"max_hat_excess_U{u}", len(g_fb) - (u - 2), name, a)
        except Budget: bump(acc, "HF_phase_budget_skip")
        # ---------- N5-NHN-box40 (working doc, l-new; sha1 81302f57): T0U, EV2-FB, SG-EV, T0-PIN, NHN-BOUND, for τ(o) ≠ o
        t0 = rows[a]["t"][o]; HN = [rows[t]["h1"] and not rows[t]["h2"] for t in range(a, b + 1)]
        if t0 != o and any(HN):
            bump(acc, "NHN_phases")
            if t0 not in U - {o, ct}: bump(acc, "FAIL_T0U"); print("FAIL_T0U", name, a, flush=True)
            for t in range(a, b + 1):
                if (not rows[t]["h2"]) != (t0 in rows[t]["R"]): bump(acc, "FAIL_T0U_H2"); print("FAIL_T0U_H2", name, t, flush=True)
            gi = {k: j + 1 for j, k in enumerate(g_fb)}; drops = ev2 = post = 0
            for k in range(a, b):
                if rows[k]["h1"] and not rows[k + 1]["h1"]: drops += 1
                if HN[k - a] and rows[k + 1]["h1"] and rows[k + 1]["h2"]:
                    ev2 += 1; bump(acc, "EV2_ends"); mx(acc, "max_EV2_fbindex_minus_(U-1)", gi.get(k, -99) - (u - 1), name, k, u)
                    if not rows[k]["fb"] or t0 not in rows[k]["R"] or t0 in rows[k + 1]["R"]: bump(acc, "FAIL_EV2FB"); print("FAIL_EV2FB", name, k, flush=True)
                    if not E.key(rows[k]["Xi"][t0]) < E.key(rows[k + 1]["Xi"][t0]): bump(acc, "FAIL_SGEV"); print("FAIL_SGEV", name, k, flush=True)
                    if rows[k]["fb"] and gi[k] >= u - 1:
                        post += 1; bump(acc, "EV2_post")
                        try:
                            mo = paths_best(g, Uh, {ct}, {ct: 0}, wt, max(u - 2, 0))[t0][max(u - 2, 0)]
                            if not (M(k, t0) == M(k + 1, t0) == mo): bump(acc, "FAIL_T0PIN"); print("FAIL_T0PIN", name, k, flush=True)
                        except Budget: bump(acc, "T0PIN_budget_skip")
                        if rows[k]["Xi"][t0][1] != rows[k + 1]["Xi"][t0][1]: bump(acc, "FAIL_T0LEN"); print("FAIL_T0LEN", name, k, flush=True)
            if post > u - 2: bump(acc, "FAIL_NHN_POST"); print("FAIL_NHN_POST", name, a, flush=True)
            if ev2 > 2 * (u - 2): bump(acc, "FAIL_NHN_EV2"); print("FAIL_NHN_EV2", name, a, flush=True)
            nhn = sum(1 for i in range(len(HN)) if HN[i] and (i == 0 or not HN[i - 1])); T = u * (n + 1) + n - 1
            if nhn > 1 + drops + ev2 or nhn > 1 + (T + 1) // 2 + 2 * (u - 2): bump(acc, "FAIL_NHN"); print("FAIL_NHN", name, a, flush=True)
            mx(acc, "max_N_HN", nhn, name, a, u, drops, ev2, post); mx(acc, "max_EV2_phase", ev2, name, a, u)
        # ---------- θ-runs: P-FREEZE (a)-(c), LEN-TAIL, NO-CROSS-A
        s0 = a
        while s0 <= b:
            e0 = s0
            while e0 + 1 <= b and rows[e0 + 1]["Xi"][o] == rows[s0]["Xi"][o]: e0 += 1
            bump(acc, "theta_runs")
            f_fb = [k for k in range(s0, e0) if rows[k]["fb"]]
            mx(acc, f"max_pfz_excess_U{u}", len(f_fb) - (u - 1), name, s0)
            try:
                Mth = {o: wt_set(E, rows[s0]["Xi"][o][1]), ct: 0}
                jm = max(u - 1, 0); bp = paths_best(g, U, {o, ct}, Mth, wt, jm)
                for j in range(0, min(jm, len(f_fb)) + 1):
                    t0 = s0 if j == 0 else f_fb[j - 1] + 1
                    for t in range(t0, e0 + 1):
                        for z in U:
                            if bp[z][j] is None: continue
                            bump(acc, "PFa_checks")
                            if M(t, z) < bp[z][j]: bump(acc, "FAIL_PFa"); print("FAIL_PFa", name, s0, j, t, z, flush=True)
                for t in range(s0, e0 + 1):
                    for z in U:
                        bump(acc, "PFb_checks")
                        if bp[z][jm] is None or M(t, z) > bp[z][jm]: bump(acc, "FAIL_PFb"); print("FAIL_PFb", name, t, z, flush=True)
                if len(f_fb) >= u - 1 and u >= 2:
                    st = f_fb[u - 2] + 1
                    bump(acc, f"PF_post_U{u}", e0 - st + 1); bump(acc, f"PF_tr_U{u}", e0 - st)
                    if any(M(s0, z) != bp[z][jm] for z in U):   # NONTRIVIAL: M was below Mopt somewhere at the run's start
                        bump(acc, f"PF_post_nontriv_U{u}", e0 - st + 1); mx(acc, "max_PF_nontriv_U", u, name, s0, e0 - st + 1)
                    for t in range(st, e0 + 1):
                        for z in U:
                            bump(acc, f"PFc_checks_U{min(u, 9)}")
                            if M(t, z) != bp[z][jm] or rows[t]["Xi"][z][1] != rows[st]["Xi"][z][1]:
                                bump(acc, "FAIL_PFc"); print("FAIL_PFc", name, s0, t, z, flush=True)
                    nr = 0
                    for t in range(st, e0):
                        rise = [z for z in U if E.key(rows[t]["Xi"][z]) < E.key(rows[t + 1]["Xi"][z])]
                        if rise:
                            nr += 1; bump(acc, "LT_rise_transitions")
                            if any(rows[t]["Xi"][z][1] != rows[t + 1]["Xi"][z][1] for z in rise):
                                bump(acc, "FAIL_LT_notlen"); print("FAIL_LT_notlen", name, t, flush=True)
                        if caseA and rows[t]["h1"] and rows[t + 1]["h1"]:
                            bump(acc, "NCA_checks")
                            if rows[t]["R"] != rows[t + 1]["R"]: bump(acc, "FAIL_NCA"); print("FAIL_NCA", name, t, flush=True)
                    mx(acc, f"max_LT_U{min(u, 9)}", nr, name, s0)
                    if nr > u * (u - 1): bump(acc, "FAIL_LT"); print("FAIL_LT", name, s0, nr, flush=True)
            except Budget: bump(acc, "PF_run_budget_skip")
            s0 = e0 + 1
        a = b + 1
    return acc

def wt_set(E, mask): return E.weight(mask)   # wt(P(θ)) = signed weight of θ's path set (its vertices have rank > rank(c_θ))

if __name__ == "__main__":
    acc = {}
    for f in sys.argv[1:]:
        try: g = sox.load(f)
        except Exception: bump(acc, "load_fail"); continue
        if len(sox.oddchoice(g)) != 1: bump(acc, "skipped_not_C1O"); continue
        analyse(g, acc, f)
    for k in sorted(acc): print(k, acc[k])
