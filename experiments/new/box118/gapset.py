#!/usr/bin/env python3
"""L-NEW box 118: the gap set GAP_k := {v : W_k(v) != Xi_k(v)} along N5's tau-stretches (W in G_tau); prints |GAP_k| per state, the
number of transitions inside stretches where GAP gains a vertex (GROW) and the sum of A_k := sum_v lcp(cs Xi_k(v), cs W_k(v)) drops.
Usage: gapset.py G.pg [START|-] [v]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None; VERB = len(sys.argv) > 3
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T = [tuple(s)], [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1]))
K = len(S) - 1; Wc = {}
def weng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau]
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
GAP, A = [], []
for k in range(K + 1):
    X = E.evaluate(S[k])[0]; W = weng(T[k]).evaluate(S[k])[0]
    GAP.append(frozenset(v for v in range(n) if X[v] != W[v])); A.append(sum(lcp(cs(X[v]), cs(W[v])) for v in range(n)))
ins = [k for k in range(K) if T[k + 1] == T[k]]
grow = sum(1 for k in ins if GAP[k + 1] - GAP[k]); shrink = sum(1 for k in ins if GAP[k] - GAP[k + 1])
adrop = sum(1 for k in ins if A[k + 1] < A[k])
if VERB: print("GAPSIZE", " ".join(str(len(x)) for x in GAP))
print(f"GAPSET {os.path.basename(sys.argv[1])} n {n} iters {K} tauconst {len(ins)} GROW {grow} SHRINK {shrink} ADROP {adrop} gap0 {len(GAP[0])} gapmax {max(map(len, GAP))}")
