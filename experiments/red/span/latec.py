#!/usr/bin/env python3
"""L-RED successor 31 (R127): second, independent late-adoption counter (not derived from L-NEW's frozen.py / latepair.py code).
Engine: L-COMP's n5b SPEC trace and its PGSolver-port valuations (SpecSI). W_t = val(sigma_t, tau_t) on G_tau_t (Odd restricted to tau_t).
W-run: maximal run of states with tau constant, no S4c fallback, and the W cycle-node map constant (R89). (v, c) BLOCKED at t: c is
W_t-better than sigma_t(v) and (v, c) not in I_sigma_t. LATE adoption at t -> t+1 (inside a W-run): sigma_(t+1)(v) = c != sigma_t(v) and
(v, c) blocked at some earlier state of the same W-run. Prints R* (transitions of the W-run with a late adoption, max over W-runs), the
total, and the most late adoptions of one edge in one W-run. REP=1 also prints REP (max over W-runs of late adoptions minus
distinct late-adopted edges: L-SI box 42's REPEAT count).  Usage: latec.py GAME.pg START"""
import sys, os
R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
for p in ("experiments/n5-second", "experiments/hard-families", "experiments/harness"): sys.path.insert(0, os.path.join(R, p))
import n5b, pg
from collections import Counter
g = pg.read(sys.argv[1]); s0, t0 = n5b.read_start(sys.argv[2], g)
N = n5b.N5(g, mode="spec"); tr = []; fb = []; N.run(s0, t0, trace=tr, fbtrace=fb)
fbs = {k for k, x in enumerate(fb) if x}
SG = N.SG; T = len(tr) - 1; WE = {}
def W(t):
    tau = tuple(tr[t][1])
    if tau not in WE: WE[tau] = n5b.SpecSI(pg.Game(g.prio, g.owner, [g.succ[v] if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]))
    return WE[tau], WE[tau].evaluate(list(tr[t][0]))
ev = [v for v in range(g.n) if g.owner[v] == 0]
blocked = []; lamW = []
for t in range(T + 1):
    sig = list(tr[t][0]); xv = SG.evaluate(sig); I = n5b.N5.improving(SG, sig, xv); si, wv = W(t)
    blocked.append({(v, c) for v in ev for c in g.succ[v] if c != sig[v] and si.nvo(wv[sig[v]], wv[c]) < 0 and c not in I.get(v, [])})
    lamW.append(tuple(wv[v][0] for v in range(g.n)))
cut = [tuple(tr[t][1]) != tuple(tr[t + 1][1]) or lamW[t] != lamW[t + 1] or t in fbs for t in range(T)]
best = tot = 0; per = 0; start = 0; seen = set(); rs = 0; cnt = Counter(); rep = 0
for t in range(T):
    seen |= blocked[t]
    lat = [(v, tr[t + 1][0][v]) for v in ev if tr[t + 1][0][v] != tr[t][0][v] and (v, tr[t + 1][0][v]) in seen]
    if lat: rs += 1; tot += len(lat); cnt.update(lat)
    if cut[t] or t == T - 1:
        best = max(best, rs); per = max([per] + list(cnt.values())); rep = max(rep, sum(cnt.values()) - len(cnt)); rs = 0; seen = set(); cnt = Counter()
print(f"LATEC {os.path.basename(sys.argv[1])} n {g.n} iter {T} cuts {sum(cut)} fallbacks {len(fbs)} R* {best} late {tot} max-per-edge-Wrun {per}" + (f" REP {rep}" if os.environ.get("REP") == "1" else ""))
