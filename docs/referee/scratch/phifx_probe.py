#!/usr/bin/env python3
"""REFEREE succ. 10 probe for packets P-N5-PHI (docs/si/P-N5-PHI-box14.md, sha1 35e79ec1...) and P-N5-FX (docs/si/P-N5-FX-box14.md,
sha1 aa227b0b...), both pinned at trunk 02ad3f88. Own engine (rl_engine; no lane code).
 PHI (every game): reward(lambda_k(v)) non-decreasing, reward(lambda^U_k(v)) non-increasing (G's reward, U = Odd's dual valuation of tau_k);
     equality of reward <=> equal cycle node; transitions changing lambda <= n(n-1), lambda^U <= n(n-1); joint lambda-runs <= 2n(n-1)+1
 PHI1O (C^1O): tau changes <= d - 1; phases ((lambda, tau)-runs) <= n(n-1) + d
 FX (C^1O): per phase X <= n(f + X_SN) + n - 1 and the sharper landed SN-PREFIX bound X <= (f+1)(n-1) + f + X_SN (R30 (c));
     (b): X <= n(F* + 13(d+1)n^3(F*+1+T) + T) + n - 1, F* = 1 + (n-2)(2n-1), T = n^2 + 2n - 1
Usage: phifx_probe.py lib | files... | rand N seed (random general games n 3-10 and random C^1O games n 4-14)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P, rho_probe as RP
EX = []


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def run(g, cnt, name):
    n = g.n
    rs = RE.run(g)
    T = len(rs) - 1
    lam = [[a["Xi"][v][0] for v in range(n)] for a in rs]
    lamU = [[a["Ut"][v][0] for v in range(n)] for a in rs]
    chl = chu = 0; runs = 1
    for k in range(T):
        for v in range(n):
            a, b = g.rew[lam[k][v]], g.rew[lam[k + 1][v]]
            cnt["PHI_a_chk"] += 1
            if b < a or ((a == b) != (lam[k][v] == lam[k + 1][v])): fail(cnt, "PHI_a", name, k, v)
            a, b = g.rew[lamU[k][v]], g.rew[lamU[k + 1][v]]
            cnt["PHI_b_chk"] += 1
            if b > a or ((a == b) != (lamU[k][v] == lamU[k + 1][v])): fail(cnt, "PHI_b", name, k, v)
        chl += lam[k] != lam[k + 1]; chu += lamU[k] != lamU[k + 1]
        runs += (lam[k] != lam[k + 1]) or (lamU[k] != lamU[k + 1])
    if chl > n * (n - 1) or chu > n * (n - 1) or runs > 2 * n * (n - 1) + 1: fail(cnt, "PHI_c", name, chl, chu, runs)
    cnt["PHI_lamU_changes"] += chu; cnt["PHI_lam_changes"] += chl
    cnt["PHI_c_max_ratio_x1000"] = max(cnt["PHI_c_max_ratio_x1000"], (1000 * runs) // (2 * n * (n - 1) + 1))
    try: o = P.assert_c1o(g)
    except AssertionError: return
    cnt["c1o_runs"] += 1
    o, st = P.states(g)
    d = len(g.succ[o])
    tch = sum(st[k]["t"][o] != st[k + 1]["t"][o] for k in range(T))
    if tch > d - 1: fail(cnt, "PHI1O_a", name, tch, d)
    phases, k = [], 0
    while k <= T:
        j = k
        while j < T and st[j]["key"] == st[j + 1]["key"]: j += 1
        phases.append((k, j)); k = j + 1
    if len(phases) > n * (n - 1) + d: fail(cnt, "PHI1O_b", name, len(phases))
    cnt["PHI1O_max_phases"] = max(cnt["PHI1O_max_phases"], len(phases))
    Fs = 1 + (n - 2) * (2 * n - 1); Tc = n * n + 2 * n - 1
    for (p0, p1) in phases:
        cnt["FX_phases"] += 1
        c = st[p0]["Xi"][o][0]
        R = lambda t: st[t]["Rb"] - {o}
        X = f = XSN = 0
        for t in range(p0, p1):
            cr = R(t) != R(t + 1)
            if st[t]["fb"]: f += 1
            if cr:
                X += 1
                if not st[t]["fb"] and st[t]["W"][o][0] == c: XSN += 1
                if not st[t]["fb"] and st[t]["W"][o][0] != c and not R(t) < R(t + 1): fail(cnt, "FX_RSTICK", name, t)
        if X > n * (f + XSN) + n - 1: fail(cnt, "FX_a", name, p0)
        if X > (f + 1) * (n - 1) + f + XSN: fail(cnt, "FX_SNPREFIX", name, p0)
        if X > n * (Fs + 13 * (d + 1) * n ** 3 * (Fs + 1 + Tc) + Tc) + n - 1: fail(cnt, "FX_b", name, p0)
        cnt["FX_X_total"] += X; cnt["FX_X_max"] = max(cnt["FX_X_max"], X); cnt["FX_XSN_total"] += XSN


def rand(N, seed):
    rng = random.Random(int(seed)); cnt = Counter()
    for i in range(int(N)):
        if i % 2 == 0:
            n = rng.randint(3, 10)
            owner = [rng.randint(0, 1) for _ in range(n)]
            succ = [rng.sample(range(n), rng.randint(1, min(3, n))) for _ in range(n)]
        else:
            n = rng.randint(4, 14)
            owner = [rng.randint(0, 1) for _ in range(n)]
            o = rng.randrange(n); owner[o] = 1
            succ = [rng.sample(range(n), rng.randint(1, min(3, n))) if owner[v] == 0 else [rng.randrange(n)] for v in range(n)]
            succ[o] = rng.sample(range(n), rng.randint(2, min(4, n)))
        prio = list(range(n)); rng.shuffle(prio)
        g = RE.Game(prio, owner, succ)
        cnt["games"] += 1
        try: run(g, cnt, "rand%d" % i)
        except RuntimeError: cnt["maxit"] += 1
    out(cnt)


def out(cnt):
    for k in sorted(cnt): print("%-30s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:40]: print("EX", e)


def main(a):
    if a and a[0] == "rand": return rand(a[1], a[2])
    files = RP.lib() if a == ["lib"] else a
    cnt = Counter()
    for f in files:
        g = RE.parse(f)
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1
        try: run(g, cnt, os.path.relpath(f, P.ROOT))
        except (RuntimeError, AssertionError) as e: cnt["err_" + type(e).__name__] += 1
    out(cnt)


if __name__ == "__main__":
    main(sys.argv[1:])
