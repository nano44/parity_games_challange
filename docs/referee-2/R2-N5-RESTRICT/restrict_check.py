#!/usr/bin/env python3
r"""REFEREE-2 successor 18 (Opus 5.5, D15): mechanical check of P-N5-RESTRICT-box48 (sha1 48c63a8e). N5 on G: my lane's SPEC loop
(R2-N5-DUAL/dual_check.Runner on si.py). N5 / N5^tau one step on an Odd cut H: my lane's R2-N5-EPR/epr_check.step (S4a, S4b, S4c with FIX 3;
S4b^tau keeps tau when tau is value-optimal against sigma in S4b's arena). Lane tools (phrestrict.py, fsrestrict.py, multi.py, eprestrict.py)
NOT run or imported.
For every phase P = (x..y) (maximal (lambda_Xi, tau)-constant run) and every instance (H, J) of §2:
  GP    H = G^P (Odd v keeps tau(v) and every sigmabar_k(v), k in P), J = P
  GU    H = G^u for u in Q (v in Q \ {u} cut to tau(v); u keeps all), J = every maximal u-run of P (D_k subset of {u})
  GUJ   H = G^{u|J} for u in Q (v in D- cut to {tau(v), sbar_J(v)}, other v != u to tau(v)), J = every frozen-side u-stretch of P
  GE    H = G'_E, J = every epoch E of P (sbar|Q constant)
Checks per (H, J): ADM admissibility; RI (i) Xi' = Xi, W' = W at every k in J; RII (ii) Isigma' = Isigma and S4a's output equal; RIII (iii)
Itau' = Itau n E(H); RIV (iv) Itau' != {} at an in-phase k -> tau value-optimal in S4b's arena of H; REP REPRO_H: N5^tau on H from (sigma_x, tau)
reproduces (sigma_k, tau) and the fallback type for len(J) transitions; LAM lambda' = lambda at x..y.
Phase-sentence data (G^P only): after reproducing P, does the N5^tau run on G^P stay in the same (lambda', tau)-phase at state y + 1 of H
(GP_extends: the N5^tau phase on G^P is LONGER than P, so "every phase of N5 on G IS one N5^tau phase on G^P" holds only as containment)?
Controls: MUT (G^P with the edge (v, sbar_x(v)) dropped for one v with sbar_x(v) != tau(v)): counted CTL_* (must bite).
Usage: restrict_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-EPR"))
import epr_check as P
DC, pg, Stats = P.DC, P.pg, P.Stats
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
WHERE = os.environ.get("WHERE")


def cut(g, keep):
    return pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else sorted(keep[v]) for v in range(g.n)])


def check_instance(tag, g, H, keep, states, fbs, infos, lam, x, y, k1, st, name, ctl=False):
    n = g.n; tau = list(states[x][1])
    pre = "CTL_" + tag if ctl else tag
    # admissibility
    adm = all(tau[v] in keep[v] and all(infos[k][1][v] in keep[v] for k in range(x, y + 1)) for v in range(n) if g.owner[v] == 1)
    if not ctl:
        st.inc(tag + "_instances")
        if not adm: st.bad(tag + "_ADM", f"{name} [{x},{y}]"); return
    Ep = set((v, w) for v in range(n) for w in H.succ[v])
    inphase_last = y < k1
    lenJ = (y - x) + (1 if inphase_last else 0)
    yp = x + lenJ
    bad = False
    for k in range(x, y + 1):
        sg = states[k][0]
        _, vsp, _ = P.evalE(H, sg)
        if not ctl: st.inc(tag + "_RI_checks")
        if vsp != infos[k][0] or P.Wvals(H, sg, tau) != P.Wvals(g, sg, tau):
            if ctl: bad = True; break
            st.bad(tag + "_RI", f"{name}@{k} [{x},{y}]")
    cur = (list(states[x][0]), list(tau))
    for k in range(x, yp):
        r_g = P.step(g, states[k][0], states[k][1], False)
        r_p = P.step(H, cur[0], cur[1], True)
        if r_p is None:
            if ctl: bad = True; break
            st.bad(tag + "_REP", f"{name}@{k}: N5^tau stops on H"); return
        ns, nt, fb, ip = r_p; nsg, ntg, fbg, ig = r_g
        if (tuple(nsg), tuple(ntg)) != tuple(states[k + 1]) or (fbg != 0) != (fbs[k] != 0): st.bad("SELF", f"{name}@{k}: my step != Runner")
        if not ctl:
            st.inc(tag + "_REP_steps")
            if ip["Is"] != ig["Is"] or (ig["Is"] and ip["s4a"] != ig["s4a"]): st.bad(tag + "_RII", f"{name}@{k}")
            if ip["It"] != (ig["It"] & Ep): st.bad(tag + "_RIII", f"{name}@{k}")
            if ip["It"]:
                st.inc(tag + "_RIV_checks")
                if not ip["tau_opt"]: st.bad(tag + "_RIV", f"{name}@{k}")
        if tuple(ns) != tuple(states[k + 1][0]) or tuple(nt) != tuple(tau) or (fb != 0) != (fbs[k] != 0):
            if ctl: bad = True; break
            st.bad(tag + "_REP", f"{name}@{k} [{x},{y}]: state or fallback flag differs"); return
        cur = (ns, nt)
    if ctl:
        st.inc(pre + "_runs")
        if bad: st.inc(pre + "_bites")
        return
    for k in range(x, y + 1):
        _, vsp, _ = P.evalE(H, states[k][0])
        if tuple(vsp[v][0] for v in range(n)) != lam[k]: st.bad(tag + "_LAM", f"{name}@{k}")
    if tag == "GP":
        # does the N5^tau phase on G^P continue past y?  cur = (sigma_y', tau) with y' = y (len(P) = y - x for a maximal phase not at the end)
        if not inphase_last and y + 1 < len(states):
            st.inc("GP_phase_end_checks")
            r = P.step(H, cur[0], cur[1], True)
            if r is None: st.inc("GP_Hstops_at_y"); return
            ns, nt, fb, ip = r
            _, v0, _ = P.evalE(H, cur[0]); _, v1, _ = P.evalE(H, ns)
            l0 = tuple(v0[v][0] for v in range(n)); l1 = tuple(v1[v][0] for v in range(n))
            gch = "tau" if tuple(states[y + 1][1]) != tuple(tau) else "lambda"
            st.inc("GP_G_phase_ends_by_" + gch)
            if l0 == l1 and tuple(nt) == tuple(tau):
                st.inc("GP_extends"); st.inc("GP_extends_G_by_" + gch)
                st.mxr("GP_extends_example", (n, name, x, y, gch))
                if WHERE: print("GP_EXTENDS", name, "phase", x, y, "G ends by", gch, "n", n, flush=True)


def check_run(g, states, fbs, st, name, rng):
    n = g.n
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    infos = []
    for sg, tu in states:
        E, vs, tf = P.evalE(g, sg); infos.append((vs, tf))
    lam = [tuple(vs[v][0] for v in range(n)) for vs, _ in infos]
    tauk = [tuple(t[v] for v in range(n) if g.owner[v] == 1) for _, t in states]
    st.inc("runs")
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and (lam[k1 + 1], tauk[k1 + 1]) == (lam[k0], tauk[k0]): k1 += 1
        st.inc("phases")
        if k1 > k0: st.inc("phases_ge2")
        tau = list(states[k0][1])
        # G^P
        keep = [set([tau[v]]) | set(infos[k][1][v] for k in range(k0, k1 + 1)) if g.owner[v] == 1 else None for v in range(n)]
        QP = sum(1 for v in range(n) if g.owner[v] == 1 and len(keep[v]) >= 2)
        st.mxr("max_QP", (QP, name, k0, k1, n)); st.inc("QP_ge2" if QP >= 2 else "QP_le1")
        check_instance("GP", g, cut(g, keep), keep, states, fbs, infos, lam, k0, k1, k1, st, name)
        # control: drop (v, sbar_x(v)) for one v with sbar_x(v) != tau(v) and sbar_x(v) used nowhere else? (drop it outright)
        cand = [v for v in range(n) if g.owner[v] == 1 and infos[k0][1][v] != tau[v]]
        if cand:
            v = rng.choice(cand); keep2 = [set(s) if s is not None else None for s in keep]; keep2[v].discard(infos[k0][1][v])
            check_instance("GP", g, cut(g, keep2), keep2, states, fbs, infos, lam, k0, k1, k1, st, name, ctl=True)
        # G^u on u-runs; G^{u|J} on frozen-side u-stretches
        for u in Q:
            a = k0
            while a <= k1:
                D = lambda k: set(v for v in range(n) if g.owner[v] == 1 and infos[k][1][v] != tau[v])
                if D(a) <= {u}:
                    b = a
                    while b + 1 <= k1 and D(b + 1) <= {u}: b += 1
                    keep = [None if g.owner[v] == 0 else (set(g.succ[v]) if v == u else {tau[v]}) for v in range(n)]
                    check_instance("GU", g, cut(g, keep), keep, states, fbs, infos, lam, a, b, k1, st, name)
                    a = b + 1
                else: a += 1
            sq = [tuple(infos[k][1][q] for q in Q if q != u) for k in range(k0, k1 + 1)]
            a = k0
            while a <= k1:
                b = a
                while b + 1 <= k1 and sq[b + 1 - k0] == sq[a - k0]: b += 1
                sb = infos[a][1]
                keep = [None if g.owner[v] == 0 else (set(g.succ[v]) if v == u else ({tau[v], sb[v]} if v in Q else {tau[v]})) for v in range(n)]
                check_instance("GUJ", g, cut(g, keep), keep, states, fbs, infos, lam, a, b, k1, st, name)
                a = b + 1
        # G'_E on epochs
        sq = [tuple(infos[k][1][q] for q in Q) for k in range(k0, k1 + 1)]
        a = k0
        while a <= k1:
            b = a
            while b + 1 <= k1 and sq[b + 1 - k0] == sq[a - k0]: b += 1
            sb = infos[a][1]
            keep = [None if g.owner[v] == 0 else {tau[v], sb[v]} for v in range(n)]
            check_instance("GE", g, cut(g, keep), keep, states, fbs, infos, lam, a, b, k1, st, name)
            a = b + 1
        k0 = k1 + 1


def run_game(g, s, t, st, name, rng):
    states, fbs = DC.Runner(g).run(s, t)
    check_run(g, states, fbs, st, name, rng)


def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(4848)
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; srng = random.Random(4849)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(g, r, srng); run_game(g, s, t, st, f"{path}#{r}", rng)
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        srng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
        for i in range(N):
            nn = srng.randint(nmin, nmax)
            g = DC.rand_game(srng, nn, "kO") if k == 0 else H3.rand_kO(srng, nn, k)
            for r in range(ns):
                s, t = R.starts(g, r, srng); run_game(g, s, t, st, f"random{seed}:{i}#{r}", rng)
    elif a[0] == "start":
        g = pg.read(a[1])
        if len(a) > 2: s, t = R.read_start(g, a[2])
        else: s, t = R.starts(g, 0, None)
        run_game(g, s, t, st, os.path.basename(a[1]), rng)
    print("MODE", " ".join(a))
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
