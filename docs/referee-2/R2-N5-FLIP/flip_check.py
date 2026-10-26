#!/usr/bin/env python3
r"""REFEREE-2 successor 16 (Opus 5.5, D15): mechanical check of packet P-N5-FLIP (docs/si/P-N5-FLIP-box18.md sha1 96a7e088 @ d67fdb87).
State sequence: succ. 13's SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py, read-only). Xi = my own PLAY values of (sigma, sigmabar)
(R2-N5-RUND/rund_check). The lane's experiments/si/rund/{relay,flipck,frzrho}.py are NOT run or imported.
Definitions as in the packet: phase = (lambda, tau) constant; Q = Odd vertices of out-degree >= 2; U_c = lambda^{-1}(c); Q_c = (Q ∩ U_c) \ {c};
kappa = (weight of P, s_c * length); rho event at q = in-phase transition with Xi_t(q) != Xi_{t+1}(q).
Checks:
  ROOT     all Q-exit paths equal at t, t+1 => Xi equal on Reach_t(Q); every rho transition changes some Q-exit path (an Even vertex on one)
  RR       ROUTE-RELAY: every RELAY event (q on no honest cycle at t, t+1) has a source; SELF-FREE: |Q_c| = 1 => ROUTE
  RC       ROOT-C: (exits form) all class exit paths AND exits of class c equal => kappa(q) equal for all q in Q_c; also recorded:
           RC_LIT = the literal form (paths equal as vertex sequences, an exit changed) with a kappa change; RC_MIN: kappa_s(q) = min over
           Pi_s(q) (walks enumerated, n <= WALKMAX); RC_POS: walks through a Q_c vertex on c's honest cycle whose positional realisation
           does not have cycle node c (the proof's "each walk is the play of a positional strategy with cycle node c")
  ST       STATIC: on every rho-free interval (no fallback, Xi|Q and sigmabar|Q constant): sigmabar constant on all Odd vertices; I_sigma =
           improving set of sigma in G_{sigmabar_I}
  FL       FLIP (a) FLIP-COST; (b) FLIP-1 when p1 intact at t2; (c) Z = C and strict rise >= wt(C) when also p1 ∩ p2 = {};
           NEC: N1 or N2 or N3; N3L: N3-LEVEL; recorded: N3L_LOW = intact, disjoint flips whose C-top is ranked BELOW c (the parenthesis
           "both hold when p1 is intact at t2, by (c)")
Mutations FL_MUT: root (ROOT with Xi asked to CHANGE), cost (FLIP-COST with wt(C) doubled), lev (N3-LEVEL with lev > rank(h)).
Usage: flip_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Engine, Stats = R.DC, R.pg, R.Engine, R.Stats
MUT = os.environ.get("FL_MUT", "")
WALKMAX = int(os.environ.get("WALKMAX", "16"))


def honest_next(I, k):
    return I[k]["hn"]


def kappa(E, val, c):
    s = 1 if E.par[c] == 1 else -1
    return (E.weight(val[1]), s * val[2])


def class_exit(I, k, y, Qc, c):
    """(path tuple, exit) of y's honest play at k: first vertex of Qc ∪ {c}"""
    nx = I[k]["hn"]; path, x, seen = [], y, set()
    while x not in Qc and x != c:
        if x in seen: return None
        seen.add(x); path.append(x); x = nx[x]
    return tuple(path), x


def on_honest_cycle(nx, v):
    path, x = R.lasso(nx, v)
    return v in path[path.index(x):]


def qexit_paths(g, sg, Q):
    out = {}
    for q in Q:
        for y in sorted(set(g.succ[q])):
            path, x, seen = [], y, set()
            while True:
                path.append(x)
                if x in Q or x in seen: break
                seen.add(x)
                x = sg[x] if g.owner[x] == 0 else g.succ[x][0]
            out[(q, y)] = tuple(path)
    return out


def check_game(gp, s, t, st, name):
    g, n = gp, gp.n
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); E = ctx.E
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    st.inc("runs"); st.inc("states", len(I))
    tauk = [tuple(b[v] for v in range(n) if g.owner[v] == 1) for _, b in states]
    key = [(I[k]["lamX"], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        if k1 > k0: check_phase(ctx, g, I, fbs, k0, k1, Q, st, name)
        k0 = k1 + 1


def check_phase(ctx, g, I, fbs, a, b, Q, st, name):
    n, E = ctx.n, ctx.E
    st.inc("phases")
    lam = I[a]["lamX"]
    C = sorted(set(lam))
    U = {c: set(v for v in range(n) if lam[v] == c) for c in C}
    Qc = {c: set(q for q in Q if lam[q] == c and q != c) for c in C}
    QX = {k: qexit_paths(g, I[k]["sg"], set(Q)) for k in range(a, b + 1)}
    for t in range(a, b):
        S, T = I[t], I[t + 1]
        st.inc("transitions")
        rho = [q for q in Q if S["xi"][q] != T["xi"][q]]
        if rho: st.inc("rho_transitions"); st.inc("rho_events", len(rho))
        # ROOT
        same = QX[t] == QX[t + 1]
        if same:
            st.inc("ROOT_static")
            reach = set(Q) | set(v for p in QX[t].values() for v in p)
            ch = [v for v in reach if S["xi"][v] != T["xi"][v]]
            if (MUT != "root" and ch) or (MUT == "root" and not ch): st.bad("ROOT", f"{name}@{t}: Xi changes on Reach at {ch[:3]}")
        if rho and same: st.bad("ROOT2", f"{name}@{t}: rho event without a Q-exit path change")
        if rho and not same:
            sw = [v for p in QX[t].values() for v in p if g.owner[v] == 0 and S["sg"][v] != T["sg"][v]]
            if not sw: st.bad("ROOT2", f"{name}@{t}: no Even vertex on a Q-exit path switches")
        # per class
        for c in C:
            qs = Qc[c]
            if not qs: continue
            ex = {}
            for k in (t, t + 1):
                ex[k] = {(q2, y): class_exit(I, k, y, qs, c) for q2 in qs for y in sorted(set(g.succ[q2])) if y in U[c]}
            ev = [q for q in qs if S["xi"][q] != T["xi"][q]]
            # ROOT-C
            if ex[t] == ex[t + 1]:
                st.inc("RC_static")
                if ev: st.bad("RC", f"{name}@{t}: class {c} exits static but kappa changes at {ev}")
            elif all((ex[t][kk] or (None,))[0] == (ex[t + 1][kk] or (None,))[0] for kk in ex[t]) and ev:
                st.inc("RC_LIT"); st.mxr("RC_LIT_example", (1, f"{name}@{t} class {c} q {ev}"))
            # ROUTE-RELAY
            for q in ev:
                if on_honest_cycle(S["hn"], q) or on_honest_cycle(T["hn"], q): continue
                ys = [y for y in sorted(set(g.succ[q])) if y in U[c]]
                route = any(ex[t].get((q, y)) != ex[t + 1].get((q, y)) for y in ys)
                st.inc("RR_events"); st.inc("RR_route" if route else "RR_relay")
                if len(qs) == 1 and not route: st.bad("SELF", f"{name}@{t}: |Q_c| = 1 but RELAY at {q}")
                if not route:
                    src = False
                    for y in ys:
                        e = ex[t][(q, y)][1]
                        if e in (q, c): continue
                        if kappa(E, S["xi"][e], c) != kappa(E, T["xi"][e], c): src = True
                        av = lambda k: q not in R.lasso(I[k]["hn"], e)[0][:R.lasso(I[k]["hn"], e)[0].index(c) + 1]
                        if av(t) != av(t + 1): src = True
                    if not src: st.bad("RR", f"{name}@{t}: RELAY at {q} without a source")
    # RC_MIN / RC_POS (walk enumeration) at every state of the phase
    if n <= WALKMAX:
        for k in range(a, b + 1):
            for c in C:
                qs = Qc[c]
                if not qs: continue
                cyc = set(R.lasso(I[k]["hn"], c)[0])
                for q in qs:
                    best = None
                    for walk, choices in walks(ctx, g, I, k, q, qs, c, U[c]):
                        m = 0
                        for v in walk[:-1]:
                            if E.rank[v] > E.rank[c]: m |= E.bit[v]
                        kv = kappa(E, (c, m, len(walk) - 1), c)
                        best = kv if best is None or kv < best else best
                        st.inc("RC_walks")
                        if any(e in cyc and choices[e] != I[k]["hn"][e] for e in choices):
                            st.inc("RC_walks_via_cycle")
                            sgm = list(I[k]["hn"])
                            for e, y in choices.items(): sgm[e] = y
                            pv = R.play_value(E, sgm, q)
                            if pv[0] != c:
                                st.inc("RC_POS"); st.mxr("RC_POS_example", (1, f"{name}@{k} class {c} q {q} walk {walk} -> cycle node {pv[0]}"))
                    st.inc("RC_MIN_checks")
                    if best != kappa(E, I[k]["xi"][q], c): st.bad("RC_MIN", f"{name}@{k}: q {q} kappa {kappa(E, I[k]['xi'][q], c)} min {best}")
    # STATIC
    k = a
    while k < b:
        e = k
        sq = lambda j: (tuple(I[j]["xi"][q] for q in Q), tuple(I[j]["hn"][q] for q in Q))
        while e < b and not fbs[e] and sq(e + 1) == sq(k): e += 1
        if e > k:
            st.inc("ST_intervals")
            odd = [v for v in range(n) if g.owner[v] == 1]
            for j in range(k, e + 1):
                if any(I[j]["hn"][v] != I[k]["hn"][v] for v in odd): st.bad("ST", f"{name}@{j}: sigmabar changes on I")
                st.inc("ST_states")
        k = e + 1 if e > k else k + 1
    # FLIPs
    check_flips(ctx, g, I, fbs, a, b, Q, C, U, Qc, st, name)


def walks(ctx, g, I, k, q, qs, c, Uc):
    """Pi_k(q): walks q = e_0, y_0, (class exit path of y_0), e_1, ..., e_j = c, e_i in Q_c distinct; yields (vertex list, choices)"""
    out = []
    def rec(e, used, walk, ch):
        for y in sorted(set(g.succ[e])):
            if y not in Uc: continue
            r = class_exit(I, k, y, qs, c)
            if r is None: continue
            path, nxt = r
            if nxt != c and nxt in used: continue
            w2 = walk + [e] + list(path)
            ch2 = dict(ch); ch2[e] = y
            if nxt == c: out.append((w2 + [c], ch2))
            else: rec(nxt, used | {nxt}, w2, ch2)
            if len(out) > 20000: return
    rec(q, {q}, [], {})
    return out


def check_flips(ctx, g, I, fbs, a, b, Q, C, U, Qc, st, name):
    n, E = ctx.n, ctx.E
    for c in C:
        qs = Qc[c]
        if len(qs) < 2: continue
        par, pth = {}, {}
        for k in range(a, b + 1):
            for q in qs:
                y = I[k]["hn"][q]
                if y not in U[c]: continue
                r = class_exit(I, k, y, qs, c)
                if r and r[1] in qs and r[1] != q: par[(k, q)] = r[1]; pth[(k, q)] = r[0]
        for (t1, q1), q2 in par.items():
            for t2 in range(t1 + 1, b + 1):
                if par.get((t2, q2)) != q1: continue
                st.inc("FL_flips")
                p1, p2 = pth[(t1, q1)], pth[(t2, q2)]
                y1 = I[t1]["hn"][q1]
                Cw = [q1] + list(p1) + [q2] + list(p2)
                s_c = 1 if E.par[c] == 1 else -1
                wtC = (sum((1 if E.par[v] == 0 else -1) * (1 << E.rank[v]) for v in Cw if E.rank[v] > E.rank[c]), s_c * len(Cw))
                k1, k2 = kappa(E, I[t1]["xi"][q2], c), kappa(E, I[t2]["xi"][q2], c)
                mult = 2 if MUT == "cost" else 1
                lhs = (k1[0] + mult * wtC[0], k1[1] + mult * wtC[1])
                if k2 < lhs: st.bad("FLa", f"{name}: flip {(q1, q2, t1, t2)}")
                nx1, nx2 = I[t1]["hn"], I[t2]["hn"]
                intact1 = all(nx2[v] == nx1[v] for v in p1)
                intact2 = all(nx1[v] == nx2[v] for v in p2)
                disj = not (set(p1) & set(p2))
                if not intact1: st.inc("FL_N1")
                if not disj: st.inc("FL_N2")
                if intact1:
                    st.inc("FL_b_checks")
                    sg = list(nx2); sg[q1] = y1
                    pv = R.play_value(E, sg, q1)
                    if not (pv[0] != c and E.rew[pv[0]] > E.rew[c]): st.bad("FLb", f"{name}: flip {(q1, q2, t1, t2)} w {pv[0]}")
                    if disj:
                        st.inc("FL_c_checks")
                        path, x = R.lasso(sg, q1)
                        if set(path[path.index(x):]) != set(Cw): st.bad("FLc", f"{name}: Z != C")
                        if not (wtC > (0, 0) and k2 > k1): st.bad("FLc", f"{name}: no strict rise")
                        st.inc("FL_N3")
                if intact1 and not disj: pass
                if not (not intact1 or not disj or (k2 > k1 and k2 >= lhs)): st.bad("NEC", f"{name}: flip {(q1, q2, t1, t2)}")
                # N3-LEVEL
                if disj:
                    h = max(Cw, key=lambda v: E.rank[v])
                    if intact1 and not (E.rank[h] > E.rank[c] and E.par[h] == 0):
                        st.inc("N3L_LOW"); st.mxr("N3L_LOW_example", (1, f"{name}: flip {(q1, q2, t1, t2)} class {c} top {h}"))
                    if E.rank[h] > E.rank[c] and E.par[h] == 0 and (h not in p2 or intact2):
                        st.inc("N3L_checks")
                        X1, X2 = I[t1]["xi"][q2][1], I[t2]["xi"][q2][1]
                        d = X1 ^ X2
                        lev = d.bit_length() - 1 if d else -1
                        need = E.rank[h] + (1 if MUT == "lev" else 0)
                        if lev < need: st.bad("N3L", f"{name}: flip {(q1, q2, t1, t2)} lev {lev} rank(h) {E.rank[h]}")
                        if lev == E.rank[h]: st.inc("N3L_equal")


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1619)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); check_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); check_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        s, t = R.read_start(gp, a[2]) if len(a) > 2 else R.starts(gp, 0, None)
        check_game(gp, s, t, st, os.path.basename(a[1]))
    print("MODE", " ".join(a), "MUT", MUT or "-", "WALKMAX", WALKMAX)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
