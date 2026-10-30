#!/usr/bin/env python3
"""L-NEW box 87 (XI-CH-POLY via the ARV rank trick; docs/new/N5-ARV-box87.md). For every vertex v and every transition of a W-run F
(R89) at which Xi(v) changes with lambda(Xi(v)) fixed and the path set P changing, DEPTH := the number of elements of P (above the cycle
node) that both old and new P contain and that rank above r, the top of the symmetric difference (= the length of the common prefix of
the signed descending term lists). Checks Lemma PREFIX-MON: for every k <= 3 the k-term prefix key never decreases while lambda is fixed.
FLIP := the most path-set changes of one (F, v) whose top differing rank is the same r (CONJECTURE FLIP-c).
Prints per game max DEPTH, the depth histogram, max per (F, v) of changes with depth >= 1, >= 2, >= 4 (DEEP_4), and max XICH_F(v).
Usage: depth.py GAME.pg [START]"""
import sys, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
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
rk = E.rank; par = E.rankpar                                     # par[r] = parity of the vertex of rank r
def terms(mask):                                                 # signed descending term list of a path set (bit r = rank r)
    out = []; r = mask.bit_length() - 1
    while r >= 0:
        if mask >> r & 1: out.append(r)
        r -= 1
    return out
def tkey(r):                                                      # total order on terms: (r,+) above None above (r,-)
    return (1, r) if par[r] == 0 else (-1, -r)
def pkey(mask, k):
    ts = terms(mask)[:k]
    return tuple(tkey(r) for r in ts) + ((0, 0),) * (k - len(ts))
hist = Counter(); c = dict(prefix_viol=0); mx = dict(depth=0, d1=0, d2=0, d4=0, xich=0, flip=0)
for a, b in runs:
    for v in range(n):
        d1 = d2 = d4 = xich = 0; flips = Counter()
        for q in range(a, b):
            x0, x1 = XI[q][v], XI[q + 1][v]
            if x0 == x1: continue
            xich += 1
            if x0[0] != x1[0] or x0[1] == x1[1]: continue
            for k in (1, 2, 3):
                if pkey(x1[1], k) < pkey(x0[1], k): c['prefix_viol'] += 1
            diff = x0[1] ^ x1[1]; r = diff.bit_length() - 1; common = x0[1] & x1[1]
            dep = bin(common >> (r + 1)).count("1")
            flips[r] += 1; hist[dep] += 1; mx['depth'] = max(mx['depth'], dep); d1 += dep >= 1; d2 += dep >= 2; d4 += dep >= 4
        mx['d1'] = max(mx['d1'], d1); mx['d2'] = max(mx['d2'], d2); mx['d4'] = max(mx['d4'], d4); mx['xich'] = max(mx['xich'], xich); mx['flip'] = max([mx['flip']] + list(flips.values()))
print(f"DEPTH n {n} runs {len(runs)} {c} maxima {mx} hist {dict(sorted(hist.items()))}")
