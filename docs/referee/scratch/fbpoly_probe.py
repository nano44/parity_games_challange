#!/usr/bin/env python3
"""REFEREE succ. 10 probe for packet P-N5-FBPOLY (docs/new/P-N5-FBPOLY-box41.md, pin 42d8c3a9, sha1 de244dcd...).
Own engine (rl_engine, rl_probe.states; no lane code). C^1O asserted per game. Phase = (lambda_Xi, tau)-run; U = lambda^-1(c);
T = {o, c}; kappa_t(z) = (M_t(z), s_theta * len(Xi_t z)); kwt(v) = (wt(v), s_theta). At every in-phase Even S4c fallback k = g_j = f^Theta_i:
 SW     S_k (vertices whose sigma changes) = gate sources; S_U := S_k cap (U \\ T)
 CN     S_U empty: every gate (y, z) has lambda(y) = y and lev = -1, and k+1 is the phase's last state
 EX     S_U nonempty: kind of each u in S_U (first of {u} cup T on the honest k-play from x*_u: loop / ct / o); some u not loop;
        kappa_k(x*_u) = kwt(p_u minus {u, e}) + kappa_k(e)
 FE     (proof's per-vertex form) kind ct only if j <= |U| - 2; kind o only if i <= |U| - 2  (o != c); o = c: kind o only if i <= |U| - 1
 TA     THETA-AFTER: theta-changes after g_{|U|-2} <= deg_U(o) + |U| - 2 (o != c, >= |U| - 2 fallbacks)
 FB     FB-POLY (a) f <= 1 + (|U|-2)(deg_U(o)+|U|), (b) |U| = 2: f <= 1, (c) o = c: f <= |U|, (d) <= 1 fallback with S_U empty
 KH     kappa-HAT-FREEZE (a), (c) exact (|U| <= UMAX); KP kappa-PFZ exact (|U| <= UMAX)
Also: FBCAP excess f - max(1, |U| - 2) (conjecture, counted) and the regime counter POSTFZ (a fallback g_j with j >= |U| - 1, |U| >= 3).
Usage: fbpoly_probe.py lib | files...   (env START, RANDSTARTS as in needb_probe.py)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP
EX = []
UMAX = int(os.environ.get("UMAX", "12"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def run(g, cnt, name):
    o, st = P.states(g); n = g.n; T = len(st) - 1
    sgn = lambda v: 1 if g.prio[v] % 2 == 0 else -1
    phases, k = [], 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        phases.append((k, j)); k = j + 1
    for (p0, p1) in phases:
        cnt["phases"] += 1
        c = st[p0]["Xi"][o][0]
        U = [v for v in range(n) if st[p0]["Xi"][v][0] == c]; Us = set(U); Tm = {o, c}
        sth = 1 if g.prio[c] % 2 == 1 else -1
        wt = {v: (sgn(v) << g.rank[v]) if g.rank[v] > g.rank[c] else 0 for v in U}
        kwt = lambda v: (wt[v], sth)

        def kap(t, z):
            m, s, r = st[t]["Xi"][z][1], 0, 0
            while m:
                if m & 1: s += (1 << r) if g.prio[g.byrank[r]] % 2 == 0 else -(1 << r)
                m >>= 1; r += 1
            return (s, sth * st[t]["Xi"][z][2])
        add = lambda a, b: (a[0] + b[0], a[1] + b[1])
        fbs = [t for t in range(p0, p1) if st[t]["fb"]]
        f = len(fbs); u_ = len(U); degU = len([y for y in g.succ[o] if y in Us])
        # theta-runs
        trun = {}; rid = 0
        for t in range(p0, p1 + 1):
            if t > p0 and st[t]["Xi"][o] != st[t - 1]["Xi"][o]: rid += 1
            trun[t] = rid
        cnt_in_run = Counter(); nSUempty = 0
        if u_ >= 3 and f >= u_ - 1 and o != c: cnt["POSTFZ_phases"] += 1
        cnt["FBCAP_excess_max_U3plus" if u_ >= 3 else "FBCAP_excess_max_U12"] = max(
            cnt["FBCAP_excess_max_U3plus" if u_ >= 3 else "FBCAP_excess_max_U12"], f - max(1, u_ - 2) + 100) if f else cnt[
            "FBCAP_excess_max_U3plus" if u_ >= 3 else "FBCAP_excess_max_U12"]
        for jj, k in enumerate(fbs, start=1):
            cnt_in_run[trun[k]] += 1; ii = cnt_in_run[trun[k]]
            a, b = st[k], st[k + 1]
            cnt["fallbacks"] += 1
            if not a["Is"]: fail(cnt, "NOT_EVEN_FB", name, k); continue
            Sk = {v for v in range(n) if g.owner[v] == 0 and a["s"][v] != b["s"][v]}
            if Sk != {y for (y, z) in a["Is"]}: fail(cnt, "SW", name, k)
            SU = Sk & (Us - Tm)
            if not SU:
                nSUempty += 1; cnt["CN_cases"] += 1
                okg = all(a["Xi"][y][0] == y and P.lev(a["Xi"][a["s"][y]], a["Xi"][z]) == -1 for (y, z) in a["Is"])
                if not okg or k + 1 != p1: fail(cnt, "CN", name, k, okg, k + 1 == p1)
                continue
            cnt["SU_nonempty"] += 1
            kinds = {}
            for u in SU:
                x = b["s"][u]; seen = 0; v = x; path = []
                while True:
                    if v == u: kinds[u] = ("loop", None); break
                    if v in Tm: kinds[u] = ("ct" if v == c else "o", v); break
                    path.append(v); v = a["hg"][v]; seen += 1
                    if seen > 2 * n: kinds[u] = ("stuck", None); break
                kd, e = kinds[u]
                cnt["EX_kind_" + kd] += 1
                if kd in ("ct", "o"):
                    s_ = (0, 0)
                    for v in path: s_ = add(s_, kwt(v))
                    if kap(k, x) != add(s_, kap(k, e)): fail(cnt, "EX_kappa", name, k, u)
                    if o != c:
                        if kd == "ct" and jj > u_ - 2: fail(cnt, "FE_ct", name, k, u)
                        if kd == "o" and ii > u_ - 2: fail(cnt, "FE_o", name, k, u)
                    else:
                        if ii > u_ - 1: fail(cnt, "FE_c_eq_o", name, k, u)
                    if (o != c and ((kd == "ct" and jj >= u_ - 1) or (kd == "o" and ii >= u_ - 1))): cnt["FE_regime_hit"] += 1
            if all(kd == "loop" for kd, _ in kinds.values()): fail(cnt, "EX", name, k)
            if any(kd == "stuck" for kd, _ in kinds.values()): fail(cnt, "EX_stuck", name, k)
        if nSUempty > 1: fail(cnt, "FB_d", name, p0)
        if o != c and f > 1 + (u_ - 2) * (degU + u_): fail(cnt, "FB_a", name, p0, f)
        if u_ == 2 and f > 1: fail(cnt, "FB_b", name, p0, f)
        if o == c and f > u_: fail(cnt, "FB_c", name, p0, f)
        if o == c and u_ == 2: cnt["phases_c_eq_o_U2"] += 1
        cnt["f_max"] = max(cnt["f_max"], f)
        # THETA-AFTER
        if o != c and f >= u_ - 2 and u_ >= 2:
            fz = fbs[u_ - 3] if u_ >= 3 else p0 - 1
            ch = sum(st[t]["Xi"][o] != st[t + 1]["Xi"][o] for t in range(fz + 1, p1))
            cnt["TA_phases"] += 1
            if u_ >= 3: cnt["TA_phases_U3plus"] += 1
            cnt["TA_changes_max"] = max(cnt["TA_changes_max"], ch)
            if ch > degU + u_ - 2: fail(cnt, "TA", name, p0, ch)
        # exact kappa checks
        if 3 <= u_ <= UMAX:
            Uh = set(U) - {o}

            def best(z, j, allowed, sink):
                res = [None]

                def dfs(v, seen, acc, d):
                    if v == sink:
                        if res[0] is None or acc > res[0]: res[0] = acc
                        return
                    if d == j: return
                    nxs = g.succ[v] if g.owner[v] == 0 else ([g.succ[v][0]] if len(g.succ[v]) == 1 else [])
                    for x in nxs:
                        if x in allowed and x not in seen: seen.add(x); dfs(x, seen, add(acc, kwt(v)), d + 1); seen.discard(x)
                if z in allowed: dfs(z, {z}, (0, 0), 0)
                return res[0]
            for jj in range(1, min(f, u_ - 2) + 1):
                bj = {z: best(z, jj, Uh, c) for z in Uh}
                for t in range(fbs[jj - 1] + 1, p1 + 1):
                    for z in Uh:
                        if bj[z] is None: continue
                        cnt["KH_chk"] += 1
                        if kap(t, z) < bj[z]: fail(cnt, "KH", name, jj, t, z)
            if f >= u_ - 2:
                kopt = {z: best(z, u_, Uh, c) for z in Uh}
                fz = fbs[u_ - 3]
                for t in range(fz + 1, p1 + 1):
                    for z in Uh:
                        if z in st[t]["F"]:
                            cnt["KHC_chk"] += 1
                            if kap(t, z) != kopt[z]: fail(cnt, "KHC", name, t, z)
            if o != c:
                Uo = set(U) - {c}
                for r_ in set(trun.values()):
                    ts = [t for t in range(p0, p1 + 1) if trun[t] == r_]
                    fr = [t for t in fbs if trun[t] == r_]
                    for jj in range(1, min(len(fr), u_ - 2) + 1):
                        bj = {z: best(z, jj, Uo, o) for z in Uo if z != o}
                        for t in ts:
                            if t <= fr[jj - 1]: continue
                            for z, bz in bj.items():
                                if bz is None: continue
                                cnt["KP_chk"] += 1
                                if kap(t, z) < add(bz, kap(t, o)): fail(cnt, "KP", name, r_, t, z)


def main(a):
    if os.environ.get("START"):
        sp, tp = os.environ["START"].split(";")
        s0 = [int(x) for x in sp.split(",")]; t0 = [int(x) for x in tp.split(",")]
        RE.best_reward_start = lambda g: ([s0[v] if g.owner[v] == 0 else None for v in range(g.n)],
                                          [t0[v] if g.owner[v] == 1 else None for v in range(g.n)])
    files = RP.lib() if a == ["lib"] else a
    cnt = Counter()
    for f in files:
        g = RE.parse(f)
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        cnt["games"] += 1
        try: run(g, cnt, os.path.relpath(f, P.ROOT))
        except RuntimeError: cnt["maxit"] += 1
        nr = int(os.environ.get("RANDSTARTS", "0"))
        if nr:
            rng = random.Random(f); orig = RE.best_reward_start
            for _ in range(nr):
                s0 = [rng.choice(g.succ[v]) if g.owner[v] == 0 else None for v in range(g.n)]
                t0 = [rng.choice(g.succ[v]) if g.owner[v] == 1 else None for v in range(g.n)]
                RE.best_reward_start = lambda h, s0=s0, t0=t0: (s0, t0)
                cnt["runs_randstart"] += 1
                try: run(g, cnt, os.path.relpath(f, P.ROOT) + "@rand")
                except RuntimeError: cnt["maxit"] += 1
            RE.best_reward_start = orig
    for k in sorted(cnt):
        v = cnt[k] - 100 if k.startswith("FBCAP_excess") else cnt[k]
        print("%-30s %d" % (k, v))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
