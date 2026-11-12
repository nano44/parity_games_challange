#!/usr/bin/env python3
"""REFEREE-2 successor 37: own replay of packet P-N5-GATE (L-SI, claude/l-si 4066f579 + fixes 9c0349b1) on BOTH runs it names:
  g3  : Γ3(G), N5′-xi from S3 until its first fallback (HOW3) — REFEREE-2's R2-P-N5-SPLIT/r2split.howrun on R2-P-N5-END/r2end.py
  cyc : IDEAL-CYC(G) on Γ(G), Howard at the movers (keep σ(x) unless strictly better; else the largest best option) — REFEREE-2's
        R2-P-ACYC/r2acyc.py (builder, VJ values, Odd's optimum), loop as R2-P-N5-QN/r2qn.py.
No lane code is imported (no gamma3, n5v, n5x, eg195, own.py, si.py, gate92 / mult91 / np93 / lev94 / astar92).
Counters: unit in brackets; every «…fail» must be 0; «rec_…» are records; «n_…» count the cases a lemma was applied to.
  §3.1 grfail   [flip]  o flips p→q at t and Ω_t(p) = Ω_(t−1)(p)                                   GATE-RACE (a)
       gr2fail  [gate]  flips(o) > min(ch_p + ch_q, 2·min(ch_p, ch_q) + 1)                          GATE-RACE (b)
       locfail  [(t, gate)] σ̄_t(o) is not the strictly ◁-smaller face (premise LOC-GATE(3) / NO-TIE(3))
  §3.2 decfail  [(t, gate), LAM ∧ PRIV ∧ e_o ∈ E(p_e)] sign(Ω(p_e) vs Ω(p_b)) ≠ sign(π(E(p_e)) vs π(E(p_b))) or π's equal  (a)
       glnfail  [flip, t−1 and t LAM ∧ PRIV ∧ UP] neither π changes                                         (b)
       gbpfail  [flip, as (b) with the same Λ at t−1, t] relock: π(E(p_e)) not strictly lex-up; unlock: π(E(p_b)) not   (b′)
       rec_k10  [(t, gate)] LAM ∧ PRIV ∧ not UP («K10»; fixes entry 1 G1: empty on IDEAL-CYC by R123 B-ONLY)
  §3.3 npfail   [(t, gate), NP_t] σ̄_t(o) ≠ p_e, or P_t(p_b) ≠ A·o·P_t(p_e), or Λ differ, or E(p_e) ⊄ E(p_b)     NP-SHAPE (a)
       npbfail  [flip] NP at t−1 and t; or NP_(t−1) and not a relock; or NP_t and not an unlock                    (b)
  §3.4 efafail  [gate]  relocks > ch(p_e) or unlocks > 1 + relocks or unlocks > ch(p_b)                     E-FACE-PAYS (a)
       efbfail  [(t, gate), e_o ∉ P_(t−1)(D) ∪ P_t(D)] (Ω(p_e) changes) ≠ (Ω(D) changes)                    (b)
       dpass    [(t, gate)] e_o ∈ P_t(D)   (the PROVISO; fixes entry 2: never on IDEAL-CYC by R123 B-ONLY)
       efcfail  [gate with dpass 0] unlocks > 1 + ch_D, or lam_D > 2M + 2, or ech_D > (2M + 3)·M·C            (c)
       efdfail  [gate]  flips > 2·min(ch_pe, ch_pb) + 1 or > 2·lamch + 2·min(nl) + 1                           (d)
       wqfail   [gate with dpass 0] unlocks > ch_D + 1 or flips > 2·ch_D + 1                                   WAIT-QUIET
  §3.5 ssfail   [(t, o), {t−1, t} satisfies SAME-SUFFIX's hypotheses for some y] the pairwise ⊴-order of o's successors differs
       ssofail  [same, o Odd] σ̄_(t−1)(o) ≠ σ̄_t(o);  ssefail [(t, o) mover, hypotheses on {t−2, t−1, t}] σ_(t−1)(o) ≠ σ_t(o)
       sbfail   [(t, x), Ω_t(x) ≠ Ω_(t−1)(x)] no vertex of P_(t−1)(x) changes successor at t                   STEP-BOUND
  §3.6 parfail  [(b, t, y), y = w or an e-vertex above w, H := E(b) ∩ U_y changes inside a Λ-interval] (i), (ii) or (iii) fails  PARALLEL
  §3.7 pefail   [same-pair expulsion couple (b, J, z, s < s′)] E_s′(b′) ∩ U_z not >lex E_s(b′) ∩ U_z           PAIR-EXPEL
       pe1fail / pe2fail / pe3fail: Steps 1, 2, 3 of the proof;  pekind: split u′ neither a mover nor a gate;  pelam: Λ(b′) ≠ w
       ecfail   [(b, J, z)] a_z(b, J) > 1 + Σ_(u′,b′) Dhi_z(b′, J_b′);  ec3fail [(b, J, z)] more than 3M split pairs   EXPEL-COUNT
  §3.8 cfail    [(v, I, y)] c_y(v, I) > a_y(v, I);  a1fail [run] C > A*_all or A*_all > 1 + M·C (A*-EQUIV (i), my proof)
       a2fail   [route tuple (b, J, y)] Dhi_y(b, J) − 1 > Σ_(x ∈ U_y) a_x(b, J);  a3fail [run] C > 3M·(1 + M·A*_route)
Controls (--ctrl NAME; each must FIRE its counter): gr (GATE-RACE (a) on the entered face q), low (π := letters BELOW e_o),
  np (NP-SHAPE with p_e and p_b swapped), efb (compare p_e with p_b instead of D), ss (order compared on windows that FAIL the
  hypotheses), sb (only x's own successor counts), par ((iii) as «at least 2 after u′»), uz (U_z := ∅ in PAIR-EXPEL),
  ec (EXPEL-COUNT bound without the 1 +), c (c_y ≤ a_y − 1), a2 ((ii)'s per-tuple bound − 1).
Usage: r2gate.py [--eng g3|cyc|both] [--eorder lev|gate] [--ctrl NAME] [--gen COUNT SEED KIND] FILES.json ..."""
import sys, os, json, random
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [os.path.join(H, "..", "R2-P-N5-SPLIT"), os.path.join(H, "..", "R2-P-N5-END"), os.path.join(H, "..", "R2-P-ACYC")]
import r2split as SP
import r2end as RE
import r2acyc as A

CTRL = None
LIMIT = 10 ** 9      # --limit L: runs with more than L vertices get §3.1-§3.4, §3.4 (c) and §3.8 only (n_light counts them)

def run_g3(G):
    g, od, hist = SP.howrun(G)
    n, ow, succ, V = g["n"], g["ow"], g["E"], g["V"]
    states = [([sig[v] if ow[v] == 0 else sbar[v] for v in range(n)], val) for (val, sbar, sig) in hist]
    gates = [(V[("g", o)], V[("pe", o)], V[("pB", o)], V[("e", o)]) for o in g["O"]]
    evs = {V[("e", o)] for o in g["O"]}; movers = {V[("x", x)] for x in range(g["N"])}
    return dict(n=n, succ=succ, owner=ow, rel=od.rank, cmp=od.cmp, states=states, gates=gates, evs=evs, movers=movers, M=g["M"])

def run_cyc(G, cap=3000):
    g = A.build(G, False); vj = A.VJ(g); V = g["V"]; succ = g["succ"]; n = g["n"]; N = g["N"]
    ms = list(G["start"]); states = []
    while True:
        sig = A.mover_sig(g, ms); tau, val = A.odd_opt(g, vj, sig, A.worst_start(g))
        states.append(([sig[v] if g["owner"][v] == 0 else tau[v] for v in range(n)], val))
        new = list(ms); ch = False
        for x in range(N):
            xv = V[("x", x)]; cur = sig[xv]; best = cur
            for w in succ[xv]:
                if vj.cmp(val[w], val[best]) > 0: best = w
            if vj.cmp(val[best], val[cur]) > 0:
                bl = [w for w in succ[xv] if vj.cmp(val[w], val[best]) == 0]; new[x] = succ[xv].index(max(bl)); ch = True
        if not ch or len(states) > cap: break
        ms = new
    gates = [(V[("g", o)], V[("e", o)], V[("b", o)], V[("e", o)]) for o in g["O"]]
    evs = {V[("e", o)] for o in g["O"]}; movers = {V[("x", x)] for x in range(N)}
    return dict(n=n, succ=succ, owner=g["owner"], rel=vj.rel, cmp=vj.cmp, states=states, gates=gates, evs=evs, movers=movers,
                M=g["M"], capped=len(states) > cap)

def analyse(R, C):
    n, succ, owner, rel, cmp, S, gates, evs, movers, M = (R[k] for k in ("n", "succ", "owner", "rel", "cmp", "states", "gates", "evs",
                                                                        "movers", "M"))
    T = len(S) - 1; C["runs"] += 1; C["states"] += T + 1; C["rec_maxT"] = max(C["rec_maxT"], T)
    f = [s[0] for s in S]; val = [s[1] for s in S]
    pc = {}
    def play(t, v):
        k = (t, v)
        if k not in pc:
            P = [v]; seen = {v}
            while True:
                y = f[t][P[-1]]
                if y in seen: break
                P.append(y); seen.add(y)
            pc[k] = P
        return pc[k]
    Lam = lambda t, v: val[t][v][0]
    Ec = {}
    def E(t, v):
        k = (t, v)
        if k not in Ec: Ec[k] = frozenset(u for u in val[t][v][1] if u in evs)
        return Ec[k]
    key = lambda X: sorted((rel[u] for u in X), reverse=True)
    def lexc(X, Y):
        a, b = key(X), key(Y); return (a > b) - (a < b)
    up = lambda X, z: frozenset(u for u in X if rel[u] > rel[z])        # X ∩ U_z
    top = lambda X, Y: max(X ^ Y, key=lambda u: rel[u])
    chg = lambda t, v: val[t][v] != val[t - 1][v]
    multi = [v for v in range(n) if len(succ[v]) > 1]
    # ------------------------------------------------ §3.1-§3.4 per gate
    for (o, pe, pb, eo) in gates:
        D = succ[eo][0]; assert len(succ[eo]) == 1
        flips = rel_ = unl = 0; chp = {pe: 0, pb: 0}; lamch = 0; lamf = {pe: 0, pb: 0}; dp = 0
        chD = lamD = echD = gamD = 0
        for t in range(T + 1):
            # LOC-GATE premise
            a = f[t][o]; b = pb if a == pe else pe
            if cmp(val[t][a], val[t][b]) >= 0: C["locfail"] += 1
            LAM = Lam(t, pe) == Lam(t, pb); PRIV = eo not in E(t, pb); UP = rel[eo] > rel[Lam(t, pe)]
            if LAM and PRIV and not UP: C["rec_k10"] += 1
            if LAM and PRIV and eo in E(t, pe):
                C["n_deca"] += 1
                if CTRL == "low": pi = lambda X: frozenset(u for u in X if rel[u] < rel[eo])
                else: pi = lambda X: frozenset(u for u in X if rel[u] >= rel[eo])
                c1 = cmp(val[t][pe], val[t][pb]); c2 = lexc(pi(E(t, pe)), pi(E(t, pb)))
                if c2 == 0 or c1 != c2: C["decfail"] += 1
            NP = eo in E(t, pb)
            if NP:
                C["n_np"] += 1; x, y = (pb, pe) if CTRL == "np" else (pe, pb)
                Pb, Pe = play(t, y), play(t, x); bad = f[t][o] != x or o not in Pb or Lam(t, x) != Lam(t, y) or not E(t, x) <= E(t, y)
                if not bad and Pb[Pb.index(o) + 1:] != Pe: bad = True
                if bad: C["npfail"] += 1
            if eo in play(t, D): dp += 1; C["dpass"] += 1
            if t == 0: continue
            for p in (pe, pb):
                if chg(t, p): chp[p] += 1
                if Lam(t, p) != Lam(t - 1, p): lamf[p] += 1
            if Lam(t, pe) != Lam(t - 1, pe) or Lam(t, pb) != Lam(t - 1, pb): lamch += 1
            if chg(t, D):
                chD += 1
                if Lam(t, D) != Lam(t - 1, D): lamD += 1
                elif E(t, D) != E(t - 1, D): echD += 1
                else: gamD += 1
            # (b) of E-FACE-PAYS
            if eo not in play(t - 1, D) and eo not in play(t, D):
                C["n_efb"] += 1; other = pb if CTRL == "efb" else D
                if chg(t, pe) != chg(t, other): C["efbfail"] += 1
            if f[t][o] != f[t - 1][o]:
                flips += 1; p, q = f[t - 1][o], f[t][o]
                if q == pb: rel_ += 1
                else: unl += 1
                if not chg(t, q if CTRL == "gr" else p): C["grfail"] += 1
                NP0, NP1 = eo in E(t - 1, pb), eo in E(t, pb)
                if (NP0 and NP1) or (NP0 and q != pb) or (NP1 and q != pe): C["npbfail"] += 1
                ok = [Lam(s, pe) == Lam(s, pb) and eo not in E(s, pb) and rel[eo] > rel[Lam(s, pe)] for s in (t - 1, t)]
                if all(ok):
                    C["n_glnb"] += 1
                    pi = lambda X: frozenset(u for u in X if rel[u] >= rel[eo])
                    ce = pi(E(t, pe)) != pi(E(t - 1, pe)); cb = pi(E(t, pb)) != pi(E(t - 1, pb))
                    if not (ce or cb): C["glnfail"] += 1
                    if Lam(t, pe) == Lam(t - 1, pe):
                        C["n_glnbp"] += 1; w = pe if q == pb else pb
                        if lexc(pi(E(t, w)), pi(E(t - 1, w))) <= 0: C["gbpfail"] += 1
        C["n_gates"] += 1; C["rec_maxflips"] = max(C["rec_maxflips"], flips)
        chpe, chpb = chp[pe], chp[pb]
        if flips > min(chpe + chpb, 2 * min(chpe, chpb) + 1): C["gr2fail"] += 1
        if rel_ > chpe or unl > 1 + rel_ or unl > chpb: C["efafail"] += 1
        nl = min(chpe - lamf[pe], chpb - lamf[pb])
        if flips > 2 * min(chpe, chpb) + 1 or flips > 2 * lamch + 2 * nl + 1: C["efdfail"] += 1
        R.setdefault("_gate", []).append((o, dp, unl, flips, chD, lamD, echD))
    # ------------------------------------------------ Λ-intervals, changes, tops, splits (for §3.4 (c), §3.6-§3.8)
    ivs = {}                                      # v -> list of (s, e) Λ-intervals
    for v in range(n):
        L = []; s = 0
        for t in range(1, T + 2):
            if t == T + 1 or Lam(t, v) != Lam(s, v): L.append((s, t - 1)); s = t
        ivs[v] = L
        if len(L) > 2 * M + 3: C["cycfail"] += 1
    def iv_of(v, t):
        for (s, e) in ivs[v]:
            if s <= t <= e: return (s, e)
    def split(t, b):                               # first vertex of P_t(b) whose successor differs at t − 1
        for u in play(t, b):
            if f[t][u] != f[t - 1][u]: return u
        return None
    cmax = 0; cy = {}
    for v in range(n):
        for (s, e) in ivs[v]:
            cnt = defaultdict(int)
            for t in range(s + 1, e + 1):
                if E(t, v) != E(t - 1, v):
                    y = top(E(t, v), E(t - 1, v))
                    if y not in E(t, v): C["emonfail"] += 1           # premise E-MON(3): the top enters
                    cnt[y] += 1
            for y, c in cnt.items(): cy[(v, s, y)] = c; cmax = max(cmax, c)
    rc = {}
    def runcnt(b, J):
        if (b, J) not in rc:
            s, e = J; c = defaultdict(int)
            for t in range(s, e + 1):
                for z in (E(t, b) if t == s else E(t, b) - E(t - 1, b)): c[z] += 1
            rc[(b, J)] = c
        return rc[(b, J)]
    runs = lambda b, J, z: runcnt(b, J).get(z, 0)
    Mletters = len(evs)
    for (o, dp, unl, flips, chD, lamD, echD) in R.pop("_gate"):
        if dp == 0:
            if unl > 1 + chD or lamD > 2 * M + 2 or echD > (2 * M + 3) * Mletters * cmax: C["efcfail"] += 1
            if unl > chD + 1 or flips > 2 * chD + 1: C["wqfail"] += 1
    # §3.8 (i) per tuple and A*_all
    Aall = 0
    for (v, s, y), c in cy.items():
        a = runs(v, ivs[v][[i for i, J in enumerate(ivs[v]) if J[0] == s][0]], y)
        if c > a - (1 if CTRL == "c" else 0): C["cfail"] += 1
    for b in range(n):
        for J in ivs[b]:
            c = runcnt(b, J)
            if c: Aall = max(Aall, max(c.values()))
    if cmax > Aall or Aall > 1 + Mletters * cmax: C["a1fail"] += 1
    C["rec_maxC"] = max(C["rec_maxC"], cmax); C["rec_maxAall"] = max(C["rec_maxAall"], Aall)
    # §3.8 (ii): route tuples (b, J_b, y) of the y-tops of every (v, I)
    Aroute = 0; route = set()
    for v in range(n):
        for (s, e) in ivs[v]:
            for t in range(s + 1, e + 1):
                if E(t, v) != E(t - 1, v):
                    y = top(E(t, v), E(t - 1, v)); u = split(t, v)
                    if u is None: continue
                    b = f[t][u]; route.add((b, iv_of(b, t), y))
    for (b, J, y) in route:
        Hs = [up(E(t, b), y) for t in range(J[0], J[1] + 1)]
        dhi = len(set(Hs)); U = {u for u in evs if rel[u] > rel[y]}
        c = runcnt(b, J); rs = [v for x, v in c.items() if x in U]
        if rs: Aroute = max(Aroute, max(rs))
        if dhi - 1 > sum(rs) - (1 if CTRL == "a2" else 0): C["a2fail"] += 1
    if cmax > 3 * M * (1 + Mletters * Aroute): C["a3fail"] += 1
    C["rec_maxAroute"] = max(C["rec_maxAroute"], Aroute)
    if n > LIMIT: C["n_light"] += 1; return
    # ------------------------------------------------ §3.5 STEP-BOUND
    for t in range(1, T + 1):
        chs = {u for u in range(n) if f[t][u] != f[t - 1][u]}
        for x in range(n):
            P = [x] if CTRL == "sb" else play(t - 1, x)          # control: only x's own successor counts
            if chg(t, x) and not any(u in chs for u in P): C["sbfail"] += 1
    # ------------------------------------------------ §3.5 SAME-SUFFIX on windows {t−1, t} (and {t−2, t−1, t} for movers)
    def hyp(o, ts):
        if len({Lam(t, o) for t in ts}) != 1: return None
        f0 = succ[o][0]
        for y in play(ts[-1], f0):
            Pf = {}
            ok = True
            for fs in succ[o]:
                pre = None
                for t in ts:
                    P = play(t, fs)
                    if y not in P: ok = False; break
                    i = P.index(y); pr = tuple(P[:i])
                    if P[i:] != play(t, y): ok = False; break
                    if pre is None: pre = pr
                    elif pre != pr: ok = False; break
                if not ok: break
                Pf[fs] = pre
            if not ok: continue
            allpre = set().union(*[set(p) for p in Pf.values()])
            if any(set(play(t, y)) & allpre for t in ts): continue
            if o in allpre: continue
            return y
        return None
    def order(t, o):
        return tuple(cmp(val[t][a], val[t][b]) for a in succ[o] for b in succ[o])
    for t in range(1, T + 1):
        for o in multi:
            y = hyp(o, (t - 1, t))
            if (y is not None) != (CTRL == "ss"):
                C["n_ss"] += 1
                if order(t - 1, o) != order(t, o): C["ssfail"] += 1
                if owner[o] == 1 and f[t - 1][o] != f[t][o]: C["ssofail"] += 1
            if t >= 2 and o in movers and CTRL != "ss" and hyp(o, (t - 2, t - 1, t)) is not None:
                C["n_sse"] += 1
                if f[t - 1][o] != f[t][o]: C["ssefail"] += 1
    # ------------------------------------------------ §3.6 PARALLEL and §3.7 PAIR-EXPEL / EXPEL-COUNT
    for b in range(n):
        for (s0, e0) in ivs[b]:
            w = Lam(s0, b)
            letters = [w]          # y = w implies every y ≻ w: when H_y changes its top is the top x of E's change, and Z_y ⊆ Z_w
            for t in range(s0 + 1, e0 + 1):
                if E(t, b) == E(t - 1, b): continue
                u1 = split(t, b); P1, P0 = play(t, b), play(t - 1, b)
                for y in letters:
                    H0, H1 = up(E(t - 1, b), y), up(E(t, b), y)
                    if H0 == H1: continue
                    C["n_par"] += 1; x = top(H0, H1); Z = H0 - H1; bad = False
                    if x not in P1 or x in P0: bad = True
                    for z in Z:
                        if z not in P0 or z in P1 or rel[z] >= rel[x]: bad = True
                    sh = 1 if CTRL == "par" else 0                      # control: «at least 2 after u′»
                    if u1 is None: bad = True
                    elif not bad:
                        i0, i1 = P0.index(u1) if u1 in P0 else -1, P1.index(u1) if u1 in P1 else -1
                        if i0 < 0 or i1 < 0 or P1.index(x) <= i1 + sh or any(P0.index(z) <= i0 + sh for z in Z): bad = True
                    if bad: C["parfail"] += 1
            # expulsions of every letter z from E(b) on this interval, by split pair
            exp = defaultdict(lambda: defaultdict(list))
            for t in range(s0 + 1, e0 + 1):
                for z in E(t - 1, b) - E(t, b):
                    u1 = split(t, b)
                    if u1 is None: C["pekind"] += 1; continue
                    if u1 not in movers and owner[u1] != 1: C["pekind"] += 1
                    exp[z][(u1, f[t][u1])].append(t)
            for z, byp in exp.items():
                Uz = (lambda X: frozenset()) if CTRL == "uz" else (lambda X, z=z: up(X, z))
                bound = 0
                if len(byp) > 3 * M: C["ec3fail"] += 1
                for (u1, b1), ts in byp.items():
                    for i in range(len(ts)):
                        for j in range(i + 1, len(ts)):
                            s, s2 = ts[i], ts[j]; C["n_pe"] += 1; a1 = f[s2 - 1][u1]
                            if any(Lam(r, b1) != w for r in range(s, s2 + 1)): C["pelam"] += 1
                            if cmp(val[s2 - 1][a1], val[s][b1]) <= 0: C["pe1fail"] += 1
                            if lexc(Uz(E(s2 - 1, a1)), Uz(E(s, b1))) < 0: C["pe2fail"] += 1
                            if lexc(Uz(E(s2, b1)), Uz(E(s2 - 1, a1))) <= 0: C["pe3fail"] += 1
                            if lexc(Uz(E(s2, b1)), Uz(E(s, b1))) <= 0: C["pefail"] += 1
                    Jb = iv_of(b1, ts[0])
                    if any(iv_of(b1, t) != Jb for t in ts): C["pelam"] += 1
                    bound += len({up(E(t, b1), z) for t in range(Jb[0], Jb[1] + 1)})
                C["n_ec"] += 1
                if runs(b, (s0, e0), z) > (0 if CTRL == "ec" else 1) + bound: C["ecfail"] += 1

FAILS = ["locfail", "grfail", "gr2fail", "decfail", "glnfail", "gbpfail", "npfail", "npbfail", "efafail", "efbfail", "dpass", "efcfail",
         "efdfail", "wqfail", "ssfail", "ssofail", "ssefail", "sbfail", "parfail", "pefail", "pe1fail", "pe2fail", "pe3fail", "pekind",
         "pelam", "ecfail", "ec3fail", "cfail", "a1fail", "a2fail", "a3fail", "emonfail", "cycfail"]

def load(fn):
    G = json.load(open(fn)); G = G.get("genome", G) if isinstance(G, dict) else G
    return G if isinstance(G, dict) and "opts" in G and "start" in G else None

def main(a):
    global CTRL, LIMIT
    eng, gens, files, eorder = "both", [], [], "lev"
    i = 0
    while i < len(a):
        if a[i] == "--eng": eng = a[i + 1]; i += 2
        elif a[i] == "--ctrl": CTRL = a[i + 1]; i += 2
        elif a[i] == "--eorder": eorder = a[i + 1]; i += 2
        elif a[i] == "--limit": LIMIT = int(a[i + 1]); i += 2
        elif a[i] == "--gen": gens.append((int(a[i + 1]), int(a[i + 2]), a[i + 3])); i += 4
        else: files.append(a[i]); i += 1
    A.EORDER = eorder
    jobs = [(os.path.basename(fn), load(fn)) for fn in files if not fn.endswith(".names.json")]
    for cnt, seed, kind in gens:
        rng = random.Random(seed)
        jobs += [(f"gen_{kind}_{seed}_{k}", RE.gen(rng, kind)) for k in range(cnt)]
    tot = {e: defaultdict(int) for e in ("g3", "cyc")}
    for nm, G in jobs:
        if G is None: print(nm, "skipped"); continue
        for e in (("g3", "cyc") if eng == "both" else (eng,)):
            C = defaultdict(int)
            for k in FAILS: C[k] += 0
            try:
                R = run_g3(G) if e == "g3" else run_cyc(G)
                if R.get("capped"): C["capped"] += 1
                analyse(R, C)
            except RuntimeError as ex:
                C["error"] += 1; print(nm, e, "ERROR", ex)
            for k, v in C.items():
                tot[e][k] = max(tot[e][k], v) if k.startswith("rec_max") else tot[e][k] + v
            if files and not gens:
                print(nm, e, " ".join(f"{k} {C[k]}" for k in sorted(C)), flush=True)
    for e in tot:
        if tot[e]: print("TOTAL", e, " ".join(f"{k} {tot[e][k]}" for k in sorted(tot[e])), flush=True)

if __name__ == "__main__":
    main(sys.argv[1:])
