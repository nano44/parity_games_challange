#!/usr/bin/env python3
"""L-NEW box 108: NA_F = transitions k of a W-run F at which the Even arena H_k = {sigma_k} u I_k gains an edge over H_(k-1) (first
transition of F counted as new), against |F|, CN_F (switches at Even W-cycle nodes) and the bound CN + (m_E + 2n + 1)(1 + NA) of
Corollary ARENA-RED. Also NAWC: new-arena transitions with W constant. Usage: na.py GAME.pg [START]"""
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
mE = sum(len(set(g.succ[v])) for v in range(n) if own[v] == 0)
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
TOT = NA = CN = NAWC = VIOL = 0; MAXF = MAXNA = 0; WORST = 0.0
for run in runs:
    tau = TAU[run[0]]; na = cn = 0
    for i, k in enumerate(run):
        new = i == 0 or not H(k) <= H(k - 1)
        na += new; NAWC += new and Wv(k, tau) == Wv(k + 1, tau)
        C = {v for v in range(n) if Wv(k, tau)[v][0] == v}; cn += any(S[k][y] != S[k + 1][y] for y in C if own[y] == 0)
    TOT += len(run); NA += na; CN += cn; MAXF = max(MAXF, len(run)); MAXNA = max(MAXNA, na)
    VIOL += len(run) > cn + (mE + 2 * n + 1) * (1 + na); WORST = max(WORST, len(run) / max(1, na))
print(f"NA {os.path.basename(sys.argv[1])} n {n} mE {mE} WT {TOT} NA {NA} NAWC {NAWC} CN {CN} MAXF {MAXF} MAXNA {MAXNA} max|F|/NA {WORST:.2f} BOUNDVIOL {VIOL}")
