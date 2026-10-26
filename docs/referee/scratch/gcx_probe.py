#!/usr/bin/env python3
"""REFEREE succ. 16 probe for P-N5-GCX-box21 (sha1 5a91bebb, pin l-si 02240121). Own engine only (rl_engine: SPEC; epr_probe.wval for
W = (sigma, tau)-play values; root_probe.firstD / route). No lane code. Phase: (lambda_Xi, tau) constant; U_c = lambda_Xi^{-1}(c).
 MS    MIG-SPLIT at every in-phase S4a transition t -> t+1, every class c, every u in DD_t n DD_{t+1}, every X-migration z: u' := first
       D_t-vertex of z's play exists, u' != u, u' in U_c (TC-CLASS), and (L) u' not in D_{t+1} or (S) an Even w on pi (z included) switches;
       in (S) z's (sigma, tau)-play changes. Counts L_only / S_only / both; per-vertex X-migrations per run (XPV).
 MSC   consequence per maximal fallback-free in-phase run S and per (c, u): X_u(S) <= #{t: a vertex of D n U_c leaves D} + #{t: a z in U_c
       changes its play}.
 UL    per run S with (ii) (lambda_W constant), U(S) at L = -1 (forbidden: COARSE_{-1} W(z) > COARSE_{-1} W(a), not Xi(z) > Xi(a); a switch
       into an edge forbidden at a state of [k'-n+1, k'-1] n S). Global C-intervals under two transition-local readings:
       R1: every c: A^c_{t+1} <= A^c_t; D_{t+1} = D_t; Delta_t(u) = Delta_{t+1}(u) for u in DD_t n DD_{t+1};  R2: R1 and DD_t = DD_{t+1}.
       K = transitions not in a good run. ULG: every U event at k' in a good run [a, b] has k' - a < n - 1 (DATA on the conjecture).
       ULa: |U(S)| <= n_E((n-1)(K+1)+K) (checked always; a failure with ULG holding would refute (a)); ULb: COARSE_{-1} W(x) changes
       <= (n-1)(1 + n_E((n-1)(K+1)+K)). R3: a gate u in DD at t1 < t2 of one R1-interval, not in DD at some state between, with
       Delta_{t1}(u) != Delta_{t2}(u) (the interval-level reading of "Delta constant" would cut there).
 RD    READING data (§5, not signed): in every R1-interval [a, b] and class c whose gates are all D-direct (D n U_c = DD at every state),
       for t >= a + |A^c_a| - 1: is M_t(sigmabar_t u) constant (RD_hvar counts changes) and is every X-migration before that time (RD_xlate)?
Mutations: MUT=1 MS without (S) (only (L) accepted); MUT=2 (S) with z excluded from pi; MUT=3 ULa without the "+K" cut term;
 MUT=4 ULG threshold 0 instead of n - 1 (every U event inside an interval counts).
Usage: gcx_probe.py rand N nmin nmax kmax seed | files[:start]...  (env RANDSTARTS 2, MAXN 40, NOS3)"""
import sys, os, random
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, dual_probe as D, epr_probe as E
from root_probe import firstD, route
EX = []
MUT = int(os.environ.get("MUT", "0"))


def fail(cnt, key, *info):
    cnt[key + "_FAIL"] += 1
    if len(EX) < 40: EX.append((key,) + info)


def play(nx, v):
    pre, cy = RE.lasso(nx, v)
    return tuple(pre), tuple(cy)


def coarse_m1(x): return (x[0], x[1])


def ckey(g, cx): return (g.rew[cx[0]], g.weight(cx[1]))


def load_start(g, path):
    b0 = RE.best_reward_start(g); s0, t0 = list(b0[0]), list(b0[1])
    for l in open(path):
        p_ = l.split()
        if p_ and p_[0] in ("SIGMA0", "TAU0"):
            for vw in p_[1:]:
                v, w = map(int, vw.split(":")); (s0 if p_[0] == "SIGMA0" else t0)[v] = w
    return s0, t0


def analyse(g, start, cnt, name):
    st = RE.run(g, start); n = g.n
    Q = {v for v in range(n) if g.owner[v] == 1}
    for x in st:
        x["nx"] = [x["s"][v] if g.owner[v] == 0 else x["t"][v] for v in range(n)]
        x["W"] = E.wval(g, x["s"], x["t"])
        x["D"] = frozenset(u for u in Q if x["sb"][u] != x["t"][u])
        x["fu"] = [firstD(g, x["s"], x["t"], x["D"], v) for v in range(n)]
        x["pl"] = [play(x["nx"], v) for v in range(n)]
    K = len(st); k = 0
    cnt["RUN_STATES"] += K
    while k < K:
        j = k; lam = tuple(v[0] for v in st[k]["Xi"])
        while j + 1 < K and tuple(v[0] for v in st[j + 1]["Xi"]) == lam and st[j + 1]["t"] == st[k]["t"]: j += 1
        r = k
        while r <= j:
            e = r
            while e < j and not st[e]["fb"]: e += 1
            if e > r: runS(g, st, r, e, lam, cnt, name)
            r = e + 1
        k = j + 1


def runS(g, st, a, b, lam, cnt, name):
    n = g.n; cnt["RUNS_S"] += 1
    tau = st[a]["t"]
    M = lambda t, z: g.weight(st[t]["Xi"][z][1])
    classes = sorted(set(lam))
    U = {c: {v for v in range(n) if lam[v] == c} for c in classes}
    A = {(c, t): {v for v in U[c] if st[t]["fu"][v] is None} for c in classes for t in range(a, b + 1)}
    def DD(c, t): return {u for u in st[t]["D"] if u in U[c] and st[t]["sb"][u] in A[c, t] and tau[u] in A[c, t]}
    DDs = {(c, t): DD(c, t) for c in classes for t in range(a, b + 1)}
    Dl = lambda t, u: M(t, tau[u]) - M(t, st[t]["sb"][u])
    Ru = lambda c, t, u: {z for z in U[c] if st[t]["fu"][z] == u}
    plchg = {t: {z for z in range(n) if st[t]["pl"][z] != st[t + 1]["pl"][z]} for t in range(a, b)}
    xmig = defaultdict(set)  # (c, u) -> transitions
    xpv = Counter(); xtimes = defaultdict(list)
    for t in range(a, b):
        s0, s1 = st[t], st[t + 1]
        for c in classes:
            for u in DDs[c, t] & DDs[c, t + 1]:
                R1 = Ru(c, t + 1, u); R0 = Ru(c, t, u)
                for z in R1 - (R0 | A[c, t]):
                    cnt["MS_chk"] += 1; xmig[c, u].add(t); xpv[z] += 1; xtimes[c].append((t, z, u))
                    up = s0["fu"][z]
                    if up is None or up == u: fail(cnt, "MS_up", name, t, c, z, u); continue
                    if up not in U[c]: fail(cnt, "MS_tcclass", name, t, c, z, up)
                    L = up not in s1["D"]
                    pi = route(g, s0["s"], s0["t"], s0["D"], z)
                    if MUT == 2: pi = [w for w in pi if w != z]
                    S = any(g.owner[w] == 0 and s0["s"][w] != s1["s"][w] for w in pi)
                    if MUT == 1: S = False
                    if L and S: cnt["MS_both"] += 1
                    elif L: cnt["MS_L_only"] += 1
                    elif S: cnt["MS_S_only"] += 1
                    if S and g.owner[z] == 0 and s0["s"][z] != s1["s"][z]: cnt["MS_S_zswitch"] += 1
                    if not (L or S): fail(cnt, "MS", name, t, c, z, u, up)
                    if S and z not in plchg[t]: fail(cnt, "MS_Splay", name, t, c, z)
    if xpv: cnt["MAX_XPV"] = max(cnt["MAX_XPV"], max(xpv.values()))
    # MSC
    for (c, u), ts in xmig.items():
        leave = sum(1 for t in range(a, b) if any(v in U[c] and v not in st[t + 1]["D"] for v in st[t]["D"]))
        pc = sum(1 for t in range(a, b) if plchg[t] & U[c])
        cnt["MSC_chk"] += 1; cnt["MAX_Xu"] = max(cnt["MAX_Xu"], len(ts))
        if len(ts) > leave + pc: fail(cnt, "MSC", name, a, c, u, len(ts), leave, pc)
    # UL-RED
    lamW = [tuple(x[0] for x in st[t]["W"]) for t in range(a, b + 1)]
    if any(l != lamW[0] for l in lamW): cnt["UL_skip_not_ii"] += 1; return
    Ev = [v for v in range(n) if g.owner[v] == 0]; nE = len(Ev)
    W = {t: st[t]["W"] for t in range(a, b + 1)}; Xi = {t: st[t]["Xi"] for t in range(a, b + 1)}
    forb = set()
    for t in range(a, b + 1):
        for x in Ev:
            aa = st[t]["s"][x]
            for z in g.succ[x]:
                if z != aa and ckey(g, coarse_m1(W[t][z])) > ckey(g, coarse_m1(W[t][aa])) and not g.key(Xi[t][z]) > g.key(Xi[t][aa]):
                    forb.add((t, x, z))
    Uev = []
    for kk in range(a, b):
        for y in Ev:
            z = st[kk + 1]["s"][y]
            if z != st[kk]["s"][y] and any((f, y, z) in forb for f in range(max(a, kk - n + 1), kk)): Uev.append((kk, y, z))
    cnt["UL_runs"] += 1; cnt["U_events"] += len(Uev); cnt["MAX_U"] = max(cnt["MAX_U"], len(Uev))
    def good(t, strict):
        if st[t]["D"] != st[t + 1]["D"]: return False
        for c in classes:
            if not A[c, t + 1] <= A[c, t]: return False
            d0, d1 = DDs[c, t], DDs[c, t + 1]
            if strict and d0 != d1: return False
            if any(Dl(t, u) != Dl(t + 1, u) for u in d0 & d1): return False
        return True
    chg = {x: sum(1 for t in range(a, b) if coarse_m1(W[t][x]) != coarse_m1(W[t + 1][x])) for x in range(n)}
    for tag, strict in (("R1", False), ("R2", True)):
        gd = [good(t, strict) for t in range(a, b)]
        Kc = gd.count(False); cnt["MAX_K_" + tag] = max(cnt["MAX_K_" + tag], Kc)
        start_of = {}; s_ = None; ints = []
        for i, t in enumerate(range(a, b)):
            if gd[i]:
                if s_ is None: s_ = t
                start_of[t] = s_
            else:
                if s_ is not None: ints.append((s_, t)); s_ = None
        if s_ is not None: ints.append((s_, b))
        if len(ints) > Kc + 1: fail(cnt, "ULcount_" + tag, name, a, len(ints), Kc)
        viol = [(kk, y, z, kk - start_of[kk]) for (kk, y, z) in Uev if kk in start_of and kk - start_of[kk] >= (0 if MUT == 4 else n - 1)]
        inside = [(kk - start_of[kk]) for (kk, y, z) in Uev if kk in start_of]
        if inside: cnt["MAX_ULG_idx_minus_n1_" + tag] = max(cnt["MAX_ULG_idx_minus_n1_" + tag], max(inside) - (n - 1) + 1000)
        if ints: cnt["MAX_GCI_len_minus_n1_" + tag] = max(cnt["MAX_GCI_len_minus_n1_" + tag], max(e - s for s, e in ints) - (n - 1) + 1000)
        if ints and tag == "R1" and max(e - s for s, e in ints) >= n - 1 and len(EX) < 40: EX.append(("GCI_LONG", name, n, [(s, e) for s, e in ints if e - s >= n - 1]))
        cnt["ULG_inside_" + tag] += len(inside)
        holds = not viol
        if not holds: fail(cnt, "ULG_" + tag, name, a, viol[:2])
        bnd = nE * ((n - 1) * (Kc + 1) + (0 if MUT == 3 else Kc))
        cnt["ULa_chk_" + tag] += 1
        if len(Uev) > bnd: fail(cnt, ("ULa_" if holds else "ULa_noULG_") + tag, name, a, len(Uev), bnd)
        for x in range(n):
            cnt["ULb_chk_" + tag] += 1
            if chg[x] > (n - 1) * (1 + bnd): fail(cnt, ("ULb_" if holds else "ULb_noULG_") + tag, name, a, x, chg[x])
        if tag == "R1":
            for (s, e) in ints:
                for c in classes:
                    gates = set().union(*[st[t]["D"] & U[c] for t in range(s, e + 1)])
                    for u in gates:
                        ts = [t for t in range(s, e + 1) if u in DDs[c, t]]
                        for i in range(len(ts) - 1):
                            if ts[i + 1] > ts[i] + 1 and Dl(ts[i], u) != Dl(ts[i + 1], u):
                                cnt["R3_diff"] += 1
                                if len(EX) < 40: EX.append(("R3", name, s, e, c, u, ts[i], ts[i + 1], Dl(ts[i], u), Dl(ts[i + 1], u)))
                        if ts and (ts[-1] - ts[0] + 1) != len(ts): cnt["R3_reentry"] += 1
                    pure = all(st[t]["D"] & U[c] == DDs[c, t] for t in range(s, e + 1))
                    if not pure or not (st[s]["D"] & U[c]): continue
                    cnt["RD_pure_ints"] += 1
                    fz = s + max(len(A[c, s]) - 1, 0)
                    if fz < e: cnt["RD_pure_pastfreeze"] += 1
                    for u in st[s]["D"] & U[c]:
                        hv = [M(t, st[t]["sb"][u]) for t in range(fz, e + 1)]
                        if len(set(hv)) > 1: cnt["RD_hvar"] += 1
                    for (t, z, u) in xtimes[c]:
                        if s <= t < e:
                            cnt["RD_xmig"] += 1
                            if t >= fz: cnt["RD_xlate"] += 1


def main(a):
    cnt = Counter(); rng = random.Random(1616); nst = int(os.environ.get("RANDSTARTS", "2"))
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
            ex = load_start(g, sp) if sp else None
            do(g, os.path.relpath(path), random.Random(os.path.relpath(path)), ex)
    for k in sorted(cnt):
        v = cnt[k] - 1000 if k.startswith("MAX_ULG") or k.startswith("MAX_GCI") else cnt[k]
        print(k, v)
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
