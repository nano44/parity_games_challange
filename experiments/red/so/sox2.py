#!/usr/bin/env python3
"""Box 37 (L-RED): independent checker of L-NEW succ. 13's box-33 lemmas, read on claude/l-new fb157c31
(docs/new/N5-K-box33.md §1, §2, §8, §9; not packeted), written from that text. Trace and helpers: sox.py (trace asserted = n5.run).
Notation: R_k includes o (P-N5-LP §0 = P-N5-CLS's R̄); F_k = V \\ R_k; W_k = valuation of the (σ_k, τ_k)-play (si.py Engine on the arena
with Odd fixed to τ_k); c_θ = λ_Ξ(o); c_w(k) = λ_W(o); H1: o not on its H_k-cycle; H2: o not on its (σ_k,τ_k)-cycle; H3: c_w = c_θ.
E_k / O_k: max level of the relevant Even changes / of the relevant σ̄(o) change (⊥ = -2). ε-transition: O_k > E_k.
Checked (counters):
  RSTICK   S4a in-phase transition: x in R_s with λ_W(x) != λ_Ξ(x)  =>  x in R_{s+1}       RSTICK2  c_w(s) != c_θ => R_s ⊆ R_{s+1}
  PREFIX   in each maximal fallback-free run of in-phase transitions, the states with c_w = c_θ form a prefix
  PREFR    after the prefix R never loses a vertex;   PREFN  crossings after the prefix <= n-1 per run
  XSN      per phase X <= (f+1)(n-1) + f + X_SN  (X_SN = S4a crossings at states k with c_w(k) = c_θ)
  OR_A     ε-transition: x0 = σ̄_k(o) in R_{k+1};  OR_F  under H1: x0 in F_k;  OR_C  lev(θ_k, θ_{k+1}) = O_k
  EXITR    ε-transition: x0 in R_t for t in [k+1, next fallback transition index] (or the phase's last state)   [CONJECTURE]
  ORX      each exit absorbed at most once per fallback-free segment (ε-transitions)
  TCS      θ-change: lev(θ_k,θ_{k+1}) <= E_k, or ε and = O_k
  REL      (box 38) exit releases per phase: (k, x) with k a non-fallback transition, x in succ(o) minus {o}, x in R_k but not R_{k+1}
  NJB      (box 38, L-SI CONJECTURE) no COARSE_M change at a non-fallback transition strictly inside a level-M block (M >= 0) of
           consecutive in-scope fallbacks of a scope run;  FLATALL  none at f_1 .. f_{N-1} (FLAT-ALL (iii))
  ABSL_i/ii/iii/cnt  Lemma ABS-L on scope runs (CLS §0), consecutive fallbacks k0 < k in S, L = M_{k0}, r_j > L on [k0+1, k]
Usage: sox2.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, pg
from si import Engine
from sox import BOT, INF, lev

def analyse(g, cap=5000):
    oc = sox.oddchoice(g); assert len(oc) == 1, "not C^1O"; o = oc[0]; n = g.n; d_o = len(set(g.succ[o]))
    S, FB, E = sox.trace(g, cap)
    import n5
    it, fb, *_ = n5.run(g, cap=cap); assert (it, fb) == (len(FB), sum(FB)), "trace differs from n5.run"
    N = len(S); ev = [E.evaluate(s) for s, _ in S]; Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]
    lam = [tuple(x[0] for x in X) for X in Xi]
    Wv = []
    for s, t in S:
        succ = [list(g.succ[v]) if g.owner[v] == 0 else [t[v]] for v in range(n)]
        Wv.append(Engine(pg.Game(list(g.prio), list(g.owner), succ)).evaluate(s)[0])
    def play(k, v, odd):
        x, seen, out = v, set(), []
        while x not in seen:
            seen.add(x); out.append(x); x = S[k][0][x] if g.owner[x] == 0 else (S[k][1][x] if odd == "tau" else sb[k][x])
        return out, x
    R = []; H1 = []; H2 = []
    for k in range(N):
        r = {o}
        for v in range(n):
            if o in play(k, v, "tau")[0]: r.add(v)
        R.append(frozenset(r))
        p, back = play(k, sb[k][o], "sbar"); H1.append(o not in p)
        p, back = play(k, S[k][1][o], "tau"); H2.append(o not in p)
    def EO(k):
        Ek = Ok = BOT
        for v in range(n):
            if lam[k][v] == v: continue
            if g.owner[v] == 0 and S[k][0][v] != S[k + 1][0][v]: Ek = max(Ek, lev(Xi[k][S[k][0][v]], Xi[k][S[k + 1][0][v]]))
            if v == o and sb[k][v] != sb[k + 1][v]: Ok = lev(Xi[k][sb[k][v]], Xi[k][sb[k + 1][v]])
        return Ek, Ok
    def M(k):
        return max((lev(Xi[k][S[k][0][y]], Xi[k][z]) for y, z in E.improving(S[k][0], Xi[k])), default=BOT)
    inph = [lam[k] == lam[k + 1] and S[k][1] == S[k + 1][1] for k in range(N - 1)]
    C = {}; ex = {}
    def bad(nm, k): C[nm] = C.get(nm, 0) + 1; ex.setdefault(nm, k)
    phases = []; k = 0
    while k < N - 1:
        if not inph[k]: k += 1; continue
        j = k
        while j + 1 < N - 1 and inph[j + 1]: j += 1
        phases.append((k, j)); k = j + 1
    rows = []
    for (a, b) in phases:
        cth = lam[a][o]; cw = [Wv[k][o][0] for k in range(N)]
        X = sum(R[k] != R[k + 1] for k in range(a, b + 1)); f = sum(FB[a:b + 1])
        XSN = sum(R[k] != R[k + 1] and not FB[k] and cw[k] == cth for k in range(a, b + 1))
        REL = sum(1 for k in range(a, b + 1) if not FB[k] for x in set(g.succ[o]) if x != o and x in R[k] and x not in R[k + 1])
        epsx = {}
        for k in range(a, b + 1):
            Ek, Ok = EO(k)
            if Ok != BOT and Ok > Ek: epsx.setdefault(k, sb[k][o])
        absorbed = set(); RELe = 0
        for k in range(a, b + 1):
            if k in epsx and epsx[k] in R[k + 1]: absorbed.add(epsx[k])
            for x in list(absorbed):
                if x not in R[k + 1]:
                    absorbed.discard(x)
                    if not FB[k]: RELe += 1
        if X > (f + 1) * (n - 1) + f + XSN: bad("XSN", a)
        eo = {k: EO(k) for k in range(a, b + 1)}
        # R-STICK
        for k in range(a, b + 1):
            if FB[k]: continue
            for x in R[k]:
                if Wv[k][x][0] != Xi[k][x][0] and x not in R[k + 1]: bad("RSTICK", k)
            if cw[k] != cth and not R[k] <= R[k + 1]: bad("RSTICK2", k)
        # SN-PREFIX on maximal fallback-free runs
        k = a; maxpost = 0; maxpre = 0; runs = []
        while k <= b:
            if FB[k]: k += 1; continue
            j = k
            while j + 1 <= b and not FB[j + 1]: j += 1
            st = list(range(k, j + 2)); eq = [cw[s] == cth for s in st]
            p = 0
            while p < len(eq) and eq[p]: p += 1
            if any(eq[p:]): bad("PREFIX", k)
            pre = sum(R[s] != R[s + 1] for s in st[:p] if s < st[-1])
            maxpre = max(maxpre, pre)
            post = 0
            for s in st[p:-1]:
                if not R[s] <= R[s + 1]: bad("PREFR", s)
                post += R[s] != R[s + 1]
            if post > n - 1: bad("PREFN", k)
            maxpost = max(maxpost, post); runs.append((k, j)); k = j + 1
        # ε-transitions: OR, EXIT-R, ORX, TC-SPLIT
        eps = []; epsSN = 0; hard = 0
        for k in range(a, b + 1):
            Ek, Ok = eo[k]
            th0, th1 = Xi[k][o], Xi[k + 1][o]
            isE = Ok != BOT and Ok > Ek
            if th0 != th1:
                lt = lev(th0, th1)
                if not (lt <= Ek or (isE and lt == Ok)): bad("TCS", k)
            if not isE: continue
            x0 = sb[k][o]; eps.append((k, x0))
            if x0 not in R[k + 1]: bad("OR_A", k)
            if H1[k] and x0 in R[k]: bad("OR_F", k)
            if lev(th0, th1) != Ok: bad("OR_C", k)
            nf = next((t for t in range(k + 1, b + 1) if FB[t]), None); end = nf if nf is not None else b + 1
            if any(x0 not in R[t] for t in range(k + 1, end + 1)): bad("EXITR", k)
            if cw[k + 1] == cth: epsSN += 1
            if cw[k + 1] == cth: hard += 1
        seg = {}
        for k, x0 in eps:
            sid = sum(FB[a:k + 1]); seg.setdefault(sid, []).append(x0)
        for sid, xs in seg.items():
            if len(xs) != len(set(xs)): bad("ORX", a)
        maxseg = max((len(v) for v in seg.values()), default=0)
        # ABS-L on scope runs
        scope = [H1[k] and H2[k] and cw[k] == cth and H2[k + 1] and Wv[k + 1][o] == Wv[k][o] for k in range(a, b + 1)]
        k = a; absl_checked = 0; nblocks = 0; blockfb = 0; nrel = 0; reabs_ = 0; minmn = 10 ** 9; mnabs = 0; soleabs = 0
        while k <= b:
            if not scope[k - a]: k += 1; continue
            j = k
            while j + 1 <= b and scope[j + 1 - a]: j += 1
            fbs = [t for t in range(k, j + 1) if FB[t]]
            # box 38: CONJECTURE NJB (L-SI docs/si/N5-C-box9.md §3): level-M blocks of consecutive in-scope fallbacks, M >= 0
            Mf = {t: M(t) for t in fbs}; bi = 0
            while bi < len(fbs):
                bj = bi
                while bj + 1 < len(fbs) and Mf[fbs[bj + 1]] == Mf[fbs[bi]]: bj += 1
                Mb = Mf[fbs[bi]]
                if Mb >= 0 and bj > bi:
                    f1, fN = fbs[bi], fbs[bj]; nblocks += 1; blockfb = max(blockfb, bj - bi + 1)
                    for t in range(f1, fN):
                        ch = any(sox.coarse(Xi[t + 1][v], Mb) != sox.coarse(Xi[t][v], Mb) for v in range(n))
                        if t == f1 or FB[t]:
                            if ch: bad("FLATALL", t)
                        elif ch: bad("NJB", t)
                    for t in range(f1 + 1, fN + 1):  # MINSET guide (P-N5-NJB §2): Mn_t = free exits whose o ⊕ Ξ has θ's COARSE_M
                        th = sox.coarse(Xi[t][o], Mb)  # (min over states f1+1 .. fN as minset.py; absorptions at non-fallback t < fN)
                        Mn = [x for x in set(g.succ[o]) if x != o and x not in R[t] and sox.coarse(E.extend(o, Xi[t][x]), Mb) == th]
                        minmn = min(minmn, len(Mn))
                        if FB[t] or t == fN: continue
                        ab = [x for x in Mn if x in R[t + 1]]
                        mnabs += len(ab)
                        if len(Mn) == 1 and ab: soleabs += 1
                    rel = set()
                    for t in fbs[bi:bj]:
                        rel |= {x for x in set(g.succ[o]) if x != o and x in R[t] and x not in R[t + 1]}
                        nrel += len({x for x in set(g.succ[o]) if x != o and x in R[t] and x not in R[t + 1]})
                    for t in range(f1, fN):
                        for x in rel:
                            if x not in R[t] and x in R[t + 1] and not FB[t]: reabs_ += 1
                bi = bj + 1
            for k0, k1 in zip(fbs, fbs[1:]):
                L = M(k0)
                if not all(lev(Xi[t][o], Wv[t][o]) > L for t in range(k0 + 1, k1 + 1)): continue
                absl_checked += 1; cnt = 0
                for t in range(k0 + 1, k1):
                    if lev(Xi[t][o], Xi[t + 1][o]) <= L: continue
                    cnt += 1; x0, x1 = sb[t][o], sb[t + 1][o]
                    if x0 == x1 or not (lev(Xi[t][o], Xi[t + 1][o]) == lev(Xi[t][x0], Xi[t][x1]) == eo[t][1] > L): bad("ABSL_i", t)
                    if x0 in R[t] or x0 not in R[t + 1]: bad("ABSL_ii", t)
                    if any(x0 not in R[u] for u in range(t + 1, k1 + 1)): bad("ABSL_iii", t)
                if cnt > d_o - 1: bad("ABSL_cnt", k0)
            k = j + 1
        rows.append(dict(a=a, b=b, T=b - a + 1, X=X, XSN=XSN, REL=REL, RELe=RELe, f=f, eps=len(eps), epsSN=epsSN, maxseg=maxseg, maxpost=maxpost, maxpre=maxpre,
                         absl=absl_checked, d_o=d_o, nblocks=nblocks, blockfb=blockfb, blkrel=nrel, reabs=reabs_, minmn=minmn, mnabs=mnabs, soleabs=soleabs))
    return dict(n=n, o=o, it=len(FB), fb=sum(FB), rows=rows, C=C, ex=ex)

if __name__ == "__main__":
    tot = {}; mx = {}
    for f in sys.argv[1:]:
        g = sox.load(f)
        if len(sox.oddchoice(g)) != 1: print(os.path.basename(f), "SKIP not C^1O"); continue
        r = analyse(g); rs = r["rows"]
        m = {k: max((x[k] for x in rs), default=0) for k in ("X", "XSN", "REL", "RELe", "f", "eps", "epsSN", "maxseg", "maxpost", "maxpre", "absl", "nblocks", "blockfb", "blkrel", "reabs", "mnabs", "soleabs")}
        for k, v in m.items():
            if v > mx.get(k, (0,))[0]: mx[k] = (v, os.path.basename(f))
        print(os.path.basename(f), f"n {r['n']} o {r['o']} it {r['it']} fb {r['fb']} phases {len(rs)} max", m, "FAILS", r["C"] or 0, r["ex"] or "", flush=True)
        for k, v in r["C"].items(): tot[k] = tot.get(k, 0) + v
        tot["files"] = tot.get("files", 0) + 1; tot["phases"] = tot.get("phases", 0) + len(rs)
        for x in rs: tot["eps"] = tot.get("eps", 0) + x["eps"]; tot["epsSN"] = tot.get("epsSN", 0) + x["epsSN"]; tot["absl"] = tot.get("absl", 0) + x["absl"]
    print("TOTAL", tot); print("MAX", mx)
