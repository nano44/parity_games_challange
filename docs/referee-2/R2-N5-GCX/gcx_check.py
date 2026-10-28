#!/usr/bin/env python3
r"""REFEREE-2 successor 18 (Opus 5.5, D15): N5-side checks of P-N5-GCX-box21 (sha1 5a91bebb) §1-§3. State loop = my lane's SPEC loop
(R2-N5-DUAL/dual_check.Runner on si.py); Xi, W = my own play values (R2-N5-RUND/rund_check.state_info, ENGXI). Lane tools (gcx.py etc.) NOT run.
Runs S: maximal fallback-free runs inside one (lambda_Xi, tau)-phase, cut into maximal sub-runs with lambda_W constant ((ii)).
Per class c (U_c = lambda_Xi^{-1}(c)) and state t: play = (sigma_t, tau)-play; fd(z) = first D_t-vertex on it; A_t, R_u(t), DD_t, Delta_t(u).
Checks:
  MIG   Lemma MIG-SPLIT at every X-migration: u' := fd_t(z) != u; (L) u' not in D_{t+1} or (S) an Even w on pi switches; in (S) z's play changes;
        and u' in U_c (implicit in the Consequence)
  MIGC  the Consequence: X_u(S) <= #(transitions with a vertex of D cap U_c leaving D) + #(transitions with some z in U_c changing its play)
  ULG   premise UL_G (COUNTED as data, not a violation): U event in a global C-interval [a, b] at k' with k' - a >= n - 1
  ULa   UL-RED (a) on runs where UL_G holds: |U(S)| <= n_E((n-1)(K+1)+K)  (also counted on runs where UL_G fails)
  CHU   RESULTS R67 (f) CHARGE-U at L = -1 (landed premise): COARSE_{-1}(W(x)) changes <= (n-1)(1+|U(S)|) for every x
  ULb   UL-RED (b) on runs where UL_G holds
  INT   global C-intervals are disjoint runs of good transitions; their number <= K + 1
Usage: gcx_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats


def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); g, n = gp, gp.n
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    key = [(I[k]["lamX"], tuple(b[v] for v in range(n) if g.owner[v] == 1)) for k, (_, b) in enumerate(states)]
    k0 = 0
    while k0 < len(states) - 1:
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0] and not fbs[k1] and I[k1 + 1]["lamW"] == I[k0]["lamW"]: k1 += 1
        if k1 > k0: check_run(ctx, g, I, k0, k1, st, name)
        k0 = k1 + 1 if k1 > k0 else k0 + 1


def first_D(wn, D, v):
    path, _ = R.lasso(wn, v)
    for i, x in enumerate(path):
        if x in D: return x, path[:i]
    return None, path


def check_run(ctx, g, I, a, b, st, name):
    n, E = ctx.n, ctx.E
    st.inc("S_runs"); st.inc("S_transitions", b - a)
    lam = I[a]["lamX"]; tu = I[a]["tu"]
    C = sorted(set(lam))
    nE = sum(1 for v in range(n) if g.owner[v] == 0)
    info = {}
    for c in C:
        U = frozenset(v for v in range(n) if lam[v] == c)
        rows = []
        for k in range(a, b + 1):
            D, wn, hn = I[k]["D"], I[k]["wn"], I[k]["hn"]
            fd = {z: first_D(wn, D, z) for z in U}
            A = frozenset(z for z in U if fd[z][0] is None)
            DU = frozenset(u for u in D if u in U)
            Ru = {u: frozenset(z for z in U if fd[z][0] == u) for u in DU}
            DD = frozenset(u for u in DU if hn[u] in A and tu[u] in A)
            M = lambda z: E.weight(I[k]["xi"][z][1])
            Dl = {u: M(tu[u]) - M(hn[u]) for u in DD}
            rows.append(dict(fd=fd, A=A, DU=DU, Ru=Ru, DD=DD, Dl=Dl))
        info[c] = (U, rows)
        # MIG-SPLIT
        Xu = {}; leave = 0; pchg = 0
        for k in range(a, b):
            r0, r1 = rows[k - a], rows[k + 1 - a]
            if r0["DU"] - I[k + 1]["D"]: leave += 1
            if any(R.lasso(I[k]["wn"], z) != R.lasso(I[k + 1]["wn"], z) for z in U): pchg += 1
            for u in r0["DD"] & r1["DD"]:
                migs = r1["Ru"][u] - r0["Ru"][u] - r0["A"]
                if migs: Xu[u] = Xu.get(u, 0) + 1
                for z in migs:
                    st.inc("MIG_checks")
                    up, pi = r0["fd"][z]
                    if up == u: st.bad("MIG", f"{name}@{k} c={c} z={z}: u' = u")
                    if up not in U: st.bad("MIG", f"{name}@{k} c={c} z={z}: u'={up} not in U_c")
                    L = up not in I[k + 1]["D"]
                    Sw = any(g.owner[w] == 0 and I[k]["sg"][w] != I[k + 1]["sg"][w] for w in pi)
                    if not (L or Sw): st.bad("MIG", f"{name}@{k} c={c} z={z}: neither (L) nor (S)")
                    if Sw and R.lasso(I[k]["wn"], z) == R.lasso(I[k + 1]["wn"], z): st.bad("MIG", f"{name}@{k} c={c} z={z}: (S) without play change")
                    st.inc("MIG_caseL" if L else "MIG_caseS_only")
                    if L and Sw: st.inc("MIG_both")
        for u, x in Xu.items():
            st.inc("MIGC_checks")
            if x > leave + pchg: st.bad("MIGC", f"{name} c={c} u={u}: X_u {x} > {leave} + {pchg}")
            st.mxr("max_Xu", (x, name, c, u, leave, pchg))
    # global C-intervals
    good = []
    for k in range(a, b):
        ok = I[k]["D"] == I[k + 1]["D"]
        for c in C:
            r0, r1 = info[c][1][k - a], info[c][1][k + 1 - a]
            if not (r1["A"] <= r0["A"]) or r0["DD"] != r1["DD"] or r0["Dl"] != r1["Dl"]: ok = False
        good.append(ok)
    K = sum(1 for x in good if not x)
    intervals = []; i = 0
    while i < len(good):
        if good[i]:
            j = i
            while j + 1 < len(good) and good[j + 1]: j += 1
            intervals.append((a + i, a + j + 1)); i = j + 1
        else: i += 1
    if len(intervals) > K + 1: st.bad("INT", f"{name}: {len(intervals)} intervals > K + 1 = {K + 1}")
    st.inc("C_intervals", len(intervals)); st.inc("C_cuts", K)
    # U events at level -1
    Uev = []
    for k in range(a, b):
        for y in range(n):
            if g.owner[y] != 0: continue
            z = I[k + 1]["sg"][y]
            if z == I[k]["sg"][y]: continue
            if any(R.forbidden(ctx, I[j], -1, y, z) for j in range(max(a, k - n + 1), k)): Uev.append((k, y, z))
    st.inc("U_events", len(Uev))
    ulg = True
    for (k, y, z) in Uev:
        for (ia, ib) in intervals:
            if ia <= k < ib:
                st.inc("U_in_interval"); st.mxr("max_U_index_in_interval", (k - ia, name, ia, ib, k, y, z, n))
                if k - ia >= n - 1: ulg = False; st.inc("ULG_FAIL"); print("ULG_FAIL", name, ia, ib, k, y, z, flush=True)
    bound_a = nE * ((n - 1) * (K + 1) + K)
    st.inc("ULa_checks")
    if len(Uev) > bound_a:
        if ulg: st.bad("ULa", f"{name}: |U| {len(Uev)} > {bound_a}")
        else: st.inc("ULa_fail_where_ULG_fails")
    st.mxr("max_U_over_bound_a", (round(len(Uev) / max(1, bound_a), 4), name, len(Uev), bound_a, K))
    for x in range(n):
        ch = sum(1 for k in range(a, b) if ctx.ck(I[k]["w"][x], -1) != ctx.ck(I[k + 1]["w"][x], -1))
        st.inc("CHU_checks")
        if ch > (n - 1) * (1 + len(Uev)): st.bad("CHU", f"{name} x={x}: {ch}")
        if ulg and ch > (n - 1) * (1 + bound_a): st.bad("ULb", f"{name} x={x}: {ch}")
        st.mxr("max_coarseW_changes", (ch, name, x, len(Uev)))


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; srng = random.Random(2121)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, srng); run_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        srng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
        for i in range(N):
            nn = srng.randint(nmin, nmax)
            gp = DC.rand_game(srng, nn, "kO") if k == 0 else H3.rand_kO(srng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, srng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2: s, t = R.read_start(gp, a[2])
        else: s, t = R.starts(gp, 0, None)
        run_game(gp, s, t, st, os.path.basename(a[1]))
    print("MODE", " ".join(a))
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
