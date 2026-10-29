#!/usr/bin/env python3
r"""REFEREE-2 successor 19 (Opus 5.5, D15): mechanical check of P-N5-FBCK (docs/new/P-N5-FBCK-box49.md, sha1 7747ecf2 @ l-new 0e63596d).
State loop = my lane's SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py = SPEC S1, read-only); Xi = my own play value of (sigma, sigmabar)
(R2-N5-RUND/rund_check.state_info, ENGXI). Lane tools (experiments/new/box49/fbconf.py, quotecheck3.py) NOT run or imported.
K := vertices reachable (>= 0 edges) from an Even vertex of out-degree >= 2; n_K = |K|; Q_K = Q cap K; K-configuration C = sigmabar|Q_K.
Per phase P (lambda_Xi, tau constant) with an in-phase fallback, per K-configuration C of a fallback source: H^K_C = G[K] with Odd v in K cut to
C(v) (taken from the first source's sigmabar); LEV^K_C(k) EXACT at every state of P by enumeration of the simple H^K_C-paths from x in K to a
cycle node of lambda, cap n_K - 1 (budget per (phase, C); over budget -> UNK, skipped, counted).
Checks (each must be 0):
  K1      K closed under successors; the honest play from x in K stays in K; lambda(x) in K
  K2      Even x not in K has out-degree 1, and I_sigma(x) = 0 at every state;  K3  K empty => no in-phase fallback
  LEV0    LEV^K_C >= 0 at every state;  MONO  LEV^K_C non-decreasing on P
  RISE    FB-RISE^K at every source that is a K-C-state;  ODDC  its Odd case at every K-C-state (Xi_t(x) >= value(r) for Odd x in K, |r| <=
          min(LEV+1, n_K-1));  XIB  at K-C-states Xi_t(x) <= B^K_C(x) and is a simple-path value
  SAT     LEV = n_K - 1 at a K-C-state => Xi_t = B^K_C on K; Xi constant on K from it to every later K-C-state
  SATFB   saturated source t: t + 1 is the last state of P or no K-C-state of P after t; and if a later K-C-state exists, I_sigma_{t+1} = 0
  SATFB1  <= 1 saturated source per (P, C);  CNT  per C: sources <= n_K;  THM  f <= n_K |C^K_f|;  COR1  n_K |C^K_f| <= n |C_f|, |C^K_f| <= |C_f|
Controls (FBCK_MUT; counted as MUT_* failures, expected to bite): plus2 (RISE with +2); tau (Odd vertices of Q_K cut to tau, not C);
open1 (K replaced by K' = Even choice vertices + their successors, NOT closed; LEV over G[K'], cap |K'| - 1; SAT/SATFB/RISE re-run);
nk1 (THM with (n_K - 1) per C).
Usage: fbck_check.py files list.txt [runs] | pairs list.txt prefix | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats
MUT = os.environ.get("FBCK_MUT", "")
BUDGET = int(os.environ.get("BUDGET", "400000"))


class Over(Exception): pass


def reach_set(g, srcs):
    seen, st = set(srcs), list(srcs)
    while st:
        x = st.pop()
        for y in g.succ[x]:
            if y not in seen: seen.add(y); st.append(y)
    return frozenset(seen)


def frame_K(g):
    n = g.n
    E2 = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    if MUT == "open1": return frozenset(E2) | frozenset(y for v in E2 for y in g.succ[v])
    return reach_set(g, E2)


def simple_values(ctx, frame, cyc, K, budget, D=None):
    """per x in K: list of (edges, key, path) over simple paths of frame[K] from x to a cycle node (paths may pass cycle nodes);
    with D: only paths with <= D edges (exact for that length range)."""
    g, E = ctx.g, ctx.E
    out, cnt = {}, [0]
    for x in K:
        res = []
        def dfs(y, vis, path):
            cnt[0] += 1
            if cnt[0] > budget: raise Over()
            if y in cyc:
                m = 0
                for p in path[:-1]:
                    if E.rank[p] > E.rank[y]: m |= E.bit[p]
                res.append((len(path) - 1, E.key((y, m, len(path) - 1)), tuple(path)))
            if D is not None and len(path) - 1 >= D: return
            for z in ([frame[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))):
                if z in K and z not in vis:
                    vis.add(z); path.append(z); dfs(z, vis, path); path.pop(); vis.discard(z)
        dfs(x, {x}, [x])
        out[x] = res
    return out


def table(sv, K, cap):
    B = {}
    for x in K:
        best = {}
        for e, k, _ in sv[x]:
            if e not in best or k > best[e]: best[e] = k
        row, cur = [], None
        for j in range(cap + 1):
            if j in best and (cur is None or best[j] > cur): cur = best[j]
            row.append(cur)
        B[x] = row
    return B


def lev(ctx, B, vals, xs, cap):
    L = -1
    for j in range(cap + 1):
        if all(B[x][j] is None or ctx.key(vals[x]) >= B[x][j] for x in xs): L = j
        else: break
    return L


def run_game(gp, s, t, st, name):
    g, n = gp, gp.n
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp)
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    K = frame_K(g)
    # K1, K2 (static and per state)
    if MUT != "open1":
        if any(y not in K for x in K for y in g.succ[x]): st.bad("K1", f"{name}: not closed")
    for x in range(n):
        if g.owner[x] == 0 and x not in K and len(set(g.succ[x])) != 1: st.bad("K2", f"{name}: x {x}")
    for k, S in enumerate(I):
        if any(x not in K for x, _ in S["Is"]): st.bad("K2", f"{name}@{k}: I_sigma outside K")
        if MUT != "open1":
            for x in K:
                path, _ = R.lasso(S["hn"], x)
                if any(y not in K for y in path) or S["lamX"][x] not in K: st.bad("K1", f"{name}@{k}: x {x}")
    st.inc("nK_total", len(K)); st.inc("n_total", n)
    key = [(I[k]["lamX"], I[k]["tu"]) for k in range(len(I))]
    k0 = 0
    while k0 < len(I):
        k1 = k0
        while k1 + 1 < len(I) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(ctx, g, I, fbs, k0, k1, K, st, name)
        k0 = k1 + 1


def check_phase(ctx, g, I, fbs, a, b, K, st, name):
    n, E = ctx.n, ctx.E
    st.inc("phases")
    fbk = [k for k in range(a, b) if fbs[k]]
    f = len(fbk)
    if not K:
        st.inc("K_empty_phases")
        if f: st.bad("K3", f"{name}@{a}: f {f} with K empty")
        return
    if not fbk: return
    nK = len(K); cap = nK - 1
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    QK = [q for q in Q if q in K]
    lam = I[a]["lamX"]; tu = I[a]["tu"]
    cyc = frozenset(v for v in range(n) if lam[v] == v)
    confK = {k: tuple(I[k]["hn"][q] for q in QK) for k in range(a, b + 1)}
    conf = {k: tuple(I[k]["hn"][q] for q in Q) for k in range(a, b + 1)}
    CfK = set(confK[t] for t in fbk); Cf = set(conf[t] for t in fbk)
    st.inc("fb_phases"); st.inc("f_total", f); st.inc("CfK_total", len(CfK)); st.inc("Cf_total", len(Cf))
    st.mxr("max_CfK", (len(CfK), name, a, f, nK, n))
    if len(CfK) < len(Cf): st.inc("phases_CfK_below_Cf")
    if nK < n: st.inc("fb_phases_nK_below_n")
    if f > nK * len(CfK): st.bad("THM", f"{name}@{a}: f {f} > {nK} * {len(CfK)}")
    if MUT == "nk1" and f > (nK - 1) * len(CfK): st.bad("MUT_nk1", f"{name}@{a}")
    if MUT != "open1" and (nK * len(CfK) > n * len(Cf) or len(CfK) > len(Cf)): st.bad("COR1", f"{name}@{a}")
    st.mxr("max_f_over_nKCfK", (round(f / (nK * len(CfK)), 3), name, a, f, nK, len(CfK)))
    Ks = sorted(K); oddK = [x for x in Ks if g.owner[x] == 1]
    for C in sorted(CfK):
        src = [t for t in fbk if confK[t] == C]
        cst = [k for k in range(a, b + 1) if confK[k] == C]
        frame = list(I[src[0]]["hn"]) if MUT != "tau" else list(tu)
        st.mxr("max_src_per_C_over_nK", (round(len(src) / nK, 3), name, a, len(src), nK))
        if len(src) > nK: st.bad("CNT", f"{name}@{a}: {len(src)} sources > n_K {nK}")
        try:
            sv = simple_values(ctx, frame, cyc, K, BUDGET)
        except Over:
            deep(ctx, g, I, cst, src, frame, cyc, K, Ks, oddK, cap, a, b, st, name); continue
        st.inc("C_checked")
        B = table(sv, Ks, cap)
        LEV = {k: lev(ctx, B, I[k]["xi"], Ks, cap) for k in range(a, b + 1)}
        for k in range(a, b + 1):
            if LEV[k] < 0: st.bad("LEV0", f"{name}@{k}")
        for k in range(a, b):
            if LEV[k + 1] < LEV[k]: st.bad("MONO", f"{name}@{k}: {LEV[k]} -> {LEV[k + 1]}")
        for t in cst:
            st.inc("Kstates")
            xi = I[t]["xi"]
            LO = lev(ctx, B, xi, oddK, cap) if oddK else cap
            if LO < min(LEV[t] + 1, cap): st.bad("ODDC", f"{name}@{t}: LEV {LEV[t]} odd {LO}")
            for x in Ks:
                kx = ctx.key(xi[x])
                if B[x][cap] is not None and kx > B[x][cap]: st.bad("XIB", f"{name}@{t}: x {x}")
                if MUT != "open1" and not any(kv == kx for _, kv, _ in sv[x]): st.bad("XIB_path", f"{name}@{t}: x {x}")
        sat = [t for t in cst if LEV[t] >= cap]
        for t in sat:
            st.inc("SAT_checks")
            if any(B[x][cap] is not None and ctx.key(I[t]["xi"][x]) != B[x][cap] for x in Ks): st.bad("SAT", f"{name}@{t}")
            for t2 in cst:
                if t2 > t and any(I[k]["xi"][x] != I[t]["xi"][x] for k in range(t, t2 + 1) for x in Ks): st.bad("SAT_const", f"{name}@{t}..{t2}")
        uns = [t for t in src if LEV[t] <= cap - 1]; sats = [t for t in src if LEV[t] >= cap]
        st.inc("sources", len(src)); st.inc("sources_unsat", len(uns)); st.inc("sources_sat", len(sats))
        if len(sats) > 1: st.bad("SATFB1", f"{name}@{a}: {len(sats)}")
        for t in sats:
            st.inc("SATFB_checks")
            later = [k for k in cst if k > t]
            if t + 1 != b and later: st.bad("SATFB", f"{name}@{t}: later K-C-state {later[0]}, phase ends {b}")
            if later:
                st.inc("SATFB_with_later")
                if I[t + 1]["Is"]: st.bad("SATFB_Is", f"{name}@{t}")
            if t + 1 == b: st.inc("SATFB_lastcase")
        for t in src:
            j = min(LEV[t] + (2 if MUT == "plus2" else 1), cap)
            st.inc("RISE_checks")
            if j > LEV[t]: st.inc("RISE_needed")
            if LEV[t + 1] < j: st.bad("RISE", f"{name}@{t}: {LEV[t]} -> {LEV[t + 1]} (n_K {nK})")


def deep(ctx, g, I, cst, src, frame, cyc, K, Ks, oddK, cap, a, b, st, name):
    """iterative deepening: largest D <= cap with all paths <= D edges within budget; LEVc = min(LEV, D) exact. Decides MONO (capped),
    LEV0, RISE where LEVc(t) <= D - 1, ODDC where LEVc(t) <= D - 1. SAT / SATFB undecided (need D = cap)."""
    best = None
    for D in range(1, cap + 1):
        try: sv = simple_values(ctx, frame, cyc, K, BUDGET, D)
        except Over: break
        best = (D, sv)
    if best is None:
        st.inc("UNK_C"); st.inc("UNK_C_sources", len(src)); return
    D, sv = best
    st.inc("DEEP_C"); st.mxr("deep_D_min", (-D, name, a))
    B = table(sv, Ks, D)
    L = {k: lev(ctx, B, I[k]["xi"], Ks, D) for k in range(a, b + 1)}
    for k in range(a, b + 1):
        if L[k] < 0: st.bad("LEV0", f"{name}@{k} (deep)")
    for k in range(a, b):
        if L[k + 1] < L[k]: st.bad("MONO", f"{name}@{k} (deep)")
    for t in cst:
        if L[t] <= D - 1:
            st.inc("Kstates_deep")
            LO = lev(ctx, B, I[t]["xi"], oddK, D) if oddK else D
            if LO < min(L[t] + 1, cap): st.bad("ODDC", f"{name}@{t} (deep)")
    for t in src:
        if L[t] <= D - 1:
            st.inc("RISE_checks_deep")
            if L[t + 1] < min(L[t] + (2 if MUT == "plus2" else 1), cap, D): st.bad("RISE", f"{name}@{t} (deep) {L[t]} -> {L[t + 1]}")
        else: st.inc("RISE_undecided")


def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(4919)
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "pairs":
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(a[2], line[0]))
            if len(line) > 1:
                s, t = R.read_start(gp, os.path.join(a[2], line[1]))
                for v in range(gp.n):
                    x = s if gp.owner[v] == 0 else t
                    if x[v] not in gp.succ[v]: st.inc("INVALID_START_ENTRIES"); x[v] = gp.succ[v][0]
            else: s, t = R.starts(gp, 0, None)
            run_game(gp, s, t, st, line[0] + ("#start" if len(line) > 1 else "#S3"))
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); k = int(a[5]) if len(a) > 5 else 2; ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "dress":   # dress N nmin nmax seed k h [starts]: base random game + h new vertices (no old -> new edges;
        # new Even vertices out-degree 1, new Odd vertices out-degree 2-3; targets: old vertices or earlier new ones)
        N, nmin, nmax, seed, k, h = map(int, a[1:7]); ns = int(a[7]) if len(a) > 7 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            g0 = DC.rand_game(rng, nn, "kO") if k == 0 else H.rand_kO(rng, nn, k)
            prio, owner, succ = list(g0.prio), list(g0.owner), [list(x) for x in g0.succ]
            for j in range(h):
                v = nn + j; o = rng.randint(0, 1)
                d = 1 if o == 0 else rng.randint(2, 3)
                tg = sorted(set(rng.randrange(0, v) for _ in range(d)))
                prio.append(rng.randint(0, max(prio) + 1)); owner.append(o); succ.append(tg)
            gp = pg.Game(prio, owner, succ)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"dress{seed}:{i}#{r}")
    elif a[0] == "dressfiles":   # dressfiles list.txt h runs seed: each library game + h new vertices as in "dress"
        h, runs, seed = int(a[2]), int(a[3]), int(a[4]); rng = random.Random(seed)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g0 = pg.read(os.path.join(DC.ROOT, path)); nn = g0.n
            prio, owner, succ = list(g0.prio), list(g0.owner), [list(x) for x in g0.succ]
            for j in range(h):
                v = nn + j; o = 1 if rng.random() < 0.7 else 0
                d = 1 if o == 0 else rng.randint(2, 3)
                tg = sorted(set(rng.randrange(0, v) for _ in range(d)))
                prio.append(rng.randint(0, max(prio) + 1)); owner.append(o); succ.append(tg)
            gp = pg.Game(prio, owner, succ)
            for r in range(runs):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"{path}+{h}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2: s, t = R.read_start(gp, a[2]); nm = os.path.basename(a[1]) + "#start"
        else: s, t = R.starts(gp, 0, None); nm = os.path.basename(a[1]) + "#S3"
        run_game(gp, s, t, st, nm)
    print("MODE", " ".join(a), "MUT", MUT or "-", "BUDGET", BUDGET)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
