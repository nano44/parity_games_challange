#!/usr/bin/env python3
"""REFEREE succ. 17 probe for packet P-N5-FBCK (docs/new/P-N5-FBCK-box49.md, sha1 7747ecf2..., freeze l-new 0e63596d). Own engine only
(rl_engine; exact path levels by simple-path enumeration, ff_probe.best_le_budget / level, as fbc_probe.py). No lane code.
K := vertices reachable (>= 0 edges) from an Even vertex of out-degree >= 2; n_K = |K|; Q_K = Q n K; K-configuration C = sigmabar|Q_K;
H^K_C = G[K] with Odd v in Q_K cut to C(v). Per phase ((lambda, tau) constant):
 K1     K closed under successors;  K2  Even x outside K has out-degree 1 and Isigma(x) empty at every state;  K3  K empty => no in-phase fallback
 REAL   Xi_k(x) = value of the honest play (every state)
 MONO   LEV^K_C non-decreasing along P, every K-configuration visited in P
 RISE   FB-RISE^K at every in-phase fallback t -> t+1, C := K-config of t
 SATB   SAT^K (1): saturated K-C-state t has Xi_t = B^K_C on K;  SATW  SAT^K (2): Xi constant on K from a saturated K-C-state to any later K-C-state
 SATFB  SAT-FB^K: saturated fallback source t => t+1 is the last state of P, or no K-C-state after t
 SATFB1 at most one saturated fallback source per K-configuration;  THM  per C: fallback sources <= n_K; f <= n_K |C^K_f|
 COR1   n_K <= n, |C^K_f| <= |C_f|  (and f <= n |C_f|, R73's FB-C')
Mutations: MUT=1 RISE asks +2;  MUT=2 C read at t+1 (sigmabar_{t+1}|Q_K) in RISE;  MUT=3 THM per-C bound n_K // 2 (sensitivity);
 MUT=4 engine: S4c picks the (Xi, w)-MINIMUM (fbc_probe.run_mut3); SATFB / RISE should bite.
Usage: fbck_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 40, LEVMAX 40, BUDGET 2e6)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, hon_probe as HP, ff_probe as FF
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def kset(g):
    seeds = [v for v in range(g.n) if g.owner[v] == 0 and len(g.succ[v]) >= 2]
    K = set(seeds); st = list(seeds)
    while st:
        v = st.pop()
        for w in g.succ[v]:
            if w not in K: K.add(w); st.append(w)
    return K


def analyse(g, start, cnt, name):
    if MUT == 4:
        import fbc_probe as FB
        FB.MUT = 3; st = FB.run_mut3(g, start)
    else: st = RE.run(g, start)
    n = g.n
    K = kset(g); nK = len(K)
    Q = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]; QK = [q for q in Q if q in K]
    cnt["K_chk"] += 1
    if any(w not in K for v in K for w in g.succ[v]): fail(cnt, "K1", name)
    if any(g.owner[v] == 0 and v not in K and len(g.succ[v]) != 1 for v in range(n)): fail(cnt, "K2", name)
    for x in st:
        if any(v not in K for (v, w) in x["Is"]): fail(cnt, "K2_Is", name)
    if nK < n: cnt["RUNS_nK_lt_n"] += 1
    info = []
    for x in st:
        nx = [x["s"][v] if g.owner[v] == 0 else x["sb"][v] for v in range(n)]
        cnt["REAL_chk"] += 1
        if any(RE.play_value(g, nx, v) != tuple(x["Xi"][v]) for v in range(n)): fail(cnt, "REAL", name)
        info.append(dict(lam=tuple(v[0] for v in x["Xi"]), t=tuple(x["t"]), CK=tuple(x["sb"][q] for q in QK),
                         C=tuple(x["sb"][q] for q in Q)))
    T = len(st); k = 0
    while k < T:
        j = k
        while j + 1 < T and info[j + 1]["lam"] == info[k]["lam"] and info[j + 1]["t"] == info[k]["t"]: j += 1
        phase(g, st, info, k, j, cnt, name, n, K, nK, QK)
        k = j + 1


def phase(g, st, info, a, b, cnt, name, n, K, nK, QK):
    cnt["PHASES"] += 1
    fbs = [t for t in range(a, b) if st[t]["fb"]]
    for t in fbs: assert st[t + 1]["t"] == st[t]["t"]
    if not K:
        cnt["K3_chk"] += 1
        if fbs: fail(cnt, "K3", name, a)
        return
    if not fbs: return
    CfK = {info[t]["CK"] for t in fbs}; Cf = {info[t]["C"] for t in fbs}
    cnt["PH_FB"] += 1; cnt["F"] += len(fbs); cnt["SUM_CF"] += len(Cf); cnt["SUM_CFK"] += len(CfK)
    cnt["MAX_CFK"] = max(cnt["MAX_CFK"], len(CfK))
    if len(CfK) < len(Cf): cnt["PH_CFK_lt_CF"] += 1
    if nK < n: cnt["PH_nK_lt_n"] += 1
    cnt["COR1_chk"] += 1
    if nK > n or len(CfK) > len(Cf) or len(fbs) > n * len(Cf): fail(cnt, "COR1", name, a)
    cnt["THMtot_chk"] += 1
    if len(fbs) > nK * len(CfK): fail(cnt, "THMtot", name, a, len(fbs), nK, len(CfK))
    if n > int(os.environ.get("LEVMAX", "40")): cnt["SKIP_LEV"] += 1; return
    lam = info[a]["lam"]; cyc = {u for u in range(n) if lam[u] == u}
    confs = sorted({info[k]["CK"] for k in range(a, b + 1)})
    best = {}
    try:
        for C in confs:
            cm = dict(zip(QK, C))
            succ = [list(g.succ[v]) if (g.owner[v] == 0 or v not in cm) else [cm[v]] for v in range(n)]
            best[C] = FF.best_le_budget(g, succ, cyc, n, float(os.environ.get("BUDGET", "2e6")))
    except FF.Over: cnt["UNK_PHASES"] += 1; return
    Kl = sorted(K)
    LEV = {C: [min(FF.level(g, st[k]["Xi"], best[C], n, Kl), nK - 1) for k in range(a, b + 1)] for C in confs}
    for C in confs:
        L = LEV[C]; cnt["MONO_chk"] += 1
        if any(L[i + 1] < L[i] for i in range(len(L) - 1)): fail(cnt, "MONO", name, a, C)
        if min(L) < 0: fail(cnt, "LEV0", name, a, C)
        Cst = [k for k in range(a, b + 1) if info[k]["CK"] == C]
        sat = [k for k in Cst if L[k - a] == nK - 1]
        for k in sat:
            cnt["SATB_chk"] += 1
            if any(best[C][x][n - 1] is not None and tuple(st[k]["Xi"][x]) != best[C][x][n - 1] for x in Kl): fail(cnt, "SATB", name, k)
        if sat:
            t1 = sat[0]; tl = Cst[-1]; cnt["SATW_chk"] += 1
            if any(st[k]["Xi"][x] != st[t1]["Xi"][x] for k in range(t1, tl + 1) for x in Kl): fail(cnt, "SATW", name, t1, tl)
        fC = [t for t in fbs if info[t]["CK"] == C]
        sf = [t for t in fC if L[t - a] == nK - 1]
        for t in sf:
            cnt["SATFB_chk"] += 1
            if not (t + 1 == b or not any(k > t for k in Cst)): fail(cnt, "SATFB", name, t, C)
        cnt["SATFB1_chk"] += 1
        if len(sf) > 1: fail(cnt, "SATFB1", name, a, C, len(sf))
        cnt["THM_chk"] += 1
        bound = nK // 2 if MUT == 3 else nK
        if len(fC) > bound: fail(cnt, "THM" + ("_MUT3" if MUT == 3 else ""), name, a, C, len(fC), nK)
        cnt["MAX_FC_x1000_over_nK"] = max(cnt["MAX_FC_x1000_over_nK"], 1000 * len(fC) // nK)
        cnt["SAT_FB"] += len(sf)
    for t in fbs:
        C = info[t + 1]["CK"] if MUT == 2 else info[t]["CK"]
        if C not in LEV: cnt["RISE_skip_C"] += 1; continue
        L = LEV[C]; cnt["RISE_chk"] += 1
        if L[t - a] <= nK - 2: cnt["RISE_unsat"] += 1
        if L[t + 1 - a] < min(L[t - a] + (2 if MUT == 1 else 1), nK - 1): fail(cnt, "RISE", name, t, C, L[t - a], L[t + 1 - a])


def main(a):
    cnt = Counter(); rng = random.Random(4917); nst = int(os.environ.get("RANDSTARTS", "2"))
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
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "40")): cnt["skip_big"] += 1; continue
            if not sp and os.path.exists(path[:-3] + ".start"): sp = path[:-3] + ".start"
            ex = None
            if sp:
                try: ex = HP.parse_start(g, sp)
                except Exception: cnt["bad_start"] += 1
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
