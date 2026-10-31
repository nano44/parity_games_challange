#!/usr/bin/env python3
"""L-NEW box 106 (docs/new/N5-TIE-box106.md): Lemma KEY-MON on W-constant intervals. W-runs as box92/xirun.py; a W-constant interval is a
maximal run of consecutive states of a W-run with W unchanged. For every vertex x with lambda_W(x) = c != x and c EVEN (SPEC par 0):
key_t(x) := the (sigma_t, tau)-path x = x_0 -> ... -> x_l = c read from c's end (x_{l-1}, ..., x_0) (T54's key). Checks inside each interval:
  KEYUP   key_{t+1}(x) > key_t(x) lexicographically (KEY-MON claims never)
  SWNOTDOWN  an Even x switches at t but key_{t+1}(x) is not < key_t(x) (KEY-MON claims never)
  ODDUP   for c ODD and Even x: index(sigma_{t+1}(x)) > index(sigma_t(x)) (IDX-MONO claims never)
Reports also max key changes of one vertex in one interval (KEYCH), max switches of one Even vertex in one interval, and the tie returns
inside one interval. Usage: keymon.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
c = dict(intervals=0, KEYUP=0, SWNOTDOWN=0, ODDUP=0, KEYCH=0, SWI=0, TRETI=0, LEN=0)
def key(k, x, tau, cn):
    p = [x]; y = x
    while y != cn:
        y = S[k][y] if own[y] == 0 else tau[y]; p.append(y)
        if len(p) > n + 1: return None
    return tuple(reversed(p[:-1]))
for a, b in runs:
    tau = TAU[a]; k = a
    while k < b:
        e = k
        while e < b and Wv(e + 1, tau) == Wv(e, tau): e += 1
        if e > k:
            c['intervals'] += 1; c['LEN'] = max(c['LEN'], e - k); W = Wv(k, tau)
            kc = {}; sw = {}; held = {}
            for q in range(k, e):
                for x in range(n):
                    cn = W[x][0]
                    if cn == x: continue
                    if E.par[cn] == 0:
                        k0, k1 = key(q, x, tau, cn), key(q + 1, x, tau, cn)
                        if k0 is None or k1 is None: continue
                        if k1 > k0: c['KEYUP'] += 1
                        if k1 != k0: kc[x] = kc.get(x, 0) + 1
                        if own[x] == 0 and S[q + 1][x] != S[q][x] and not k1 < k0: c['SWNOTDOWN'] += 1
                    elif own[x] == 0 and S[q + 1][x] > S[q][x] and S[q + 1][x] != S[q][x]: c['ODDUP'] += 1
                    if own[x] == 0 and S[q + 1][x] != S[q][x]:
                        sw[x] = sw.get(x, 0) + 1
                        if (x, S[q + 1][x]) in held: c['TRETI'] += 1
                        held[(x, S[q][x])] = 1
            c['KEYCH'] = max([c['KEYCH']] + list(kc.values())); c['SWI'] = max([c['SWI']] + list(sw.values()))
        k = e if e > k else k + 1
print(f"KEYMON {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
