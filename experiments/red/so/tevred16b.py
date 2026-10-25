#!/usr/bin/env python3
"""Box 39 (L-RED succ. 16): TEV-RED (4) at EVERY TEVLAST failure (k0, t, L) of rx16 at an S4a state t: e = the last Ev vertex on the threat's
play, u_e = σ_k0(e). (4): if u_e in R̄_t then (e, u_e) is an improving edge of level > L at t, and e in R̄_{t+1} unless e is on e*'s
(σ_t, τ)-play. Also counts u_e in Ev ∩ F_t (configuration (5) shape), and N5-TEV-box11 §5's lane reading (WALK's v from
v0 = the first and the last Ev vertex on the threat's play: (v, a_j) a gate of level > L at t; v in R̄_{t+1} unless on e*'s play; wbad = failures). Usage: tevred16b.py game.pg ..."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import sox, rx16
from sox import lev
for f in sys.argv[1:]:
    g = sox.load(f); o = sox.oddchoice(g)[0]; n = g.n; r = rx16.analyse(g); S, FB, E = sox.trace(g, 5000)
    ev = [E.evaluate(s) for s, _ in S]; Xi = [x[0] for x in ev]; sb = [x[1] for x in ev]
    def tplay(k, v):
        x, seen = v, []
        while x not in seen: seen.append(x); x = S[k][0][x] if g.owner[x] == 0 else S[k][1][x]
        return seen
    def hplay(k, v):
        x, seen = v, []
        while x not in seen: seen.append(x); x = S[k][0][x] if g.owner[x] == 0 else sb[k][x]
        return seen
    Rb = lambda k: {o} | {v for v in range(n) if o in tplay(k, v)}
    c = dict(fail=0, s4a=0, ue_in_R=0, gate_ok=0, back_ok=0, on_estar=0, conf_shape=0, bad4=0, walk=0, wgate=0, wback=0, westar=0, wbad=0)
    for (k0, t, L) in r.get("tevlist", []):
        c["fail"] += 1
        if FB[t]: continue
        c["s4a"] += 1; Ev = Rb(k0) - Rb(k0 + 1); p = hplay(t, sb[t][o]); e = [v for v in p if v in Ev][-1]
        ue = S[k0][0][e] if g.owner[e] == 0 else None; Rt, Rt1 = Rb(t), Rb(t + 1)
        if ue is None: c["bad4"] += 1; continue          # TEV-RED (1): e must be Even
        # N5-TEV-box11 §5 lane reading: v0 in Ev on the threat's play (first and last); walk v0's k0-route to the first a_j in R̄_t
        for v0 in {[v for v in p if v in Ev][0], e}:
            rt = tplay(k0, v0); rt = rt[:rt.index(o)] + [o]
            j = next(i for i in range(1, len(rt)) if rt[i] in Rt); v, aj = rt[j - 1], rt[j]; c["walk"] += 1
            gs = set(E.improving(S[t][0], Xi[t])); okg = g.owner[v] == 0 and (v, aj) in gs and lev(Xi[t][S[t][0][v]], Xi[t][aj]) > L
            c["wgate"] += okg
            if v in tplay(t, S[t][1][o]): c["westar"] += 1
            elif v in Rt1: c["wback"] += 1
            if not okg or (v not in Rt1 and v not in tplay(t, S[t][1][o])): c["wbad"] += 1; c.setdefault("wex", (k0, t, L, v0, v, aj))
        if ue in Ev and ue not in Rt: c["conf_shape"] += 1
        if ue in Rt:
            c["ue_in_R"] += 1; gs = set(E.improving(S[t][0], Xi[t]))
            ok = (e, ue) in gs and lev(Xi[t][S[t][0][e]], Xi[t][ue]) > L
            c["gate_ok"] += ok; c["bad4"] += not ok
            if e in tplay(t, S[t][1][o]): c["on_estar"] += 1
            elif e in Rt1: c["back_ok"] += 1
            else: c["bad4"] += 1
    print(os.path.basename(f), c, flush=True)
