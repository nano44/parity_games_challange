#!/usr/bin/env python3
"""REFEREE successor 18: own control for packet P-N5-COMPOSE (L-SI box 28, l-si 3ca0932d, sha1 e1b977aa).
Own engine rl_engine (SPEC S1-S5 from the text); no lane code imported. Per N5 run it checks, for BOTH players
(Even: Xi on G, sigma, I_sigma; Odd: U = Odd's valuation of tau on G^d, tau, I_tau):
  FSW   every switch goes along an improving edge of the source state          (packet §1 F-SW)
  FMON  Xi (U) non-decreasing at every vertex and transition (G / G^d order)  (packet §1 F-MON)
  SUCC  Xi_t(sigma_t v) non-decreasing                                         (§2 Xi-SUCC)
  SWR   ENT_R(v, c) <= 1 + RISE_R(c) on the whole run, every lambda-run, every phase, and random stretches  (§2)
  SWRS  strong form: between two consecutive entries e < e' of v into c, Xi(c) changes at a transition in [e+1, e'-1]
  LEN   on every lambda-run: cycle node of c fixed, l moves the preferred way inside a P-block, l <= n-1,
        RISE <= PCH + (PCH + 1)(n - 1)                                                                     (§3)
  CMP   on every lambda-run: sum SW <= sum_{(v,c), SW(v)>0} (1 + RISE(c)) <= sum n (PCH(c) + 1) <= m n (P*_R + 1)  (§4)
  PH    on every phase (lambda, tau constant): transitions <= sum SW and the same sums                 (§4, phase part)
  RUN   classification (i) lambda changes, (ii) sigma changes, (iii) lambda^U changes, (iv) rest: (iv) changes tau;
        #(i), #(iii) <= n(n-1); #(ii) <= Even switches on lambda-runs, #(iv) <= Odd switches on lambda^U-runs;
        #lambda-runs <= n(n-1)+1; T <= 2n(n-1) + (n(n-1)+1) n (m_E (P*+1) + m_O (P*^U+1)); fallbacks: Even ones only in (i)/(ii),
        Odd ones only in (iii)/(iv)                                                                          (§5)
MUT controls (must bite): 1 SWR without "+1"; 2 SWR with PCH in place of RISE; 3 LEN without the length term (RISE <= PCH);
4 the phase bound applied to whole lambda-runs (tau-only transitions counted).
Usage: compose_probe.py rand N lo hi seed | FILES... (env RANDSTARTS, MAXN, MUT)"""
import sys, os, random
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE
MUT = int(os.environ.get("MUT", "0"))
EX = []


def fail(cnt, tag, *a):
    cnt[tag + "_V"] += 1
    if len(EX) < 30: EX.append((tag,) + a)


def stretches(keys):
    """maximal runs [i, j] of states with keys constant"""
    out, i, T = [], 0, len(keys) - 1
    while i <= T:
        j = i
        while j < T and keys[j + 1] == keys[i]: j += 1
        out.append((i, j)); i = j + 1
    return out


def side_counts(g, key, strat, vals, own, i, j):
    """switch entries, switches, RISE, PCH of one player on states i..j"""
    n = g.n; ent = Counter(); sw = Counter(); rise = Counter(); pch = Counter()
    for t in range(i, j):
        for v in range(n):
            if g.owner[v] == own and strat[t][v] != strat[t + 1][v]: sw[v] += 1; ent[(v, strat[t + 1][v])] += 1
        for x in range(n):
            a, b = vals[t][x], vals[t + 1][x]
            if a != b:
                rise[x] += 1
                if a[1] != b[1]: pch[x] += 1
    return ent, sw, rise, pch


def check_swr(cnt, g, own, ent, rise, pch, tag, name):
    for (v, c), e in ent.items():
        cnt["SWR_chk"] += 1
        bound = (rise[c] if MUT == 1 else 1 + pch[c] if MUT == 2 else 1 + rise[c])
        if e > bound: fail(cnt, "SWR" + ("_MUT%d" % MUT if MUT in (1, 2) else ""), name, tag, own, v, c, e, rise[c])


def player(cnt, g, gg, own, strat, vals, imp, name, rng, run_info):
    n, T = g.n, len(vals) - 1
    key = gg.key
    # FSW, FMON, SUCC
    for t in range(T):
        I = set(imp[t])
        for v in range(n):
            if g.owner[v] != own: continue
            if strat[t][v] != strat[t + 1][v]:
                cnt["FSW_chk"] += 1
                if (v, strat[t + 1][v]) not in I: fail(cnt, "FSW", name, own, t, v)
            cnt["SUCC_chk"] += 1
            if key(vals[t + 1][strat[t + 1][v]]) < key(vals[t][strat[t][v]]): fail(cnt, "SUCC", name, own, t, v)
        for x in range(n):
            cnt["FMON_chk"] += 1
            if key(vals[t + 1][x]) < key(vals[t][x]): fail(cnt, "FMON", name, own, t, x)
    # SWRS (strong form, whole run)
    for v in range(n):
        if g.owner[v] != own: continue
        entries = {}
        for t in range(T):
            if strat[t][v] != strat[t + 1][v]: entries.setdefault(strat[t + 1][v], []).append(t)
        for c, es in entries.items():
            for e, e2 in zip(es, es[1:]):
                cnt["SWRS_chk"] += 1
                if not any(vals[u][c] != vals[u + 1][c] for u in range(e + 1, e2)): fail(cnt, "SWRS", name, own, v, c, e, e2)
    # SWR on the whole run and on random stretches
    for (i, j) in [(0, T)] + [tuple(sorted(rng.sample(range(T + 1), 2))) for _ in range(3 if T >= 1 else 0)]:
        ent, sw, rise, pch = side_counts(g, key, strat, vals, own, i, j)
        check_swr(cnt, g, own, ent, rise, pch, "stretch", name)
    # lambda-runs
    lam = [tuple(x[0] for x in vals[t]) for t in range(T + 1)]
    runs = stretches(lam)
    m_own = sum(len(g.succ[v]) for v in range(n) if g.owner[v] == own)
    tot_sw = 0; pstar = 0
    for (i, j) in runs:
        ent, sw, rise, pch = side_counts(g, key, strat, vals, own, i, j)
        check_swr(cnt, g, own, ent, rise, pch, "lamrun", name)
        # LEN
        for x in range(n):
            c0 = vals[i][x][0]; blk = 0
            for t in range(i, j):
                a, b = vals[t][x], vals[t + 1][x]
                if b[2] > n - 1: fail(cnt, "LEN_l", name, own, t, x)
                if a == b: continue
                if b[0] != c0: fail(cnt, "LEN_c", name, own, t, x)
                if a[1] == b[1]:
                    blk += 1; cnt["LEN_lonly"] += 1
                    pref = (b[2] < a[2]) if gg.prio[c0] % 2 == 0 else (b[2] > a[2])
                    if not pref: fail(cnt, "LEN_dir", name, own, t, x)
                    if blk > n - 1: fail(cnt, "LEN_blk", name, own, t, x)
                else:
                    blk = 0
                    if gg.weight(b[1]) <= gg.weight(a[1]): fail(cnt, "LEN_w", name, own, t, x)
            cnt["LEN_chk"] += 1
            lb = pch[x] if MUT == 3 else pch[x] + (pch[x] + 1) * (n - 1)
            if rise[x] > lb: fail(cnt, "LEN" + ("_MUT3" if MUT == 3 else ""), name, own, i, j, x, rise[x], pch[x])
        if os.environ.get("MPHI"):     # MATCH-Phi's Corollary per lambda-run (both players; Odd: on G^d with U)
            import matchphi_probe as MP
            for x in range(n):
                rc = gg.rank[vals[i][x][0]]; K = n - 1 - rc
                par = [gg.prio[gg.byrank[rc + 1 + p]] % 2 for p in range(K)]
                seq = [frozenset(r - rc - 1 for r in range(n) if (vals[t][x][1] >> r) & 1) for t in range(i, j + 1)]
                if any(min(s, default=0) < 0 for s in seq): fail(cnt, "MPHI_RC", name, own, i, x)
                p_, nm_ = MP.corollary(seq, par, K, cnt, "MPHI%d" % own)
                cnt["MPHI_nm_max"] = max(cnt["MPHI_nm_max"], nm_)
        # CMP
        S1 = sum(sw.values()); pairs = [(v, c) for v in sw for c in g.succ[v]]
        S2 = sum(1 + rise[c] for v, c in pairs); S3 = sum(n * (pch[c] + 1) for v, c in pairs)
        P = max(pch.values(), default=0); S4 = m_own * n * (P + 1)
        cnt["CMP_chk"] += 1
        if not (S1 <= S2 <= S3 <= S4): fail(cnt, "CMP", name, own, i, j, S1, S2, S3, S4)
        if MUT == 4 and own == 0 and (j - i) > S1: fail(cnt, "PH_MUT4", name, i, j, j - i, S1)
        tot_sw += S1; pstar = max(pstar, P)
        cnt["slack_S1_S2_num"] += S1; cnt["slack_S1_S2_den"] += S2
    run_info[own] = dict(runs=len(runs), sw=tot_sw, pstar=pstar, m=m_own)
    return lam


def analyse(g, start, cnt, name, rng):
    gd = g.dual(); n = g.n
    st = RE.run(g, start); T = len(st) - 1
    cnt["RUNS"] += 1; cnt["TRANS"] += T
    S = [x["s"] for x in st]; Tt = [x["t"] for x in st]
    Xi = [x["Xi"] for x in st]; U = [x["Ut"] for x in st]
    info = {}
    lam = player(cnt, g, g, 0, S, Xi, [x["Is"] for x in st], name, rng, info)
    lamU = player(cnt, g, gd, 1, Tt, U, [x["It"] for x in st], name, rng, info)
    # phases: (lambda, tau) constant
    for (i, j) in stretches([(lam[t], tuple(Tt[t])) for t in range(T + 1)]):
        ent, sw, rise, pch = side_counts(g, g.key, S, Xi, 0, i, j)
        check_swr(cnt, g, 0, ent, rise, pch, "phase", name)
        S1 = sum(sw.values()); pairs = [(v, c) for v in sw for c in g.succ[v]]
        S2 = sum(1 + rise[c] for v, c in pairs); S3 = sum(n * (pch[c] + 1) for v, c in pairs)
        cnt["PH_chk"] += 1
        if not ((j - i) <= S1 <= S2 <= S3): fail(cnt, "PH", name, i, j, j - i, S1, S2, S3)
        cnt["PH_eq"] += (j - i) == S1 and j > i
    # RUN classification
    k = Counter()
    for t in range(T):
        if lam[t + 1] != lam[t]: kind = 1
        elif S[t + 1] != S[t]: kind = 2
        elif lamU[t + 1] != lamU[t]: kind = 3
        else:
            kind = 4
            if Tt[t + 1] == Tt[t]: fail(cnt, "RUN_iv_notau", name, t)
        k[kind] += 1
        if st[t]["fb"]:
            even_fb = bool(st[t]["Is"])
            cnt["FB_%s_kind%d" % ("E" if even_fb else "O", kind)] += 1
            if even_fb and kind > 2: fail(cnt, "RUN_fbE", name, t, kind)
            if not even_fb and kind < 3: fail(cnt, "RUN_fbO", name, t, kind)
            if even_fb and Tt[t + 1] != Tt[t]: fail(cnt, "RUN_fbE_tau", name, t)
            if not even_fb and S[t + 1] != S[t]: fail(cnt, "RUN_fbO_sigma", name, t)
        if S[t + 1] != S[t] and Tt[t + 1] != Tt[t]: cnt["both_change"] += 1
    for kd in range(1, 5): cnt["kind%d" % kd] += k[kd]
    N2 = n * (n - 1); E, O = info[0], info[1]
    cnt["RUN_chk"] += 1
    ok = (k[1] <= N2 and k[3] <= N2 and k[2] <= E["sw"] and k[4] <= O["sw"] and E["runs"] <= N2 + 1 and O["runs"] <= N2 + 1
          and T <= 2 * N2 + (N2 + 1) * n * (E["m"] * (E["pstar"] + 1) + O["m"] * (O["pstar"] + 1))
          and T <= k[1] + k[3] + E["sw"] + O["sw"])
    if not ok: fail(cnt, "RUN", name, T, dict(k), E, O)
    cnt["max_lamruns"] = max(cnt["max_lamruns"], E["runs"]); cnt["max_lamUruns"] = max(cnt["max_lamUruns"], O["runs"])
    cnt["max_T"] = max(cnt["max_T"], T)


def main(a):
    import core_probe as CP, dual_probe as D
    cnt = Counter(); rng = random.Random(1818); nst = int(os.environ.get("RANDSTARTS", "1"))
    def do(g, name, extra=None):
        r = random.Random(name)
        starts = ([extra] if extra else []) + [RE.best_reward_start(g)] + [D.rand_start(g, r) for _ in range(nst)]
        for s0 in starts:
            try: analyse(g, s0, cnt, name, rng)
            except RuntimeError: cnt["maxit"] += 1
    if a[0] == "rand":
        N, lo, hi, seed = map(int, a[1:5]); r2 = random.Random(seed)
        for i in range(N):
            nn = r2.randint(lo, hi)
            do(D.rand_ck(r2, nn, r2.randint(0, min(5, nn - 1))), "rand%d" % i)
    else:
        for path in a:
            if path.endswith(".start"): continue
            try: g = RE.parse(path)
            except Exception: cnt["parse_err"] += 1; continue
            if g.n > int(os.environ.get("MAXN", "64")): cnt["skip_big"] += 1; continue
            sp = path[:-3] + ".start"
            ex = None
            if os.path.exists(sp):
                try: ex = CP.parse_start(g, sp)
                except Exception: cnt["start_err"] += 1
            cnt["GAMES"] += 1; do(g, os.path.relpath(path), ex)
    for k in sorted(cnt): print(k, cnt[k])
    bad = sum(v for k, v in cnt.items() if k.endswith("_V"))
    print("VIOLATIONS", bad)
    for e in EX: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
