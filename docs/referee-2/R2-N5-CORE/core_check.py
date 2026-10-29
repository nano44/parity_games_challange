#!/usr/bin/env python3
r"""REFEREE-2 successor 19 (Opus 5.5, D15): mechanical check of P-N5-CORE (docs/si/P-N5-CORE-box23.md, sha1 7b66f1ba @ l-si 081ae740).
State loop = my lane's SPEC loop (R2-N5-DUAL/dual_check.Runner on si.py = SPEC S1's own implementation, imported read-only, as every
REFEREE-2 checker since succ. 13); Xi = my own play value of (sigma, sigmabar) (R2-N5-RUND/rund_check.state_info, ENGXI cross-check).
The lane's experiments/si/root/corecheck.py is NOT run or imported. Every quantity is written here from the packet's definitions.
Phase = maximal run with (lambda_Xi, tau) constant (RESULTS R38 (a)). kappa_t(z) = (signed weight of P(Xi_t z), s_c * len), s_c = +1 iff
Omega(c) odd; kwt_c(v) = (sgn(v) 2^rank(v) if rank(v) > rank(c) else 0, s_c); Q = Odd vertices of out-degree >= 2.
Checks (each must be 0):
  C1    every in-phase transition changes sigma
  C2    |P| <= sum_w SW_P(w) per phase
  C3    w Even, sigma(w) changes, w off honest cycles at t and t+1 => Xi_{t+1}(w) > Xi_t(w); proof steps C3a (y in I_sigma_t),
        C3b (Xi_{t+1}(y) >= Xi_t(y)), C3c (both plays avoid w), C3d (both cycle nodes = lambda(w)); MONO (Xi_{t+1} >= Xi_t everywhere)
  C3cons  (C3)'s Consequence: |P| <= sum_{Even w} XR_P(w) + #(w, t) Even switches on an honest cycle at t or t+1
  C4    u in Q cap U_c, u != c, off honest cycles at t, t+1, sigmabar(u) y1 -> y2, CLEAN (y2 in Y^u_t, y1 in Y^u_{t+1}):
        kappa_{t+1}(y1) >= kappa_t(y1), strict unless kappa_{t+1}(y1) = kappa_{t+1}(y2); premises AK, YF (kappa-Y-FORM_D) at t and t+1;
        chain steps C4a..C4c; C4X: Xi_{t+1}(y1) > Xi_t(y1) when kappa strictly rises (M1kappa)
  C5    every interval I (whole phase; every sub-interval if the phase has <= ALLSUB transitions, else SUBN random ones):
        |I| <= m_E + NOFRESH(I); C5p: non-fresh transitions = every switching Even vertex returns to an edge held before in I
  C6    on global C-intervals (maximal runs of GOOD transitions, transition-local reading F2) inside a phase (C6) and inside each
        fallback-free lambda_W-constant sub-run S (C6S): the three counts <= m_E, <= sum_{Odd u}(deg u - 1), <= sum_c |A_a(U_c)| <= n
Controls (counted; expected to bite somewhere; NOT violations):
  X1    sigma unchanged at transitions that leave the phase (tau changes);  X3y  Xi_{t+1}(y) > Xi_t(y) fails (y = new successor);
  X3cyc C3's conclusion fails at switches of w ON an honest cycle at t or t+1;  X4u  C4's conclusion fails at UNCLEAN changes;
  X4h1/X4h2 fails with only half of CLEAN (y2 in Y_t only / y1 in Y_{t+1} only);  X4tie  clean change with kappa_{t+1}(y1) = kappa_t(y1)
  (the tie clause used);  X4strict  conclusion with the tie exception dropped fails;  X5nE  fresh transitions > n_E (bound m_E -> n_E);
  X5loc fresh-vs-previous-state count > m_E;  X6A  A-shrink transitions over the whole phase (not on good transitions only) > sum |A_a|;
  X6Ax  A_{t+1} not subset of A_t over the phase.
RULE=n5 (default) or RULE=rand (robustness: Even switches a random non-empty subset of I_sigma, random improving successor, tau fixed;
then C3/C4/C5 only, phases = runs with lambda_Xi constant).
Usage: core_check.py files list.txt [runs] | pairs list.txt prefix | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats
RULE = os.environ.get("RULE", "n5")
ALLSUB = int(os.environ.get("ALLSUB", "60"))
SUBN = int(os.environ.get("SUBN", "200"))
RANDCAP = int(os.environ.get("RANDCAP", "400"))


def tadd(a, b): return (a[0] + b[0], a[1] + b[1])


def oncyc(hn, v):
    path, x = R.lasso(hn, v)
    return v in path[path.index(x):]


def avoids(hn, start, w):
    path, _ = R.lasso(hn, start)
    return w not in path


def rand_run(gp, sg, tu, rng):
    E = DC.Engine(gp); g, n = gp, gp.n
    states, fbs = [(tuple(sg), tuple(tu))], []
    sg = list(sg)
    while len(fbs) < RANDCAP:
        vs, _ = E.evaluate(tuple(sg[v] if g.owner[v] == 0 else -1 for v in range(n)))
        Is = E.improving(tuple(sg), vs)
        if not Is: break
        byv = {}
        for v, w in Is: byv.setdefault(v, []).append(w)
        vv = sorted(byv); k = rng.randint(1, len(vv))
        for v in rng.sample(vv, k): sg[v] = rng.choice(byv[v])
        states.append((tuple(sg), tuple(tu))); fbs.append(0)
    return states, fbs


def run_game(gp, s, t, st, name, rng):
    states, fbs = DC.Runner(gp).run(s, t) if RULE == "n5" else rand_run(gp, s, t, rng)
    ctx = R.Ctx(gp); g, n = gp, gp.n
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    key = [(I[k]["lamX"], I[k]["tu"]) for k in range(len(I))]
    for k in range(len(I) - 1):
        if key[k] != key[k + 1]:
            st.inc("X_cross_transitions")
            if I[k]["sg"] == I[k + 1]["sg"]: st.inc("X1")
            check_C3(ctx, g, I, k, st, name, cross=True)
    k0 = 0
    while k0 < len(I):
        k1 = k0
        while k1 + 1 < len(I) and key[k1 + 1] == key[k0]: k1 += 1
        if k1 > k0: check_phase(ctx, g, I, fbs, k0, k1, st, name, rng)
        k0 = k1 + 1


def check_C3(ctx, g, I, k, st, name, cross=False):
    E, n = ctx.E, ctx.n
    s0, s1 = I[k], I[k + 1]
    K = ctx.key
    pre = "XC3_" if cross else ""
    if not cross:
        st.inc("MONO_checks")
        if any(K(s1["xi"][v]) < K(s0["xi"][v]) for v in range(n)): st.bad("MONO", f"{name}@{k}")
    for w in range(n):
        if g.owner[w] != 0 or s0["sg"][w] == s1["sg"][w]: continue
        y, x0 = s1["sg"][w], s0["sg"][w]
        rise = K(s1["xi"][w]) > K(s0["xi"][w])
        off = not oncyc(s0["hn"], w) and not oncyc(s1["hn"], w)
        if cross:
            st.inc(pre + "checks" + ("" if off else "_oncyc"))
            if not rise: st.inc(pre + "fail" + ("" if off else "_oncyc"))
            continue
        if not K(s1["xi"][y]) > K(s0["xi"][y]): st.inc("X3y")
        st.inc("X3y_checks")
        if not off:
            st.inc("C3_oncyc_switches")
            if not rise: st.inc("X3cyc")
            continue
        st.inc("C3_checks")
        if not rise: st.bad("C3", f"{name}@{k} w={w}")
        if (w, y) not in s0["Is"]: st.bad("C3a", f"{name}@{k} w={w}")
        if not K(s1["xi"][y]) >= K(s0["xi"][y]): st.bad("C3b", f"{name}@{k} w={w}")
        if not (avoids(s1["hn"], y, w) and avoids(s0["hn"], x0, w)): st.bad("C3c", f"{name}@{k} w={w}")
        c = s0["lamX"][w]
        if not (s1["lamX"][y] == c and s0["lamX"][x0] == c and s1["lamX"][w] == c): st.bad("C3d", f"{name}@{k} w={w}")
        if K(s0["xi"][y]) <= K(s0["xi"][x0]): st.bad("C3a2", f"{name}@{k} w={w}")


def check_phase(ctx, g, I, fbs, a, b, st, name, rng):
    n, E = ctx.n, ctx.E
    st.inc("phases"); st.inc("transitions", b - a)
    if RULE == "n5": st.inc("fallback_transitions", sum(1 for k in range(a, b) if fbs[k]))
    lam = I[a]["lamX"]
    Qall = frozenset(v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)
    evens = [v for v in range(n) if g.owner[v] == 0]
    mE = sum(len(set(g.succ[v])) for v in evens); nE = len(evens)
    # C1, C2, C3
    SW = {}
    for k in range(a, b):
        st.inc("C1_checks")
        if I[k]["sg"] == I[k + 1]["sg"]: st.bad("C1", f"{name}@{k}")
        for w in evens:
            if I[k]["sg"][w] != I[k + 1]["sg"][w]: SW[w] = SW.get(w, 0) + 1
        check_C3(ctx, g, I, k, st, name)
    XR = sum(1 for k in range(a, b) for w in evens if ctx.key(I[k]["xi"][w]) != ctx.key(I[k + 1]["xi"][w]))
    CY = sum(1 for k in range(a, b) for w in evens if I[k]["sg"][w] != I[k + 1]["sg"][w] and (oncyc(I[k]["hn"], w) or oncyc(I[k + 1]["hn"], w)))
    st.inc("C3cons_checks")
    if b - a > XR + CY: st.bad("C3cons", f"{name}[{a},{b}]")
    st.inc("C2_checks")
    if b - a > sum(SW.values()): st.bad("C2", f"{name}[{a},{b}]")
    if b - a == sum(SW.values()): st.inc("C2_tight")
    st.mxr("max_SW_over_P", (round(sum(SW.values()) / (b - a), 3), name, a, b))
    # C4
    classes = sorted(set(lam))
    for c in classes:
        U = frozenset(v for v in range(n) if lam[v] == c)
        sc = 1 if E.par[c] == 1 else -1
        kw = {v: ((E.weight(E.bit[v]) if E.rank[v] > E.rank[c] else 0), sc) for v in U}
        QU = [q for q in sorted(Qall) if q in U and q != c]
        kap = []
        for k in range(a, b + 1):
            xi = I[k]["xi"]
            kap.append({z: (E.weight(xi[z][1]), sc * xi[z][2]) for z in U})
        def Y(k, u):
            hn = I[k]["hn"]
            return frozenset(y for y in set(g.succ[u]) if y in U and avoids(hn, y, u))
        for k in range(a, b + 1):
            hn = I[k]["hn"]; kp = kap[k - a]
            st.inc("AK_checks")
            if kp[c] != (0, 0): st.bad("A0", f"{name}@{k} c={c}")
            for z in U:
                if z != c and (hn[z] not in U or kp[z] != tadd(kw[z], kp[hn[z]])): st.bad("AK", f"{name}@{k} c={c} z={z}")
            for q in QU:
                if oncyc(hn, q): continue
                Yq = Y(k, q); st.inc("YF_checks")
                if not Yq or kp[q] != tadd(kw[q], min(kp[y] for y in Yq)): st.bad("YF", f"{name}@{k} c={c} q={q}")
        for k in range(a, b):
            h0, h1 = I[k]["hn"], I[k + 1]["hn"]
            k0, k1 = kap[k - a], kap[k + 1 - a]
            for u in QU:
                if h0[u] == h1[u] or oncyc(h0, u) or oncyc(h1, u): continue
                y1, y2 = h0[u], h1[u]
                Y0, Y1 = Y(k, u), Y(k + 1, u)
                conc = k1[y1] >= k0[y1] and (k1[y1] > k0[y1] or k1[y1] == k1[y2])
                h1ok, h2ok = y2 in Y0, y1 in Y1
                st.inc("C4_changes")
                if not (h1ok and h2ok):
                    st.inc("C4_unclean")
                    if not conc: st.inc("X4u")
                    if h1ok and not conc: st.inc("X4h1")
                    if h2ok and not conc: st.inc("X4h2")
                    if h1ok: st.inc("C4_half1_only")
                    if h2ok: st.inc("C4_half2_only")
                    continue
                st.inc("C4_checks")
                if not conc: st.bad("C4", f"{name}@{k} c={c} u={u} y1={y1} y2={y2}")
                if not k0[y1] <= k0[y2]: st.bad("C4a", f"{name}@{k} u={u}")
                if not k0[y2] <= k1[y2]: st.bad("C4b", f"{name}@{k} u={u}")
                if not k1[y2] <= k1[y1]: st.bad("C4c", f"{name}@{k} u={u}")
                if k1[y1] == k0[y1]: st.inc("X4tie"); print("X4TIE", name, k, "c", c, "u", u, "y1", y1, "y2", y2, k0[y1], k1[y1], k0[y2], k1[y2], flush=True)
                if k1[y1] == k1[y2]: st.inc("C4_tie_at_t1")
                if not k1[y1] > k0[y1]: st.inc("X4strict")
                else:
                    st.inc("C4_strict")
                    if not ctx.key(I[k + 1]["xi"][y1]) > ctx.key(I[k]["xi"][y1]): st.bad("C4X", f"{name}@{k} u={u}")
    # C5
    L = b - a
    if L <= ALLSUB: ivs = [(i, j) for i in range(a, b) for j in range(i + 1, b + 1)]
    else: ivs = [(a, b)] + [tuple(sorted(rng.sample(range(a, b + 1), 2))) for _ in range(SUBN)]
    for (i, j) in ivs:
        held = {w: {I[i]["sg"][w]} for w in evens}
        fresh = nof = loc = 0
        for k in range(i, j):
            sw = [w for w in evens if I[k]["sg"][w] != I[k + 1]["sg"][w]]
            fr = any(I[k + 1]["sg"][w] not in held[w] for w in sw)
            if fr: fresh += 1
            else:
                nof += 1
                if not sw or not all(I[k + 1]["sg"][w] in held[w] for w in sw): st.bad("C5p", f"{name}@{k}")
            if sw: loc += 1
            for w in sw: held[w].add(I[k + 1]["sg"][w])
        st.inc("C5_checks")
        if j - i > mE + nof: st.bad("C5", f"{name}[{i},{j}]")
        if fresh > nE: st.inc("X5nE")
        if loc > mE: st.inc("X5loc")
        st.mxr("max_fresh_over_mE", (round(fresh / mE, 3), name, i, j))
        st.mxr("max_NOFRESH", (nof, name, i, j))
    if RULE != "n5": return
    # C6: per state, D, A per class, DD, Delta (as R2-N5-GCX/gcx_check.py)
    rows = []
    oddu = [u for u in range(n) if g.owner[u] == 1]
    bound2 = sum(len(set(g.succ[u])) - 1 for u in oddu)
    for k in range(a, b + 1):
        D, wn, hn, xi = I[k]["D"], I[k]["wn"], I[k]["hn"], I[k]["xi"]
        tu = I[k]["tu"]
        r = {}
        for c in classes:
            U = [v for v in range(n) if lam[v] == c]
            fd = {}
            for z in U:
                path, _ = R.lasso(wn, z)
                fd[z] = next((x for x in path if x in D), None)
            A = frozenset(z for z in U if fd[z] is None)
            DU = [u for u in D if u in U]
            DD = frozenset(u for u in DU if hn[u] in A and tu[u] in A)
            Dl = {u: E.weight(xi[tu[u]][1]) - E.weight(xi[hn[u]][1]) for u in DD}
            r[c] = (A, DD, Dl)
        rows.append(r)
    good = []
    for k in range(a, b):
        r0, r1 = rows[k - a], rows[k + 1 - a]
        ok = I[k]["D"] == I[k + 1]["D"]
        for c in classes:
            if not (r1[c][0] <= r0[c][0]) or r0[c][1] != r1[c][1] or r0[c][2] != r1[c][2]: ok = False
        good.append(ok)
    def runs_of(mask, lo):
        out, i = [], 0
        while i < len(mask):
            if mask[i]:
                j = i
                while j + 1 < len(mask) and mask[j + 1]: j += 1
                out.append((lo + i, lo + j + 1)); i = j + 1
            else: i += 1
        return out
    def c6(ia, ib, tag):
        heldE = {w: {I[ia]["sg"][w]} for w in evens}
        heldO = {u: {I[ia]["hn"][u]} for u in oddu}
        e1 = e2 = e3 = 0
        for k in range(ia, ib):
            s0, s1 = I[k], I[k + 1]
            if any(s1["sg"][w] not in heldE[w] for w in evens if s0["sg"][w] != s1["sg"][w]): e1 += 1
            if any(s1["hn"][u] not in heldO[u] for u in oddu if s0["hn"][u] != s1["hn"][u]): e2 += 1
            if any(rows[k + 1 - a][c][0] < rows[k - a][c][0] for c in classes): e3 += 1
            for w in evens: heldE[w].add(s1["sg"][w])
            for u in oddu: heldO[u].add(s1["hn"][u])
        b3 = sum(len(rows[ia - a][c][0]) for c in classes)
        st.inc(tag + "_intervals")
        if e1 > mE: st.bad(tag + "a", f"{name}[{ia},{ib}] {e1} > {mE}")
        if e2 > bound2: st.bad(tag + "b", f"{name}[{ia},{ib}] {e2} > {bound2}")
        if e3 > b3 or b3 > n: st.bad(tag + "c", f"{name}[{ia},{ib}] {e3} > {b3}")
        for nm, v in (("fresh", e1), ("oddopt", e2), ("Ashrink", e3)):
            if v: st.inc(f"{tag}_nonzero_{nm}")
        st.mxr(tag + "_max_Ashrink", (e3, b3, name, ia, ib))
        st.mxr(tag + "_max_oddopt", (e2, bound2, name, ia, ib))
        st.mxr(tag + "_max_len", (ib - ia, name, ia, ib))
    for (ia, ib) in runs_of(good, a): c6(ia, ib, "C6")
    # inside fallback-free lambda_W-constant sub-runs S
    k = a
    while k < b:
        j = k
        while j < b and not fbs[j] and I[j + 1]["lamW"] == I[k]["lamW"]: j += 1
        if j > k:
            for (ia, ib) in runs_of(good[k - a:j - a], k): c6(ia, ib, "C6S")
        k = j + 1 if j > k else k + 1
    # controls on the whole phase
    sh = sum(1 for k in range(a, b) if any(rows[k + 1 - a][c][0] < rows[k - a][c][0] for c in classes))
    if sh > sum(len(rows[0][c][0]) for c in classes): st.inc("X6A")
    if any(not (rows[k + 1 - a][c][0] <= rows[k - a][c][0]) for k in range(a, b) for c in classes): st.inc("X6Ax")
    st.inc("C6_cuts", sum(1 for x in good if not x))


def starts(gp, r, rng):
    return R.starts(gp, r, rng)


def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(2319)
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"{path}#{r}", rng)
    elif a[0] == "pairs":   # each line: pg [start], relative to a[2]; the given start if present, else S3
        for line in [l.split() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(a[2], line[0]))
            if len(line) > 1: s, t = R.read_start(gp, os.path.join(a[2], line[1]))
            else: s, t = starts(gp, 0, None)
            run_game(gp, s, t, st, line[0] + ("#start" if len(line) > 1 else "#S3"), rng)
    elif a[0] == "random":
        N, nmin, nmax, seed = map(int, a[1:5]); k = int(a[5]) if len(a) > 5 else 2; ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H.rand_kO(rng, nn, k)
            for r in range(0, ns):
                s, t = starts(gp, r, rng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}", rng)
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2: s, t = R.read_start(gp, a[2]); nm = os.path.basename(a[1]) + "#start"
        else: s, t = starts(gp, 0, None); nm = os.path.basename(a[1]) + "#S3"
        run_game(gp, s, t, st, nm, rng)
    print("MODE", " ".join(a), "RULE", RULE)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:50]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
