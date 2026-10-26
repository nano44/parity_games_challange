#!/usr/bin/env python3
"""Box 49 DATA (successor 29, queue item 3 (a)): the TIE and ODDC cycle changes of P-N5-OFFMONO-add-box49 §3, event by event.
For a TIE transition t -> t+1 of class c and each v in N (Odd, kappa unchanged): y1 := next_t(v), y2 := next_{t+1}(v); reports
  c's parity, v in Z_t(c) or not, d1 := kappa_{t+1}(y1) - kappa_t(y1) (sign), kappa_t(y2) vs kappa_t(y1) (the option was tied at t or worse),
  and whether some Even vertex switched at t -> t+1 (ESW).
For an ODDC transition (c in Q, only c's own choice changed): s1 := next_t(c), s2 := next_{t+1}(c), index order, and kappa_{t+1}(s1).
Characterisation checks (every in-phase state / transition, every class c; A_t := path-free vertices of U_c - {c} (P = empty, kappa in
F := {(0, s_c l) : 1 <= l <= n-1})):
  CHAR_V   an Odd x in A_t whose next_t(x) is not the argmin over its path-free successors y in U_c (A_t or c) of (kappa_t(y), tb_t(y)),
           tb = the index of y (c even) or the index sequence of y's honest path read from c (c odd; empty for c);
  FT_V     a transition at which A changes or some x in A_t n A_{t+1} changes next_t(x), and no z in U_c - {c} has kappa_t(z) != kappa_{t+1}(z)
           with kappa_t(z) in F or kappa_{t+1}(z) in F (Lemma TIE-CHARGE, draft);
  FTCOUNT  per phase and class, the transitions with an F-touching kappa change (FTX) must be <= 2 (n-1)(|U_c|-1): FTB_V.
Controls (CHAR_V must bite): MUT=1 index tie-break for both parities; MUT=2 path-sequence tie-break for both; MUT=3 reversed index.
Per phase and class: TIE_c, ODDC_c, ZCH_c, len. Prints the totals, the per-phase maxima and (VERB=1) one line per event.
Usage: tie.py STARTS SEED (--list FILE | files) [--nmax N] [--start F]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart, M
C = {}; TOP = []
VERB = os.environ.get("VERB") == "1"; MUT = os.environ.get("MUT", "0")
def inc(k, v=1): C[k] = C.get(k, 0) + v
def mx(k, v): C[k] = max(C.get(k, v), v)
def cyc_seq(A, c):
    nx = A["nxt"]; out, x = [c], nx[c]
    while x != c and len(out) <= len(nx): out.append(x); x = nx[x]
    return tuple(out)
def sgn(a, b): return ">" if a > b else ("<" if a < b else "=")
def phase_events(g, E, R, i, j, Q, nm):
    """Yields per class c: (c, tie, oddc, zch, events)."""
    n = g.n
    for c in sorted({R[i]["vs"][v][0] for v in range(n)}):
        sc = 1 if E.par[c] == 1 else -1
        kap = lambda S, v: (M(E, S["vs"][v]), sc * S["vs"][v][2])
        tie = oddc = zch = 0; ev = []
        for k in range(i, j):
            A, B = R[k], R[k + 1]
            za, zb = cyc_seq(A, c), cyc_seq(B, c)
            if za == zb: continue
            zch += 1; N = [v for v in zb if v != c and A["nxt"][v] != B["nxt"][v]]
            if any(kap(B, v) > kap(A, v) for v in N): continue
            esw = any(A["s"][x] != B["s"][x] for x in range(n) if g.owner[x] == 0)
            if N:
                tie += 1
                for v in N:
                    y1, y2 = A["nxt"][v], B["nxt"][v]
                    ev.append(("TIE", k - i, c, "odd" if E.par[c] == 1 else "even", v, "onZt" if v in za else "offZt", y1, y2,
                               "y1:" + sgn(kap(B, y1), kap(A, y1)), "y2_t-vs-y1_t:" + sgn(kap(A, y2), kap(A, y1)),
                               "y2:" + sgn(kap(B, y2), kap(A, y2)), "ESW" if esw else "noESW", "y2<y1" if y2 < y1 else "y2>y1"))
            elif c in Q:
                oddc += 1; s1, s2 = A["nxt"][c], B["nxt"][c]
                ev.append(("ODDC", k - i, c, s1, s2, "s2<s1" if s2 < s1 else "s2>s1", "s1:" + sgn(kap(B, s1), kap(A, s1)),
                           "M_t+1(s1)=" + str(kap(B, s1)[0]), "ESW" if esw else "noESW"))
        yield c, tie, oddc, zch, ev
def seq(S, c, x):
    out = []
    while x != c and len(out) <= len(S["nxt"]): out.append(x); x = S["nxt"][x]
    return tuple(reversed(out))
def charcheck(g, E, R, i, j):
    n = g.n
    for c in sorted({R[i]["vs"][v][0] for v in range(n)}):
        U = [v for v in range(n) if R[i]["vs"][v][0] == c]; Us = set(U)
        sc = 1 if E.par[c] == 1 else -1
        def A(S): return {x for x in U if x != c and M(E, S["vs"][x]) == 0}
        def kap(S, v): return (M(E, S["vs"][v]), sc * S["vs"][v][2])
        def tb(S, y):
            if MUT == "1": return (y,)                   # control: index tie-break for both parities (must bite on odd c)
            if MUT == "2": return seq(S, c, y)           # control: path-sequence tie-break for both parities (must bite on even c)
            if MUT == "3": return (-y,)                  # control: reversed index
            return (y,) if E.par[c] == 0 else seq(S, c, y)
        F = lambda k: k[0] == 0 and k[1] != 0
        ftx = 0
        for k in range(i, j + 1):
            S = R[k]; As = A(S)
            for x in As:
                if g.owner[x] != 1: continue
                opts = [y for y in g.succ[x] if y in Us and (y == c or y in As)]
                best = min(opts, key=lambda y: (kap(S, y), tb(S, y)))
                inc("char_checks")
                if best != S["nxt"][x]: inc("CHAR_V")
            if k == j: break
            T = R[k + 1]; At = A(T)
            ft = any(kap(S, z) != kap(T, z) and (F(kap(S, z)) or F(kap(T, z))) for z in U if z != c)
            if ft: ftx += 1
            chg = As != At or any(S["nxt"][x] != T["nxt"][x] for x in As & At)
            if chg: inc("A_next_changes")
            if chg and not ft: inc("FT_V")
        inc("FTX", ftx)
        if ftx > 2 * (n - 1) * (len(U) - 1): inc("FTB_V")
def run(g, start, nm):
    E, R = rows(g, start)
    Q = {v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2}
    for i, j in phases(R):
        inc("phases"); inc("trans", j - i)
        charcheck(g, E, R, i, j)
        for c, tie, oddc, zch, ev in phase_events(g, E, R, i, j, Q, nm):
            inc("TIE", tie); inc("ODDC", oddc); inc("ZCH", zch); mx("max_TIE", tie); mx("max_ODDC", oddc)
            for e in ev:
                inc("ev_" + e[0]); inc("|".join(str(x) for x in (e[0],) + tuple(y for y in e if isinstance(y, str) and (":" in y or y in ("onZt", "offZt", "ESW", "noESW", "odd", "even", "y2<y1", "y2>y1", "s2<s1", "s2>s1")))))
                if VERB: print("  ", nm, *e)
            if tie or oddc: TOP.append((tie + oddc, tie, oddc, zch, j - i, g.n, nm))
if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9; fixed = None
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    if "--start" in a: i = a.index("--start"); fixed = readstart(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    if a[0] == "--list":
        gs = [(l.split()[0], load(os.path.join(ROOT, l.split()[0]))) for l in open(a[1]) if l.strip() and not l.startswith("#")]
    else: gs = [(f, load(f)) for f in a]
    for nm, g in gs:
        if g.n > nmax: continue
        sts = [fixed] if fixed else [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: run(g, st, nm)
            except RecursionError: inc("RECERR")
    for k in ("CHAR_V", "FT_V", "FTB_V"): C.setdefault(k, 0)
    for k, v in sorted(C.items()): print(k, v)
    for w in sorted(TOP, reverse=True)[:10]: print("  top (TIE+ODDC TIE ODDC ZCH len n name):", *w)
