#!/usr/bin/env python3
r"""REFEREE-2 successor 7 (Opus 5.5, D15): mechanical check of packet P-N5-TOG (docs/new/P-N5-TOG-box35.md sha1 7dfda8c8 @ trunk d3daae1).
Own code on my lane's R2-N5-FRZ/frz_check.py (own N5, any S4a arena optimum). No lane script (togz.py, fbtau.py, fbtclimb.py, dlclimb.py)
and no REFEREE probe. Every game asserts exactly one Odd vertex with out-degree > 1. Phase key (lambda_Xi, tau).
Checks (per phase with c = lambda(o) != o):
  F       fact (F) on c's honest cycle.
  LMONO   L_k = length of c's honest cycle: monotone by the parity of c, strict at every sigma(c) change; sigma(c) changes <= n-1.
  ZCNT    Z_k changes at <= |U|(n+1) transitions; per v: P = {} states an interval, length monotone there.
  TOGGLE  every H1-toggle with Z_{k+1} = Z_k changes next(c) (c Even, sigma(c) changes); Step 1 (next unchanged on C \ {c, o}) checked
          at every toggle.
  TCOUNT  toggles <= |U|(n+1) + n-1, drops <= ceil(T/2); c = o => no toggle.
  XSN     X_SN per phase (S4a crossings starting at c_w = c_theta states) <= 13(d_o+1)n^3 (f+1+T) + T; also counted: S4a crossings at the
          transition leaving an SN prefix (outside X-RUN''s "both ends in P").
  RST     maximal (h)-runs per phase <= 1 + T + f; restarts classified (toggle / Even fallback); S4a restarts from H1 and not-H2 = 0.
Usage: tog_check.py random N nmin nmax seed [--rand] | inst game.pg [runs] [--rand]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC
RC = FC.RC

def honest_cycle(fh, v):
    seen, path, x = {}, [], v
    while x not in seen: seen[x] = len(path); path.append(x); x = fh[x]
    return path[seen[x]:]

def Zset(S, U):
    return {(v, S.Xi[v][2]) for v in U if not S.Xi[v][1]}

def check_phase(g, o, A, fbs, a, b, st, name):
    n = g.n; d_o = len(set(g.succ[o])); c = A[a].lamX[o]
    st.c["phases"] += 1
    togs = [k for k in range(a, b) if A[k].H1 != A[k + 1].H1]
    if c == o:
        st.c["phases_c=o"] += 1
        if togs: st.bad(f"{name} TCOUNT toggle with c = o")
        return
    U = [v for v in range(n) if A[a].lamX[v] == c]
    even_c = g.prio[c] % 2 == 0
    Ls = []
    for k in range(a, b + 1):
        S = A[k]; C = honest_cycle(S.fh, c)
        if c not in C: st.bad(f"{name} c not on its own cycle at {k}"); return
        i = C.index(c)
        for j, x in enumerate(C):
            if S.Xi[x] != (c, frozenset(), (i - j) % len(C)): st.bad(f"{name} F fails at {k} x={x}")
        Ls.append(len(C))
    sc = 0
    for k in range(a, b):
        L0, L1 = Ls[k - a], Ls[k - a + 1]; sw = A[k].fh[c] != A[k + 1].fh[c]
        st.c["LMONO_transitions"] += 1
        ok = (L1 <= L0) if even_c else (L1 >= L0)
        if not ok: st.bad(f"{name} LMONO L {L0}->{L1} at {k}")
        if sw:
            sc += 1; st.c["LMONO_next(c)_changes"] += 1
            if L1 == L0: st.bad(f"{name} LMONO not strict at a sigma(c) change at {k}")
    if sc > n - 1: st.bad(f"{name} LMONO {sc} changes")
    st.mxu("max_sigma(c)_changes_per_phase", sc)
    zc = 0
    for v in U:
        E = [k for k in range(a, b + 1) if not A[k].Xi[v][1]]
        if E and E != list(range(E[0], E[-1] + 1)): st.bad(f"{name} ZCNT P={{}} not an interval v={v}")
        ls = [A[k].Xi[v][2] for k in E]
        if any((ls[i] > ls[i - 1]) if even_c else (ls[i] < ls[i - 1]) for i in range(1, len(ls))): st.bad(f"{name} ZCNT length not monotone v={v}")
    for k in range(a, b):
        if Zset(A[k], U) != Zset(A[k + 1], U): zc += 1
    if zc > len(U) * (n + 1): st.bad(f"{name} ZCNT {zc}")
    st.mxu("max_Z_changes_per_phase", zc)
    T = len(U) * (n + 1) + n - 1
    for k in togs:
        st.c["TOGGLE_toggles"] += 1
        if fbs[k]: st.c["TOGGLE_toggles_at_fallbacks"] += 1
        zsame = Zset(A[k], U) == Zset(A[k + 1], U); sw = A[k].fh[c] != A[k + 1].fh[c]
        st.c[f"TOGGLE_kind Z_changed={not zsame} next(c)_changed={sw}"] += 1
        if zsame:
            if not sw: st.bad(f"{name} TOGGLE Z same but next(c) same at {k}")
            if g.owner[c] != 0: st.bad(f"{name} TOGGLE c not Even")
            ai = k if not A[k].H1 else k + 1; bi = k + 1 if ai == k else k
            C = honest_cycle(A[ai].fh, c)
            for x in C:
                if x not in (c, o) and A[ai].fh[x] != A[bi].fh[x]: st.bad(f"{name} TOGGLE step 1 next({x}) changed at {k}")
    drops = sum(1 for k in togs if A[k].H1)
    st.mxu("max_toggles_per_phase", len(togs)); st.mxu("max_drops_per_phase", drops)
    if len(togs) > T or drops > -(-T // 2): st.bad(f"{name} TCOUNT {len(togs)} toggles {drops} drops > T={T}")
    # X_SN per phase
    f = sum(fbs[a:b]); xsn = 0; exitx = 0
    for k in range(a, b):
        if fbs[k] == 0 and A[k].H3 and A[k].Rr != A[k + 1].Rr:
            xsn += 1
            if not A[k + 1].H3: exitx += 1
    st.c["XSN_crossings"] += xsn; st.c["XSN_crossings_at_transition_leaving_SN_prefix"] += exitx; st.mxu("max_X_SN_per_phase", xsn)
    if xsn > 13 * (d_o + 1) * n ** 3 * (f + 1 + T) + T: st.bad(f"{name} XSN {xsn}")
    # RESTARTS
    runs = 0; prev = False
    for k in range(a, b + 1):
        if A[k].hh and not prev:
            runs += 1
            if k > a:
                if not A[k - 1].H1: st.c["RST_restart_by_toggle"] += 1
                elif not A[k - 1].H2:
                    st.c["RST_restart_from_H1_notH2"] += 1
                    if fbs[k - 1] == 0: st.bad(f"{name} RST S4a restart from H1 and not-H2 at {k-1}")
                    else: st.c["RST_restart_by_Even_fallback"] += 1
                else: st.bad(f"{name} RST restart from H1 and H2 and not-(h) (H3-CONST)")
        prev = A[k].hh
    st.mxu("max_h_runs_per_phase", runs)
    if runs > 1 + T + f: st.bad(f"{name} RST {runs} runs")

def check_run(g, o, A, fbs, st, name):
    T = len(fbs); st.c["runs"] += 1; st.c["transitions"] += T; st.c["fallbacks"] += sum(fbs)
    inph = [A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] for k in range(T)]
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        check_phase(g, o, A, fbs, k, j, st, f"{name}[{k},{j}]"); k = j

def main():
    st = FC.Stats(); args = [a for a in sys.argv[1:] if a != "--rand"]; rand = "--rand" in sys.argv
    if args[0] == "random":
        N, nmin, nmax, seed = map(int, args[1:5]); rng = random.Random(seed)
        for i in range(N):
            g, o = RC.rand_game(rng, rng.randint(nmin, nmax)); assert FC.odd_vertex(g) == o
            s, t = RC.rand_start(rng, g) if rng.random() < 0.7 else FC.s3_start(g)
            A, fbs = FC.run_n5(g, o, s, t, rng, rand); check_run(g, o, A, fbs, st, f"seed{seed}#{i}")
    else:
        path = args[1]; runs = int(args[2]) if len(args) > 2 else 3
        g = RC.parse(open(path).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(runs):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = FC.run_n5(g, o, s, t, rng, rand); check_run(g, o, A, fbs, st, f"{os.path.basename(path)}#{r}")
    FC.report(st)

if __name__ == "__main__":
    main()
