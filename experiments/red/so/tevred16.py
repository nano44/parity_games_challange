#!/usr/bin/env python3
"""Box 39 (L-RED succ. 16): TEV-RED (1)-(4) at one TEV failure (k0, t, L). Usage: tevred16.py game.pg k0 t L (run from the repo root)."""
import sys; sys.path.insert(0, "experiments/red/so")
import sox, pg
from si import Engine
from sox import lev, coarse, BOT
g = sox.load(sys.argv[1]); o = sox.oddchoice(g)[0]; n = g.n; k0, t, L = int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
S, FB, E = sox.trace(g, 5000); N = len(S)
ev = [E.evaluate(s) for s, _ in S]; Xi = [e[0] for e in ev]; sb = [e[1] for e in ev]
def play(k, v):
    x, seen = v, []
    while x not in seen: seen.append(x); x = S[k][0][x] if g.owner[x] == 0 else (S[k][1][x] if x == o else sb[k][x])
    return seen
def tplay(k, v):
    x, seen = v, []
    while x not in seen: seen.append(x); x = S[k][0][x] if g.owner[x] == 0 else S[k][1][x]
    return seen
R = [frozenset({o} | {v for v in range(n) if o in tplay(k, v)}) for k in range(N)]
Ev = R[k0] - R[k0 + 1]; F0 = set(range(n)) - R[k0]
x = sb[t][o]; p = play(t, x); evs = [v for v in p if v in Ev]; e = evs[-1]
f = S[t][0][e] if g.owner[e] == 0 else None; ue = S[k0][0][e] if g.owner[e] == 0 else sb[k0][e]
print("threat play", p, "Ev on it", evs, "e", e, "owner", g.owner[e], "prio", g.prio[e])
print("(1) e Even:", g.owner[e] == 0, " f =", f, " f's play in F_k0:", set(play(t, f)) <= F0 if f is not None else None, " Xi_t(f) == Xi_k0(f):", Xi[t][f] == Xi[k0][f] if f is not None else None)
print("    f's play", play(t, f) if f is not None else None)
rc = Xi[k0][o][0]
print("theta_k0", Xi[k0][o], " theta_t", Xi[t][o], " lev", lev(Xi[k0][o], Xi[t][o]))
print("(2) u_e =", ue, " u_e in Ev:", ue in Ev, " COARSE_L(Xi_k0 u_e) == COARSE_L(theta_k0):", coarse(Xi[k0][ue], L) == coarse(Xi[k0][o], L), " u_e in R_t:", ue in R[t])
gates = E.improving(S[t][0], Xi[t])
print("(4) (e,u_e) is an improving edge at t:", (e, ue) in set(gates), " level:", lev(Xi[t][S[t][0][e]], Xi[t][ue]) if (e, ue) in set(gates) else None, " FB[t]:", FB[t], " e in R_{t+1}:", e in R[t + 1], " e on e* play:", e in tplay(t, S[t][1][o]))
print("    sigma_t+1(e) =", S[t + 1][0][e])
