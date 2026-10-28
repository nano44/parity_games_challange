#!/usr/bin/env python3
r"""REFEREE-2 successor 18 (Opus 5.5, D15): mechanical check of the P-N5-OFFMONO unit (box 49), reviewed as ONE unit:
  P-N5-OFFMONO-box49 d9705ac6, -add- 5911aba8, -add2- f2d123ef, -add3- b7cd0ff1 (all on trunk 77f2664e).
State loop = my lane's SPEC loop (R2-N5-DUAL/dual_check.Runner, SPEC S1-S5 on si.py = SPEC S1's own implementation, read-only);
Xi = my own play value of (sigma, sigmabar) (R2-N5-RUND/rund_check.state_info, with the ENGXI cross-check against the engine).
The lane's experiments/new/box48/*.py are NOT run or imported. Every quantity below is written here from the packet's definitions.
Phase = maximal run with (lambda_Xi, tau) constant (as root_check.py; RESULTS R38 (a): a (lambda_Xi, tau)-phase).
Per phase, class c (U = lambda^{-1}(c)), state t: kappa_t(z) = (signed weight of P, s_c * len); par_t(q); Z_t(c); A_t; F.
Checks (each must be 0):
  AK      (A kappa): kappa_t(z) = kwt_c(z) + kappa_t(next_t z), z in U \ {c}; A0: kappa_t(c) = (0, 0)
  CYCID   x in U on an honest cycle at t <=> x in Z_t(c);  CSH  (CYC-SHAPE) kappa on Z_t(c) \ {c} = (0, s_c l), 1 <= l <= n-1
  AF      (A-F): z in A_t <=> kappa_t(z) in F
  OM      OFFSET-MONO (q on no honest cycle at t): off_{t+1}(q; p) >= off_t(q; p), p = par_{t+1}(q); also the proof's steps:
          OM1 (Step 1 at every vertex of pi), OM2 (kappa_t(y2) >= kappa_t(y1)); cases N / L counted
  OMP     OFFSET-MONO+ (q on an honest cycle at t): same, with OM1/OM2; cases L1 / L2 counted (L2 split by P(Xi_t y2) empty or not)
  CSUM    CHAIN-SUM identity, and the (t+1)-chain = the Q-vertices of q's play before c in order
  ZC      Remark Z-CONST at every transition with Z_t(c) = Z_{t+1}(c)
  ZCH     Lemma ZCH-COUNT: kinds partition ZCH; STRICT charges per v <= n-1; CEVEN <= n-1 (psi non-decreasing: PSI); TIE vertices Odd and
          kappa-equal; ODDC => c in Q and sigmabar(c) changed; |ZCH| <= (n-1)|U| + TIE + ODDC
  FTC     Lemma FT-COUNT: |FT_c| <= 2(n-1)(|U|-1);  FTK  Remark FT-CONST at every transition not in FT_c
  PFC     Lemma PF-CHOICE at every state, every Odd x in A_t;  TCH  Corollary TIE-CHARGE (next unchanged on A_t off FT_c; STRICT,TIE in FT)
  CC0/CC1/CC2/CC3  CHAIN-COUNT (cut CYC), CHAIN-COUNT' (cut ZC), CHAIN-COUNT'' (cut ZC''), CHAIN-COUNT''' (no cut): offset non-decreasing on
          every piece (PM*), sum form (CCS*) and D form (CCD*) for every q, on J = the whole phase and on one random sub-run J per (phase, class)
Controls (counted, expected to bite somewhere; they are NOT violations): CTL_sign (OM/OMP with the opposite length sign), CTL_part (p :=
par_t(q)), CTL_tbidx / CTL_tbrev (PF-CHOICE with index / reversed-index tie-break for both parities), CTL_ft1 (FT-COUNT with (n-1)(|U|-1)),
CTL_cc3m (CHAIN-COUNT''' sum form minus 1: counts q with count = sum form > 0, i.e. tight), CTL_noexit (pieces not cut at EXIT_x, p := current parent: offset falls inside).
CMP_*: cut-version bounds (CC0-CC2) smaller than CC3's (add3 §3 reading: not implied numerically by CHAIN-COUNT''').
Usage: offmono_check.py files list.txt [runs] | start game.pg [game.start] | random N nmin nmax seed k [starts]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-RUND"))
import rund_check as R
DC, pg, Stats = R.DC, R.pg, R.Stats
SUBSEED = int(os.environ.get("SUBSEED", "4949"))


def tadd(a, b): return (a[0] + b[0], a[1] + b[1])
def tsub(a, b): return (a[0] - b[0], a[1] - b[1])
Z0 = (0, 0)


def run_game(gp, s, t, st, name, rng):
    states, fbs = DC.Runner(gp).run(s, t)
    ctx = R.Ctx(gp); g, n = gp, gp.n
    I = [R.state_info(ctx, a, b, st, f"{name}@{k}") for k, (a, b) in enumerate(states)]
    st.inc("runs"); st.inc("states", len(I))
    key = [(I[k]["lamX"], tuple(b[v] for v in range(n) if g.owner[v] == 1)) for k, (_, b) in enumerate(states)]
    k0 = 0
    while k0 < len(states):
        k1 = k0
        while k1 + 1 < len(states) and key[k1 + 1] == key[k0]: k1 += 1
        check_phase(ctx, g, I, fbs, k0, k1, st, name, rng)
        k0 = k1 + 1


def play_to(hn, x, c):
    """vertices of x's honest play from x up to (excluding) its first visit of c; None if c is never reached."""
    out, seen = [], set()
    while x != c:
        if x in seen: return None
        seen.add(x); out.append(x); x = hn[x]
    return out


def cycle_of(hn, c):
    z, x = [c], hn[c]
    while x != c:
        z.append(x); x = hn[x]
        if len(z) > len(hn): return None
    return z


def check_phase(ctx, g, I, fbs, a, b, st, name, rng):
    n, E = ctx.n, ctx.E
    st.inc("phases"); st.inc("transitions", b - a)
    lam = I[a]["lamX"]
    Qall = frozenset(v for v in range(n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2)
    for c in sorted(set(lam)):
        U = frozenset(v for v in range(n) if lam[v] == c)
        st.inc("classes")
        sc = 1 if E.par[c] == 1 else -1
        wt = {v: (E.weight(E.bit[v]) if E.rank[v] > E.rank[c] else 0) for v in U}
        kw = {v: (wt[v], sc) for v in U}
        QU = sorted(v for v in Qall if v in U and v != c)
        F = set((0, sc * l) for l in range(1, n))
        S = {}
        for k in range(a, b + 1):
            hn, xi = I[k]["hn"], I[k]["xi"]
            kap = {z: (E.weight(xi[z][1]), sc * xi[z][2]) for z in U}
            kapX = {z: (E.weight(xi[z][1]), -sc * xi[z][2]) for z in U}   # control: opposite length sign
            Z = cycle_of(hn, c); Zs = set(Z)
            plays = {z: play_to(hn, z, c) for z in U}
            par = {}
            for q in QU:
                p = c
                for x in plays[q][1:]:
                    if x in Qall and x != q: p = x; break
                par[q] = p
            A = frozenset(z for z in U if z != c and xi[z][1] == 0)
            S[k] = dict(hn=hn, kap=kap, kapX=kapX, Z=Z, Zs=Zs, plays=plays, par=par, A=A)
            # AK, A0, CYCID, CSH, AF
            st.inc("AK_checks", len(U))
            if kap[c] != Z0: st.bad("AK", f"{name}@{k} c={c}: kappa(c) = {kap[c]}")
            for z in U:
                if z == c: continue
                if hn[z] not in U or kap[z] != tadd(kw[z], kap[hn[z]]): st.bad("AK", f"{name}@{k} c={c} z={z}")
                path, x = R.lasso(hn, z)
                oncyc = z in path[path.index(x):]
                if oncyc != (z in Zs): st.bad("CYCID", f"{name}@{k} c={c} z={z}")
                if z in Zs:
                    l = Z.index(z); l = len(Z) - l
                    if kap[z] != (0, sc * l) or not (1 <= l <= n - 1): st.bad("CSH", f"{name}@{k} c={c} z={z}")
                if (z in A) != (kap[z] in F): st.bad("AF", f"{name}@{k} c={c} z={z}")
            # PF-CHOICE
            for x in A:
                if g.owner[x] != 1: continue
                opts = [y for y in sorted(set(g.succ[x])) if y == c or y in A]
                if not opts: st.bad("PFC", f"{name}@{k} c={c} x={x}: no option"); continue
                def tb(y, mode):
                    if mode == "idx": return (y,)
                    if mode == "rev": return (-y,)
                    return tuple(reversed(plays[y])) if y != c else ()
                mode = "idx" if E.par[c] == 0 else "seq"
                best = min(opts, key=lambda y: (kap[y], tb(y, mode)))
                st.inc("PFC_checks")
                if len(opts) >= 2: st.inc("PFC_checks_multi")
                if best != hn[x]: st.bad("PFC", f"{name}@{k} c={c} x={x}: min {best} != sigmabar {hn[x]}")
                if min(opts, key=lambda y: (kap[y], tb(y, "idx"))) != hn[x]: st.inc("CTL_tbidx")
                if min(opts, key=lambda y: (kap[y], tb(y, "rev"))) != hn[x]: st.inc("CTL_tbrev")
                if E.par[c] == 0 and min(opts, key=lambda y: (kap[y], tb(y, "seq"))) != hn[x]: st.inc("CTL_tbseq_ceven")
        # transitions
        T = list(range(a, b))
        EXIT = {x: set() for x in QU}
        CYC, ZCH, FT = set(), set(), set()
        kinds = {"STRICT": 0, "TIE": 0, "CEVEN": 0, "ODDC": 0}
        charges = {}
        offseq = {}   # (x, k) -> (off_k(x; par_{k+1} x), off_{k+1}(x; par_{k+1} x))
        for k in T:
            s0, s1 = S[k], S[k + 1]
            k0p, k1p = s0["kap"], s1["kap"]
            if any(x in s0["Zs"] for x in QU): CYC.add(k)
            if s0["Z"] != s1["Z"]: ZCH.add(k)
            for z in U:
                if z != c and k0p[z] != k1p[z] and (k0p[z] in F or k1p[z] in F): FT.add(k); break
            for x in QU:
                if s0["par"][x] != s1["par"][x]: EXIT[x].add(k)
            # OFFSET-MONO and OFFSET-MONO+
            for q in QU:
                p = s1["par"][q]
                o0, o1 = tsub(k0p[q], k0p[p]), tsub(k1p[q], k1p[p])
                offseq[(q, k)] = (o0, o1)
                oncyc = q in s0["Zs"]
                tag = "OMP" if oncyc else "OM"
                st.inc(tag + "_checks")
                if o1 < o0: st.bad(tag, f"{name}@{k} c={c} q={q} p={p}: {o0} -> {o1}")
                if o1 > o0: st.inc(tag + "_strict")
                if s0["par"][q] != p: st.inc(tag + "_parent_changed")
                # Step 1 along pi = q's (t+1)-play from y2 up to p
                y1, y2 = s0["hn"][q], s1["hn"][q]
                pl = s1["plays"][q]
                pi = pl[1:pl.index(p)] if p != c else pl[1:]
                for x in pi + [p]:
                    if tsub(k1p[x], k1p[p]) < tsub(k0p[x], k0p[p]): st.bad(tag + "1", f"{name}@{k} c={c} q={q} x={x}")
                if k0p[y2] < k0p[y1]: st.bad(tag + "2", f"{name}@{k} c={c} q={q}: kappa_t(y2) < kappa_t(y1)")
                # case
                pt = play_to(s0["hn"], y2, c) if y2 != c else []
                if not oncyc:
                    st.inc("OM_caseL" if q in pt else "OM_caseN")
                else:
                    if q in pt: st.inc("OMP_caseL1")
                    else:
                        st.inc("OMP_caseL2"); st.inc("OMP_caseL2_P" + ("0" if I[k]["xi"][y2][1] == 0 else "1"))
                # controls
                kx0, kx1 = s0["kapX"], s1["kapX"]
                if tsub(kx1[q], kx1[p]) < tsub(kx0[q], kx0[p]): st.inc("CTL_sign")
                pp = s0["par"][q]
                if tsub(k1p[q], k1p[pp]) < tsub(k0p[q], k0p[pp]): st.inc("CTL_part")
            # CHAIN-SUM
            for q in QU:
                ch = [q]
                while ch[-1] != c: ch.append(s1["par"][ch[-1]] if ch[-1] != c else c)
                qs = [x for x in s1["plays"][q] if x in Qall and x != c]
                if ch[:-1] != qs: st.bad("CSUM", f"{name}@{k} c={c} q={q}: chain {ch} vs play Q-vertices {qs}")
                tot = Z0
                for i in range(len(ch) - 1):
                    tot = tadd(tot, tsub(tsub(k1p[ch[i]], k1p[ch[i + 1]]), tsub(k0p[ch[i]], k0p[ch[i + 1]])))
                if tot != tsub(k1p[q], k0p[q]): st.bad("CSUM", f"{name}@{k} c={c} q={q}: sum")
                st.inc("CSUM_checks")
            # Z-CONST
            if s0["Z"] == s1["Z"]:
                st.inc("ZC_checks")
                for x in s0["Z"]:
                    if k0p[x] != k1p[x]: st.bad("ZC", f"{name}@{k} c={c} x={x}: kappa")
                for x in QU:
                    if x in s0["Zs"]:
                        p = s0["par"][x]
                        if s1["par"][x] != p or tsub(k0p[x], k0p[p]) != tsub(k1p[x], k1p[p]): st.bad("ZC", f"{name}@{k} c={c} x={x}: par/off")
            else:
                # ZCH kinds
                Nset = [v for v in s1["Z"][1:] if s1["hn"][v] != s0["hn"][v]]
                strict = [v for v in Nset if k1p[v] > k0p[v]]
                if strict:
                    kinds["STRICT"] += 1; v = strict[0]; charges[v] = charges.get(v, 0) + 1
                elif Nset:
                    kinds["TIE"] += 1
                    for v in Nset:
                        if g.owner[v] != 1 or k1p[v] != k0p[v]: st.bad("ZCH", f"{name}@{k} c={c} TIE vertex {v}")
                elif g.owner[c] == 0:
                    kinds["CEVEN"] += 1
                else:
                    kinds["ODDC"] += 1
                    if c not in Qall or s0["hn"][c] == s1["hn"][c]: st.bad("ZCH", f"{name}@{k} c={c} ODDC")
                # TIE-CHARGE: STRICT and TIE lie in FT
                if Nset and k not in FT: st.bad("TCH", f"{name}@{k} c={c}: STRICT/TIE not in FT")
            # PSI for c Even
            if g.owner[c] == 0:
                if k1p[s1["hn"][c]] < k0p[s0["hn"][c]]: st.bad("PSI", f"{name}@{k} c={c}")
            # FT-CONST and TIE-CHARGE (next unchanged on A_t)
            if k not in FT:
                st.inc("FTK_checks")
                if s0["A"] != s1["A"]: st.bad("FTK", f"{name}@{k} c={c}: A changes")
                for z in list(s0["A"]) + [c]:
                    if k0p[z] != k1p[z]: st.bad("FTK", f"{name}@{k} c={c} z={z}: kappa")
                for x in s0["Z"][1:]:
                    p = s1["par"].get(x)
                    if p is None:   # x not in Q: offset to its (t+1) parent is defined for Q only; check kappa(x) instead (done above)
                        continue
                    if tsub(k0p[x], k0p[p]) != tsub(k1p[x], k1p[p]): st.bad("FTK", f"{name}@{k} c={c} x={x}: offset")
                for z in s0["A"]:
                    if s0["hn"][z] != s1["hn"][z]: st.bad("TCH", f"{name}@{k} c={c} z={z}: next changes on A off FT")
        # per-phase counts
        if ZCH:
            st.inc("ZCH_total", len(ZCH))
            for kk, vv in kinds.items(): st.inc("ZCH_" + kk, vv)
            if any(vv > n - 1 for vv in charges.values()): st.bad("ZCH", f"{name} c={c}: STRICT charges > n-1")
            if sum(charges.values()) > (n - 1) * (len(U) - 1): st.bad("ZCH", f"{name} c={c}: STRICT total")
            if kinds["CEVEN"] > n - 1: st.bad("ZCH", f"{name} c={c}: CEVEN > n-1")
            if len(ZCH) > (n - 1) * len(U) + kinds["TIE"] + kinds["ODDC"]: st.bad("ZCH", f"{name} c={c}: |ZCH| bound")
            st.mxr("max_ZCH_per_phase_class", (len(ZCH), name, c))
            st.mxr("max_TIE_per_phase_class", (kinds["TIE"], name, c))
            st.mxr("max_ODDC_per_phase_class", (kinds["ODDC"], name, c))
        st.inc("FT_total", len(FT)); st.inc("CYC_total", len(CYC))
        st.mxr("max_FT_per_phase_class", (len(FT), name, c))
        if len(FT) > 2 * (n - 1) * (len(U) - 1): st.bad("FTC", f"{name} c={c}: |FT| = {len(FT)}")
        if len(FT) > (n - 1) * (len(U) - 1): st.inc("CTL_ft1")
        if not QU or not T: continue
        ZC = ZCH & CYC; ZC2 = ZCH & CYC & FT
        st.inc("ZC_total", len(ZC)); st.inc("ZC2_total", len(ZC2))
        # CHAIN-COUNT family on J = whole phase and one random sub-run
        Js = [(a, b - 1)]
        if b - a >= 2:
            i = rng.randrange(a, b); j = rng.randrange(i, b); Js.append((i, j))
        for (ja, jb) in Js:
            J = list(range(ja, jb + 1))
            Jset = set(J)
            chg = {q: sum(1 for k in J if S[k]["kap"][q] != S[k + 1]["kap"][q]) for q in QU}
            bnd = {}
            for tag, X in (("CC0", CYC & Jset), ("CC1", ZC & Jset), ("CC2", ZC2 & Jset), ("CC3", set())):
                sumform = len(X); D = 1; ex = {}
                pieces_all = {}
                for x in QU:
                    cut = (EXIT[x] & Jset) | X
                    pieces, cur = [], []
                    for k in J:
                        if k in cut:
                            if cur: pieces.append(cur); cur = []
                        else: cur.append(k)
                    if cur: pieces.append(cur)
                    tot = len(EXIT[x] & Jset)
                    for pc in pieces:
                        p = S[pc[0]]["par"][x]
                        vals = []
                        for k in pc + [pc[-1] + 1]:
                            if S[k]["par"][x] != p: st.bad("PM" + tag[2:], f"{name} c={c} x={x}: parent not constant on a piece")
                            vals.append(tsub(S[k]["kap"][x], S[k]["kap"][p]))
                        if any(vals[i + 1] < vals[i] for i in range(len(vals) - 1)):
                            st.bad("PM" + tag[2:], f"{name} c={c} x={x} piece {pc[0]}..{pc[-1]}: offset falls")
                        v = len(set(vals)); D = max(D, v); tot += v - 1
                    sumform += tot; ex[x] = len(EXIT[x] & Jset)
                    pieces_all[x] = pieces
                dform = (sum(D * (ex[x] + 1) for x in QU) if tag == "CC3"
                         else len(X) + sum(D * (ex[x] + len(X) + 1) for x in QU))
                st.inc(tag + "_checks", len(QU)); bnd[tag] = (sumform, dform)
                for q in QU:
                    if chg[q] > sumform: st.bad("CCS" + tag[2:], f"{name} c={c} q={q} J={ja}..{jb}: {chg[q]} > {sumform}")
                    if chg[q] > dform: st.bad("CCD" + tag[2:], f"{name} c={c} q={q} J={ja}..{jb}: {chg[q]} > {dform}")
                    if tag == "CC3" and chg[q] > sumform - 1 and chg[q] > 0: st.inc("CTL_cc3m")
                    if tag == "CC3": st.mxr("max_kappa_changes_q", (chg[q], name, c, q, sumform, dform))
            # add3 §3 reading: is a cut version's bound ever SMALLER than CHAIN-COUNT'''s (then it is not implied numerically)
            for tag in ("CC0", "CC1", "CC2"):
                if bnd[tag][0] < bnd["CC3"][0]: st.inc("CMP_sum_" + tag + "_lt_CC3"); st.mxr("CMPX_sum_" + tag, (bnd["CC3"][0] - bnd[tag][0], name, c, ja, jb, bnd[tag][0], bnd["CC3"][0]))
                if bnd[tag][1] < bnd["CC3"][1]: st.inc("CMP_D_" + tag + "_lt_CC3")
            # control: no exit cut, p := current parent (offset to par_t), within J
            for x in QU:
                for k in J:
                    p0 = S[k]["par"][x]
                    if tsub(S[k + 1]["kap"][x], S[k + 1]["kap"][p0]) < tsub(S[k]["kap"][x], S[k]["kap"][p0]):
                        st.inc("CTL_noexit"); break
            st.mxr("max_EXIT_per_x", (max(len(EXIT[x] & Jset) for x in QU), name, c))


def main():
    st = Stats(); a = sys.argv[1:]; rng = random.Random(SUBSEED)
    if a[0] == "files":
        runs = int(a[2]) if len(a) > 2 else 3; srng = random.Random(4918)
        for path in [l.strip() for l in open(a[1]) if l.strip()]:
            gp = pg.read(os.path.join(DC.ROOT, path))
            for r in range(runs):
                s, t = R.starts(gp, r, srng); run_game(gp, s, t, st, f"{path}#{r}", rng)
    elif a[0] == "random":
        N, nmin, nmax, seed, k = map(int, a[1:6]); ns = int(a[6]) if len(a) > 6 else 2
        srng = random.Random(seed)
        sys.path.insert(0, os.path.join(HERE, "..", "R2-N5-H3")); import h3_check as H3
        for i in range(N):
            nn = srng.randint(nmin, nmax)
            gp = DC.rand_game(srng, nn, "kO") if k == 0 else H3.rand_kO(srng, nn, k)
            for r in range(ns):
                s, t = R.starts(gp, r, srng); run_game(gp, s, t, st, f"random{seed}:{i}#{r}", rng)
    elif a[0] == "start":
        gp = pg.read(a[1])
        if len(a) > 2: s, t = R.read_start(gp, a[2])
        else: s, t = R.starts(gp, 0, None)
        run_game(gp, s, t, st, os.path.basename(a[1]), rng)
    print("MODE", " ".join(a))
    for k in sorted(st.c): print(f"{k}: {st.c[k]}")
    for k in sorted(st.mx): print(f"{k}: {st.mx[k]}")
    for v in st.viol[:40]: print("VIOLATION", v)
    print("RESULT", "FAIL" if st.c.get("VIOLATIONS") else "OK", f"violations={st.c.get('VIOLATIONS', 0)}")


if __name__ == "__main__":
    main()
