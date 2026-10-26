#!/usr/bin/env python3
r"""REFEREE-2 successor 16 (Opus 5.5, D15): mechanical check of packet P-N5-HONFF (docs/new/P-N5-HONFF-box47.md sha1 98101d1f @ 4a0a8aba).
Built on my R2-N5-HON/hon_check.py (state sequence = succ. 13's SPEC loop; Xi, W = my own play values). Lane tools
(experiments/new/box47/*.py) NOT run or imported.
LEV(k), LEV_odd(k) EXACT by enumeration of all simple paths of G_tau to cycle nodes of lambda, with a path BUDGET per phase (over budget:
the phase is UNK and skipped for the LEV checks; counted).
Checks:
  FBa    FB-RISE (a): at every in-phase S4c fallback t -> t+1: LEV(t + 1) >= min(LEV(t) + 1, LEV_odd(t), n - 1)
  FBb    FB-RISE (b): for every W-honest h <= t in the phase: LEV(t + 1) >= min(LEV(h) + 1, n - 1); also the proof's step
         LEV_odd(t) >= LEV(h) + 1 (FBb_odd)
  QA     Q-A, pointwise: at every state t, Even x, z in succ(x) with Xi_t(z) <= Xi_t(sigma_t x), and every simple path r = x z r' to a cycle
         node with Xi_t(z) >= value(r'): value(r) <= Xi_t(x)  (Lemma P's Case A with Omega := Xi_t)
  HFF    Theorem HON-FF: W-honest states per phase <= 4n^2 - 3n; and every gap between consecutive unsaturated W-honest states rises (the
         proof's claim, gaps WITH a fallback included)
  H0FF   HON-0-FF (a)-(c) <= 4n^2 - 3n; REC-0's bound - (4n^2 - 3n) = f(n + 1) + 2
  R1FF   REC-1-FF (a): {u}-intervals <= 1 + 4n^2 - 3n + X_dir + X_big
Controls HF_MUT: ctrl (FB-RISE without the LEV_odd term: must fail where the Odd term binds), b2 ((b) with LEV(h) + 2).
Usage: honff_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-HON"))
import hon_check as H
R, DC, pg, Engine, Stats = H.R, H.DC, H.pg, H.Engine, H.Stats
MUT = os.environ.get("HF_MUT", "")
BUDGET = int(os.environ.get("BUDGET", "400000"))


class Over(Exception): pass


def simple_values(ctx, tu, cyc, budget):
    g, n, E = ctx.g, ctx.n, ctx.E
    out, cnt = {}, [0]
    for x in range(n):
        res = []
        def dfs(y, vis, path):
            cnt[0] += 1
            if cnt[0] > budget: raise Over()
            if y in cyc:
                m = 0
                for p in path[:-1]:
                    if E.rank[p] > E.rank[y]: m |= E.bit[p]
                res.append((len(path) - 1, E.key((y, m, len(path) - 1)), tuple(path)))
            for z in ([tu[y]] if g.owner[y] == 1 else sorted(set(g.succ[y]))):
                if z not in vis:
                    vis.add(z); path.append(z); dfs(z, vis, path); path.pop(); vis.discard(z)
        dfs(x, {x}, [x])
        out[x] = res
    return out


def table(ctx, sv, xs):
    n = ctx.n
    B = {}
    for x in xs:
        best = {}
        for e, k, _ in sv[x]:
            if e not in best or k > best[e]: best[e] = k
        row, cur = [], None
        for j in range(n):
            if j in best and (cur is None or best[j] > cur): cur = best[j]
            row.append(cur)
        B[x] = row
    return B


def lev(ctx, B, vals, xs):
    n = ctx.n; L = -1
    for j in range(n):
        if all(B[x][j] is None or ctx.key(vals[x]) >= B[x][j] for x in xs): L = j
        else: break
    return L


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
        check_phase(ctx, g, I, fbs, k0, k1, Q, st, name)
        k0 = k1 + 1


def check_phase(ctx, g, I, fbs, a, b, Q, st, name):
    n, E = ctx.n, ctx.E
    st.inc("phases")
    tu = I[a]["tu"]; lam = I[a]["lamX"]
    cyc = frozenset(v for v in range(n) if lam[v] == v)
    hon = [k for k in range(a, b + 1) if I[k]["xi"] == I[k]["w"]]
    f = sum(1 for k in range(a, b) if fbs[k])
    N = len(hon)
    st.mxr("HFF_max_honest", (N, f"{name}@{a} n {n} f {f}"))
    if N > 4 * n * n - 3 * n: st.bad("HFF", f"{name}@{a}: {N}")
    # HON-0-FF, REC-1-FF (a) (reuse the HON structures)
    Dk = {k: frozenset(I[k]["D"]) for k in range(a, b + 1)}
    epochs, k = [], a
    while k <= b:
        e = k
        while e + 1 <= b and tuple(I[e + 1]["hn"][q] for q in Q) == tuple(I[k]["hn"][q] for q in Q): e += 1
        epochs.append((k, e)); k = e + 1
    d0 = sum(1 for k in range(a, b + 1) if not Dk[k]); N0 = sum(1 for p, q in epochs if not Dk[p])
    tr0 = sum(1 for (p, q) in epochs if not Dk[p] for k in range(p, q + 1) if k < b)
    for nm, val in (("a", d0), ("b", N0), ("c", tr0)):
        if val > 4 * n * n - 3 * n: st.bad("H0FF" + nm, f"{name}@{a}")
    if (f + 1) * (n + 1) + 4 * n * (n - 1) + 1 - (4 * n * n - 3 * n) != f * (n + 1) + 2: st.bad("H0FF_rec0", name)
    ints, k = [], a
    while k <= b:
        if len(Dk[k]) != 1: k += 1; continue
        e = k
        while e + 1 <= b and Dk[e + 1] == Dk[k]: e += 1
        ints.append((k, e)); k = e + 1
    xdir = sum(1 for k in range(a, b) if len(Dk[k]) == 1 and len(Dk[k + 1]) == 1 and Dk[k] != Dk[k + 1])
    xbig = sum(1 for k in range(a, b) if len(Dk[k]) >= 2 and len(Dk[k + 1]) == 1)
    if len(ints) > 1 + 4 * n * n - 3 * n + xdir + xbig: st.bad("R1FF", f"{name}@{a}")
    st.inc("R1FF_phases")
    # LEV-based checks
    fbk = [k for k in range(a, b) if fbs[k]]
    if not fbk and len(hon) < 2 and not os.environ.get("QA_ALL"): return
    try:
        sv = simple_values(ctx, tu, cyc, BUDGET)
    except Over:
        st.inc("UNK_phases"); return
    allx = list(range(n)); oddx = [x for x in allx if g.owner[x] == 1]
    B = table(ctx, sv, allx)
    LEV = {k: lev(ctx, B, I[k]["xi"], allx) for k in range(a, b + 1)}
    LO = {k: lev(ctx, B, I[k]["xi"], oddx) for k in range(a, b + 1)}
    st.inc("LEV_phases")
    for t in fbk:
        st.inc("FB_fallbacks")
        if t not in hon: st.inc("FB_at_nonhonest")
        if any(h < t for h in hon) and t not in hon: st.inc("FB_after_honest_nonhonest")
        j = min(LEV[t] + 1, LO[t], n - 1)
        if MUT == "ctrl": j = min(LEV[t] + 1, n - 1)
        if LO[t] <= LEV[t]: st.inc("FB_odd_binds")
        if LEV[t + 1] < j: st.bad("FBa", f"{name}@{t}: LEV {LEV[t]} -> {LEV[t + 1]}, LEV_odd {LO[t]}")
        for h in hon:
            if h > t: break
            st.inc("FBb_checks")
            L = LEV[h]
            need = min(L + (2 if MUT == "b2" else 1), n - 1)
            if LEV[t + 1] < need: st.bad("FBb", f"{name}@{t}: h {h} LEV(h) {L} LEV(t+1) {LEV[t + 1]}")
            if L <= n - 2 and LO[t] < L + 1: st.bad("FBb_odd", f"{name}@{t}: h {h} LEV_odd(t) {LO[t]} < {L + 1}")
    # every gap between consecutive unsaturated honest states rises
    for h1, h2 in zip(hon, hon[1:]):
        if LEV[h1] >= n - 1: continue
        st.inc("HFF_gaps")
        inside = any(fbs[k] for k in range(h1, h2))
        if inside: st.inc("HFF_gaps_with_fallback")
        if inside and not fbs[h1]: st.inc("HFF_gaps_inside_fallback")
        if LEV[h2] < LEV[h1] + 1: st.bad("HFF_gap", f"{name}@{h1}->{h2}: LEV {LEV[h1]} -> {LEV[h2]} (fallback inside: {inside})")
    # Q-A pointwise
    for t in range(a, b + 1):
        xi = I[t]["xi"]; sg = I[t]["sg"]
        for x in allx:
            if g.owner[x] != 0: continue
            kx = ctx.key(xi[x]); ka = ctx.key(xi[sg[x]])
            for e, kv, path in sv[x]:
                if e == 0: continue
                z = path[1]
                if ctx.key(xi[z]) > ka: continue
                rp = path[1:]
                u = rp[-1]; m = 0
                for p in rp[:-1]:
                    if E.rank[p] > E.rank[u]: m |= E.bit[p]
                if ctx.key(xi[z]) < E.key((u, m, len(rp) - 1)): continue
                st.inc("QA_checks")
                if kv > kx: st.bad("QA", f"{name}@{t}: x {x} path {path}")


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1620)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, rng); check_game(gp, s, t, st, f"{path}#{r}")
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        rng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
        for i in range(N):
            nn = rng.randint(nmin, nmax)
            gp = DC.rand_game(rng, nn, "kO") if k == 0 else H3.rand_kO(rng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, rng); check_game(gp, s, t, st, f"random{seed}:{i}#{r}")
    elif a[0] == "start":
        gp = pg.read(a[1])
        s, t = R.read_start(gp, a[2]) if len(a) > 2 else R.starts(gp, 0, None)
        check_game(gp, s, t, st, os.path.basename(a[1]))
    print("MODE", " ".join(a), "MUT", MUT or "-", "BUDGET", BUDGET)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
