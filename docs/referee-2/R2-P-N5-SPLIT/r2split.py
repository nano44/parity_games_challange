#!/usr/bin/env python3
"""REFEREE-2 successor 36: own replay of packet P-N5-SPLIT (L-NEW 67, claude/l-new 399cda07) on HOW3(G). Shares no code with L-NEW,
L-RED, REFEREE or L-SI: Γ3 builder, SPEC S1, VJ values / order, S3 and N5′-xi's S4a are REFEREE-2's own R2-P-N5-END/r2end.py
(successor 34); the xi stepping loop is R2-P-N5-CHAIN/r2chain.py's (successor 35), copied so that every state can be inspected.
Counters are written from the packet's TEXT (not from split199.py). Unit in brackets. Every «...fail» counter must be 0.
  §1   entfail   [change] top of E_(t-1)(v) Δ E_t(v) not in E_t(v) (a top must ENTER)
  §2   playfail  [change] plays P_(t-1)(v), P_t(v) equal;   prefail [change] plays differ before the first departure u
       kindfail  [change] u not (a mover whose σ changed, or a gate whose σ̄ changed)                       SPLIT (i)
       hwfail    [change, mover u] not Ω_(t-1)(new) ▷ Ω_(t-1)(old)                                           SPLIT (ii)
       gtfail    [change, gate u] not (Ω_(t-1)(old) ◁ Ω_(t-1)(new) and Ω_t(new) ◁ Ω_t(old))                  SPLIT (iii)
       trfail    [change] Λ_(t-1)(u) ≠ w or Λ_t(u) ≠ w or Δ(v) ≠ Δ(u)                                        TRANSFER (iv)
  §3/4 couples = same-pair y-tops t < t′ of (v, I, y), ALL such pairs (PAIR-SPLIT); rewins = those consecutive among y's tops (REWIN)
       abfail    [couple] a := nx_(t′-1)(u) = b
       psa       [couple] not Ω_(t′-1)(a) ▷ Ω_t(b)                                                         (a) / (a′)
       psb       [couple] not (Ω_(t′-1)(b) ▷ Ω_(t′-1)(a) and Ω_(t′-1)(b) ▷ Ω_t(b))                         (b) / (b′)
       psc       [couple] not E_t′(b) ∩ U_y >lex E_t(b) ∩ U_y                                              (c) / (c′)
       lamb      [y-top] Λ_t(b) ≠ w;  lamm [y-top] Λ_t(wt(y)) ≠ w (wt(y) = y's successor)
       spfail    [(v,I,y)] c_y > Σ_(u,b) Dhi_y(b, J_b)  (J_b = b's Λ-interval holding the pair's tops, Dhi over ALL of J_b)
       spl3M     [(v,I,y)] #split pairs > 3M;    rcfail [(v,I,y)] c_y > 1 + W + Σ (Dhi_y(b, J_b) − 1)      SPLIT-COUNT / REWIN-COUNT
       decfail   [couple, s = t, t′] E_s(b) ∩ U_y ≠ B_s ⊔ S_s, or y ∉ P_s(b), or y not followed by wt(y)    RW-SHAPE decomposition
       rws1      [couple with S_t = S_t′] B_t′ = ∅                                                         RW-SHAPE(*) (i)
       rws2      [couple with S_t = S_t′, f ∈ B_t′] no q strictly between f and y on P_t′(b) with nx changed  RW-SHAPE(*) (ii)
       rw1fail   [couple, t′-step single-split before y on P_t′(v)] S_t = S_t′                              RW-1
  §5   ph_a [(v,I,y)] c_y > Dhi_y(v,I);  ph_c [(v,I,y)] Dhi_y ≠ 1 + Σ_(z∈U_y) c_z;  ph_b [(v,I,x,y)] A_xy > 2·Dhi_y + 1
       rafail [gap] most relevant top of a gap between consecutive y-tops not in U_y (or gap empty);  rpfail [(v,I,y)] c_y > P(y)
  §6   rptfail [(v,I)] two equal consecutive tops;  recfail [(v,I)] D_I > 1 + Mact_I + Rtop_I;  dmon [(v,I)] D_I ≠ 1 + #changes
       pcfail [(v,I)] |tops| > 1 + Σ_(x<y) max(0, A_xy − 1)
       bdfail [run] T3 > any of the RE-EQUIV / ALT-EQUIV / C-EQUIV bounds, or Rtop > n3·T3, or A > max(1, T3), or C > max(1, T3)
  §7   awa / awb / awc / awd [(t, v, ascent)] ASC-WIT (a) / (b) / (c) / (d);  awmv [(t,v,ascent)] successor of c_i not a mover
       rootfail  [(t, v) with an ascent] no gate g* with lev(g*) < lev(c_i), σ̄(g*) = pβ, Ω(pe) ▷ Ω(pβ), reward(Λ(pe)) > reward(Λ(v))
  DEAD (§8), counted with the packet's units: d1 [rewin] no vertex of P_t2(b) changes Λ or an e-letter less relevant than y between
       t1 and t2 − 1 (endpoints);  d2 [consecutive y-tops] E(wt(y)) ∩ U_y one value on [t1, t2];  d3 [(v,I,y)] c_y > #values of
       E(wt(y)) ∩ U_y on [first, last y-top];  d4 [y-top] a U_y-letter on P_t(v) from u to y;  d5 [(v,I,y)] Pre (U_y-letters before y
       on P_t(v) at the y-tops) not lex-nondecreasing;  d6 [rewin] E(wt(y)) ∩ U_y one value on [t1, t2] (= RW-WT fails), d6m: of those,
       multi-split;  maxRA (max |RA(y)|), maxC, maxSPL, maxW, maxDep (longest RA chain).
--ctrl K : K = neg (every must-0 condition negated: each fires wherever its unit occurs), K = U0 (U_y := ∅: psc, spfail must fire),
           K = how (Howard order reversed in hwfail), K = root (rootfail demands lev(g*) < 0).
Usage: r2split.py [--ctrl K] [--gen COUNT SEED KIND]... [--mut COUNT SEED FILE]... FILES..."""
import sys, json, random, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2-P-N5-END"))
import r2end as R
from collections import defaultdict

def howrun(G):
    """N5′-xi from S3 on Γ3(G) (r2chain.py's loop): returns g, od and the pre-fallback states (val, sbar, sig)."""
    g = R.build(G, "lev"); n, pr, ow, E, V = g["n"], g["pr"], g["ow"], g["E"], g["V"]
    od = R.Order(pr); dpr, dow = R.dual(pr, ow); dod = R.Order(dpr)
    st = R.s3(g); sig = [st[v] if ow[v] == 0 else None for v in range(n)]; tau = [st[v] if ow[v] == 1 else None for v in range(n)]
    it = 0; F = None; hist = []
    while True:
        val, sbar = R.s1(pr, ow, E, sig, od)
        Is = {v: [w for w in E[v] if w != sig[v] and od.cmp(val[w], val[sig[v]]) > 0] for v in range(n) if ow[v] == 0}
        Is = {v: l for v, l in Is.items() if l}
        dval, tbar = R.s1(dpr, dow, E, tau, dod)
        It = {v: [w for w in E[v] if w != tau[v] and dod.cmp(dval[w], dval[tau[v]]) > 0] for v in range(n) if ow[v] == 1}
        It = {v: l for v, l in It.items() if l}
        if F is None: hist.append((val, sbar, list(sig)))
        if not Is and not It: break
        it += 1
        if it > 100000: raise RuntimeError("cap")
        snew = list(sig); tnew = list(tau)
        if Is:
            A = {v: sorted(set([sig[v]] + Is.get(v, []))) if ow[v] == 0 else None for v in range(n)}
            HE = [A[v] if ow[v] == 0 else [tau[v]] for v in range(n)]
            _, hch = R.s1(dpr, dow, HE, tau, dod)
            for v in range(n):
                if ow[v] == 0: snew[v] = hch[v] if hch[v] is not None else HE[v][0]
            fx = [None if ow[v] == 0 else tau[v] for v in range(n)]; ch0 = [v for v in range(n) if ow[v] == 0]
            fw, W = R.one_player_opt(od, HE, fx, ch0, sig)
            for v in ch0:
                if len(A[v]) >= 2 and W[v][0] != v:
                    TIE = [w for w in A[v] if R.oplus(od, v, W[w]) == W[v]]
                    best = [w for w in TIE if all(od.cmp(val[w], val[u]) >= 0 for u in TIE)]
                    snew[v] = snew[v] if snew[v] in best else max(best)
        if It:
            HE2 = [[sig[v]] if ow[v] == 0 else sorted(set([tau[v]] + It.get(v, []))) for v in range(n)]
            _, hc2 = R.s1(pr, ow, HE2, sig, od)
            for v in range(n):
                if ow[v] == 1: tnew[v] = hc2[v]
        isfb = snew == sig and tnew == tau
        if isfb:
            if F is None: F = it
            if Is:
                for v, l in Is.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = od.cmp(val[w], val[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    snew[v] = bw
            else:
                for v, l in It.items():
                    bw = l[0]
                    for w in l[1:]:
                        c = dod.cmp(dval[w], dval[bw])
                        if c > 0 or (c == 0 and w > bw): bw = w
                    tnew[v] = bw
        sig, tau = snew, tnew
    return g, od, hist

KEYS = ["runs", "changes", "ytops", "couples", "rewins", "entfail", "playfail", "prefail", "kindfail", "hwfail", "gtfail", "trfail", "abfail", "psa",
        "psb", "psc", "rw_psa", "rw_psb", "rw_psc", "lamb", "lamm", "spfail", "spl3M", "rcfail", "decfail", "rws1", "rws2", "Seq", "rw1fail", "ph_a",
        "ph_b", "ph_c", "rafail", "rpfail", "rptfail", "recfail", "dmon", "pcfail", "bdfail", "awa", "awb", "awc", "awd", "awmv", "rootfail",
        "ascents", "d1", "d2", "d3", "d4", "d5", "d6", "d6m", "maxRA", "maxC", "maxSPL", "maxW", "maxDep", "maxT3"]
MAXK = ("maxRA", "maxC", "maxSPL", "maxW", "maxDep", "maxT3")

def analyse(G, C, ctrl=None):
    X = ctrl == "neg"
    g, od, hist = howrun(G)
    n, pr, ow, V, O, N, M = g["n"], g["pr"], g["ow"], g["V"], g["O"], g["N"], g["M"]
    nm = {i: k for k, i in V.items()}; EX = C.setdefault("_ex", {})
    def ex(key, *t):
        if key not in EX: EX[key] = tuple(nm.get(q, q) if isinstance(q, int) and q >= 0 and not isinstance(q, bool) else q for q in t)
    rk = od.rank; T3 = len(hist) - 1; C["runs"] += 1; C["maxT3"] = max(C["maxT3"], T3)
    movers = {V[("x", x)] for x in range(N)}; gates = {V[("g", o)]: o for o in O}
    evs = frozenset(V[("e", o)] for o in O); elev = {V[("e", o)]: G["lev"][o[0]] for o in O}
    VAL = [h[0] for h in hist]; SB = [h[1] for h in hist]; SG = [h[2] for h in hist]
    f = [[SG[t][v] if ow[v] == 0 else SB[t][v] for v in range(n)] for t in range(T3 + 1)]
    Lm = [[VAL[t][v][0] for v in range(n)] for t in range(T3 + 1)]
    Es = [[frozenset(VAL[t][v][1]) & evs for v in range(n)] for t in range(T3 + 1)]
    cmp = od.cmp
    pc = {}
    def play(t, v):
        k = (t, v)
        if k not in pc:
            seq = []; seen = set(); u = v
            while u not in seen: seen.add(u); seq.append(u); u = f[t][u]
            pc[k] = seq
        return pc[k]
    def U(y): return set() if ctrl == "U0" else {e for e in evs if rk[e] > rk[y]}
    def lexgt(S, T):      # S >lex T
        d = S ^ T
        return bool(d) and max(d, key=lambda u: rk[u]) in S
    def lexge(S, T): return S == T or lexgt(S, T)
    def F(cond): return bool(cond) != X       # must-0 condition (negated under --ctrl neg)
    def rew(c): return od.rew[c]
    # Λ-intervals of every vertex
    ivs = []
    for v in range(n):
        iv = []; s = 0
        for t in range(1, T3 + 2):
            if t == T3 + 1 or Lm[t][v] != Lm[s][v]: iv.append((s, t - 1)); s = t
        ivs.append(iv)
    def ivof(v, t):
        for (a, b) in ivs[v]:
            if a <= t <= b: return (a, b)
    Rtop = 0; Amax = 1; Cmax = 0
    pairs_seen = 0
    for v in range(n):
        for (a, b_) in ivs[v]:
            w = Lm[a][v]; tops = []      # (t, y, u, new)
            for t in range(a + 1, b_ + 1):
                if Es[t - 1][v] == Es[t][v]: continue
                C["changes"] += 1; d = Es[t - 1][v] ^ Es[t][v]; y = max(d, key=lambda u: rk[u])
                if F(y not in Es[t][v]): C["entfail"] += 1
                P0, P1 = play(t - 1, v), play(t, v); u = None
                for i, q in enumerate(P1):
                    if i >= len(P0) or P0[i] != q: C["prefail"] += 1; break
                    if f[t - 1][q] != f[t][q]: u = q; break
                if u is None:
                    C["playfail"] += 1; continue
                old, new = f[t - 1][u], f[t][u]
                ismov = u in movers and SG[t - 1][u] != SG[t][u]; isgate = u in gates and SB[t - 1][u] != SB[t][u]
                if F(not (ismov or isgate)): C["kindfail"] += 1
                if ismov:
                    c0 = cmp(VAL[t - 1][new], VAL[t - 1][old])
                    if F(not (c0 < 0 if ctrl == "how" else c0 > 0)): C["hwfail"] += 1
                if isgate and F(not (cmp(VAL[t - 1][old], VAL[t - 1][new]) < 0 and cmp(VAL[t][new], VAL[t][old]) < 0)): C["gtfail"] += 1
                if F(Lm[t - 1][u] != w or Lm[t][u] != w or d != (Es[t - 1][u] ^ Es[t][u])): C["trfail"] += 1
                tops.append((t, y, u, new))
            # ---- per (v, I)
            seq = [y for (_, y, _, _) in tops]
            if any(F(seq[i] == seq[i + 1]) for i in range(len(seq) - 1)): C["rptfail"] += 1
            vals = [Es[t][v] for t in range(a, b_ + 1)]
            DI = len(set(vals))
            if F(DI != 1 + len(tops)): C["dmon"] += 1
            Mact = len(frozenset().union(*vals))
            rti = 0
            for (t, y, _, _) in tops:
                if any(y in Es[s][v] for s in range(a, t - 1)): rti += 1
            Rtop += rti
            if F(DI > 1 + Mact + rti): C["recfail"] += 1
            letters = sorted(set(seq), key=lambda u: rk[u])
            cy = {y: seq.count(y) for y in letters}
            Cmax = max([Cmax] + list(cy.values()))
            def alt(x, y):
                r = [z for z in seq if z in (x, y)]; return sum(1 for i in range(len(r)) if i == 0 or r[i] != r[i - 1])
            A = {}
            for i, x in enumerate(letters):
                for y in letters[i + 1:]: A[(x, y)] = alt(x, y); Amax = max(Amax, A[(x, y)])
            if F(len(seq) > 1 + sum(max(0, A[p] - 1) for p in A)): C["pcfail"] += 1
            Dhi = {y: len({vv & U(y) for vv in vals}) for y in letters}
            for y in letters:
                if F(cy[y] > Dhi[y]): C["ph_a"] += 1
                if F(Dhi[y] != 1 + sum(cy[z] for z in letters if z in U(y))): C["ph_c"] += 1
            for (x, y), Axy in A.items():     # y more relevant than x (letters sorted by relevance)
                if F(Axy > 2 * Dhi[y] + 1): C["ph_b"] += 1
            # RA
            RA = {}
            for y in letters:
                ts = [i for i, z in enumerate(seq) if z == y]; RA[y] = set()
                for i1, i2 in zip(ts, ts[1:]):
                    gap = seq[i1 + 1:i2]
                    z = max(gap, key=lambda u: rk[u]) if gap else None
                    if F(z is None or z not in U(y)): C["rafail"] += 1
                    if z is not None: RA[y].add(z)
                C["maxRA"] = max(C["maxRA"], len(RA[y]))
            Pp = {}; dep = {}
            for y in reversed(letters):
                Pp[y] = 1 + sum(Pp.get(z, 0) for z in RA[y]); dep[y] = 1 + max([dep.get(z, 0) for z in RA[y]] + [0])
                if F(cy[y] > Pp[y]): C["rpfail"] += 1
                C["maxDep"] = max(C["maxDep"], dep[y])
            # ---- per (v, I, y): splits, couples, DEAD
            for y in letters:
                Uy = U(y); yt = [(t, u, b) for (t, z, u, b) in tops if z == y]; C["ytops"] += len(yt)
                m = f[0][y]   # e-vertex: one successor, frozen
                byp = defaultdict(list)
                for (t, u, b) in yt:
                    byp[(u, b)].append(t)
                    if F(Lm[t][b] != w): C["lamb"] += 1
                    if F(Lm[t][m] != w): C["lamm"] += 1
                    P = play(t, v)
                    if u in P and y in P and P.index(u) < P.index(y) and any(q in Uy for q in P[P.index(u):P.index(y)]): C["d4"] += 1; ex("d4", "v", v, "t", ("state", t), "y", y, "u", u)
                C["maxC"] = max(C["maxC"], len(yt)); C["maxSPL"] = max(C["maxSPL"], len(byp))
                if F(len(byp) > 3 * M): C["spl3M"] += 1
                sumD = 0; sumD1 = 0
                for (u, b), ts in byp.items():
                    J = ivof(b, ts[0])
                    Db = len({Es[s][b] & Uy for s in range(J[0], J[1] + 1)}); sumD += Db; sumD1 += Db - 1
                Wc = sum(1 for i in range(len(yt) - 1) if (yt[i][1], yt[i][2]) != (yt[i + 1][1], yt[i + 1][2]))
                C["maxW"] = max(C["maxW"], Wc)
                if F(len(yt) > sumD): C["spfail"] += 1
                if F(len(yt) > 1 + Wc + sumD1): C["rcfail"] += 1
                # DEAD D2, D3, D5
                for i in range(len(yt) - 1):
                    t1, t2 = yt[i][0], yt[i + 1][0]
                    if len({Es[s][m] & Uy for s in range(t1, t2 + 1)}) < 2: C["d2"] += 1; ex("d2", "v", v, "y", y, "wt", m, "t1", ("state", t1), "t2", ("state", t2))
                if yt and len(yt) > len({Es[s][m] & Uy for s in range(yt[0][0], yt[-1][0] + 1)}): C["d3"] += 1
                pre = []
                for (t, u, b) in yt:
                    P = play(t, v); pre.append(frozenset(q for q in P[:P.index(y)] if q in Uy))
                if any(not lexge(q2, q1) for q1, q2 in zip(pre, pre[1:])): C["d5"] += 1
                # couples (all same-pair t < t′)
                cons = {(yt[i][0], yt[i + 1][0]) for i in range(len(yt) - 1) if (yt[i][1], yt[i][2]) == (yt[i + 1][1], yt[i + 1][2])}
                for (u, b), ts in byp.items():
                    for i in range(len(ts)):
                        for j in range(i + 1, len(ts)):
                            t, t2 = ts[i], ts[j]; isrw = (t, t2) in cons
                            C["couples"] += 1; C["rewins"] += isrw
                            aa = f[t2 - 1][u]
                            if F(aa == b): C["abfail"] += 1
                            if aa == b: continue
                            ca = F(not cmp(VAL[t2 - 1][aa], VAL[t][b]) > 0)
                            cb = F(not (cmp(VAL[t2 - 1][b], VAL[t2 - 1][aa]) > 0 and cmp(VAL[t2 - 1][b], VAL[t][b]) > 0))
                            cc = F(not lexgt(Es[t2][b] & Uy, Es[t][b] & Uy))
                            C["psa"] += ca; C["psb"] += cb; C["psc"] += cc
                            if isrw: C["rw_psa"] += ca; C["rw_psb"] += cb; C["rw_psc"] += cc
                            # RW-SHAPE decomposition and (i), (ii)
                            BS = {}
                            for s in (t, t2):
                                Pb = play(s, b)
                                if y not in Pb or Pb.index(y) + 1 >= len(Pb) or Pb[Pb.index(y) + 1] != m:
                                    C["decfail"] += 1; BS = None; break
                                Bs = frozenset(q for q in Pb[:Pb.index(y)] if q in Es[s][b] and q in Uy); Ss = Es[s][m] & Uy
                                if F((Bs | Ss) != (Es[s][b] & Uy) or (Bs & Ss)): C["decfail"] += 1
                                BS[s] = (Bs, Ss)
                            if BS is None: continue
                            Pv = play(t2, v); before = Pv[:Pv.index(y)]
                            single = [q for q in before if f[t2 - 1][q] != f[t2][q]] == [u]
                            if BS[t][1] == BS[t2][1]:
                                C["Seq"] += 1
                                if F(single): C["rw1fail"] += 1
                                if F(not BS[t2][0]): C["rws1"] += 1
                                Pb = play(t2, b); iy = Pb.index(y)
                                for fq in BS[t2][0]:
                                    i0 = Pb.index(fq)
                                    if F(not any(f[t2 - 1][q] != f[t2][q] for q in Pb[i0 + 1:iy])): C["rws2"] += 1
                            if isrw:
                                if len({Es[s][m] & Uy for s in range(t, t2 + 1)}) < 2:
                                    C["d6"] += 1; C["d6m"] += not single; ex("d6", "v", v, "u", u, "b", b, "y", y, "wt", m, "t", ("state", t), "t2", ("state", t2), "Ewt", tuple(nm[q] for q in BS[t][1]), tuple(nm[q] for q in BS[t2][1]), "Eb", tuple(nm[q] for q in Es[t][b] & Uy), tuple(nm[q] for q in Es[t2][b] & Uy))
                                lo = {e for e in evs if rk[e] < rk[y]}
                                if not any(Lm[t][q] != Lm[t2 - 1][q] or ((Es[t][q] ^ Es[t2 - 1][q]) & lo) for q in play(t2, b)): C["d1"] += 1; ex("d1", "v", v, "y", y, "t1", ("state", t), "t2", ("state", t2), "u", u, "b", b)
    # ---- run bounds (§6)
    L3 = (M + 1) * (2 * M + 1) * (N + 1) + N * (n - 1)
    from math import comb
    b1 = (1 + n * ((2 * M + 3) * (M + 1) - 1) + Rtop) * (L3 + 1)
    b2 = (1 + n * ((2 * M + 3) * (2 + comb(M, 2) * (Amax - 1)) - 1)) * (L3 + 1)
    b3 = (1 + n * ((2 * M + 3) * (1 + M * Cmax) - 1)) * (L3 + 1)
    if F(T3 > min(b1, b2, b3) or Rtop > n * T3 or Amax > max(1, T3) or Cmax > max(1, T3)): C["bdfail"] += 1
    # ---- §7 ASC-WIT / ASC-ROOT, every state and vertex
    for t in range(T3 + 1):
        for v in range(n):
            w = Lm[t][v]; P = play(t, v); sq = [q for q in P if q in Es[t][v]]
            first = True
            for i in range(len(sq) - 1):
                if rk[sq[i + 1]] <= rk[sq[i]]: continue
                C["ascents"] += 1; ci = sq[i]; y = f[t][ci]
                if F(y not in movers): C["awmv"] += 1
                if y not in movers: continue
                g1 = f[t][f[t][y]]; o = gates.get(g1)
                pe, pB = V[("pe", o)], V[("pB", o)]
                if F(SB[t][g1] != pB): C["awa"] += 1
                if F(not cmp(VAL[t][pe], VAL[t][pB]) > 0): C["awb"] += 1
                if Lm[t][pe] == w:
                    if F(not any(rk[e] >= rk[sq[i + 1]] for e in Es[t][pe])): C["awc"] += 1
                elif F(not rew(Lm[t][pe]) > rew(w)): C["awd"] += 1
                if first:
                    first = False; lim = -1 if ctrl == "root" else elev[ci]
                    ok = any(G["lev"][oo[0]] < lim and SB[t][gv] == V[("pB", oo)] and cmp(VAL[t][V[("pe", oo)]], VAL[t][V[("pB", oo)]]) > 0
                             and rew(Lm[t][V[("pe", oo)]]) > rew(w) for gv, oo in gates.items())
                    if F(not ok): C["rootfail"] += 1
    return T3

def mutate(rng, G0):
    """Own mutation of a genome: 1-4 random edits among (Ξ-target of an option := any mover or none), (W-target := another mover one level
    down), (swap two β ranks), (flip a β parity bit), (start option of a mover). The result is a genome in R104's sense (levels kept)."""
    G = json.loads(json.dumps(G0)); N = G["N"]; lev = G["lev"]
    byl = {}
    for x in range(N): byl.setdefault(lev[x], []).append(x)
    O = [(x, k) for x in range(N) for k in range(len(G["opts"][x]))]
    for _ in range(rng.randint(1, 4)):
        r = rng.randrange(5); x, k = rng.choice(O); op = G["opts"][x][k]
        if r == 0: op[1] = rng.choice([-1] + list(range(N)))
        elif r == 1 and lev[x] > 0: op[0] = rng.choice(byl[lev[x] - 1])
        elif r == 2:
            i, j = rng.randrange(len(G["br"])), rng.randrange(len(G["br"])); G["br"][i], G["br"][j] = G["br"][j], G["br"][i]
        elif r == 3: b = op[2]; G["bp"][b] = 1 - G["bp"][b]
        else: G["start"][x] = rng.randrange(len(G["opts"][x]))
    return G

def main(a):
    gens, files, muts, ctrl, i = [], [], [], None, 0
    while i < len(a):
        if a[i] == "--gen": gens.append((int(a[i + 1]), int(a[i + 2]), a[i + 3])); i += 4
        elif a[i] == "--ctrl": ctrl = a[i + 1]; i += 2
        elif a[i] == "--mut": muts.append((int(a[i + 1]), int(a[i + 2]), a[i + 3])); i += 4
        else: files.append(a[i]); i += 1
    Gs = []
    for fn in files:
        G = json.load(open(fn))
        if isinstance(G, dict) and "genome" in G: G = G["genome"]
        if not (isinstance(G, dict) and "opts" in G and "start" in G): print(os.path.basename(fn), "skipped (not a genome)"); continue
        Gs.append((os.path.basename(fn), G))
    for cnt, seed, fn in muts:
        G0 = json.load(open(fn)); G0 = G0["genome"] if "genome" in G0 else G0; rng = random.Random(seed)
        Gs += [(f"gen-mut{seed}-{os.path.basename(fn)}#{j}", mutate(rng, G0)) for j in range(cnt)]
    for cnt, seed, kind in gens:
        rng = random.Random(seed); Gs += [(f"gen{kind}{seed}#{j}", R.gen(rng, kind)) for j in range(cnt)]
    tot = {k: 0 for k in KEYS}
    for name, G in Gs:
        C = {k: 0 for k in KEYS}; T3 = analyse(G, C, ctrl)
        for k in KEYS: tot[k] = max(tot[k], C[k]) if k in MAXK else tot[k] + C[k]
        if not name.startswith("gen"):
            print(name, "T3", T3, " ".join(f"{k} {C[k]}" for k in KEYS if C[k] and k not in ("runs",)), flush=True)
            for k2, e2 in sorted(C.get("_ex", {}).items()): print("   first", k2, e2)
    print("TOTAL" + (f" CTRL {ctrl}" if ctrl else "") + ": " + " ".join(f"{k} {tot[k]}" for k in KEYS), flush=True)

if __name__ == "__main__":
    main(sys.argv[1:])
