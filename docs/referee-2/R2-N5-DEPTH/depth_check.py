#!/usr/bin/env python3
r"""REFEREE-2 successor 18 (Opus 5.5, D15): N5-side checks of P-N5-DEPTH-box22 (sha1 549c7fb7) §2-§3 and P-N5-DEPTH-add-box22
(sha1 4d51aa5e) §1-§3. State loop = my lane's SPEC loop (dual_check.Runner on si.py); Xi, W = my own play values (rund_check.state_info).
Lane tools (experiments/si/root/staticdepth.py, absdepth.py, evenside.py, exitx.py) NOT run or imported.
Runs S: maximal fallback-free runs inside one (lambda_Xi, tau)-phase with lambda_W constant ((H1)).
DEPTH:
  SD    STATIC-DEPTH on every [a, b] inside a maximal sigmabar-constant sub-run of S ((H2)) with (H3) on [a, b] and (H4) at b: per-vertex
        settling (both plays equal those at b on [a + d*(v), b]) and b - a <= max d*. GEN_W checked in its USED form (distinct W-plays of v
        at states of [a, b] have distinct W-valuations); intervals where it fails are counted apart (SD_noGEN) and still checked.
  PE    PURE-END at every state where every gate (D-vertex) is D-direct: (H4) holds and every W-cycle and honest cycle is common.
  GL    GCI-LEN-rhoF: global C-intervals (transition-local: every class A non-increasing, D, DD, Delta constant) with sigmabar constant,
        (H3), (H4) at b: b - a <= n - 1.
DEPTH-add:
  GP    GATE-PUSH on every per-class pure C-interval [a, b] (per class: A_c non-increasing, D cap U_c, DD_c, Delta constant; pure: every gate
        of U_c D-direct at every state): at t in [a + L, b) with a sigmabar change at a gate u from y1 to y2, y1 in A_{t+1}: M(y1) unchanged and
        kappa(y1) rises, or the tie kappa_{t+1}(y1) = kappa_{t+1}(y2). Count N_sb <= sum deg(u)(|U_c| - 2) + |A_a| + TIES (GPC).
  PL    PURE-LEN as stated: b - a <= L + (1 + N_sb + N_cyc)(|U_c| - 1) + N_sb + N_cyc  (COUNTED as PL_FAIL: expected to fail when another
        class keeps switching); PLR (repaired): the transitions of [a, b] with an Even switch in U_c obey the same bound.
  MR    MONO-REF at every in-phase transition, z in U \ {c}, m in T on z's (t+1)-play, m != z, with the no-cycle hypothesis: split by m at or
        before z's first visit of c (MR, must hold) and m after it (MR_after: COUNTED, the packet's proof does not cover it).
Usage: depth_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts] | union a.pg a.start"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats
SDCAP = int(os.environ.get("SDCAP", "60"))


def tsub(a, b): return (a[0] - b[0], a[1] - b[1])


def cycles(nx):
    seen, out = set(), set()
    for v in range(len(nx)):
        path, x = R.lasso(nx, v)
        cyc = path[path.index(x):]
        i = cyc.index(min(cyc)); out.add(tuple(cyc[i:] + cyc[:i]))
    return frozenset(out)


def run_game(gp, s, t, st, name):
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); g, n = gp, gp.n
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    for k in range(len(I)):
        I[k]["cW"] = cycles(I[k]["wn"]); I[k]["cH"] = cycles(I[k]["hn"])
        check_pure_end(ctx, g, I[k], st, f"{name}@{k}")
    key = [(I[k]["lamX"], tuple(b[v] for v in range(n) if g.owner[v] == 1)) for k, (_, b) in enumerate(states)]
    # MONO-REF on all in-phase transitions
    for k in range(len(I) - 1):
        if key[k] == key[k + 1]: check_monoref(ctx, g, I, k, st, name)
    k0 = 0
    while k0 < len(states) - 1:
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0] and not fbs[k1] and I[k1 + 1]["lamW"] == I[k0]["lamW"]: k1 += 1
        if k1 > k0: check_run(ctx, g, I, k0, k1, st, name)
        k0 = k1 + 1 if k1 > k0 else k0 + 1


def Hb(g, Ib, n):
    D = Ib["D"]; tu = Ib["tu"]; sg = Ib["sg"]; hn = Ib["hn"]
    cv = set(x for c in Ib["cW"] for x in c)
    E = {}
    for v in range(n):
        if v in cv: E[v] = []
        elif g.owner[v] == 0: E[v] = [sg[v]]
        elif v in D: E[v] = sorted(set([tu[v], hn[v]]))
        else: E[v] = [tu[v]]
    return E, cv


def dag_dstar(g, E, cv, n):
    """d* per the packet, or None if H_b has a cycle outside cycle vertices."""
    state, d = {}, {}
    def go(v):
        if v in d: return d[v]
        if state.get(v) == 1: raise ValueError
        state[v] = 1
        if v in cv: r = 0
        elif g.owner[v] == 0: r = 1 + go(E[v][0])
        else: r = max(go(y) for y in E[v])
        d[v] = r; state[v] = 2; return r
    try:
        for v in range(n): go(v)
    except (ValueError, RecursionError):
        return None
    return d


def check_pure_end(ctx, g, Ik, st, name):
    n = ctx.n; D = Ik["D"]
    if not D: return
    A = set(v for v in range(n) if Ik["u"].get(v) is None)
    if not all(Ik["hn"][u] in A and Ik["tu"][u] in A for u in D): return
    st.inc("PE_checks")
    E, cv = Hb(g, Ik, n)
    if dag_dstar(g, E, cv, n) is None: st.bad("PE", f"{name}: H_b cyclic")
    if Ik["cW"] != Ik["cH"]: st.bad("PE", f"{name}: cycles not common")


def plays_eq(I, t, b, v):
    return R.lasso(I[t]["wn"], v) == R.lasso(I[b]["wn"], v) and R.lasso(I[t]["hn"], v) == R.lasso(I[b]["hn"], v)


def check_static(ctx, g, I, a, b, st, name, tag="SD"):
    n = ctx.n
    E, cv = Hb(g, I[b], n)
    d = dag_dstar(g, E, cv, n)
    if d is None: return False
    st.inc(tag + "_checks")
    gen = True
    for v in range(n):
        seen = {}
        for t in range(a, b + 1):
            p = R.lasso(I[t]["wn"], v); w = I[t]["w"][v]
            if w in seen and seen[w] != p: gen = False
            seen[w] = p
    if not gen: st.inc(tag + "_noGEN")
    md = max(d.values())
    if b - a > md:
        if gen: st.bad(tag, f"{name} [{a},{b}]: length {b - a} > max d* {md}")
        else: st.inc(tag + "_FAIL_noGEN")
    for v in range(n):
        if v in cv: continue
        for t in range(a + d[v], b + 1):
            if not plays_eq(I, t, b, v):
                if gen: st.bad(tag, f"{name} [{a},{b}] v={v}: not settled at {t} (d*={d[v]})")
                else: st.inc(tag + "_FAIL_noGEN")
                break
    if b - a == md and md > 0: st.inc(tag + "_sharp")
    st.mxr(tag + "_max_len", (b - a, name, a, b, md, n, len(I[b]["D"])))
    if I[b]["D"]: st.inc(tag + "_with_gates")
    return True


def check_run(ctx, g, I, a, b, st, name):
    n, E = ctx.n, ctx.E
    st.inc("S_runs")
    check_eoneway(ctx, g, I, a, b, st, name)
    # STATIC-DEPTH: sigmabar-constant sub-runs
    sbar = [tuple(I[k]["hn"][v] for v in range(n) if g.owner[v] == 1) for k in range(a, b + 1)]
    i = a
    while i <= b:
        j = i
        while j + 1 <= b and sbar[j + 1 - a] == sbar[i - a]: j += 1
        for x in range(i, j + 1):
            for y in range(x + 1, min(j, x + SDCAP) + 1):
                # (H3) on [x, y]
                if all(I[t]["cW"] == I[t]["cH"] == I[x]["cW"] for t in range(x, y + 1)):
                    check_static(ctx, g, I, x, y, st, name)
        i = j + 1
    # classes
    lam = I[a]["lamX"]; tu = I[a]["tu"]; C = sorted(set(lam))
    rows = {}
    for c in C:
        U = frozenset(v for v in range(n) if lam[v] == c)
        sc = 1 if E.par[c] == 1 else -1
        rr = []
        for k in range(a, b + 1):
            D = I[k]["D"]
            A = frozenset(z for z in U if I[k]["u"].get(z) is None)
            DU = frozenset(u for u in D if u in U)
            DD = frozenset(u for u in DU if I[k]["hn"][u] in A and tu[u] in A)
            M = lambda z: E.weight(I[k]["xi"][z][1])
            kap = {z: (E.weight(I[k]["xi"][z][1]), sc * I[k]["xi"][z][2]) for z in U}
            Dl = {u: M(tu[u]) - M(I[k]["hn"][u]) for u in DD}
            Z = []; x = c
            while True:
                Z.append(x); x = I[k]["hn"][x]
                if x == c or len(Z) > n: break
            rr.append(dict(A=A, DU=DU, DD=DD, Dl=Dl, kap=kap, Z=tuple(Z)))
        rows[c] = (U, rr)
    # global C-intervals (GCI-LEN-rhoF)
    good = []
    for k in range(a, b):
        ok = I[k]["D"] == I[k + 1]["D"]
        for c in C:
            r0, r1 = rows[c][1][k - a], rows[c][1][k + 1 - a]
            if not (r1["A"] <= r0["A"]) or r0["DD"] != r1["DD"] or r0["Dl"] != r1["Dl"]: ok = False
        good.append(ok)
    for (x, y) in runs_of(good, a):
        st.inc("GCI_intervals")
        if any(sbar[t - a] != sbar[x - a] for t in range(x, y + 1)): st.inc("GCI_sbar_changes"); continue
        if not all(I[t]["cW"] == I[t]["cH"] == I[x]["cW"] for t in range(x, y + 1)): st.inc("GCI_noH3"); continue
        if check_static(ctx, g, I, x, y, st, name, tag="GL"):
            if y - x > n - 1: st.bad("GL", f"{name} [{x},{y}]")
    # per-class pure C-intervals: GATE-PUSH, PURE-LEN
    for c in C:
        U, rr = rows[c]
        goodc = []
        for k in range(a, b):
            r0, r1 = rr[k - a], rr[k + 1 - a]
            goodc.append(r1["A"] <= r0["A"] and r0["DU"] == r1["DU"] and r0["DD"] == r1["DD"] and r0["Dl"] == r1["Dl"])
        for (x, y) in runs_of(goodc, a):
            if not all(rr[t - a]["DD"] == rr[t - a]["DU"] for t in range(x, y + 1)): continue
            st.inc("PURE_intervals")
            if rr[x - a]["DU"]: st.inc("PURE_intervals_with_gates")
            L = max(len(rr[x - a]["A"]) - 1, 0)
            Nsb = 0; ties = 0; leave = 0; pushes = {}
            for t in range(x, y):
                ch = [u for u in rr[t - a]["DU"] if I[t]["hn"][u] != I[t + 1]["hn"][u]]
                if t >= x + L and ch: Nsb += 1
                for u in ch:
                    if t < x + L: continue
                    y1, y2 = I[t]["hn"][u], I[t + 1]["hn"][u]
                    k0, k1 = rr[t - a]["kap"], rr[t + 1 - a]["kap"]
                    if y1 in rr[t + 1 - a]["A"]:
                        st.inc("GP_checks")
                        if k1[y1] == k1[y2]: st.inc("GP_tie"); ties += 1
                        elif not (k1[y1][0] == k0[y1][0] and k1[y1] > k0[y1]): st.bad("GP", f"{name}@{t} c={c} u={u} y1={y1}")
                        else: pushes[(u, y1)] = pushes.get((u, y1), 0) + 1
                    else: leave += 1
            bound_sb = sum(len(set(g.succ[u])) for u in rr[x - a]["DU"]) * max(len(U) - 2, 0) + len(rr[x - a]["A"]) + ties
            if Nsb > bound_sb: st.bad("GPC", f"{name} c={c} [{x},{y}]: N_sb {Nsb} > {bound_sb}")
            if any(v > max(len(U) - 2, 0) for v in pushes.values()): st.bad("GPC", f"{name} c={c}: a (u, y1) pushed more than |U|-2 times")
            Ncyc = sum(1 for t in range(x, y) if rr[t - a]["Z"] != rr[t + 1 - a]["Z"])
            bound = L + (1 + Nsb + Ncyc) * (len(U) - 1) + Nsb + Ncyc
            evsw = sum(1 for t in range(x, y) if any(g.owner[v] == 0 and I[t]["sg"][v] != I[t + 1]["sg"][v] for v in U))
            gen = True
            for v in U:
                seen = {}
                for t in range(x, y + 1):
                    p = R.lasso(I[t]["wn"], v); w = I[t]["w"][v]
                    if w in seen and seen[w] != p: gen = False
                    seen[w] = p
            st.inc("PL_checks")
            if y - x > bound:
                st.inc("PL_FAIL"); st.mxr("PL_worst", (y - x - bound, name, c, x, y, len(U), bound, evsw))
                if os.environ.get("WHERE") and len(U) >= 3: print("PL_FAIL_AT", name, "c", c, "[", x, y, "] |U|", len(U), "gates", sorted(rr[x - a]["DU"]), "L", L, "N_sb", Nsb, "N_cyc", Ncyc, "bound", bound, "Even switches in U_c", evsw, flush=True)
            if evsw > bound:
                if gen: st.bad("PLR", f"{name} c={c} [{x},{y}]: Even switches in U_c {evsw} > {bound}")
                else: st.inc("PLR_FAIL_noGEN")


def check_eoneway(ctx, g, I, a, b, st, name):
    """E-ONEWAY on the in-phase transitions of [a, b]: Even w in U \\ {c} switches a0 -> b0 at t -> t+1; e1 = first T-vertex on a0's
    honest play at t, pi_a its path; for t' > t while pi_a, e1 unchanged on [t, t'] and e1 on w's honest play at every state of [t+1, t'] with
    the no-cycle hypothesis: w must not switch back to a0 at t' -> t'+1. Split by e1 after c on w's play at some state (EOW_after)."""
    n, E = ctx.n, ctx.E
    lam = I[a]["lamX"]
    Qall = set(v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)
    def tpath(k, x, c):
        path, rep = R.lasso(I[k]["hn"], x)
        for i, y in enumerate(path):
            if y == c or y in Qall: return tuple(path[:i + 1])
        return None
    def oncyc(k, c):
        s0, x = set(), c
        while True:
            s0.add(x); x = I[k]["hn"][x]
            if x == c: return s0
    for t in range(a, b):
        for w in range(n):
            if g.owner[w] != 0: continue
            a0, b0 = I[t]["sg"][w], I[t + 1]["sg"][w]
            if a0 == b0: continue
            c = lam[w]
            if w == c: continue
            pa = tpath(t, a0, c)
            if pa is None: continue
            e1 = pa[-1]; after = False; ok = True
            for tp in range(t + 1, b):
                if tpath(tp, a0, c) != pa: break
                path, rep = R.lasso(I[tp]["hn"], w)
                if e1 not in path: break
                j = path.index(e1); ic = path.index(c) if c in path else len(path)
                if j > ic: after = True
                cyc = oncyc(tp - 1, c) if tp - 1 >= t + 1 else oncyc(t, c)
                if any(x in Qall and x in cyc for x in path[:j]): break
                st.inc("EOW_checks" + ("_after" if after else ""))
                if I[tp + 1]["sg"][w] == a0:
                    if after: st.inc("EOW_after_FAIL"); print("EOW_after_FAIL", name, t, tp, w, a0, e1, flush=True) if os.environ.get("WHERE") else None
                    else: st.bad("EOW", f"{name} w={w} switch {a0}->{b0} at {t}, back at {tp}")
                    break


def runs_of(good, a):
    out = []; i = 0
    while i < len(good):
        if good[i]:
            j = i
            while j + 1 < len(good) and good[j + 1]: j += 1
            out.append((a + i, a + j + 1)); i = j + 1
        else: i += 1
    return out


def check_monoref(ctx, g, I, k, st, name):
    n, E = ctx.n, ctx.E
    lam = I[k]["lamX"]
    Qall = set(v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)
    for c in set(lam):
        U = [v for v in range(n) if lam[v] == c]
        sc = 1 if E.par[c] == 1 else -1
        kap0 = {z: (E.weight(I[k]["xi"][z][1]), sc * I[k]["xi"][z][2]) for z in U}
        kap1 = {z: (E.weight(I[k + 1]["xi"][z][1]), sc * I[k + 1]["xi"][z][2]) for z in U}
        # honest cycle membership at t
        oncyc = set()
        x = c
        while True:
            oncyc.add(x); x = I[k]["hn"][x]
            if x == c: break
        for z in U:
            if z == c: continue
            path, rep = R.lasso(I[k + 1]["hn"], z)
            ic = path.index(c)
            seq = path + path[path.index(rep):path.index(rep) + 1]   # the play, with the cycle once
            for j in range(1, len(path)):
                m = path[j]
                if not (m == c or m in Qall): continue
                qs = [x for x in path[:j] if x in Qall]
                if any(x in oncyc for x in qs): continue
                d0, d1 = tsub(kap0[z], kap0[m]), tsub(kap1[z], kap1[m])
                tag = "MR" if j <= ic else "MR_after"
                st.inc(tag + "_checks")
                if d1 < d0:
                    if tag == "MR": st.bad("MR", f"{name}@{k} c={c} z={z} m={m}")
                    else:
                        st.inc("MR_after_FAIL")
                        if os.environ.get("WHERE"): print("MR_after_FAIL", name, "t", k, "c", c, "z", z, "m", m, "off", d0, "->", d1, flush=True)


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; srng = random.Random(2222)
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
    for k in sorted(st.c):
        if not k.startswith("_"): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
