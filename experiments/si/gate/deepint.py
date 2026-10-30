#!/usr/bin/env python3
"""L-SI box 51b §6 (Lead 14:09Z): L-NEW's DEEP_4 (experiments/new/box87/depth.py, l-new b46f7759; read-only copy depth_lnew_b46f7759.py
here, definitions unchanged: W-runs by tau, no fallback, sigma moves, lambda_W fixed; a path-set change of v at q -> q+1 has lambda(Xi(v))
fixed and P changing; DEPTH = common elements of old and new P above the top r of the symmetric difference) split by WHERE the change
happens: IN = at a W-flat transition (W_{q+1} = W_q read with tau: inside a W-constant interval), BD = at a W-changing transition (an
interval boundary). Prints totals of changes with depth >= 4 (N4_IN, N4_BD) and >= 1, the max per (F, v) of depth >= 4 changes in each
class (D4_IN, D4_BD; D4 = the box 87 DEEP_4 for the sum), the most depth >= 4 changes at one W-flat transition (PERFLAT4) and
at one W-changing transition (PERBD4; Lead 14:46Z: deep changes per W-change), and the W-changing transitions BDT. Usage: deepint.py GAME.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "..", "new", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); start = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); S = [tuple(s)]; TAU = [tuple(t)]; FB = []
while True:
    r = step(g, E, Ed, list(S[-1]), list(TAU[-1]))
    if r is None: break
    S.append(tuple(r[0])); TAU.append(tuple(r[1])); FB.append(r[4])
T = len(S) - 1
XI = [E.evaluate(x)[0] for x in S]
Wc = {}
def Wv(k, tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(g.owner), [[tau[v]] if g.owner[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau].evaluate(S[k])[0]
runs = []; cur = None
for k in range(T):
    ok = TAU[k + 1] == TAU[k] and not FB[k] and S[k + 1] != S[k] and [x[0] for x in Wv(k, TAU[k])] == [x[0] for x in Wv(k + 1, TAU[k])]
    if not ok: cur = None; continue
    if cur is None: cur = [k, k]; runs.append(cur)
    cur[1] = k + 1
c = dict(N1_IN=0, N1_BD=0, N4_IN=0, N4_BD=0, D4=0, D4_IN=0, D4_BD=0, FLAT=0, PERFLAT4=0, PERBD4=0, BDT=0)
for a, b in runs:
    flat = [Wv(q, TAU[q]) == Wv(q + 1, TAU[q]) for q in range(a, b)]; c['FLAT'] += sum(flat); c['BDT'] += len(flat) - sum(flat)
    per = [0] * (b - a)
    for v in range(n):
        di = db = 0
        for q in range(a, b):
            x0, x1 = XI[q][v], XI[q + 1][v]
            if x0 == x1 or x0[0] != x1[0] or x0[1] == x1[1]: continue
            diff = x0[1] ^ x1[1]; r = diff.bit_length() - 1; dep = bin((x0[1] & x1[1]) >> (r + 1)).count("1")
            k = 'IN' if flat[q - a] else 'BD'
            c['N1_' + k] += dep >= 1; c['N4_' + k] += dep >= 4
            if dep >= 4:
                if flat[q - a]: di += 1; per[q - a] += 1
                else: db += 1; per[q - a] += 1
        c['D4'] = max(c['D4'], di + db); c['D4_IN'] = max(c['D4_IN'], di); c['D4_BD'] = max(c['D4_BD'], db)
    c['PERFLAT4'] = max([c['PERFLAT4']] + [per[i] for i in range(b - a) if flat[i]])
    c['PERBD4'] = max([c['PERBD4']] + [per[i] for i in range(b - a) if not flat[i]])
print(f"DEEPINT {os.path.basename(sys.argv[1])} n {n} " + " ".join(f"{k} {v}" for k, v in c.items()))
