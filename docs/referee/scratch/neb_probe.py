#!/usr/bin/env python3
"""REFEREE succ. 9 probe for packet P-N5-NEB (docs/new/P-N5-NEB-box38.md, pin 314d220, sha1 ba15e51f...). Own engine (rl_engine,
rl_probe.states; no lane code). C^1O asserted (rl_probe.assert_c1o). Phase key = (lambda_Xi, tau); HN = H1 and not H2; HN stretch =
maximal run of HN states of one phase; crossing = in-phase transition with R changing; c_w = cycle node of o's W-play (o on it).
Checks (*_FAIL must be 0 for the claims to sign; counters also say how often each hypothesis occurs):
 FBLN0   at every Even fallback HN state: no gate F -> Rbar (FBL-N (iii) + (iii+))
 RISE    s1: from every in-phase Even fallback a in a stretch, first t+1 in S (theta constant on [a, t+1]) with a gate F -> Rbar:
         (star) for EVERY such gate, an Rbar-rise at t -> t+1, at the gate's z; HIGH (s2) in case A; chain rule on (star)
 NOENT   s3: case A, c_w(a) = o, any tau(o), every Even fallback HN state a (also phase-exiting: b = a): W_a(r) formula, Omega(o) even,
         INV (i), (ii), no entry, Rbar shrinks, Xi_t(z) ==_o Xi_a(z), on the theta-constant run [a, b] in S
 CASEB   s4: case B, c_w(a) = o: every R -> Rbar gate at a has lev -1 and z's route longer; Omega(c_theta) odd
 LOWR    s5: case B, c_w(a) = o: INV_B (ii_B), ==_B freeze, no entry on [a, t+1] while (i) held on [a, t]; at the first (i) failure
         a LOW rise (both values in C_theta) at t -> t+1
 BRK     s6: per stretch: breaks (eviction state a, entry k) classified A/B x (c_w(a) = o or not); (a), (b), (c) charges; (d) bound;
         LR_S <= (n-2)^2 (theta_S + 1)
 OUT1    s7: per tau(o) = o phase: X_HN and f_HN bounds; N_HN <= floor(T_ph/2) + 1
 BAND    s8 (not to sign; report only): case A, c_w(a) != o: R -> Rbar gates and Rbar-rises on [a, b] at level >= rank(c_w(a))
Usage: neb_probe.py lib37 | rand N nmin nmax seed [loop] | files... (a file may be followed by its .state start file)"""
import sys, os
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rl_engine as RE, rl_probe as P
EX = []


def ex(*a):
    EX.append(a)


def states_from(g, s0):
    """rl_probe.states with an optional start sigma (tau canonical, tau(o) = o if o has a self-loop), as the lane's neb_run.py"""
    if s0 is None: return P.states(g)
    o = P.assert_c1o(g)
    s, t = RE.best_reward_start(g)
    s = [None if g.owner[v] == 1 else s0[v] for v in range(g.n)]
    if o in g.succ[o]: t[o] = o
    orig = RE.run
    RE.run = lambda gg, start=None, maxit=100000: orig(gg, (s, t), maxit)
    try: return P.states(g)
    finally: RE.run = orig


def run(g, cnt, name, s0=None):
    o, st = states_from(g, s0); n = g.n; T = len(st) - 1; ro = g.rank[o]
    nE = sum(1 for v in range(n) if g.owner[v] == 0); KK = nE * (2 * n - 1)
    key = lambda x: g.key(x)
    lt = lambda x, y: key(x) < key(y)
    inph = [st[k]["key"] == st[k + 1]["key"] for k in range(T)]
    HN = [a["H1"] and not a["H2"] for a in st]
    Rb = [a["Rb"] for a in st]; R = [a["Rb"] - {o} for a in st]
    cross = [inph[k] and R[k] != R[k + 1] for k in range(T)]
    th = [a["Xi"][o] for a in st]
    thch = [th[k] != th[k + 1] for k in range(T)]
    inP = lambda x, v: (x[1] >> g.rank[v]) & 1
    cw = [a["W"][o][0] if not a["H2"] else None for a in st]

    def gatesFR(k): return [(y, z) for y, z in st[k]["Is"] if y in st[k]["F"] and z in Rb[k]]

    def gatesRR(k): return [(v, z) for v, z in st[k]["Is"] if v in R[k] and z in Rb[k]]

    def rises(t):
        return [z for z in (Rb[t] & Rb[t + 1]) if z != o and lt(st[t]["Xi"][z], st[t + 1]["Xi"][z])]

    def eqo(x, y): return P.lev(x, y) < ro

    def eqB(x, y): return P.lev(x, y) <= -1

    def rlen(k, z): return 0 if z == o else len(P.route(st[k]["nx"], z, o))

    def entry(t): return R[t] < R[t + 1] or (not R[t + 1] <= R[t])

    # stretches
    stretches, k = [], 0
    while k <= T:
        if HN[k]:
            j = k
            while j < T and HN[j + 1] and inph[j]: j += 1
            stretches.append((k, j)); k = j + 1
        else: k += 1
    sof = {}
    for (s0_, s1_) in stretches:
        for k in range(s0_, s1_ + 1): sof[k] = (s0_, s1_)
    efb = [st[k]["fb"] and bool(st[k]["Is"]) for k in range(T + 1)]
    # FBLN0 and per-fallback-state checks (s3, s4, s5, s8, s1)
    for a in range(T):
        if not (efb[a] and HN[a]): continue
        cnt["HNfb_states"] += 1
        if gatesFR(a): cnt["FBLN0_FAIL"] += 1; ex(name, "FBLN0", a)
        s0_, s1_ = sof[a]
        b = a
        while b + 1 <= s1_ and th[b + 1] == th[a]: b += 1
        c = th[a][0]; caseA = ro > g.rank[c]; too = st[a]["t"][o] == o; cwo = cw[a] == o
        cls = ("A" if caseA else "B") + ("_cw=o" if cwo else "_cw!=o") + ("_tauo=o" if too else "_tauo!=o")
        cnt["fbclass_" + cls] += 1
        if not inph[a]: cnt["fbclass_" + cls + "_exits"] += 1
        if too and not cwo: cnt["TAUO_CWO_FAIL"] += 1; ex(name, "tauo=o but c_w != o", a)
        # s1 / s2 (in-phase fallback only)
        if inph[a]:
            for t1 in range(a + 1, b + 1):
                G = gatesFR(t1)
                if not G: continue
                t = t1 - 1; cnt["RISE_events"] += 1
                rz = rises(t)
                if not rz: cnt["RISE_FAIL"] += 1; ex(name, "RISE none", a, t1)
                for (y, z) in G:
                    cnt["RISE_gates"] += 1
                    q = st[t1]["s"][y]
                    x0, x1, x2 = st[t]["Xi"][z], st[t1]["Xi"][q], st[t1]["Xi"][z]
                    if not (key(x0) <= key(x1) < key(x2)): cnt["STAR_FAIL"] += 1; ex(name, "STAR", a, t1, y, z)
                    if z not in rz: cnt["RISEz_FAIL"] += 1; ex(name, "RISE at z", a, t1, z)
                    if key(x0) < key(x1) < key(x2):
                        cnt["CHAIN_chk"] += 1
                        if P.lev(x0, x2) != max(P.lev(x0, x1), P.lev(x1, x2)): cnt["CHAIN_FAIL"] += 1; ex(name, "CHAIN", a, t1)
                    if caseA:
                        cnt["HIGH_chk"] += 1
                        if not P.lev(x0, x2) >= ro: cnt["HIGH_FAIL"] += 1; ex(name, "HIGH", a, t1, z)
                break
        # s3
        if caseA and cwo:
            Wa = st[a]["W"]
            if g.prio[o] % 2: cnt["NOENT_par_FAIL"] += 1
            for r in Rb[a]:
                pr = P.route(st[a]["nx"], r, o) if r != o else []
                m = 0
                for u in pr:
                    if g.rank[u] > ro: m |= 1 << g.rank[u]
                if Wa[r] != (o, m, len(pr)): cnt["NOENT_Wform_FAIL"] += 1; ex(name, "Wform", a, r)
            cnt["NOENT_runs"] += 1
            if too: cnt["NOENT_runs_tauo=o"] += 1
            else: cnt["NOENT_runs_tauo!=o"] += 1
            for t in range(a, b + 1):
                x = st[t]; cnt["NOENT_states"] += 1
                i1 = not gatesFR(t)
                i2 = all(P.lev(x["Xi"][x["s"][v]], x["Xi"][z]) < ro for v, z in gatesRR(t))
                fr = all(eqo(x["Xi"][z], st[a]["Xi"][z]) for z in Rb[t])
                ne = t == b or (not entry(t) and Rb[t + 1] <= Rb[t])
                if gatesRR(t): cnt["NOENT_RRgates_present"] += len(gatesRR(t))
                if not (i1 and i2 and fr and ne): cnt["NOENT_FAIL"] += 1; ex(name, "NOENT", a, t, i1, i2, fr, ne)
        # s4, s5
        if (not caseA) and cwo:
            if g.prio[c] % 2 == 0: cnt["CASEB_par_FAIL"] += 1
            for v, z in gatesRR(a):
                cnt["CASEB_gates"] += 1
                if P.lev(st[a]["Xi"][st[a]["s"][v]], st[a]["Xi"][z]) != -1 or not rlen(a, z) > rlen(a, st[a]["s"][v]):
                    cnt["CASEB_FAIL"] += 1; ex(name, "CASEB", a, v, z)
            cnt["LOWR_runs"] += 1
            for t1 in range(a + 1, b + 1):
                t = t1 - 1
                if gatesFR(t): break          # (i) failed at t: hypothesis of s5 ends
                cnt["LOWR_steps"] += 1
                okA = not entry(t) and Rb[t1] <= Rb[t] and all(eqB(st[t1]["Xi"][z], st[t]["Xi"][z]) for z in Rb[t1])
                okB = all(P.lev(st[t1]["Xi"][st[t1]["s"][v]], st[t1]["Xi"][z]) == -1 for v, z in gatesRR(t1))
                if not (okA and okB): cnt["LOWR_ab_FAIL"] += 1; ex(name, "LOWR ab", a, t1, okA, okB)
                if gatesFR(t1):
                    cnt["LOWR_c_events"] += 1
                    Cth = (c, th[a][1])
                    low = [z for z in rises(t) if st[t]["Xi"][z][:2] == Cth and st[t1]["Xi"][z][:2] == Cth]
                    if not low: cnt["LOWR_c_FAIL"] += 1; ex(name, "LOWR c", a, t1)
        # s8 BAND (report only)
        if caseA and not cwo and cw[a] is not None:
            rc = g.rank[cw[a]]; cnt["BAND_runs"] += 1
            for t in range(a, b + 1):
                for v, z in gatesRR(t):
                    lg = P.lev(st[t]["Xi"][st[t]["s"][v]], st[t]["Xi"][z])
                    if lg >= rc:
                        cnt["BAND_gate_viol" + ("_at_base" if t == a else "_later")] += 1; ex(name, "BANDgate", a, t, v, z, lg, rc)
                        if lg > rc: cnt["BAND_gate_strict" + ("_at_base" if t == a else "_later")] += 1
                if t < b:
                    for z in rises(t):
                        if P.lev(st[t]["Xi"][z], st[t + 1]["Xi"][z]) >= rc: cnt["BAND_rise_viol"] += 1; ex(name, "BANDrise", a, t, z)
    # s6 per stretch
    for (s0_, s1_) in stretches:
        trs = list(range(s0_, s1_))
        ent = [t for t in trs if cross[t] and R[t] < R[t + 1]]
        ev = [t for t in trs if cross[t] and Rb[t + 1] < Rb[t]]
        if len(ent) + len(ev) != sum(cross[t] for t in trs): cnt["mixed_crossing"] += 1
        breaks = []
        for e in ent:
            pe = max([x for x in ent if x < e], default=-1)
            evs = [x for x in ev if pe < x < e]
            if evs: breaks.append((evs[0], e))
        thS = sum(thch[t] for t in trs)
        c = th[s0_][0]; caseA = ro > g.rank[c]
        lowT = set()
        for t in trs:
            if thch[t]: continue
            Cth = (th[t][0], th[t][1])
            if any(st[t]["Xi"][z][:2] == Cth and st[t + 1]["Xi"][z][:2] == Cth for z in rises(t)): lowT.add(t)
        LR = len(lowT)
        if LR > (n - 2) ** 2 * (thS + 1): cnt["LR_FAIL"] += 1; ex(name, "LR", s0_)
        RW = set()
        for (a, kk) in breaks:
            cwo = cw[a] == o; cl = ("A" if caseA else "B") + ("=" if cwo else "!=")
            cnt["breaks_" + cl] += 1
            if not efb[a]: cnt["BRK_evfb_FAIL"] += 1; ex(name, "eviction not Even fb", a)
            thc = any(thch[j] for j in range(a + 1, kk + 1))
            if thch[a]: cnt["BRK_FFLAT_FAIL"] += 1
            riseT = [t for t in range(a, kk) if not thch[t] and rises(t)]
            highT = [t for t in riseT if any(P.lev(st[t]["Xi"][z], st[t + 1]["Xi"][z]) >= ro for z in rises(t))]
            lowB = [t for t in range(a, kk) if t in lowT]
            if caseA and cwo and not thc: cnt["BRK_a_FAIL"] += 1; ex(name, "BRK a", a, kk)
            if (not caseA) and cwo and not (thc or lowB): cnt["BRK_b_FAIL"] += 1; ex(name, "BRK b", a, kk)
            if not (thc or (highT if caseA else riseT)): cnt["BRK_c_FAIL"] += 1; ex(name, "BRK c", a, kk)
            if thc: cnt["breaks_charged_theta"] += 1
            elif lowB: cnt["breaks_charged_low"] += 1
            else: cnt["breaks_charged_rise"] += 1
            if not cwo: RW |= set(riseT)
        B = len(breaks)
        if B > thS + LR + len(RW): cnt["BRK_d_FAIL"] += 1; ex(name, "BRK d", s0_, B, thS, LR, len(RW))
        if all(cw[a] == o for a, _ in breaks):
            if B > thS + (n - 2) ** 2 * (thS + 1) or (caseA and B > thS): cnt["BRK_d2_FAIL"] += 1; ex(name, "BRK d2", s0_)
        cnt["stretches"] += 1; cnt["breaks"] += B
    # s7 per tau(o) = o phase
    k = 0
    while k <= T:
        j = k
        while j < T and inph[j]: j += 1
        if st[k]["t"][o] == o:
            cnt["OUT1_phases"] += 1
            Tph = sum(st[t]["H1"] != st[t + 1]["H1"] for t in range(k, j))
            thph = sum(thch[t] for t in range(k, j))
            sts = [(a, b) for (a, b) in stretches if k <= a <= j]
            NHN = len(sts)
            XHN = sum(cross[t] for (a, b) in sts for t in range(a, b))
            fHN = sum(1 for t in range(k, j) if HN[t] and st[t]["fb"])
            D = (n - 2) ** 2 + 1
            if NHN > Tph // 2 + 1: cnt["OUT1_NHN_FAIL"] += 1; ex(name, "NHN", k)
            if XHN > 2 * (n - 1) * D * (thph + NHN): cnt["OUT1_X_FAIL"] += 1; ex(name, "XHN", k)
            if fHN > (KK + 1) * (2 * (n - 1) * D * (thph + NHN) + NHN): cnt["OUT1_f_FAIL"] += 1; ex(name, "fHN", k)
            cnt["OUT1_fHN_total"] += fHN; cnt["OUT1_XHN_total"] += XHN
        k = j + 1


def main(a):
    if a and a[0] == "rand":
        import random
        N, lo, hi, seed = map(int, a[1:5]); rng = random.Random(seed); cnt = Counter()
        for i in range(N):
            g = P.rand_c1o(rng, rng.randint(lo, hi))
            if len(a) > 5 and a[5] == "loop":          # give o a self-loop (tau(o) = o reachable)
                o = P.assert_c1o(g)
                if o not in g.succ[o]: g = RE.Game(g.prio, g.owner, [s_ + [o] if v == o else s_ for v, s_ in enumerate(g.succ)])
            cnt["games"] += 1
            try: run(g, cnt, "rand%d_%d" % (seed, i))
            except RuntimeError: cnt["maxit"] += 1
        for k in sorted(cnt): print("%-30s %d" % (k, cnt[k]))
        print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
        for e in EX[:30]: print("EX", e)
        return
    if a == ["lib37"]:
        items = [(os.path.join(P.ROOT, l.split()[0]), None) for l in open(os.path.join(P.ROOT, "experiments/new/box37/lib37.txt")) if l.strip()]
    else:
        items, i = [], 0
        while i < len(a):
            s0 = None
            if i + 1 < len(a) and a[i + 1].endswith(".state"):
                s0 = list(map(int, open(a[i + 1]).read().split())); i += 1
            items.append((a[i - (1 if s0 is not None else 0)], s0)); i += 1
    cnt = Counter()
    for f, s0 in items:
        g = RE.parse(f)
        try: P.assert_c1o(g)
        except AssertionError: cnt["skip_not_c1o"] += 1; continue
        if g.n > 64: cnt["skip_big"] += 1; continue
        cnt["games"] += 1; run(g, cnt, os.path.relpath(f, P.ROOT), s0)
    for k in sorted(cnt): print("%-30s %d" % (k, cnt[k]))
    print("FAILS", sum(v for k, v in cnt.items() if k.endswith("_FAIL")))
    for e in EX[:30]: print("EX", e)


if __name__ == "__main__":
    main(sys.argv[1:])
