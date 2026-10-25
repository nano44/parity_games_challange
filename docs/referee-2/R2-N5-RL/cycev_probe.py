#!/usr/bin/env python3
"""REFEREE-2 succ. 8: probe of Lemma CYC-EV's steps (docs/si/P-N5-RL-fixes-box10.md sha1 ac027458, RL-1) in setting (Σ): k0 < k
consecutive fallbacks of a scope run S, L = M_k0 >= 0, r > L on [k0+1, k] (rise not required). Own N5 (frz_check.run_n5).
Checks at k: FZ (v in F_k: COARSE_L(Xi) equal at k0 and k), BF (Even v in R_k0 & F_k: COARSE_L(b_k v) = COARSE_L(Xi_k0 sigma_k0 v)),
RB (a = sigma_k0(v) in Rbar_k: COARSE_L equal), WALK identity ((pi^k_aj & H) + B = (pi^k0_aj & H) + A) for every v0 in R_k0 & F_k,
and CYC-EV's contrapositive (an Ev & F_k vertex on C_k forces A = {} and B = {}). Usage: cycev_probe.py random N nmin nmax seed | file.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FRZ"))
import frz_check as FC, rl_check as RL
RC = FC.RC
st = FC.Stats()
def cl(g, x, L): return FC.coarse(g, x, L)
def route(S, v, o):
    p, x = [], v
    while x != o: p.append(x); x = S.f[x]
    return p
def probe(g, o, A, fbs, name):
    T = len(fbs)
    inph = [A[k].lamX == A[k + 1].lamX and A[k].tu[o] == A[k + 1].tu[o] for k in range(T)]
    insc = [inph[k] and A[k].hh and A[k + 1].H2 and A[k].w == A[k + 1].w for k in range(T)]
    fl = [k for k in range(T) if insc[k] and fbs[k]]
    for i in range(len(fl) - 1):
        k0, k = fl[i], fl[i + 1]
        if not all(insc[j] for j in range(k0, k + 1)): continue
        if not A[k0].gates: continue
        L = max(A[k0].gates.values())
        if L < 0 or not all(A[s].r > L for s in range(k0 + 1, k + 1)): continue
        S0, Sk = A[k0], A[k]; c = S0.theta[0]
        st.c["SIGMA_settings"] += 1
        Mk = max(Sk.gates.values()) if Sk.gates else FC.BOT
        if Mk > L: st.bad(f"{name} M_k > L (CLS2)")
        H = {v for v in range(g.n) if g.rank[v] > max(L, g.rank[c])}
        Aset, B = S0.theta[1] & H, Sk.theta[1] & H
        for v in Sk.F:
            st.c["FZ"] += 1
            if cl(g, Sk.Xi[v], L) != cl(g, S0.Xi[v], L): st.bad(f"{name} FZ v={v}")
        for v0 in (S0.Rr & Sk.F):
            if g.owner[v0] == 0:
                st.c["BF"] += 1
                if cl(g, Sk.Xi[Sk.sg[v0]], L) != cl(g, S0.Xi[S0.sg[v0]], L): st.bad(f"{name} BF v={v0}")
            rt = route(S0, v0, o) + [o]
            j = next(i for i, x in enumerate(rt) if x in Sk.Rbar)
            pv, aj = rt[j - 1], rt[j]
            if g.owner[pv] != 0: st.bad(f"{name} WALK predecessor not Even"); continue
            st.c["RB_WALK"] += 1
            if cl(g, Sk.Xi[aj], L) != cl(g, S0.Xi[aj], L): st.bad(f"{name} RB a={aj}")
            pk = set(Sk.pi.get(aj, [])) if aj != o else set(); p0 = set(S0.pi.get(aj, [])) if aj != o else set()
            if (pk & H) | B != (p0 & H) | Aset or (pk & H) & B or (p0 & H) & Aset: st.bad(f"{name} WALK identity v0={v0}")
        Ev = A[k0 + 1].F - S0.F
        cyc = set(RL.honest_cycle(Sk.fh, c))
        if cyc & Ev & Sk.F:
            st.c["CYCEV_Ev_on_C_k"] += 1
            if Aset or B: st.bad(f"{name} CYC-EV contrapositive")
        rise = B != Aset
        if rise: st.c["SIGMA_with_rise (ENT-like)"] += 1
if sys.argv[1] == "random":
    N, a, b, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
    for i in range(N):
        g, o = RC.rand_game(rng, rng.randint(a, b)); s, t = RC.rand_start(rng, g)
        A, fbs = FC.run_n5(g, o, s, t, rng, i % 2 == 1); probe(g, o, A, fbs, f"r{i}")
else:
    for p in sys.argv[1:]:
        g = RC.parse(open(p).read()); o = FC.odd_vertex(g); rng = random.Random(7)
        for r in range(4):
            s, t = FC.s3_start(g) if r == 0 else RC.rand_start(rng, g)
            A, fbs = FC.run_n5(g, o, s, t, rng, r >= 2); probe(g, o, A, fbs, f"{os.path.basename(p)}#{r}")
FC.report(st)
