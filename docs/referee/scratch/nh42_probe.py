#!/usr/bin/env python3
"""REFEREE succ. 10 probe for packet P-N5-NH-box42 (docs/new/P-N5-NH-box42.md, pin 54ac72e6, sha1 93d19be8...).
Own engine (rl_engine, rl_probe.states; no lane code). C^1O asserted per game. R := rl_probe's Rb (o included, the R22 convention).
Per phase: crossing-free intervals I (R constant), stretches S (R, theta, w constant), state types EQ / THR / OTHER, classes.
 ST    OTHER status constant on every stretch; (a)/(b) per clause pattern
 CL    OTHER route-form stretch has c_theta != c_w (class P3' / U1); others U2 / U3 / U23
 SW    a transition of a stretch with a Xi- or W-change on R has an Even R-vertex switching
 STR   Theta_I <= n-1; H2: WC_I <= n-1; not H2: WC_I <= (f^O_I+1)(|R|^2-1)+f^O_I; stretches of I <= 1+Theta_I+WC_I <= n-1+(f^O_I+1)n^2
 NR    per OTHER stretch, N_R(S) <= class bound and <= n^3(1+f_S)+2n(K_S+E_S)
 NH    (a), (b), (c) of Theorem NH with the computed X, f^O, K_W, E, O, T
Usage: nh42_probe.py lib | files...   (env START, RANDSTARTS as in needb_probe.py)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def run(g, cnt, name):
    o, st = P.states(g); n = g.n; T = len(st) - 1
    D = 4 * n * (n - 1) + 1
    phases, k = [], 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        phases.append((k, j)); k = j + 1
    for (p0, p1) in phases:
        cnt["phases"] += 1
        ct = st[p0]["Xi"][o][0]
        R = lambda t: st[t]["Rb"]
        typ = {}
        for t in range(p0, p1 + 1):
            a = st[t]
            eq = all(a["Xi"][v] == a["W"][v] for v in range(n))
            typ[t] = "EQ" if eq else ("THR" if a["h"] else "OTHER")
        trs = list(range(p0, p1))
        X = sum(R(t) != R(t + 1) for t in trs)
        O = sum(typ[t] == "OTHER" or typ[t + 1] == "OTHER" for t in trs)
        fO = sum(st[t]["fb"] and typ[t] == "OTHER" for t in trs)
        # intervals
        ivs, t = [], p0
        while t <= p1:
            u = t
            while u < p1 and R(u + 1) == R(t): u += 1
            ivs.append((t, u)); t = u + 1
        N = 0; KW = 0; E = 0; NRsum = 0; NFsum = 0; Ssum = 0
        for (i0, i1) in ivs:
            Rs = R(i0); F = set(range(n)) - Rs
            H1, H2 = st[i0]["H1"], st[i0]["H2"]
            if any(st[x]["H1"] != H1 or st[x]["H2"] != H2 for x in range(i0, i1 + 1)): fail(cnt, "TC_const", name, i0)
            th = sum(st[x]["Xi"][o] != st[x + 1]["Xi"][o] for x in range(i0, i1))
            wc = sum(st[x]["W"][o] != st[x + 1]["W"][o] for x in range(i0, i1))
            fOI = sum(st[x]["fb"] and typ[x] == "OTHER" for x in range(i0, i1))
            if th > n - 1: fail(cnt, "STR_a", name, i0, th)
            if H2 and wc > n - 1: fail(cnt, "STR_b_H2", name, i0, wc)
            r = len(Rs)
            if not H2 and wc > (fOI + 1) * (r * r - 1) + fOI: fail(cnt, "STR_b_notH2", name, i0, wc)
            nF = sum(any(st[x]["Xi"][v] != st[x + 1]["Xi"][v] for v in F) for x in range(i0, i1))
            if nF > max(0, len(F) - 1): fail(cnt, "F1deg", name, i0)
            N += 1 + th + wc
            # stretches
            sts, t = [], i0
            while t <= i1:
                u = t
                while u < i1 and st[u + 1]["Xi"][o] == st[t]["Xi"][o] and st[u + 1]["W"][o] == st[t]["W"][o]: u += 1
                sts.append((t, u)); t = u + 1
            Ssum += len(sts)
            if len(sts) > 1 + th + wc or len(sts) > n - 1 + (fOI + 1) * n * n: fail(cnt, "STR_c", name, i0)
            for (s0, s1) in sts:
                ty = {typ[x] == "OTHER" for x in range(s0, s1 + 1)}
                if len(ty) > 1: fail(cnt, "ST", name, s0)
                # SW (b) on every stretch
                for x in range(s0, s1):
                    chg = any(st[x]["Xi"][v] != st[x + 1]["Xi"][v] or st[x]["W"][v] != st[x + 1]["W"][v] for v in Rs)
                    if chg:
                        cnt["SW_chk"] += 1
                        if not any(g.owner[v] == 0 and st[x]["s"][v] != st[x + 1]["s"][v] for v in Rs): fail(cnt, "SW", name, x)
                if typ[s0] != "OTHER": continue
                cw = st[s0]["W"][o][0]
                hrf = H1 or ct == o; wrf = H2 or cw == o
                if hrf and wrf:
                    if ct == cw: fail(cnt, "CL", name, s0); continue
                    cls = "P3p" if g.rank[ct] > g.rank[cw] else "U1"
                elif wrf: cls = "U2"
                elif hrf: cls = "U3"
                else: cls = "U23"
                cnt["class_" + cls] += 1
                fS = sum(st[x]["fb"] for x in range(s0, s1))
                NR = sum(any(st[x]["Xi"][v] != st[x + 1]["Xi"][v] for v in Rs) for x in range(s0, s1))
                NF = sum(any(st[x]["Xi"][v] != st[x + 1]["Xi"][v] for v in F) for x in range(s0, s1))
                KS = ES = 0
                if cls in ("U2", "U3", "U23"):
                    KS = sum((not st[x]["fb"]) and any(st[x]["W"][v] != st[x + 1]["W"][v] for v in Rs) for x in range(s0, s1))
                if cls in ("U3", "U23"):
                    for x in range(s0, s1):
                        ev = False
                        for v in Rs - {o}:
                            if g.owner[v] == 0 and st[x]["s"][v] != st[x + 1]["s"][v]:
                                ka = cw in P.route(st[x]["nx"], v, o); kb = cw in P.route(st[x + 1]["nx"], v, o)
                                if ka != kb: ev = True
                        if g.owner[cw] == 0 and st[x]["s"][cw] != st[x + 1]["s"][cw]: ev = True
                        ES += ev
                r = len(Rs)
                if cls == "P3p": b = (n + 1) * r
                elif cls == "U1":
                    K = (fS + 1) * (r - 1) * (r - 2); b = r + fS + K + (K + fS + 1) * (r - 2)
                elif cls == "U2": b = fS + KS + (KS + fS + 1) * (r - 2)
                else: b = fS + KS + ES + (KS + fS + ES + 1) * (2 * r - 4)
                cnt["NR_chk"] += 1
                if NR > b: fail(cnt, "NR_class_" + cls, name, s0, NR, b)
                if NR > n ** 3 * (1 + fS) + 2 * n * (KS + ES): fail(cnt, "NR_crude", name, s0)
                L = s1 - s0
                if L > D * (NR + NF + 1): fail(cnt, "NH_stretch_len", name, s0, L)
                KW += KS; E += ES; NRsum += NR; NFsum += NF
                cnt["max_NR_" + cls] = max(cnt["max_NR_" + cls], NR)
        if N > n * n * (2 * X + 2 + fO): fail(cnt, "STR_d", name, p0)
        if O > X + N + D * (n * (X + 1) + (n ** 3 + 1) * N + n ** 3 * fO + 2 * n * (KW + E)): fail(cnt, "NH_a", name, p0)
        Q = 1 + X + fO
        if O > 11 * n ** 7 * Q + 8 * n ** 3 * (KW + E): fail(cnt, "NH_b", name, p0)
        Tp = p1 - p0
        if Tp > 156 * n ** 11 * Q + 104 * n ** 7 * (KW + E): fail(cnt, "NH_c", name, p0)
        if Tp > (3 * n * n * (1 + X + O) + X + O + 1) * D: fail(cnt, "THMX", name, p0)
        cnt["O_total"] += O; cnt["phases_O_pos"] += O > 0
        for key, val in (("O", O), ("X", X), ("T", Tp), ("fO", fO), ("KW", KW), ("E", E)):
            cnt["max_" + key] = max(cnt["max_" + key], val)


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
    for k in sorted(cnt): print("%-30s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
