#!/usr/bin/env python3
"""L-NEW box 93 §3 (obstruction for the contraction-free route): run Vöge-Jurdziński switch-all (L-RED R140 hybrid.py V0, same engine and
rule: every Even v with an improving edge takes its Xi-best improving successor, ties to the larger index) from the best-reward start, and
measure on the WHOLE run (reference = the final sigma, Xi_end = its valuation): BETA-MON violations (beta_t(v) := Xi_t(sigma_t v) falls),
ELIM-ORD-beta violations (an adoption of (v, w) at s after some t <= s with beta_t(v) >= Xi_end(w)), steps without a Xi change, and the HMZ
window HW (as box93/elimwin.py). Usage: swall_hw.py GAME.pg"""
import sys, os
EXP = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
for p in ("si", "harness", "new"): sys.path.insert(0, os.path.join(EXP, p))
import pg
from si import Engine
g = pg.parse("".join(l for l in open(sys.argv[1]) if not l.lstrip().startswith("%"))); n = g.n
E = Engine(g); sigma = tuple(E.initial("best")); S = [sigma]; XI = []
while len(S) < 100000:
    vs, _ = E.evaluate(S[-1]); XI.append(vs); Is = E.improving(S[-1], vs)
    if not Is: break
    ns = list(S[-1]); bestw = {}
    for v, w in Is:
        if v not in bestw or (E.key(vs[w]), w) > (E.key(vs[bestw[v]]), bestw[v]): bestw[v] = w
    for v, w in bestw.items(): ns[v] = w
    S.append(tuple(ns))
T = len(S) - 1; ev = [v for v in range(n) if g.owner[v] == 0]; key = E.key; end = XI[T]
bmon = sum(1 for k in range(T) for v in ev if key(XI[k + 1][S[k + 1][v]]) < key(XI[k][S[k][v]]))
flat = sum(1 for k in range(T) if XI[k + 1] == XI[k])
elim = 0; best = {v: None for v in ev}
for k in range(T + 1):
    for v in ev:
        if k > 0 and S[k][v] != S[k - 1][v] and best[v] is not None and key(best[v]) >= key(end[S[k][v]]): elim += 1
        b = XI[k][S[k][v]]
        if best[v] is None or key(b) > key(best[v]): best[v] = b
last = {}
for k in range(T + 1):
    for v in ev: last[(v, S[k][v])] = k
hw = 0
for k in range(T + 1):
    nf = [v for v in ev if S[k][v] != S[T][v]]
    if nf: hw = max(hw, min(last[(v, S[k][v])] + 1 - k for v in nf))
mE = sum(len(g.succ[v]) for v in ev)
print(f"SWALL {os.path.basename(sys.argv[1])} n {n} mE {mE} iterations {T} bmon_viol {bmon} elim_viol {elim} xi_flat_steps {flat} HW {hw} count_ok {T <= (mE + 1) * hw}")
