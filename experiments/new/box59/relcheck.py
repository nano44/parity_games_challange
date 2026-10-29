#!/usr/bin/env python3
"""L-NEW box 59: relevant SBC (REL-R). R := vertices reachable in G from an Even vertex with >= 2 distinct successors (successor-closed;
contains every Even branching vertex). SBC_R := #{j : sbar(sigma^(j+1)) != sbar(sigma^(j)) on some Odd vertex of R}. R-stretch := maximal
interval of the distinct-sigma sequence on which sbar|R and lambda|R are constant. Checks, at EVERY j < p (not only inside stretches):
  LOC_V  F(sigma^(j)) != n5x.step on G* := G cut to sbar* at Odd vertices, sbar* = sbar(sigma^(a)) on R (a = start of j's R-stretch) and
         an arbitrary FIXED choice (first successor) outside R, tau := sbar*   [Lemma ONE-PLAYER-R (b), under ASSUMPTION LOC]
  VAL_V  Xi of sigma^(j) on G* != Xi_j on R                               [Lemma ONE-PLAYER-R (a)]
  SEG_V  an R-stretch with >= n + m transitions;  TOT_V  #sigma - 1 >= (n + m + 1)(1 + LAM + SBC_R)
Prints one REL line. Usage: relcheck.py GAME.pg"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box54"))
import n5sf, n5x, pg
from n5x import load, Engine, dual
g = load(sys.argv[1]); n = g.n; m = sum(len(set(s)) for s in g.succ)
E, T = n5sf.trace(g)
seq = [T[0]]
for x in T[1:]:
    if x.get("cycle"): break
    if x["s"] != seq[-1]["s"]: seq.append(x)
R = set(); st = [v for v in range(n) if g.owner[v] == 0 and len(set(g.succ[v])) > 1]
while st:
    v = st.pop()
    if v in R: continue
    R.add(v); st += g.succ[v]
OR = [u for u in R if g.owner[u] == 1]
vals = [E.evaluate(tuple(x["s"]))[0] for x in seq]
lamR = lambda j: tuple(vals[j][v][0] for v in sorted(R))
sbR = lambda j: tuple(seq[j]["sb"][u] for u in OR)
sbc = sum(1 for j in range(len(seq) - 1) if seq[j]["sb"] != seq[j + 1]["sb"])
sbcR = sum(1 for j in range(len(seq) - 1) if sbR(j) != sbR(j + 1))
lam = sum(1 for j in range(len(seq) - 1) if tuple(v[0] for v in vals[j]) != tuple(v[0] for v in vals[j + 1]))
viol = set(); a = 0; seg = 0; cache = {}
for j in range(len(seq) - 1):
    if j > 0 and (sbR(j) != sbR(j - 1) or lamR(j) != lamR(j - 1)): a = j
    if j + 1 < len(seq) and (sbR(j + 1) != sbR(j) or lamR(j + 1) != lamR(j)): seg = max(seg, j - a)
    if a not in cache:
        sstar = [seq[a]["sb"][u] if (g.owner[u] == 1 and u in R) else (g.succ[u][0] if g.owner[u] == 1 else -1) for u in range(n)]
        succ = [[sstar[u]] if g.owner[u] == 1 else list(g.succ[u]) for u in range(n)]
        gs = pg.Game(list(g.prio), list(g.owner), succ); cache = {a: (gs, Engine(gs), Engine(dual(gs)), sstar)}
    gs, Es, Eds, sstar = cache[a]
    vst, _ = Es.evaluate(tuple(seq[j]["s"]))
    if any(vst[v] != vals[j][v] for v in R): viol.add("VAL_V")
    r = n5x.step(gs, Es, Eds, list(seq[j]["s"]), [sstar[u] if g.owner[u] == 1 else -1 for u in range(n)])
    if r is None or [r[0][v] for v in range(n) if g.owner[v] == 0] != [seq[j + 1]["s"][v] for v in range(n) if g.owner[v] == 0]:
        viol.add("LOC_V")
seg = max(seg, len(seq) - 1 - a)
if seg >= n + m: viol.add("SEG_V")
if len(seq) - 1 >= (n + m + 1) * (1 + lam + sbcR): viol.add("TOT_V")
print(f"REL {os.path.basename(sys.argv[1])} n {n} m {m} |R| {len(R)} orbit {len(seq)} SBC {sbc} SBC_R {sbcR} LAM {lam} SEGMAX {seg} "
      f"{'PASS' if not viol else 'FAIL ' + ' '.join(sorted(viol))}", flush=True)
