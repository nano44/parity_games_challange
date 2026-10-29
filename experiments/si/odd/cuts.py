#!/usr/bin/env python3
"""L-SI box 40 (docs/si/N5-CUT-box40.md): re-entries across cuts, Even side, plain N5 run. A CUT is a transition t -> t+1 that is not a
guided S4a step with tau constant (a tau-change or an S4c fallback, or both). A PIECE is a maximal run of states joined by guided transitions.
For every lambda-run (of Xi) and every Even v, every re-entry of v into c (transition j-1 -> j with sigma_j(v) = c, after a leave of c at
s -> s+1 inside the same lambda-run) is classified:
  CUTRE   the re-entry transition j-1 -> j is itself a cut;
  FRESH   no anchor: no state q-1 in [max(s, p0), j-2] (p0 = first state of j's piece) with (v, c) in H_{q-1} = sigma_{q-1} ∪ I_sigma_{q-1};
  CYC     an anchor q exists (smallest) and v is its own W-cycle node at some state of [q, j];
  WPAID   W(c) changes on [q, j] (W_t = val(sigma_t, tau_t) on G_tau);
  SILENT  W(c) constant on [q, j] and W_j(sigma_{j-1} v) = W_j(c)  (Lemma W-RETURN-G's conclusion);
  VIOL    W(c) constant on [q, j], not silent: Lemma W-RETURN-G FAILS (must be 0). Controls that must fire: MUT=off1 (anchor q = j allowed,
          an empty chain), MUT=nofresh (anchor allowed before the piece, i.e. across a cut).
  XCUT    re-entries whose out-window [s, j) contains a cut (the ones box 39's per-pair bound charges to G_vc).
FR=1: a transition is GUIDED iff S4a moved sigma (tau_{t+1} free), and W in the chain is read against tau_{j-1} (the frame of the
re-entry's arena); pieces still have tau constant. CUTRE_T / FRESH_T: the attached cut changes tau. FRESH0: the re-entry is the first
transition of its piece. LRISE_V: a FRESH re-entry with j-1 > piece start and no change of Xi(c) at j-2 -> j-1 (LATE-RISE; must be 0).
Per pair: G = transitions inside span(v, c) that are not guided (default mode: Even fallbacks and tau-changes = B_vc); maxima of FRESH + CUTRE per pair, of G per pair, of XCUT per pair. Usage: cuts.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21"))
from n5x import load, trace, Engine, dual, readstart
import pg
args = [a for a in sys.argv[1:] if not a.startswith("--")]; MUT = os.environ.get("MUT", "")
g = load(args[0]); n = g.n; E = Engine(g)
ev = [v for v in range(n) if g.owner[v] == 0]
st, _ = trace(g, readstart(args[1]) if len(args) > 1 else None, check=False); T = len(st) - 1
S = [tuple(s[0]) for s in st]; TAU = [tuple(s[1]) for s in st]
XI = [E.evaluate(s) for s in S]
IMP = [set(E.improving(S[t], XI[t][0])) for t in range(T + 1)]
def br(t):
    sigma, tau = S[t], TAU[t]; imp = IMP[t]
    if not imp: return sigma
    opt = {v: {sigma[v]} for v in ev}
    for v, w in imp: opt[v].add(w)
    succ = [sorted(opt[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(g.owner), succ)))
    _, best = Er.evaluate(tuple(tau[v] if g.owner[v] == 1 else -1 for v in range(n)))
    return tuple(best[v] if g.owner[v] == 0 else -1 for v in range(n))
FR = os.environ.get("FR", "") == "1"     # FR=1: a transition is guided iff S4a moved sigma (tau_{t+1} free); W read in tau_{j-1}'s frame
s4a = [S[t + 1] == br(t) and S[t + 1] != S[t] for t in range(T)]
guided = [s4a[t] and (FR or TAU[t + 1] == TAU[t]) for t in range(T)]
p0 = [0] * (T + 1)                       # first state of t's piece: tau constant, transitions S4a
for t in range(1, T + 1): p0[t] = p0[t - 1] if (guided[t - 1] and TAU[t] == TAU[t - 1]) else t
WE = {}
def wval(t):
    tau = TAU[t]
    if tau not in WE:
        WE[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]))
    return WE[tau].evaluate(S[t])[0]
WV = [wval(t) for t in range(T + 1)]
WK = [[WE[TAU[t]].key(x) for x in WV[t]] for t in range(T + 1)]
def wfr(t, tau):                         # W of state t read against tau (the frame of the re-entry's arena)
    if tau == TAU[t]: return WV[t], WK[t]
    if tau not in WE:
        WE[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [list(g.succ[v]) if g.owner[v] == 0 else [tau[v]] for v in range(n)]))
    wv = WE[tau].evaluate(S[t])[0]; return wv, [WE[tau].key(x) for x in wv]
lam = [tuple(u[v][0] for v in range(n)) for u, _ in XI]; runs = [0] + [k + 1 for k in range(T) if lam[k + 1] != lam[k]]
cnt = dict.fromkeys(["REENT", "CUTRE", "FRESH", "CYC", "WPAID", "SILENT", "VIOL", "XCUT", "CUTRE_T", "FRESH_T", "FRESH0", "LRISE_V"], 0); mx = dict.fromkeys(["G", "FC", "XC", "ENT"], 0)
ex = None; pairs = 0
for i, j0 in zip(runs, runs[1:] + [T + 1]):
    for v in ev:
        sw = [t for t in range(i, j0 - 1) if S[t + 1][v] != S[t][v]]
        for c in {S[t + 1][v] for t in sw}:
            ent = [t + 1 for t in sw if S[t + 1][v] == c]; lv = [t for t in sw if S[t][v] == c]
            if not (lv and ent and max(ent) > lv[0]): continue
            pairs += 1; fc = xc = 0
            G = sum(1 for t in range(lv[0], max(ent) - 1) if not guided[t])
            for s in lv:
                nx = [e for e in ent if e > s]
                if not nx: continue
                j = nx[0]; cnt["REENT"] += 1
                if any(not guided[t] for t in range(s, j)): cnt["XCUT"] += 1; xc += 1
                if not guided[j - 1]:
                    cnt["CUTRE"] += 1; fc += 1; cnt["CUTRE_T"] += TAU[j] != TAU[j - 1]; continue
                lo = s if MUT == "nofresh" else max(s, p0[j - 1])
                hi = j - 1 if MUT == "off1" else j - 2
                qs = [q1 for q1 in range(lo, hi + 1) if S[q1][v] == c or (v, c) in IMP[q1]]
                if not qs:
                    cnt["FRESH"] += 1; fc += 1; a = p0[j - 1]
                    if a > s: cnt["FRESH_T"] += TAU[a] != TAU[a - 1]
                    if j - 1 == a: cnt["FRESH0"] += 1           # re-entry is the first transition of its piece
                    elif not XI[j - 1][0][c] != XI[j - 2][0][c]: cnt["LRISE_V"] += 1   # LATE-RISE: Xi(c) changes at j-2 -> j-1
                    continue
                q = qs[0] + 1; fr = [wfr(t, TAU[j - 1]) for t in range(q, j + 1)]
                if any(fr[t - q][0][v][0] == v for t in range(q, j + 1)): cnt["CYC"] += 1; continue
                if any(fr[t - q][1][c] != fr[0][1][c] for t in range(q, j + 1)): cnt["WPAID"] += 1; continue
                if fr[-1][1][S[j - 1][v]] == fr[-1][1][c]: cnt["SILENT"] += 1
                else: cnt["VIOL"] += 1; ex = ex or (v, c, s, q, j)
            mx["G"] = max(mx["G"], G); mx["FC"] = max(mx["FC"], fc); mx["XC"] = max(mx["XC"], xc); mx["ENT"] = max(mx["ENT"], len(ent))
cuts = sum(1 for t in range(T) if not guided[t])
print(f"CUTS{' FR' if FR else ''} {os.path.basename(args[0])} n {n} iter {T} cuts {cuts} pairs {pairs} " + " ".join(f"{k} {x}" for k, x in cnt.items())
      + f" maxG {mx['G']} maxFRESHCUT {mx['FC']} maxXCUT {mx['XC']} maxENT {mx['ENT']} ex {ex} {'PASS' if cnt['VIOL'] == cnt['LRISE_V'] == 0 else 'FAIL'}")
