#!/usr/bin/env python3
"""REFEREE succ. 17 probe for packet P-N5-REL (docs/si/P-N5-REL-box25.md, sha1 f79300a2..., freeze l-si 07f19760). Own engine only
(rl_engine; cycles / play from depth_probe.py; start parsing from core_probe.py). No lane code.
RUN S: maximal fallback-free stretch of one phase ((lambda_Xi, tau) constant).
 GR     Lemma GATE-RISE at every transition of S and Odd u with a sigmabar change: classify CLEAN / TIE / CYC / THRU; clean => Xi_{t+1}(u) > Xi_t(u)
 CNT    per run and u: CH_S(u) <= XR_S(u) + TIE + CYC + THRU; G(S) <= sum_u (...)
 REL    per end state b of S: X_b, RO_b, CW_b, CH_b, T, V^W_b, V^H_b; a := least state of S with [a, b] REL-admissible; depths dW / dH / d; (H4'_rel);
        GEN_W in its used form for v in X_b - T. Checks: SDV (settling on V^W / V^H from a + dW / a + dH), SIG (sigma_t = sigma_b on
        [a + max_{Q-T} d, b]), LEN (b - a <= max_{Q-T} d <= |Even - T| <= n - 1)
 SPLIT  per run: segments from the end; SEG; |S| <= SEG n - 1 if (H4'_rel), GEN_W at every b_i; every cut is a sigmabar change on RO_{b_i}
        or an appearance of a CW_{b_i} u CH_{b_i} cycle; SEG - 1 <= G(S) + CF(S)
 REMK   REL's a <= the a of STATIC-DEPTH' (sigmabar constant everywhere, all end cycles persist)  (Remark, not to sign; a sanity check)
Mutations: MUT=1 SDV from a + d - 1; MUT=2 GATE-RISE demanded also for THRU changes; MUT=3 also for TIE changes;
 MUT=4 REL-admissible without the sigmabar-on-RO_b condition; MUT=5 X_b := Q only (no closure).
Usage: rel_probe.py list FILE BASE | files...   (env RANDSTARTS 1, MAXN 60)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E, core_probe as CP
from depth_probe import cycles, play
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def lassoset(nx, v):
    pre, cy = RE.lasso(nx, v); return pre, cy


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    for x in st:
        x["nxH"] = [x["s"][v] if g.owner[v] == 0 else x["sb"][v] for v in range(n)]
        x["nxW"] = [x["s"][v] if g.owner[v] == 0 else x["t"][v] for v in range(n)]
        x["W"] = E.wval(g, x["s"], x["t"])
        x["cyc"] = (cycles(x["nxW"]), cycles(x["nxH"]))
        x["oncyc"] = (set(v for c in x["cyc"][0] for v in c), set(v for c in x["cyc"][1] for v in c))
        x["Isv"] = {}
        for (v, w) in x["Is"]: x["Isv"].setdefault(v, set()).add(w)
    K = len(st); k = 0
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        r = k
        while r <= j:
            e = r
            while e < j and not st[e]["fb"]: e += 1
            run(g, st, r, e, cnt, name)
            r = e + 1
        k = j + 1


def gate_rise(g, st, s0, e, cnt, name):
    n = g.n; Odd = [u for u in range(n) if g.owner[u] == 1 and len(g.succ[u]) >= 2]
    CH = Counter(); XR = Counter(); TIE = Counter(); CYC = Counter(); THRU = Counter(); G = 0
    for t in range(s0, e):
        x0, x1 = st[t], st[t + 1]
        if any(x0["sb"][u] != x1["sb"][u] for u in Odd): G += 1
        for u in Odd:
            if x0["Xi"][u] != x1["Xi"][u]: XR[u] += 1
            y1, y2 = x0["sb"][u], x1["sb"][u]
            if y1 == y2: continue
            CH[u] += 1
            i_ok = u not in x0["oncyc"][1] and u not in x1["oncyc"][1]
            pre, cy = lassoset(x0["nxH"], y2); ii_ok = u not in pre and u not in cy
            iii_ok = x0["Xi"][y1] != x0["Xi"][y2]
            if not i_ok:
                CYC[u] += 1; kind = "CYC"
                if u not in x0["oncyc"][1] and x1["Xi"][u][0] != u and ii_ok and iii_ok:   # (i) fails only at t + 1, u not its cycle node
                    cnt["GR_CYC1"] += 1
                    if not g.key(x1["Xi"][u]) > g.key(x0["Xi"][u]): cnt["GR_CYC1_norise"] += 1
            elif not ii_ok: THRU[u] += 1; kind = "THRU"
            elif not iii_ok: TIE[u] += 1; kind = "TIE"
            else: kind = "CLEAN"
            cnt["GR_" + kind] += 1
            demand = kind == "CLEAN" or (MUT == 2 and kind == "THRU") or (MUT == 3 and kind == "TIE")
            if demand:
                cnt["GR_chk"] += 1
                if not g.key(x1["Xi"][u]) > g.key(x0["Xi"][u]): fail(cnt, "GR" + ("_MUT%d" % MUT if MUT in (2, 3) and kind != "CLEAN" else ""), name, t, u, kind)
    tot = 0
    for u in Odd:
        cnt["CNT_chk"] += 1
        if CH[u] > XR[u] + TIE[u] + CYC[u] + THRU[u]: fail(cnt, "CNT", name, s0, u)
        tot += XR[u] + TIE[u] + CYC[u] + THRU[u]
    if G > tot: fail(cnt, "CNTG", name, s0)
    return G


def sets_at(g, x):
    n = g.n
    Q = [v for v in range(n) if g.owner[v] == 0 and len(g.succ[v]) >= 2]
    X = set(Q); stack = list(Q)
    if MUT != 5:
        while stack:
            v = stack.pop()
            for key in ("nxW", "nxH"):
                pre, cy = lassoset(x[key], v)
                for w in pre + cy:
                    if g.owner[w] == 0 and w not in X: X.add(w); stack.append(w)
    VW, VH, RO, CW, CHc = set(), set(), set(), set(), set()
    for v in X:
        pre, cy = lassoset(x["nxW"], v); VW.update(pre); VW.update(cy)
        m = min(cy); i = cy.index(m); CW.add(tuple(cy[i:] + cy[:i]))
        pre, cy = lassoset(x["nxH"], v); VH.update(pre); VH.update(cy)
        RO.update(w for w in pre + cy if g.owner[w] == 1)
        m = min(cy); i = cy.index(m); CHc.add(tuple(cy[i:] + cy[:i]))
    TW = {v for c in CW for v in c}; TH = {v for c in CHc for v in c}
    return Q, X, VW, VH, RO, frozenset(CW), frozenset(CHc), TW, TH


def admissible(st, a, b, RO, CW, CHc):
    xb = st[b]
    for t in range(a, b + 1):
        if MUT != 4 and any(st[t]["sb"][u] != xb["sb"][u] for u in RO): return False
        if not CW <= st[t]["cyc"][0] or not CHc <= st[t]["cyc"][1]: return False
    return True


def depths(g, x, VW, VH, TW, TH):
    memo = {}; onstack = set()
    def rec(v, f):
        key = (v, f)
        if key in memo: return memo[key]
        if (f == 'W' and v in TW) or (f == 'H' and v in TH): return 0
        if key in onstack: raise ValueError
        onstack.add(key)
        if g.owner[v] == 1: val = rec(x["t"][v], 'W') if f == 'W' else rec(x["sb"][v], 'H')
        else:
            y = x["s"][v]
            if v in TH and v not in TW: val = rec(y, 'W') if f == 'W' else 0
            elif v in TW and v not in TH: val = rec(y, 'H') if f == 'H' else 0
            else: val = 1 + max(rec(y, 'W'), rec(y, 'H'))
        onstack.discard(key); memo[key] = val; return val
    try:
        dW = {v: rec(v, 'W') for v in VW}; dH = {v: rec(v, 'H') for v in VH}
    except (ValueError, RecursionError): return None
    return dW, dH


def genw_used(g, st, a, b, vs):
    Wb = st[b]["W"]
    for t in range(a, b + 1):
        for v in vs:
            if st[t]["W"][v] == Wb[v]:
                p1, p2 = play(st[t]["nxW"], v), play(st[b]["nxW"], v)
                if p1 != p2 and set(p1[1]) == set(p2[1]): return False
    return True


def rel_at(g, st, s0, b, cnt, name, check=True):
    """returns (a, ok) where ok = (H4'_rel) and GEN_W(used) hold"""
    n = g.n; x = st[b]
    Q, X, VW, VH, RO, CW, CHc, TW, TH = sets_at(g, x)
    a = b
    while a > s0 and admissible(st, a - 1, b, RO, CW, CHc): a -= 1
    dd = depths(g, x, VW, VH, TW, TH)
    if dd is None: cnt["H4rel_fail"] += 1; return a, False, None
    dW, dH = dd; T = TW | TH
    gen = genw_used(g, st, a, b, [v for v in X if v not in T])
    if not gen: cnt["GENW_used_fail"] += 1
    if not check or a == b: return a, gen, (dW, dH, Q, T, VW, VH)
    cnt["REL_chk"] += 1
    QT = [v for v in Q if v not in T]; md = max((dW[v] for v in QT), default=0)
    evout = sum(1 for v in range(n) if g.owner[v] == 0 and v not in T)
    if len(X) > len(Q): cnt["REL_X_gt_Q"] += 1
    if any(st[t]["sb"][u] != x["sb"][u] for t in range(a, b + 1) for u in range(n) if g.owner[u] == 1): cnt["REL_sigmabar_moves_off_RO"] += 1
    if not (md <= evout <= n - 1): fail(cnt, "LENcap", name, a, b)
    if b - a > md:
        if gen: fail(cnt, "LEN", name, a, b, md)
        else: cnt["LEN_over_nonGEN"] += 1
    if b - a == md: cnt["REL_sharp"] += 1
    cnt["MAX_REL_len"] = max(cnt["MAX_REL_len"], b - a)
    for t in range(a + md, b + 1):
        cnt["SIG_chk"] += 1
        if st[t]["s"] != x["s"] and gen: fail(cnt, "SIG", name, a, b, t)
    sub = 1 if MUT == 1 else 0
    for dom, dd_, key in ((VW, dW, "nxW"), (VH, dH, "nxH")):
        for v in dom:
            pb = play(x[key], v)
            for t in range(max(a, a + dd_[v] - sub), b + 1):
                cnt["SDV_chk"] += 1
                if play(st[t][key], v) != pb:
                    if gen: fail(cnt, "SDV", name, a, b, v, key, t, dd_[v])
                    else: cnt["SDV_nonGEN"] += 1
                    break
    # Remark sanity: STATIC-DEPTH' start
    a2 = b
    while a2 > s0 and st[a2 - 1]["sb"] == x["sb"] and all(x["cyc"][f] <= st[a2 - 1]["cyc"][f] for f in (0, 1)) and \
            all(x["cyc"][f] <= st[tt]["cyc"][f] for tt in range(a2 - 1, b + 1) for f in (0, 1)): a2 -= 1
    cnt["REMK_chk"] += 1
    if a2 < a and MUT not in (4, 5): fail(cnt, "REMK", name, a2, a, b)
    if a < a2: cnt["REL_longer_than_SDp"] += 1
    return a, gen, (dW, dH, Q, T, VW, VH)


def run(g, st, s0, e, cnt, name):
    n = g.n; cnt["RUNS_S"] += 1
    G = gate_rise(g, st, s0, e, cnt, name)
    for b in range(s0, e + 1): rel_at(g, st, s0, b, cnt, name)
    # REL-SPLIT
    segs = []; bi = e; allok = True
    while bi >= s0:
        ai, ok, _ = rel_at(g, st, s0, bi, Counter(), name, check=False)
        if not ok: allok = False
        segs.append((ai, bi)); bi = ai - 1
    segs.reverse(); SEG = len(segs)
    CF = sum(1 for t in range(s0, e) if any(not st[t + 1]["cyc"][f] <= st[t]["cyc"][f] for f in (0, 1)))
    cnt["SPLIT_chk"] += 1; cnt["MAX_SEG"] = max(cnt["MAX_SEG"], SEG)
    cnt["MAX_SEG_x100_over_n"] = max(cnt["MAX_SEG_x100_over_n"], 100 * SEG // n)
    if e - s0 != sum(b_ - a_ for a_, b_ in segs) + SEG - 1: fail(cnt, "SPLITsum", name, s0, e)
    for (a_, b_) in segs[1:]:
        _, X, VW, VH, RO, CW, CHc, TW, TH = sets_at(g, st[b_])
        sbchg = any(st[a_ - 1]["sb"][u] != st[a_]["sb"][u] for u in RO)
        app = any(c not in st[a_ - 1]["cyc"][0] for c in CW) or any(c not in st[a_ - 1]["cyc"][1] for c in CHc)
        cnt["CUT_chk"] += 1
        if not (sbchg or app): fail(cnt, "CUT", name, a_)
    if SEG - 1 > G + CF: fail(cnt, "SEGcount", name, s0, e, SEG, G, CF)
    if allok:
        cnt["SPLIT_hyp"] += 1
        if e - s0 > SEG * n - 1: fail(cnt, "SPLIT", name, s0, e, SEG)
    cnt["MAX_RUN"] = max(cnt["MAX_RUN"], e - s0)


def main(a):
    cnt = Counter(); nst = int(os.environ.get("RANDSTARTS", "1")); rng = random.Random(2526)
    def do(g, name, r, extra=None):
        starts = ([extra] if extra else []) + ([RE.best_reward_start(g)] if (not extra or nst > 0) else []) + \
                 [D.rand_start(g, r) for _ in range(nst)]
        for j, s0 in enumerate(starts):
            cnt["RUNS"] += 1; analyse(g, s0, cnt, "%s/%d" % (name, j))
    if a[0] == "rand":
        N, lo, hi, km, seed = map(int, a[1:6]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(km, nn - 1))), "rand%d" % i, rng)
    elif a[0] == "list":
        base = a[2]
        for l in open(a[1]):
            p = l.split()
            if not p: continue
            g = RE.parse(os.path.join(base, p[0]))
            if g.n > int(os.environ.get("MAXN", "60")): cnt["skip_big"] += 1; continue
            ex = CP.parse_start(g, os.path.join(base, p[1])) if len(p) > 1 else None
            cnt["GAMES"] += 1; do(g, p[0], random.Random(p[0]), ex)
    else:
        for path in a:
            if path.endswith(".start"): continue
            g = RE.parse(path)
            if g.n > int(os.environ.get("MAXN", "60")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"
            ex = CP.parse_start(g, sp) if os.path.exists(sp) else None
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt): print(k, cnt[k])
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
