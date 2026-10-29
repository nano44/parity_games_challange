#!/usr/bin/env python3
r"""REFEREE-2 successor 19 (Opus 5.5, D15): mechanical check of P-N5-SDPRIME (docs/si/P-N5-SDPRIME-box25.md, sha1 54678c38 @ l-si edc14c51).
State loop = my lane's SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py = SPEC S1, read-only); Xi, W = my own play values
(R2-N5-RUND/rund_check.state_info, ENGXI). Lane tools (experiments/si/piece/sdprime.py, epochs.py) NOT run or imported.
S = maximal fallback-free runs inside one (lambda_Xi, tau)-phase (lambda_W NOT required constant: (H1')). PIECE = maximal sigmabar-constant
sub-run of S ((H2)). Every sub-interval [a, b] of a piece with b - a <= SDCAP is tested for (H3') (every W-cycle / honest cycle of b is one at
every t in [a, b]); then T_W, T_H, the depth recursion dW, dH, d, and (H4') (recursion well founded), GEN_W in its USED form (W-plays of a vertex
at states of [a, b] with equal W-valuation are equal; intervals where it fails are counted apart, SD_noGEN, and still checked).
Checks (each must be 0, on intervals with (H3'), (H4'), GEN_W):
  H4EQ    (H4') recursion well founded <=> J_b acyclic;  DEQ  d(v) = number of vertices of a longest J_b-path from v
  SETW / SETH   W-play (honest play) of every v at every t in [a + dW(v), b] (resp. [a + dH(v), b]) equals that at b
  LEN     b - a <= max d <= |Even \ T| <= n - 1;  SIGB  sigma_t = sigma_b on [a + max d, b]
  STEPA   step 4 (A): Even v not in T, y = sigma_b(v), t in [a + max(dW y, dH y), b]: y in {sigma_t v} cup I_sigma_t(v)
  STEPB   step 4 (B): W_{t+1}(v) = W_b(v) for t in [s, b - 1]
  WMONO / XSUCC  W_{t+1} >= W_t and Xi_t(sigma_t v) non-decreasing at every transition of S (also where lambda_W changes: WMONO_lw / XSUCC_lw)
  REM     on intervals with R77's (H1)-(H4) (lambda_W constant, W- and honest cycles equal and constant, H_b acyclic off cycles): (H3'), (H4')
          hold and d(v) <= d*(v)
  EP*     Corollary EPOCH on every piece: epochs built backwards; each epoch has (H3'); EPAPP: a cycle of b_i appears at a_i - 1 -> a_i (i >= 2);
          k - 1 <= CF; where (H4') and GEN_W hold at every epoch end: every epoch b_i - a_i <= n - 1 and b - a <= (CF + 1) n - 1
Controls (SD_MUT, counted as violations, expected to bite): dm1 (settling demanded from a + d - 1); onlyW ((H3') demanded for W-cycles only,
T_H := honest cycle vertices at b); onlyH (symmetric).
Usage: sdprime_check.py files list.txt [runs] | pairs list.txt prefix | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DEPTH"))
import rund_check as R
import depth_check as DPC
DC, pg, Stats = R.DC, R.pg, R.Stats
MUT = os.environ.get("SD_MUT", "")
SDCAP = int(os.environ.get("SDCAP", "60"))
cycles = DPC.cycles


def cyc_verts(cs): return frozenset(x for c in cs for x in c)


def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); g, n = gp, gp.n
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    for k in range(len(I)):
        I[k]["cW"] = cycles(I[k]["wn"]); I[k]["cH"] = cycles(I[k]["hn"])
    key = [(I[k]["lamX"], I[k]["tu"]) for k in range(len(I))]
    k0 = 0
    while k0 < len(I) - 1:
        k1 = k0
        while k1 + 1 < len(I) and key[k1 + 1] == key[k0] and not fbs[k1]: k1 += 1
        if k1 > k0: check_S(ctx, g, I, k0, k1, st, name)
        k0 = k1 + 1 if k1 > k0 else k0 + 1


def depths(g, Ib, TW, TH, n):
    """dW, dH, d per the packet, or None if the recursion is not well founded."""
    sg, tu, hn = Ib["sg"], Ib["tu"], Ib["hn"]
    dW, dH, st = {}, {}, {}
    def gw(v):
        if v in dW: return dW[v]
        if st.get(("W", v)) == 1: raise ValueError
        st[("W", v)] = 1
        if v in TW: r = 0
        elif g.owner[v] == 1: r = gw(tu[v])
        elif v in TH: r = gw(sg[v])
        else: r = 1 + max(gw(sg[v]), gh(sg[v]))
        dW[v] = r; st[("W", v)] = 2; return r
    def gh(v):
        if v in dH: return dH[v]
        if st.get(("H", v)) == 1: raise ValueError
        st[("H", v)] = 1
        if v in TH: r = 0
        elif g.owner[v] == 1: r = gh(hn[v])
        elif v in TW: r = gh(sg[v])
        else: r = 1 + max(gw(sg[v]), gh(sg[v]))
        dH[v] = r; st[("H", v)] = 2; return r
    try:
        for v in range(n): gw(v); gh(v)
    except (ValueError, RecursionError):
        return None
    return dW, dH


def Jb(g, Ib, T, n):
    out = {}
    for v in range(n):
        if g.owner[v] != 0 or v in T: continue
        nx = set()
        for mp in (Ib["wn"], Ib["hn"]):
            path, _ = R.lasso(mp, v)
            for x in path[1:]:
                if g.owner[x] == 0 and x not in T: nx.add(x); break
        out[v] = nx
    return out


def longest(J):
    """vertex count of a longest path from each v, or None if J has a cycle."""
    memo, st = {}, {}
    def go(v):
        if v in memo: return memo[v]
        if st.get(v) == 1: raise ValueError
        st[v] = 1
        r = 1 + max([go(x) for x in J[v]], default=0)
        memo[v] = r; st[v] = 2; return r
    try:
        for v in J: go(v)
    except (ValueError, RecursionError):
        return None
    return memo


def h3p(I, a, b, mode=""):
    cWb, cHb = I[b]["cW"], I[b]["cH"]
    for t in range(a, b + 1):
        if mode != "onlyH" and not cWb <= I[t]["cW"]: return False
        if mode != "onlyW" and not cHb <= I[t]["cH"]: return False
    return True


def gen_used(I, a, b, n):
    for v in range(n):
        seen = {}
        for t in range(a, b + 1):
            p = R.lasso(I[t]["wn"], v); w = I[t]["w"][v]
            if w in seen and seen[w] != p: return False
            seen[w] = p
    return True


def check_interval(ctx, g, I, a, b, st, name, gen):
    """returns (ok_hyp, maxd) ; runs every check of STATIC-DEPTH' on [a, b] if (H3') and (H4') hold."""
    n = ctx.n
    if not h3p(I, a, b, MUT if MUT in ("onlyW", "onlyH") else ""): return None
    Ib = I[b]
    TW, TH = cyc_verts(Ib["cW"]), cyc_verts(Ib["cH"])
    T = TW | TH
    dd = depths(g, Ib, TW, TH, n)
    J = Jb(g, Ib, T, n); L = longest(J)
    st.inc("H3p_intervals")
    if (dd is None) != (L is None): st.bad("H4EQ", f"{name} [{a},{b}]")
    if dd is None: st.inc("H4p_fail"); return None
    dW, dH = dd
    evo = [v for v in range(n) if g.owner[v] == 0 and v not in T]
    for v in evo:
        if dW[v] != dH[v] or dW[v] != L[v]: st.bad("DEQ", f"{name} [{a},{b}] v={v}")
    maxd = max((dW[v] for v in evo), default=0)
    tag = "SD" if gen else "SDng"
    st.inc(tag + "_intervals")
    if TW != TH: st.inc(tag + "_TW_ne_TH")
    if any(I[t]["lamW"] != Ib["lamW"] for t in range(a, b + 1)): st.inc(tag + "_lamW_moves")
    if any(I[t]["cW"] != Ib["cW"] or I[t]["cH"] != Ib["cH"] for t in range(a, b + 1)): st.inc(tag + "_other_cycles_move")
    bad = lambda chk, msg: st.bad(chk, msg) if gen else st.inc("FAIL_noGEN_" + chk)
    sh = 1 if MUT == "dm1" else 0
    for v in range(n):
        for t in range(max(a, a + dW[v] - sh), b + 1):
            if R.lasso(I[t]["wn"], v) != R.lasso(Ib["wn"], v): bad("SETW", f"{name} [{a},{b}] v={v} t={t} dW={dW[v]}"); break
        for t in range(max(a, a + dH[v] - sh), b + 1):
            if R.lasso(I[t]["hn"], v) != R.lasso(Ib["hn"], v): bad("SETH", f"{name} [{a},{b}] v={v} t={t} dH={dH[v]}"); break
    if MUT == "dm1": return True, maxd
    if not (b - a <= maxd <= len(evo) <= n - 1): bad("LEN", f"{name} [{a},{b}] len {b - a} maxd {maxd} |Even\\T| {len(evo)}")
    for t in range(a + maxd, b + 1):
        if I[t]["sg"] != Ib["sg"]: bad("SIGB", f"{name} [{a},{b}] t={t}"); break
    K = ctx.key
    for v in evo:
        y = Ib["sg"][v]; s = a + max(dW[y], dH[y])
        for t in range(s, b + 1):
            st.inc("STEPA_checks")
            if not (I[t]["sg"][v] == y or (v, y) in I[t]["Is"]): bad("STEPA", f"{name} [{a},{b}] v={v} t={t}")
        for t in range(s, b):
            st.inc("STEPB_checks")
            if K(I[t + 1]["w"][v]) != K(Ib["w"][v]): bad("STEPB", f"{name} [{a},{b}] v={v} t={t}")
    if b - a == maxd and maxd > 0: st.inc(tag + "_sharp")
    st.mxr(tag + "_max_len", (b - a, name, a, b, maxd, n))
    return True, maxd


def r77_hyp(ctx, g, I, a, b):
    n = ctx.n
    if any(I[t]["lamW"] != I[b]["lamW"] for t in range(a, b + 1)): return None
    if not all(I[t]["cW"] == I[t]["cH"] == I[b]["cW"] for t in range(a, b + 1)): return None
    E, cv = DPC.Hb(g, I[b], n)
    return DPC.dag_dstar(g, E, cv, n)


def check_S(ctx, g, I, a, b, st, name):
    n, K = ctx.n, ctx.K if hasattr(ctx, "K") else ctx.key
    st.inc("S_runs")
    lw_const = all(I[t]["lamW"] == I[a]["lamW"] for t in range(a, b + 1))
    for t in range(a, b):
        mono = all(K(I[t + 1]["w"][v]) >= K(I[t]["w"][v]) for v in range(n))
        xs = all(K(I[t + 1]["xi"][I[t + 1]["sg"][v]]) >= K(I[t]["xi"][I[t]["sg"][v]]) for v in range(n) if g.owner[v] == 0)
        st.inc("WMONO_checks")
        if not mono: st.bad("WMONO" + ("" if lw_const else "_lw"), f"{name}@{t}")
        if not xs: st.bad("XSUCC" + ("" if lw_const else "_lw"), f"{name}@{t}")
        if I[t + 1]["lamW"] != I[t]["lamW"]: st.inc("lamW_change_transitions")
    sbar = [tuple(I[k]["hn"][v] for v in range(n) if g.owner[v] == 1) for k in range(a, b + 1)]
    i = a
    while i <= b:
        j = i
        while j + 1 <= b and sbar[j + 1 - a] == sbar[i - a]: j += 1
        if j > i: check_piece(ctx, g, I, i, j, st, name)
        i = j + 1


def check_piece(ctx, g, I, a, b, st, name):
    n = ctx.n
    st.inc("pieces"); st.mxr("max_piece_len", (b - a, name, a, b, n))
    if b - a > n - 1: st.inc("pieces_over_n_minus_1")
    for x in range(a, b + 1):
        for y in range(x + 1, min(b, x + SDCAP) + 1):
            gen = gen_used(I, x, y, n)
            if not gen: st.inc("GEN_used_fail_intervals")
            res = check_interval(ctx, g, I, x, y, st, name, gen)
            if MUT: continue
            d = r77_hyp(ctx, g, I, x, y)
            if d is not None:
                st.inc("REM_intervals")
                if res is None: st.bad("REM", f"{name} [{x},{y}]: R77 hypotheses but not (H3')/(H4')"); continue
                Ib = I[y]; T = cyc_verts(Ib["cW"]) | cyc_verts(Ib["cH"])
                dd = depths(g, Ib, cyc_verts(Ib["cW"]), cyc_verts(Ib["cH"]), n)
                for v in range(n):
                    if g.owner[v] == 0 and v not in T and dd[0][v] > d[v]: st.bad("REM_d", f"{name} [{x},{y}] v={v}")
            elif res is not None: st.inc("NEW_coverage_intervals")
    if MUT: return
    # Corollary EPOCH
    eps, bk = [], b
    while bk >= a:
        ak = bk
        while ak - 1 >= a and h3p(I, ak - 1, bk): ak -= 1
        eps.append((ak, bk)); bk = ak - 1
    eps.reverse(); k = len(eps)
    CF = sum(1 for t in range(a, b) if not (I[t + 1]["cW"] <= I[t]["cW"]) or not (I[t + 1]["cH"] <= I[t]["cH"]))
    st.inc("EP_pieces"); st.inc("EP_epochs", k)
    if eps[0][0] != a or any(eps[i][0] != eps[i - 1][1] + 1 for i in range(1, k)): st.bad("EPcut", f"{name} [{a},{b}]")
    if (b - a) != sum(y - x for x, y in eps) + (k - 1): st.bad("EPsum", f"{name} [{a},{b}]")
    for (x, y) in eps:
        if not h3p(I, x, y): st.bad("EPh3", f"{name} [{x},{y}]")
    for i in range(1, k):
        x, y = eps[i]
        appW = [c for c in I[y]["cW"] if c in I[x]["cW"] and c not in I[x - 1]["cW"]]
        appH = [c for c in I[y]["cH"] if c in I[x]["cH"] and c not in I[x - 1]["cH"]]
        if not (appW or appH): st.bad("EPAPP", f"{name} epoch [{x},{y}]")
    if k - 1 > CF: st.bad("EPCF", f"{name} [{a},{b}] k {k} CF {CF}")
    if k - 1 == CF: st.inc("EP_k1_eq_CF")
    st.mxr("EP_max_k", (k, CF, name, a, b, n)); st.mxr("EP_max_CF", (CF, k, name, a, b, n))
    hyp = True
    for (x, y) in eps:
        Ib = I[y]
        if depths(g, Ib, cyc_verts(Ib["cW"]), cyc_verts(Ib["cH"]), n) is None or not gen_used(I, x, y, n): hyp = False
    if hyp:
        st.inc("EP_hyp_pieces")
        if CF > 0: st.inc("EP_hyp_pieces_CFpos")
        for (x, y) in eps:
            if y - x > n - 1: st.bad("EPlen", f"{name} [{x},{y}]")
        if b - a > (CF + 1) * n - 1: st.bad("EPOCH", f"{name} [{a},{b}] CF {CF}")
    else: st.inc("EP_nohyp_pieces")


def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(2525)
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
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2: s, t = R.read_start(gp, a[2]); nm = os.path.basename(a[1]) + "#start"
        else: s, t = R.starts(gp, 0, None); nm = os.path.basename(a[1]) + "#S3"
        run_game(gp, s, t, st, nm)
    print("MODE", " ".join(a), "MUT", MUT or "-", "SDCAP", SDCAP)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
