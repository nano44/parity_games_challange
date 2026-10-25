#!/usr/bin/env python3
"""REFEREE-2 (Opus 5.5, D15): mechanical check of companion packet P-N5-SO (docs/new/P-N5-SO-box32.md sha1 deb5ee44 @ trunk 1ef02bb).
Own code on my R2-N5-FB/fb_check.py. PHASE = maximal run of transitions with lambda_Xi and tau constant (P-N5-LP §0). On C^1O, phases with
lambda(o) != o. Per phase: Theta, X, d_o, S_o (relevant sigma-bar(o) changes), J (non-tame), f. Checks:
  TH    Theta <= (n-1) + n(X+1) + X; its cases: crossing-free theta-changes under not-H1 <= n-1 per phase; under H1 each changes Xi at
        x0 = sigma-bar_k(o), and x0 in F_k.
  F1o   per crossing-free interval of THIS phase notion: transitions with a Xi-change on F <= max(0, |F|-1) (R22 (a) used with a coarser
        phase than R22's key).
  SO    S_o <= Theta + (d_o-1)(Theta+1); at a relevant change with theta fixed the old choice leaves T; T only shrinks on theta-runs;
        for x in T_k and T_{k+1} the H-path to c is unchanged; the choice is the key-minimum of T (index / root-first H-path).
  XJ    J <= S_o; S_o <= d_o(2n + (n+1)X); f <= n_E(2n-1)(J+1)+J.
Usage: so_check.py c1o N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FB"))
import fb_check as F
RC, lpg, INF, BOT, lev, coarse = F.RC, F.lpg, F.INF, F.BOT, F.lev, F.coarse

def returns(f, o):
    x, seen = f[o], set()
    while x not in seen:
        if x == o: return True
        seen.add(x); x = f[x]
    return False

def hpath(S, x, c):
    p, seen = [], set()
    while x != c and x not in seen: seen.add(x); p.append(x); x = S.H[x]
    return tuple(p)

def check_run(g, s, t, st, name, o):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for S in A: S.H1 = not returns(S.H, o)
    T = len(fbs); n = g.n
    inph = [A[k].lam == A[k + 1].lam and states[k][1] == states[k + 1][1] for k in range(T)]
    st.c["runs"] += 1
    k = 0
    while k < T:
        if not inph[k]: k += 1; continue
        j = k
        while j < T and inph[j]: j += 1
        phase(g, E, A, states, fbs, k, j, st, f"{name}[{k},{j})", o)
        k = j

def phase(g, E, A, states, fbs, k0, k1, st, name, o):
    n = g.n
    st.c["phases"] += 1
    if A[k0].lam[o] == o: st.c["phases_lam_o_eq_o"] += 1; return
    c = A[k0].lam[o]; succ = E.succ[o]; d = len(succ); nE = sum(1 for v in range(n) if g.owner[v] == 0)
    st.c["phases_checked"] += 1
    cross = [A[k].Rbar != A[k + 1].Rbar for k in range(k0, k1)]
    X = sum(cross); Th = sum(1 for k in range(k0, k1) if A[k].Xi[o] != A[k + 1].Xi[o])
    So = sum(1 for k in range(k0, k1) if A[k].sbar[o] != A[k + 1].sbar[o])
    J = sum(1 for k in range(k0, k1) if any(coarse(A[k + 1].Xi[v], A[k].M) != coarse(A[k].Xi[v], A[k].M) for v in range(n)))
    f = sum(fbs[k0:k1])
    # ---- TH
    if Th > (n - 1) + n * (X + 1) + X: st.bad(f"{name} TH Theta={Th} X={X}")
    nh1 = 0
    for k in range(k0, k1):
        if cross[k - k0] or A[k].Xi[o] == A[k + 1].Xi[o]: continue
        if not A[k].H1:
            nh1 += 1
            th = A[k].Xi[o]
            if th[0] != c or th[1] != 0: st.bad(f"{name} TH notH1 theta shape {th}")
        else:
            x0 = A[k].sbar[o]
            st.c["TH_H1_cases"] += 1
            if x0 in A[k].Rbar: st.bad(f"{name} TH H1: x0 not in F")
            if A[k + 1].Xi[x0] == A[k].Xi[x0]: st.bad(f"{name} TH H1: theta changed with Xi(x0) fixed")
    if nh1 > n - 1: st.bad(f"{name} TH notH1 changes {nh1}")
    st.c["TH_notH1_cases"] += nh1
    # ---- F1o on crossing-free intervals of this phase
    k = k0
    while k < k1:
        j = k
        while j < k1 and not cross[j - k0]: j += 1
        Fset = [v for v in range(n) if v not in A[k].Rbar]
        fch = sum(1 for x in range(k, j) if any(A[x].Xi[v] != A[x + 1].Xi[v] for v in Fset))
        st.c["F1o_intervals"] += 1
        if fch > max(0, len(Fset) - 1): st.bad(f"{name} F1o: {fch} F-changes on |F|={len(Fset)} interval [{k},{j})")
        k = j + 1
    # ---- SO
    if So > Th + (d - 1) * (Th + 1): st.bad(f"{name} SO S_o={So} Theta={Th} d_o={d}")
    for k in range(k0, k1):
        A0, A1 = A[k], A[k + 1]
        mu0 = min((A0.Xi[x] for x in succ), key=E.key); mu1 = min((A1.Xi[x] for x in succ), key=E.key)
        T0 = {x for x in succ if A0.Xi[x] == mu0}; T1 = {x for x in succ if A1.Xi[x] == mu1}
        if A0.sbar[o] not in T0: st.bad(f"{name} SO: sbar(o) not a minimiser at {k}")
        # key-minimum rule inside T
        if g.prio[c] % 2 == 0: kmin = min(T0)
        else: kmin = min(T0, key=lambda x: (list(reversed(hpath(A0, x, c))), x))
        st.c["SO_keymin_checks"] += 1
        if kmin != A0.sbar[o]: st.bad(f"{name} SO key-min rule fails at {k}: sbar {A0.sbar[o]} keymin {kmin}")
        if A0.Xi[o] != A1.Xi[o]: continue
        st.c["SO_theta_fixed_transitions"] += 1
        if mu0 != mu1: st.bad(f"{name} SO: mu moved with theta fixed at {k}")
        if not T1 <= T0: st.bad(f"{name} SO: T grew at {k}")
        for x in T0 & T1:
            st.c["SO_frozen_key_checks"] += 1
            if hpath(A0, x, c) != hpath(A1, x, c): st.bad(f"{name} SO: H-path of {x} changed while in T at {k}")
        if A0.sbar[o] != A1.sbar[o]:
            st.c["SO_relevant_changes_theta_fixed"] += 1
            if A0.sbar[o] in T1: st.bad(f"{name} SO: old choice still in T at {k}")
    # ---- XJ
    if J > So: st.bad(f"{name} XJ J={J} > S_o={So}")
    if So > d * (2 * n + (n + 1) * X): st.bad(f"{name} XJ S_o bound")
    if f > nE * (2 * n - 1) * (J + 1) + J: st.bad(f"{name} XJ f bound")
    for key, val in (("Theta", Th), ("S_o", So), ("J", J), ("X", X), ("f", f)): st.mx[f"max_{key}"] = max(st.mx[f"max_{key}"], val)
    st.mx["max(S_o - d_o(Theta+1))"] = max(st.mx.get("max(S_o - d_o(Theta+1))", -10 ** 6), So - d * (Th + 1))
    st.mx["max(J - S_o)"] = max(st.mx.get("max(J - S_o)", -10 ** 6), J - So)
    st.c["sum_S_o"] += So; st.c["sum_J"] += J; st.c["sum_Theta"] += Th

def main():
    st = F.Stats(); mode = sys.argv[1]
    if mode == "c1o":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            rg, o = RC.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.7); g = F.to_lpg(rg); assert F.one_odd(g) == o
            s, t = F.start(g, rng, rng.random() < 0.6); check_run(g, s, t, st, f"c1o{seed}#{i}", o)
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); o = F.one_odd(g); rng = random.Random(7)
        for r in range(runs):
            s, t = F.start(g, rng, r > 0); check_run(g, s, t, st, f"{os.path.basename(path)}#{r}", o)
    F.report(st)

if __name__ == "__main__":
    main()
