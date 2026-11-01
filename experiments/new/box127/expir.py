#!/usr/bin/env python3
"""L-NEW box 127: the EXPIRATION (alternation-free) property of Odd's optimal plays inside W-runs.
Source of the property: Gajjar & Radhakrishnan, arXiv 1811.05115, Proposition 5 (alternation-free / expiration property, Nikolova)
and the recursion f(n, 2^k - 1) <= 2n f(n, 2^(k-1) - 1) that follows it (p. 5-6), which gives Gusfield's n^(log n + O(1)).
For a state k and a vertex x, PI_k(x) := the path part of the (sigma_k, sbar_k)-play from x (x .. first visit of the cycle node c of
Xi_k(x)) followed by a virtual terminal T. Xi_k(x) = (c, P, l) is a function of PI_k(x) (asserted: len = l, P recomputed).
Per W-run (RESULTS R89: maximal run of consecutive states of one tau-stretch with no S4c fallback and lambda_W constant) and per source
x, the PI sequence is collapsed into blocks (consecutive equal entries merged). Checked:
  RET  : a path part that returns after being left (block i = block k, i < j < k)               [AF with (u, v) = (x, T)]
  AF   : i < j < k blocks, u, v on all three, PI_i[u:v] = PI_k[u:v] = q, PI_j[u:v] != q (incl. v before u on PI_j)
  QOFF : at an AF violation, q is not followable under sigma_j (an Even vertex of q has another successor at j); Q2OFF: PI_j[u:v]
         is not followable under sigma_i or sigma_k; NEITHER: both followable at all three times (only a cycle-node / threshold change
         or Odd's tie-break can then explain the alternation).
  XCH  : Xi_k(x) changes; BLK : blocks - 1 (>= XCH).
Usage: expir.py G.pg [START|-]   prints one EXP line (totals and maxima over all W-runs and sources) and up to 3 AF witnesses."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
import pg
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] != "-" else None
n = g.n; own = g.owner; E, Ed = Engine(g), Engine(dual(g))
s, t = start_pair(g, E, Ed, st); S, T, FB = [tuple(s)], [tuple(t)], []
while True:
    r = step(g, E, Ed, list(S[-1]), list(T[-1]))
    if r is None: break
    S.append(tuple(r[0])); T.append(tuple(r[1])); FB.append(r[4])
K = len(S) - 1
Wc = {}
def weng(tau):
    if tau not in Wc: Wc[tau] = Engine(pg.Game(list(g.prio), list(own), [[tau[v]] if own[v] == 1 else g.succ[v] for v in range(n)]))
    return Wc[tau]
LAM = [tuple(w[0] for w in weng(T[k]).evaluate(S[k])[0]) for k in range(K + 1)]
EV = [E.evaluate(x) for x in S]
TERM = -1
def pathpart(k, x):
    val, sb = EV[k]; c = val[x][0]; p = [x]; y = x
    while y != c:
        y = S[k][y] if own[y] == 0 else sb[y]; p.append(y)
        assert len(p) <= n + 1, "no cycle node on play"
    assert len(p) - 1 == val[x][2], (k, x, p, val[x])
    return tuple(p) + (TERM,)
# W-runs: maximal [a, b] with T, lambda_W constant and no fallback on every transition
runs = []; k = 0
while k < K:
    if FB[k] or T[k + 1] != T[k] or LAM[k + 1] != LAM[k]: k += 1; continue
    a = k
    while k < K and not FB[k] and T[k + 1] == T[k] and LAM[k + 1] == LAM[k]: k += 1
    runs.append((a, k))
tot = dict(runs=len(runs), maxrun=0, xch=0, blk=0, ret=0, af=0, afrev=0, maxxch=0, maxblk=0, srcviol=0, srcs=0, qoff=0, q2off=0, neither=0)
wit = []; bidx = {}
for a, b in runs:
    tot["maxrun"] = max(tot["maxrun"], b - a)
    PI = [[pathpart(k, x) for x in range(n)] for k in range(a, b + 1)]
    for x in range(n):
        xc = sum(EV[k][0][x] != EV[k + 1][0][x] for k in range(a, b))
        B = []; bidx.setdefault(x, [])
        bidx[x] = []
        for k in range(b - a + 1):
            if not B or B[-1] != PI[k][x]: B.append(PI[k][x]); bidx[x].append(k)
        tot["xch"] += xc; tot["blk"] += len(B) - 1; tot["maxxch"] = max(tot["maxxch"], xc); tot["maxblk"] = max(tot["maxblk"], len(B) - 1)
        tot["srcs"] += 1; bad = 0
        if len(set(B)) < len(B): tot["ret"] += 1; bad = 1
        pos = [{v: i for i, v in enumerate(p)} for p in B]
        for i in range(len(B)):
            for kk in range(i + 2, len(B)):
                pi, pk = B[i], B[kk]
                for iu, u in enumerate(pi):
                    if u not in pos[kk]: continue
                    ku = pos[kk][u]; A = []   # agreement prefix from u: the v with PI_i[u:v] = PI_k[u:v]
                    while iu + len(A) + 1 < len(pi) and ku + len(A) + 1 < len(pk) and pi[iu + len(A) + 1] == pk[ku + len(A) + 1]:
                        A.append(pi[iu + len(A) + 1])
                    if not A: continue
                    for j in range(i + 1, kk):
                        pj = B[j]
                        if u not in pos[j]: continue
                        ju = pos[j][u]
                        for m, v in enumerate(A):
                            if v not in pos[j]: continue
                            if pj[ju:ju + m + 2] != tuple([u] + A[:m + 1]):
                                tot["af"] += 1; bad = 1; tot["afrev"] += pos[j][v] < ju
                                q = (u,) + tuple(A[:m + 1]); qj = pj[ju:pos[j][v] + 1] if pos[j][v] > ju else None
                                ka, kb, kc = a + bidx[x][i], a + bidx[x][j], a + bidx[x][kk]
                                off = lambda seg, kz: any(own[y] == 0 and S[kz][y] != z for y, z in zip(seg, seg[1:]))
                                qoff = off(q, kb); q2off = qj is not None and (off(qj, ka) or off(qj, kc))
                                tot["qoff"] += qoff; tot["q2off"] += q2off; tot["neither"] += not (qoff or q2off)
                                if len(wit) < 3: wit.append((a, b, x, i, j, kk, u, v, pi, pj, pk))
                            break   # first v of A that lies on PI_j decides (later ones follow)
        tot["srcviol"] += bad
print(f"EXP {os.path.basename(sys.argv[1])} n {n} K {K} WRUNS {tot['runs']} MAXRUN {tot['maxrun']} SRCS {tot['srcs']} XCH {tot['xch']} "
      f"BLK {tot['blk']} MAXXCH {tot['maxxch']} MAXBLK {tot['maxblk']} RET {tot['ret']} AF {tot['af']} AFREV {tot['afrev']} SRCVIOL {tot['srcviol']} QOFF {tot['qoff']} Q2OFF {tot['q2off']} NEITHER {tot['neither']}")
for w in wit:
    a, b, x, i, j, kk, u, v, pi, pj, pk = w
    print(f"  WIT run [{a},{b}] src {x} blocks {i}<{j}<{kk} u {u} v {v}\n    PI_i {pi}\n    PI_j {pj}\n    PI_k {pk}")
