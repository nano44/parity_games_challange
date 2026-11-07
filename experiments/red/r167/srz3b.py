#!/usr/bin/env python3
"""L-RED successor 39 (R168): srz3.py with TWO E3 lines A and B that ALTERNATE per phase, so that no driver restarts while its gates
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
SY = ["T", "QS"] + [f"{c}{j}" for j in range(1, J + 1) for c in ("A", "BB", "H")]
STATIC = os.environ.get("STATICESC") == "1"                # every gate aa_j (j >= 2) also gets a static escape hh_j (H_j) -> q
for L in LINES:
    SY += [f"BA3{L}", f"BBB{L}", f"R{L}0"] + [f"{c}{L}{j}" for j in range(1, J + 1) for c in ("R", "M", "X", "G")]
s = z3.Solver()
rk = {x: z3.Int(f"rk_{x}") for x in SY}; ev = {x: z3.Bool(f"ev_{x}") for x in SY}; pr = {x: z3.Bool(f"pr_{x}") for x in SY}
s.add(z3.Distinct(*rk.values())); s.add(ev["T"], pr["T"])
for x in SY:
    s.add(rk[x] >= 0, rk[x] < 10000)
    if x not in ("T", "QS"): s.add(rk[x] < rk["T"])        # QS (hps's tau-bar value vs the root's) is free: under tau-bar hps
                                                          # can reach the top ladder too
esc = {(L, j): z3.Int(f"esc_{L}{j}") for L in LINES for j in range(1, J + 1)}
for e in esc.values(): s.add(e >= 0, e <= 2)
if os.environ.get("UNIFORM") == "1":                       # period-2 shift-invariant placement for j >= 3 (extends to any m2)
    Dz = z3.Int("D")
    for j in range(3, J - 1):
        for c in ["A", "BB", "H"] + [c + L for L in LINES for c in ("R", "M", "X", "G")]:
            x, y = f"{c}{j}", f"{c}{j + 2}"
            s.add(rk[y] - rk[x] == Dz, pr[y] == pr[x], ev[y] == ev[x])
        for L in LINES: s.add(esc[L, j + 2] == esc[L, j])
TRUE = z3.BoolVal(True)
def better(S1, S2):
    D = sorted(set(S1) ^ set(S2))
    if not D: return z3.BoolVal(False)
    return z3.Or(*[z3.And(pr[e], (ev[e] if e in S1 else z3.Not(ev[e])), *[z3.Or(z3.Not(pr[f]), rk[f] < rk[e]) for f in D if f != e]) for e in D])
def evenwon(C):
    return z3.Or(*[z3.And(pr[e], ev[e], *[z3.Or(z3.Not(pr[f]), rk[f] < rk[e]) for f in C if f != e]) for e in C])
def graph(risen, pos, L3, mode="xi"):
    """pos[L] = (hs index, hps index); L3[L] in 'ab'. mode 'xi': Odd all options, Even fixed; 'w': Odd tau only, Even fixed;
    'tb': Odd tau only, Even ALL options (tau-bar); q's value is [] ('xi', 'w') or [QS] ('tb')."""
    G = {}; E = lambda lst: ("E", lst); O = lambda lst: ("O", lst)
    for j in range(1, J + 1):
        G[f"u{j}"] = E([(TRUE, [], f"aa{j}"), (TRUE, [], f"bb{j}")] if mode == "tb" else [(TRUE, [], f"aa{j}" if j in risen else f"bb{j}")])
        G[f"bb{j}"] = O([(TRUE, [f"BB{j}"], "q")])
        G[f"aa{j}"] = O([(TRUE, [f"A{j}"], "T")] if j == 1 else [(TRUE, [f"A{j}"], f"u{j - 1}")] + [(TRUE, [f"A{j}", f"G{L}{j}"], f"L3{L}") for L in LINES] + ([(TRUE, [f"A{j}", f"H{j}"], "q")] if STATIC else []))
        for L in LINES:
            G[f"rho{L}{j}"] = O([(TRUE, [f"R{L}{j}", f"M{L}{j}"], f"u{j}"), (esc[L, j] == 1, [f"R{L}{j}", f"X{L}{j}"], "q"), (esc[L, j] == 2, [f"R{L}{j}", f"X{L}{j}"], "T")])
    for L in LINES:
        G[f"rho{L}0"] = O([(TRUE, [f"R{L}0"], "q")])
        a, b = (TRUE, [f"BA3{L}"], f"hs{L}"), (TRUE, [f"BBB{L}"], f"hps{L}")
        G[f"L3{L}"] = E([a, b] if mode == "tb" else [a] if L3[L] == "a" else [b])
        odds = [j for j in range(1, J + 1) if j % 2]; evens = [0] + [j for j in range(2, J + 1, 2)]
        G[f"hs{L}"] = E([(TRUE, [], f"rho{L}{j}") for j in odds] if mode == "tb" else [(TRUE, [], f"rho{L}{pos[L][0]}")])
        G[f"hps{L}"] = E([(TRUE, [], f"rho{L}{j}") for j in evens] if mode == "tb" else [(TRUE, [], f"rho{L}{pos[L][1]}")])
    if mode in ("w", "tb"): G = {v: (o, lst[:1]) if o == "O" else (o, lst) for v, (o, lst) in G.items()}
    return G
def paths(G, v, qsym):
    out = []
    def go(x, conds, syms, stack):
        if x == "q": out.append((conds, syms + qsym)); return
        if x == "T": out.append((conds, syms + ["T"])); return
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
        if x in ("q", "T"): return
        if x in stack:
            i = stack.index(x); C = sum(symstack[i:], []); key = (tuple(sorted(stack[i:])), tuple(sorted(C)))
            if key not in seen: seen.add(key); cons.append(z3.Implies(z3.And(*conds) if conds else TRUE, evenwon(C) if C else z3.BoolVal(False)))
            return
        for c, sy, nx in G[x][1]: go(nx, conds + [c], stack + [x], symstack + [list(sy)])
    for v in G: go(v, [], [], [])
    return cons
TRACK = {}
SKIP1 = os.environ.get("SKIP1") == "1"
E2STAY = os.environ.get("E2STAY", "1") == "1"
def track(f, tag):
    b = z3.Bool(f"t{len(TRACK)}"); TRACK[b] = tag; s.assert_and_track(f, b)
def sw_req(G, GW, cur, tgt, L, who):
    """driver who in {'hs','hps'} of line L moves cur -> tgt: Xi-improving and W-better."""
    return z3.And(req(G, f"rho{L}{tgt}", [], f"rho{L}{cur}", []), req(GW, f"rho{L}{tgt}", [], f"rho{L}{cur}", []))
def stay(G, GW, L, cur, tgt, opts):
    return [z3.Not(z3.And(req(G, f"rho{L}{j}", [], f"rho{L}{cur}", []), req(GW, f"rho{L}{j}", [], f"rho{L}{tgt}", []))) for j in opts if j not in (cur, tgt)]
ODDS = [j for j in range(1, J + 1) if j % 2]; EVENS = [0] + [j for j in range(2, J + 1, 2)]
JO = J if J % 2 else J - 1; JE = J - 1 if J % 2 else J
def phase(P, O):
    """the schedule of P's phase: list of (risen, P-positions, P-L3, P-targets, reqs-builder, tag)."""
    st = [(set(), (1, H0), "b", (1, H0), [], f"{P}START")]
    for k in range(1, J - 1, 2):
        R = set(range(1, k + 1)); R1 = R | {k + 1}; hp = H0 if k == 1 else k - 1
        if k >= 3: st.append((R, (k - 2, hp), "b", (k, hp), ["CLIMB"], f"{P}CLIMB@{k}"))
        st.append((R, (k, hp), "b", (k, hp), ["CLOSED", "WAVE"], f"{P}CLOSED@{k}"))
        st.append((R, (k, hp), "a", (k, hp), ["OPEN"], f"{P}OPEN@{k}"))
        st.append((R1, (k, hp), "a", (k, k + 1), ["CLIMB2"] if hp != k + 1 else [], f"{P}CLIMB2@{k}"))
        st.append((R1, (k, k + 1), "a", (k, k + 1), ["FLIP"], f"{P}FLIP@{k}"))
        st.append((R1, (k, k + 1), "b", (k, k + 1), ["NEXT"], f"{P}NEXT@{k}"))
    return st
ONE = os.environ.get("ONEPHASE") == "1" or COPIES                    # control: phase A only, the idle line B already low (no restart anywhere)
if COPIES and os.environ.get("DROPIDLE") != "1":       # IDLE state of the copy: every reactor reset (unrisen), drivers high,
    for l3 in "ab":                                        # L3 free: the restart (both drivers) must be Xi-improving and W-better
        G = graph(set(), {"A": (JO, JE)}, {"A": l3}); GW = graph(set(), {"A": (JO, JE)}, {"A": l3}, "w")
        cs = cycles_ok(G) + [sw_req(G, GW, JO, 1, "A", "hs"), sw_req(G, GW, JE, H0, "A", "hps")]
        track(z3.Implies(z3.Bool("idle_l3a") if l3 == "a" else z3.Not(z3.Bool("idle_l3a")), z3.And(*cs)), "IDLE-RESTART")
for P, O in ((("A", "B"),) if ONE else (("A", "B"), ("B", "A"))):
    st = phase(P, O); n = len(st)
    lo = [z3.Bool(f"lo_{P}{i}") for i in range(n + 1)]                     # idle line O is low at state i (lo[n]: after the phase)
    s.add(lo[0] if ONE else z3.Not(lo[0]), lo[n]); [s.add(z3.Implies(lo[i], lo[i + 1])) for i in range(n)]
    for i, (risen, pp, l3, tg, kinds, tag) in enumerate(st):
        k = int(tag.split("@")[1]) if "@" in tag else 0
        if SKIP1 and k == 1: kinds = [x for x in kinds if x == "CLIMB2"]   # the first wave of a phase may be lost (as gate 2 in R167)
        for olo in (False, True):
            for ol3 in "ab":
                cfg = z3.And(lo[i] if olo else z3.Not(lo[i]), z3.Bool(f"l3_{P}{i}") if ol3 == "a" else z3.Not(z3.Bool(f"l3_{P}{i}")))
                opos = (1, H0) if olo else (JO, JE)
                if COPIES and not olo: continue
                pos = {P: pp, O: opos}; L3 = {P: l3, O: ol3}
                G = graph(risen, pos, L3); GW = graph(risen, pos, L3, "w")
                cons = cycles_ok(G)
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
                        cons.append(z3.Not(z3.And(req(G, f"aa{j}", [], f"bb{j}", []), req(GW, f"aa{j}", [], f"bb{j}", []))))
                for kind in kinds:
                    for GG, nm in ((G, ""), (GW, "W")):
                        if kind == "CLOSED" and nm == "W": continue
                        if kind == "CLIMB": cons.append(req(GG, f"rho{P}{k}", [], f"rho{P}{k - 2}", []))
                        if kind == "CLOSED": cons.append(req(GG, f"aa{k + 1}", [], f"bb{k + 1}", [], strict=False))
                        if kind == "WAVE": cons.append(req(GG, f"hs{P}", [f"BA3{P}"], f"hps{P}", []))
                        if kind == "OPEN": cons.append(req(GG, f"aa{k + 1}", [], f"bb{k + 1}", []))
                        if kind == "CLIMB2": cons.append(req(GG, f"rho{P}{k + 1}", [], f"rho{P}{pp[1]}", []))
                        if kind == "FLIP": cons.append(req(GG, f"hps{P}", [], f"hs{P}", [f"BA3{P}"]))
                        if kind == "NEXT": cons.append(req(GG, f"aa{k + 2}", [], f"bb{k + 2}", []))
                track(z3.Implies(cfg, z3.And(*cons) if cons else TRUE), f"{tag}")
if ITAU:   # I_tau = {}: at every Odd vertex with options, the alternative is not worse for Even than tau's edge, under tau-bar
    G = graph(set(), {"A": (1, H0), "B": (1, H0)}, {"A": "a", "B": "a"}, "tb"); q = ["QS"]
    for j in range(2, J + 1):
        for L in LINES:
            alt = paths({**G, "_x": ("O", [(TRUE, [f"A{j}", f"G{L}{j}"], f"L3{L}")])}, "_x", q); tau = paths(G, f"u{j - 1}", q)
            track(z3.Or(*[z3.And(cond(pa), *[z3.Implies(cond(pt), z3.Not(better(pt[1] + [f"A{j}"], pa[1]))) for pt in tau]) for pa in alt]), f"ITAU@aa{j}{L}")
    for L in LINES:
        for j in range(1, J + 1):
            tau = paths(G, f"u{j}", q)
            for e, tgt in ((1, ["QS"]), (2, ["T"])):
                track(z3.Implies(esc[L, j] == e, z3.Or(*[z3.Not(better(pt[1] + [f"M{L}{j}"], [f"X{L}{j}"] + tgt)) for pt in tau]) if False else
                      z3.And(*[z3.Not(better(pt[1] + [f"M{L}{j}"], [f"X{L}{j}"] + tgt)) for pt in tau])), f"ITAU@rho{L}{j}")
r = s.check()
print("J", J, "SKIP1", int(SKIP1), "STATIC", int(STATIC), "COPIES", int(COPIES), "ONEPHASE", int(ONE), "HPS0", H0, "ITAU", int(ITAU), "STAY", int(STAY), "->", r)
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
                   "D": m.eval(z3.Int("D")).as_long() if os.environ.get("UNIFORM") == "1" else None, "J": J}, open(os.environ["MODEL_OUT"], "w"))
