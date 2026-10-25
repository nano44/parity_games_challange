#!/usr/bin/env python3
"""REFEREE succ. 10 probe for packet P-N5-RHO (docs/new/P-N5-RHO-box40.md, pin c814455, sha1 cd5df65c...).
Own engine (rl_engine, rl_probe.states; no lane code). C^1O asserted per game. Phase = (lambda_Xi, tau)-run; U = lambda^-1(c_theta);
Uh = U \\ {o}; M_t(z) = signed weight of P(Xi_t z); wt(v) = sgn(v) 2^rank(v) if rank(v) > rank(c_theta) else 0; HN = H1 and not H2.
g_1 < g_2 < ... = in-phase Even S4c fallback transitions. Checks (every *_FAIL must be 0):
 CLS   every in-phase transition is S4a (Is nonempty, no fb) or an Even fallback (fb with Is nonempty); F-FLAT at HN fallbacks
 YFA   Y-FORM (a) at every H1 state: sigmabar(o) in Y_t and M(o) = wt(o) + min_Y M; YFB: at not-H1 states M(o) = 0
 HFA   HAT-FREEZE (a) for every j <= #fallbacks, t > g_j, z in Uh, against the exact best path of G_Uh with <= j edges (|U| <= UMAX)
 HFB   HAT-FREEZE (b) every state, z in F_t cap U: Mopt defined and M <= Mopt;  HFC: (c) after g_{|U|-2}
 RT    RHO-TAIL: P(theta)-changes after g_{|U|-2} <= deg(o)
 BFF   BF-F at in-phase S4a transitions with HN at k and k+1 (and, separately, HN at k only: BFFk), with sub-case counts
 FFA/FFB/FFC  FREEZE-F on maximal fallback-free HN runs (exact G[F_t cap U] paths when |U| <= UMAX)
 RHO   RHO-HN per phase; HNP: HN-POLY's per-stretch chain (i'), (ii) with the packet's constants, EPOCH sums
Usage: rho_probe.py lib | files..."""
import sys, os, glob
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P
EX = []
UMAX = int(os.environ.get("UMAX", "14"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def run(g, cnt, name):
    o, st = P.states(g); n = g.n; T = len(st) - 1
    sgn = lambda v: 1 if g.prio[v] % 2 == 0 else -1
    deg = len(g.succ[o]); nE = sum(1 for v in range(n) if g.owner[v] == 0); K = nE * (2 * n - 1)
    phases, k = [], 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        phases.append((k, j)); k = j + 1
    for (p0, p1) in phases:
        cnt["phases"] += 1
        c = st[p0]["Xi"][o][0]
        U = [v for v in range(n) if st[p0]["Xi"][v][0] == c]; Us = set(U); Uh = [v for v in U if v != o]
        wt = {v: (sgn(v) << g.rank[v]) if g.rank[v] > g.rank[c] else 0 for v in U}

        def M(t, z):
            m, s, r = st[t]["Xi"][z][1], 0, 0
            while m:
                if m & 1: s += (1 << r) if g.prio[g.byrank[r]] % 2 == 0 else -(1 << r)
                m >>= 1; r += 1
            return s
        HN = {t: st[t]["H1"] and not st[t]["H2"] for t in range(p0, p1 + 1)}
        fbs = [t for t in range(p0, p1) if st[t]["fb"]]
        for t in range(p0, p1):
            ok = (st[t]["Is"] and not st[t]["fb"] and st[t + 1]["t"] == st[t]["t"]) or (st[t]["fb"] and st[t]["Is"])
            cnt["CLS_chk"] += 1
            if not ok: fail(cnt, "CLS", name, t)
            if st[t]["fb"] and HN[t] and st[t + 1]["Xi"][o] != st[t]["Xi"][o]: fail(cnt, "FFLAT", name, t)
        small = len(U) <= UMAX

        def best(z, j, allowed):
            """max wt(p minus c) over simple paths z -> c with <= j edges inside allowed (c a sink; Odd forced edge; Even edges in)"""
            res = [None]

            def dfs(v, seen, acc, d):
                if v == c:
                    if res[0] is None or acc > res[0]: res[0] = acc
                    return
                if d == j: return
                nxs = g.succ[v] if g.owner[v] == 0 else ([g.succ[v][0]] if len(g.succ[v]) == 1 else [])
                for x in nxs:
                    if x in allowed and x not in seen: seen.add(x); dfs(x, seen, acc + wt[v], d + 1); seen.discard(x)
            if z not in allowed: return None
            dfs(z, {z}, 0, 0)
            return res[0]
        UhS = set(Uh)
        if c == o: cnt["phases_c_eq_o"] += 1
        # Y-FORM
        for t in range(p0, p1 + 1):
            if st[t]["H1"]:
                Y = [y for y in g.succ[o] if y in Us and y in st[t]["F"]]
                cnt["YFA_chk"] += 1
                if st[t]["sb"][o] not in Y or M(t, o) != wt[o] + min(M(t, y) for y in Y): fail(cnt, "YFA", name, t)
            else:
                cnt["YFB_chk"] += 1
                if st[t]["Xi"][o][1] != 0: fail(cnt, "YFB", name, t)
        # HAT-FREEZE
        mopt = {z: best(z, len(U), UhS) for z in Uh} if small else None
        if not small: cnt["HF_bigU_phases_skipped"] += 1
        if small:
            for jj in range(1, len(fbs) + 1):
                bj = {z: best(z, jj, UhS) for z in Uh}
                for t in range(fbs[jj - 1] + 1, p1 + 1):
                    for z in Uh:
                        if bj[z] is None: continue
                        cnt["HFA_chk"] += 1
                        if M(t, z) < bj[z]: fail(cnt, "HFA", name, jj, t, z)
            for t in range(p0, p1 + 1):
                for z in U:
                    if z not in st[t]["F"]: continue
                    cnt["HFB_chk"] += 1
                    if z == o or mopt.get(z) is None or M(t, z) > mopt[z]: fail(cnt, "HFB", name, t, z)
        if len(U) >= 2 and len(fbs) >= len(U) - 2:
            fz = fbs[len(U) - 3] if len(U) >= 3 else p0 - 1
            key = "U2" if len(U) == 2 else ("U3" if len(U) == 3 else "U4+")
            cnt["postfreeze_phases_" + key] += 1
            post = list(range(fz + 1, p1 + 1))
            if any(st[t]["H1"] for t in post): cnt["postfreeze_phases_withH1_" + key] += 1
            for t in post:
                if small:
                    for y in U:
                        if y in st[t]["F"]:
                            cnt["HFC_chk_" + key] += 1
                            if M(t, y) != mopt[y]: fail(cnt, "HFC", name, t, y)
            ch = sum(st[t]["Xi"][o][1] != st[t + 1]["Xi"][o][1] for t in post[:-1])
            cnt["RT_changes_" + key] += ch
            cnt["RT_max"] = max(cnt["RT_max"], ch)
            if ch > deg: fail(cnt, "RT", name, p0, ch, deg)
        # BF-F
        for k in range(p0, p1):
            if st[k]["fb"] or not HN[k]: continue
            for v in U:
                if v == c or g.owner[v] != 0 or v not in st[k + 1]["F"]: continue
                for x in g.succ[v]:
                    if x not in Us: continue
                    both = HN[k + 1]
                    tag = "BFF" if both else "BFFk"
                    cnt[tag + "_chk"] += 1
                    if M(k, x) <= M(k, st[k]["s"][v]): cnt[tag + "_case1"] += 1
                    elif x in st[k]["Rb"]: cnt[tag + "_case2_R"] += 1
                    else:
                        pre, cyc = RE.lasso(st[k]["nx"], x)
                        cnt[tag + ("_case2_passv" if v in pre + cyc else "_case2_avoid")] += 1
                    if M(k + 1, v) < wt[v] + M(k, x): fail(cnt, tag, name, k, v, x)
        # FREEZE-F on maximal fallback-free HN runs
        t = p0
        while t <= p1:
            if not HN[t]: t += 1; continue
            s = t
            while t < p1 and HN[t + 1] and not st[t]["fb"]: t += 1
            e = t; t += 1
            cnt["FF_runs"] += 1
            if e > s: cnt["FF_runs_gt1"] += 1
            for x in range(s, e):
                if not st[x + 1]["F"] <= st[x]["F"]: fail(cnt, "FF_shrink", name, x)
            if small:
                for x in range(s, e + 1):
                    A = (st[x]["F"] & Us) | {c}
                    if c not in st[x]["F"]: fail(cnt, "FF_cF", name, x)
                    for z in st[x]["F"] & Us:
                        bz = best(z, min(x - s, len(U)), A)
                        if bz is not None:
                            cnt["FFA_chk"] += 1
                            if M(x, z) < bz: fail(cnt, "FFA", name, s, x, z)
            t0 = s + max(len(U) - 2, 0)
            for x in range(t0, e + 1):
                for x2 in range(x, e + 1):
                    for z in st[x2]["F"] & Us:
                        cnt["FFB_chk"] += 1
                        if M(x2, z) != M(x, z): fail(cnt, "FFB", name, s, x, x2, z)
            ch = sum(st[x]["Xi"][o][1] != st[x + 1]["Xi"][o][1] for x in range(s, e))
            ch2 = sum(st[x]["Xi"][o][1] != st[x + 1]["Xi"][o][1] for x in range(max(s, t0), e))
            cnt["FFC_changes"] += ch; cnt["FFC_changes_second_term"] += ch2
            cnt["FFC_max"] = max(cnt["FFC_max"], ch)
            if e >= t0 and e > s: cnt["FFB_runs_nonvacuous"] += 1
            if ch > max(len(U) - 2, 0) + deg - 1: fail(cnt, "FFC", name, s, ch)
        # RHO-HN, HN-POLY
        rho = sum(HN[x] and HN[x + 1] and st[x]["Xi"][o][1] != st[x + 1]["Xi"][o][1] for x in range(p0, p1))
        stretches, t = [], p0
        while t <= p1:
            if not HN[t]: t += 1; continue
            s = t
            while t < p1 and HN[t + 1]: t += 1
            stretches.append((s, t)); t += 1
        NHN = len(stretches)
        if NHN: cnt["phases_with_HN"] += 1
        cnt["RHO_total"] += rho; cnt["RHO_max"] = max(cnt["RHO_max"], rho)
        if len(U) >= 2 and rho > (NHN + len(U) - 2) * (len(U) + deg - 3) + deg: fail(cnt, "RHO", name, p0, rho)
        sB = sX = sf = sth = srho = 0
        for (s, e) in stretches:
            R = [st[x]["Rb"] - {o} for x in range(s, e + 1)]
            th = sum(st[x]["Xi"][o] != st[x + 1]["Xi"][o] for x in range(s, e))
            rS = sum(st[x]["Xi"][o][1] != st[x + 1]["Xi"][o][1] for x in range(s, e))
            ent = [x for x in range(s, e) if R[x - s] < R[x + 1 - s]]
            ev = [x for x in range(s, e) if R[x - s] != R[x + 1 - s] and not R[x - s] < R[x + 1 - s]]
            X = sum(R[x - s] != R[x + 1 - s] for x in range(s, e))
            f = sum(1 for x in range(s, e) if st[x]["fb"])
            B = 0
            for a in ent:
                pe = max([x for x in ent if x < a], default=-1)
                if any(pe < x < a for x in ev): B += 1
            u = len(U)
            if th > rS + (rS + 1) * max(u - 2, 0): fail(cnt, "HNP_i_weak", name, s)
            if B > th + (rS + 1) * (u * u - 1): fail(cnt, "HNP_ii", name, s)
            if B > (rS + 1) * (u * u + u - 2): fail(cnt, "HNP_ii_mid", name, s)
            if B > (rS + 1) * (2 * n * n - 1): fail(cnt, "HNP_ii_final", name, s)
            if X > 2 * (n - 1) * (B + 1): fail(cnt, "EPOCH_X", name, s)
            if f > K * (X + 1) + X: fail(cnt, "EPOCH_f", name, s)
            sB += B; sX += X; sf += f; sth += th; srho += rS
        if srho > rho: fail(cnt, "HNP_rhosum", name, p0)
        if sth > rho + (rho + NHN) * max(len(U) - 2, 0): fail(cnt, "HNP_thsum", name, p0)
        if sB > (rho + NHN) * (2 * n * n - 1): fail(cnt, "HNP_Bsum", name, p0)
        fHN = sum(1 for x in range(p0, p1) if st[x]["fb"] and HN[x])
        if fHN > sf + NHN: fail(cnt, "HNP_fbHN", name, p0)
        cnt["HN_breaks"] += sB; cnt["HN_crossings"] += sX; cnt["HN_fallbacks"] += fHN; cnt["HN_theta_changes"] += sth
        if st[p0]["t"][o] == o:
            # NHN-TOG (citation note): tau(o) = o => not-H2 everywhere, so HN = H1 and N_HN <= floor(T_ph/2) + 1 (R34 (e)), cases A and B
            if any(st[x]["H2"] for x in range(p0, p1 + 1)): fail(cnt, "TAUO_H2", name, p0)
            Tph = sum(st[x]["H1"] != st[x + 1]["H1"] for x in range(p0, p1))
            case = "A" if g.rank[o] > g.rank[c] else ("B" if g.rank[o] < g.rank[c] else "c=o")
            if NHN > 0: cnt["tauo_eq_o_phases_HN_case" + case] += 1
            if NHN > Tph // 2 + 1: fail(cnt, "NHN_TOG", name, p0, case)


def lib():
    files = [os.path.join(P.ROOT, l.split()[0]) for l in open(os.path.join(P.ROOT, "experiments/new/box37/lib37.txt")) if l.strip()]
    files = [f for f in files if "/out/" not in f and os.path.exists(f)]
    files += sorted(glob.glob(os.path.join(P.ROOT, "experiments/new/box37/instances/*.pg")))
    files += sorted(glob.glob(os.path.join(P.ROOT, "experiments/new/box38/instances/*.pg")))
    return files


def main(a):
    files = lib() if a == ["lib"] else a
    cnt = Counter()
    for f in files:
        g = RE.parse(f)
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        cnt["games"] += 1
        try: run(g, cnt, os.path.relpath(f, P.ROOT))
        except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-36s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
