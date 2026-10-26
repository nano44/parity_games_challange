#!/usr/bin/env python3
"""REFEREE succ. 15 probe for the addendum P-N5-OFFMONO-add-box49 (sha1 5911aba8). Own engine (rl_engine; offmono_probe's kap/kwt/par).
No lane code. Per phase and class c (U = U_c, Q_c := Q n U - {c}, Z_t(c) = c's honest cycle as a sequence from c):
 CID    (CYC-ID): x in U on an honest cycle at t <=> x in Z_t(c);  CSH  (CYC-SHAPE): kappa_t(v) = (0, s_c * dist(v, c)) on Z_t(c), v != c
 ZC     Remark Z-CONST: Z_t = Z_{t+1} => kappa, par and off(x; par) unchanged on the cycle
 SA     CHAIN-COUNT' Step A at every transition NOT in ZC_c, every x in Q_c, p := par_{t+1}(x): off_{t+1}(x; p) >= off_t(x; p)
 ZCF    (the Lead's question) the same inequality AT the ZC_c transitions, for x on c's cycle at t: counted, not a claim (does the cut bite?)
 CCP    CHAIN-COUNT' sum form and stated form (D := max v_x over x-pieces') on J := the phase
 ZK     ZCH-COUNT: kinds STRICT / TIE / CEVEN / ODDC partition ZCH_c; TIE: N all Odd with kappa unchanged; ODDC: c in Q and sigmabar(c) changed;
        STRICT charges <= n - 1 per vertex; CEVEN <= n - 1; psi non-decreasing for c Even; |ZCH_c| <= (n - 1)|U_c| + TIE_c + ODDC_c
Mutations: MUT=1 pieces' not cut at ZC_c (the lane's control);  MUT=2 opposite length sign;  MUT=3 pieces' not cut at EXIT_x.
Usage: zch_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 64, NOS3)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, hon_probe as HP
import offmono_probe as OM
from flip_probe import nxt, on_cycle
EX = []
MUT = int(os.environ.get("MUT", "0"))
OM.MUT = 2 if MUT == 2 else 0


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def Zc(nx, c):
    z = [c]; x = nx[c]
    while x != c and len(z) <= len(nx): z.append(x); x = nx[x]
    return tuple(z)


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1}
    for x in st: x["nx"] = nxt(g, x["s"], x["sb"])
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        if j > k: phase(g, st, k, j, lam, Q, cnt, name)
        k = j + 1


def phase(g, st, a, b, lam, Q, cnt, name):
    n = g.n
    for c in sorted(set(lam)):
        U = {v for v in range(n) if lam[v] == c}
        Qc = sorted((Q & U) - {c})
        Kp = lambda t, z: OM.kap(g, c, st[t]["Xi"][z])
        Z = {t: Zc(st[t]["nx"], c) for t in range(a, b + 1)}
        sc = (1 if g.prio[c] % 2 else -1) * (-1 if MUT == 2 else 1)
        for t in range(a, b + 1):
            zs = set(Z[t])
            for x in U:
                cnt["CID_chk"] += 1
                if on_cycle(st[t]["nx"], x) != (x in zs): fail(cnt, "CID", name, t, c, x)
            for i, v in enumerate(Z[t][1:], 1):
                cnt["CSH_chk"] += 1
                if MUT != 2 and Kp(t, v) != (0, sc * (len(Z[t]) - i)): fail(cnt, "CSH", name, t, c, v)
        ZCH = {t for t in range(a, b) if Z[t] != Z[t + 1]}
        CYC = {t for t in range(a, b) if any(x in set(Z[t]) for x in Qc)}
        ZC = ZCH & CYC
        par = lambda t, x: OM.par(st[t]["nx"], Q, x, c)
        for t in range(a, b):
            if t not in ZCH:
                for x in Z[t]:
                    cnt["ZC_chk"] += 1
                    if Kp(t, x) != Kp(t + 1, x): fail(cnt, "ZC_k", name, t, c, x)
                    if x != c and x in Q:
                        p0, p1 = par(t, x), par(t + 1, x)
                        if p0 != p1 or OM.sub(Kp(t, x), Kp(t, p0)) != OM.sub(Kp(t + 1, x), Kp(t + 1, p1)): fail(cnt, "ZC_par", name, t, c, x)
            for x in Qc:
                p = par(t + 1, x)
                o0, o1 = OM.sub(Kp(t, x), Kp(t, p)), OM.sub(Kp(t + 1, x), Kp(t + 1, p))
                if t in ZC:
                    if x in set(Z[t]):
                        cnt["ZCF_chk"] += 1
                        if o1 < o0: cnt["ZCF_fall"] += 1; EX.append(("ZCF_fall", name, t, c, x)) if len(EX) < 40 else None
                    continue
                cnt["SA_chk"] += 1
                if o1 < o0: fail(cnt, "SA", name, t, c, x, p, o0, o1)
        # CHAIN-COUNT' on J = the phase
        cut = lambda x: ({t for t in range(a, b) if par(t, x) != par(t + 1, x)} if MUT != 3 else set()) | (ZC if MUT != 1 else set())
        EXIT = {x: {t for t in range(a, b) if par(t, x) != par(t + 1, x)} for x in Qc}
        sumv = {}; Dm = 1
        for x in Qc:
            cx = cut(x); tot = 0; t = a
            while t < b:
                if t in cx: t += 1; continue
                s = t
                while t < b and t not in cx: t += 1
                p = par(s, x)
                vals = {OM.sub(Kp(k, x), Kp(k, p)) for k in range(s, t + 1)}
                tot += len(vals) - 1; Dm = max(Dm, len(vals))
                seq = [OM.sub(Kp(k, x), Kp(k, p)) for k in range(s, t + 1)]
                if any(seq[i + 1] < seq[i] for i in range(len(seq) - 1)): fail(cnt, "PM", name, s, c, x)
            sumv[x] = tot
        cnt["MAX_D"] = max(cnt["MAX_D"], Dm)
        for q in Qc:
            chg = sum(1 for t in range(a, b) if Kp(t, q) != Kp(t + 1, q))
            sform = len(ZC) + sum(len(EXIT[x]) + sumv[x] for x in Qc)
            dform = len(ZC) + sum(Dm * (len(EXIT[x]) + len(ZC) + 1) for x in Qc)
            cnt["CCP_chk"] += 1
            if chg > sform or chg > dform: fail(cnt, "CCP", name, a, c, q, chg, sform, dform)
        # ZCH-COUNT
        kinds = Counter(); charges = Counter(); psi_prev = None
        for t in range(a, b + 1):
            if g.owner[c] == 0:
                psi = Kp(t, st[t]["nx"][c])
                if psi_prev is not None and psi < psi_prev: fail(cnt, "PSI", name, t, c)
                psi_prev = psi
        for t in sorted(ZCH):
            Nn = [v for v in Z[t + 1][1:] if st[t + 1]["nx"][v] != st[t]["nx"][v]]
            strict = [v for v in Nn if Kp(t + 1, v) > Kp(t, v)]
            if strict: kinds["STRICT"] += 1; charges[strict[0]] += 1
            elif Nn:
                kinds["TIE"] += 1
                if any(g.owner[v] == 0 or Kp(t + 1, v) != Kp(t, v) for v in Nn): fail(cnt, "TIE", name, t, c)
            elif g.owner[c] == 0: kinds["CEVEN"] += 1
            else:
                kinds["ODDC"] += 1
                if c not in Q or st[t]["sb"][c] == st[t + 1]["sb"][c]: fail(cnt, "ODDC", name, t, c)
        for k2, v2 in kinds.items(): cnt["ZK_" + k2] += v2
        cnt["ZK_chk"] += 1
        if any(v2 > n - 1 for v2 in charges.values()) or kinds["CEVEN"] > n - 1 or len(ZCH) > (n - 1) * len(U) + kinds["TIE"] + kinds["ODDC"]:
            fail(cnt, "ZK", name, a, c)
        cnt["SUM_ZCH"] += len(ZCH); cnt["SUM_CYC"] += len(CYC); cnt["SUM_ZC"] += len(ZC)


def main(a):
    cnt = Counter(); rng = random.Random(1597); nst = int(os.environ.get("RANDSTARTS", "2"))
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
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), HP.parse_start(g, sp) if sp else None)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
