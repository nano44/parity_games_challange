#!/usr/bin/env python3
r"""REFEREE-2 successor 14 (Opus 5.5, D15): mechanical check of packet P-N5-FBK (docs/new/P-N5-FBK-box44.md sha1 afd7c65a @ 5d723af6).
State sequence and honest frame as in R2-N5-2T/tt_check.py (own code; succ. 13's SPEC loop and fbred_check.Ctx). The lane's
experiments/new/box44/altcheck.py is NOT run or imported.
Checks per phase (classes with |U_c| <= UCAP enumerated):
  ROUTEK  par_t(q) relation acyclic for every class at every state; depth <= m_c - 1
  SATK    t > g_{w_c}, q not direct, p = par_t(q), t in p-run Theta with >= w_c fallbacks of Theta before t => kappa_t(q) in S_{q,p} + kappa_t(p)
  DEPTH   per phase, at late indices (fallback index >= n; never reached so far) and at the 'reachable' indices >= 1 + max w_c (my
          strengthening; step 2 of the proof uses only k_i > g_{w_c}): V_{q,h} <= sum_{p != q} D_c V_{p,h-1}, V_{q,0} <= |A_q|,
          N <= 1 + sum_q (V_q - 1), and #distinct tuples = #Q-runs
  ALT     every in-phase transition with sigma-bar(q) change, q in Q_c: classify clean strict / clean tie / non-clean / cycle node; clean =>
          kappa_{t+1}(q) >= kappa_t(q), equality only if (kappa_t(y2) = kappa_t(y1) and kappa_{t+1}(y2) = kappa_t(y2))
  NEP     epochs of the phase <= 1 + sum_q (rho_q + tie_q + nc_q + cyc_q)
Mutations FK_MUT: satk0 (SATK without saturation), shift (S_{q,p} + kappa at the run's start replaced by (0,0)), altstrict (ALT asks
strict always).
Usage: fbk_check.py files list.txt [runs] | union list.txt gadget [runs] | random N nmin nmax seed"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-2T"))
import tt_check as TT
DC, FC, pg, Engine, Stats = TT.DC, TT.FC, TT.pg, TT.Engine, TT.Stats
MUT = os.environ.get("FK_MUT", "")
UCAP = int(os.environ.get("UCAP", "13"))
kadd, honest_play, spb, on_own_cycle = FC.kadd, FC.honest_play, FC.simple_paths_best_g, TT.on_own_cycle

def par(nxt, q, c, Qc):
    """first vertex of Qc - {q} on q's honest play before c, or None if q is direct"""
    if on_own_cycle(nxt, q): return None
    path, _ = honest_play(nxt, q)
    for x in path[1:]:
        if x == c: return None
        if x in Qc: return x
    return None

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
    def kap(t, z): return ctx.kap(info[t][0][z], lam[z])
    def jt(t): return sum(1 for k in fb if k < t)
    def runs_of(qs):
        ids, r = {}, 0
        for t in range(k0, k1 + 1):
            if t > k0 and any(info[t][0][q] != info[t - 1][0][q] for q in qs): r += 1
            ids[t] = r
        return ids
    Qcs = {c: frozenset(q for q in Q & U[c] if q != c) for c in C}
    st.mxr("max_m_c", (max([len(x) for x in Qcs.values()] + [0]), name))
    # ROUTEK at every state (no enumeration needed)
    depth = {}
    for t in range(k0, k1 + 1):
        nxt = info[t][1]
        for c in C:
            Qc = Qcs[c]
            if len(Qc) < 2: continue
            for q in Qc:
                seen, x, d = {q}, q, 0
                while True:
                    p = par(nxt, x, c, Qc)
                    if p is None: break
                    if p in seen: st.bad("ROUTEK", f"{name}@{t}: cycle at {q}"); break
                    seen.add(p); x = p; d += 1
                st.inc("ROUTEK_checks"); st.mxr("max_depth", (d, f"{name}@{t} m_c {len(Qc)}"))
                if d > len(Qc) - 1: st.bad("ROUTEK", f"{name}@{t}: depth {d} > m_c - 1")
                depth[(t, q)] = d
    # ALT and NEP (no enumeration)
    eps = 1; cnt = {"rho": 0, "tie": 0, "nc": 0, "cyc": 0}
    for t in range(k0, k1):
        nxt0, nxt1 = info[t][1], info[t + 1][1]
        if any(nxt0[q] != nxt1[q] for q in Q): eps += 1
        for q in Q:
            if info[t][0][q] != info[t + 1][0][q]: cnt["rho"] += 1
            y1, y2 = nxt0[q], nxt1[q]
            if y1 == y2: continue
            c = lam[q]
            if q == c: cnt["cyc"] += 1; st.inc("ALT_cycnode"); continue
            clean = (not on_own_cycle(nxt0, q)) and (not on_own_cycle(nxt1, q)) and q not in honest_play(nxt0, y2)[0]
            if not clean: cnt["nc"] += 1; st.inc("ALT_nonclean"); continue
            a, b = kap(t, q), kap(t + 1, q)
            tie = kap(t, y2) == kap(t, y1) and kap(t + 1, y2) == kap(t, y2)
            if b < a: st.bad("ALT", f"{name}@{t}: q {q} decreases")
            if b == a:
                st.inc("ALT_clean_equal")
                if not tie or MUT == "altstrict": st.bad("ALT", f"{name}@{t}: q {q} equal without tie")
                cnt["tie"] += 1
            else: st.inc("ALT_clean_strict")
    st.inc("NEP_checks")
    if eps > 1 + sum(cnt.values()): st.bad("NEP", f"{name}: epochs {eps} > 1 + {cnt}")
    st.mxr("max_epochs", (eps, name))
    # SATK and DEPTH need enumeration
    A, Dc, Sset = {}, {}, {}
    for c in C:
        Qc = Qcs[c]
        if not Qc: continue
        Uc = U[c]; wc = len(Uc) - 1
        if len(Uc) > UCAP:
            st.inc("classes_skipped_UCAP"); continue
        sc = 1 if g.prio[c] % 2 == 1 else -1
        Gc = frozenset(v for v in Uc if v == c or v not in Q)
        dq = {q: len(set(y for y in g.succ[q] if y in Uc)) for q in Qc}
        Dc[c] = max(dq.values()) + wc
        for q in Qc:
            s = {(0, sc * l) for l in range(1, wc + 1)}
            for y in set(g.succ[q]):
                if y not in Uc: continue
                if y == c: s.add(ctx.kwt(q, c))
                if y not in Q:
                    b = spb(ctx, Gc, y, c, c) if y in Gc else {}
                    if b: s.add(kadd(ctx.kwt(q, c), max(b.values())))
            A[q] = s
        for p in Qc:
            Gp = frozenset(v for v in Uc if v == p or v not in T)
            for q in Qc:
                if q == p: continue
                s = set()
                for y in set(g.succ[q]):
                    if y not in Uc: continue
                    if y == p: s.add(ctx.kwt(q, c))
                    elif y not in T and y in Gp:
                        b = spb(ctx, Gp, y, p, c)
                        if b: s.add(kadd(ctx.kwt(q, c), max(b.values())))
                if len(s) > dq[q]: st.bad("SSIZE", f"{name}: |S| {len(s)} > d_q {dq[q]}")
                Sset[(q, p)] = s
        if len(Qc) < 1: continue
        pruns = {p: runs_of([p]) for p in Qc}
        for t in range(k0, k1 + 1):
            nxt = info[t][1]; j = jt(t)
            for q in Qc:
                p = par(nxt, q, c, Qc)
                if p is None: continue
                it = sum(1 for k in fb if k < t and pruns[p][k] == pruns[p][t])
                need = 0 if MUT == "satk0" else wc
                st.mxr("SATK_closeness", (min(j, it) - wc, f"{name}@{t} c {c} q {q} p {p} |U_c| {len(Uc)}"))
                if j >= need and it >= need:
                    st.inc("SATK_checks")
                    shift = (0, 0) if MUT == "shift" else kap(t, p)
                    if kap(t, q) not in {kadd(s, shift) for s in Sset[(q, p)]}: st.bad("SATK", f"{name}@{t}: q {q} p {p}")
                    st.inc("SATKbr_y_is_p" if nxt[q] == p else "SATKbr_free")
                    st.inc(f"SATK_at_depth_{depth.get((t, q), 1)}")
    # DEPTH / outer count at index thresholds
    cls = [c for c in C if Qcs[c]]
    if any(c not in Dc for c in cls): return
    def depth_check(thr, tag):
        src = [k for jj, k in enumerate(fb, start=1) if jj >= thr]
        if not src: return
        st.inc(f"{tag}_checks")
        allq = sorted(q for c in cls for q in Qcs[c])
        Qr = runs_of(Q)
        tuples = set(tuple(kap(k, q) for q in sorted(Q)) for k in src)
        if len(tuples) != len(set(Qr[k] for k in src)): st.bad(tag, f"{name}: tuples vs Q-runs")
        Vq = {q: len(set(kap(k, q) for k in src)) for q in allq}
        if len(tuples) > 1 + sum(Vq[q] - 1 for q in allq): st.bad(tag, f"{name}: outer count")
        for c in cls:
            Qc = Qcs[c]
            for q in Qc:
                Vh = {}
                for k in src:
                    d = depth.get((k, q), 0)
                    Vh.setdefault(d, set()).add(kap(k, q))
                if 0 in Vh and len(Vh[0]) > len(A[q]): st.bad(tag, f"{name}: V_q0 > |A_q|")
                for h in Vh:
                    if h == 0: continue
                    rhs = sum(Dc[c] * len(set(kap(k, p) for k in src if depth.get((k, p), 0) == h - 1)) for p in Qc if p != q)
                    if len(Vh[h]) > rhs: st.bad(tag, f"{name}: V_qh recursion h {h}")
                st.mxr(f"{tag}_max_V_q", (len(set(kap(k, q) for k in src)), name))
    depth_check(n, "FBKT")
    W = max(len(U[c]) - 1 for c in cls) if cls else 0
    depth_check(W + 1, "FBKW")

def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    check_run(gp, states, fbs, st, name)

def gadget(base, kind, P):
    """k3: a chain class: cycle c <-> x; q1 -> {h1, c}; q2 -> {y2, c}, Even y2 -> {q1, h2}; q3 -> {y3, c}, Even y3 -> {q2, h3};
    h's forced to c with odd priorities above c, more negative further down so Even routes y2 -> q1, y3 -> q2 (depth 2 for q3)."""
    if kind != "k3": return TT.gadget(base, kind, P)
    prio, owner, succ = list(base.prio), list(base.owner), [list(s) for s in base.succ]
    n = base.n; c, x, q1, h1, q2, y2, h2, q3, y3, h3 = range(n, n + 10)
    o = P + 1 if P % 2 == 0 else P + 2
    prio += [P, 0, 1, o, 3, 2, o + 2, 5, 4, o + 4]
    owner += [1, 1, 1, 1, 1, 0, 1, 1, 0, 1]
    succ += [[x], [c], [h1, c], [c], [y2, c], [q1, h2], [c], [y3, c], [q2, h3], [c]]
    return pg.Game(prio, owner, succ)

def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 2; rng = random.Random(1616)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = TT.starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "union":
        kind = a[2]; runs = int(a[3]) if len(a) > 3 else 2; rng = random.Random(1617)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            base = pg.read(os.path.join(DC.ROOT, path))
            for P in (max(base.prio) + 1, max(base.prio) + 2):
                gp = gadget(base, kind, P)
                for r in range(runs):
                    s, t = TT.starts(gp, r, rng); run_game(gp, s, t, st, f"{path}+{kind}P{P}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); rng = random.Random(seed)
        for i in range(N):
            gp = DC.rand_game(rng, rng.randint(nmin, nmax), "kO")
            s, t = TT.starts(gp, 1, rng); run_game(gp, s, t, st, f"random{seed}:{i}")
    print("MODE", " ".join(a), "MUT", MUT or "-", "UCAP", UCAP)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")

if __name__ == "__main__":
    main()
