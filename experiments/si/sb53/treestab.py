#!/usr/bin/env python3
"""L-SI box 53b (Lead 01:57Z, KEYCH-POLY proof side): Lemma TREE-STABLE inside W-constant intervals (W-runs and intervals as L-NEW
box105/keymon.py; read, not imported). For a state q of an interval I, an even W-cycle node c and an Even y != c with lambda_W(y) = c:
A_q(y) := ({sigma_q(y)} u Isigma_q(y)) restricted to W-tight edges (y (+) W(z) = W(y)); LexTree(A_q) := the tree of class c in which
every Even y takes the tight arena successor of least key (key = path to c read from c's end), Odd vertices follow tau.
LTX: sigma_(q+1) differs from LexTree(A_q) on class c (LEX-BFS as a tree statement claims never).
TSX: a class-c Even vertex switches at q+1 -> q+2 although no tight arena edge of class c is in A_(q+1) \\ A_q (TREE-STABLE claims never).
INS: per (I, c), transitions q -> q+1 with an insertion (A_(q+1) \\ A_q nonempty for some class-c y); NOVT: insertions that are not a
strict Xi-overtake of y's current target. KB: per (I, c, x), KEYCH_I(x) - (1 + INS_I(c)) > 0 (the bound claims never).
Reports MAXKEYCH, MAXINS, intervals. MUT=1 (control): LexTree takes the max, so LTX must become > 0. Usage: treestab.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
MUT = os.environ.get('MUT') == '1'  # control: LexTree with max in place of min must give LTX > 0
T = len(S) - 1; SU = [sorted(set(x)) for x in g.succ]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
XI = {}
def xi(k):
    if k not in XI:
        v, _ = E.evaluate(S[k]); XI[k] = (v, set(E.improving(S[k], v)))
    return XI[k]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
c = dict(intervals=0, LTX=0, TSX=0, NOVT=0, KB=0, MAXKEYCH=0, MAXINS=0)
def key(k, x, tau, cn):
    p = [x]; y = x
    while y != cn:
        y = S[k][y] if own[y] == 0 else tau[y]; p.append(y)
    return tuple(reversed(p[:-1]))
for a, b in runs:
    tau = TAU[a]; k = a
    while k < b:
        e = k
        while e < b and Wv(e + 1, tau) == Wv(e, tau): e += 1
        if e > k:
            c['intervals'] += 1; W = Wv(k, tau)
            cls = {}
            for x in range(n):
                if W[x][0] != x and E.par[W[x][0]] == 0: cls.setdefault(W[x][0], []).append(x)
            for cn, X in cls.items():
                EV = [x for x in X if own[x] == 0]
                tight = {y: [z for z in SU[y] if W[z][0] == cn and E.extend(y, W[z]) == W[y]] for y in EV}
                def arena(q):
                    _, I = xi(q)
                    return {y: frozenset(z for z in tight[y] if z == S[q][y] or (y, z) in I) for y in EV}
                def lextree(A):
                    order = sorted(X, key=lambda x: W[x][2]); K = {cn: ()}; ch = {}
                    for x in order:
                        if own[x] == 1: K[x] = K[tau[x]] + (x,)
                        else:
                            best = (max if MUT else min)(A[x], key=lambda z: K[z]); ch[x] = best; K[x] = K[best] + (x,)
                    return ch
                AR = [arena(q) for q in range(k, e + 1)]; ins = 0
                for i, q in enumerate(range(k, e)):
                    ch = lextree(AR[i])
                    if any(S[q + 1][y] != ch[y] for y in EV): c['LTX'] += 1
                    if i + 1 <= e - k:
                        new = [(y, z) for y in EV for z in AR[i + 1][y] - AR[i][y]] if i + 1 < len(AR) else []
                        if new: ins += 1
                        for y, z in new:
                            v0, _ = xi(q); v1, _ = xi(q + 1); t0 = S[q][y]; t1 = S[q + 1][y]
                            if not (E.key(v1[z]) > E.key(v1[t1]) and not E.key(v0[z]) > E.key(v0[t0])): c['NOVT'] += 1
                        if q + 2 <= e and any(S[q + 2][y] != S[q + 1][y] for y in EV) and not new: c['TSX'] += 1
                c['MAXINS'] = max(c['MAXINS'], ins)
                for x in X:
                    kc = sum(1 for q in range(k, e) if key(q, x, tau, cn) != key(q + 1, x, tau, cn))
                    c['MAXKEYCH'] = max(c['MAXKEYCH'], kc)
                    if kc > 1 + ins: c['KB'] += 1
        k = e if e > k else k + 1
print(f"TREESTAB {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
