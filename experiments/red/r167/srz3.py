#!/usr/bin/env python3
"""L-RED successor 39 (R167): EXACT order-constraint model of a level-2 gate + re-climbing level-3 driver pair inside one W-run (z3).
Abstract Xi-graph (all values relative to the common tail q = Xi(hps), the E2 reset driver; T = the current outer root, an even
symbol above every band symbol, reached only through u_1's advance side):
  u_j (Even, E2 reactor, j = 1..J): risen -> aa_j, unrisen -> bb_j.   bb_j (Odd, BB_j) -> q.
  aa_1 (Odd, A_1) -> T.   aa_j (j >= 2, Odd, A_j) -> {u_(j-1), gg_j};  gg_j (Odd, G_j) -> L3 (the E3 head).
  L3: a-state (wave done) -> L3A (BA3) -> hs2;  b-state -> L3B (BBB) -> hps2.   hs2 rides odd riders, hps2 rides rho_0 and even riders.
  rider rho_j (Odd, R_j) -> {mdd_j (M_j) -> u_j} + optional escape x_j (X_j) -> q or -> T (per-j choice: none / q / T). rho_0 (R_0) -> q.
Every symbol: free rank, free parity, free presence (absent = inert). Xi(v) = Odd's minimum over the simple paths of the Xi-graph
(Even's choices fixed by the state); every cycle Odd could close must be Even-won (top present symbol even), else Odd closes it.
Value order: the top present symbol of the symmetric difference decides (even: its side is better for Even; odd: worse).
Requirements, for the waves k = 3 and k = 5 (J = 7) and the phase restart (S4a: a switch must be Xi-improving):
  RESTART hs2: risen {1}: Xi(rho_1) > Xi(rho_7).   RESTART hps2: risen {1, 2}, hs2 on rho_1: Xi(rho_2) > Xi(rho_6).
  CLIMB: risen 1..k, hs2 on rho_(k-2), hps2 on rho_(k-1), L3 b: Xi(rho_k) > Xi(rho_(k-2)).
  CLOSED: risen 1..k, hs2 on rho_k, hps2 on rho_(k-1), L3 b: Xi(aa_(k+1)) <= Xi(bb_(k+1)); and the E3 wave is Xi-improving there:
          BA3 + Xi(hs2) > Xi(hps2).
  OPEN: same, L3 a: Xi(aa_(k+1)) > Xi(bb_(k+1)).
  CLIMB2: risen 1..k+1, L3 a: Xi(rho_(k+1)) > Xi(rho_(k-1)) (hps2 switches).   FLIP: hps2 on rho_(k+1), L3 a: Xi(hps2) > BA3 + Xi(hs2).
  NEXT: hps2 on rho_(k+1), L3 b: Xi(aa_(k+2)) > Xi(bb_(k+2)) (the next E2 step is not blocked forever).
W (the ladder T decides every W choice; tau fixed) and I_tau = {} are NOT modelled (assumed). Prints sat + a model, or unsat.
Env ESCQ=0 forbids escapes to q (the non-self-referential horn only), ESCT=0 forbids escapes to T. Usage: srz3.py [J]"""
import sys, os, itertools
import z3
J = int(sys.argv[1]) if len(sys.argv) > 1 else 7
SY = ["T", "BA3", "BBB", "R0"] + [f"{c}{j}" for j in range(1, J + 1) for c in ("R", "M", "X", "A", "G", "BB")]
s = z3.Solver()
rk = {x: z3.Int(f"rk_{x}") for x in SY}; ev = {x: z3.Bool(f"ev_{x}") for x in SY}; pr = {x: z3.Bool(f"pr_{x}") for x in SY}
s.add(z3.Distinct(*rk.values()))
for x in SY: s.add(rk[x] >= 0, rk[x] < 1000)
s.add(ev["T"], pr["T"])
TFREE = os.environ.get("TFREE") == "1"                     # the outer root's symbol T may sit below band symbols (R165 case 2)
WREQ = TFREE or os.environ.get("WREQ") == "1"              # also require every switch to be W-better (S4a's W-optimum, tau-graph)
if not TFREE:
    for x in SY:
        if x != "T": s.add(rk[x] < rk["T"])
esc = {j: z3.Int(f"esc_{j}") for j in range(1, J + 1)}          # 0 none, 1 -> q, 2 -> T
UNIFORM = os.environ.get("UNIFORM") == "1"                 # period-2 shift-invariant placement for j >= 3 (extends to any m2)
if UNIFORM:
    Dz = z3.Int("D")
    for c in ("R", "M", "X", "A", "G", "BB"):
        for j in range(3, J - 1):
            s.add(rk[f"{c}{j + 2}"] - rk[f"{c}{j}"] == Dz, pr[f"{c}{j + 2}"] == pr[f"{c}{j}"], ev[f"{c}{j + 2}"] == ev[f"{c}{j}"])
    for j in range(3, J - 1): s.add(esc[j + 2] == esc[j])
for j in esc:
    s.add(esc[j] >= 0, esc[j] <= 2)
    if os.environ.get("ESCQ") == "0": s.add(esc[j] != 1)
    if os.environ.get("ESCT") == "0": s.add(esc[j] != 2)
def better(S1, S2):
    """z3 formula: value S1 strictly better for Even than S2 (top present symbol of the symmetric difference is good for S1)."""
    D = sorted(set(S1) ^ set(S2))
    if not D: return z3.BoolVal(False)
    return z3.Or(*[z3.And(pr[e], (ev[e] if e in S1 else z3.Not(ev[e])), *[z3.Or(z3.Not(pr[f]), rk[f] < rk[e]) for f in D if f != e]) for e in D])
def evenwon(C):
    return z3.Or(*[z3.And(pr[e], ev[e], *[z3.Or(z3.Not(pr[f]), rk[f] < rk[e]) for f in C if f != e]) for e in C])
def graph(risen, hs2, hps2, L3, W=False):
    """successors: Odd vertices list [(cond, (symbols, next))]; Even fixed. Sinks 'q' (empty) and 'T'."""
    G = {}
    for j in range(1, J + 1):
        G[f"u{j}"] = ("E", [(z3.BoolVal(True), [], f"aa{j}" if j in risen else f"bb{j}")])
        G[f"bb{j}"] = ("O", [(z3.BoolVal(True), [f"BB{j}"], "q")])
        G[f"aa{j}"] = ("O", [(z3.BoolVal(True), [f"A{j}"], "T")] if j == 1 else [(z3.BoolVal(True), [f"A{j}"], f"u{j - 1}"), (z3.BoolVal(True), [f"A{j}", f"G{j}"], "L3")])
        G[f"rho{j}"] = ("O", [(z3.BoolVal(True), [f"R{j}", f"M{j}"], f"u{j}"), (esc[j] == 1, [f"R{j}", f"X{j}"], "q"), (esc[j] == 2, [f"R{j}", f"X{j}"], "T")])
    G["rho0"] = ("O", [(z3.BoolVal(True), ["R0"], "q")])
    G["L3"] = ("E", [(z3.BoolVal(True), ["BA3"], "hs2")] if L3 == "a" else [(z3.BoolVal(True), ["BBB"], "hps2")])
    G["hs2"] = ("E", [(z3.BoolVal(True), [], f"rho{hs2}")]); G["hps2"] = ("E", [(z3.BoolVal(True), [], f"rho{hps2}")])
    if W:                                                    # tau-graph: every Odd vertex keeps its tau edge (the first) only
        G = {v: (o, lst[:1]) for v, (o, lst) in G.items()}
    return G
def paths(G, v):
    """simple paths from v: list of (condition list, symbol list, end) where end in {q, T} or ('cyc', symbols-of-cycle)."""
    out = []
    def go(x, conds, syms, stack):
        if x in ("q", "T"): out.append((conds, syms + (["T"] if x == "T" else []), x)); return
        if x in stack:
            i = stack.index(x); cyc = []
            for y in stack[i:]: pass
            out.append((conds, None, ("cyc", tuple(stack[i:])))); return
        for c, sy, nx in G[x][1]: go(nx, conds + [c], syms + sy, stack + [x])
    go(v, [], [], [])
    return out
def cycsyms(G, cyc, conds):
    return None
def xi_req(G, v1, extra1, v2, extra2, strict=True):
    """Xi(v1)+extra1 > Xi(v2)+extra2 (strict) or <= (not strict). Paths ending in a cycle: the cycle must be Even-won (added as a
    side constraint per state); such paths are never Odd's choice, so they are dropped."""
    P1 = [p for p in paths(G, v1) if p[1] is not None]; P2 = [p for p in paths(G, v2) if p[1] is not None]
    A = lambda p: z3.And(*p[0]) if p[0] else z3.BoolVal(True)
    if strict:   # min(P1) > min(P2): every available p1 beats some available p2
        return z3.And(*[z3.Implies(A(p1), z3.Or(*[z3.And(A(p2), better(p1[1] + extra1, p2[1] + extra2)) for p2 in P2])) for p1 in P1])
    return z3.Or(*[z3.And(A(p1), *[z3.Implies(A(p2), z3.Not(better(p1[1] + extra1, p2[1] + extra2))) for p2 in P2]) for p1 in P1])
def cycles_ok(G):
    """every cycle reachable by Odd's options (with its edge conditions) must be Even-won."""
    cons = []; seen = set()
    def go(x, conds, syms, stack, symstack):
        if x in ("q", "T"): return
        if x in stack:
            i = stack.index(x); C = sum(symstack[i:], []); key = (tuple(sorted(stack[i:])), tuple(sorted(C)))
            if key not in seen: seen.add(key); cons.append(z3.Implies(z3.And(*conds) if conds else z3.BoolVal(True), evenwon(C) if C else z3.BoolVal(False)))
            return
        for c, sy, nx in G[x][1]: go(nx, conds + [c], syms + sy, stack + [x], symstack + [list(sy)])
    for v in G: go(v, [], [], [], [])
    return cons
DROP = set(os.environ.get("DROP", "").split(","))         # requirement groups to drop (sanity: each drop should restore sat)
TRACK = {}
STAY = os.environ.get("STAY") == "1"                      # also: no driver makes an UNINTENDED switch (S4a: W-optimum among
ODDS = [j for j in range(1, J + 1) if j % 2]; EVENS = [0] + [j for j in range(2, J + 1, 2)]   # the Xi-improving options)
def stay_cons(G, GW, cur, tgt, opts):
    out = []
    for j in opts:
        if j in (cur, tgt): continue
        out.append(z3.Not(z3.And(xi_req(G, f"rho{j}", [], f"rho{cur}", []), xi_req(GW, f"rho{j}", [], f"rho{tgt}", []))))
    return out
def state(risen, hs2, hps2, L3, reqs, tags, wreqs=(), go=None):
    G = graph(risen, hs2, hps2, L3)
    if STAY:
        GW0 = graph(risen, hs2, hps2, L3, W=True); t1, t2 = go if go else (hs2, hps2)
        for c in stay_cons(G, GW0, hs2, t1, ODDS) + stay_cons(G, GW0, hps2, t2, EVENS):
            b = z3.Bool(f"T_STAY{len(TRACK)}"); TRACK[b] = f"STAY@{sorted(risen)[-1] if risen else 0}{L3}"; s.assert_and_track(c, b)
    if WREQ:
        GW = graph(risen, hs2, hps2, L3, W=True)
        for r, tag in wreqs:
            if tag.split("@")[0] in DROP: continue
            b = z3.Bool(f"T_W{tag}"); TRACK[b] = "W" + tag; s.assert_and_track(r(GW), b)
    for c in cycles_ok(G): s.add(c)
    for r, tag in zip(reqs, tags):
        if tag.split("@")[0] in DROP: continue
        b = z3.Bool(f"T_{tag}"); TRACK[b] = tag; s.assert_and_track(r(G), b)
odd_top = J if J % 2 else J - 1; even_top = J - 1 if J % 2 else J
PHASE1 = os.environ.get("PHASE1") == "1"                  # one phase only: drivers start on rho_1 / rho_0, no restart, waves k = 1, 3, ...
if PHASE1:
    state(set(), 1, 0, "b", [], [])
if not PHASE1: state({1}, odd_top, even_top, "a", [lambda G: xi_req(G, "rho1", [], f"rho{odd_top}", [])], ["RESTART@hs2"],
      [(lambda G: xi_req(G, "rho1", [], f"rho{odd_top}", []), "RESTART@hs2")], go=(1, even_top))
HPSLATE = os.environ.get("HPSLATE") == "1"                # variant: hps2 does not restart at step 2; it stays on its top rider
if not HPSLATE and not PHASE1:                             # until the k = 3 wave and then switches straight to rho_4
    state({1, 2}, 1, even_top, "a", [lambda G: xi_req(G, "rho2", [], f"rho{even_top}", [])], ["RESTART@hps2"],
          [(lambda G: xi_req(G, "rho2", [], f"rho{even_top}", []), "RESTART@hps2")], go=(1, 2))
for k in range(1 if PHASE1 else 3, J - 1, 2):
    R = set(range(1, k + 1)); R1 = R | {k + 1}
    hp_ = even_top if (HPSLATE and k == 3) else k - 1
    if k >= 3: state(R, k - 2, hp_, "b", [lambda G, k=k: xi_req(G, f"rho{k}", [], f"rho{k - 2}", [])], [f"CLIMB@{k}"],
          [(lambda G, k=k: xi_req(G, f"rho{k}", [], f"rho{k - 2}", []), f"CLIMB@{k}")], go=(k, hp_))
    state(R, k, hp_, "b", [lambda G, k=k: xi_req(G, f"aa{k + 1}", [], f"bb{k + 1}", [], strict=False), lambda G: xi_req(G, "hs2", ["BA3"], "hps2", [])], [f"CLOSED@{k}", f"WAVE@{k}"],
          [(lambda G: xi_req(G, "hs2", ["BA3"], "hps2", []), f"WAVE@{k}")])
    state(R, k, hp_, "a", [lambda G, k=k: xi_req(G, f"aa{k + 1}", [], f"bb{k + 1}", [])], [f"OPEN@{k}"],
          [(lambda G, k=k: xi_req(G, f"aa{k + 1}", [], f"bb{k + 1}", []), f"OPEN@{k}")])
    state(R1, k, hp_, "a", [lambda G, k=k, hp_=hp_: xi_req(G, f"rho{k + 1}", [], f"rho{hp_}", [])], [f"CLIMB2@{k}"],
          [(lambda G, k=k, hp_=hp_: xi_req(G, f"rho{k + 1}", [], f"rho{hp_}", []), f"CLIMB2@{k}")], go=(k, k + 1))
    state(R1, k, k + 1, "a", [lambda G: xi_req(G, "hps2", [], "hs2", ["BA3"])], [f"FLIP@{k}"],
          [(lambda G: xi_req(G, "hps2", [], "hs2", ["BA3"]), f"FLIP@{k}")])
    state(R1, k, k + 1, "b", [lambda G, k=k: xi_req(G, f"aa{k + 2}", [], f"bb{k + 2}", [])], [f"NEXT@{k}"],
          [(lambda G, k=k: xi_req(G, f"aa{k + 2}", [], f"bb{k + 2}", []), f"NEXT@{k}")])
r = s.check()
if r == z3.unsat: print("unsat core:", sorted(TRACK[b] for b in s.unsat_core()))
print("J", J, "TFREE", int(TFREE), "WREQ", int(WREQ), "HPSLATE", int(HPSLATE), "ESCQ", os.environ.get("ESCQ", "1"), "ESCT", os.environ.get("ESCT", "1"), "->", r)
if r == z3.sat:
    m = s.model()
    order = sorted((m.eval(rk[x]).as_long(), x) for x in SY if z3.is_true(m.eval(pr[x])))
    print("ascending:", " < ".join(f"{x}{'+' if z3.is_true(m.eval(ev[x])) else '-'}" for _, x in order))
    print("inert:", [x for x in SY if not z3.is_true(m.eval(pr[x]))]); print("esc:", {j: m.eval(esc[j]).as_long() for j in esc})
    if UNIFORM: print("D", m.eval(Dz))
    import json
    if os.environ.get("MODEL_OUT"):
        json.dump({"rank": {x: m.eval(rk[x]).as_long() for x in SY}, "even": {x: z3.is_true(m.eval(ev[x])) for x in SY},
                   "present": {x: z3.is_true(m.eval(pr[x])) for x in SY}, "esc": {j: m.eval(esc[j]).as_long() for j in esc},
                   "D": m.eval(Dz).as_long() if UNIFORM else None, "J": J}, open(os.environ["MODEL_OUT"], "w"))
