#!/usr/bin/env python3
r"""REFEREE-2 successor 14 (Opus 5.5, D15): mechanical check of packet P-N5-EPR (docs/new/P-N5-EPR-box45.md sha1 8fecca79 @ a3b1cff3).
N5 on G: succ. 13's own SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py, read-only). N5 / N5^tau on G'_E: my own one-step function below,
transcribed from the same Runner (S4a, S4b, S4c with FIX 3), with S4b^tau = "keep tau if tau is value-optimal against sigma in S4b's arena".
The lane's experiments/new/box45/eprestrict.py, itcheck.py NOT run or imported.
Per epoch E = (x..y) of every phase (epoch: maximal run with sbar|Q constant), with G'_E built from (tau, sbar_E):
  RI     RESTRICT_E (i): Xi' = Xi and W' = W at every k in E
  RII    (ii): Isigma' = Isigma and S4a's output on G'_E = on G (k in E with Isigma != {})
  RIII   (iii): Itau' = Itau n E(G'_E)
  RIV    (iv): k -> k+1 in-phase and Itau' != {} => tau value-optimal in S4b's arena on G'_E
  REP    REPRO: N5^tau on G'_E from (sigma_x, tau) reproduces (sigma_k, tau) and the fallback flags for len(E) transitions
  LAM    REPRO's "one phase": lambda' at every visited pair = lambda; recorded separately at y' = y + 1 (outside E) as LAMEND
  DIV    SPEC's own S4b on G'_E moves tau at some reproduced state (where N5 and N5^tau on G'_E differ)
  EP0    D_E = {} => len(E) <= n + m
  EP1L   |D_E| = 1: record len(E) (no bound check: T* is astronomically larger)
Mutation EP_MUT: d1 (u in D keeps only tau(u) in G'_E).
Usage: epr_check.py files list.txt [runs] | random N nmin nmax seed [k] [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("EP_MUT", "")

def evalE(g, sg):
    E = Engine(g); n = g.n
    vs, tf = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    return E, vs, tf

def step(g, sg, tu, keep_tau):
    """one N5 (keep_tau False) or N5^tau (True) iteration on g from (sg, tu). Returns (ns, nt, fb, info) or None if N5 stops."""
    n = g.n
    E, vs, tf = evalE(g, sg)
    Is = E.improving(tuple(sg), vs)
    Ed = Engine(DC.dual(g))
    vt, _ = Ed.evaluate(tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
    It = Ed.improving(tuple(tu), vt)
    info = dict(vs=vs, tf=tf, Is=set(Is), vt=vt, It=set(It), s4a=None, s4b=None, s4b_spec=None, tau_opt=None)
    if not Is and not It: return None
    ns, nt = list(sg), list(tu)
    if Is:
        opt = {v: {sg[v]} for v in range(n) if g.owner[v] == 0}
        for v, w in Is: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 0 else [tu[v]] for v in range(n)]
        _, best = Engine(DC.dual(pg.Game(list(g.prio), list(g.owner), succ))).evaluate(
            tuple(tu[v] if g.owner[v] == 1 else -1 for v in range(n)))
        for v in range(n):
            if g.owner[v] == 0: ns[v] = best[v]
        info["s4a"] = tuple(ns)
    if It:
        opt = {v: {tu[v]} for v in range(n) if g.owner[v] == 1}
        for v, w in It: opt[v].add(w)
        succ = [sorted(opt[v]) if g.owner[v] == 1 else [sg[v]] for v in range(n)]
        H = pg.Game(list(g.prio), list(g.owner), succ)
        hv, best = Engine(H).evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        spec = [best[v] if g.owner[v] == 1 else tu[v] for v in range(n)]
        # tau's own value in H: fix Odd to tau
        Ht = pg.Game(list(g.prio), list(g.owner), [[tu[v]] if g.owner[v] == 1 else [sg[v]] for v in range(n)])
        tv, _ = Engine(Ht).evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        tau_opt = all(tv[v] == hv[v] for v in range(n))
        info["s4b_spec"] = tuple(spec); info["tau_opt"] = tau_opt
        if keep_tau and tau_opt: spec = list(tu)
        for v in range(n):
            if g.owner[v] == 1: nt[v] = spec[v]
        info["s4b"] = tuple(nt)
    fb = 0
    if ns == list(sg) and nt == list(tu):
        fb = 1 if not (Is and It) else 2
        if Is:
            Ek = E
            for v in {v for v, _ in Is}: ns[v] = max((w for x, w in Is if x == v), key=lambda w: (Ek.key(vs[w]), w))
        else:
            for v in {v for v, _ in It}: nt[v] = max((w for x, w in It if x == v), key=lambda w: (Ed.key(vt[w]), w))
    return ns, nt, fb, info

def Wvals(g, sg, tu):
    n = g.n
    G2 = pg.Game(list(g.prio), list(g.owner), [[tu[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(n)])
    vs, _ = Engine(G2).evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
    return vs

WIT = []
def check_run(g, states, fbs, st, name):
    n = g.n; m = sum(len(set(s)) for s in g.succ)
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    infos = []
    for sg, tu in states:
        E, vs, tf = evalE(g, sg); infos.append((vs, tf))
    lam = [tuple(vs[v][0] for v in range(n)) for vs, _ in infos]
    tauk = [tuple(t[v] for v in range(n) if g.owner[v] == 1) for _, t in states]
    st.inc("runs")
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and (lam[k1 + 1], tauk[k1 + 1]) == (lam[k0], tauk[k0]): k1 += 1
        st.inc("phases")
        # epochs
        sq = [tuple(infos[t][1][q] for q in Q) for t in range(k0, k1 + 1)]
        a = k0
        while a <= k1:
            b = a
            while b + 1 <= k1 and sq[b + 1 - k0] == sq[a - k0]: b += 1
            check_epoch(g, n, m, Q, states, fbs, infos, lam, a, b, k1, st, name)
            a = b + 1
        k0 = k1 + 1

def check_epoch(g, n, m, Q, states, fbs, infos, lam, x, y, k1, st, name):
    st.inc("epochs")
    tau = list(states[x][1]); sbar = infos[x][1]
    D = [u for u in range(n) if g.owner[u] == 1 and sbar[u] != tau[u]]
    succ = []
    for v in range(n):
        if g.owner[v] == 0: succ.append(list(g.succ[v]))
        elif v in D and MUT != "d1": succ.append(sorted({tau[v], sbar[v]}))
        else: succ.append([tau[v]])
    Gp = pg.Game(list(g.prio), list(g.owner), succ)
    Ep = set((v, w) for v in range(n) for w in succ[v])
    inphase_last = y < k1
    lenE = (y - x) + (1 if inphase_last else 0)
    yp = x + lenE
    st.mxr(f"max_len_by_D{min(len(D), 3)}", (lenE, name))
    if not D:
        st.inc("EP0_checks")
        if lenE > n + m: st.bad("EP0", f"{name}@{x}: len {lenE} > n + m {n + m}")
    # RESTRICT_E (i) at every k in E
    for k in range(x, y + 1):
        sg = states[k][0]
        _, vsp, _ = evalE(Gp, sg)
        st.inc("RI_checks")
        if vsp != infos[k][0] or Wvals(Gp, sg, tau) != Wvals(g, sg, tau): st.bad("RI", f"{name}@{k}: D {D}")
    # (ii)-(iv) and REPRO by stepping N5^tau on G'_E
    cur = (list(states[x][0]), list(tau))
    for k in range(x, yp):
        r_g = step(g, states[k][0], states[k][1], False)
        r_p = step(Gp, cur[0], cur[1], True)
        st.inc("REP_steps")
        if r_p is None: st.bad("REP", f"{name}@{k}: N5^tau stops on G'_E"); return
        ns, nt, fb, ip = r_p
        nsg, ntg, fbg, ig = r_g
        if (tuple(nsg), tuple(ntg)) != tuple(states[k + 1]) or (fbg != 0) != (fbs[k] != 0): st.bad("SELF", f"{name}@{k}: my step != Runner")
        if k <= y:
            st.inc("RII_checks")
            if ip["Is"] != ig["Is"] or (ig["Is"] and ip["s4a"] != ig["s4a"]): st.bad("RII", f"{name}@{k}")
            st.inc("RIII_checks")
            if ip["It"] != (ig["It"] & Ep): st.bad("RIII", f"{name}@{k}")
            if ip["It"]:
                st.inc("RIV_checks")
                if not ip["tau_opt"]: st.bad("RIV", f"{name}@{k}: tau not value-optimal in G'_E's S4b arena")
        if ip["It"] and ip["s4b_spec"] is not None and list(ip["s4b_spec"]) != list(cur[1]):
            st.inc("DIV_states"); st.mxr("DIV_example", (len(D), f"{name}@{k} |D| {len(D)}"))
        if tuple(ns) != tuple(states[k + 1][0]) or tuple(nt) != tuple(tau) or (fb != 0) != (fbs[k] != 0):
            st.bad("REP", f"{name}@{k}: state or fallback flag differs"); return
        cur = (ns, nt)
    # one phase: lambda' at the visited pairs
    for k in range(x, yp + 1):
        _, vsp, _ = evalE(Gp, states[k][0])
        lp = tuple(vsp[v][0] for v in range(n))
        if k <= y:
            st.inc("LAM_checks")
            if lp != lam[k]: st.bad("LAM", f"{name}@{k}")
        else:
            st.inc("LAMEND_checks")
            if lp != lam[k]:
                st.inc("LAMEND_differs"); st.mxr("LAMEND_example", (len(D), f"{name}@{k} |D| {len(D)} len {lenE} n {n}"))
                WIT.append((len(D), lenE, g, states[0], name, x, y))
                if not D: st.inc("LAMEND_differs_D0")
                if len(D) == 1: st.inc("LAMEND_differs_D1")

def run_game(g, s, t, st, name):
    states, fbs = DC.Runner(g).run(s, t)
    check_run(g, states, fbs, st, name)

def starts(g, r, rng):
    if r == 0: return list(Engine(g).initial("best")), list(Engine(DC.dual(g)).initial("best"))
    return [rng.choice(g.succ[v]) for v in range(g.n)], [rng.choice(g.succ[v]) for v in range(g.n)]

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(2020)
        cap = int(os.environ.get("MAXN", "64"))
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            g = pg.read(os.path.join(DC.ROOT, path))
            if g.n > cap: st.inc("skipped_n_gt_cap"); continue
            for r in range(runs):
                s, t = starts(g, r, rng); run_game(g, s, t, st, f"{path}#{r}")
    elif a[0] == "start":
        g = pg.read(a[1]); s, t = [x[0] for x in g.succ], [x[0] for x in g.succ]
        for line in open(a[2]):
            parts = line.split()
            if not parts or parts[0].startswith("#"): continue
            tgt = s if parts[0] == "SIGMA0" else t
            for kv in parts[1:]:
                v, w = map(int, kv.split(":")); tgt[v] = w
        run_game(g, s, t, st, os.path.basename(a[1]) + "#start")
    elif a[0] == "climb": pass
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); k = int(a[5]) if len(a) > 5 else 2; rng = random.Random(seed)
        for i in range(N):
            g = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            for r in range(1, k + 1):
                s, t = starts(g, r, rng); run_game(g, s, t, st, f"random{seed}:{i}#{r}")
    out = os.environ.get("WITOUT")
    if out and WIT:
        for tag, want in (("D0", 0), ("D1", 1)):
            c = [w for w in WIT if w[0] == want]
            if not c: continue
            d, L, g, (s0, t0), nm, x, y = min(c, key=lambda w: (w[2].n, w[1]))
            open(f"{out}_{tag}.pg", "w").write(pg.dumps(g))
            open(f"{out}_{tag}.start", "w").write("SIGMA0 " + " ".join(f"{v}:{s0[v]}" for v in range(g.n) if g.owner[v] == 0) +
                "\nTAU0 " + " ".join(f"{v}:{t0[v]}" for v in range(g.n) if g.owner[v] == 1) + f"\n# from {nm}; epoch {x}..{y}, len {L}, |D| {d}\n")
    if a[0] == "climb":
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FBRED")); import fbred_check as FC
        steps, nmin, nmax, seed, outp = int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]; rng = random.Random(seed)
        best = DC.rand_game(rng, rng.randint(nmin, nmax), "kO"); bsc = -1
        for it in range(steps):
            cand = FC.mutate(rng, best) if it else best
            if cand.n > nmax: continue
            sc, bp = -1, None
            for r in range(6):
                s0, t0 = starts(cand, 1 if r else 0, rng); s2 = Stats()
                run_game(cand, s0, t0, s2, f"climb{seed}:{it}:{r}")
                for k2, v2 in s2.c.items(): st.c[k2] = st.c.get(k2, 0) + v2
                for v in s2.viol: st.viol.append(v)
                sc2 = 1000 * s2.c.get("DIV_states", 0) + s2.c.get("RIV_checks", 0)
                if sc2 > sc: sc, bp = sc2, (s0, t0)
            if sc >= bsc and bp is not None:
                bsc, best = sc, cand
                open(outp + ".pg", "w").write(pg.dumps(best))
                open(outp + ".start", "w").write("SIGMA0 " + " ".join(f"{v}:{bp[0][v]}" for v in range(best.n) if best.owner[v] == 0) +
                    "\nTAU0 " + " ".join(f"{v}:{bp[1][v]}" for v in range(best.n) if best.owner[v] == 1) + f"\n# score {bsc}\n")
        st.mxr("climb_best", (bsc, outp))
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
