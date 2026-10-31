#!/usr/bin/env python3
"""L-NEW box 96 (docs/new/N5-TAU-box96.md): N5 (new/box21/n5x.py) on a game from different Odd starts tau_0, sigma_0 = best-reward:
  BEST  best-reward tau_0 (the default);
  OPT   tau_0 := tau_end of the default run at EVERY Odd vertex (Odd starts optimal: its own S4b step never moves);
  BR    tau_0 := sigma-bar(sigma_0), Odd's best response to Even's start (then tau moves only by S4b);
  OPTH  tau_0 := tau_end only at the Odd vertices named h* (switchbestexp's stubborn-cycle exits), best-reward elsewhere.
Prints iterations, tau-changes and the largest W-run (as box85/xirise.py). Usage: taustart.py GAME.pg MODE"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, Engine, dual
import pg
path, mode = sys.argv[1], sys.argv[2]; g = load(path); n = g.n; own = g.owner
NM = {}
for l in open(path):
    a = l.strip().rstrip(";").split()
    if len(a) >= 5 and a[0].isdigit(): NM[int(a[0])] = a[4].strip('"')
E, Ed = Engine(g), Engine(dual(g))
def run(s, t):
    S, TAU, FB = [tuple(s)], [tuple(t)], []
    while len(S) < 200000:
        r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
        if r is None: break
        S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
    return S, TAU, FB
s0, t0 = start_pair(g, E, Ed, None)
if mode != "BEST":
    S, TAU, _ = run(s0, t0); tend = TAU[-1]
    if mode == "OPT": t0 = [tend[v] if own[v] == 1 else t0[v] for v in range(n)]
    elif mode == "OPTH": t0 = [tend[v] if own[v] == 1 and NM.get(v, "").startswith("h") else t0[v] for v in range(n)]
    elif mode == "BR": sb = E.evaluate(tuple(s0))[1]; t0 = [sb[v] if own[v] == 1 else t0[v] for v in range(n)]
S, TAU, FB = run(s0, t0); T = len(S) - 1
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
L, cur = 0, 0
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    cur = cur + 1 if ok else 0; L = max(L, cur)
print(f"TAUSTART {os.path.basename(path)} n {n} {mode} iterations {T} tau_changes {sum(1 for k in range(T) if TAU[k + 1] != TAU[k])} fallbacks {sum(1 for x in FB if x)} maxWrun {L}")
