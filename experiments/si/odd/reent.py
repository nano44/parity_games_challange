#!/usr/bin/env python3
"""L-SI box 33 (docs/si/N5-ODD-box33.md): Odd's re-entries on plain N5 (box21/n5x.trace, read only) against R86 COMPOSE's Odd side.
U_t, tbar_t := Ed.evaluate(tau_t) on G^d (R86's U). For Odd o, an ENTRY into e is a transition r -> r+1 with tau_r(o) != e = tau_{r+1}(o);
a RE-ENTRY is an entry into an e that o held earlier; s is the transition at which o last left e (s < r).
Per re-entry, at state r (before the switch), protection as L-NEW's ODD-FREEZE (exact H1 form, box63 §1): P_e := (tau_r, tbar_r)-play
from e cut at the first visit of o (o included); H1 it reaches o; H2 the play from tau_r(o) has no vertex of P_e; H3 the top of P_e
has even priority and is more relevant than the cycle node of tau_r(o)'s play. PROT_V counts re-entries with H1-H3 all true (must be 0).
Class of the re-entry: X (H1 fails: e's play never comes back to o), Y (H1, not H2), Z (H1, H2, not H3).
Charge (R86 Lemma SW-RETURN, Odd side): U(e) changes at some transition t in [s, r-1] (else SWR_V). Each change of U(e) is one of
LAM (cycle node of U(e) changes), CAR (P changes and is not MATCHED, read with G^d's parities, R85/R86 F3), MAT (matched P-change),
LEN (length only). The re-entry's charge class is the strongest kind in its window: LAM > CAR > MAT > LEN.
COPY: a change of U(e) at t with U(o) changing at t by the SAME P-difference and the same cycle node (e's change is o's change seen
through e's prefix). Prints per game: iterations, tau-changes, lambda^U-runs, re-entries, classes, charges, the most re-entries of
one Odd vertex, NM^U max per vertex per lambda^U-run, and counters. Usage: reent.py GAME.pg [START] [--mut]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "chg"))
from n5x import load, trace, Engine, dual, readstart
from compose import matched, bits

args = [a for a in sys.argv[1:] if not a.startswith("--")]; MUT = "--mut" in sys.argv
g = load(args[0]); n = g.n
st, fb = trace(g, readstart(args[1]) if len(args) > 1 else None, check=False)
Ed = Engine(dual(g)); T = len(st) - 1
UT = [Ed.evaluate(s[1]) for s in st]; U = [u for u, _ in UT]
rk2v = {Ed.rank[v]: v for v in range(n)}; odd = lambda r: Ed.par[rk2v[r]] == 1       # G^d's parities (F3)

def kind(a, b):
    if a == b: return None
    if a[0] != b[0]: return "LAM"
    if a[1] == b[1]: return "LEN"
    rc = Ed.rank[a[0]]; w = lambda r: (r - rc) if not odd(r) else -(r - rc)
    return "MAT" if matched(bits(a[1]), bits(b[1]), w, odd) else "CAR"

def play(t, tb, x, stop=None):
    path, seen = [], set()
    while x not in seen:
        seen.add(x); path.append(x)
        if x == stop: return path, True
        x = t[x] if g.owner[x] == 1 else tb[x]
    return path, x                                   # x = first repeated vertex; the cycle is path[path.index(x):]

def prot(r, o, e):
    t = st[r][1]; tb = UT[r][1]
    pe, hit = play(t, tb, e, stop=o)
    if hit is not True: return "X"
    po, x = play(t, tb, t[o])
    if set(po) & set(pe): return "Y"
    cyc = po[po.index(x):]; wn = max(cyc, key=lambda v: Ed.rank[v])
    top = max(pe, key=lambda v: Ed.rank[v])
    h3 = g.prio[top] % 2 == 0 and Ed.rank[top] > Ed.rank[wn]
    if MUT: h3 = not h3
    return "P" if h3 else "Z"

C = Counter(); per_o = Counter(); per_oe = Counter(); ex = {}
tauch = sum(1 for k in range(T) if st[k][1] != st[k + 1][1])
lam = [tuple(u[v][0] for v in range(n)) for u in U]
runs = [0]
for k in range(T):
    if lam[k + 1] != lam[k]: runs.append(k + 1)
# NM^U per vertex per lambda^U-run
nmmax = 0
for i, j in zip(runs, runs[1:] + [T + 1]):
    for x in range(n):
        c = sum(1 for t in range(i, j - 1) if kind(U[t][x], U[t + 1][x]) == "CAR")
        nmmax = max(nmmax, c)
for o in range(n):
    if g.owner[o] != 1: continue
    held = {st[0][1][o]: None}; last_leave = {}
    for r in range(T):
        a, b = st[r][1][o], st[r + 1][1][o]
        if a == b: continue
        last_leave[a] = r
        e = b
        if e in held:
            s = last_leave[e]; C["reentries"] += 1; per_o[o] += 1; per_oe[(o, e)] += 1
            cl = prot(r, o, e); C["class_" + cl] += 1
            if lam[r] != lam[r + 1]: C["lamchg_at_" + cl] += 1
            if U[r][o][0] != U[r + 1][o][0]: C["lamo_at_" + cl] += 1
            if cl == "P": C["PROT_V"] += 1; ex.setdefault("PROT", (r, o, e))
            ks = [(t, kind(U[t][e], U[t + 1][e])) for t in range(s, r)]
            ks = [(t, k) for t, k in ks if k]
            if not ks: C["SWR_V"] += 1; ex.setdefault("SWR", (r, o, e, s)); continue
            best = min((k for _, k in ks), key=["LAM", "CAR", "MAT", "LEN"].index); C["charge_" + best] += 1
            C["charge_" + best + "_" + cl] += 1
            if best == "LEN":                                    # Lemma LEN-REENTRY: (c, P) of U(tau_t(o)) = that of U(e), t in [s, r]
                cp = U[r][e][:2]
                if any(U[t][st[t][1][o]][:2] != cp or U[t][e][:2] != cp for t in range(s, r + 1)) ^ MUT: C["LENTIE_V"] += 1; ex.setdefault("LENTIE", (r, o, e, s))
            for t, k in ks:
                C["wchg"] += 1
                if U[t][o][0] == U[t][e][0] and U[t + 1][o][0] == U[t + 1][e][0] and \
                   (U[t][o][1] ^ U[t + 1][o][1]) == (U[t][e][1] ^ U[t + 1][e][1]) and U[t][o] != U[t + 1][o]:
                    C["wchg_COPY"] += 1
        held[e] = None
# per lambda^U-run R and Odd pair (o, e): ENT_R(o, e) against 1 + NM^U_R(e) (CONJECTURE ENT-NM) and 1 + PCH^U_R(e)
for i, j in zip(runs, runs[1:] + [T + 1]):
    nmR = Counter(); pchR = Counter(); ent = Counter()
    for t in range(i, j - 1):
        for x in range(n):
            k = kind(U[t][x], U[t + 1][x])
            if k in ("CAR", "MAT"): pchR[x] += 1
            if k == "CAR": nmR[x] += 1
        for o in range(n):
            if g.owner[o] == 1 and st[t][1][o] != st[t + 1][1][o]: ent[(o, st[t + 1][1][o])] += 1
    for (o, e), c in ent.items():
        C["pairs"] += 1
        if c > 1 + nmR[e]: C["ENTNM_V"] += 1; ex.setdefault("ENTNM", (i, j, o, e, c, nmR[e]))
        if c > 1 + pchR[e]: C["ENTPCH_V"] += 1; ex.setdefault("ENTPCH", (i, j, o, e, c, pchR[e]))
mx = max(per_o.values(), default=0); mxe = max(per_oe.values(), default=0)
print(f"REENT {os.path.basename(args[0])} n {n} m {sum(len(s) for s in g.succ)} iter {T} fb {fb} tau_changes {tauch} lamU_runs {len(runs)} "
      f"reentries {C['reentries']} odd_reentering {len(per_o)} max_per_o {mx} max_per_oe {mxe} NMU_max {nmmax} "
      + " ".join(f"{k} {C[k]}" for k in sorted(C) if k != "reentries") + f" ex {ex}"
      + (" PASS" if C["PROT_V"] == 0 and C["SWR_V"] == 0 and C["LENTIE_V"] == 0 else " FAIL"), flush=True)
