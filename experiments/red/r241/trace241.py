#!/usr/bin/env python3
"""L-RED 69 R241: SPEC-line trace of a saved NUMB_* instance: per degree-2 mover with moves(x) > 1 + KF_x (gate keys), its options
(W-target, gate index, e-vertex index in the renumbered Γ3), its option at every state 0..F1-1 of N5 (n5s237 spec), and the least option
under gate keys (KP) and under e-index keys (KP_e) at every state. Usage: trace241.py NUMB_*.json   (env LNEW)"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import kt241 as K
import gamma3
D = json.load(open(sys.argv[1])); G = D["genome"]; K.PERM, K.PSEED = D["perm"], D["pseed"]
g, _, _, V = gamma3.build(G, K.PADS); g, V = K.renumber(g, V, D["perm"], D["pseed"])
prio, owner, succ = list(g.prio), list(g.owner), [sorted(set(s)) for s in g.succ]
tr = []; fbt = []; K.S.run(prio, owner, succ, "spec", trace=tr, fbtrace=fbt); F1 = fbt[0]
N, opts, lev, gate = G["N"], G["opts"], G["lev"], G["gate"]
pad = {V[("m", (x, k))]: k for x in range(N) for k in range(len(opts[x]))}
S = [tuple(pad[tr[t][0][V[("x", x)]]] for x in range(N)) for t in range(F1)]
order = sorted(range(N), key=lambda x: (lev[x], x))
def keys(s, f):
    own = {}; allk = {}
    for x in order:
        allk[x] = [((own[o[0]] if o[0] >= 0 else ()) + (f(x, k),)) for k, o in enumerate(opts[x])]; own[x] = allk[x][s[x]]
    return allk
gk = lambda x, k: gate[x][k]; ek = lambda x, k: V[("e", (x, k))]
for x in range(N):
    if len(opts[x]) != 2: continue
    mv = sum(S[t][x] != S[t - 1][x] for t in range(1, F1))
    KP = [min((0, 1), key=lambda k: keys(S[t], gk)[x][k]) for t in range(F1)]; KF = sum(KP[t] != KP[t - 1] for t in range(1, F1))
    KPe = [min((0, 1), key=lambda k: keys(S[t], ek)[x][k]) for t in range(F1)]; KFe = sum(KPe[t] != KPe[t - 1] for t in range(1, F1))
    if mv <= 1 + KF: continue
    print(f"TRACE241 {os.path.basename(sys.argv[1])}: mover x={x} (Γ3 vertex {V[('x', x)]}), level {lev[x]}, F1 {F1}")
    for k, o in enumerate(opts[x]):
        print(f"  option {k}: W-target {o[0]}, Ξ-target {o[1]}, gate index {gate[x][k]}, e-vertex index {V[('e', (x, k))]} (Γ3 as built: {gamma3.build(G, K.PADS)[3][('e', (x, k))]})")
    print(f"  s_t(x), t = 0..{F1 - 1}: {[S[t][x] for t in range(F1)]}; moves {mv}")
    print(f"  KP (gate keys) per state: {KP}; KF {KF}   -> moves {mv} > 1 + KF = {1 + KF}")
    print(f"  KP_e (e-index keys) per state: {KPe}; KF_e {KFe} -> moves {mv} <= 1 + KF_e = {1 + KFe}")
    for t in range(F1): print(f"  state {t}: gate keys {keys(S[t], gk)[x]}  e keys {keys(S[t], ek)[x]}")
