#!/usr/bin/env python3
r"""REFEREE-2 successor 17 (Opus 5.5, D15): mechanical check of packet P-N5-EPC (docs/new/P-N5-EPC-box48.md sha1 9f48ded7, l-new 81ab0b72).
On my R2-N5-FBC/fbc_check.py machinery (state loop = succ. 13's SPEC loop via R2-N5-HON; Xi own play values, ENGXI cross-check; LEV_C EXACT
per (phase, configuration) by enumeration of all simple H_C-paths, budget; over budget -> that configuration UNK, counted). Lane tools
(experiments/new/box48/*.py) NOT run or imported.
For EVERY configuration C visited in a phase (not only those at fallback sources):
  RETFB   Lemma RET-FB: in-phase fallback t -> t+1 (any configuration), C-state s >= t+1: LEV_C(s) >= min(LEV_C(t) + 1, n - 1)
  EVEN    its Even step: at t+1 the Even vertices already satisfy level min(LEV_C(t) + 1, n - 1) in H_C (frame-free relaxation)
  VIS     V_C <= 2n^2 - n + R0_C, with the kinds: (a) <= 2n(n-1), (b) <= n - 1 and LEV_C rises along kind-(b) returns
  EPC     N_ep <= NCONF (2n^2 - n) + R0 and R0 <= sum_S REV(S) over maximal fallback-free runs S
  SATFB   saturated C-state fallback source t: t+1 last state of P or no C-state after t; SATFB1 <= 1 per C; ISE: at a Xi-flat in-phase
          fallback, I_sigma(t+1) = empty (SAT-FB's proof step); FBC' f <= n |C_f|
  ASM     N_ep = N_0 + N_1 + N_>=2; N_0 <= 4n^2 - 3n; N_>=2 <= NCONF_>=2 (2n^2 - n) + R0_>=2  (N_1's bound is an implication from (Sigma tau),
          not checked); REM: (D changes) + 1 <= N_ep
  DEAD    counts saturated fallbacks that are not Xi-flat / not the phase's last transition (the packet's §5 DEAD guess)
Controls EPC_MUT: plus2 (RET-FB with + 2), nonC (RET-FB asserted at EVERY state s >= t+1, not only C-states), last (SAT-FB without its second
disjunct: "a saturated fallback ends the phase" = the DEAD guess), noR0 (VIS without R0_C).
Usage: epc_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-HONFF"))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-HON"))
import honff_check as HF
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-FBC"))
import fbc_check as FB
H = HF.H
R, DC, pg, Stats = H.R, H.DC, H.pg, H.Stats
MUT = os.environ.get("EPC_MUT", "")
BUDGET = int(os.environ.get("BUDGET", "400000"))


def check_game(gp, s, t, st, name):
    g, n = gp, gp.n
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp)
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    Q = [v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]
    st.inc("runs"); st.inc("states", len(I))
    tauk = [tuple(b[v] for v in range(n) if g.owner[v] == 1) for _, b in states]
    key = [(I[k]["lamX"], tauk[k]) for k in range(len(states))]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(ctx, g, I, fbs, k0, k1, Q, st, name, last_run=(k1 == len(states) - 1))
        k0 = k1 + 1


def check_phase(ctx, g, I, fbs, a, b, Q, st, name, last_run):
    n = ctx.n
    st.inc("phases")
    lam = I[a]["lamX"]; tu = I[a]["tu"]
    cyc = frozenset(v for v in range(n) if lam[v] == v)
    conf = {k: tuple(I[k]["hn"][q] for q in Q) for k in range(a, b + 1)}
    tq = tuple(tu[q] for q in Q)
    Dsz = lambda C: sum(1 for i in range(len(Q)) if C[i] != tq[i])
    fbk = [k for k in range(a, b) if fbs[k]]
    f = len(fbk)
    # epochs
    epochs, k = [], a
    while k <= b:
        e = k
        while e + 1 <= b and conf[e + 1] == conf[k]: e += 1
        epochs.append((k, e)); k = e + 1
    Nep = len(epochs)
    confs = sorted(set(conf.values()))
    NCONF = len(confs)
    starts = {C: [p for p, q in epochs if conf[p] == C] for C in confs}
    # remark and ASM parts not needing LEV
    dch = sum(1 for k in range(a, b) if Dsz(conf[k]) != Dsz(conf[k + 1]) or
              frozenset(i for i in range(len(Q)) if conf[k][i] != tq[i]) != frozenset(i for i in range(len(Q)) if conf[k + 1][i] != tq[i]))
    st.inc("REM_checks")
    if dch + 1 > Nep: st.bad("REM", f"{name}@{a}")
    N0 = sum(1 for p, q in epochs if Dsz(conf[p]) == 0); N1 = sum(1 for p, q in epochs if Dsz(conf[p]) == 1)
    N2 = Nep - N0 - N1
    st.inc("ASM_checks")
    if N0 > 4 * n * n - 3 * n: st.bad("ASM_N0", f"{name}@{a}")
    # Xi-flat fallbacks: I_sigma(t+1) empty and t+1 last
    for t in fbk:
        if I[t + 1]["xi"] == I[t]["xi"]:
            st.inc("ISE_checks")
            if I[t + 1]["Is"]: st.bad("ISE", f"{name}@{t}: Xi-flat in-phase fallback leaves I_sigma nonempty")
            if t + 1 != b: st.bad("FLATLAST", f"{name}@{t}")
    if Nep > 1: st.mxr("max_Nep", (Nep, f"{name}@{a} n {n} NCONF {NCONF}"))
    st.mxr("max_NCONF", (NCONF, f"{name}@{a} n {n} N_ep {Nep}"))
    st.mxr("max_V_C", (max(len(v) for v in starts.values()), f"{name}@{a} n {n}"))
    # LEV_C for every configuration visited
    allx = list(range(n)); evx = [x for x in allx if g.owner[x] == 0]
    LEVs, unk = {}, set()
    for C in confs:
        s0 = next(k for k in range(a, b + 1) if conf[k] == C)
        if not fbk and len(starts[C]) < 2:
            LEVs[C] = (None, 0); st.inc("C_nothing_to_check"); continue
        need = sorted(set([t for t in fbk] + starts[C]))
        res = levels(ctx, I, I[s0]["hn"], cyc, a, b, need, n, allx, evx)
        if res is None:
            unk.add(C); st.inc("UNK_C"); continue
        LEV, LEVE, D = res
        st.inc("C_checked")
        if D < n - 1: st.inc("C_deep")
        exact = lambda k: LEV[k] < D or D >= n - 1
        for k in range(a, b):
            if LEV[k + 1] < LEV[k]: st.bad("MONO", f"{name}@{k}")
        # RET-FB and its Even step, for every in-phase fallback (any configuration)
        for t in fbk:
            L = min(LEV[t] + (2 if MUT == "plus2" else 1), n - 1)
            st.inc("EVEN_checks")
            if not exact(t): st.inc("RETFB_src_not_exact"); continue
            if LEVE[t + 1] < min(LEV[t] + 1, n - 1, D): st.bad("EVEN", f"{name}@{t} C {C}")
            for s in range(t + 1, b + 1):
                if conf[s] != C and MUT != "nonC": continue
                st.inc("RETFB_checks")
                if conf[t] != C: st.inc("RETFB_checks_other_config")
                if L > D and D < n - 1: st.inc("RETFB_skip_cap"); continue
                if LEV[s] < L: st.bad("RETFB", f"{name}@{t}->{s} C {C}: LEV_C {LEV[t]} -> {LEV[s]}")
        # VIS
        ss = starts[C]; V = len(ss)
        ka = kb = kc = 0; lastb = None
        if not all(exact(x) for x in ss[:-1]):
            st.inc("VIS_not_exact"); LEVs[C] = None; unk.add(C); continue
        for i in range(V - 1):
            si, sj = ss[i], ss[i + 1]
            if LEV[si] >= n - 1: ka += 1
            elif any(a <= t < sj and t >= si for t in fbk):
                kb += 1
                if LEV[sj] < min(LEV[si] + 1, n - 1): st.bad("VIS_b_rise", f"{name}@{si}")
            else: kc += 1
        st.inc("VIS_checks"); st.inc("VIS_returns", V - 1); st.inc("VIS_a", ka); st.inc("VIS_b", kb); st.inc("VIS_R0", kc)
        if ka > 2 * n * (n - 1): st.bad("VIS_a", f"{name}@{a}")
        if kb > n - 1: st.bad("VIS_b", f"{name}@{a}")
        r0 = 0 if MUT == "noR0" else kc
        if V > 2 * n * n - n + r0: st.bad("VIS", f"{name}@{a} C {C}: V {V}")
        LEVs[C] = (LEV, kc)
        # SAT-FB
        satsrc = [t for t in fbk if conf[t] == C and exact(t) and LEV[t] >= n - 1]
        st.mxr("max_sat_src_per_C", (len(satsrc), f"{name}@{a}"))
        if len(satsrc) > 1: st.bad("SATFB1", f"{name}@{a} C {C}")
        for t in satsrc:
            st.inc("SATFB_checks")
            later = any(conf[s] == C for s in range(t + 1, b + 1))
            flat = I[t + 1]["xi"] == I[t]["xi"]
            if not flat: st.inc("DEAD_nonflat")
            if t + 1 != b: st.inc("DEAD_notlast")
            if t + 1 != b and later: st.bad("SATFB", f"{name}@{t}")
            if MUT == "last" and t + 1 != b: st.bad("MUT_last", f"{name}@{t}")
    Cf = set(conf[t] for t in fbk)
    if f:
        st.inc("FBCp_checks")
        if f > n * len(Cf): st.bad("FBCp", f"{name}@{a}")
    if not unk:
        st.inc("EPC_phases")
        R0 = sum(LEVs[C][1] for C in confs)
        if Nep > NCONF * (2 * n * n - n) + R0: st.bad("EPC", f"{name}@{a}")
        # fallback-free runs
        runs, k = [], a
        while k <= b:
            e = k
            while e < b and not fbs[e]: e += 1
            runs.append((k, e)); k = e + 1
        rev = 0
        for p, q in runs:
            stt = [s for s, _ in epochs if p <= s <= q]
            rev += len(stt) - len(set(conf[s] for s in stt))
        if R0 > rev: st.bad("EPC_REV", f"{name}@{a}: R0 {R0} REV {rev}")
        st.inc("R0_total", R0)
        R02 = sum(LEVs[C][1] for C in confs if Dsz(C) >= 2)
        NC2 = sum(1 for C in confs if Dsz(C) >= 2)
        if N2 > NC2 * (2 * n * n - n) + R02: st.bad("ASM_N2", f"{name}@{a}")
        st.inc("ASM_N2_checks")


def levels(ctx, I, hC, cyc, a, b, need, n, allx, evx):
    """LEV_C (and its Even-only version) at every state of [a, b]: full enumeration if within budget (exact, D = n - 1); else iterative
    deepening on the path length D until every state in `need` has min(LEV_C, D) < D; values are min(LEV_C, D)."""
    try:
        sv = HF.simple_values(ctx, hC, cyc, BUDGET)
        B = HF.table(ctx, sv, allx)
        return ({k: HF.lev(ctx, B, I[k]["xi"], allx) for k in range(a, b + 1)},
                {k: HF.lev(ctx, B, I[k]["xi"], evx) for k in range(a, b + 1)}, n - 1)
    except HF.Over:
        pass
    D = 1
    while D < n - 1:
        try:
            sv = FB.values_upto(ctx, hC, cyc, BUDGET, D)
        except HF.Over:
            return None
        LEV = {k: FB.lev_capped(ctx, sv, I[k]["xi"], allx, D) for k in range(a, b + 1)}
        if all(LEV[k] < D for k in need):
            LEVE = {k: FB.lev_capped(ctx, sv, I[k]["xi"], evx, D) for k in range(a, b + 1)}
            return LEV, LEVE, D
        D += 1
    return None


def main():
    st = Stats(); a = sys.argv[1:]
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; rng = random.Random(1748)
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
        s, t = R.read_start(gp, a[2]) if len(a) > 2 and not a[2].isdigit() else R.starts(gp, int(a[2]) if len(a) > 2 else 0, random.Random(int(a[3]) if len(a) > 3 else 0))
        check_game(gp, s, t, st, os.path.basename(a[1]))
    print("MODE", " ".join(a), "MUT", MUT or "-", "BUDGET", BUDGET)
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
