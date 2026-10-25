#!/usr/bin/env python3
"""REFEREE succ. 9 probe for packets P-N5-PFZ (docs/new/P-N5-PFZ-box39.md, pin 283bcb6, sha1 3c617e06...) and P-N5-PFZ-ext
(docs/new/P-N5-PFZ-ext-box39.md, pin c61ecc4, sha1 b3702b1b...). Own engine (rl_engine, rl_probe.states; no lane code). C^1O asserted.
Phase key = (lambda_Xi, tau); U = lambda^-1(c_theta); M_t(z) = signed weight of P(Xi_t z); wt(v) = sgn(v) 2^rank(v) above c_theta.
Every check runs for both epoch kinds: EP = "theta" (theta-runs, P-N5-PFZ) and EP = "P" (P-epochs, P-N5-PFZ-ext).
 ADD     (A) at every state, z in U \\ {c_theta}: next(z) in U and M(z) = wt(z) + M(next z)
 FBR     FB-ROUND at every in-phase Even fallback, Even v in U \\ {c_theta}, successor x in U
 UB      P-FREEZE (b): M_t <= Mopt (exact DFS over simple paths in G_U; |U| <= UMAX)
 PFA     P-FREEZE (a): for t > f_j, M_t(z) >= best path value with <= j edges (|U| <= UMAX)
 PFC     P-FREEZE (c): after f_{|U|-1}: M_t = Mopt (if computed) and P constant on U
 LEN     LEN-TAIL: post-freeze U-rises are length rises and number <= |U|(|U|-1) per epoch
 NXA     NO-CROSS-A: case A, post-freeze transition, H1 at both ends: no crossing
 TLEN    theta-LEN (P-epochs): theta-changes inside an epoch <= max(|U|-2, 0)
 RISE    RISE' for every break window; BRK-POLY (i), (ii); BRK-POLY' (i) as stated and corrected, (ii), (iii)
Usage: pfz_probe.py lib37 | files..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P
EX = []
UMAX = int(os.environ.get("UMAX", "13"))


def run(g, cnt, name):
    o, st = P.states(g); n = g.n; T = len(st) - 1
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    # phases
    phases, k = [], 0
    while k <= T:
        j = k
        while j < T and inph[j]: j += 1
        phases.append((k, j)); k = j + 1
    sgn = lambda v: 1 if g.prio[v] % 2 == 0 else -1
    for (p0, p1) in phases:
        c = st[p0]["Xi"][o][0]
        U = [v for v in range(n) if st[p0]["Xi"][v][0] == c]
        Us = set(U)
        if any({v for v in range(n) if st[t]["Xi"][v][0] == c} != Us for t in range(p0, p1 + 1)): cnt["U_const_FAIL"] += 1
        wt = {v: (sgn(v) << g.rank[v]) if g.rank[v] > g.rank[c] else 0 for v in U}

        def M(t, z):
            m, s = st[t]["Xi"][z][1], 0
            r = 0
            while m:
                if m & 1: s += (1 << r) if g.prio[g.byrank[r]] % 2 == 0 else -(1 << r)
                m >>= 1; r += 1
            return s
        nxt = lambda t, z: st[t]["s"][z] if g.owner[z] == 0 else st[t]["sb"][z]
        # (A)
        for t in range(p0, p1 + 1):
            for z in U:
                if z == c: continue
                cnt["ADD_chk"] += 1
                x = nxt(t, z)
                if x not in Us or M(t, z) != wt[z] + M(t, x): cnt["ADD_FAIL"] += 1; EX.append((name, "ADD", t, z))
        # FB-ROUND
        for t in range(p0, p1):
            if not (st[t]["fb"] and st[t]["Is"]): continue
            for v in U:
                if v == c or g.owner[v] != 0: continue
                for x in g.succ[v]:
                    if x not in Us: continue
                    cnt["FBR_chk"] += 1
                    if M(t + 1, v) < wt[v] + M(t, x): cnt["FBR_FAIL"] += 1; EX.append((name, "FBR", t, v, x))
        # G_U
        succU = {}
        for v in U:
            if v in (o, c): succU[v] = []
            elif g.owner[v] == 0: succU[v] = [x for x in g.succ[v] if x in Us]
            else: succU[v] = [g.succ[v][0]]

        def best(z, j, term):
            """max wt(p \\ end) + term[end] over simple paths p from z to a terminal with <= j edges (None if none)"""
            bestv = [None]

            def dfs(v, seen, acc, d):
                if v in term:
                    val = acc + term[v]
                    if bestv[0] is None or val > bestv[0]: bestv[0] = val
                    return
                if d == j: return
                for x in succU[v]:
                    if x not in seen: seen.add(x); dfs(x, seen, acc + wt[v], d + 1); seen.discard(x)
            dfs(z, {z}, 0, 0)
            return bestv[0]
        for EP in ("theta", "P"):
            keyf = (lambda t: st[t]["Xi"][o]) if EP == "theta" else (lambda t: st[t]["Xi"][o][1])
            epochs, t = [], p0
            while t <= p1:
                u = t
                while u < p1 and keyf(u + 1) == keyf(t): u += 1
                epochs.append((t, u)); t = u + 1
            for (e0, e1) in epochs:
                cnt["%s_epochs" % EP] += 1
                fbs = [t for t in range(e0, e1) if st[t]["fb"] and st[t]["Is"]]
                term = {o: M(e0, o), c: 0}
                small = len(U) <= UMAX
                if small:
                    mopt = {z: best(z, len(U), term) for z in U}
                    for t in range(e0, e1 + 1):
                        for z in U:
                            cnt["%s_UB_chk" % EP] += 1
                            if M(t, z) > mopt[z]: cnt["%s_UB_FAIL" % EP] += 1; EX.append((name, EP, "UB", t, z))
                    for jj in range(1, min(len(fbs), len(U) - 1) + 1):
                        bj = {z: best(z, jj, term) for z in U}
                        for t in range(fbs[jj - 1] + 1, e1 + 1):
                            for z in U:
                                if bj[z] is None: continue
                                cnt["%s_PFA_chk" % EP] += 1
                                if M(t, z) < bj[z]: cnt["%s_PFA_FAIL" % EP] += 1; EX.append((name, EP, "PFA", jj, t, z))
                else: cnt["%s_epochs_bigU_skipped" % EP] += 1
                fz = fbs[len(U) - 2] if len(U) >= 2 and len(fbs) >= len(U) - 1 else (e0 - 1 if len(U) == 1 else None)
                if EP == "P":
                    th = sum(st[t]["Xi"][o] != st[t + 1]["Xi"][o] for t in range(e0, e1))
                    cnt["P_theta_changes_in_epochs"] += th
                    if th > max(len(U) - 2, 0): cnt["TLEN_FAIL"] += 1; EX.append((name, "TLEN", e0, th, len(U)))
                    # referee's refined count (repair of BRK-POLY' (i)): moves <= |A_low| - [o low], A_low = U \ {c} below c
                    alow = sum(1 for v in U if v != c and g.rank[v] < g.rank[c])
                    if th > alow - (1 if g.rank[o] < g.rank[c] else 0): cnt["TLEN_refined_FAIL"] += 1; EX.append((name, "TLENref", e0, th))
                    if len(set(st[t]["Xi"][o][1] for t in range(p0, p1 + 1))) > 1 and not any(v not in (o, c) and g.rank[v] > g.rank[c] for v in U):
                        cnt["RHO_needs_high_FAIL"] += 1
                if fz is None: continue
                cnt["%s_postfreeze_epochs_U%s" % (EP, "1" if len(U) == 1 else ("2" if len(U) == 2 else ">=3"))] += 1
                post = [t for t in range(fz + 1, e1 + 1)]
                for t in post:
                    cnt["%s_PFC_states" % EP] += 1
                    if any(st[t]["Xi"][z][1] != st[post[0]]["Xi"][z][1] for z in U): cnt["%s_PFC_FAIL" % EP] += 1; EX.append((name, EP, "PFC", t))
                    if small and any(M(t, z) != mopt[z] for z in U): cnt["%s_PFCopt_FAIL" % EP] += 1
                urise = 0
                for t in post[:-1]:
                    rz = [z for z in U if g.key(st[t]["Xi"][z]) < g.key(st[t + 1]["Xi"][z])]
                    if rz:
                        urise += 1
                        if any(st[t]["Xi"][z][1] != st[t + 1]["Xi"][z][1] for z in rz): cnt["%s_LEN_shape_FAIL" % EP] += 1
                    if g.rank[o] > g.rank[c] and st[t]["H1"] and st[t + 1]["H1"]:
                        cnt["%s_NXA_chk" % EP] += 1
                        if st[t]["Rb"] != st[t + 1]["Rb"]: cnt["%s_NXA_FAIL" % EP] += 1; EX.append((name, EP, "NXA", t))
                cnt["%s_post_urise_transitions" % EP] += urise
                if urise > len(U) * (len(U) - 1): cnt["%s_LEN_FAIL" % EP] += 1
        # HN stretches of the phase: breaks, RISE', BRK-POLY / BRK-POLY'
        HN = [st[t]["H1"] and not st[t]["H2"] for t in range(T + 1)]
        R = [st[t]["Rb"] - {o} for t in range(T + 1)]
        t = p0
        while t <= p1:
            if not HN[t]: t += 1; continue
            s0 = t
            while t < p1 and HN[t + 1]: t += 1
            s1 = t; t += 1
            trs = range(s0, s1)
            cr = lambda x: R[x] != R[x + 1]
            ent = [x for x in trs if cr(x) and R[x] < R[x + 1]]
            ev = [x for x in trs if cr(x) and st[x + 1]["Rb"] < st[x]["Rb"]]
            thS = sum(st[x]["Xi"][o] != st[x + 1]["Xi"][o] for x in trs)
            rhoS = sum(st[x]["Xi"][o][1] != st[x + 1]["Xi"][o][1] for x in trs)
            B = 0
            for e in ent:
                pe = max([x for x in ent if x < e], default=-1)
                evs = [x for x in ev if pe < x < e]
                if not evs: continue
                B += 1; a = evs[-1]
                if not (st[a]["fb"] and st[a]["Is"]): cnt["BRK_evfb_FAIL"] += 1
                k1 = any(st[x]["Xi"][o] != st[x + 1]["Xi"][o] for x in range(a + 1, e + 1))
                k2 = False
                for x in range(a, e):
                    if any(st[y]["Xi"][o] != st[y + 1]["Xi"][o] for y in range(a, x + 1)): break
                    if any(z != o and g.key(st[x]["Xi"][z]) < g.key(st[x + 1]["Xi"][z]) for z in st[x]["Rb"] & st[x + 1]["Rb"]): k2 = True; break
                cnt["RISE_chk"] += 1
                if not (k1 or k2): cnt["RISE_FAIL"] += 1; EX.append((name, "RISE'", a, e))
                cnt["breaks_kind1" if k1 else "breaks_kind2"] += 1
            u = len(U); cnt["stretches"] += 1; cnt["breaks"] += B
            if B > thS + (thS + 1) * (u - 1 + u * (u - 1)): cnt["BRKi_FAIL"] += 1; EX.append((name, "BRK-POLY i", s0))
            if g.rank[o] > g.rank[c] and B > thS + (thS + 1) * (u - 1): cnt["BRKii_FAIL"] += 1; EX.append((name, "BRK-POLY ii", s0))
            # BRK-POLY' (ext)
            if thS > (rhoS + 1) * max(u - 2, 0):
                cnt["BRKP_i_AS_STATED_viol"] += 1; EX.append((name, "BRK-POLY' (i) as stated", s0, s1, "theta_S", thS, "rho_S", rhoS, "|U|", u))
            if thS > rhoS + (rhoS + 1) * max(u - 2, 0): cnt["BRKP_i_corrected_FAIL"] += 1
            if B > thS + (rhoS + 1) * (u - 1 + u * (u - 1)): cnt["BRKP_ii_FAIL"] += 1
            if B > (rhoS + 1) * (2 * n * n - 1): cnt["BRKP_ii_final_FAIL"] += 1
            if B > (rhoS + 1) * (u * u + u - 3): cnt["BRKP_ii_mid_AS_STATED_viol"] += 1
            if g.rank[o] > g.rank[c]:
                if B > thS + (rhoS + 1) * (u - 1): cnt["BRKP_iii_FAIL"] += 1
                if u >= 2 and B > (rhoS + 1) * (2 * n - 3): cnt["BRKP_iii_final_AS_STATED_viol"] += 1
            cnt["stretch_rho_pos"] += rhoS > 0


def main(a):
    files = [os.path.join(P.ROOT, l.split()[0]) for l in open(os.path.join(P.ROOT, "experiments/new/box37/lib37.txt")) if l.strip()] \
        if a == ["lib37"] else a
    cnt = Counter()
    for f in files:
        g = RE.parse(f)
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        try: run(g, cnt, os.path.relpath(f, P.ROOT))
        except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-34s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:25]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
