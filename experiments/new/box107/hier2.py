#!/usr/bin/env python3
"""L-NEW box 107: depth of the nested frozen-ceiling hierarchy on each W-run. Level 1 block = the W-run's W-changing transitions,
reference W_end (state after the block); P := sum_v lcp(CS W_k v, CS W_ref v) (monotone in k by SANDWICH + W-MON). Transitions where
P rises are paid at this level; maximal stretches of W-changing transitions with P flat (W-constant transitions do not break a
stretch) are sub-blocks with their own reference W at the stretch's end. DEPTH = deepest level that pays a transition.
Also NLEV<d> = transitions paid at level d.  Usage: hier.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); S, TAU, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
def cs(v):
    c, m, l = v
    return (E.rew[c],) + tuple(((1 if E.rankpar[r] == 0 else -1) if (m >> r) & 1 else 0) for r in range(n - 1, -1, -1)) + ((l if E.par[c] == 1 else -l),)
def lcp(a, b):
    i = 0
    while i < len(a) and a[i] == b[i]: i += 1
    return i
runs = []
for k in range(len(S) - 1):
    if TAU[k + 1] != TAU[k] or FB[k] or [x[0] for x in Wv(k, TAU[k])] != [x[0] for x in Wv(k + 1, TAU[k])]: continue
    if runs and runs[-1][-1] == k - 1: runs[-1].append(k)
    else: runs.append([k])
NL = {}; DEPTH = 0; MAXSUB = 0; MONOX = 0
def block(ks, tau, lev):
    global DEPTH, MAXSUB, MONOX
    if not ks: return
    ref = [cs(x) for x in Wv(ks[-1] + 1, tau)]
    P = lambda j: sum(lcp(cs(x), ref[v]) for v, x in enumerate(Wv(j, tau)))
    sub, subs = [], []
    for k in ks:
        p0, p1 = P(k), P(k + 1); MONOX += p1 < p0
        if p1 > p0:
            NL[lev] = NL.get(lev, 0) + 1; DEPTH = max(DEPTH, lev)
            if sub: subs.append(sub); sub = []
        else: sub.append(k)
    if sub: subs.append(sub)
    for sb in subs: MAXSUB = max(MAXSUB, len(sb)); block(sb, tau, lev + 1)
XV = lambda j: E.evaluate(S[j])[0]
NLV = {}; DEPTHV = 0; NOV = 0
def blockv(ks, tau, lev):
    # joint vector V_k = (W_k, Xi_k) (2n monotone lex values), reference V at the block end
    global DEPTHV
    if not ks: return
    e = ks[-1] + 1; ref = [cs(x) for x in Wv(e, tau)] + [cs(x) for x in XV(e)]
    P = lambda j: sum(lcp(cs(x), ref[v]) for v, x in enumerate(list(Wv(j, tau)) + list(XV(j))))
    sub, subs = [], []
    for k in ks:
        if P(k + 1) > P(k):
            NLV[lev] = NLV.get(lev, 0) + 1; DEPTHV = max(DEPTHV, lev)
            if sub: subs.append(sub); sub = []
        else: sub.append(k)
    if sub: subs.append(sub)
    for sb in subs: blockv(sb, tau, lev + 1)
WT = WCH = 0
for run in runs:
    tau = TAU[run[0]]; ks = [k for k in run if Wv(k, tau) != Wv(k + 1, tau)]; WT += len(run); WCH += len(ks)
    block(ks, tau, 1)
    kv = [k for k in run if Wv(k, tau) != Wv(k + 1, tau) or XV(k) != XV(k + 1)]; NOV += len(run) - len(kv); blockv(kv, tau, 1)
print(f"HIER {os.path.basename(sys.argv[1])} n {n} WT {WT} WCH {WCH} DEPTH {DEPTH} MONOX {MONOX} MAXSUB1 {MAXSUB} " + " ".join(f"NLEV{d} {NL[d]}" for d in sorted(NL)) + f" | NOV {NOV} DEPTHV {DEPTHV} " + " ".join(f"NLV{d} {NLV[d]}" for d in sorted(NLV)))
