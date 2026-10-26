#!/usr/bin/env python3
"""REFEREE succ. 15 probe for packet P-N5-EPC (docs/new/P-N5-EPC-box48.md, l-new 81ab0b72, sha1 9f48ded7...). Own engine only (rl_engine;
exact LEV_C per configuration by simple-path enumeration in H_C, my fbc_probe / ff_probe helpers). No lane code. Per phase ((lambda, tau)):
 FBR    FB-RISE_C at every in-phase fallback (restated §1);  SATB  SAT_C (1);  SATW  SAT_C (2) (Xi constant up to a later C-state)
 RET    Lemma RET-FB: every in-phase fallback t -> t+1, EVERY configuration C visited in P, every C-state s >= t+1 of P:
        LEV_C(s) >= min(LEV_C(t) + 1, n - 1)
 VIS    Corollary VIS: per C, returns of kind (a) (LEV_C(s_i) = n-1) <= 2n(n-1), kind (b) (fallback source in [s_i, s_i+1)) <= n-1 and each
        rises LEV_C, V_C <= 2n^2 - n + R0_C
 EPC    Theorem EP-C: N_ep <= NCONF (2n^2 - n) + R0, and R0 <= sum over maximal fallback-free runs S of REV(S)
 SATFB  Lemma SAT-FB: saturated C-state fallback source t => t+1 last state of P or no C-state after t; and if a C-state follows, Is_{t+1} = {}
 SATFB1 <= 1 saturated fallback source per C;  FBCP  Theorem FB-C': f <= n |C_f|
 ASM    EP-ASM pieces: N_0 <= 4n^2-3n; N_>=2 <= NCONF_>=2 (2n^2-n) + R0_>=2; N_ep = N_0 + N_1 + N_>=2; X_dir, X_big recorded
 DREM   remark: (D changes in P) + 1 <= N_ep
 DEAD   counts saturated fallbacks that are not Xi-flat / not last (the packet's DEAD guess)
Mutations (must bite): MUT=1 RET asks + 2;  MUT=2 RET checked at EVERY later state s (not only C-states);  MUT=3 SAT-FB read as the DEAD
 guess "t + 1 is the last state of P" (no disjunction).
Usage: epc_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 34, LEVMAX 34, BUDGET 2e6 per configuration)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, hon_probe as HP, ff_probe as FF
EX = []
MUT = int(os.environ.get("MUT", "0"))


def best_depth(g, succ, cyc, n, Dd, budget):
    """best[x][j] for j <= Dd: best value over simple paths with <= j edges to a cycle node (depth-capped ff_probe.best_le_budget)"""
    best = [[None] * (Dd + 1) for _ in range(g.n)]; used = 0
    for x in range(g.n):
        byL = [None] * (Dd + 1); stack = [(x, (x,))]
        while stack:
            v, p = stack.pop(); used += 1
            if used > budget: raise FF.Over()
            if v in cyc:
                val = (v, 0, 0)
                for w in reversed(p[:-1]): val = g.ext(w, val)
                Lp = len(p) - 1
                if byL[Lp] is None or g.key(val) > g.key(byL[Lp]): byL[Lp] = val
            if len(p) - 1 >= Dd: continue
            for w in succ[v]:
                if w not in p: stack.append((w, p + (w,)))
        cur = None
        for j in range(Dd + 1):
            if byL[j] is not None and (cur is None or g.key(byL[j]) > g.key(cur)): cur = byL[j]
            best[x][j] = cur
    return best


def deep_phase(g, st, info, a, b, cnt, name, n, Q, fbs, confs):
    """DEPTH mode: levels capped at Dd; a check counts only when decided (RET, FBR)."""
    Dd = min(int(os.environ["DEPTH"]), n - 1)
    lam = info[a]["lam"]; cyc = {u for u in range(n) if lam[u] == u}; LEV = {}
    try:
        for C in confs:
            cm = dict(zip(Q, C))
            succ = [list(g.succ[v]) if (g.owner[v] == 0 or v not in cm) else [cm[v]] for v in range(n)]
            bd = best_depth(g, succ, cyc, n, Dd, float(os.environ.get("BUDGET", "2e6")))
            LEV[C] = [FF.level(g, st[k]["Xi"], bd, Dd + 1, range(n)) for k in range(a, b + 1)]
    except FF.Over: cnt["UNK_PHASES"] += 1; return
    cnt["PH_DEEP"] += 1
    def dec(C, t, s, plus):
        lt, ls = LEV[C][t - a], LEV[C][s - a]
        if lt == Dd and Dd < n - 1: return None
        tg = min(lt + plus, n - 1)
        if ls >= tg: return True
        if ls == Dd and Dd < n - 1: return None
        return False
    for t in fbs:
        r = dec(info[t]["C"], t, t + 1, 1); cnt["FBR_UNDEC" if r is None else "FBR_chk"] += 1
        if r is False: fail(cnt, "FBR", name, t)
        for C in confs:
            for s in range(t + 1, b + 1):
                if MUT != 2 and info[s]["C"] != C: continue
                r = dec(C, t, s, 2 if MUT == 1 else 1)
                cnt["RET_UNDEC" if r is None else "RET_chk"] += 1
                if r is False: fail(cnt, "RET", name, t, s, C)


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = [v for v in range(n) if g.owner[v] == 1 and len(g.succ[v]) > 1]
    info = [dict(lam=tuple(v[0] for v in x["Xi"]), t=tuple(x["t"]), C=tuple(x["sb"][q] for q in Q),
                 D=frozenset(q for q in Q if x["sb"][q] != x["t"][q])) for x in st]
    K = len(st); k = 0
    while k < K:
        j = k
        while j + 1 < K and info[j + 1]["lam"] == info[k]["lam"] and info[j + 1]["t"] == info[k]["t"]: j += 1
        phase(g, st, info, k, j, cnt, name, n, Q)
        k = j + 1


def phase(g, st, info, a, b, cnt, name, n, Q):
    cnt["PHASES"] += 1; bnd = 4 * n * n - 3 * n; w2 = 2 * n * n - n
    fbs = [t for t in range(a, b) if st[t]["fb"]]
    eps = []; k = a
    while k <= b:
        j = k
        while j + 1 <= b and info[j + 1]["C"] == info[k]["C"]: j += 1
        eps.append((k, j)); k = j + 1
    Nep = len(eps); confs = sorted({info[x]["C"] for x, _ in eps})
    # remark: D changes + 1 <= N_ep
    dch = sum(1 for k in range(a, b) if info[k + 1]["D"] != info[k]["D"])
    cnt["DREM_chk"] += 1
    if dch + 1 > Nep: fail(cnt, "DREM", name, a)
    # EP-ASM pieces that need no level
    N0 = sum(1 for x, _ in eps if not info[x]["D"]); N1 = sum(1 for x, _ in eps if len(info[x]["D"]) == 1)
    N2 = Nep - N0 - N1
    cnt["ASM_chk"] += 1
    if N0 > bnd: fail(cnt, "ASM0", name, a)
    xdir = sum(1 for k in range(a, b) if len(info[k]["D"]) == 1 and len(info[k + 1]["D"]) == 1 and info[k]["D"] != info[k + 1]["D"])
    xbig = sum(1 for k in range(a, b) if len(info[k]["D"]) >= 2 and len(info[k + 1]["D"]) == 1)
    cnt["MAX_XDIR"] = max(cnt["MAX_XDIR"], xdir); cnt["MAX_XBIG"] = max(cnt["MAX_XBIG"], xbig)
    cnt["MAX_NEP"] = max(cnt["MAX_NEP"], Nep); cnt["MAX_NCONF"] = max(cnt["MAX_NCONF"], len(confs))
    Cf = {info[t]["C"] for t in fbs}
    cnt["FBCP_chk"] += 1
    if len(fbs) > n * len(Cf): fail(cnt, "FBCP", name, a, len(fbs), len(Cf))
    if os.environ.get("DEPTH"): deep_phase(g, st, info, a, b, cnt, name, n, Q, fbs, confs); return
    if n > int(os.environ.get("LEVMAX", "34")): cnt["SKIP_N"] += 1; return
    if not fbs and all(len([1 for x, _ in eps if info[x]["C"] == C]) < 2 for C in confs): cnt["PH_TRIVIAL"] += 1; return
    lam = info[a]["lam"]; cyc = {u for u in range(n) if lam[u] == u}
    best = {}
    try:
        for C in confs:
            cm = dict(zip(Q, C))
            succ = [list(g.succ[v]) if (g.owner[v] == 0 or v not in cm) else [cm[v]] for v in range(n)]
            best[C] = FF.best_le_budget(g, succ, cyc, n, float(os.environ.get("BUDGET", "2e6")))
    except FF.Over: cnt["UNK_PHASES"] += 1; return
    cnt["PH_LEV"] += 1
    LEV = {C: [FF.level(g, st[k]["Xi"], best[C], n, range(n)) for k in range(a, b + 1)] for C in confs}
    def L(C, k): return LEV[C][k - a]
    # §1 restated
    for t in fbs:
        C = info[t]["C"]; cnt["FBR_chk"] += 1
        if L(C, t + 1) < min(L(C, t) + 1, n - 1): fail(cnt, "FBR", name, t)
    R0tot = 0; R0ge2 = 0; NCONF2 = 0
    for C in confs:
        Cst = [k for k in range(a, b + 1) if info[k]["C"] == C]
        sat = [k for k in Cst if L(C, k) == n - 1]
        for k in sat:
            cnt["SATB_chk"] += 1
            if any(best[C][x][n - 1] is not None and tuple(st[k]["Xi"][x]) != best[C][x][n - 1] for x in range(n)): fail(cnt, "SATB", name, k)
        if sat:
            cnt["SATW_chk"] += 1
            if any(st[k]["Xi"] != st[sat[0]]["Xi"] for k in range(sat[0], Cst[-1] + 1)): fail(cnt, "SATW", name, sat[0])
        # RET-FB: every fallback t, every later C-state s (MUT=2: every later state)
        for t in fbs:
            later = range(t + 1, b + 1) if MUT == 2 else [s for s in Cst if s >= t + 1]
            for s in later:
                cnt["RET_chk"] += 1
                if info[t]["C"] != C: cnt["RET_chk_otherC"] += 1
                if L(C, s) < min(L(C, t) + (2 if MUT == 1 else 1), n - 1): fail(cnt, "RET", name, t, s, C, L(C, t), L(C, s))
        # VIS
        starts = [x for x, _ in eps if info[x]["C"] == C]
        V = len(starts); ka = kb = r0 = 0
        for i in range(V - 1):
            si, sj = starts[i], starts[i + 1]
            if L(C, si) == n - 1: ka += 1
            elif any(si <= t < sj for t in fbs):
                kb += 1
                if L(C, sj) < min(L(C, si) + 1, n - 1): fail(cnt, "VISB_rise", name, si, sj)
            else: r0 += 1
        cnt["VIS_chk"] += 1
        if ka > 2 * n * (n - 1) or kb > n - 1 or V > w2 + r0: fail(cnt, "VIS", name, a, C, ka, kb, r0, V)
        cnt["RET_A"] += ka; cnt["RET_B"] += kb; cnt["RET_R0"] += r0; cnt["MAX_V_C"] = max(cnt["MAX_V_C"], V)
        R0tot += r0
        DC = sum(1 for q, c in zip(Q, C) if c != st[a]["t"][q])
        if DC >= 2: NCONF2 += 1; R0ge2 += r0
        # SAT-FB, SAT-FB1, DEAD
        sf = [t for t in fbs if info[t]["C"] == C and L(C, t) == n - 1]
        cnt["SATFB1_chk"] += 1
        if len(sf) > 1: fail(cnt, "SATFB1", name, a, C, sf)
        for t in sf:
            cnt["SATFB_chk"] += 1
            laterC = [s for s in Cst if s > t]
            if MUT == 3:
                if t + 1 != b: fail(cnt, "SATFB", name, t, "mut3")
            elif not (t + 1 == b or not laterC): fail(cnt, "SATFB", name, t)
            if laterC and st[t + 1]["Is"]: fail(cnt, "SATFB_Is", name, t)
            flat = st[t + 1]["Xi"] == st[t]["Xi"]
            if not flat: cnt["DEAD_nonflat"] += 1
            if t + 1 != b:
                cnt["DEAD_notlast"] += 1
                if len(EX) < 40 and cnt["DEAD_ex"] < 4: cnt["DEAD_ex"] += 1; EX.append(("DEAD", name, a, b, t, flat))
    # EP-C and REV
    runs = []; k = a
    while k <= b:
        j = k
        while j < b and not st[j]["fb"]: j += 1
        runs.append((k, j)); k = j + 1
    rev = 0
    for (x, y) in runs:
        ss = [s for s, _ in eps if x <= s <= y]
        rev += len(ss) - len({info[s]["C"] for s in ss})
    cnt["EPC_chk"] += 1
    if Nep > len(confs) * w2 + R0tot or R0tot > rev: fail(cnt, "EPC", name, a, Nep, len(confs), R0tot, rev)
    if N2 > NCONF2 * w2 + R0ge2: fail(cnt, "ASM2", name, a)
    cnt["SUM_R0"] += R0tot; cnt["SUM_NEP"] += Nep; cnt["SUM_NCONF"] += len(confs); cnt["SUM_R0GE2"] += R0ge2; cnt["SUM_NCONF2"] += NCONF2


def main(a):
    cnt = Counter(); rng = random.Random(1567); nst = int(os.environ.get("RANDSTARTS", "2"))
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
            if g.n > int(os.environ.get("MAXN", "34")): cnt["skip_big"] += 1; continue
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), HP.parse_start(g, sp) if sp else None)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
