#!/usr/bin/env python3
r"""REFEREE-2 successor 16 (Opus 5.5, D15): mechanical check of packet P-N5-HON (docs/new/P-N5-HON-box46.md sha1 07f8e767 @ 31835c4b).
State sequence: succ. 13's SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py, read-only). Xi, W: my own PLAY values (R2-N5-RUND/rund_check).
N5^tau: my own loop below (Runner's S4a / S4c, S4b replaced by S4b^tau). The lane's experiments/new/box46/*.py are NOT run or imported.
Definitions as in the packet §0: phase = maximal run with (lambda, tau) constant; f = in-phase S4c fallbacks; Q = Odd vertices of out-degree
>= 2; D_k = {q in Q : sigmabar_k(q) != tau(q)}; epoch = maximal run of a phase with sigmabar|Q constant; W-honest: Xi_k = W_k; f_in.
LEV(k) EXACT for n <= LEVMAX: B_j(x) := max value(r) over simple paths r of G_tau with <= j edges from x to a cycle node of lambda (paths may
pass other cycle nodes), LEV(k) := max j <= n - 1 with Xi_k >= B_j pointwise.
Checks:
  HON / HONp   W-honest states per phase <= f + 4n^2 - 3n / <= f_in + 4n^2 - 3n
  S0           LEV non-decreasing along a phase; LEV >= 0                                              (n <= LEVMAX)
  S1           fallback-free gap h -> h' between consecutive W-honest states: W chain non-decreasing (WM), lambda_W(h + 1) = lambda,
               W_{h+1} >= B_{LEV(h)+1} (the Lemma P step), LEV(h') >= min(LEV(h) + 1, n - 1)            (LEV parts n <= LEVMAX)
  S2           W-honest with LEV = n - 1 => Xi = B (= B_{n-1})
  S3           after the first saturated W-honest t: Xi constant on [t, h_N], h_N - t <= 4n(n - 1)
  SAT0         sigma with no W-improving edge in G_tau => W >= value(r) for every simple r to a W-cycle node (n <= LEVMAX); W-honest =>
               LEV = n - 1
  FB           HON-FB at a W-honest h with an in-phase fallback: (i) every W-improving edge flat (x its own cycle node, z's W-play returns
               to x through vertices ranked below x), (ii) W_{h+1} = W_h, (iii) no W-improving edge at sigma_{h+1}, (iv) h + 1 W-honest,
               saturated (n <= LEVMAX), last state of the phase
  H0           HON-0 (a) D = {} states, (b) D = {} epochs, (c) in-phase transitions with source in a D = {} epoch, each <= f_in + 4n^2 - 3n;
               REC-0's bound (f + 1)(n + 1) + 4n(n - 1) + 1 - (f + 4n^2 - 3n) = f n + 2
  RU           RESTRICT_u (i)-(iv) at every state of a phase with D_k ⊆ {u}, on G^u (u keeps all its edges, other Odd v cut to tau(v))
  RP           REPRO_u: for every u-run J, N5^tau on G^u from (sigma_x, tau) reproduces len(J) transitions (states and fallback types);
               lambda' = lambda on J; EP-1u: len(J) <= T*(G^u) + 1 (vacuous in practice; recorded)
  R1           REC-1 (a): {u}-intervals per phase <= 1 + (f_in + 4n^2 - 3n) + X_dir + X_big, entries classified; (b) |I| <= len(J) + 1
               (structural part) and <= T*(G^u) + 2; (c), (d) against T* (recorded)
Mutations HN_MUT: hon (bound f_in + n - 1, the saturated tail dropped), fb4 (HON-FB (iv) asks h + 1 NOT last), ru (G^u with u cut to tau(u)
too), r1 (REC-1 (a) without the "1 +" and the D = {} term), s1 (Lemma P step with LEV(h) + 2).
Usage: hon_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-1O"))
import rund_check as R
from onecheck import tstar
DC, pg, Engine, Stats = R.DC, R.pg, R.Engine, R.Stats
MUT = os.environ.get("HN_MUT", "")
LEVMAX = int(os.environ.get("LEVMAX", "11"))
RUMAX = int(os.environ.get("RUMAX", "3"))     # u's checked at a D = {} state (all u in Q if <= RUMAX)
dual = DC.dual


def s4a(g, sg, tu, Is):
    n = g.n
    opt = {v: {sg[v]} for v in range(n) if g.owner[v] == 0}
    for v, w in Is: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [tu[v]] for v in range(n)]
    _, best = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return [best[v] if g.owner[v] == 0 else sg[v] for v in range(n)]


def s4b_arena_vals(g, sg, tu, It):
    """S1's valuation on S4b's arena H' (Odd v restricted to {tau(v)} + It(v), Even fixed to sigma) and its counterstrategy"""
    n = g.n
    opt = {v: {tu[v]} for v in range(n) if g.owner[v] == 1}
    for v, w in It: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 1 else [sg[v]] for v in range(n)]
    return Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))


def switch_all(g, E, sg, vals, I):
    ns = list(sg)
    for v in {v for v, _ in I}: ns[v] = max((w for x, w in I if x == v), key=lambda w: (E.key(vals[w]), w))
    return ns


def run_ntau(g, sg, tu, steps):
    """N5^tau (SPEC N5 with S4b^tau: if I_tau != {} and tau is value-optimal against sigma in S4b's arena, keep tau). Returns states,
    fallback flags, and per state the cycle-node map of Xi."""
    n = g.n; E = Engine(g); Ed = Engine(dual(g))
    sg, tu = list(sg), list(tu)
    states, fbs, lams = [(tuple(sg), tuple(tu))], [], []
    for _ in range(steps + 1):
        vs, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        lams.append(tuple(x[0] for x in vs))
        if len(fbs) == steps: break
        Is = E.improving(tuple(sg), vs)
        vt, _ = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        It = Ed.improving(tuple(tu), vt)
        if not Is and not It: break
        ns = s4a(g, sg, tu, Is) if Is else list(sg)
        nt = list(tu)
        if It:
            av, ach = s4b_arena_vals(g, sg, tu, It)
            nx = [sg[v] if g.owner[v] == 0 else tu[v] for v in range(n)]
            own = [R.play_value(E, nx, v) for v in range(n)]
            if not all(E.key(own[v]) == E.key(av[v]) for v in range(n)):   # tau not value-optimal: SPEC's S4b
                nt = [ach[v] if g.owner[v] == 1 else tu[v] for v in range(n)]
        fb = 0
        if ns == sg and nt == tu:
            fb = 1
            if Is: ns = switch_all(g, E, sg, vs, Is)
            else:
                for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
        sg, tu = ns, nt
        states.append((tuple(sg), tuple(tu))); fbs.append(fb)
    return states, fbs, lams


def Gu(g, tu, u):
    n = g.n
    succ = [list(g.succ[v]) if (g.owner[v] == 0 or v == u) else [tu[v]] for v in range(n)]
    if MUT == "ru": succ[u] = [tu[u]]
    return pg.Game(list(g.prio), list(g.owner), succ)


def all_simple_values(ctx, tu, cyc):
    """vals[x] = list of (edges, key) over simple paths of G_tau from x ending at a vertex of cyc (paths may pass cyc vertices)"""
    g, n, E = ctx.g, ctx.n, ctx.E
    out = {}
    for x in range(n):
        res = []
        def dfs(y, vis, path):
            if y in cyc:
                m = 0
                for p in path[:-1]:
                    if E.rank[p] > E.rank[y]: m |= E.bit[p]
                res.append((len(path) - 1, E.key((y, m, len(path) - 1))))
            for z in ([tu[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))):
                if z not in vis:
                    vis.add(z); path.append(z); dfs(z, vis, path); path.pop(); vis.discard(z)
        dfs(x, {x}, [x])
        out[x] = res
    return out


def bj_table(ctx, sv):
    n = ctx.n
    B = {}
    for x in range(n):
        row, cur = [], None
        best = {}
        for e, k in sv[x]:
            if e not in best or k > best[e]: best[e] = k
        for j in range(n):
            if j in best and (cur is None or best[j] > cur): cur = best[j]
            row.append(cur)
        B[x] = row
    return B


def lev(ctx, B, vals):
    n = ctx.n; L = -1
    for j in range(n):
        if all(B[x][j] is None or ctx.key(vals[x]) >= B[x][j] for x in range(n)): L = j
        else: break
    return L


def check_game(gp, s, t, st, name):
    g, n = gp, gp.n
    runner = DC.Runner(gp)
    states, fbs = runner.run(s, t)
    ctx = R.Ctx(gp); E = ctx.E
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    Ed = Engine(dual(gp))
    for k, (a, b) in enumerate(states):
        vt, _ = Ed.evaluate(tuple(b[v] if g.owner[v] == 1 else -1 for v in range(n)))
        I[k]["vt"] = vt; I[k]["It"] = set(Ed.improving(tuple(b), vt))
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    st.inc("runs"); st.inc("states", len(I))
    tauk = [tuple(b[v] for v in range(n) if g.owner[v] == 1) for _, b in states]
    key = [(I[k]["lamX"], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(ctx, gp, I, fbs, k0, k1, Q, st, name, runner)
        k0 = k1 + 1


def check_phase(ctx, g, I, fbs, a, b, Q, st, name, runner):
    n, E = ctx.n, ctx.E
    st.inc("phases")
    tu = I[a]["tu"]; lam = I[a]["lamX"]
    cyc = frozenset(v for v in range(n) if lam[v] == v)
    f = sum(1 for k in range(a, b) if fbs[k])
    hon = [k for k in range(a, b + 1) if I[k]["xi"] == I[k]["w"]]
    Dk = {k: frozenset(I[k]["D"]) for k in range(a, b + 1)}
    for k in range(a, b + 1):
        if not Dk[k] and k not in hon: st.bad("D0HON", f"{name}@{k}: D = {{}} but not W-honest")
    fin = sum(1 for k in range(a, b) if fbs[k] and k not in hon and hon and hon[0] < k < hon[-1])
    N = len(hon)
    bnd, bndp = f + 4 * n * n - 3 * n, fin + 4 * n * n - 3 * n
    if MUT == "hon": bndp = fin + n - 1
    st.inc("HON_phases"); st.mxr("HON_max_honest", (N, f"{name}@{a} n {n} f {f} f_in {fin}"))
    if N > bnd: st.bad("HON", f"{name}@{a}: {N} > {bnd}")
    if N > bndp: st.bad("HONp", f"{name}@{a}: {N} > {bndp}")
    if fin: st.inc("f_in_phases"); st.inc("f_in_total", fin)
    exact = n <= LEVMAX
    LEV = {}
    if exact:
        sv = all_simple_values(ctx, tu, cyc)
        B = bj_table(ctx, sv)
        for k in range(a, b + 1): LEV[k] = lev(ctx, B, I[k]["xi"])
        for k in range(a, b + 1):
            st.inc("S0_checks")
            if LEV[k] < 0: st.bad("S0", f"{name}@{k}: LEV < 0")
            if k > a and LEV[k] < LEV[k - 1]: st.bad("S0", f"{name}@{k}: LEV drops")
    # step 1 over gaps
    for h, h2 in zip(hon, hon[1:]):
        if any(fbs[k] for k in range(h, h2)):
            st.inc("gaps_with_fallback")
            if fbs[h]: st.inc("gaps_fallback_at_h")
            continue
        st.inc("S1_gaps")
        for k in range(h, h2):
            if any(ctx.key(I[k + 1]["w"][v]) < ctx.key(I[k]["w"][v]) for v in range(n)): st.bad("S1_WM", f"{name}@{k}")
        if I[h + 1]["lamW"] != lam: st.bad("S1_lam", f"{name}@{h + 1}: lambda_W(h + 1) != lambda")
        if exact:
            j = min(LEV[h] + (2 if MUT == "s1" else 1), n - 1)
            st.inc("S1_step_checks")
            if any(B[x][j] is not None and ctx.key(I[h + 1]["w"][x]) < B[x][j] for x in range(n)):
                st.bad("S1_step", f"{name}@{h}: W_(h+1) below B_(LEV+1) (LEV {LEV[h]})")
            if LEV[h2] < min(LEV[h] + 1, n - 1): st.bad("S1_rise", f"{name}@{h}->{h2}: LEV {LEV[h]} -> {LEV[h2]}")
            if LEV[h] < n - 1: st.inc("S1_rise_checks_unsat")
    # step 2, step 3
    if exact:
        for h in hon:
            if LEV[h] == n - 1:
                st.inc("S2_checks")
                if any(B[x][n - 1] is not None and ctx.key(I[h]["xi"][x]) != B[x][n - 1] for x in range(n)): st.bad("S2", f"{name}@{h}")
        sat = [h for h in hon if LEV[h] == n - 1]
        if sat:
            t0, hN = sat[0], hon[-1]
            st.inc("S3_phases"); st.mxr("S3_max_span", (hN - t0, f"{name}@{a} n {n}"))
            if any(I[k]["xi"] != I[t0]["xi"] for k in range(t0, hN + 1)): st.bad("S3", f"{name}@{t0}: Xi not constant")
            if hN - t0 > 4 * n * (n - 1): st.bad("S3", f"{name}@{t0}: span {hN - t0}")
    # SAT0 at every state of the phase with no W-improving edge
    for k in range(a, b + 1):
        if I[k]["Iw"]: continue
        st.inc("SAT0_states")
        if exact:
            wc = frozenset(v for v in range(n) if I[k]["lamW"][v] == v)
            svw = sv if wc == cyc else all_simple_values(ctx, tu, wc)
            for x in range(n):
                for e, kk in svw[x]:
                    if ctx.key(I[k]["w"][x]) < kk: st.bad("SAT0", f"{name}@{k}: x {x}"); break
            if k in hon and LEV[k] != n - 1: st.bad("SAT0", f"{name}@{k}: honest, no W-improving edge, LEV {LEV[k]}")
    # HON-FB
    for h in hon:
        if h >= b or not fbs[h]: continue
        st.inc("FB_cases")
        S, T = I[h], I[h + 1]
        for (x, z) in S["Iw"]:
            path, _ = R.lasso(S["wn"], z)
            flat = S["lamW"][x] == x and x in path and all(E.rank[y] < E.rank[x] for y in path[:path.index(x)])
            if not flat: st.bad("FB_i", f"{name}@{h}: edge {(x, z)} not flat")
        if T["w"] != S["w"]: st.bad("FB_ii", f"{name}@{h}")
        if T["Iw"]: st.bad("FB_iii", f"{name}@{h}")
        if T["xi"] != T["w"]: st.bad("FB_iv", f"{name}@{h + 1}: not honest")
        if exact and LEV[h + 1] != n - 1: st.bad("FB_iv", f"{name}@{h + 1}: not saturated")
        last = (h + 1 == b)
        if MUT == "fb4": last = not last
        if not last: st.bad("FB_iv", f"{name}@{h + 1}: not the last state of the phase")
    # HON-0 and REC-0's difference
    epochs, k = [], a
    while k <= b:
        e = k
        sq = lambda j: tuple(I[j]["hn"][q] for q in Q)
        while e + 1 <= b and sq(e + 1) == sq(k): e += 1
        epochs.append((k, e)); k = e + 1
    d0 = sum(1 for k in range(a, b + 1) if not Dk[k])
    N0 = sum(1 for (p, q) in epochs if not Dk[p])
    tr0 = sum(1 for (p, q) in epochs if not Dk[p] for k in range(p, q + 1) if k < b)
    st.inc("H0_phases"); st.mxr("H0_max_N0", (N0, f"{name}@{a} n {n}")); st.mxr("H0_max_D0_states", (d0, f"{name}@{a} n {n}"))
    for nm, val in (("a", d0), ("b", N0), ("c", tr0)):
        if val > fin + 4 * n * n - 3 * n: st.bad("H0" + nm, f"{name}@{a}: {val}")
    rec0 = (f + 1) * (n + 1) + 4 * n * (n - 1) + 1
    if rec0 - (f + 4 * n * n - 3 * n) != f * n + 2: st.bad("H0_rec0", f"{name}@{a}")
    if N0 > rec0: st.bad("H0_rec0", f"{name}@{a}: REC-0 itself fails")
    # RESTRICT_u, REPRO_u, REC-1
    check_u(ctx, g, I, fbs, a, b, Q, Dk, fin, st, name)


def check_u(ctx, g, I, fbs, a, b, Q, Dk, fin, st, name):
    n = ctx.n
    tu = I[a]["tu"]
    m = sum(len(set(s)) for s in g.succ); D = max(len(set(s)) for s in g.succ)
    cache = {}
    def gctx(u):
        if u not in cache:
            G = Gu(g, tu, u); cache[u] = (G, Engine(G), Engine(dual(G)))
        return cache[u]
    for k in range(a, b + 1):
        if len(Dk[k]) > 1: continue
        us = list(Dk[k]) if Dk[k] else Q[:RUMAX]
        for u in us:
            G, Eu, Edu = gctx(u)
            S = I[k]; sg = S["sg"]
            st.inc("RU_checks")
            xe, tf = Eu.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
            hn = [sg[v] if g.owner[v] == 0 else tf[v] for v in range(n)]
            xi2 = [R.play_value(Eu, hn, v) for v in range(n)]
            if xi2 != S["xi"] or [tuple(x) for x in xe] != S["xi"]: st.bad("RU_i", f"{name}@{k}: u {u} Xi' != Xi"); continue
            Is2 = set(Eu.improving(tuple(sg), xe))
            if Is2 != S["Is"]: st.bad("RU_ii", f"{name}@{k}: u {u} I_sigma' != I_sigma")
            if S["Is"]:
                if s4a(G, sg, tu, Is2) != s4a(g, sg, tu, S["Is"]): st.bad("RU_ii", f"{name}@{k}: u {u} S4a differs")
                if switch_all(G, Eu, sg, xe, Is2) != switch_all(g, ctx.E, sg, S["xi"], S["Is"]): st.bad("RU_ii", f"{name}@{k}: S4c differs")
            vt2, _ = Edu.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
            if [tuple(x) for x in vt2] != [tuple(x) for x in S["vt"]]: st.bad("RU_iii", f"{name}@{k}: u {u} dual valuation differs")
            It2 = set(Edu.improving(tuple(tu), vt2))
            EG = set((v, w) for v in range(n) for w in G.succ[v])
            if It2 != set(e for e in S["It"] if e in EG): st.bad("RU_iii", f"{name}@{k}: u {u} I_tau' != I_tau ∩ E(G^u)")
            if k < b and It2:
                st.inc("RU_iv_checks")
                av, _ = s4b_arena_vals(G, sg, tu, It2)
                if not all(Eu.key(av[v]) == Eu.key(S["w"][v]) for v in range(n)): st.bad("RU_iv", f"{name}@{k}: u {u}")
    # u-runs and REPRO_u
    for u in Q:
        k = a
        while k <= b:
            if not Dk[k] <= {u}: k += 1; continue
            e = k
            while e + 1 <= b and Dk[e + 1] <= {u}: e += 1
            ln = e - k + (1 if e < b else 0)       # in-phase transitions with source in J
            if all(not Dk[j] for j in range(k, e + 1)) and u not in Q[:RUMAX]: k = e + 1; continue
            st.inc("RP_runs"); st.mxr("RP_max_len", (ln, f"{name}@{k} u {u} n {n}"))
            G = gctx(u)[0]
            sts, fb2, lams = run_ntau(G, I[k]["sg"], tu, ln)
            if len(fb2) < ln: st.bad("RP", f"{name}@{k}: u {u} N5^tau stopped early"); k = e + 1; continue
            for j in range(ln + 1):
                if sts[j] != (I[k + j]["sg"], tuple(I[k + j]["tu"])): st.bad("RP", f"{name}@{k + j}: u {u} state differs"); break
            if [bool(x) for x in fb2[:ln]] != [bool(x) for x in fbs[k:k + ln]]: st.bad("RP", f"{name}@{k}: u {u} fallback types differ")
            for j in range(e - k + 1):
                if lams[j] != I[k]["lamX"]: st.bad("RP_phase", f"{name}@{k + j}: u {u} lambda' != lambda")
            if ln > tstar(n, sum(len(set(s)) for s in G.succ), len(set(g.succ[u])), D) + 1: st.bad("EP1u", f"{name}@{k}")
            k = e + 1
    # REC-1
    ints, k = [], a
    while k <= b:
        if len(Dk[k]) != 1: k += 1; continue
        e = k
        while e + 1 <= b and Dk[e + 1] == Dk[k]: e += 1
        ints.append((k, e)); k = e + 1
    xdir = sum(1 for k in range(a, b) if len(Dk[k]) == 1 and len(Dk[k + 1]) == 1 and Dk[k] != Dk[k + 1])
    xbig = sum(1 for k in range(a, b) if len(Dk[k]) >= 2 and len(Dk[k + 1]) == 1)
    ent = {"start": 0, "D0": 0, "dir": 0, "big": 0}
    for p, q in ints:
        if p == a: ent["start"] += 1
        elif not Dk[p - 1]: ent["D0"] += 1
        elif len(Dk[p - 1]) == 1: ent["dir"] += 1
        else: ent["big"] += 1
    for kk, v in ent.items(): st.inc("R1_entries_" + kk, v)
    bound = 1 + (fin + 4 * n * n - 3 * n) + xdir + xbig
    if MUT == "r1": bound = xdir + xbig
    st.inc("R1_phases"); st.inc("R1_intervals", len(ints)); st.mxr("R1_max_intervals", (len(ints), f"{name}@{a} n {n}"))
    if len(ints) > bound: st.bad("R1a", f"{name}@{a}: {len(ints)} > {bound}")
    if xdir: st.inc("R1_Xdir", xdir)
    if xbig: st.inc("R1_Xbig", xbig)
    Tq = max([tstar(n, sum(len(set(s)) for s in Gu(g, tu, u).succ), len(set(g.succ[u])), D) for u in Q] or [0])
    for p, q in ints:
        u = next(iter(Dk[p]))
        jk = p
        while jk - 1 >= a and Dk[jk - 1] <= {u}: jk -= 1
        je = q
        while je + 1 <= b and Dk[je + 1] <= {u}: je += 1
        ln = je - jk + (1 if je < b else 0)
        st.mxr("R1_max_interval_states", (q - p + 1, f"{name}@{p} u {u}"))
        if q - p + 1 > ln + 1: st.bad("R1b", f"{name}@{p}: |I| {q - p + 1} > len(J) + 1 = {ln + 1}")
        if q - p + 1 > tstar(n, sum(len(set(s)) for s in Gu(g, tu, u).succ), len(set(g.succ[u])), D) + 2: st.bad("R1b_T", f"{name}@{p}")
    d1 = sum(1 for k in range(a, b + 1) if len(Dk[k]) == 1)
    if d1 > (1 + fin + 4 * n * n - 3 * n + xdir + xbig) * (Tq + 2): st.bad("R1c", f"{name}@{a}")
    if all(len(Dk[k]) <= 1 for k in range(a, b + 1)):
        st.inc("R1_d_phases")
        if xbig: st.bad("R1d", f"{name}@{a}: X_big != 0")
        if b - a + 1 > (fin + 4 * n * n - 3 * n) + (1 + fin + 4 * n * n - 3 * n + xdir) * (Tq + 2): st.bad("R1d", f"{name}@{a}")


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1618)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); check_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); check_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        s, t = R.read_start(gp, a[2]) if len(a) > 2 else R.starts(gp, 0, None)
        check_game(gp, s, t, st, os.path.basename(a[1]))
    print("MODE", " ".join(a), "MUT", MUT or "-", "LEVMAX", LEVMAX, "RUMAX", RUMAX)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
