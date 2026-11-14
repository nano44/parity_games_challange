#!/usr/bin/env python3
"""L-SI box 104, Addendum B probe: does N5 (SPEC) on a guided wrapper make exactly the GLOBALLY OPTIMAL improvement step of H
(Schewe's policy, [F11] Section 4: the optimal strategy inside the arena of the current and the improving edges)? DATA only.
Per step before the first fallback: A(v) = {current} + {improving successors of v in H} by H's own valuation (si.Engine on H);
OPT = the optimal valuation of the two-player game H restricted to Even's edges A (Howard iteration on H|A from the current
strategy, to its fixpoint). Counter iglofail (unit: steps before the first fallback): the H-valuation of N5's new H-part differs
from OPT at some vertex. cntfail (unit: games): the first fallback is not at (steps of this file's own globally optimal policy
run from s0) + 1; the two runs may resolve ties between equally valued strategies differently. endfail: iterations != first fallback + 2.
Usage: glo104.py lmcs MODE n...     G_n of arXiv 1106.0778v2 (Figure 4 priorities, iota). MODE emul: rho0(e_i) = d_i and the fixed
                                    face of the Even edge d_i -> e_i leads to h_i (Odd's reply at e_i, copied by the faces);
                                    MODE plain: every face leads to w, rho0 = Odd's optimal counterstrategy to iota (control)
       glo104.py hn GF G3 RE COPY n...   H_n with gscan104.py's parameters
       glo104.py rand1p SEED COUNT NMAX  random games (harness gen.random_game) with every Odd vertex cut to its first successor
                                    (ONE-player games), a random s0; faces to w.   (env as guide104.py)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gscan104 as GS
from gscan104 import W, pg, n5v, n5, n5x, zielonka, Engine, ALG

def optimum(H, A, s):
    HA = pg.Game(list(H.prio), list(H.owner), [sorted(A[v]) if H.owner[v] == 0 else list(H.succ[v]) for v in range(H.n)]); E = Engine(HA)
    s = list(s)
    while True:
        vs, _ = E.evaluate(tuple(s)); ch = False
        for v in range(H.n):
            if H.owner[v] == 0:
                b = max(HA.succ[v], key=lambda w: E.key(vs[w]))
                if E.key(vs[b]) > E.key(vs[s[v]]): s[v] = b; ch = True
        if not ch: return vs

def run(H, s0, rho0, gamma, copy):
    g, std_s, std_t, mp, inv, valves = GS.wrapg(H, s0, rho0, gamma, copy); E, Ed = Engine(g), Engine(n5.dual(g)); EH = Engine(H); n = H.n
    ev = [v for v in range(n) if H.owner[v] == 0]
    sigma, tau = n5x.start_pair(g, E, Ed, None); its = 0; F1 = None; fail = 0; steps = 0; glo = 0
    while its < 100000:
        if F1 is None:
            sH = [inv[sigma[v]] if H.owner[v] == 0 else -1 for v in range(n)]; vs, _ = EH.evaluate(tuple(sH))
            A = {v: {sH[v]} | {w for w in H.succ[v] if EH.key(vs[w]) > EH.key(vs[sH[v]])} for v in ev}
        r = n5v.step(g, E, Ed, sigma, tau, ALG)
        if r is None: break
        ns, nt, _, _, fb = r; its += 1
        if fb and F1 is None: F1 = its
        if F1 is None:
            nH = [inv[ns[v]] if H.owner[v] == 0 else -1 for v in range(n)]; nv, _ = EH.evaluate(tuple(nH)); opt = optimum(H, A, sH)
            steps += 1; fail += int(any(nv[v] != opt[v] for v in range(n)))
        sigma, tau = ns, nt
    # the globally optimal policy itself, from s0
    s = [s0[v] if H.owner[v] == 0 else -1 for v in range(n)]
    while glo < 100000:
        vs, _ = EH.evaluate(tuple(s)); A = {v: {s[v]} | {w for w in H.succ[v] if EH.key(vs[w]) > EH.key(vs[s[v]])} for v in ev}
        if all(len(A[v]) == 1 for v in ev): break
        HA = pg.Game(list(H.prio), list(H.owner), [sorted(A[v]) if H.owner[v] == 0 else list(H.succ[v]) for v in range(n)]); EA = Engine(HA); t = list(s)
        while True:
            ws, _ = EA.evaluate(tuple(t)); ch = False
            for v in ev:
                b = max(HA.succ[v], key=lambda w: EA.key(ws[w]))
                if EA.key(ws[b]) > EA.key(ws[t[v]]): t[v] = b; ch = True
            if not ch: break
        s = t; glo += 1
    return its, F1, steps, fail, glo, g.n

if __name__ == "__main__":
    famname = sys.argv[1]
    if famname == "rand1p":
        # random games (harness gen.random_game) with every Odd vertex cut to its first successor: ONE-player (Even-only) games
        import random
        gen = W.gen; seed, cnt, nmax = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed)
        tot = dict(games=0, steps=0, iglofail=0, cntfail=0, maxglo=0, maxW=0)
        for _ in range(cnt):
            n = rng.randint(3, nmax); H0 = gen.random_game(n, rng.randint(1, n + 1), 1, min(n, 4), rng.randrange(10 ** 9))
            H = pg.Game(list(H0.prio), list(H0.owner), [list(ss) if H0.owner[v] == 0 else [ss[0]] for v, ss in enumerate(H0.succ)])
            s0 = [rng.choice(H.succ[v]) if H.owner[v] == 0 else -1 for v in range(H.n)]; rho0 = {v: H.succ[v][0] for v in range(H.n) if H.owner[v] == 1}
            its, F1, steps, fail, glo, wn = run(H, s0, rho0, {}, True)
            tot["games"] += 1; tot["steps"] += steps; tot["iglofail"] += fail; tot["cntfail"] += int(F1 != glo + 1); tot["endfail"] = tot.get("endfail", 0) + int(F1 is None or its != F1 + 2); tot["maxglo"] = max(tot["maxglo"], glo); tot["maxW"] = max(tot["maxW"], wn)
        print(f"GLO104 rand1p seed {seed} games {tot['games']} n<={nmax}: steps before the first fallback {tot['steps']} iglofail {tot['iglofail']} | cntfail (first fallback != policy steps + 1) {tot['cntfail']} endfail (iterations != first fallback + 2) {tot['endfail']} | max steps of the globally optimal policy {tot['maxglo']} max |Wg| {tot['maxW']}", flush=True)
    elif famname == "lmcs":
        mode = sys.argv[2]
        for n in map(int, sys.argv[3:]):
            H, s0 = W.lmcs_game(n, "fig4"); s0 = list(s0); EH = Engine(H); _, cs = EH.evaluate(tuple(s0[v] if H.owner[v] == 0 else -1 for v in range(H.n)))
            rho0 = {v: cs[v] for v in range(H.n) if H.owner[v] == 1}; gamma = {}; multi = [o for o in range(H.n) if H.owner[o] == 1 and len(H.succ[o]) > 1]
            if mode == "emul":
                for o in multi:
                    d = [a for a in H.succ[o] if H.owner[a] == 0 and o in H.succ[a]]; assert len(d) == 1 and len(H.succ[o]) == 2, (o, H.succ[o])
                    h = [a for a in H.succ[o] if a != d[0]][0]; rho0[o] = d[0]; gamma[(d[0], o)] = h
            its, F1, steps, fail, glo, wn = run(H, s0, rho0, gamma, True)
            print(f"GLO104 lmcs {mode} n {n}: Odd vertices with 2 successors {len(multi)} | |Wg| {wn} | N5 iterations {its} first fallback {F1} | steps before it {steps} iglofail {fail} | globally optimal policy on H from iota: {glo} steps", flush=True)
    else:
        GF, G3, RE, COPY = sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5] == "1"
        sys.path.insert(0, os.environ["HN"]); import hn
        for n in map(int, sys.argv[6:]):
            H, ix = hn.build(n, "fig"); io = hn.iota(n, ix); s0 = [io.get(v, H.succ[v][0]) if H.owner[v] == 0 else -1 for v in range(H.n)]
            rho0 = {v: H.succ[v][0] for v in range(H.n) if H.owner[v] == 1}; gamma = {}
            for i in range(1, n + 1):
                e, d1, d3, h, f = ix[f"e{i}"], ix[f"d1_{i}"], ix[f"d3_{i}"], ix[f"h{i}"], ix[f"f{i}"]
                rho0[e] = d1 if RE == "d1" else h
                if GF != "e": rho0[f] = (d1 if GF == "d1" else h, e)
                if G3 != "e": gamma[(d3, e)] = d1 if G3 == "d1" else h
            its, F1, steps, fail, glo, wn = run(H, s0, rho0, gamma, COPY)
            print(f"GLO104 hn GF {GF} G3 {G3} RE {RE} copy {int(COPY)} n {n}: |Wg| {wn} | N5 iterations {its} first fallback {F1} | steps before it {steps} iglofail {fail} | globally optimal policy on H from iota: {glo} steps", flush=True)
