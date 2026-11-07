#!/usr/bin/env python3
"""L-NEW box 108: check of Lemma NEW-EDGE. For every transition k -> k+1 with tau_(k+1) = tau_k = tau_(k-1), no fallback at k-1 or k
(so W_k = OPT(H_(k-1)) and W_(k+1) = OPT(H_k), H_j := Even arena {sigma_j} u I_j against tau), and every vertex v with W_(k+1)(v) !=
W_k(v): the sigma_(k+1)-play of v against tau uses an Even edge of N_k := H_k minus H_(k-1). Also: every such new edge (y, z) is a strict
Xi-overtake: Xi_k(z) > Xi_k(sigma_k y) and Xi_(k-1)(z) <= Xi_(k-1)(sigma_(k-1) y). Prints NEWEDGE <game> checked C viol V overtake_viol O.
Usage: newedge.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB, IS = [tuple(s)], [tuple(t)], [], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4]); IS.append(set(r[2]))
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def H(j): return {(y, S[j][y]) for y in range(n) if own[y] == 0} | IS[j]
C = V = O = 0
for k in range(1, len(S) - 1):
    if not (TAU[k + 1] == TAU[k] == TAU[k - 1]) or FB[k] or FB[k - 1]: continue
    tau = TAU[k]; W0, W1 = Wv(k, tau), Wv(k + 1, tau); Nk = H(k) - H(k - 1)
    X0, Xm = E.evaluate(S[k])[0], E.evaluate(S[k - 1])[0]
    for (y, z) in Nk:
        if z == S[k][y]: continue
        if not (E.key(X0[z]) > E.key(X0[S[k][y]]) and E.key(Xm[z]) <= E.key(Xm[S[k - 1][y]])): O += 1
    sig = S[k + 1]
    for v in range(n):
        if W0[v] == W1[v]: continue
        C += 1; x, seen, ok = v, set(), False
        while x not in seen:
            seen.add(x)
            if own[x] == 0:
                if (x, sig[x]) in Nk: ok = True; break
                x = sig[x]
            else: x = tau[x]
        V += not ok
print(f"NEWEDGE {os.path.basename(sys.argv[1])} n {n} checked {C} viol {V} overtake_viol {O}")
