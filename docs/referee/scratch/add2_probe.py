#!/usr/bin/env python3
"""REFEREE succ. 16 probe for P-N5-OFFMONO-add2-box49 (sha1 f2d123ef, l-new 6ef3dd25, trunk pin d5ad0929). Own engine (rl_engine;
offmono_probe's kap / par; zch_probe's Zc). Per phase P and class c (U = U_c, Qc = Q n U - {c}), states a..b:
 AF     Fact (A-F): z in U - {c}: P(Xi_t z) = {} <=> kappa_t(z) in F = {(0, s_c l) : 1 <= l <= n - 1}
 FT     Lemma FT-COUNT: |FT_c| <= 2(n - 1)(|U| - 1); per-z F-touching changes <= 2(n - 1) (and the finer count <= n, FTZ_MAX)
 FTC    Remark FT-CONST at every transition NOT in FT_c: A_t = A_{t+1}; kappa unchanged on A_t u {c}; off(x; par_{t+1} x) unchanged, x in Z_t(c) - {c}
 SA2    CHAIN-COUNT'' Step A'' at every transition not in ZC''_c = CYC n ZCH n FT, every x in Qc, p := par_{t+1}(x): off_{t+1} >= off_t
 ZC2F   (count) at transitions IN ZC''_c, x in Qc on Z_t(c): does off(x; p) fall (would the cut be needed)?
 CC2    CHAIN-COUNT'' sum form and D form (D := max v_x over x-pieces'') on J := the phase; |ZC''| <= min(|ZC|, |FT|) <= 2(n - 1)(|U| - 1)
 PF     Lemma PF-CHOICE at every state, every Odd x in A_t: sigmabar_t(x) = argmin over y in succ(x) n (A_t u {c}) of (kappa_t(y), tb_t(y)),
        tb = (y) if c even, the index sequence of y's honest play from c's side if c odd. sigmabar from my engine AND from si.py's
        Engine.evaluate (the code under review, sha1 e688b963, loaded from experiments/si/si.py; it is the OBJECT here, not a checker); also
        SIAGREE = my engine's (Xi, sigmabar) equals si.py's at every state
 TC     Corollary TIE-CHARGE: at every transition not in FT_c, next unchanged on A_t; every STRICT / TIE transition (add1 §3) is in FT_c;
        STRICT_c + TIE_c <= 2(n - 1)(|U| - 1)
Mutations: MUT=1 PF with reversed index tie-break; MUT=2 FTC checked at FT_c transitions too (must bite: the hypothesis is needed);
 MUT=3 CC2 pieces not cut at ZC'' (the lane's no-cut control).
Usage: add2_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 40, NOS3, SI=1 to run si.py's evaluate)"""
import sys, os, random, importlib.util
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rl_engine as RE, dual_probe as D
import offmono_probe as OM
from zch_probe import Zc
from flip_probe import nxt, on_cycle
from gcx_probe import load_start
EX = []
MUT = int(os.environ.get("MUT", "0"))
OM.MUT = 0  # offmono_probe / zch_probe read the same env variable; keep their kappa unmutated
SI = None
if os.environ.get("SI"):
    root = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
    sys.path.insert(0, os.path.join(root, "experiments", "harness"))
    spec = importlib.util.spec_from_file_location("si_object", os.path.join(root, "experiments", "si", "si.py"))
    SI = importlib.util.module_from_spec(spec); spec.loader.exec_module(SI)


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    eng = SI.Engine(g) if SI else None
    for x in st:
        x["nx"] = nxt(g, x["s"], x["sb"])
        if eng:
            strat = tuple(x["s"][v] if g.owner[v] == 0 else -1 for v in range(n))
            val, tf = eng.evaluate(strat)
            cnt["SIAGREE_chk"] += 1
            if [tuple(vv) for vv in val] != [tuple(vv) for vv in x["Xi"]] or any(tf[v] != x["sb"][v] for v in range(n) if g.owner[v] == 1):
                fail(cnt, "SIAGREE", name, len(cnt))
            x["sbsi"] = tf
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        if j > k: phase(g, st, k, j, lam, Q, cnt, name)
        k = j + 1


def tb(st, t, c, y):
    """indices of y's honest play from c's side (y last); empty for y = c"""
    seq = []; x = y; seen = set()
    while x != c and x not in seen:
        seen.add(x); seq.append(x); x = st[t]["nx"][x]
    return tuple(reversed(seq))


def phase(g, st, a, b, lam, Q, cnt, name):
    n = g.n
    for c in sorted(set(lam)):
        U = {v for v in range(n) if lam[v] == c}
        if len(U) < 2: continue
        Qc = sorted((Q & U) - {c})
        sc = 1 if g.prio[c] % 2 else -1
        Kp = lambda t, z: OM.kap(g, c, st[t]["Xi"][z])
        F = {(0, sc * l) for l in range(1, n)}
        A = {t: {z for z in U if z != c and st[t]["Xi"][z][1] == 0} for t in range(a, b + 1)}
        for t in range(a, b + 1):
            for z in U - {c}:
                cnt["AF_chk"] += 1
                if (z in A[t]) != (Kp(t, z) in F): fail(cnt, "AF", name, t, c, z)
        Z = {t: Zc(st[t]["nx"], c) for t in range(a, b + 1)}
        par = lambda t, x: OM.par(st[t]["nx"], Q, x, c)
        # FT-COUNT
        FT = set(); per = Counter()
        for t in range(a, b):
            for z in U - {c}:
                k0, k1 = Kp(t, z), Kp(t + 1, z)
                if k0 != k1 and (k0 in F or k1 in F): FT.add(t); per[z] += 1
        cnt["FT_chk"] += 1; cnt["SUM_FT"] += len(FT); cnt["MAX_FT"] = max(cnt["MAX_FT"], len(FT))
        if per: cnt["FTZ_MAX"] = max(cnt["FTZ_MAX"], max(per.values()))
        if len(FT) > 2 * (n - 1) * (len(U) - 1): fail(cnt, "FT", name, a, c, len(FT))
        if any(v > 2 * (n - 1) for v in per.values()): fail(cnt, "FTz", name, a, c)
        if any(v > n for v in per.values()): fail(cnt, "FTzfine", name, a, c)
        # FT-CONST
        for t in range(a, b):
            if t in FT and MUT != 2: continue
            cnt["FTC_chk"] += 1
            if A[t] != A[t + 1]: fail(cnt, "FTC_A", name, t, c)
            if any(Kp(t, z) != Kp(t + 1, z) for z in A[t] | {c}): fail(cnt, "FTC_k", name, t, c)
            for x in Z[t][1:]:
                p = par(t + 1, x)
                if OM.sub(Kp(t, x), Kp(t, p)) != OM.sub(Kp(t + 1, x), Kp(t + 1, p)): fail(cnt, "FTC_off", name, t, c, x)
        ZCH = {t for t in range(a, b) if Z[t] != Z[t + 1]}
        CYC = {t for t in range(a, b) if any(x in set(Z[t]) for x in Qc)}
        ZC = ZCH & CYC; ZC2 = ZC & FT
        cnt["SUM_ZC"] += len(ZC); cnt["SUM_ZC2"] += len(ZC2); cnt["SUM_CYC"] += len(CYC)
        if len(ZC2) > min(len(ZC), len(FT)) or len(ZC2) > 2 * (n - 1) * (len(U) - 1): fail(cnt, "ZC2b", name, a, c)
        for t in range(a, b):
            for x in Qc:
                p = par(t + 1, x)
                o0, o1 = OM.sub(Kp(t, x), Kp(t, p)), OM.sub(Kp(t + 1, x), Kp(t + 1, p))
                if t in ZC2:
                    if x in set(Z[t]):
                        cnt["ZC2F_chk"] += 1
                        if o1 < o0: cnt["ZC2F_fall"] += 1
                    continue
                cnt["SA2_chk"] += 1
                if t in CYC and x in set(Z[t]): cnt["SA2_cycle_chk"] += 1
                if o1 < o0: fail(cnt, "SA2", name, t, c, x, p)
        # CHAIN-COUNT''
        EXIT = {x: {t for t in range(a, b) if par(t, x) != par(t + 1, x)} for x in Qc}
        cutZ = ZC2 if MUT != 3 else set()
        sumv = {}; Dm = 1
        for x in Qc:
            cx = EXIT[x] | cutZ; tot = 0; t = a
            while t < b:
                if t in cx: t += 1; continue
                s = t
                while t < b and t not in cx: t += 1
                p = par(s, x)
                seq = [OM.sub(Kp(k, x), Kp(k, p)) for k in range(s, t + 1)]
                tot += len(set(seq)) - 1; Dm = max(Dm, len(set(seq)))
                if any(seq[i + 1] < seq[i] for i in range(len(seq) - 1)): fail(cnt, "CC2_mono", name, s, c, x)
            sumv[x] = tot
        for q in Qc:
            chg = sum(1 for t in range(a, b) if Kp(t, q) != Kp(t + 1, q))
            sform = len(ZC2) + sum(len(EXIT[x]) + sumv[x] for x in Qc)
            dform = len(ZC2) + sum(Dm * (len(EXIT[x]) + len(ZC2) + 1) for x in Qc)
            cnt["CC2_chk"] += 1
            if chg > sform or chg > dform: fail(cnt, "CC2", name, a, c, q, chg, sform, dform)
        # PF-CHOICE
        for t in range(a, b + 1):
            for x in A[t]:
                if g.owner[x] != 1: continue
                opts = [y for y in g.succ[x] if y in A[t] or y == c]
                if not opts: fail(cnt, "PF_noopt", name, t, c, x); continue
                if sc == -1: keyf = lambda y: (Kp(t, y), (-y,) if MUT == 1 else (y,))
                else: keyf = lambda y: (Kp(t, y), tuple(-i for i in tb(st, t, c, y)) if MUT == 1 else tb(st, t, c, y))
                best = min(opts, key=keyf)
                cnt["PF_chk"] += 1
                if len(opts) > 1 and sum(1 for y in opts if Kp(t, y) == Kp(t, best)) > 1: cnt["PF_tied"] += 1
                if st[t]["sb"][x] != best: fail(cnt, "PF", name, t, c, x)
                if "sbsi" in st[t]:
                    cnt["PFSI_chk"] += 1
                    if st[t]["sbsi"][x] != best: fail(cnt, "PFSI", name, t, c, x)
        # TIE-CHARGE
        strict_tie = 0
        for t in range(a, b):
            if t not in FT:
                for z in A[t]:
                    cnt["TC_chk"] += 1
                    if st[t + 1]["nx"][z] != st[t]["nx"][z]: fail(cnt, "TC_next", name, t, c, z)
            if t in ZCH:
                Nn = [v for v in Z[t + 1][1:] if st[t + 1]["nx"][v] != st[t]["nx"][v]]
                if Nn:
                    strict_tie += 1
                    if any(Kp(t + 1, v) > Kp(t, v) for v in Nn): cnt["TC_STRICT"] += 1
                    else: cnt["TC_TIE"] += 1
                    if t not in FT: fail(cnt, "TC_inFT", name, t, c)
        if strict_tie > 2 * (n - 1) * (len(U) - 1): fail(cnt, "TC_count", name, a, c)


def main(a):
    cnt = Counter(); rng = random.Random(4949); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([] if (extra and os.environ.get("NOS3")) else [RE.best_reward_start(g)]) + \
                 [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    else:
        for f in a:
            path, _, sp = f.partition(":")
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            if not sp and os.path.exists(path[:-3] + ".start"): sp = path[:-3] + ".start"
            ex = None
            if sp:
                try: ex = load_start(g, sp)
                except Exception: cnt["start_err"] += 1
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
