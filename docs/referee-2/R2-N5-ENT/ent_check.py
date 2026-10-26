#!/usr/bin/env python3
"""REFEREE-2 successor 9 (Opus 5.5, D15): mechanical check of packet P-N5-ENT (docs/si/P-N5-ENT-box11.md sha1 4fd22be7 @ trunk 765e893).
Own code on my lane's R2-N5-OUT/out_check.py (traces own | rand | spec), R2-N5-FRZ/frz_check.py and R2-N5-RE/re_check.py. No lane script
is imported. Every game asserts exactly one Odd vertex with out-degree > 1. Scope run: maximal run of in-phase transitions k -> k+1 with
(h) at k, H2 at k+1 and w_{k+1} = w_k. Phase key (lambda_Xi, tau). M_k = max gate level (BOT if no gate). Levels: BOT < -1 < 0 < ... < INF.
Setting (Sigma): k0 < k consecutive fallbacks of a scope run S, L := M_k0 >= 0, r_s > L for s in [k0+1, k]. Ev := F_{k0+1} \\ F_k0.
H := V_{>max(L, rank c)}, A := P(theta_k0) & H, B := P(theta_k) & H. Rise: some S4a step in (k0, k) changes COARSE_L(theta).
Checks (packet items):
  SIGMA   (S1)-(S6): S4a in-phase steps inside; (h) on [k0, k]; (A_s) on [k0+1, k]; no leave at the S4a steps; F_k <= F_s; F_k0 <= F_k0+1;
          Ev & F_k = R_k0 & F_k; M_k <= L; c in F_k0 & F_k; rise <=> B != A (and "rise" by definition vs by B != A agree).
  FZ      every v in F_k: v in F_s on [k0+1, k], COARSE_L(Xi_k v) = COARSE_L(Xi_k0 v).
  BF      Even v in R_k0 & F_k: COARSE_L(b_k v) = COARSE_L(Xi_k0 sigma_k0 v), both with cycle node c; v off its successor's pre-c path.
  RB      as BF with a = sigma_k0(v) in Rbar_k: COARSE_L(Xi_k a) = COARSE_L(Xi_k0 a).
  WALK    every v0 in R_k0 & F_k: (a) v Even, sigma_k0(v) = a_j, v in R_k0 & F_k; (b) the H-identity; (c) low tail => B <= A.
  CYCEV   (rise) no Ev & F_k vertex on C_k.        TEVFB  (rise) x_k's honest play avoids Ev.
  ENTX    no (Sigma) with M_k = L and a rise.
  NJBA    level-M block intervals (M >= 0) with r > M on [f_i+1, f_{i+1}] are clean.  D1  D_M <= 1.  PLS2  N <= n_E(1 + D_M) per block
          and fallbacks of level >= 0 per scope run <= sum_M n_E(1 + D_M) <= 2 n n_E.
Records (not checks): (Sigma) pairs with/without rise; rises after a fallback with no next fallback in reach; straddling intervals; Ev
vertices on C_k / on x_k's play in (Sigma) WITHOUT a rise (shows the rise is what the two lemmas use).
Usage: ent_check.py random N nmin nmax seed [own|rand|spec] | inst game.pg [runs] [own|rand|spec]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-OUT")); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import out_check as OC, frz_check as FC
RC = FC.RC
INF, BOT = FC.INF, FC.BOT
lev, cl = FC.lev, FC.coarse
MUT = os.environ.get("ENT_MUT", "")   # mutation tests only: nor (drop r > L), nofzk (FZ over all v)

def M(S): return max(S.gates.values()) if S.gates else BOT

def honest_play(S, x):
    """vertices of the honest play from x up to (excluding) the first repeat; returns (pre-c path, cycle)"""
    seen, path = {}, []
    while x not in seen: seen[x] = len(path); path.append(x); x = S.fh[x]
    cyc = path[seen[x]:]
    return path, cyc

def precpath(g, S, x):
    path, cyc = honest_play(S, x)
    c = max(cyc, key=lambda u: g.rank[u])
    return path[:path.index(c)], c, cyc

def k0route(S, v, o):
    p, x = [], v
    while x != o: p.append(x); x = S.f[x]
    return p

def check_run(g, o, A, fbs, st, name):
    n = g.n; nE = sum(1 for v in range(n) if g.owner[v] == 0); T = len(fbs)
    inph = [OC.key(A[k], o) == OC.key(A[k + 1], o) for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    st.c["runs"] += 1; st.c["states"] += len(A)
    # scope runs
    runs, k = [], 0
    while k < T:
        if not insc[k]: k += 1; continue
        j = k
        while j + 1 < T and insc[j + 1]: j += 1
        runs.append((k, j)); k = j + 1          # transitions k..j
    for (s0, s1) in runs:
        st.c["scope_runs"] += 1
        fl = [k for k in range(s0, s1 + 1) if fbs[k]]
        # ---------------- setting (Sigma)
        for i in range(len(fl) - 1):
            k0, k = fl[i], fl[i + 1]
            L = M(A[k0])
            if L < 0: continue
            if MUT != "nor" and not all(A[s].r > L for s in range(k0 + 1, k + 1)): continue
            check_sigma(g, o, A, fbs, k0, k, L, nE, st, name)
        # rises after a fallback (record: how close does data get to (Sigma) + rise?)
        for k0 in fl:
            L = M(A[k0])
            if L < 0: continue
            for s in range(k0 + 1, s1 + 1):
                if fbs[s] or A[s].r <= L: break
                if cl(g, A[s + 1].theta, L) != cl(g, A[s].theta, L):
                    st.c["RECORD_rise_after_fallback_with_r_gt_L"] += 1
                    nxt = [f for f in fl if f > s]
                    if nxt and all(A[t].r > L for t in range(s, nxt[0] + 1)): st.c["RECORD_rise_with_next_fallback_and_r_gt_L"] += 1
                    elif nxt: st.c["RECORD_rise_then_r_drops_before_next_fallback"] += 1
                    else: st.c["RECORD_rise_with_no_next_fallback_in_S"] += 1
                    break
        # ---------------- corollaries: blocks
        levels = {}
        for f in fl:
            Mf = M(A[f])
            if Mf >= 0: levels.setdefault(Mf, []).append(f)
        tot_ge0 = sum(len(v) for v in levels.values()); bound = 0
        prevM = INF
        for f in fl:
            if M(A[f]) > prevM: st.bad(f"{name} CLS2 fallback level rose at {f}")
            prevM = M(A[f])
        for Mv, fs in sorted(levels.items()):
            D = 0; st.c["blocks"] += 1
            for i in range(len(fs) - 1):
                a, b = fs[i], fs[i + 1]
                st.c["intervals"] += 1
                if any(f for f in fl if a < f < b): st.bad(f"{name} block fallbacks not consecutive in S")
                dirty = any(cl(g, A[t + 1].Xi[v], Mv) != cl(g, A[t].Xi[v], Mv) for t in range(a, b) for v in range(n))
                allr = all(A[t].r > Mv for t in range(a + 1, b + 1))
                first_le = A[a + 1].r <= Mv
                if dirty: D += 1; st.c["dirty_intervals"] += 1
                if allr:
                    st.c["NJBA_intervals_r_gt_M"] += 1
                    if dirty: st.bad(f"{name} NJBA dirty interval ({a},{b}) M={Mv} with r > M")
                elif not first_le:
                    st.c["RECORD_straddling_intervals"] += 1
                    if dirty: st.c["RECORD_straddling_dirty"] += 1
                else:
                    st.c["intervals_r_le_M_from_start"] += 1
                    if dirty: st.bad(f"{name} D1 case 2 interval dirty (RDROP)")
            if D > 1: st.bad(f"{name} D1 D_M={D} > 1 at M={Mv}")
            st.mxu("max_D_M", D); st.mxu("max_block_size", len(fs))
            if len(fs) > nE * (1 + D): st.bad(f"{name} PL(a) N={len(fs)} > n_E(1+D)")
            bound += nE * (1 + D)
        if tot_ge0 > bound or tot_ge0 > 2 * n * nE: st.bad(f"{name} PLS2 {tot_ge0} > {bound} / 2 n n_E")
        st.mxu("max_fallbacks_ge0_per_scope_run", tot_ge0)

def check_sigma(g, o, A, fbs, k0, k, L, nE, st, name):
    n = g.n; S0, S1, Sk = A[k0], A[k0 + 1], A[k]
    st.c["SIGMA_pairs"] += 1
    if MUT == "nor" and not all(A[s].r > L for s in range(k0 + 1, k + 1)): st.c["MUT_nor_pairs_without_r_gt_L"] += 1
    # (S1)-(S5)
    for s in range(k0 + 1, k):
        if fbs[s]: st.bad(f"{name} S1 fallback inside")
    for s in range(k0, k + 1):
        if not A[s].hh: st.bad(f"{name} S2 (h) fails at {s}")
    for s in range(k0 + 1, k + 1):
        if any(L2 > L for (y, z), L2 in A[s].gates.items() if z in A[s].F): st.bad(f"{name} S2 (A_s) fails at {s}")
    for s in range(k0 + 1, k):
        if not A[s].Rr <= A[s + 1].Rbar: st.bad(f"{name} S3 leave at S4a step {s}")
    for s in range(k0 + 1, k + 1):
        if not Sk.F <= A[s].F: st.bad(f"{name} S3 F_k not in F_{s}")
    if not S0.F <= S1.F: st.bad(f"{name} S3 F_k0 not in F_k0+1")
    Ev = S1.F - S0.F
    if Ev & Sk.F != S0.Rr & Sk.F: st.bad(f"{name} S3 Ev & F_k != R_k0 & F_k")
    if M(Sk) > L: st.bad(f"{name} S4 M_k > L")
    c = S0.theta[0]
    if Sk.theta[0] != c or c not in S0.F or c not in Sk.F: st.bad(f"{name} S5 c")
    H = {v for v in range(n) if g.rank[v] > max(L, g.rank[c])}
    Aset, B = S0.theta[1] & H, Sk.theta[1] & H
    rise_def = any(cl(g, A[s + 1].theta, L) != cl(g, A[s].theta, L) for s in range(k0 + 1, k))
    rise = B != Aset
    if rise_def != rise: st.bad(f"{name} S6 rise by definition != (B != A)")
    if cl(g, S1.theta, L) != cl(g, S0.theta, L): st.bad(f"{name} theta coarse changed across the fallback k0")
    st.c["SIGMA_with_rise" if rise else "SIGMA_without_rise"] += 1
    if M(Sk) == L: st.c["SIGMA_with_M_k=L"] += 1
    if rise and M(Sk) == L: st.bad(f"{name} ENTX ENT setting non-empty (k0={k0}, k={k}, L={L})")
    # FZ
    for v in (range(n) if MUT == "nofzk" else Sk.F):
        st.c["FZ"] += 1
        if cl(g, Sk.Xi[v], L) != cl(g, S0.Xi[v], L): st.bad(f"{name} FZ v={v} (k0={k0}, k={k})")
    # BF, RB
    for v in S0.Rr & Sk.F:
        if g.owner[v] != 0: continue
        a = S0.sg[v]; bk = Sk.Xi[Sk.sg[v]]
        st.c["BF"] += 1
        if cl(g, bk, L) != cl(g, S0.Xi[a], L) or bk[0] != c or S0.Xi[a][0] != c: st.bad(f"{name} BF v={v}")
        for S, x in ((S0, a), (Sk, Sk.sg[v])):
            pre, cc, _ = precpath(g, S, x)
            if v in pre: st.bad(f"{name} BF v={v} on its successor's pre-c path")
        if a in Sk.Rbar:
            st.c["RB"] += 1
            if cl(g, Sk.Xi[a], L) != cl(g, S0.Xi[a], L): st.bad(f"{name} RB v={v} a={a}")
    # WALK
    for v0 in S0.Rr & Sk.F:
        st.c["WALK"] += 1
        rt = k0route(S0, v0, o) + [o]
        j = next(i for i in range(1, len(rt)) if rt[i] in Sk.Rbar)
        v, aj = rt[j - 1], rt[j]
        if g.owner[v] != 0 or S0.sg[v] != aj or v not in S0.Rr or v not in Sk.F: st.bad(f"{name} WALK(a) v0={v0}")
        pk = set(k0route(Sk, aj, o)) if aj != o else set(); p0 = set(k0route(S0, aj, o)) if aj != o else set()
        if (pk & H) | B != (p0 & H) | Aset or (pk & H) & B or (p0 & H) & Aset: st.bad(f"{name} WALK(b) v0={v0}")
        if not (set(rt[1:-1]) & H):
            st.c["WALK_c_low_tail"] += 1
            if not B <= Aset: st.bad(f"{name} WALK(c) v0={v0}")
    # CYC-EV, TEV-FB
    xk = Sk.sbar
    pre, cc, cyc = precpath(g, Sk, xk)
    if cc != c: st.bad(f"{name} threat's cycle node != c")
    on_cyc = Ev & Sk.F & set(cyc); on_play = Ev & (set(pre) | set(cyc))
    if rise:
        st.c["CYCEV_TEVFB_cases"] += 1
        if on_cyc: st.bad(f"{name} CYCEV Ev vertex on C_k")
        if on_play: st.bad(f"{name} TEVFB threat's play meets Ev")
    else:
        if on_cyc: st.c["RECORD_no_rise_Ev_on_C_k"] += 1
        if on_play: st.c["RECORD_no_rise_threat_meets_Ev"] += 1

def main():
    args = sys.argv[1:]; st = OC.Stats()
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); mode = args[5] if len(args) > 5 else "own"; rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:seed{seed}#{i}")
    else:
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3; mode = args[3] if len(args) > 3 else "own"
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = OC.run_trace(g, o, s, t, rng, mode); check_run(g, o, A, fbs, st, f"{mode}:{os.path.basename(path)}#{r}")
    FC.report(st)

if __name__ == "__main__":
    main()
