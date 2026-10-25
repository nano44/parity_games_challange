#!/usr/bin/env python3
"""REFEREE-2 succ. 6: check of P-N5-SN fixes §2b (l-new 0883157, file sha1 e5394445): Lemma H1-DROP (with its divergence claim),
Corollary H1-KEEP, Corollary ABS-COUNT'. Own code on sn_check's machinery; one Odd choice vertex asserted; phase = (lambda_Xi, tau).
Usage: h1_check.py c1o N nmin nmax seed | inst game.pg [runs]"""
import sys, os, random
import sn_check as C
F = C.F; LP = C.LP; RC = F.RC; BOT = F.BOT; lev = F.lev

def check_run(g, s, t, st, name, o):
    states, fbs, E, Ed = F.run_n5(g, s, t)
    if (len(fbs), sum(fbs)) != F.n5.run(g, "n5", ({v: s[v] for v in range(g.n) if g.owner[v] == 0},
                                                   {v: t[v] for v in range(g.n) if g.owner[v] == 1}))[:2]:
        st.bad(f"{name} run differs from n5.run")
    A = [F.analyse(g, E, Ed, a, b, o) for a, b in states]
    for k, S in enumerate(A): LP.extra(g, E, S, states[k][0], states[k][1], o)
    T = len(fbs); so = set(g.succ[o]); d_o = len(so)
    st.c["runs"] += 1
    inph = [A[k].lam == A[k + 1].lam and states[k][1] == states[k + 1][1] for k in range(T)]
    eps = {}
    for k in range(T):
        if not inph[k]: continue
        A0, A1 = A[k], A[k + 1]
        if A0.H1 and not A1.H1:
            st.c["DROP_transitions(H1 -> notH1 in phase)"] += 1
            if A0.Xi[o][1] != 0: st.bad(f"{name} H1-DROP at {k}: P(theta_k) nonempty")
            # divergence claim along C (o's H_{k+1}-cycle) from c
            c = A0.lam[o]; q = c; walk = [c]
            while q != o:
                q = A1.H[q]; walk.append(q)
                if len(walk) > g.n + 1: st.bad(f"{name} H1-DROP walk at {k}"); break
            for i in range(len(walk) - 1):
                qt = walk[i]
                if A0.H[qt] != A1.H[qt]:
                    st.c["DROP_divergences"] += 1
                    if g.owner[qt] != 0: st.bad(f"{name} H1-DROP: Odd divergence at {k}")
                    if A0.Xi[A0.H[qt]][1] != 0 or A0.Xi[walk[i + 1]][1] != 0: st.bad(f"{name} H1-DROP claim at {k} q={qt}")
        R = LP.relevant(g, A0, A1, states[k], states[k + 1])
        Ek = max([x[1] for x in R if x[2] == "E"], default=BOT)
        Oc = [x for x in R if x[2] == "O"]; Ok = Oc[0][1] if Oc else BOT
        if Ok > Ek and A0.H1:
            eps[k] = Ok
            st.c["H1_eps"] += 1
            if Ok == -1: st.c["H1_eps_with_O=-1"] += 1
            else:
                st.c["KEEP_checks"] += 1
                if not A1.H1: st.bad(f"{name} H1-KEEP at {k}")
    # ABS-COUNT' per fallback-free run of each phase
    k = 0
    while k < T:
        if not inph[k] or fbs[k]: k += 1; continue
        a = k
        while k < T and inph[k] and not fbs[k]: k += 1
        b = k
        e = [x for x in range(a, b) if x in eps]
        rel = sum(len(((A[x].Rbar - A[x + 1].Rbar) & so) - {o}) for x in range(a, b))
        if not e: continue
        st.c["ABSC'_runs_with_H1_eps"] += 1
        if eps[e[-1]] >= 0:
            st.c["ABSC'_checks"] += 1
            if len(e) > d_o - 1 + rel: st.bad(f"{name} ABS-COUNT' run [{a},{b}) eps={len(e)} d_o={d_o} REL={rel}")
            if len(e) == d_o - 1 + rel: st.c["ABSC'_tight"] += 1
        else: st.c["ABSC'_runs_last_O=-1"] += 1

def main():
    st = F.Stats(); st.ex = {}; mode = sys.argv[1]
    if mode == "c1o":
        N, nmin, nmax, seed = map(int, sys.argv[2:6]); rng = random.Random(seed)
        for i in range(N):
            rg, o = RC.rand_game(rng, rng.randint(nmin, nmax), cyc=rng.random() < 0.7); g = F.to_lpg(rg); assert F.one_odd(g) == o
            s, t = F.start(g, rng, rng.random() < 0.6); check_run(g, s, t, st, f"c1o{seed}#{i}", o)
    else:
        path = sys.argv[2]; runs = int(sys.argv[3]) if len(sys.argv) > 3 else 1
        g = F.lpg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%"))); o = F.one_odd(g); rng = random.Random(7)
        for r in range(runs):
            s, t = F.start(g, rng, r > 0); check_run(g, s, t, st, f"{os.path.basename(path)}#{r}", o)
    F.report(st)

if __name__ == "__main__":
    main()
