#!/usr/bin/env python3
r"""REFEREE-2 successor 13 (Opus 5.5, D15): mechanical check of packet P-N5-FBRED (docs/new/P-N5-FBRED-box44.md sha1 11b15455 @ c3f6f2bf).
State sequence: own SPEC N5 loop (R2-N5-DUAL/dual_check.Runner on L-SI's si.py engine, read-only), any game, S3 / random starts.
Honest frame from SPEC S1 (si evaluate: Xi = (c, mask, l), sbar). kappa_t(z) := (signed weight of P(Xi_t z), s_c * l), s_c = +1 iff
Omega(c) odd; kwt_c(v) := (sgn(v) 2^rank(v) if rank(v) > rank(c) else 0, s_c). Q = Odd vertices of out-degree >= 2; C = honest cycle
nodes of the phase; T = C u Q; U_c = lambda^{-1}(c). Lane's fbf.py / fbclimb.py not run or imported.
Checks per phase: AK ((Akappa): next in U_c, kappa = kwt + kappa(next)); ROUND (kappa-FB-ROUND); HAT (kappa-HAT-FREEZE (a) for all j and
(b), (c), by simple-path enumeration, n <= PATHCAP); PFZ (kappa-PFZ per q and Q_c-run, all j); YF (kappa-Y-FORM at states where q is on no
honest cycle); EXS (EXIT-SWITCH_D: some u in S_c exits, and the kappa identity); FEX (FREEZE-EXIT_D: j >= |U_c| and i >= |U_c| => S_c
empty; also FBP's sharper |U_c| - 1 indices, recorded); CNO (CN-ONLY_D: <= 1 fallback with S empty, and it ends the phase); RED (f <= 1 +
(n-1)(2 + rho)); REDL (late form); TV (Lemma TV at qualifying states).
Records: max f per phase, max f - n, max j over fallbacks with S != {} (late regime reached iff some j >= n), closeness of FEX.
Mutations FB_MUT: fex (FREEZE-EXIT_D with |U_c| - 2), red (FB-RED with rho := 0), yf (Y-FORM with max for min), cno (CN-ONLY asks 0).
Usage: fbred_check.py random N nmin nmax seed | files list.txt [runs] | climb steps nmin nmax seed outprefix"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("FB_MUT", "")
PATHCAP = int(os.environ.get("PATHCAP", "11"))

def kadd(a, b): return (a[0] + b[0], a[1] + b[1])

class Ctx:
    def __init__(s, g):
        s.g = g; s.n = g.n; s.E = Engine(g)
        s.Q = frozenset(v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)
    def state(s, sg):
        g, n = s.g, s.n
        vs, tf = s.E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        nxt = [sg[v] if g.owner[v] == 0 else tf[v] for v in range(n)]
        lam = tuple(vs[v][0] for v in range(n))
        return vs, nxt, lam
    def kap(s, val, c):
        sc = 1 if s.g.prio[c] % 2 == 1 else -1
        return (s.E.weight(val[1]), sc * val[2])
    def kwt(s, v, c):
        sc = 1 if s.g.prio[c] % 2 == 1 else -1
        r = s.E.rank
        w = 0
        if r[v] > r[c]: w = (1 << r[v]) if s.g.prio[v] % 2 == 0 else -(1 << r[v])
        return (w, sc)

def honest_play(nxt, v):
    seen, path, x = set(), [], v
    while x not in seen: seen.add(x); path.append(x); x = nxt[x]
    return path, x   # x = first repeated vertex

def simple_paths_best(ctx, verts, src, sink, c, sinks_drop):
    """max over simple paths p of the graph on verts (sink a sink; Even keep edges inside; Odd non-Q keep their edge) from src to sink of
    kwt_c(p minus sink), grouped by number of edges: returns dict edges -> best (prefix-max taken by caller)."""
    g = ctx.g; best = {}
    def dfs(x, vis, acc, ne):
        if x == sink:
            if ne not in best or acc > best[ne]: best[ne] = acc
            return
        acc2 = kadd(acc, ctx.kwt(x, c))
        for y in set(g.succ[x]):
            if y in verts and y not in vis:
                vis.add(y); dfs(y, vis, acc2, ne + 1); vis.discard(y)
    dfs(src, {src}, (0, 0), 0)
    return best

def check_run(gp, states, fbs, st, name):
    ctx = Ctx(gp); g, n = gp, gp.n
    info = [ctx.state(list(s)) for s, _ in states]
    tauk = [tuple(t[v] for v in range(n) if g.owner[v] == 1) for _, t in states]
    st.inc("runs")
    key = [(info[k][2], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(ctx, states, fbs, info, k0, k1, st, name)
        k0 = k1 + 1

def check_phase(ctx, states, fbs, info, k0, k1, st, name):
    g, n, Q = ctx.g, ctx.n, ctx.Q
    lam = info[k0][2]; C = frozenset(lam); T = C | Q
    U = {c: frozenset(v for v in range(n) if lam[v] == c) for c in C}
    st.inc("phases")
    K = {}
    def kap(t, z): return ctx.kap(info[t][0][z], lam[z])
    # (A kappa)
    for t in range(k0, k1 + 1):
        vs, nxt, _ = info[t]
        for z in range(n):
            c = lam[z]
            if z == c: continue
            if lam[nxt[z]] != c or kap(t, z) != kadd(ctx.kwt(z, c), kap(t, nxt[z])): st.bad("AK", f"{name}@{t} z {z}"); break
    trans = list(range(k0, k1))
    fb = [k for k in trans if fbs[k]]
    f = len(fb)
    # rho, Q-runs, Q_c-runs
    rho = sum(1 for k in trans for q in Q if info[k][0][q] != info[k + 1][0][q])
    def run_id(qs):
        ids, r = {}, 0
        for t in range(k0, k1 + 1):
            if t > k0 and any(info[t][0][q] != info[t - 1][0][q] for q in qs): r += 1
            ids[t] = r
        return ids
    qrun = run_id(Q)
    Sall = {}
    late_runs = set(); nS0 = 0
    for jj, k in enumerate(fb, start=1):
        sg0, sg1 = states[k][0], states[k + 1][0]
        Sk = [v for v in range(n) if g.owner[v] == 0 and sg0[v] != sg1[v]]
        if any(states[k][1][v] != states[k + 1][1][v] for v in range(n) if g.owner[v] == 1): st.bad("PH", f"{name}: in-phase fallback changes tau")
        S = [v for v in Sk if v not in T]
        vs, nxt, _ = info[k]
        # ROUND
        for c in C:
            for v in U[c]:
                if v == c or g.owner[v] != 0: continue
                for x in set(g.succ[v]):
                    if x in U[c] and kap(k + 1, v) < kadd(ctx.kwt(v, c), kap(k, x)): st.bad("ROUND", f"{name}@{k} v {v} x {x}")
        if not S:
            nS0 += 1
            if k + 1 != k1: st.bad("CNO", f"{name}: S-empty fallback at {k} not the phase's last transition")
            for y in Sk:
                if lam[y] != y: st.bad("CNO", f"{name}: switched y {y} not a cycle node")
            continue
        st.mxr("max_j_with_S", (jj, name)); st.mxr("max_j_minus_n_with_S", (jj - n, name))
        if jj >= n: st.inc("LATE_fallbacks"); late_runs.add(qrun[k])
        for c in C:
            Sc = [v for v in S if v in U[c]]
            if not Sc: continue
            TU = (T & U[c])
            # EXS
            ok = False
            for u in Sc:
                xs = states[k + 1][0][u]
                path, _ = honest_play(nxt, xs)
                e = next((x for x in path if x in TU or x == u), None)
                if e is not None and e != u:
                    ok = True
                    pre = path[:path.index(e)]
                    acc = (0, 0)
                    for x in pre: acc = kadd(acc, ctx.kwt(x, c))
                    if kap(k, xs) != kadd(acc, kap(k, e)): st.bad("EXS", f"{name}@{k}: kappa identity u {u}")
            if not ok: st.bad("EXS", f"{name}@{k}: no exiting u in S_c (c {c})")
            # FEX: index of k among the fallbacks of its Q_c-run
            qc = run_id(Q & U[c])
            i = sum(1 for k2 in fb if k2 <= k and qc[k2] == qc[k])
            lim = len(U[c]) - (2 if MUT == "fex" else 0)
            if jj >= lim and i >= lim: st.bad("FEX", f"{name}@{k}: j {jj} i {i} |U_c| {len(U[c])}")
            st.mxr("FEX_closeness", (min(jj, i) - len(U[c]), name))
            if jj >= len(U[c]) - 1 and i >= len(U[c]) - 1: st.inc("REC_FBP_sharp_index_reached")
    if nS0 > (0 if MUT == "cno" else 1): st.bad("CNO", f"{name}: {nS0} S-empty fallbacks")
    r_ = 0 if MUT == "red" else rho
    if f > 1 + (n - 1) * (2 + r_): st.bad("RED", f"{name}: f {f} rho {rho}")
    if f > 1 + (n - 1) + (n - 1) * len(late_runs): st.bad("REDL", f"{name}: f {f} late runs {len(late_runs)}")
    st.mxr("max_f", (f, name)); st.mxr("max_f_minus_n", (f - n, name)); st.mxr("max_rho", (rho, name))
    # YF
    for t in range(k0, k1 + 1):
        vs, nxt, _ = info[t]
        for q in Q:
            c = lam[q]
            if q == c: continue
            path, rep = honest_play(nxt, q)
            if q in path[path.index(rep):]: continue          # q on its honest cycle
            Y = [y for y in set(g.succ[q]) if lam[y] == c and q not in honest_play(nxt, y)[0]]
            agg = max if MUT == "yf" else min
            st.inc("YF_checks")
            if not Y or kap(t, q) != kadd(ctx.kwt(q, c), agg(kap(t, y) for y in Y)): st.bad("YF", f"{name}@{t}: q {q}")
    # HAT, PFZ, TV by simple-path enumeration
    if n > PATHCAP: return
    gidx = {k: j for j, k in enumerate(fb, start=1)}
    def after_j(t):  # number of fallbacks g_j with g_j < t (state index)
        return sum(1 for k in fb if k < t)
    for c in C:
        Uc = U[c]
        Gc = frozenset(v for v in Uc if v == c or v not in Q)
        best_c = {}
        for z in Gc:
            if z == c: continue
            if g.owner[z] == 1 and z in Q: continue
            bp = simple_paths_best_g(ctx, Gc, z, c, c)
            best_c[z] = bp
        qc = run_id(Q & Uc)
        for t in range(k0, k1 + 1):
            vs, nxt, _ = info[t]
            jt = after_j(t)
            for z, bp in best_c.items():
                lim = [w for ne, w in bp.items() if ne <= jt]
                if lim and kap(t, z) < max(lim): st.bad("HATa", f"{name}@{t}: z {z}")
                path, _ = honest_play(nxt, z)
                pre = path[:path.index(c)] if c in path else None
                avoids = pre is not None and not any(x in Q and x != c for x in pre)
                if avoids and bp:
                    allbest = max(bp.values())
                    if kap(t, z) > allbest: st.bad("HATb", f"{name}@{t}: z {z}")
                    if jt >= len(Uc) - 1:
                        st.inc("HATc_checks")
                        if kap(t, z) != allbest: st.bad("HATc", f"{name}@{t}: z {z}")
        # PFZ and TV
        for q in Q & Uc:
            if q == c: continue
            Gq = frozenset(v for v in Uc if v == q or v not in T)
            bq = {z: simple_paths_best_g(ctx, Gq, z, q, c) for z in Gq if z != q}
            for t in range(k0, k1 + 1):
                i_t = sum(1 for k in fb if k < t and qc[k] == qc[t])
                for z, bp in bq.items():
                    lim = [w for ne, w in bp.items() if ne <= i_t]
                    if lim and kap(t, z) < kadd(max(lim), kap(t, q)): st.bad("PFZ", f"{name}@{t}: z {z} q {q}")
                    st.inc("PFZ_checks")
        # TV at qualifying states
        for t in range(k0, k1 + 1):
            jt = after_j(t); it = sum(1 for k in fb if k < t and qrun[k] == qrun[t])
            if jt < len(Uc) - 1 or it < len(Uc) - 1: continue
            for z in Uc - T:
                cand = []
                if z in best_c and best_c[z]: cand.append(max(best_c[z].values()))
                for q in Q & Uc:
                    if q == c: continue
                    Gq = frozenset(v for v in Uc if v == q or v not in T)
                    bp = simple_paths_best_g(ctx, Gq, z, q, c)
                    if bp: cand.append(kadd(max(bp.values()), kap(t, q)))
                st.inc("TV_checks")
                if cand and kap(t, z) != max(cand): st.bad("TV", f"{name}@{t}: z {z}")

def simple_paths_best_g(ctx, verts, src, sink, c):
    """graph on verts: sink keeps no edge; Even keep edges inside; Odd (non-Q inside) keep their unique edge if inside."""
    g = ctx.g; best = {}
    def dfs(x, vis, acc, ne):
        if x == sink:
            if ne not in best or acc > best[ne]: best[ne] = acc
            return
        acc2 = kadd(acc, ctx.kwt(x, c))
        for y in set(g.succ[x]):
            if y in verts and y not in vis:
                vis.add(y); dfs(y, vis, acc2, ne + 1); vis.discard(y)
    if src not in verts: return best
    dfs(src, {src}, (0, 0), 0)
    # prefix max over edge counts
    out, cur = {}, None
    for ne in sorted(best):
        cur = best[ne] if cur is None or best[ne] > cur else cur
        out[ne] = cur
    return out

def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    check_run(gp, states, fbs, st, name)
    return states, fbs

def phase_fmax(gp, states, fbs):
    E = Engine(gp); n = gp.n; best = 0; cur = 0; prev = None
    for k in range(len(states)):
        vs, _ = E.evaluate(tuple(states[k][0][v] if gp.owner[v] == 0 else -1 for v in range(n)))
        key = (tuple(vs[v][0] for v in range(n)), tuple(states[k][1][v] for v in range(n) if gp.owner[v] == 1))
        if prev is not None and key == prev: cur += fbs[k - 1] != 0
        else: cur = 0
        prev = key; best = max(best, cur)
    return best

def mutate(rng, gp):
    n = gp.n; prio, owner, succ = list(gp.prio), list(gp.owner), [list(s) for s in gp.succ]
    r = rng.random(); v = rng.randrange(n)
    if r < 0.4: prio[v] = rng.randrange(0, n + 1)
    elif r < 0.55: owner[v] = 1 - owner[v]
    elif r < 0.8: succ[v] = sorted(set(succ[v]) | {rng.randrange(n)})
    elif len(succ[v]) > 1: succ[v].remove(rng.choice(succ[v]))
    return pg.Game(prio, owner, succ)

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            gp = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            s = [rng.choice(gp.succ[v]) for v in range(gp.n)]; t = [rng.choice(gp.succ[v]) for v in range(gp.n)]
            run_game(gp, s, t, st, f"random{seed}:{i}")
    elif a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2; rng = random.Random(5151)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                if r == 0:
                    s, t = list(Engine(gp).initial("best")), list(Engine(DC.dual(gp)).initial("best"))
                else:
                    s = [rng.choice(gp.succ[v]) for v in range(gp.n)]; t = [rng.choice(gp.succ[v]) for v in range(gp.n)]
                run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "climb":
        # hill climb on (max in-phase fallbacks per phase) - n over small games and start pairs; every scored run is fully checked
        steps, nmin, nmax, seed, out = int(a[1]), int(a[2]), int(a[3]), int(a[4]), a[5]; rng = random.Random(seed)
        gp = DC.rand_game(rng, rng.randint(nmin, nmax), "kO"); bestsc = -10 ** 9; bestg = gp
        for it in range(steps):
            cand = mutate(rng, bestg) if it else bestg
            sc = -10 ** 9; bs = None
            for r in range(4):
                s = [rng.choice(cand.succ[v]) for v in range(cand.n)]; t = [rng.choice(cand.succ[v]) for v in range(cand.n)]
                states, fbs = run_game(cand, s, t, st, f"climb{seed}:{it}:{r}")
                f = phase_fmax(cand, states, fbs) - cand.n
                if f > sc: sc, bs = f, (s, t)
            if sc >= bestsc:
                bestsc, bestg = sc, cand
                with open(out + ".pg", "w") as fh: fh.write(pg.dumps(bestg))
                with open(out + ".txt", "w") as fh: fh.write(f"score {bestsc}\nSIGMA0 {' '.join(f'{v}:{w}' for v, w in enumerate(bs[0]))}\nTAU0 {' '.join(f'{v}:{w}' for v, w in enumerate(bs[1]))}\n")
        st.mxr("climb_best_fmax_minus_n", (bestsc, out))
    print("MODE", " ".join(a), "MUT", MUT or "-")
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
