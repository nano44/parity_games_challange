#!/usr/bin/env python3
"""L-RED successor 39 (R169): srz3b.py + the OPEN list of R168 as options (env):
  MID=1    (i) E3 has a mid vertex L3m below the head; each gate gg^L_j reads the head or the mid (free per j); the wave passes mid
           then head (states b -> m -> a), every gate must stay closed in b and m;
  THIRD=1  (ii) every reactor j >= 2 gets a third option cc_j (C_j) -> u_(j-1), used as the ARMED comparison side: reset b, pre-armed
           c (all at once, Xi-improving and W-better, before the phase), risen a; gates compare aa_j with cc_j (R159 self-reference);
  EXTTGT=1 (iii) rider escapes may also go to a second ladder rung T2 (free rank / parity, tau-bar value T2S free) or into the line's
           own E3 head; static gate escapes hh_j go to q or to T2 (free per j).
(iv) the E1 coupling is not modelled. ITAU here also covers the static escapes hh_j (missing in srz3b).
Original docstring (R168): srz3.py with TWO E3 lines A and B that ALTERNATE per phase, so that no driver restarts while its gates
bind. Shared: E2 reactors u_j, aa_j (A_j) -> {u_(j-1) (tau), gg^A_j (G^A_j) -> L3^A, gg^B_j (G^B_j) -> L3^B}, bb_j (BB_j) -> q, root T.
Per line L: riders rho^L_j (R^L_j) -> {mdd (M^L_j) -> u_j (tau)} + optional escape x^L_j (X^L_j) -> q | T; floor rho^L_0 (R^L_0) -> q;
drivers hs^L (odd riders), hps^L (floor + even riders); L3^L a-state -> (BA3^L) hs^L, b-state -> (BBB^L) hps^L.
Phase of line P (active), other line O (idle). P's drivers start FRESH (hs^P on rho_1, hps^P on rho_H0, H0 = env HPS0 in {0, 2}) and
climb with the waves k = 1, 3, ..., J-2 exactly as srz3 PHASE1 (CLIMB / CLOSED / WAVE / OPEN / CLIMB2 / FLIP / NEXT, Xi and W, STAY).
The idle line O starts HIGH (hs^O on rho_Jodd, hps^O on rho_Jeven) and must get back LOW (rho_1 / rho_H0) at some transition of P's
phase: there the switch is Xi-improving and W-better for both O-drivers (O's restart, moved into the other line's phase). Before it O
is high, after it low; O's L3 state is FREE per state (a relaxation). Both phases (P = A and P = B) are required.
Env ITAU=1 adds I_tau = {} (no Odd improving switch against tau-bar = Even's best response to tau; hps's tau-bar value is a free
symbol QS relative to q). Every requirement is necessary for the run, so UNSAT is a proof for this model; SAT is a candidate only.
Usage: srz3b.py [J]"""
import sys, os
import z3
J = int(sys.argv[1]) if len(sys.argv) > 1 else 7
H0 = int(os.environ.get("HPS0", "0")); ITAU = os.environ.get("ITAU") == "1"; WREQ = True; STAY = os.environ.get("STAY", "1") == "1"
COPIES = os.environ.get("COPIES") == "1"                  # two FULL copies (own E2 + E3 each), alternating per phase: by symmetry one
LINES = ("A",) if COPIES else ("A", "B")                   # copy suffices: its phase (fresh start) + its restart while IDLE (E2 reset)
SY = ["T", "QS", "T2", "T2S"] + [f"{c}{j}" for j in range(1, J + 1) for c in ("A", "BB", "H", "C")]
MID = os.environ.get("MID") == "1"; THIRD = os.environ.get("THIRD") == "1"; EXT = os.environ.get("EXTTGT") == "1"
STATIC = os.environ.get("STATICESC") == "1"                # every gate aa_j (j >= 2) also gets a static escape hh_j (H_j) -> q
for L in LINES:
    SY += [f"BA3{L}", f"BBB{L}", f"BA3m{L}", f"BBBm{L}", f"R{L}0"] + [f"{c}{L}{j}" for j in range(1, J + 1) for c in ("R", "M", "X", "G")]
s = z3.Solver()
rk = {x: z3.Int(f"rk_{x}") for x in SY}; ev = {x: z3.Bool(f"ev_{x}") for x in SY}; pr = {x: z3.Bool(f"pr_{x}") for x in SY}
s.add(z3.Distinct(*rk.values())); s.add(ev["T"], pr["T"])
for x in SY:
    s.add(rk[x] >= 0, rk[x] < 10000)
    if x not in ("T", "QS", "T2", "T2S"): s.add(rk[x] < rk["T"])
QFIX = os.environ.get("QFIX", "1") == "1"                   # R169: tau-bar values tied to the ladder (see paths()):
t2hi = z3.Bool("t2hi")
if os.environ.get("T2HI") == "1": s.add(t2hi)              # T2 realised as a direct edge to hp: tau-bar value V_K, an even rung above T
if QFIX:                                                   # in-phase T2 (a rung's CURRENT level) is below the root; q's tau-bar
    s.add(rk["T2"] < rk["T"], rk["QS"] < rk["T"], pr["QS"])  # value is T + QS (QS a band symbol); T2's tau-bar value is a higher even
    s.add(z3.Implies(t2hi, z3.And(rk["T2S"] > rk["T"], ev["T2S"], pr["T2S"])), z3.Implies(z3.Not(t2hi), rk["T2S"] < rk["T"]))
                                                           # rung T2S > T, or T + T2S with T2S < T        # QS (hps's tau-bar value vs the root's) is free: under tau-bar hps
                                                          # can reach the top ladder too
esc = {(L, j): z3.Int(f"esc_{L}{j}") for L in LINES for j in range(1, J + 1)}
for e in esc.values(): s.add(e >= 0, e <= (4 if EXT else 2))
gm = {(L, j): z3.Bool(f"gm_{L}{j}") for L in LINES for j in range(2, J + 1)}   # gate reads mid (MID)
hq = {j: z3.Bool(f"hq_{j}") for j in range(2, J + 1)}                        # static escape -> q (else -> T2, EXT)
for j in hq:
    if not EXT: s.add(hq[j])
    if not MID:
        for L in LINES: s.add(z3.Not(gm[L, j]))
if os.environ.get("UNIFORM") == "1":                       # period-2 shift-invariant placement for j >= 3 (extends to any m2)
    Dz = z3.Int("D")
    for j in range(3, J - 1):
        for c in ["A", "BB", "H"] + [c + L for L in LINES for c in ("R", "M", "X", "G")]:
            x, y = f"{c}{j}", f"{c}{j + 2}"
            s.add(rk[y] - rk[x] == Dz, pr[y] == pr[x], ev[y] == ev[x])
        for L in LINES: s.add(esc[L, j + 2] == esc[L, j])
        if j >= 3 and j + 2 <= J: pass
    for j in range(3, J - 1):
        if j + 2 <= J: s.add(z3.Bool(f"hq_{j + 2}") == z3.Bool(f"hq_{j}"))
TRUE = z3.BoolVal(True)
def better(S1, S2):
    D = sorted(set(S1) ^ set(S2))
    if not D: return z3.BoolVal(False)
    return z3.Or(*[z3.And(pr[e], (ev[e] if e in S1 else z3.Not(ev[e])), *[z3.Or(z3.Not(pr[f]), rk[f] < rk[e]) for f in D if f != e]) for e in D])
def evenwon(C):
    return z3.Or(*[z3.And(pr[e], ev[e], *[z3.Or(z3.Not(pr[f]), rk[f] < rk[e]) for f in C if f != e]) for e in C])
def graph(risen, pos, L3, mode="xi", armed=None):
    """pos[L] = (hs index, hps index); L3[L] in 'ab'. mode 'xi': Odd all options, Even fixed; 'w': Odd tau only, Even fixed;
    'tb': Odd tau only, Even ALL options (tau-bar); q's value is [] ('xi', 'w') or [QS] ('tb')."""
    G = {}; E = lambda lst: ("E", lst); O = lambda lst: ("O", lst)
    armed = THIRD if armed is None else armed
    for j in range(1, J + 1):
        un = f"cc{j}" if (armed and j >= 2) else f"bb{j}"
        G[f"u{j}"] = E([(TRUE, [], f"aa{j}"), (TRUE, [], f"bb{j}")] + ([(TRUE, [], f"cc{j}")] if THIRD and j >= 2 else []) if mode == "tb" else [(TRUE, [], f"aa{j}" if j in risen else un)])
        G[f"bb{j}"] = O([(TRUE, [f"BB{j}"], "q")])
        if THIRD and j >= 2: G[f"cc{j}"] = O([(TRUE, [f"C{j}"], f"u{j - 1}")])
        hh = [(hq[j], [f"A{j}", f"H{j}"], "q"), (z3.Not(hq[j]), [f"A{j}", f"H{j}"], "T2")] if (STATIC and j >= 2) else []
        G[f"aa{j}"] = O([(TRUE, [f"A{j}"], "T")] if j == 1 else [(TRUE, [f"A{j}"], f"u{j - 1}")] + [(z3.Not(gm[L, j]), [f"A{j}", f"G{L}{j}"], f"L3{L}") for L in LINES] + [(gm[L, j], [f"A{j}", f"G{L}{j}"], f"L3m{L}") for L in LINES] + hh)
        for L in LINES:
            G[f"rho{L}{j}"] = O([(TRUE, [f"R{L}{j}", f"M{L}{j}"], f"u{j}"), (esc[L, j] == 1, [f"R{L}{j}", f"X{L}{j}"], "q"), (esc[L, j] == 2, [f"R{L}{j}", f"X{L}{j}"], "T"),
                                 (esc[L, j] == 3, [f"R{L}{j}", f"X{L}{j}"], "T2"), (esc[L, j] == 4, [f"R{L}{j}", f"X{L}{j}"], f"L3{L}")])
    for L in LINES:
        G[f"rho{L}0"] = O([(TRUE, [f"R{L}0"], "q")])
        if MID:                                             # head: a -> mid, b -> hps; mid: a -> hs, b -> hps; states b, m (mid done), a
            a, b = (TRUE, [f"BA3{L}"], f"L3m{L}"), (TRUE, [f"BBB{L}"], f"hps{L}")
            ma, mb = (TRUE, [f"BA3m{L}"], f"hs{L}"), (TRUE, [f"BBBm{L}"], f"hps{L}")
            G[f"L3{L}"] = E([a, b] if mode == "tb" else [a] if L3[L] == "a" else [b])
            G[f"L3m{L}"] = E([ma, mb] if mode == "tb" else [ma] if L3[L] in "am" else [mb])
        else:
            a, b = (TRUE, [f"BA3{L}"], f"hs{L}"), (TRUE, [f"BBB{L}"], f"hps{L}")
            G[f"L3{L}"] = E([a, b] if mode == "tb" else [a] if L3[L] == "a" else [b])
            G[f"L3m{L}"] = G[f"L3{L}"]
        odds = [j for j in range(1, J + 1) if j % 2]; evens = [0] + [j for j in range(2, J + 1, 2)]
        G[f"hs{L}"] = E([(TRUE, [], f"rho{L}{j}") for j in odds] if mode == "tb" else [(TRUE, [], f"rho{L}{pos[L][0]}")])
        G[f"hps{L}"] = E([(TRUE, [], f"rho{L}{j}") for j in evens] if mode == "tb" else [(TRUE, [], f"rho{L}{pos[L][1]}")])
    if mode in ("w", "tb"): G = {v: (o, lst[:1]) if o == "O" else (o, lst) for v, (o, lst) in G.items()}
    return G
def paths(G, v, qsym):
    out = []
    def go(x, conds, syms, stack):
        tb = "QS" in qsym
        if x == "q": out.append((conds, syms + ((["T"] + list(qsym)) if (tb and QFIX) else list(qsym)))); return
        if x == "T": out.append((conds, syms + ["T"])); return
        if x == "T2":
            if not tb: out.append((conds, syms + ["T2"]))
            elif not QFIX: out.append((conds, syms + ["T2S"]))
            else: out.append((conds + [t2hi], syms + ["T2S"])); out.append((conds + [z3.Not(t2hi)], syms + ["T", "T2S"]))
            return
        if x in stack: return                                       # cycles: handled by cycles_ok (Odd never closes Even-won ones)
        for c, sy, nx in G[x][1]: go(nx, conds + [c], syms + sy, stack + [x])
    go(v, [], [], []); return out
def cond(p): return z3.And(*p[0]) if p[0] else TRUE
def req(G, v1, e1, v2, e2, strict=True, maxing=False, qsym=()):
    """min-semantics (Odd chooses, 'xi'/'w'): strict: min1 > min2; else min1 <= min2. max-semantics (Even chooses, 'tb'):
    strict=False means NOT(max2 > max1), i.e. max1 >= max2."""
    P1 = paths(G, v1, list(qsym)); P2 = paths(G, v2, list(qsym))
    if maxing:   # max1 >= max2: exists p1 such that no p2 beats it
        return z3.Or(*[z3.And(cond(p1), *[z3.Implies(cond(p2), z3.Not(better(p2[1] + e2, p1[1] + e1))) for p2 in P2]) for p1 in P1])
    if strict:
        return z3.And(*[z3.Implies(cond(p1), z3.Or(*[z3.And(cond(p2), better(p1[1] + e1, p2[1] + e2)) for p2 in P2])) for p1 in P1])
    return z3.Or(*[z3.And(cond(p1), *[z3.Implies(cond(p2), z3.Not(better(p1[1] + e1, p2[1] + e2))) for p2 in P2]) for p1 in P1])
def cycles_ok(G):
    cons, seen = [], set()
    def go(x, conds, stack, symstack):
        if x in ("q", "T", "T2"): return
        if x in stack:
            i = stack.index(x); C = sum(symstack[i:], []); key = (tuple(sorted(stack[i:])), tuple(sorted(C)))
            if key not in seen: seen.add(key); cons.append(z3.Implies(z3.And(*conds) if conds else TRUE, evenwon(C) if C else z3.BoolVal(False)))
            return
        for c, sy, nx in G[x][1]: go(nx, conds + [c], stack + [x], symstack + [list(sy)])
    for v in G: go(v, [], [], [])
    return cons
TRACK = {}
KEEP = os.environ.get("KEEP") == "1"                      # [S4b-KEEP] (L-SI box 62): tau stays iff it is Odd's optimum in H' (Odd: tau
INI = {}                                                   # + I_tau edges; Even: sigma) at every state; I_tau against tau-bar
def _ext(G, conds0, syms0, tgt, qsym):
    return [(conds0 + pc, syms0 + ps) for pc, ps in paths(G, tgt, qsym)]
def _strict_min(P1, P2):   # min P1 > min P2 (for Even): every available p1 beats some available p2
    return z3.And(*[z3.Implies(cond(p1), z3.Or(*[z3.And(cond(p2), better(p1[1], p2[1])) for p2 in P2])) for p1 in P1])
def ini(v, idx, G0):
    """z3 Bool: Odd's edge idx (>= 1) at v is in I_tau (strictly worse for Even than tau's edge under tau-bar: max-semantics)."""
    if (v, idx) in INI: return INI[(v, idx)]
    TB = graph(set(), {"A": (1, H0), "B": (1, H0)}, {"A": "a", "B": "a"}, "tb"); q = ["QS"]
    c0, sy0, t0 = G0[v][1][0]; c1, sy1, t1 = G0[v][1][idx]
    Pt = _ext(TB, [c0], list(sy0), t0, q); Pa = _ext(TB, [c1], list(sy1), t1, q)
    b = z3.Bool(f"inI_{v}_{idx}"); INI[(v, idx)] = b
    s.add(b == z3.Or(*[z3.And(cond(pt), *[z3.Implies(cond(pa), better(pt[1], pa[1])) for pa in Pa]) for pt in Pt]))
    return b
def keep_cons(G):
    H = {}
    for v, (o, lst) in G.items():
        if o == "O" and len(lst) > 1:
            H[v] = (o, [lst[0]] + [(z3.And(c, ini(v, i, G)), sy, nx) for i, (c, sy, nx) in enumerate(lst) if i >= 1])
        else: H[v] = (o, lst)
    out = []
    for v, (o, lst) in H.items():
        if o != "O" or len(lst) < 2: continue
        c0, sy0, t0 = lst[0]; Pt = _ext(H, [c0], list(sy0), t0, [])
        for i in range(1, len(lst)):
            c1, sy1, t1 = lst[i]; Pa = _ext(H, [c1], list(sy1), t1, [])
            out.append(z3.Not(_strict_min(Pt, Pa)))              # Odd does not strictly prefer the I_tau edge in H'
    return out
SKIP1 = os.environ.get("SKIP1") == "1"
E2STAY = os.environ.get("E2STAY", "1") == "1"
def track(f, tag):
    b = z3.Bool(f"t{len(TRACK)}"); TRACK[b] = tag; s.assert_and_track(f, b)
def sw_req(G, GW, cur, tgt, L, who):
    """driver who in {'hs','hps'} of line L moves cur -> tgt: Xi-improving and W-better."""
    return z3.And(req(G, f"rho{L}{tgt}", [], f"rho{L}{cur}", []), req(GW, f"rho{L}{tgt}", [], f"rho{L}{cur}", []))
def stay(G, GW, L, cur, tgt, opts):
    return [z3.Not(z3.And(req(G, f"rho{L}{j}", [], f"rho{L}{cur}", []), req(GW, f"rho{L}{j}", [], f"rho{L}{tgt}", []))) for j in opts if j not in (cur, tgt)]
def cmpv(j): return f"cc{j}" if (THIRD and j >= 2) else f"bb{j}"
ODDS = [j for j in range(1, J + 1) if j % 2]; EVENS = [0] + [j for j in range(2, J + 1, 2)]
JO = J if J % 2 else J - 1; JE = J - 1 if J % 2 else J
def phase(P, O):
    """the schedule of P's phase: list of (risen, P-positions, P-L3, P-targets, reqs-builder, tag)."""
    st = [(set(), (1, H0), "b", (1, H0), [], f"{P}START")]
    for k in range(1, J - 1, 2):
        R = set(range(1, k + 1)); R1 = R | {k + 1}; hp = H0 if k == 1 else k - 1
        if k >= 3: st.append((R, (k - 2, hp), "b", (k, hp), ["CLIMB"], f"{P}CLIMB@{k}"))
        st.append((R, (k, hp), "b", (k, hp), ["CLOSED", "WAVE"], f"{P}CLOSED@{k}"))
        if MID: st.append((R, (k, hp), "m", (k, hp), ["CLOSED", "WAVEm"], f"{P}CLOSEDm@{k}"))
        st.append((R, (k, hp), "a", (k, hp), ["OPEN"], f"{P}OPEN@{k}"))
        st.append((R1, (k, hp), "a", (k, k + 1), ["CLIMB2"] if hp != k + 1 else [], f"{P}CLIMB2@{k}"))
        st.append((R1, (k, k + 1), "a", (k, k + 1), ["FLIP"], f"{P}FLIP@{k}"))
        st.append((R1, (k, k + 1), "b", (k, k + 1), ["NEXT"], f"{P}NEXT@{k}"))
    return st
ONE = os.environ.get("ONEPHASE") == "1" or COPIES                    # control: phase A only, the idle line B already low (no restart anywhere)
if COPIES and os.environ.get("DROPIDLE") != "1":       # IDLE state of the copy: every reactor reset (unrisen), drivers high,
    for l3 in "ab":                                        # L3 free: the restart (both drivers) must be Xi-improving and W-better
        G = graph(set(), {"A": (JO, JE)}, {"A": l3}, armed=False); GW = graph(set(), {"A": (JO, JE)}, {"A": l3}, "w", armed=False)
        cs = cycles_ok(G) + [sw_req(G, GW, JO, 1, "A", "hs"), sw_req(G, GW, JE, H0, "A", "hps")]
        track(z3.Implies(z3.Bool("idle_l3a") if l3 == "a" else z3.Not(z3.Bool("idle_l3a")), z3.And(*cs)), "IDLE-RESTART")
if THIRD:                                                  # PREARM: from the reset (all b), every reactor j >= 2 takes cc_j at once
    for l3 in "ab":
        G = graph(set(), {"A": (1, H0), "B": (1, H0)}, {"A": l3, "B": l3}, armed=False); GW = graph(set(), {"A": (1, H0), "B": (1, H0)}, {"A": l3, "B": l3}, "w", armed=False)
        cs = [z3.And(req(G, f"cc{j}", [], f"bb{j}", []), req(GW, f"cc{j}", [], f"bb{j}", [])) for j in range(2, J + 1)]
        track(z3.Implies(z3.Bool("pre_l3a") if l3 == "a" else z3.Not(z3.Bool("pre_l3a")), z3.And(*cs)), "PREARM")
for P, O in ((("A", "B"),) if ONE else (("A", "B"), ("B", "A"))):
    st = phase(P, O); n = len(st)
    lo = [z3.Bool(f"lo_{P}{i}") for i in range(n + 1)]                     # idle line O is low at state i (lo[n]: after the phase)
    s.add(lo[0] if ONE else z3.Not(lo[0]), lo[n]); [s.add(z3.Implies(lo[i], lo[i + 1])) for i in range(n)]
    for i, (risen, pp, l3, tg, kinds, tag) in enumerate(st):
        k = int(tag.split("@")[1]) if "@" in tag else 0
        if SKIP1 and k == 1: kinds = [x for x in kinds if x == "CLIMB2"]   # the first wave of a phase may be lost (as gate 2 in R167)
        for olo in (False, True):
            for ol3 in ("abm" if MID else "ab"):
                l3v = z3.Int(f"l3_{P}{i}"); s.add(l3v >= 0, l3v < (3 if MID else 2))   # the idle line's E3 state: one of a, b (, m)
                cfg = z3.And(lo[i] if olo else z3.Not(lo[i]), l3v == "abm".index(ol3))
                opos = (1, H0) if olo else (JO, JE)
                if COPIES and not olo: continue
                pos = {P: pp, O: opos}; L3 = {P: l3, O: ol3}
                G = graph(risen, pos, L3); GW = graph(risen, pos, L3, "w")
                cons = cycles_ok(G)
                if KEEP: cons += keep_cons(G)
                # O's restart at this transition (high now, low next)
                flip = z3.And(z3.Not(lo[i]), lo[i + 1]) if not olo else z3.BoolVal(False)
                otg = (1, H0) if (not olo) else opos
                if not olo and os.environ.get("NORESTREQ") != "1":   # control: drop the Xi/W condition on O's restart switch
                    cons.append(z3.Implies(lo[i + 1], z3.And(sw_req(G, GW, JO, 1, O, "hs"), sw_req(G, GW, JE, H0, O, "hps"))))
                if STAY:
                    for (cur, tgt, opts, idx) in ((pp[0], tg[0], ODDS, 0), (pp[1], tg[1], EVENS, 1)):
                        cons += stay(G, GW, P, cur, tgt, opts)
                    oc_tg = [(1, H0) if not olo else opos][0]
                    cons += [z3.Implies(z3.Not(lo[i + 1]), z3.And(*stay(G, GW, O, opos[0], opos[0], ODDS), *stay(G, GW, O, opos[1], opos[1], EVENS)))] if not olo else []
                    if olo and not COPIES: cons += stay(G, GW, O, opos[0], opos[0], ODDS) + stay(G, GW, O, opos[1], opos[1], EVENS)
                if E2STAY:                                         # no unintended E2 switch: an unrisen reactor other than the one this
                    top = max(risen) if risen else 0               # state may advance does not rise (Xi-improving and W-better): every
                    for j in range(2, J + 1):                      # j > top + 1, and top + 1 too while the driver climbs (CLIMB)
                        if j in risen or (j == top + 1 and "CLIMB" not in kinds): continue
                        cons.append(z3.Not(z3.And(req(G, f"aa{j}", [], cmpv(j), []), req(GW, f"aa{j}", [], cmpv(j), []))))
                    if THIRD:                                      # armed reactors do not fall back to b
                        for j in range(2, J + 1):
                            if j not in risen: cons.append(z3.Not(z3.And(req(G, f"bb{j}", [], f"cc{j}", []), req(GW, f"bb{j}", [], f"cc{j}", []))))
                for kind in kinds:
                    for GG, nm in ((G, ""), (GW, "W")):
                        if kind == "CLOSED" and nm == "W": continue
                        if kind == "CLIMB": cons.append(req(GG, f"rho{P}{k}", [], f"rho{P}{k - 2}", []))
                        if kind == "CLOSED": cons.append(req(GG, f"aa{k + 1}", [], cmpv(k + 1), [], strict=False))
                        if kind == "WAVE" and not MID: cons.append(req(GG, f"hs{P}", [f"BA3{P}"], f"hps{P}", []))
                        if kind == "WAVE" and MID: cons.append(req(GG, f"hs{P}", [f"BA3m{P}"], f"hps{P}", [f"BBBm{P}"]))
                        if kind == "WAVEm": cons.append(req(GG, f"L3m{P}", [f"BA3{P}"], f"hps{P}", [f"BBB{P}"]))
                        if kind == "OPEN": cons.append(req(GG, f"aa{k + 1}", [], cmpv(k + 1), []))
                        if kind == "CLIMB2": cons.append(req(GG, f"rho{P}{k + 1}", [], f"rho{P}{pp[1]}", []))
                        if kind == "FLIP" and not MID: cons.append(req(GG, f"hps{P}", [], f"hs{P}", [f"BA3{P}"]))
                        if kind == "FLIP" and MID:
                            cons.append(req(GG, f"hps{P}", [f"BBBm{P}"], f"hs{P}", [f"BA3m{P}"])); cons.append(req(GG, f"hps{P}", [f"BBB{P}"], f"L3m{P}", [f"BA3{P}"]))
                        if kind == "NEXT": cons.append(req(GG, f"aa{k + 2}", [], cmpv(k + 2), []))
                track(z3.Implies(cfg, z3.And(*cons) if cons else TRUE), f"{tag}")
if ITAU:   # I_tau = {}: at every Odd vertex with options, the alternative is not worse for Even than tau's edge, under tau-bar
    G = graph(set(), {"A": (1, H0), "B": (1, H0)}, {"A": "a", "B": "a"}, "tb"); q = ["QS"]
    TBV = {"q": [(TRUE, ["T", "QS"] if QFIX else ["QS"])], "T": [(TRUE, ["T"])],      # tau-bar values of the sinks
           "T2": [(t2hi, ["T2S"]), (z3.Not(t2hi), ["T", "T2S"])] if QFIX else [(TRUE, ["T2S"])]}
    for j in range(2, J + 1):
        for L in LINES:
            alt = paths({**G, "_x": ("O", [(TRUE, [f"A{j}", f"G{L}{j}"], f"L3m{L}" if MID else f"L3{L}")])}, "_x", q) if not MID else []
            if MID:
                for tgt, cnd in ((f"L3{L}", z3.Not(gm[L, j])), (f"L3m{L}", gm[L, j])):
                    alt += [((p_[0] + [cnd]), p_[1]) for p_ in paths({**G, "_x": ("O", [(TRUE, [f"A{j}", f"G{L}{j}"], tgt)])}, "_x", q)]
            tau = paths(G, f"u{j - 1}", q)
            if MID:   # per target: the gate's own target alternative must not be tau-improving
                for tgt, cnd in ((f"L3{L}", z3.Not(gm[L, j])), (f"L3m{L}", gm[L, j])):
                    al = paths({**G, "_x": ("O", [(TRUE, [f"A{j}", f"G{L}{j}"], tgt)])}, "_x", q)
                    track(z3.Implies(cnd, z3.Or(*[z3.And(cond(pa), *[z3.Implies(cond(pt), z3.Not(better(pt[1] + [f"A{j}"], pa[1]))) for pt in tau]) for pa in al])), f"ITAU@aa{j}{L}")
            else:
                track(z3.Or(*[z3.And(cond(pa), *[z3.Implies(cond(pt), z3.Not(better(pt[1] + [f"A{j}"], pa[1]))) for pt in tau]) for pa in alt]), f"ITAU@aa{j}{L}")
        if STATIC:
            tau = paths(G, f"u{j - 1}", q)
            for cnd0, tgk in ((hq[j], "q"), (z3.Not(hq[j]), "T2")):
                for c2, tg in TBV[tgk]:
                    track(z3.Implies(z3.And(cnd0, c2), z3.And(*[z3.Implies(cond(pt), z3.Not(better(pt[1] + [f"A{j}"], [f"A{j}", f"H{j}"] + tg))) for pt in tau])), f"ITAU@hh{j}")
    for L in LINES:
        for j in range(1, J + 1):
            tau = paths(G, f"u{j}", q)
            for e, tgk in ((1, "q"), (2, "T"), (3, "T2")):
                for c2, tgt in TBV[tgk]:
                    track(z3.Implies(z3.And(esc[L, j] == e, c2), z3.And(*[z3.Implies(cond(pt), z3.Not(better(pt[1] + [f"M{L}{j}"], [f"X{L}{j}"] + tgt))) for pt in tau])), f"ITAU@rho{L}{j}")
            al4 = paths(G, f"L3{L}", q)                     # escape into the line's own E3 head: max over Even's choices there
            track(z3.Implies(esc[L, j] == 4, z3.Or(*[z3.And(cond(pa), *[z3.Not(better(pt[1] + [f"M{L}{j}"], [f"X{L}{j}"] + pa[1])) for pt in tau]) for pa in al4])), f"ITAU@rho{L}{j}")
r = s.check()
print("J", J, "KEEP", int(KEEP), "QFIX", int(QFIX), "MID", int(MID), "THIRD", int(THIRD), "EXTTGT", int(EXT), "SKIP1", int(SKIP1), "STATIC", int(STATIC), "COPIES", int(COPIES), "ONEPHASE", int(ONE), "HPS0", H0, "ITAU", int(ITAU), "STAY", int(STAY), "->", r)
if r == z3.unsat:
    core = sorted(set(TRACK[b] for b in s.unsat_core())); print("unsat core:", core)
else:
    m = s.model(); order = sorted((m.eval(rk[x]).as_long(), x) for x in SY if z3.is_true(m.eval(pr[x])))
    print("ascending:", " < ".join(f"{x}{'+' if z3.is_true(m.eval(ev[x])) else '-'}" for _, x in order))
    print("esc:", {f"{L}{j}": m.eval(esc[L, j]).as_long() for (L, j) in esc})
    if os.environ.get("MODEL_OUT"):
        import json
        json.dump({"rank": {x: m.eval(rk[x]).as_long() for x in SY}, "even": {x: z3.is_true(m.eval(ev[x])) for x in SY},
                   "present": {x: z3.is_true(m.eval(pr[x])) for x in SY}, "esc": {f"{L}{j}": m.eval(esc[L, j]).as_long() for (L, j) in esc},
                   "D": m.eval(z3.Int("D")).as_long() if os.environ.get("UNIFORM") == "1" else None, "J": J,
                   "hq": {j: z3.is_true(m.eval(hq[j], model_completion=True)) for j in hq}}, open(os.environ["MODEL_OUT"], "w"))
