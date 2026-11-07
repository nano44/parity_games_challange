#!/usr/bin/env python3
"""L-NEW box 107: frozen-reference hierarchy of Xi ALONE over the WHOLE N5 run (every transition, fallbacks and tau-changes included).
Xi_k <= Xi_(k+1) pointwise, strictly somewhere at every transition that switches sigma (R15 (a)). Level-1 block = all transitions with
Xi changing, reference Xi at the run's end; recursion as hier.py. Also NOX = transitions with Xi unchanged (sigma unchanged, tau moves).
Usage: hier3.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU = [tuple(s)], [tuple(t)]
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1]))
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
X = [[cs(x) for x in E.evaluate(S[j])[0]] for j in range(len(S))]
NL = {}; DEPTH = 0; DEC = 0; SIGNOX = 0
def block(ks, lev):
    global DEPTH, DEC
    if not ks: return
    ref = X[ks[-1] + 1]; P = lambda j: sum(lcp(X[j][v], ref[v]) for v in range(n))
    sub, subs = [], []
    for k in ks:
        if P(k + 1) < P(k): DEC += 1
        if P(k + 1) > P(k):
            NL[lev] = NL.get(lev, 0) + 1; DEPTH = max(DEPTH, lev)
            if sub: subs.append(sub); sub = []
        else: sub.append(k)
    if sub: subs.append(sub)
    for sb in subs: block(sb, lev + 1)
ks = [k for k in range(len(S) - 1) if X[k] != X[k + 1]]
SIGNOX = sum(1 for k in range(len(S) - 1) if X[k] == X[k + 1] and S[k] != S[k + 1])
XDOWN = sum(1 for k in range(len(S) - 1) for v in range(n) if X[k + 1][v] < X[k][v])
block(ks, 1)
print(f"HIER3 {os.path.basename(sys.argv[1])} n {n} T {len(S) - 1} XCHG {len(ks)} NOX {len(S) - 1 - len(ks)} SIGNOX {SIGNOX} XDOWN {XDOWN} DEC {DEC} DEPTH {DEPTH} " + " ".join(f"NLEV{d} {NL[d]}" for d in sorted(NL)))
