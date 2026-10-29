#!/usr/bin/env python3
r"""REFEREE-2 successor 19 (Opus 5.5, D15): mechanical check of P-N5-REL (docs/si/P-N5-REL-box25.md, sha1 f79300a2 @ l-si 07f19760).
State loop = my lane's SPEC loop (dual_check.Runner on si.py = SPEC S1, read-only); Xi, W = my own play values. Lane tools
(experiments/si/grun/*.py) NOT run or imported. RUN S = maximal fallback-free stretch of one (lambda_Xi, tau)-phase.
GATE-RISE (every in-phase S4a transition of S, every Odd u with sigmabar(u) y1 -> y2), kinds CLEAN / TIE ((iii) fails) / CYC ((i) fails) /
THRU ((i) holds, (ii) fails):
  GR      clean => Xi_{t+1}(u) > Xi_t(u); steps GR2 (Xi_t(u) <= u (+) Xi_t(y2) = V_{sigma_t, tau'}(u), tau' = sigmabar_t with u -> y2, computed
          from the play), GR3 (Xi_t(y1) < Xi_t(y2)), GR4 (Xi_{t+1}(y2) >= Xi_t(y2))
  GRC     Count: per S and u, CH <= XR + TIE + CYC + THRU; G(S) <= sum_u (...)
STATIC-DEPTH-REL (every b of S, every [a, b] REL-admissible w.r.t. b's sets, b - a <= RELCAP): X_b, RO_b, CW_b, CH_b, T, V^W_b, V^H_b per §2;
  recursion dW on V^W, dH on V^H; (H4'_rel); GEN_W used form on X_b's W-plays (fail -> counted apart, still checked)
  RSETW / RSETH  per-vertex settling on V^W / V^H;  RSIG  sigma_t = sigma_b on [a + max_{Q\T} d, b];  RLEN  b - a <= max_{Q\T} d <= |Even\T|
  RDOM    the recursion stays in its domains;  RCLOSE  every Even vertex of V^W cup V^H is in X_b
  RREM    Remark: where STATIC-DEPTH' hypotheses hold on [a, b] (sigmabar constant everywhere, all cycles of b persist, (H4')), [a, b] is
          REL-admissible, (H4'_rel) holds, and max_{Q\T} d_rel <= max_{Even\T} d_SD'
REL-SPLIT (every run S): segments from the end; RSCUT each cut is a sigmabar change on RO_{b_i} or an appearance of a CW/CH cycle of b_i;
  RSCNT SEG - 1 <= G(S) + CF(S); RSLEN where (H4'_rel), GEN_W hold at every b_i: each segment <= n - 1 and |S| <= SEG n - 1
Controls (REL_MUT, counted as violations, expected to bite): y2rise (GATE-RISE: strict rise of Xi(y2) demanded); thru (GATE-RISE demanded at
THRU changes); tie (at TIE changes); cyc (at CYC changes); dm1 (settling from a + d - 1); nosbar (REL-admissible without the sigmabar condition
on RO_b); qonly (X_b := Q, no closure: plays of Q only).
Usage: rel_check.py files list.txt [runs] | pairs list.txt prefix | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-SDPRIME"))
import rund_check as R
import sdprime_check as SDP
DC, pg, Stats = R.DC, R.pg, R.Stats
MUT = os.environ.get("REL_MUT", "")
RELCAP = int(os.environ.get("RELCAP", "60"))
cycles = SDP.cycles


def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); g, n = gp, gp.n
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    for k in range(len(I)):
        I[k]["cW"] = cycles(I[k]["wn"]); I[k]["cH"] = cycles(I[k]["hn"])
    key = [(I[k]["lamX"], I[k]["tu"]) for k in range(len(I))]
    k0 = 0
    while k0 < len(I):
        k1 = k0
        while k1 + 1 < len(I) and key[k1 + 1] == key[k0] and not fbs[k1]: k1 += 1
        if k1 > k0: check_S(ctx, g, I, k0, k1, st, name)
        k0 = k1 + 1


def oncyc(nx, v):
    path, x = R.lasso(nx, v)
    return v in path[path.index(x):]


def play_value_with(ctx, I, k, u, y2):
    """V_{sigma_k, tau'}(u), tau' = sigmabar_k with u -> y2 (play value from the definition)."""
    hn = list(I[k]["hn"]); hn[u] = y2
    return R.play_value(ctx.E, hn, u)


def gate_rise(ctx, g, I, a, b, st, name):
    n, K = ctx.n, ctx.key
    odd2 = [u for u in range(n) if g.owner[u] == 1 and len(set(g.succ[u])) >= 2]
    CH = {u: 0 for u in odd2}; XR = {u: 0 for u in odd2}; KIND = {u: {"TIE": 0, "CYC": 0, "THRU": 0} for u in odd2}
    G = 0
    for t in range(a, b):
        s0, s1 = I[t], I[t + 1]
        if any(s0["hn"][u] != s1["hn"][u] for u in odd2): G += 1
        for u in odd2:
            if K(s0["xi"][u]) != K(s1["xi"][u]): XR[u] += 1
            y1, y2 = s0["hn"][u], s1["hn"][u]
            if y1 == y2: continue
            CH[u] += 1
            ci = not oncyc(s0["hn"], u) and not oncyc(s1["hn"], u)
            cii = u not in R.lasso(s0["hn"], y2)[0]
            ciii = K(s0["xi"][y1]) != K(s0["xi"][y2])
            rise = K(s1["xi"][u]) > K(s0["xi"][u])
            if not ciii: KIND[u]["TIE"] += 1
            if not ci: KIND[u]["CYC"] += 1
            elif not cii: KIND[u]["THRU"] += 1
            kind = "CLEAN" if (ci and cii and ciii) else ("CYC" if not ci else ("THRU" if not cii else "TIE"))
            st.inc("GR_changes_" + kind)
            if kind == "CLEAN":
                st.inc("GR_checks")
                if not rise: st.bad("GR", f"{name}@{t} u={u} {y1}->{y2}")
                if not K(s0["xi"][u]) <= K(play_value_with(ctx, I, t, u, y2)): st.bad("GR2", f"{name}@{t} u={u}")
                if not K(s0["xi"][y1]) < K(s0["xi"][y2]): st.bad("GR3", f"{name}@{t} u={u}")
                if not K(s1["xi"][y2]) >= K(s0["xi"][y2]): st.bad("GR4", f"{name}@{t} u={u}")
                if MUT == "y2rise" and not K(s1["xi"][y2]) > K(s0["xi"][y2]): st.bad("MUT_y2rise", f"{name}@{t} u={u}")
            else:
                if not rise: st.inc("GR_norise_" + kind)
                if MUT == "thru" and kind == "THRU" and not rise: st.bad("MUT_thru", f"{name}@{t} u={u}")
                if MUT == "tie" and kind == "TIE" and not rise: st.bad("MUT_tie", f"{name}@{t} u={u}")
                if MUT == "cyc" and kind == "CYC" and not rise: st.bad("MUT_cyc", f"{name}@{t} u={u}")
    tot = 0
    for u in odd2:
        rhs = XR[u] + KIND[u]["TIE"] + KIND[u]["CYC"] + KIND[u]["THRU"]
        tot += rhs
        st.inc("GRC_checks")
        if CH[u] > rhs: st.bad("GRC", f"{name} [{a},{b}] u={u}")
    if G > tot: st.bad("GRC_G", f"{name} [{a},{b}]")
    return G


def rel_sets(g, Ib, n):
    sg, wn, hn = Ib["sg"], Ib["wn"], Ib["hn"]
    Q = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) >= 2]
    X = set(Q); stack = list(Q)
    if MUT != "qonly":
        while stack:
            v = stack.pop()
            for mp in (wn, hn):
                for x in R.lasso(mp, v)[0]:
                    if g.owner[x] == 0 and x not in X: X.add(x); stack.append(x)
    VW, VH, cw, ch = set(), set(), set(), set()
    for v in X:
        pw, xw = R.lasso(wn, v); ph, xh = R.lasso(hn, v)
        VW |= set(pw); VH |= set(ph)
        zw = pw[pw.index(xw):]; zh = ph[ph.index(xh):]
        cw.add(rot(zw)); ch.add(rot(zh))
    RO = frozenset(x for x in VH if g.owner[x] == 1)
    TW = frozenset(x for c in cw for x in c); TH = frozenset(x for c in ch for x in c)
    return dict(Q=Q, X=frozenset(X), RO=RO, CW=frozenset(cw), CH=frozenset(ch), TW=TW, TH=TH, VW=frozenset(VW), VH=frozenset(VH))


def rot(c):
    i = c.index(min(c)); return tuple(c[i:] + c[:i])


def admissible(I, a, b, S):
    Ib = I[b]
    for t in range(a, b + 1):
        if MUT != "nosbar" and any(I[t]["hn"][u] != Ib["hn"][u] for u in S["RO"]): return False
        if not S["CW"] <= I[t]["cW"] or not S["CH"] <= I[t]["cH"]: return False
    return True


def rel_depths(g, Ib, S, st, name):
    sg, tu, hn = Ib["sg"], Ib["tu"], Ib["hn"]
    TW, TH, VW, VH = S["TW"], S["TH"], S["VW"], S["VH"]
    dW, dH, mark = {}, {}, {}
    def gw(v):
        if v not in VW: st.bad("RDOM", f"{name}: dW at {v}"); raise KeyError
        if v in dW: return dW[v]
        if mark.get(("W", v)) == 1: raise ValueError
        mark[("W", v)] = 1
        if v in TW: r = 0
        elif g.owner[v] == 1: r = gw(tu[v])
        elif v in TH: r = gw(sg[v])
        else: r = 1 + max(gw(sg[v]), gh(sg[v]))
        dW[v] = r; mark[("W", v)] = 2; return r
    def gh(v):
        if v not in VH: st.bad("RDOM", f"{name}: dH at {v}"); raise KeyError
        if v in dH: return dH[v]
        if mark.get(("H", v)) == 1: raise ValueError
        mark[("H", v)] = 1
        if v in TH: r = 0
        elif g.owner[v] == 1: r = gh(hn[v])
        elif v in TW: r = gh(sg[v])
        else: r = 1 + max(gw(sg[v]), gh(sg[v]))
        dH[v] = r; mark[("H", v)] = 2; return r
    try:
        for v in VW: gw(v)
        for v in VH: gh(v)
    except (ValueError, RecursionError):
        return None
    except KeyError:
        return None
    return dW, dH


def gen_used_X(I, a, b, X):
    for v in X:
        seen = {}
        for t in range(a, b + 1):
            p = R.lasso(I[t]["wn"], v); w = I[t]["w"][v]
            if w in seen and seen[w] != p: return False
            seen[w] = p
    return True


def check_rel(ctx, g, I, a, b, S, dd, st, name):
    n, K = ctx.n, ctx.key
    Ib = I[b]; dW, dH = dd
    T = S["TW"] | S["TH"]
    gen = gen_used_X(I, a, b, S["X"])
    tag = "REL" if gen else "RELng"
    st.inc(tag + "_intervals")
    bad = lambda chk, msg: st.bad(chk, msg) if gen else st.inc("FAIL_noGEN_" + chk)
    sh = 1 if MUT == "dm1" else 0
    for v in S["VW"]:
        for t in range(max(a, a + dW[v] - sh), b + 1):
            if R.lasso(I[t]["wn"], v) != R.lasso(Ib["wn"], v): bad("RSETW", f"{name} [{a},{b}] v={v} t={t}"); break
    for v in S["VH"]:
        for t in range(max(a, a + dH[v] - sh), b + 1):
            if R.lasso(I[t]["hn"], v) != R.lasso(Ib["hn"], v): bad("RSETH", f"{name} [{a},{b}] v={v} t={t}"); break
    if MUT == "dm1": return
    qt = [v for v in S["Q"] if v not in T]
    md = max((dW[v] for v in qt), default=0)
    evo = [v for v in range(n) if g.owner[v] == 0 and v not in T]
    if not (b - a <= md <= len(evo) <= n - 1): bad("RLEN", f"{name} [{a},{b}] len {b - a} md {md}")
    for t in range(a + md, b + 1):
        if I[t]["sg"] != Ib["sg"]: bad("RSIG", f"{name} [{a},{b}] t={t}"); break
    if b - a == md and md > 0: st.inc(tag + "_sharp")
    st.mxr(tag + "_max_len", (b - a, name, a, b, md, n))
    # extras: Odd vertices off RO_b whose sigmabar moves inside [a, b]
    moving = any(I[t]["hn"][u] != Ib["hn"][u] for t in range(a, b + 1) for u in range(n) if g.owner[u] == 1 and u not in S["RO"])
    if moving: st.inc(tag + "_sbar_moves_off_RO")
    allc = all(I[b]["cW"] <= I[t]["cW"] and I[b]["cH"] <= I[t]["cH"] for t in range(a, b + 1))
    if not allc: st.inc(tag + "_nonrel_cycle_breaks")
    if moving or not allc: st.inc(tag + "_beyond_SDPRIME")


def check_S(ctx, g, I, a, b, st, name):
    n = ctx.n
    st.inc("S_runs")
    G = gate_rise(ctx, g, I, a, b, st, name)
    if MUT in ("y2rise", "thru", "tie", "cyc"): return
    sets = {}
    for bb in range(a, b + 1):
        S = rel_sets(g, I[bb], n); sets[bb] = S
        for v in S["VW"] | S["VH"]:
            if g.owner[v] == 0 and v not in S["X"]: st.bad("RCLOSE", f"{name}@{bb} v={v}")
        dd = rel_depths(g, I[bb], S, st, f"{name}@{bb}")
        aa = bb - 1
        while aa >= max(a, bb - RELCAP) and admissible(I, aa, bb, S):
            st.inc("RA_intervals")
            if dd is None: st.inc("H4rel_fail")
            else: check_rel(ctx, g, I, aa, bb, S, dd, st, name)
            if MUT == "" : remark(ctx, g, I, aa, bb, S, dd, st, name)
            aa -= 1
    if MUT: return
    # REL-SPLIT
    segs, bk = [], b
    while bk >= a:
        ak = bk
        while ak - 1 >= a and admissible(I, ak - 1, bk, sets[bk]): ak -= 1
        segs.append((ak, bk)); bk = ak - 1
    segs.reverse(); k = len(segs)
    CF = sum(1 for t in range(a, b) if not (I[t + 1]["cW"] <= I[t]["cW"]) or not (I[t + 1]["cH"] <= I[t]["cH"]))
    st.inc("RS_runs"); st.inc("RS_segments", k)
    for i in range(1, k):
        x, y = segs[i]; S = sets[y]
        sb = any(I[x - 1]["hn"][u] != I[y]["hn"][u] and I[x]["hn"][u] == I[y]["hn"][u] for u in S["RO"])
        ap = any(c in I[x]["cW"] and c not in I[x - 1]["cW"] for c in S["CW"]) or any(c in I[x]["cH"] and c not in I[x - 1]["cH"] for c in S["CH"])
        if not (sb or ap): st.bad("RSCUT", f"{name} seg [{x},{y}]")
    if k - 1 > G + CF: st.bad("RSCNT", f"{name} [{a},{b}] SEG {k} G {G} CF {CF}")
    if (b - a) != sum(y - x for x, y in segs) + (k - 1): st.bad("RSsum", f"{name}")
    hyp = all(rel_depths(g, I[y], sets[y], st, name) is not None and gen_used_X(I, x, y, sets[y]["X"]) for x, y in segs)
    if hyp:
        st.inc("RS_hyp_runs")
        for x, y in segs:
            if y - x > n - 1: st.bad("RSLEN", f"{name} seg [{x},{y}]")
        if b - a > k * n - 1: st.bad("RSLEN_run", f"{name} [{a},{b}] SEG {k}")
    st.mxr("RS_max_SEG_over_n", (round(k / n, 3), name, a, b, k, n))
    st.mxr("RS_max_run_over_SEGn", (round((b - a) / (k * n), 3), name, a, b, k, n))


def remark(ctx, g, I, a, b, S, dd, st, name):
    n = ctx.n
    sd_ok = all(I[t]["hn"][u] == I[b]["hn"][u] for t in range(a, b + 1) for u in range(n) if g.owner[u] == 1) and SDP.h3p(I, a, b)
    if not sd_ok: return
    Ib = I[b]; TW, TH = SDP.cyc_verts(Ib["cW"]), SDP.cyc_verts(Ib["cH"])
    d2 = SDP.depths(g, Ib, TW, TH, n)
    if d2 is None: return
    st.inc("RREM_checks")
    if dd is None: st.bad("RREM", f"{name} [{a},{b}]: (H4') but not (H4'_rel)"); return
    T = S["TW"] | S["TH"]
    md_rel = max((dd[0][v] for v in S["Q"] if v not in T), default=0)
    md_sd = max((d2[0][v] for v in range(n) if g.owner[v] == 0 and v not in (TW | TH)), default=0)
    if md_rel > md_sd: st.bad("RREM_d", f"{name} [{a},{b}] {md_rel} > {md_sd}")


def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(2626)
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
    print("MODE", " ".join(a), "MUT", MUT or "-", "RELCAP", RELCAP)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
