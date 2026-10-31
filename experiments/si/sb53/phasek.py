#!/usr/bin/env python3
"""L-SI box 53c (Lead 06:43Z, compounding of k-SOURCE up the levels): where do transitions fall with respect to RESULTS R94's potential
K = sum_v DEPTH(v)? Phase P := a maximal run of states with (lambda_Xi, tau) constant (R38 (a)); CS(x) := R93 Fact LEX's coordinate
sequence (reward of the cycle node; per rank r from n-1 down to 0: +1 / -1 / 0 as the rank-r vertex is in the path set with even / odd
priority / not; length, negated if the cycle node is even); DEPTH_t(v) := the common prefix length of CS(Xi_t(v)) and CS(Xi_b(v)), b the
last state of P; K_t := sum_v DEPTH_t(v). Per run, over in-phase transitions: KUP (K rises), KDOWN (K falls; R94 FIXD-MON claims never),
FLAT (Xi changes somewhere, K unchanged: R94's FLATTR), NOXI (Xi unchanged), and SWFLAT (Even switches at FLAT transitions).
MAXP (longest phase), PH (phases), T. Usage: phasek.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU = [tuple(s)], [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1]))
V = [E.evaluate(x)[0] for x in S]
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
CS = [[cs(v) for v in vv] for vv in V]
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
key = [(tuple(x[0] for x in V[k]), TAU[k]) for k in range(len(S))]
c = dict(T=len(S) - 1, PH=0, MAXP=0, KUP=0, KDOWN=0, FLAT=0, NOXI=0, SWFLAT=0)
k = 0
while k < len(S):
    e = k
    while e + 1 < len(S) and key[e + 1] == key[k]: e += 1
    c['PH'] += 1; c['MAXP'] = max(c['MAXP'], e - k)
    K = [sum(lcp(CS[q][v], CS[e][v]) for v in range(n)) for q in range(k, e + 1)]
    for i, q in enumerate(range(k, e)):
        if K[i + 1] > K[i]: c['KUP'] += 1
        elif K[i + 1] < K[i]: c['KDOWN'] += 1
        elif V[q + 1] != V[q]:
            c['FLAT'] += 1; c['SWFLAT'] += sum(1 for v in range(n) if own[v] == 0 and S[q + 1][v] != S[q][v])
        else: c['NOXI'] += 1
    k = e + 1
print(f"PHASEK {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{a} {b}" for a, b in c.items()))
