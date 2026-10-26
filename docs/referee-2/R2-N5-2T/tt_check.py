#!/usr/bin/env python3
r"""REFEREE-2 successor 14 (Opus 5.5, D15): mechanical check of packet P-N5-2T (docs/si/P-N5-2T-box16.md sha1 fcb91130 @ cbb3b738).
State sequence: own SPEC N5 loop (R2-N5-DUAL/dual_check.Runner on L-SI's si.py engine, read-only), honest frame and kappa from
R2-N5-FBRED/fbred_check.Ctx (REFEREE-2 succ. 13's own code). The lane's experiments/si/fb2o/ (fb2o.py, climb2o.py) NOT run or imported.
Definitions as in the packet: Q = Odd vertices of out-degree >= 2; C = honest cycle nodes of the phase; T = C u Q; U_c = lambda^-1(c);
Q_c = (Q n U_c) - {c}; w_c = |U_c| - 1; Cyc_c = {(0, s_c l) : 1 <= l <= w_c}; G_c, G_c^q, kopt_c, kopt^q by simple-path enumeration;
A_q, V_q'(alpha) as in packet §4. Fallback index convention: a fallback k -> k+1 is counted by its SOURCE k (FBRED-N1); jt := #phase
fallbacks with source < t; for a q-run Theta containing t, it := #fallbacks with source in Theta and < t.
Checks per phase (classes with |U_c| <= UCAP enumerated; larger ones counted as skipped):
  YB     q in Q_c on its own honest cycle => kappa_t(q) in Cyc_c (every state)
  ROUTE  |Q_c| = 2 => q or q' direct (every state)
  PFZQ   per q in Q_c, q-run Theta, t in Theta, z in (U_c - T) u {q}: kappa_t(z) >= best kwt over simple paths of G_c^q to q with
         <= it edges + kappa_t(q)
  DIR    jt >= w_c and q direct => kappa_t(q) in A_q
  SAT    |Q_c| = 2, t in q-run Theta with jt >= w_c and it >= w_c => kappa_t(q') in V_q'(kappa_Theta(q))
  FB2T   phase with (2T) and late fallbacks (index >= n): N_late (distinct Q-tuples at late sources) <= 1 + sum_c (N_c - 1)
  FB2W   (my strengthening of FB2T's proof, labelled as such: step 1 uses only k_i > g_{w_c} for classes with Q_c != {}; so the same
         count holds for the fallbacks with index >= 1 + max w_c): checked when reached; also checks N = #Q-runs holding them
Records: closeness of SAT's hypothesis: max over (phase, class, ordered pair, t) of min(jt, it) - w_c (>= 0 iff SAT checked).
Mutations TT_MUT: pfz2 (PFZQ with it + 2 edges), dircyc (A_q without Cyc_c), sat0 (SAT with no saturation: it >= 0), satcyc (V without
Cyc_c), satalpha (V_q'(alpha) with alpha := kappa of q at the run's START replaced by (0,0)).
Usage: tt_check.py files list.txt [runs] | union list.txt gadget [runs] | random N nmin nmax seed | climb steps n seed outprefix"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FBRED"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-DUAL"))
import dual_check as DC
import fbred_check as FC
pg, Engine, Stats = DC.pg, DC.Engine, DC.Stats
MUT = os.environ.get("TT_MUT", "")
UCAP = int(os.environ.get("UCAP", "13"))
kadd, honest_play, spb = FC.kadd, FC.honest_play, FC.simple_paths_best_g

def on_own_cycle(nxt, v):
    path, rep = honest_play(nxt, v)
    return v in path[path.index(rep):]

def direct(nxt, q, c, Qc):
    if on_own_cycle(nxt, q): return True
    path, _ = honest_play(nxt, q)
    for x in path[1:]:
        if x == c: return True
        if x in Qc: return False
    return False

SATvals = {}
def check_run(gp, states, fbs, st, name):
    ctx = FC.Ctx(gp); n = gp.n
    info = [ctx.state(list(s)) for s, _ in states]
    tauk = [tuple(t[v] for v in range(n) if gp.owner[v] == 1) for _, t in states]
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
    fb = [k for k in range(k0, k1) if fbs[k]]
    for k in fb:
        if any(states[k][1][v] != states[k + 1][1][v] for v in range(n) if g.owner[v] == 1): st.bad("PH", f"{name}: in-phase fallback changes tau")
    def kap(t, z): return ctx.kap(info[t][0][z], lam[z])
    def jt(t): return sum(1 for k in fb if k < t)
    def runs_of(qs):
        ids, r = {}, 0
        for t in range(k0, k1 + 1):
            if t > k0 and any(info[t][0][q] != info[t - 1][0][q] for q in qs): r += 1
            ids[t] = r
        return ids
    qrunQ = runs_of(Q)
    Qcs = {c: frozenset(q for q in Q & U[c] if q != c) for c in C}
    two_t = all(len(Qcs[c]) <= 2 for c in C)
    st.mxr("max_f", (len(fb), name))
    if two_t: st.inc("phases_2T")
    Aset, Vfun, Nc = {}, {}, {}
    for c in C:
        Qc = Qcs[c]
        if not Qc: continue
        Uc = U[c]; wc = len(Uc) - 1
        if len(Qc) == 2:
            st.inc("classes_2term"); st.mxr("max_f_in_phase_with_2term_class", (len(fb), name))
            qr_all = {q: runs_of([q]) for q in Qc}
            for t in range(k0, k1 + 1):
                for q in Qc:
                    it = sum(1 for k in fb if k < t and qr_all[q][k] == qr_all[q][t])
                    st.mxr("SAT_closeness_all_classes", (min(jt(t), it) - wc, f"{name}@{t} c {c} q {q} |U_c| {len(Uc)}"))
        if len(Uc) > UCAP: st.inc("classes_skipped_UCAP"); continue
        sc = 1 if g.prio[c] % 2 == 1 else -1
        cyc = set() if MUT in ("dircyc",) else {(0, sc * l) for l in range(1, wc + 1)}
        cycV = set() if MUT == "satcyc" else {(0, sc * l) for l in range(1, wc + 1)}
        Gc = frozenset(v for v in Uc if v == c or v not in Q)
        kopt_c = {}
        def koc(y):
            if y not in kopt_c:
                b = spb(ctx, Gc, y, c, c) if y in Gc else {}
                kopt_c[y] = max(b.values()) if b else None
            return kopt_c[y]
        kq_cache = {}
        def kq(q):
            if q not in kq_cache:
                Gq = frozenset(v for v in Uc if v == q or v not in T)
                kq_cache[q] = (Gq, {z: spb(ctx, Gq, z, q, c) for z in Gq if z != q})
            return kq_cache[q]
        A = {}
        for q in Qc:
            s = set(cyc)
            for y in set(g.succ[q]):
                if y not in Uc: continue
                if y == c: s.add(ctx.kwt(q, c))
                if y not in Q:
                    v = koc(y)
                    if v is not None: s.add(kadd(ctx.kwt(q, c), v))
            A[q] = s
            if len(s) > len(set(y for y in g.succ[q] if y in Uc)) + wc: st.bad("ASIZE", f"{name}: |A_q| {len(s)}")
        Aset[c] = A
        def V(qp, q, alpha, Uc=Uc, c=c, cycV=cycV):
            s = set(cycV)
            _, bq = kq(q)
            for y in set(g.succ[qp]):
                if y not in Uc or y == qp: continue
                if y == q: b = alpha
                elif y == c: b = (0, 0)
                else:
                    cands = []
                    v = koc(y)
                    if v is not None: cands.append(v)
                    if y in bq and bq[y]: cands.append(kadd(max(bq[y].values()), alpha))
                    if not cands: continue
                    b = max(cands)
                s.add(kadd(ctx.kwt(qp, c), b))
            return s
        Vfun[c] = V
        qruns = {q: runs_of([q]) for q in Qc}
        for t in range(k0, k1 + 1):
            vs, nxt, _ = info[t]
            j = jt(t)
            for q in Qc:
                if on_own_cycle(nxt, q):
                    st.inc("YB_checks")
                    if kap(t, q) not in {(0, sc * l) for l in range(1, wc + 1)}: st.bad("YB", f"{name}@{t}: q {q}")
            if len(Qc) == 2:
                q1, q2 = sorted(Qc)
                st.inc("ROUTE_checks")
                if not (direct(nxt, q1, c, Qc) or direct(nxt, q2, c, Qc)): st.bad("ROUTE", f"{name}@{t}: {q1},{q2}")
            for q in Qc:
                it = sum(1 for k in fb if k < t and qruns[q][k] == qruns[q][t])
                # PFZQ
                Gq, bq = kq(q)
                lim_e = it + (2 if MUT == "pfz2" else 0)
                for z, bp in bq.items():
                    lim = [w for ne, w in bp.items() if ne <= lim_e]
                    st.inc("PFZQ_checks")
                    if lim and kap(t, z) < kadd(max(lim), kap(t, q)): st.bad("PFZQ", f"{name}@{t}: z {z} q {q}")
                # DIR
                if j >= wc and direct(nxt, q, c, Qc):
                    st.inc("DIR_checks"); st.inc("DIRbr_cycle" if on_own_cycle(nxt, q) else ("DIRbr_y_is_c" if nxt[q] == c else "DIRbr_free"))
                    if kap(t, q) not in A[q]: st.bad("DIR", f"{name}@{t}: q {q}")
                # SAT (ordered pair: saturated run of q, value of the other)
                if len(Qc) == 2:
                    qp = next(x for x in Qc if x != q)
                    st.mxr("SAT_closeness", (min(j, it) - wc, f"{name}@{t} c {c} q {q} |U_c| {len(Uc)}"))
                    need = 0 if MUT == "sat0" else wc
                    if j >= need and it >= need:
                        st.inc("SAT_checks")
                        alpha = (0, 0) if MUT == "satalpha" else kap(t, q)
                        if kap(t, qp) not in V(qp, q, alpha): st.bad("SAT", f"{name}@{t}: q {q} q' {qp}")
                        if on_own_cycle(nxt, qp): st.inc("SATbr_cycle")
                        else:
                            y = nxt[qp]
                            if y == q: st.inc("SATbr_y_is_q")
                            elif y == c: st.inc("SATbr_y_is_c")
                            else:
                                pth, _ = honest_play(nxt, y)
                                e = next(x for x in pth if x in (q, c))
                                st.inc("SATbr_free_via_q" if e == q else "SATbr_free_via_c")
                        SATvals.setdefault((name, c, qp), set()).add((kap(t, q), kap(t, qp)))
        # N_c
        if len(Qc) == 1:
            (q,) = tuple(Qc); Nc[c] = len(A[q])
        elif len(Qc) == 2:
            q1, q2 = sorted(Qc)
            def mxV(qp, q):
                # max over alpha of |V_qp(alpha)|: bounded by d_qp + w_c; use that bound (the packet's N_c uses max_alpha)
                return len(set(y for y in g.succ[qp] if y in Uc and y != qp)) + wc
            Nc[c] = len(A[q1]) * (wc + mxV(q2, q1)) + len(A[q2]) * (wc + mxV(q1, q2))
    # FB2T and the strengthened FB2W
    if not two_t: return
    cls = [c for c in C if Qcs[c]]
    if any(c not in Nc for c in cls): return
    bound = 1 + sum(Nc[c] - 1 for c in cls)
    def count_from(thr):
        src = [k for jj, k in enumerate(fb, start=1) if jj >= thr]
        if not src: return None
        xs = set(tuple(kap(k, q) for q in sorted(Q)) for k in src)
        runs = set(qrunQ[k] for k in src)
        return len(xs), len(runs)
    r = count_from(n)
    if r is not None:
        st.inc("FB2T_checks")
        if r[0] != r[1]: st.bad("FB2T_id", f"{name}: distinct x {r[0]} vs Q-runs {r[1]}")
        if r[0] > bound: st.bad("FB2T", f"{name}: N_late {r[0]} > {bound}")
    W = max(len(U[c]) - 1 for c in cls) if cls else 0
    r = count_from(W + 1)
    if r is not None:
        st.inc("FB2W_checks"); st.mxr("FB2W_max_count", (r[0], name))
        if r[0] != r[1]: st.bad("FB2W_id", f"{name}: distinct x {r[0]} vs Q-runs {r[1]}")
        if r[0] > bound: st.bad("FB2W", f"{name}: N {r[0]} > {bound}")

def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    check_run(gp, states, fbs, st, name)
    return states, fbs

def gadget(base, kind, P):
    """disjoint union of base with a small class {c, q, q'} (kind 'g3') or {c, q, q', e} with an Even e (kind 'g4');
    c gets priority P (above every gadget vertex), q, q' low priorities."""
    prio, owner, succ = list(base.prio), list(base.owner), [list(s) for s in base.succ]
    n = base.n; c, q, qp = n, n + 1, n + 2
    if kind == "g3":
        prio += [P, 0, 1]; owner += [1, 1, 1]
        succ += [[q], [c, qp], [q, c]]
    elif kind == "g4":
        e = n + 3
        prio += [P, 0, 1, 2]; owner += [1, 1, 1, 0]
        succ += [[q], [c, e], [q, c], [qp, c]]
    elif kind == "g4b":
        e = n + 3
        prio += [P, 2, 0, 1]; owner += [0, 1, 1, 0]
        succ += [[q, e], [c, qp], [e, c], [q, qp]]
    elif kind in ("g5", "g5c"):
        # c <-> x is the cycle (top c); q -> {h1, c}, qp -> {y, c}, y (Even) -> {q, h2}; h1, h2 forced to c with ODD priorities
        # above c (negative weights, not on the cycle). g5: h1 > h2 in rank... see below; the free branch y not in T is exercised:
        #   g5  : h2 more negative than q's route, so Even at y goes to q: q' -> y -> q -> h1 -> c (free, via q)
        #   g5c : h1 more negative, Even at y goes to h2: q' -> y -> h2 -> c (free, via c)
        x, h1, y, h2 = n + 1, n + 3, n + 5, n + 6; q, qp = n + 2, n + 4
        o1 = P + 1 if P % 2 == 0 else P + 2; o2 = o1 + 2
        ph1, ph2 = (o1, o2) if kind == "g5" else (o2, o1)
        prio += [P, 0, 1, ph1, 3, 2, ph2]; owner += [1, 1, 1, 1, 1, 0, 1]
        succ += [[x], [n], [h1, n], [n], [y, n], [q, h2], [n]]
    return pg.Game(prio, owner, succ)

def starts(gp, r, rng):
    if r == 0: return list(Engine(gp).initial("best")), list(Engine(DC.dual(gp)).initial("best"))
    return [rng.choice(gp.succ[v]) for v in range(gp.n)], [rng.choice(gp.succ[v]) for v in range(gp.n)]

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2; rng = random.Random(1414)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "union":
        kind = a[2]; runs = int(a[3]) if len(a) > 3 else 2; rng = random.Random(1415)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            base = pg.read(os.path.join(DC.ROOT, path))
            for P in (max(base.prio) + 1, max(base.prio) + 2):
                gp = gadget(base, kind, P)
                for r in range(runs):
                    s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"{path}+{kind}P{P}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            gp = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            s, t = starts(gp, 1, rng); run_game(gp, s, t, st, f"random{seed}:{i}")
    print("MODE", " ".join(a), "MUT", MUT or "-", "UCAP", UCAP)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    if SATvals:
        print("SAT_distinct_(kq,kq')_pairs_per_(run,class,q'):", "max", max(len(v) for v in SATvals.values()),
              "classes_with_>1:", sum(1 for v in SATvals.values() if len(v) > 1), "of", len(SATvals))
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
