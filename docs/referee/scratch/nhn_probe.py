#!/usr/bin/env python3
"""REFEREE succ. 10 probe for packet P-N5-NHN (docs/new/P-N5-NHN-box40.md, pin 0bb175d, sha1 da7d09ec...).
Own engine (rl_engine, rl_probe.states; no lane code). C^1O asserted per game. t0 = tau(o); EV2 end = in-phase k -> k+1 with HN at k
and H1 and H2 at k+1; DROP = in-phase H1 -> not H1. Checks (every *_FAIL must be 0):
 T0U    (a) every state of every phase with t0 != o: not H2 <=> t0 in R; (b) phases with an HN state: t0 in U \\ {o, c} at every state
 EV2    every EV2 end is an Even S4c fallback with t0 in R_k \\ R_k+1
 SG     every in-phase transition with H1 at k, t0 in R_k, t0 not in R_k+1: Xi_k(t0) < Xi_k+1(t0) (strict, Even order)
 PIN    EV2 ends that are g_j with j >= |U| - 1: M_k(t0) = M_k+1(t0) = MoptUh(t0) (exact DFS, |U| <= UMAX)
 NHN    N_HN <= 1 + #DROPs + #EV2; #EV2 <= 2 max(|U| - 2, 0); N_HN <= ceil(T/2) + 2|U| - 3, T = |U|(n+1) + n - 1 (t0 != o);
        tau(o) = o: no EV2 end and N_HN <= ceil(T/2) + 1 (also the per-phase toggle count)
 H3     phases with t0 != o and an HN state: every H2 state has H3; Q states (H1, H2, not H3) only in phases without an HN state
Usage: nhn_probe.py lib | files..."""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP
EX = []
UMAX = int(os.environ.get("UMAX", "14"))


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
        c = st[p0]["Xi"][o][0]; t0 = st[p0]["t"][o]
        U = [v for v in range(n) if st[p0]["Xi"][v][0] == c]; Us = set(U)
        wt = {v: (sgn(v) << g.rank[v]) if g.rank[v] > g.rank[c] else 0 for v in U}

        def M(t, z):
            m, s, r = st[t]["Xi"][z][1], 0, 0
            while m:
                if m & 1: s += (1 << r) if g.prio[g.byrank[r]] % 2 == 0 else -(1 << r)
                m >>= 1; r += 1
            return s
        HN = {t: st[t]["H1"] and not st[t]["H2"] for t in range(p0, p1 + 1)}
        hasHN = any(HN.values())
        Q = [t for t in range(p0, p1 + 1) if st[t]["H1"] and st[t]["H2"] and not st[t]["H3"]]
        if Q:
            cnt["phases_with_Q"] += 1
            if hasHN: fail(cnt, "Q_in_HN_phase", name, p0)
        fbs = [t for t in range(p0, p1) if st[t]["fb"]]
        Tn = len(U) * (n + 1) + n - 1
        R = lambda t: st[t]["Rb"] - {o}
        drops = [t for t in range(p0, p1) if st[t]["H1"] and not st[t + 1]["H1"]]
        ev2 = [t for t in range(p0, p1) if HN[t] and st[t + 1]["H1"] and st[t + 1]["H2"]]
        NHN = sum(1 for t in range(p0, p1 + 1) if HN[t] and (t == p0 or not HN[t - 1]))
        if NHN > 1 + len(drops) + len(ev2): fail(cnt, "NHN_split", name, p0)
        drops_end = sum(1 for t in drops if HN[t])
        cnt["NHN_drops_ending_stretch"] += drops_end
        if t0 == o:
            if hasHN: cnt["tauo_phases_HN"] += 1
            if ev2: fail(cnt, "EV2_tauo", name, p0)
            if NHN > -(-Tn // 2) + 1: fail(cnt, "NHN_tauo", name, p0)
            continue
        cnt["t0ne_phases"] += 1
        for t in range(p0, p1 + 1):
            cnt["T0U_a_chk"] += 1
            if (not st[t]["H2"]) != (t0 in R(t)): fail(cnt, "T0U_a", name, t)
        # SG-EV
        for t in range(p0, p1):
            if st[t]["H1"] and t0 in R(t) and t0 not in R(t + 1):
                cnt["SG_chk"] += 1
                if not g.key(st[t]["Xi"][t0]) < g.key(st[t + 1]["Xi"][t0]): fail(cnt, "SG", name, t)
        if not hasHN: continue
        cnt["t0ne_phases_HN"] += 1
        for t in range(p0, p1 + 1):
            cnt["T0U_b_chk"] += 1
            if not (t0 in Us and t0 != c and t0 != o): fail(cnt, "T0U_b", name, t)
        for t in range(p0, p1 + 1):
            if st[t]["H2"]:
                cnt["H3_chk"] += 1
                if not st[t]["H3"]: fail(cnt, "H3", name, t)
        cnt["EV2_ends"] += len(ev2)
        mopt = None
        if len(U) <= UMAX:
            UhS = set(v for v in U if v != o)
            res = [None]

            def dfs(v, seen, acc):
                if v == c:
                    if res[0] is None or acc > res[0]: res[0] = acc
                    return
                nxs = g.succ[v] if g.owner[v] == 0 else ([g.succ[v][0]] if len(g.succ[v]) == 1 else [])
                for x in nxs:
                    if x in UhS and x not in seen: seen.add(x); dfs(x, seen, acc + wt[v]); seen.discard(x)
            dfs(t0, {t0}, 0); mopt = res[0]
        for k in ev2:
            if not (st[k]["fb"] and st[k]["Is"] and t0 in R(k) and t0 not in R(k + 1)): fail(cnt, "EV2", name, k)
            j = fbs.index(k) + 1 if k in fbs else None
            if j is not None and j >= len(U) - 1:
                cnt["PIN_ends"] += 1
                if not (M(k, t0) == M(k + 1, t0) and (mopt is None or M(k, t0) == mopt)): fail(cnt, "PIN", name, k)
                if mopt is None: cnt["PIN_bigU_unchecked_mopt"] += 1
        if len(ev2) > 2 * max(len(U) - 2, 0): fail(cnt, "NHN_a", name, p0, len(ev2))
        if NHN > -(-Tn // 2) + 2 * len(U) - 3: fail(cnt, "NHN_b", name, p0)
        cnt["NHN_total"] += NHN; cnt["NHN_max"] = max(cnt["NHN_max"], NHN)
        cnt["EV2_max_per_phase"] = max(cnt["EV2_max_per_phase"], len(ev2))


def main(a):
    files = RP.lib() if a == ["lib"] else a
    cnt = Counter()
    for f in files:
        g = RE.parse(f)
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        cnt["games"] += 1
        try: run(g, cnt, os.path.relpath(f, P.ROOT))
        except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-34s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
