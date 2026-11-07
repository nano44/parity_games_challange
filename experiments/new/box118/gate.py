#!/usr/bin/env python3
"""L-NEW box 118: Even's climb inside a tau-stretch (maximal window of transitions with tau constant). G_tau := the one-player game with Odd
fixed to tau; W_k := sigma_k's valuation in G_tau; IW_k := G_tau's (VJ) improving edges of sigma_k; Is_k := N5's Xi-improving edges (S2).
Per transition k of a stretch: BL_k := IW_k minus Is_k (W-improving, Xi-blocked), EX_k := Is_k minus IW_k; FULL_k := the optimum of the
ungated arena {sigma_k} u IW_k in G_tau (R17's switch-best step); the step is GATED if W(sigma_(k+1)) != W(FULL_k) pointwise (LAG := the
vertices where FULL is strictly better), FLAT if W(sigma_(k+1)) = W_k. Fallback transitions (S4c) are marked FB and counted apart.
Also per stretch: steps, W-changing steps, lambda_W phases (cycle-node map of W changes), the most W-changing steps in one phase (R17 bound
for switch-best: n - 1); onep := the length of R17's switch-best run on G_tau from the stretch's first sigma (tau fixed), and the
largest ratio stretch steps / |onep| (onep < 0: R17's run stalled after -onep - 1 steps, the arena optimum being sigma itself with
IW non-empty: the own-cycle-node case); INC := transitions of stretches with Is != IW or a fallback; maxConsistentWindow := the most
consecutive stretch transitions with Is = IW and no fallback.
Usage: gate.py G.pg [START|-] [v]   (v: one line per transition)"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None; VERB = len(sys.argv) > 3
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1])); FB.append(r[4])
K = len(S) - 1
Wc = {}
def weng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau]
def opt(sig, tau, I):
    a = {v: {sig[v]} for v in range(n) if own[v] == 0}
    for v, w in I: a[v].add(w)
    succ = [sorted(a[v]) if own[v] == 0 else [tau[v]] for v in range(n)]
    Er = Engine(dual(pg.Game(list(g.prio), list(own), succ)))
    _, best = Er.evaluate(tuple(tau[v] if own[v] == 1 else -1 for v in range(n)))
    return tuple(best[v] if own[v] == 0 else sig[v] for v in range(n))
ek = E.key
tot = dict(inc=0, cwin=0, steps=0, fb=0, gated=0, flat=0, bl=0, blsteps=0, lagmax=0, ex=0)
stretches = []; cur = None
for k in range(K):
    tau = T[k]
    if cur is None or T[k] != T[k - 1]:
        run = 0
        cur = dict(start=k, steps=0, wch=0, gated=0, phases=1, maxph=0, ph=0, lam=None); stretches.append(cur)
    if T[k + 1] != T[k]:   # tau-changing transition ends the stretch (not an Even climb step of it)
        cur["end"] = k; cur = None; continue
    We = weng(tau); W0 = We.evaluate(S[k])[0]; W1 = We.evaluate(S[k + 1])[0]
    lam = tuple(w[0] for w in W0)
    if cur["lam"] is not None and lam != cur["lam"]: cur["phases"] += 1; cur["ph"] = 0
    cur["lam"] = lam
    cur["steps"] += 1; tot["steps"] += 1
    if FB[k]: tot["fb"] += 1
    vs, _ = E.evaluate(S[k]); Is = set(E.improving(S[k], vs)); IW = set(We.improving(S[k], W0))
    BL = IW - Is; EX = Is - IW
    if BL or EX or FB[k]: tot["inc"] += 1; run = 0
    else: run += 1; tot["cwin"] = max(tot["cwin"], run)
    tot["bl"] += len(BL); tot["blsteps"] += bool(BL); tot["ex"] += len(EX)
    F = opt(S[k], tau, IW) if IW else S[k]; WF = We.evaluate(F)[0]
    lag = [v for v in range(n) if ek(WF[v]) > ek(W1[v])]
    flat = W1 == W0
    if not flat: cur["wch"] += 1; cur["ph"] += 1; cur["maxph"] = max(cur["maxph"], cur["ph"])
    if lag: cur["gated"] += 1; tot["gated"] += 1; tot["lagmax"] = max(tot["lagmax"], len(lag))
    tot["flat"] += flat
    if VERB: print(f"k {k} fb {FB[k]} |IW| {len(IW)} |Is| {len(Is)} |BL| {len(BL)} |EX| {len(EX)} flat {int(flat)} lag {len(lag)}")
def onep(sig, tau, cap=100000):
    We = weng(tau); c = 0
    while c < cap:
        W0 = We.evaluate(sig)[0]; IW = We.improving(sig, W0)
        if not IW: return c
        ns = opt(sig, tau, IW)
        if ns == sig: return -c - 1   # flat stall (R17's terminal flat case; not expected)
        sig = ns; c += 1
    return c
for c in stretches: c["onep"] = onep(S[c["start"]], T[c["start"]]) if c["steps"] else 0
lst = max(stretches, key=lambda c: c["steps"]) if stretches else dict(steps=0, wch=0, gated=0, phases=0, maxph=0)
print(f"GATE {os.path.basename(sys.argv[1])} n {n} iters {K} stretches {len(stretches)} climbsteps {tot['steps']} fb {tot['fb']} flat {tot['flat']} "
      f"gated {tot['gated']} blsteps {tot['blsteps']} BLsum {tot['bl']} EXsum {tot['ex']} lagmax {tot['lagmax']} | longest: steps {lst['steps']} "
      f"wch {lst['wch']} gated {lst['gated']} phases {lst['phases']} maxWchPerPhase {max(c['maxph'] for c in stretches) if stretches else 0} onep {lst.get('onep', 0)} maxratio {max((c['steps'] / max(1, abs(c['onep'])) for c in stretches), default=0):.1f} INC {tot['inc']} maxConsistentWindow {tot['cwin']}")
