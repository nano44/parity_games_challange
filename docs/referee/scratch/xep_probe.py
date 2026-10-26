#!/usr/bin/env python3
"""REFEREE succ. 12 probe for packet P-N5-XEP (docs/new/P-N5-XEP-box44.md, pin 8460897d, sha1 237dd5eb...). Own engine (rl_engine via
dual_probe.run5). Any game. W_k := the (sigma_k, tau_k) play valuation; D_k := {Odd u : sigma-bar_k(u) != tau_k(u)}; R_D(k) := vertices whose
(sigma_k, tau_k)-play meets D_k (v included); split: cycle node of W_k(v) != lambda(v). Per phase ((lambda_Xi, tau) constant):
 GDA     premise R55 G_D (a): v not in R_D(k) => Xi_k(v) = W_k(v)
 WM      premise R23 (g): W_{k+1}(v) >= W_k(v) at every in-phase non-fallback transition
 SPLITR  (sharpening) split at k => v in R_D(k)
 RSTICK  R-STICK_D: at an in-phase S4a transition s -> s+1, every split v at s lies in R_D(s+1)
 SNPA    SN-PREFIX_D (a): inside each maximal run of in-phase S4a transitions, v's unsplit states form a prefix
 SNC     SN-PREFIX_D (c): X_D <= (f+1) n + f + X_SN^D
 DEP     Fact D-EPOCH: D constant on each epoch (sigma-bar|Q constant)
 XEP     Lemma X-EP: X_D <= (N_ep - 1) + N_ep (n^2 + n + 4n(n-1)) + sum_E X_SN^pre(E)
Counts: crossings at epoch boundaries / inside after e_{n-1} / inside before with an unsplit changer (X_SN^pre) / inside before with all
changers split (X_ALLSPLIT; at S4a transitions predicted 0 by G_D (a) + R-STICK_D: ALLSPLIT_S4A counts violations of that prediction).
Usage: xep_probe.py lib | rand N nmin nmax kmax seed | files...   (env RANDSTARTS=N, MAXN=64)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP, dual_probe as D
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def run_check(g, start, cnt, name):
    A = D.run5(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    st = []
    for a in A:
        Xi, sb = RE.evaluate(g, a["s"])
        nxw = [a["s"][v] if g.owner[v] == 0 else a["t"][v] for v in range(n)]
        W = [RE.play_value(g, nxw, v) for v in range(n)]
        Dk = {u for u in range(n) if g.owner[u] == 1 and sb[u] != a["t"][u]}
        RD = set()
        for v in range(n):
            x, seen = v, set()
            while x not in seen:
                if x in Dk: RD.add(v); break
                seen.add(x); x = nxw[x]
        st.append(dict(Xi=Xi, sb=sb, W=W, D=Dk, RD=RD, split={v for v in range(n) if W[v][0] != Xi[v][0]}))
    T_ = len(A) - 1
    key = [(tuple(x[0] for x in st[k]["Xi"]), tuple(A[k]["t"])) for k in range(T_ + 1)]
    for k in range(T_ + 1):
        s = st[k]
        for v in range(n):
            if v not in s["RD"] and s["Xi"][v] != s["W"][v]: fail(cnt, "GDA", name, k, v)
        cnt["GDA_chk"] += n
        for v in s["split"]:
            cnt["SPLITR_chk"] += 1
            if v not in s["RD"]: fail(cnt, "SPLITR", name, k, v)
    k = 0
    while k <= T_:
        j = k
        while j < T_ and key[j] == key[j + 1]: j += 1
        p0, p1 = k, j; k = j + 1
        cnt["phases"] += 1
        fbs = [x for x in range(p0, p1) if A[x]["fb"]]; f = len(fbs)
        # WM, RSTICK
        for s in range(p0, p1):
            if A[s]["fb"]: continue
            for v in range(n):
                cnt["WM_chk"] += 1
                if g.key(st[s + 1]["W"][v]) < g.key(st[s]["W"][v]): fail(cnt, "WM", name, s, v)
            for v in st[s]["split"]:
                cnt["RSTICK_chk"] += 1
                if v not in st[s + 1]["RD"]: fail(cnt, "RSTICK", name, s, v)
        # SNPA: maximal runs of S4a transitions -> states of each run
        runs, cur = [], [p0]
        for s in range(p0, p1):
            if A[s]["fb"]: runs.append(cur); cur = [s + 1]
            else: cur.append(s + 1)
        runs.append(cur)
        for R in runs:
            for v in range(n):
                seen_split = False
                for s in R:
                    if v in st[s]["split"]: seen_split = True
                    elif seen_split: fail(cnt, "SNPA", name, s, v); break
            cnt["SNPA_chk"] += 1
        # crossings
        cross = [s for s in range(p0, p1) if st[s]["RD"] != st[s + 1]["RD"]]
        XD = len(cross); cnt["max_XD"] = max(cnt["max_XD"], XD); cnt["crossings"] += XD
        def unsplit_changer(s):
            ch = st[s]["RD"] ^ st[s + 1]["RD"]
            return any(v not in st[s]["split"] for v in ch)
        XSN = sum(1 for s in cross if unsplit_changer(s))
        cnt["SNC_chk"] += 1
        if XD > (f + 1) * n + f + XSN: fail(cnt, "SNC", name, p0, XD, f, XSN)
        # epochs
        ep, cur = [], [p0]
        for s in range(p0 + 1, p1 + 1):
            if any(st[s]["sb"][q] != st[s - 1]["sb"][q] for q in Q): ep.append(cur); cur = [s]
            else: cur.append(s)
        ep.append(cur)
        Nep = len(ep); cnt["max_epochs"] = max(cnt["max_epochs"], Nep)
        epid = {}
        for i, E in enumerate(ep):
            for s in E: epid[s] = i
            if len({frozenset(st[s]["D"]) for s in E}) != 1: fail(cnt, "DEP", name, E[0])
            cnt["DEP_chk"] += 1
        pre_sum = 0
        for E in ep:
            es = [x for x in fbs if x in E]
            lim = es[n - 2] if (n >= 2 and len(es) >= n - 1) else None
            for s in cross:
                if s in E and s + 1 in E:
                    if lim is not None and s > lim: cnt["X_after_freeze"] += 1
                    elif unsplit_changer(s): cnt["X_SN_pre"] += 1; pre_sum += 1
                    else:
                        cnt["X_ALLSPLIT"] += 1
                        if not A[s]["fb"]: fail(cnt, "ALLSPLIT_S4A", name, s)
        cnt["X_boundary"] += sum(1 for s in cross if epid[s] != epid[s + 1])
        cnt["XEP_chk"] += 1
        if XD > (Nep - 1) + Nep * (n * n + n + 4 * n * (n - 1)) + pre_sum: fail(cnt, "XEP", name, p0, XD, Nep, pre_sum)


def main(a):
    nr = int(os.environ.get("RANDSTARTS", "0")); cnt = Counter(); maxn = int(os.environ.get("MAXN", "64"))
    if a and a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); rng = random.Random(seed)
        gs = [("rand%d_%d" % (seed, i), D.rand_ck(rng, rng.randint(lo, hi), rng.randint(0, km))) for i in range(N)]
    else:
        gs = [(os.path.relpath(f, P.ROOT), RE.parse(f)) for f in (RP.lib() if a == ["lib"] else a)]
    for name, g in gs:
        if g.n > maxn: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        for i, stt in enumerate([RE.best_reward_start(g)] + [D.rand_start(g, random.Random(name + str(i))) for i in range(nr)]):
            try: run_check(g, stt, cnt, name + ("@r%d" % i if i else ""))
            except RuntimeError: cnt["maxit"] += 1
    for k in sorted(cnt): print("%-26s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX (", e)


if __name__ == "__main__":
    main(sys.argv[1:])
