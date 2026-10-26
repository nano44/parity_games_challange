#!/usr/bin/env python3
r"""REFEREE-2 successor 17 (Opus 5.5, D15): mechanical check of packet P-N5-FBC (docs/new/P-N5-FBC-box47.md sha1 32d3776c @ de02d37e).
Built on my lane's R2-N5-HONFF/honff_check.py (simple-path enumeration) and R2-N5-HON/hon_check.py (state sequence = succ. 13's SPEC loop,
Runner; Xi, W = my own play values, cross-checked against the engine: ENGXI). Lane tools (experiments/new/box47/*.py) NOT run or imported.
Per phase P and per configuration C = sigmabar|Q at a fallback source: H_C = G with every Odd vertex cut to sigmabar_C; LEV_C(k) EXACT at every
state of P by enumeration of all simple H_C-paths to cycle nodes of lambda (budget per (phase, C); over budget -> UNK, skipped, counted).
Checks:
  FBC     FB-RISE_C: in-phase fallback t -> t+1 with t a C-state: LEV_C(t+1) >= min(LEV_C(t) + 1, n - 1)
  ODDC    the Odd case alone, at EVERY C-state t (fallback or not): Xi_t(x) >= value(r) for Odd x, simple H_C-path r, |r| <= min(LEV_C(t)+1, n-1)
  QAC     Lemma P's Case A pointwise in H_C at fallback sources (Even x, non-improving z, Xi_t(z) >= value(r')  =>  value(r) <= Xi_t(x))
  MONO    LEV_C non-decreasing over all states of P
  XIB     at every C-state: Xi_t(x) is the value of some simple H_C-path from x and Xi_t(x) <= B_C(x)
  SATC    at a C-state with LEV_C = n - 1: Xi_t = B_C; and from it to every later C-state t': Xi constant on [t, t'] and t' - t <= 4n(n - 1)
  CNT     per C: unsaturated sources <= n - 1, saturated <= 4n(n - 1) + 1; f <= |Cf| (4n^2 - 3n)
  CORa-d  |Cf| <= |configurations visited| <= min(N_ep, prod deg(q)); f <= Delta^k (4n^2 - 3n); if all |D_k| <= 1: visited <= 1 + sum(deg - 1)
          <= 1 + m; visited with |D| <= d <= sum_{j<=d} C(|Q|, j)(Delta - 1)^j; f <= (4n^2 - 3n) N_ep
  CMP     comparisons (not claims): EPOCH f <= 1 + n N_ep (landed; consistency), R56 f <= 1 + (n - 1)(2 + rho) (landed; consistency);
          phases where the FB-C bound |Cf|(4n^2-3n) is below EPOCH's 1 + n N_ep, or below R56's
Controls FBC_MUT: plus2 (FB-RISE_C with + 2), tau (LEV in G_tau instead of H_C, no Odd term), sat (saturated count <= 1 per C, the packet's §5 hope:
NOT claimed; reports where it fails).
Usage: fbc_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-HONFF"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-HON"))
import honff_check as HF
H = HF.H
R, DC, pg, Engine, Stats = H.R, H.DC, H.pg, H.Engine, H.Stats
MUT = os.environ.get("FBC_MUT", "")
BUDGET = int(os.environ.get("BUDGET", "400000"))


def check_game(gp, s, t, st, name):
    g, n = gp, gp.n
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp)
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    st.inc("runs"); st.inc("states", len(I))
    tauk = [tuple(b[v] for v in range(n) if g.owner[v] == 1) for _, b in states]
    key = [(I[k]["lamX"], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(ctx, g, I, fbs, k0, k1, Q, st, name)
        k0 = k1 + 1


def check_phase(ctx, g, I, fbs, a, b, Q, st, name):
    n, E = ctx.n, ctx.E
    st.inc("phases")
    lam = I[a]["lamX"]; tu = I[a]["tu"]
    cyc = frozenset(v for v in range(n) if lam[v] == v)
    conf = {k: tuple(I[k]["hn"][q] for q in Q) for k in range(a, b + 1)}
    fbk = [k for k in range(a, b) if fbs[k]]
    f = len(fbk)
    bound1 = 4 * n * n - 3 * n
    # epochs, configurations, D
    epochs, k = [], a
    while k <= b:
        e = k
        while e + 1 <= b and conf[e + 1] == conf[k]: e += 1
        epochs.append((k, e)); k = e + 1
    Nep = len(epochs)
    visited = set(conf.values())
    Cf = set(conf[t] for t in fbk)
    deg = {q: len(set(g.succ[q])) for q in Q}
    prod = 1
    for q in Q: prod *= deg[q]
    Delta = max(len(set(g.succ[v])) for v in range(n))
    m = sum(len(set(g.succ[v])) for v in range(n))
    tq = tuple(tu[q] for q in Q)
    Dsz = {C: sum(1 for i in range(len(Q)) if C[i] != tq[i]) for C in visited}
    rho = sum(1 for k in range(a, b) for q in Q if I[k + 1]["xi"][q] != I[k]["xi"][q])
    # corollaries (a)-(d)
    st.inc("COR_phases")
    if not Cf <= visited: st.bad("CORa_sub", f"{name}@{a}")
    if len(visited) > min(Nep, prod): st.bad("CORa", f"{name}@{a}: visited {len(visited)} N_ep {Nep} prod {prod}")
    if f > bound1 * min(Nep, prod): st.bad("CORa_f", f"{name}@{a}")
    if f > Delta ** len(Q) * bound1: st.bad("CORb", f"{name}@{a}")
    if f > bound1 * Nep: st.bad("CORd", f"{name}@{a}")
    if all(len(I[k]["D"]) <= 1 for k in range(a, b + 1)):
        st.inc("CORc_phases")
        cap = 1 + sum(deg[q] - 1 for q in Q)
        if len(visited) > cap or cap > 1 + m: st.bad("CORc", f"{name}@{a}: visited {len(visited)} cap {cap} m {m}")
        if f > (1 + m) * bound1: st.bad("CORc_f", f"{name}@{a}")
    for d in range(len(Q) + 1):
        cnt = sum(1 for C in visited if Dsz[C] <= d)
        if cnt > sum(comb(len(Q), j) * (Delta - 1) ** j for j in range(d + 1)): st.bad("CORc_gen", f"{name}@{a}: d {d}")
    # D_k as the code's D equals |{q in Q: sigmabar(q) != tau(q)}|
    for k in range(a, b + 1):
        if len(I[k]["D"]) != Dsz[conf[k]]: st.bad("DDEF", f"{name}@{k}")
    if f:
        st.inc("phases_with_fallback"); st.inc("f_total", f); st.inc("Cf_total", len(Cf)); st.inc("Nep_total_fbphases", Nep)
        st.inc("visited_total_fbphases", len(visited)); st.inc("rho_total_fbphases", rho)
        st.mxr("max_f_phase", (f, f"{name}@{a} n {n} |Cf| {len(Cf)} N_ep {Nep}"))
        st.mxr("max_Cf_phase", (len(Cf), f"{name}@{a} n {n} f {f}"))
        st.mxr("max_Nep_over_Cf", (Nep / len(Cf), f"{name}@{a} n {n} N_ep {Nep} |Cf| {len(Cf)} visited {len(visited)}"))
        ep_b, r56_b, fbc_b = 1 + n * Nep, 1 + (n - 1) * (2 + rho), len(Cf) * bound1
        if f > ep_b: st.bad("CMP_EPOCH_violated", f"{name}@{a}")
        if f > r56_b: st.bad("CMP_R56_violated", f"{name}@{a}")
        if fbc_b < ep_b: st.inc("CMP_fbc_below_epoch")
        # §C: REFEREE's FBC-N3 (f <= n |Cf|) checked here, and its comparisons; FLATLAST: a Xi-flat in-phase fallback ends its phase
        st.inc("N3_phases")
        if f > n * len(Cf): st.bad("N3_bound", f"{name}@{a}: f {f} n {n} |Cf| {len(Cf)}")
        if n * len(Cf) < ep_b: st.inc("N3_below_epoch")
        if n * len(Cf) < r56_b: st.inc("N3_below_r56")
        if n * len(Cf) > r56_b: st.inc("N3_above_r56")
        for t in fbk:
            if I[t + 1]["xi"] == I[t]["xi"]:
                st.inc("FLATLAST_checks")
                if t + 1 != b: st.bad("FLATLAST", f"{name}@{t}: Xi-flat in-phase fallback not at the phase end")
        if fbc_b < r56_b: st.inc("CMP_fbc_below_r56")
        if n >= 2 and bound1 * Nep < ep_b: st.bad("CMP_header_Nep_form_not_weaker", f"{name}@{a}")
        st.mxr("max_rho_over_nCf", (rho / (n * len(Cf)), f"{name}@{a} n {n} rho {rho} |Cf| {len(Cf)} f {f}"))
    if not fbk: return
    # per configuration in Cf: LEV_C at every state of P
    allx = list(range(n)); oddx = [x for x in allx if g.owner[x] == 1]
    for C in sorted(Cf):
        src = [t for t in fbk if conf[t] == C]
        cst = [k for k in range(a, b + 1) if conf[k] == C]
        hC = I[src[0]]["hn"] if MUT != "tau" else tu
        try:
            if os.environ.get("FORCE_DEEP"): raise HF.Over()
            sv = HF.simple_values(ctx, hC, cyc, BUDGET)
        except HF.Over:
            st.inc("UNK_C"); st.inc("UNK_C_fallbacks", len(src))
            deep_check(ctx, g, I, conf, C, src, cst, hC, cyc, a, b, st, name)
            continue
        st.inc("C_checked")
        B = HF.table(ctx, sv, allx)
        LEV = {k: HF.lev(ctx, B, I[k]["xi"], allx) for k in range(a, b + 1)}
        for k in range(a, b):
            if LEV[k + 1] < LEV[k]: st.bad("MONO", f"{name}@{k}: LEV_C {LEV[k]} -> {LEV[k + 1]}")
        for t in cst:
            st.inc("C_states")
            xi = I[t]["xi"]
            LO = HF.lev(ctx, B, xi, oddx)
            if LO < min(LEV[t] + 1, n - 1): st.bad("ODDC", f"{name}@{t}: LEV_C {LEV[t]} LEV_C,odd {LO}")
            for x in allx:
                kx = ctx.key(xi[x])
                if B[x][n - 1] is not None and kx > B[x][n - 1]: st.bad("XIB", f"{name}@{t}: x {x} Xi > B_C")
                if not any(kv == kx for _, kv, _ in sv[x]): st.bad("XIB_path", f"{name}@{t}: x {x} Xi not a simple H_C-path value")
            st.inc("XIB_checks")
        sat = [t for t in cst if LEV[t] >= n - 1]
        if sat:
            t0 = sat[0]
            for t in sat:
                st.inc("SATC_eq_checks")
                if any(B[x][n - 1] is not None and ctx.key(I[t]["xi"][x]) != B[x][n - 1] for x in allx): st.bad("SATC_eq", f"{name}@{t}")
            tl = cst[-1]
            st.inc("SATC_window_checks")
            if any(I[k]["xi"] != I[t0]["xi"] for k in range(t0, tl + 1)): st.bad("SATC_const", f"{name}@{t0}..{tl}")
            if tl - t0 > 4 * n * (n - 1): st.bad("SATC_window", f"{name}@{t0}..{tl}")
            st.mxr("max_sat_window", (tl - t0, f"{name}@{t0} n {n}"))
        uns = [t for t in src if LEV[t] <= n - 2]; sats = [t for t in src if LEV[t] >= n - 1]
        st.inc("FBC_fallbacks", len(src)); st.inc("FBC_unsat", len(uns)); st.inc("FBC_sat", len(sats))
        st.mxr("max_unsat_per_C", (len(uns), f"{name}@{a} n {n}"))
        st.mxr("max_sat_per_C", (len(sats), f"{name}@{a} n {n}"))
        if len(uns) > n - 1: st.bad("CNT_unsat", f"{name}@{a}: {len(uns)}")
        if len(sats) > 4 * n * (n - 1) + 1: st.bad("CNT_sat", f"{name}@{a}: {len(sats)}")
        if MUT == "sat" and len(sats) > 1: st.bad("MUT_sat", f"{name}@{a}: {len(sats)} saturated sources of one C")
        for t in src:
            j = min(LEV[t] + (2 if MUT == "plus2" else 1), n - 1)
            if j > LEV[t]: st.inc("FBC_rise_needed")
            if LEV[t + 1] < j: st.bad("FBC", f"{name}@{t}: LEV_C {LEV[t]} -> {LEV[t + 1]} (n {n})")
            if conf[t + 1] != C: st.inc("FBC_target_not_C")
            # Case A pointwise in H_C at the source
            xi = I[t]["xi"]; sg = I[t]["sg"]
            for x in allx:
                if g.owner[x] != 0: continue
                kx = ctx.key(xi[x]); ka = ctx.key(xi[sg[x]])
                for e, kv, path in sv[x]:
                    if e == 0: continue
                    z = path[1]
                    if ctx.key(xi[z]) > ka: continue
                    rp = path[1:]; u = rp[-1]; mm = 0
                    for p in rp[:-1]:
                        if E.rank[p] > E.rank[u]: mm |= E.bit[p]
                    if ctx.key(xi[z]) < E.key((u, mm, len(rp) - 1)): continue
                    st.inc("QAC_checks")
                    if kv > kx: st.bad("QAC", f"{name}@{t}: x {x} path {path}")
    if f > len(Cf) * bound1: st.bad("CNT_f", f"{name}@{a}")


def values_upto(ctx, tu, cyc, budget, D):
    """all simple H_C-paths with <= D edges from every x to a cycle node (exact for that length range)."""
    g, n, E = ctx.g, ctx.n, ctx.E
    out, cnt = {}, [0]
    for x in range(n):
        res = []
        def dfs(y, vis, path):
            cnt[0] += 1
            if cnt[0] > budget: raise HF.Over()
            if y in cyc:
                m = 0
                for p in path[:-1]:
                    if E.rank[p] > E.rank[y]: m |= E.bit[p]
                res.append((len(path) - 1, E.key((y, m, len(path) - 1)), tuple(path)))
            if len(path) - 1 >= D: return
            for z in ([tu[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))):
                if z not in vis:
                    vis.add(z); path.append(z); dfs(z, vis, path); path.pop(); vis.discard(z)
        dfs(x, {x}, [x])
        out[x] = res
    return out


def lev_capped(ctx, sv, vals, xs, D):
    """min(LEV, D): largest j <= D such that vals(x) >= value(r) for all r with <= j edges."""
    n = ctx.n; L = -1
    best = {}
    for x in xs:
        bx = {}
        for e, k, _ in sv[x]:
            if e not in bx or k > bx[e]: bx[e] = k
        best[x] = bx
    for j in range(D + 1):
        if all(all(k <= ctx.key(vals[x]) for e, k in best[x].items() if e <= j) for x in xs): L = j
        else: break
    return L


def deep_check(ctx, g, I, conf, C, src, cst, hC, cyc, a, b, st, name):
    """DEEP mode (UNK under full enumeration): iterative deepening on the path length D until every fallback source of C has
    min(LEV_C, D) < D (so its LEV_C is exact); then FBC, MONO (capped), ODDC (where exact) and the unsaturated count."""
    n = ctx.n; allx = list(range(n)); oddx = [x for x in allx if g.owner[x] == 1]
    D = 1
    while True:
        try:
            sv = values_upto(ctx, hC, cyc, BUDGET, D)
        except HF.Over:
            st.inc("DEEP_UNK_C"); st.inc("DEEP_UNK_fallbacks", len(src)); return
        LEV = {k: lev_capped(ctx, sv, I[k]["xi"], allx, D) for k in range(a, b + 1)}
        if all(LEV[t] < D for t in src) or D >= n - 1: break
        D += 1
    st.inc("DEEP_C"); st.mxr("DEEP_max_D", (D, f"{name}@{a} n {n}"))
    for k in range(a, b):
        if LEV[k + 1] < LEV[k]: st.bad("MONO", f"{name}@{k} (deep)")
    for t in cst:
        if LEV[t] < D:
            st.inc("DEEP_ODDC_checks")
            LO = lev_capped(ctx, sv, I[t]["xi"], oddx, D)
            if LO < min(LEV[t] + 1, n - 1, D): st.bad("ODDC", f"{name}@{t} (deep)")
    uns = [t for t in src if LEV[t] <= n - 2 and LEV[t] < D]
    st.inc("DEEP_fallbacks", len(src)); st.inc("DEEP_unsat", len(uns))
    st.mxr("max_unsat_per_C", (len(uns), f"{name}@{a} n {n} (deep)"))
    if len(uns) > n - 1: st.bad("CNT_unsat", f"{name}@{a} (deep)")
    for t in src:
        if LEV[t] >= D: st.inc("DEEP_src_not_exact"); continue
        j = min(LEV[t] + (2 if MUT == "plus2" else 1), n - 1)
        if LEV[t + 1] < min(j, D): st.bad("FBC", f"{name}@{t}: LEV_C {LEV[t]} -> {LEV[t + 1]} (deep, D {D})")
        st.inc("DEEP_FBC_checks")


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1717)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); check_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H3.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); check_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        s, t = R.read_start(gp, a[2]) if len(a) > 2 else R.starts(gp, 0, None)
        check_game(gp, s, t, st, os.path.basename(a[1]))
    print("MODE", " ".join(a), "MUT", MUT or "-", "BUDGET", BUDGET)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
