#!/usr/bin/env python3
r"""REFEREE-2 successor 17 (Opus 5.5, D15): mechanical check of packet P-N5-CHOSEN (docs/si/P-N5-CHOSEN-box19.md sha1 764cfbb3 @ 9196c318).
State sequence = succ. 13's SPEC loop (dual_check.Runner); Xi = my own play values of (sigma, sigmabar) (R2-N5-RUND state_info, ENGXI
cross-check). Lane tools (experiments/si/rund/chosen.py, tvend.py, ...) NOT run or imported.
kappa inside class c = (signed weight of P(Xi), s_c * length) = the engine key minus its first component; kwt_c(v) = (wt_c(v), s_c). Both
self-checked: KADD (additivity on every honest play prefix to its exit) and KORD (kappa order = Xi order inside a class).
Checks per in-phase transition t -> t+1 and class c (Q_c := Q ∩ U_c minus c; exit / class exit path per y as P-N5-FLIP §3):
  CH      CHOSEN: q in Q_c on no honest cycle at t, t+1, RELAY rho event: e := exit of sigmabar_t(q) at t; e != c, e != q, and
          (Xi_t(e) != Xi_{t+1}(e) or q on e's honest play at t+1 (TOG)); also the proof's equalities kappa_t(q) = kwt(q) + kappa_t(y*),
          kappa_s(y*) = kwt(p) + kappa_s(e), s = t, t+1 (CH_add)
  RC      RELAY-CHAIN: chain e_0 = q, e_{i+1} = chosen exit of e_i while e_i is RELAY: distinct, <= |Q_c| - 1 steps, ends at a ROUTE / CYC
          event or a TOG step; (a) every transition with a rho event in the class has a ROUTE or CYC event or a TOG step there;
          (b) per phase and class: sum rho_q <= |Q_c| (ROUTE_c + CYC_c + TOG_c)
  TV      TV-END: at every state t and class c test (H) directly (kappa_t(z) = TV_Theta(z) for all z in U_c \ T, TV from EXACT kopt_c,
          kopt^q by simple-path enumeration in G_c, G_c^q, budget); from the first t with (H): every later in-phase transition switches no
          Even x in U_c \ T, keeps Xi on Q_c, and (H) holds again. Also R56 (g)'s trigger (|U_c| - 1 fallbacks of the phase and of the Q-run
          before t) => (H) (TVG, landed; consistency)
Controls MUT: next (CHOSEN with sigmabar_{t+1}(q) as the chosen option), noH (TV-END's conclusion "no switch in U_c \ T" at every state,
without (H): must fail).
Usage: chosen_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats
MUT = os.environ.get("CH_MUT", "")
BUDGET = int(os.environ.get("BUDGET", "300000"))


class Over(Exception): pass


def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); g, n = gp, gp.n
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    Q = frozenset(v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)
    st.inc("runs"); st.inc("states", len(I))
    tauk = [tuple(b[v] for v in range(n) if g.owner[v] == 1) for _, b in states]
    key = [(I[k]["lamX"], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(ctx, g, I, fbs, k0, k1, Q, st, name)
        k0 = k1 + 1


def kap(E, val):
    k = E.key(val); return (k[1], k[2])


def kwt(E, c, v):
    s = 1 if E.par[c] == 1 else -1
    return (E.weight(E.bit[v]) if E.rank[v] > E.rank[c] else 0, s)


def add(a, b): return (a[0] + b[0], a[1] + b[1])


def check_phase(ctx, g, I, fbs, a, b, Q, st, name):
    n, E = ctx.n, ctx.E
    st.inc("phases")
    lam = I[a]["lamX"]
    C = sorted(set(lam))
    U = {c: frozenset(v for v in range(n) if lam[v] == c) for c in C}
    Qc = {c: frozenset(q for q in Q & U[c] if q != c) for c in C}
    hn = {k: I[k]["hn"] for k in range(a, b + 1)}
    xi = {k: I[k]["xi"] for k in range(a, b + 1)}

    def play(k, v):
        path, x = R.lasso(hn[k], v)
        return path, path[path.index(x):]

    def on_cycle(k, v):
        _, cyc = play(k, v); return v in cyc

    def exit_of(k, c, y):
        stop = Qc[c] | {c}; p, x, seen = [], y, set()
        while x not in stop:
            if x in seen: return None
            seen.add(x); p.append(x); x = hn[k][x]
        return tuple(p), x

    # self-checks of kappa
    for k in range(a, b + 1):
        for c in C:
            for z in U[c]:
                st.inc("KADD_checks")
                ex = exit_of(k, c, z)
                if ex is None: st.bad("EXIT_none", f"{name}@{k}"); continue
                p, e = ex
                tot = kap(E, xi[k][e])
                for v in p: tot = add(tot, kwt(E, c, v))
                if tot != kap(E, xi[k][z]): st.bad("KADD", f"{name}@{k}: z {z} c {c}")
    for c in C:
        zs = sorted(U[c])
        for z1 in zs[:6]:
            for z2 in zs[:6]:
                st.inc("KORD_checks")
                if (E.key(xi[a][z1]) < E.key(xi[a][z2])) != (kap(E, xi[a][z1]) < kap(E, xi[a][z2])): st.bad("KORD", f"{name}@{a}")
    # CHOSEN / RELAY-CHAIN
    for c in C:
        if not Qc[c]: continue
        rho_c = route_c = cyc_c = tog_c = 0
        for t in range(a, b):
            ev = {q for q in Qc[c] if xi[t][q] != xi[t + 1][q]}
            if not ev: continue
            typ = {}
            for q in ev:
                if on_cycle(t, q) or on_cycle(t + 1, q): typ[q] = "CYC"; continue
                route = False
                for y in set(g.succ[q]):
                    if y not in U[c]: continue
                    if exit_of(t, c, y) != exit_of(t + 1, c, y): route = True; break
                typ[q] = "ROUTE" if route else "RELAY"
            rho_c += len(ev)
            route_c += sum(1 for q in ev if typ[q] == "ROUTE"); cyc_c += sum(1 for q in ev if typ[q] == "CYC")
            st.inc("EV_" + "x", 0)
            for q in ev: st.inc("EV_" + typ[q])
            has_end = any(typ[q] in ("ROUTE", "CYC") for q in ev)
            tog_here = False

            def chosen(qq):
                ys = hn[t + 1][qq] if MUT == "next" else hn[t][qq]
                return ys, exit_of(t, c, ys)

            for q in ev:
                if typ[q] != "RELAY": continue
                st.inc("CH_checks")
                ys, (p, e) = chosen(q)
                if ys not in U[c]: st.bad("CH_ystar", f"{name}@{t}")
                if e == c: st.bad("CH_c", f"{name}@{t}: q {q} chosen exit is c"); continue
                if e == q: st.bad("CH_q", f"{name}@{t}")
                evt = xi[t][e] != xi[t + 1][e]
                pt1, _ = play(t + 1, e)
                tog = q in pt1
                if tog: st.inc("CH_TOG")
                if tog and evt: st.inc("CH_TOG_with_event")
                if tog and not evt: st.inc("CH_TOG_only")
                if evt: st.inc("CH_source_event")
                if not evt and not tog: st.bad("CH", f"{name}@{t}: q {q} e {e} no event, no TOG")
                # proof equalities
                kq = add(kwt(E, c, q), kap(E, xi[t][ys]))
                if MUT != "next" and kq != kap(E, xi[t][q]): st.bad("CH_add_q", f"{name}@{t}")
                for s_ in (t, t + 1):
                    if exit_of(s_, c, ys) == (p, e):
                        tot = kap(E, xi[s_][e])
                        for v in p: tot = add(tot, kwt(E, c, v))
                        if tot != kap(E, xi[s_][ys]): st.bad("CH_add_y", f"{name}@{s_}")
                    elif MUT != "next": st.bad("CH_relay_def", f"{name}@{t}")
                # chain
                chain = [q]; cur = q; end = None
                while True:
                    _, (_, nx) = chosen(cur)
                    if nx == c: end = "C"; break
                    if nx not in ev: end = "TOG"; break
                    if nx in chain: end = "REPEAT"; break
                    chain.append(nx)
                    if typ[nx] != "RELAY": end = typ[nx]; break
                    cur = nx
                st.inc("RC_chains"); st.mxr("RC_longest", (len(chain) - 1, f"{name}@{t} |Q_c| {len(Qc[c])}"))
                if end in ("C", "REPEAT"): st.bad("RC_end", f"{name}@{t}: {end} chain {chain}")
                if len(chain) - 1 > len(Qc[c]) - 1: st.bad("RC_len", f"{name}@{t}")
                if end == "TOG":
                    tog_c += 1; tog_here = True
                    _, (_, last_e) = chosen(chain[-1])
                    if not (chain[-1] in play(t + 1, last_e)[0]): st.bad("RC_tog", f"{name}@{t}")
                st.inc("RC_end_" + str(end))
            st.inc("RCa_checks")
            if not has_end and not tog_here: st.bad("RCa", f"{name}@{t} class {c}")
        if rho_c:
            st.inc("RCb_checks")
            if rho_c > len(Qc[c]) * (route_c + cyc_c + tog_c): st.bad("RCb", f"{name}@{a} class {c}")
            st.mxr("RCb_max_rho_class_phase", (rho_c, f"{name}@{a} |Q_c| {len(Qc[c])} ROUTE {route_c} CYC {cyc_c} TOG {tog_c}"))
    # TV-END
    T = Q | set(C)
    if MUT == "noH":
        for c in C:
            for k in range(a, b):
                for x in U[c] - T:
                    if g.owner[x] == 0 and I[k]["sg"][x] != I[k + 1]["sg"][x]: st.bad("TV_switch_noH", f"{name}@{k} class {c} x {x}")
        return
    for c in C:
        inner = sorted(U[c] - T)
        if not inner: continue
        try:
            kopt = {}
            for e in [c] + sorted(Qc[c]):
                kopt[e] = best_paths(ctx, g, U[c], T, c, e, BUDGET)
        except Over:
            st.inc("TV_UNK_classes"); continue
        st.inc("TV_classes")
        def H(k):
            for z in inner:
                cands = []
                if z in kopt[c]: cands.append(kopt[c][z])
                for q in Qc[c]:
                    if z in kopt[q]: cands.append(add(kopt[q][z], kap(E, xi[k][q])))
                if not cands or kap(E, xi[k][z]) != max(cands): return False
            return True
        Hk = {k: H(k) for k in range(a, b + 1)}
        # R56 (g) trigger, Q-runs
        qrun_start = a; fb_phase = 0; fb_run = 0
        for k in range(a, b + 1):
            if k > a:
                if fbs[k - 1]: fb_phase += 1
                if any(xi[k][q] != xi[k - 1][q] for q in Q): qrun_start = k; fb_run = 0
                elif fbs[k - 1]: fb_run += 1
            if fb_phase >= len(U[c]) - 1 and fb_run >= len(U[c]) - 1:
                st.inc("TVG_checks")
                if not Hk[k]: st.bad("TVG", f"{name}@{k} class {c}")
        first = next((k for k in range(a, b + 1) if Hk[k]), None)
        if first is None: continue
        st.inc("TV_H_reached"); st.mxr("TV_H_max_Qc", (len(Qc[c]), f"{name}@{first} n {n}"))
        if len(Qc[c]) >= 2: st.inc("TV_H_reached_Qc_ge2")
        if first < b: st.inc("TV_H_reached_before_end")
        for k in range(first, b):
            st.inc("TV_transitions")
            if Qc[c]: st.inc("TV_transitions_Qc_ge1")
            if len(Qc[c]) >= 2: st.inc("TV_transitions_Qc_ge2")
            if Qc[c] and any(g.owner[x] == 0 and len(set(g.succ[x]) & U[c]) >= 2 for x in inner): st.inc("TV_transitions_Qc_ge1_choice")
            for x in inner:
                if g.owner[x] == 0 and I[k]["sg"][x] != I[k + 1]["sg"][x]: st.bad("TV_switch", f"{name}@{k} class {c} x {x}")
            if any(xi[k][q] != xi[k + 1][q] for q in Qc[c]): st.bad("TV_rho", f"{name}@{k} class {c}")
            if not Hk[k + 1]: st.bad("TV_H", f"{name}@{k + 1} class {c}")
        st.mxr("TV_frozen_span", (b - first, f"{name}@{first} |Q_c| {len(Qc[c])}"))


def best_paths(ctx, g, Uc, T, c, e, budget):
    """best kwt_c-weight (end excluded) of a simple path to e in G_c (e = c) or G_c^e: vertices Uc minus (T minus {e}), e a sink."""
    E = ctx.E
    allowed = set(v for v in Uc if v not in T or v == e)
    out, cnt = {}, [0]
    for z in sorted(Uc - T):
        if z not in allowed: continue
        best = [None]
        def dfs(y, vis, w):
            cnt[0] += 1
            if cnt[0] > budget: raise Over()
            if y == e:
                if best[0] is None or w > best[0]: best[0] = w
                return
            w2 = add(w, kwt(E, c, y))
            for x in set(g.succ[y]):
                if x in allowed and x not in vis:
                    vis.add(x); dfs(x, vis, w2); vis.discard(x)
        dfs(z, {z}, (0, 0))
        if best[0] is not None: out[z] = best[0]
    return out


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1719)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H3.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        s, t = R.read_start(gp, a[2]) if len(a) > 2 else R.starts(gp, 0, None)
        run_game(gp, s, t, st, os.path.basename(a[1]))
    print("MODE", " ".join(a), "MUT", MUT or "-", "BUDGET", BUDGET)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
