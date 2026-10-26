#!/usr/bin/env python3
"""REFEREE succ. 15 probe for packet P-N5-FBC (docs/new/P-N5-FBC-box47.md, pin de02d37e, sha1 32d3776c...). Own engine only (rl_engine;
exact path levels by simple-path enumeration, ff_probe.best_le_budget / level; epr_probe.wval). No lane code. Per phase ((lambda, tau) const):
 REAL   Xi_k(x) = value of the honest play (sigma_k, sigmabar_k) from x, every state (sanity of the frame)
 MONO   LEV_C non-decreasing along P, for every configuration C visited in P (at every state of P, C-state or not)
 FBC    Lemma FB-RISE_C: in-phase fallback t -> t+1, C := sigmabar_t|Q: LEV_C(t+1) >= min(LEV_C(t) + 1, n - 1)
 ODDC   its Odd case, at EVERY C-state t (not only fallbacks): Odd level in H_C >= min(LEV_C(t) + 1, n - 1)
 SATB   Lemma SAT_C (1): C-state t with LEV_C(t) = n - 1 has Xi_t = B_C
 SATW   Lemma SAT_C (2): saturated C-state t < C-state t': Xi constant on t..t' and t' - t <= 4n(n - 1)
 THM    Theorem FB-C: per C unsaturated fallbacks <= n - 1, saturated <= 4n(n - 1) + 1; f <= |C_f|(4n^2 - 3n)
 CORA   |C_f| <= distinct configurations of P <= min(N_ep, prod deg); also landed EPOCH f <= 1 + n N_ep (comparison only)
 CORC   if every state of P has |D| <= 1: configurations <= 1 + sum_q (deg q - 1)
 stats  saturated fallbacks per C (max), fallbacks leaving Xi unchanged, after-saturation returns to C
Mutations (each must bite): MUT=1 read every fallback in G_tau (C := tau|Q) instead of H_C;  MUT=2 FBC asks + 2;
 MUT=3 engine: S4c picks the (Xi, w)-MINIMUM of Iσ(x) (Even case 3 needs the maximum).
Usage: fbc_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 40, BUDGET 2e6 per configuration)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E, hon_probe as HP, ff_probe as FF
EX = []
MUT = int(os.environ.get("MUT", "0"))


def run_mut3(g, start):
    """RE.run with S4c's argmax replaced by argmin (MUT=3 only)."""
    gd = g.dual(); s, t = start; s, t = list(s), list(t); out = []
    for _ in range(100000):
        Xi, sb = RE.evaluate(g, s)
        Ut, _ = RE.evaluate(gd, [t[v] if g.owner[v] == 1 else None for v in range(g.n)])
        Is = RE.improving(g, Xi, s, 0)
        It = [(v, w) for v in range(g.n) if g.owner[v] == 1 for w in g.succ[v] if w != t[v] and gd.key(Ut[w]) > gd.key(Ut[t[v]])]
        st = dict(s=list(s), t=list(t), Is=Is, It=It, Xi=Xi, sb=sb, fb=False); out.append(st)
        if not Is and not It: return out
        sn = E.s4a(g, s, t, Is) if Is else list(s)
        if It:
            A = {v: {t[v]} for v in range(g.n) if g.owner[v] == 1}
            for v, w in It: A[v].add(w)
            keep = [sorted(A[v]) if g.owner[v] == 1 else [s[v]] for v in range(g.n)]
            _, ch = RE.evaluate(g.restrict(keep), s); tn = [ch[v] if g.owner[v] == 1 else None for v in range(g.n)]
        else: tn = list(t)
        if sn == s and tn == t:
            st["fb"] = True
            if Is:
                for v in range(g.n):
                    cand = [w for (x, w) in Is if x == v]
                    if cand: sn[v] = min(cand, key=lambda w: (g.key(Xi[w]), w))
            else:
                for v in range(g.n):
                    cand = [w for (x, w) in It if x == v]
                    if cand: tn[v] = max(cand, key=lambda w: (gd.key(Ut[w]), w))
        s, t = sn, tn
    raise RuntimeError("maxit")


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def analyse(g, start, cnt, name):
    st = run_mut3(g, start) if MUT == 3 else RE.run(g, start); n = g.n
    Q = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    odd = [v for v in range(n) if g.owner[v] == 1]
    info = []
    for x in st:
        nx = [x["s"][v] if g.owner[v] == 0 else x["sb"][v] for v in range(n)]
        cnt["REAL_chk"] += 1
        if any(RE.play_value(g, nx, v) != tuple(x["Xi"][v]) for v in range(n)): fail(cnt, "REAL", name)
        info.append(dict(lam=tuple(v[0] for v in x["Xi"]), t=tuple(x["t"]), C=tuple(x["sb"][q] for q in Q),
                         D=frozenset(q for q in Q if x["sb"][q] != x["t"][q])))
    K = len(st); k = 0
    while k < K:
        j = k
        while j + 1 < K and info[j + 1]["lam"] == info[k]["lam"] and info[j + 1]["t"] == info[k]["t"]: j += 1
        phase(g, st, info, k, j, cnt, name, n, Q, odd)
        k = j + 1


def phase(g, st, info, a, b, cnt, name, n, Q, odd):
    cnt["PHASES"] += 1; bnd = 4 * n * n - 3 * n
    fbs = [t for t in range(a, b) if st[t]["fb"]]
    for t in fbs:
        assert st[t + 1]["t"] == st[t]["t"]          # in-phase fallback leaves tau (FIX 3)
    confs = sorted({info[k]["C"] for k in range(a, b + 1)})
    eps = 1 + sum(1 for k in range(a, b) if info[k + 1]["C"] != info[k]["C"])
    pdeg = 1
    for q in Q: pdeg *= len(g.succ[q])
    Cf = {info[t]["C"] for t in fbs}
    cnt["CORA_chk"] += 1
    if not (len(Cf) <= len(confs) <= min(eps, pdeg)): fail(cnt, "CORA", name, a)
    if len(fbs) > 1 + n * eps: fail(cnt, "EPOCH_landed", name, a)
    if all(len(info[k]["D"]) <= 1 for k in range(a, b + 1)):
        cnt["CORC_chk"] += 1
        if len(confs) > 1 + sum(len(g.succ[q]) - 1 for q in Q): fail(cnt, "CORC", name, a)
    if not fbs: return
    cnt["PH_FB"] += 1; cnt["F"] += len(fbs); cnt["SUM_CONF_FB"] += len(confs); cnt["SUM_EP_FB"] += eps; cnt["SUM_CF"] += len(Cf)
    cnt["MAX_F_PHASE"] = max(cnt["MAX_F_PHASE"], len(fbs)); cnt["MAX_CF"] = max(cnt["MAX_CF"], len(Cf))
    if len(fbs) > len(Cf) * bnd: fail(cnt, "THM", name, a, "total")
    rho = sum(1 for k in range(a, b) for q in Q if st[k + 1]["Xi"][q] != st[k]["Xi"][q])
    cnt["MAX_RHO_FBPH"] = max(cnt["MAX_RHO_FBPH"], rho)
    if 1 + (n - 1) * (2 + rho) > len(Cf) * bnd: cnt["R56_BOUND_ABOVE_FBC"] += 1; EX.append(("R56>FBC", name, a, rho, len(Cf), n))
    if n > int(os.environ.get("LEVMAX", "40")): cnt["SKIP_N"] += 1; return
    lam = info[a]["lam"]; t0 = list(st[a]["t"]); cyc = {u for u in range(n) if lam[u] == u}
    frames = set(confs) | ({tuple(t0[q] for q in Q)} if MUT == 1 else set())
    best = {}
    try:
        for C in frames:
            cm = dict(zip(Q, C))
            succ = [list(g.succ[v]) if (g.owner[v] == 0 or v not in cm) else [cm[v]] for v in range(n)]
            best[C] = FF.best_le_budget(g, succ, cyc, n, float(os.environ.get("BUDGET", "2e6")))
    except FF.Over: cnt["UNK_PHASES"] += 1; return
    LEV = {C: [FF.level(g, st[k]["Xi"], best[C], n, range(n)) for k in range(a, b + 1)] for C in frames}
    for C in confs:
        L = LEV[C]; cnt["MONO_chk"] += 1
        if any(L[i + 1] < L[i] for i in range(len(L) - 1)): fail(cnt, "MONO", name, a, C)
        Cst = [k for k in range(a, b + 1) if info[k]["C"] == C]
        for k in Cst:
            cnt["ODDC_chk"] += 1
            lo = FF.level(g, st[k]["Xi"], best[C], n, odd)
            if lo < min(L[k - a] + 1, n - 1): fail(cnt, "ODDC", name, k, L[k - a], lo)
        sat = [k for k in Cst if L[k - a] == n - 1]
        for k in sat:
            cnt["SATB_chk"] += 1
            if any(best[C][x][n - 1] is not None and tuple(st[k]["Xi"][x]) != best[C][x][n - 1] for x in range(n)):
                fail(cnt, "SATB", name, k)
        if sat:
            t1 = sat[0]; tl = Cst[-1]; cnt["SATW_chk"] += 1
            if any(st[k]["Xi"] != st[t1]["Xi"] for k in range(t1, tl + 1)) or tl - t1 > 4 * n * (n - 1): fail(cnt, "SATW", name, t1, tl)
            if any(k > t1 for k in Cst): cnt["SAT_RETURN"] += 1
        fC = [t for t in fbs if info[t]["C"] == C]
        uns = [t for t in fC if L[t - a] <= n - 2]; sf = [t for t in fC if L[t - a] == n - 1]
        cnt["MAX_UNS_C"] = max(cnt["MAX_UNS_C"], len(uns)); cnt["MAX_SAT_C"] = max(cnt["MAX_SAT_C"], len(sf))
        cnt["THM_chk"] += 1
        if len(uns) > n - 1 or len(sf) > 4 * n * (n - 1) + 1: fail(cnt, "THM", name, a, C, len(uns), len(sf))
    tauC = tuple(t0[q] for q in Q)
    for t in fbs:
        C = tauC if MUT == 1 else info[t]["C"]; L = LEV[C]; cnt["FBC_chk"] += 1
        if st[t + 1]["Xi"] == st[t]["Xi"]:
            cnt["FB_XI_FLAT"] += 1   # referee's sharpening: R15 (b) + R38 (f) CN-LAST => t + 1 is the last state of P
            if t + 1 != b: fail(cnt, "FLATLAST", name, t)
        if L[t + 1 - a] < min(L[t - a] + (2 if MUT == 2 else 1), n - 1): fail(cnt, "FBC", name, t, C, L[t - a], L[t + 1 - a])
        if L[t - a] >= n - 1: cnt["FB_SAT"] += 1


def main(a):
    cnt = Counter(); rng = random.Random(1547); nst = int(os.environ.get("RANDSTARTS", "2"))
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
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
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), HP.parse_start(g, sp) if sp else None)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
