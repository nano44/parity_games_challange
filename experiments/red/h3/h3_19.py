#!/usr/bin/env python3
"""Box 45d (L-RED successor 19; Lead 05:44Z): exact checker of P-N5-H3 (docs/si/P-N5-H3-box16.md, sha1 680e4528), written from the
packet's §1-§6 text (not from L-SI's gdnc.py / tcdir.py). Trace: experiments/red/o1/o1_19.trace (own copy of n5.py's loop).
Per state k: Ξ_k, σ̄_k from SPEC S1 (Engine.evaluate); W_k(v) := S1 value of the (σ_k, τ_k)-play from v, computed from the play itself
(lasso; cycle node = top-ranked cycle vertex; P = prefix before the first visit of the cycle node, ranked above it; ℓ = edges to it).
D_k := {Odd u : σ̄_k(u) != τ_k(u)}; u(v) := first vertex of D_k on v's (σ_k, τ_k)-play (v included); R_D := {v : u(v) exists}.
(h3_D): λ_Ξ(u) = λ_W(u) for u ∈ D_k. lev(x, y) := ∞ (cycle nodes differ) / top rank of P(x) Δ P(y) / −1 (only lengths) / ⊥ (equal).
M_D := max_{u ∈ D_k} lev(Ξ_k(u), W_k(u)), ⊥ if D_k = ∅. COARSE_L(x) := (c, P ∩ V_{>L}) (ranks > L).
Checks: RD_A   R55 (a) Ξ = W on F_D (sanity of the W computation);
        TCC    TC-CLASS: λ_Ξ(v) = λ_Ξ(u(v)), λ_W(v) = λ_W(u(v)) for v ∈ R_D (every state);
        C2H3   at every (h3_D) state: COARSE_L(Ξ(v)) = COARSE_L(W(v)) for all v, all L from max(M_D, −1) to n − 1;
        WMG    W_{k+1} ⊵ W_k pointwise at every in-phase S4a transition;
        FRZ    (frz_move_gap = max over qualifying runs of (index of the last COARSE_L(W) change) − (n − 1); > 0 is a kill)
        on every maximal fallback-free in-phase run S with (h3_D) at all its states, L := max(max_S M_D, −1): COARSE_L(W) constant
               from state k0 + n − 1 on (non-vacuous only if |S| >= n states).
Reported: counts, longest qualifying run (states) vs n, FRZ non-vacuous runs, and the 'kill' = a qualifying run of >= n states whose
COARSE_L(W) moves after its (n − 1)-th state. Usage: h3_19.py file game.pg [start.json]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "o1"))
import o1_19 as O, pg, verify
BOT, INF = -2, 10 ** 9

def play_val(E, g, sig, tau, v):
    n = g.n; seen = {}; path = []
    while v not in seen:
        seen[v] = len(path); path.append(v); v = sig[v] if g.owner[v] == 0 else tau[v]
    cyc = path[seen[v]:]; c = max(cyc, key=lambda x: E.rank[x])
    i = path.index(c); P = 0
    for x in path[:i]:
        if E.rank[x] > E.rank[c]: P |= E.bit[x]
    return (c, P, i), path

def lev(E, x, y):
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    if d: return d.bit_length() - 1
    return -1 if x[2] != y[2] else BOT

def coarse(x, L): return (x[0], x[1] & ~((1 << (L + 1)) - 1)) if L >= 0 else (x[0], x[1])

def analyse(g, start=None, cap=5000):
    n = g.n; S, FB, E = O.trace(g, start, "n5", cap)
    ev = [E.evaluate(s) for s, _ in S]; Xi = [X for X, _ in ev]; SB = [B for _, B in ev]
    r = dict(pairoc_max=0, lc2_slack=-10**9, n=n, ITER=len(FB), states=0, h3_states=0, c2_checks=0, tcc_checks=0, wmg_checks=0, frz_runs=0, frz_nonvac=0,
             frz_longest=0, frz_gap=-10 ** 9, frz_move_gap=-10 ** 9, frz_moves=0, lc_checks=0, lc_maxchg=0, lc_ratio=0.0, lc_slack=-10 ** 9, off_stretches=0, off_changes=0, off_maxpv=0, off_returns=0, off_inrun_maxpv=0, rstick_checks=0, frz_content=0, frz_L=[], snp_checks=0, crossings=0, xsn_pre_ep=0, xsn_pre_run=0, xep_slack=-10 ** 9, fails=[])
    lamX = [tuple(x[0] for x in X) for X in Xi]
    W, lamW, D, U, MD, H3 = [], [], [], [], [], []
    for k, (sig, tau) in enumerate(S):
        Wk, uk = [], []
        Dk = {u for u in range(n) if g.owner[u] == 1 and SB[k][u] != tau[u]}
        for v in range(n):
            val, path = play_val(E, g, sig, tau, v); Wk.append(val)
            uk.append(next((x for x in path if x in Dk), None))
        W.append(Wk); lamW.append(tuple(x[0] for x in Wk)); D.append(Dk); U.append(uk)
        h3 = all(lamX[k][u] == lamW[k][u] for u in Dk); H3.append(h3)
        md = max((lev(E, Xi[k][u], Wk[u]) for u in Dk), default=BOT); MD.append(md)
        r["states"] += 1
        for v in range(n):
            if uk[v] is None and tuple(Xi[k][v]) != tuple(Wk[v]): r["fails"].append(f"RD_A k={k} v={v}")
            if uk[v] is not None:
                r["tcc_checks"] += 1
                if lamX[k][v] != lamX[k][uk[v]] or lamW[k][v] != lamW[k][uk[v]]: r["fails"].append(f"TCC k={k} v={v}")
        if h3:
            r["h3_states"] += 1
            for L in range(max(md, -1), n):
                r["c2_checks"] += 1
                if any(coarse(Xi[k][v], L) != coarse(Wk[v], L) for v in range(n)): r["fails"].append(f"C2H3 k={k} L={L} MD={md}"); break
    # phases, WM-G, FRZ runs
    a = 0; N = len(S)
    while a < N:
        b = a
        while b + 1 < N and lamX[b + 1] == lamX[a] and S[b + 1][1] == S[a][1]: b += 1
        for k in range(a, b):
            if not FB[k]:
                r["wmg_checks"] += 1
                if any(E.key(W[k + 1][v]) < E.key(W[k][v]) for v in range(n)): r["fails"].append(f"WMG k={k}")
        # ---- P-N5-XEP (docs/new/P-N5-XEP-box44.md, sha1 237dd5eb): R-STICK_D, SN-PREFIX_D (a), crossings, X_SN^pre, X-EP bound
        RD = [{v for v in range(n) if U[k][v] is not None} for k in range(len(S))]
        split = lambda k, v: lamW[k][v] != lamX[k][v]
        Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1]
        for k in range(a, b):
            if FB[k]: continue
            for v in RD[k]:
                if split(k, v):
                    r["rstick_checks"] += 1
                    if v not in RD[k + 1]: r["fails"].append(f"RSTICK k={k} v={v}")
        # SN-PREFIX_D (a): within each S4a run, unsplit states of v form a prefix
        k = a
        while k < b:
            k0 = k
            while k < b and not FB[k]: k += 1
            for v in range(n):
                r["snp_checks"] += 1; seen_split = False
                for t in range(k0, k + 1):
                    if split(t, v): seen_split = True
                    elif seen_split: r["fails"].append(f"SNPREFIX v={v} t={t}"); break
            k += 1
        epid = [0] * (b - a + 1)
        for k in range(a + 1, b + 1): epid[k - a] = epid[k - a - 1] + (tuple(SB[k][q] for q in Q) != tuple(SB[k - 1][q] for q in Q))
        Nep = epid[-1] + 1; XD = 0; xpre = {}
        for k in range(a, b):
            if RD[k] == RD[k + 1]: continue
            XD += 1; r["crossings"] += 1
            e = epid[k - a]
            if epid[k + 1 - a] != e: continue
            efb = [t for t in range(a, b) if FB[t] and epid[t - a] == e]
            if len(efb) >= n - 1 and k > efb[n - 2]: continue
            if any(not split(k, v) and ((v in RD[k]) != (v in RD[k + 1])) for v in range(n)):
                xpre[e] = xpre.get(e, 0) + 1
                run0 = k
                while run0 > a and not FB[run0 - 1] and epid[run0 - 1 - a] == e: run0 -= 1
                xpre[(e, run0)] = xpre.get((e, run0), 0) + 1
        pe = max([v for kk, v in xpre.items() if not isinstance(kk, tuple)] + [0]); pr = max([v for kk, v in xpre.items() if isinstance(kk, tuple)] + [0])
        r["xsn_pre_ep"] = max(r["xsn_pre_ep"], pe); r["xsn_pre_run"] = max(r["xsn_pre_run"], pr)
        bound = (Nep - 1) + Nep * (n * n + n + 4 * n * (n - 1)) + sum(v for kk, v in xpre.items() if not isinstance(kk, tuple))
        r["xep_slack"] = max(r["xep_slack"], XD - bound)
        if XD > bound: r["fails"].append(f"XEP XD={XD} bound={bound}")
        # maximal fallback-free runs of states inside [a, b] with (h3_D) at every state
        k = a
        while k <= b:
            if not H3[k]: k += 1; continue
            k0 = k
            while k + 1 <= b and not FB[k] and H3[k + 1]: k += 1
            k1 = k; L = max(max(MD[k0:k1 + 1]), -1); length = k1 - k0 + 1
            last = None
            for t in range(k0, k1):
                if any(coarse(W[t + 1][v], L) != coarse(W[t][v], L) for v in range(n)): last = t + 1 - k0; r["frz_moves"] += 1
            if last is not None: r["frz_move_gap"] = max(r["frz_move_gap"], last - (n - 1))
            # ---- CONJECTURE OFFSET-ONCE (docs/si/N5-RUND-box17.md §5-§6, l-si d61b3cf0): stretch_D = maximal sub-run of this run with
            # D, R_D and every gate's (Ξ(u), W(u)) constant; Δ(v) = w(P(W(v))) − w(P(Ξ(v))); a RETURN = Δ(v) back to a value it left
            off = lambda t, v: E.weight(W[t][v][1]) - E.weight(Xi[t][v][1])
            sig = lambda t: (frozenset(D[t]), frozenset(v for v in range(n) if U[t][v] is not None), tuple(sorted((u, tuple(Xi[t][u]), tuple(W[t][u])) for u in D[t])))
            t = k0; runchg = {}
            while t <= k1:
                s0 = t
                while t + 1 <= k1 and sig(t + 1) == sig(s0): t += 1
                r["off_stretches"] += 1
                for v in range(n):
                    seq = [off(x, v) for x in range(s0, t + 1)]; left = set(); chg = 0
                    for i in range(1, len(seq)):
                        if seq[i] != seq[i - 1]:
                            chg += 1; left.add(seq[i - 1])
                            if seq[i] in left: r["off_returns"] += 1   # OFFSET-ONCE is DEAD (L-SI offret_n23, Lead 07:20Z): counted, not a FAIL
                    r["off_changes"] += chg; r["off_maxpv"] = max(r["off_maxpv"], chg)
                    # ---- CONJECTURE LEVEL-COUNT (L-SI, Lead 07:20Z): offset changes of v per stretch_D <= #distinct levels at which s^W(v)
                    # or s^Ξ(v) rises; and (pay form) no two offset changes paid (TWIN-GAP (i): d > 0 by s^W, d < 0 by s^Ξ) at one level
                    lvls = set(); pay = []; SL = set(); ocp = {}       # SL: (score, level) pairs of rises; ocp: pair -> #offset changes using it
                    for x in range(s0, t):
                        dW = W[x][v][1] ^ W[x + 1][v][1]; dX = Xi[x][v][1] ^ Xi[x + 1][v][1]
                        lw = dW.bit_length() - 1 if dW and E.weight(W[x + 1][v][1]) > E.weight(W[x][v][1]) else None
                        lx = dX.bit_length() - 1 if dX and E.weight(Xi[x + 1][v][1]) > E.weight(Xi[x][v][1]) else None
                        for l in (lw, lx):
                            if l is not None: lvls.add(l)
                        d = off(x + 1, v) - off(x, v)
                        if lw is not None: SL.add(("W", lw))
                        if lx is not None: SL.add(("X", lx))
                        if d:
                            pay.append(lw if d > 0 else lx)
                            for pr in ((("W", lw),) if lw is not None else ()) + ((("X", lx),) if lx is not None else ()): ocp[pr] = ocp.get(pr, 0) + 1
                    if chg:
                        r["lc_checks"] += 1; r["lc_maxchg"] = max(r["lc_maxchg"], chg); r["lc_slack"] = max(r["lc_slack"], chg - len(lvls))
                        r["lc_ratio"] = max(r["lc_ratio"], chg / n)
                        if chg > len(lvls): r["lc_viol"] = r.get("lc_viol", 0) + 1      # LEVEL-COUNT dead (R78): counter, not FAIL
                        if None in pay or len(set(pay)) < len(pay): r["lp_viol"] = r.get("lp_viol", 0) + 1   # dead with LEVEL-COUNT: counter
                        # ---- L-SI §15 (l-si 4b0aeae6): CONJECTURE LC2 |OC(v)| <= |SL(v)|; CONJECTURE PAIR-OC: no (score, level) pair rises at two
                        # offset changes of v in one stretch_D segment
                        r["pairoc_max"] = max(r.get("pairoc_max", 0), max(ocp.values(), default=0)); r["lc2_slack"] = max(r.get("lc2_slack", -10**9), chg - len(SL))
                        if chg > len(SL): r["fails"].append(f"LC2 v={v} states {s0}..{t} chg={chg} SL={sorted(SL)}")
                        if any(c > 1 for c in ocp.values()): r["fails"].append(f"PAIROC v={v} states {s0}..{t} pairs={ocp}")
                t += 1
            for v in range(n): runchg[v] = sum(1 for x in range(k0, k1) if off(x + 1, v) != off(x, v))
            r["off_inrun_maxpv"] = max([r["off_inrun_maxpv"]] + list(runchg.values()))
            r["frz_runs"] += 1; r["frz_longest"] = max(r["frz_longest"], length); r["frz_gap"] = max(r["frz_gap"], length - n)
            if length >= n + 1:                     # non-vacuous: a state after k0 + n − 1 exists (L-SI's convention, N5-RUND §3)
                r["frz_L"].append((k0, length, L, max((W[t][v][1] >> (L + 1)).bit_length() for t in range(k0, k1 + 1) for v in range(n)) if L >= 0 else -1))
                if any(coarse(W[t][v], L)[1] for t in range(k0, k1 + 1) for v in range(n)): r["frz_content"] += 1
                r["frz_nonvac"] += 1; ref = [coarse(W[k0 + n - 1][v], L) for v in range(n)]
                for t in range(k0 + n - 1, k1 + 1):
                    if [coarse(W[t][v], L) != ref[v] for v in range(n)].count(True): r["fails"].append(f"FRZ k0={k0} t={t} L={L}"); break
            k += 1
        a = b + 1
    win, ws = E.regions(S[-1][0]); e = verify.check(g, win, ws)
    if e: r["fails"].append("OUT_STRAT " + e[0])
    return r

if __name__ == "__main__" and sys.argv[1] == "file":
    a = sys.argv; g = pg.parse("".join(l for l in open(a[2]) if not l.lstrip().startswith("%")))
    st = json.load(open(a[3]))["start"] if len(a) > 3 and a[3].endswith(".json") else None
    print(json.dumps(analyse(g, st)))

def libmain(seed, R, nmax, files):
    import random
    rng = random.Random(seed); tot = {}; fails = {}; best = {}; bst = {}; runs = 0
    for f in files:
        try: g = pg.parse("".join(l for l in open(f) if not l.lstrip().startswith("%")))
        except Exception: continue
        if g.n > nmax or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) > 1) < 1: continue
        for k in range(R + 1):
            st = None if k == 0 else [rng.choice(g.succ[v]) for v in range(g.n)]
            r = analyse(g, st); runs += 1
            if r["frz_nonvac"]: print("NONVAC", os.path.basename(f), "S3" if st is None else json.dumps(st), r["n"], r["frz_L"], "content", r["frz_content"], "Dsizes", r.get("dmax"), flush=True)
            for kk in ("states", "h3_states", "c2_checks", "tcc_checks", "wmg_checks", "frz_runs", "frz_nonvac", "frz_moves", "frz_content", "off_stretches", "off_changes", "off_returns", "lc_checks", "rstick_checks", "snp_checks", "crossings"): tot[kk] = tot.get(kk, 0) + r[kk]
            for x in r["fails"]:
                fails[x.split()[0]] = fails.get(x.split()[0], 0) + 1
                if fails[x.split()[0]] <= 3: print("FAIL", f, x, st, flush=True)
            for kk in ("frz_longest", "frz_gap", "frz_move_gap", "xsn_pre_ep", "xsn_pre_run", "xep_slack", "off_maxpv", "off_inrun_maxpv", "lc_maxchg", "lc_slack", "lc_ratio"):
                if kk not in best or r[kk] > best[kk][0]: best[kk] = (r[kk], os.path.basename(f), st is None); bst[kk] = dict(file=f, start=st)
    json.dump(bst, open(os.environ.get("H3BEST", "/dev/null"), "w"))
    print("RUNS", runs, "TOT", tot, "FAILS", fails, "BEST", best, flush=True)

def randmain(seed, count, nmin, nmax, kmax):
    import random
    rng = random.Random(seed); tot = {}; fails = {}; best = {}
    for i in range(count):
        n = rng.randint(nmin, nmax); prio = [rng.randrange(2 * n) for _ in range(n)]; owner = [0 if rng.random() < 0.6 else 1 for _ in range(n)]
        succ = [sorted(set(rng.sample(range(n), rng.choice((1, 2, 2, 3)) if owner[v] == 0 else 1))) for v in range(n)]
        for o in rng.sample(range(n), rng.randint(2, kmax)): owner[o] = 1; succ[o] = sorted(set(rng.sample(range(n), rng.randint(2, max(2, n // 2)))))
        g = pg.Game(prio, owner, succ); st = None if i % 2 == 0 else [rng.choice(g.succ[v]) for v in range(n)]
        r = analyse(g, st)
        for kk in ("states", "h3_states", "c2_checks", "tcc_checks", "wmg_checks", "frz_runs", "frz_nonvac", "frz_moves", "frz_content", "off_stretches", "off_changes", "off_returns", "lc_checks", "rstick_checks", "snp_checks", "crossings"): tot[kk] = tot.get(kk, 0) + r[kk]
        for x in r["fails"]:
            fails[x.split()[0]] = fails.get(x.split()[0], 0) + 1
            if fails[x.split()[0]] <= 3: print("FAIL", x, json.dumps(dict(prio=prio, owner=owner, succ=succ, start=st)), flush=True)
        for kk in ("frz_longest", "frz_gap", "frz_move_gap", "xsn_pre_ep", "xsn_pre_run", "xep_slack", "off_maxpv", "off_inrun_maxpv", "lc_maxchg", "lc_slack", "lc_ratio"):
            if kk not in best or r[kk] > best[kk]: best[kk] = r[kk]
    print("RAND", count, "TOT", tot, "FAILS", fails, "BEST", best, flush=True)

if __name__ == "__main__" and sys.argv[1] == "lib": libmain(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), sys.argv[5:])
if __name__ == "__main__" and sys.argv[1] == "rand": randmain(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
