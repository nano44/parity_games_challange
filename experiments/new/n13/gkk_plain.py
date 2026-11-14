#!/usr/bin/env python3
"""N13 probe: the symmetric GKK potential iteration (P. Ohlmann, arXiv 2110.04533v1, Section 3) on the parity-induced mean-payoff game
(Even = Max, Odd = Min, weight of every edge leaving v = (-1)^p (n+1)^p, p = compressed priority).  Exact integers.
usage: gkk.py [--cap K] game.pg     prints: n m d iters maxbits WE status"""
import sys


def read_pg(path):
    owner, pr, succ = {}, {}, {}
    for line in open(path):
        line = line.strip()
        if not line or line.startswith('parity') or line.startswith('start'): continue
        p = line.rstrip(';').split()
        v = int(p[0]); pr[v] = int(p[1]); owner[v] = int(p[2]); succ[v] = [int(x) for x in p[3].split(',')]
    ids = sorted(owner); idx = {v: i for i, v in enumerate(ids)}
    return len(ids), [owner[v] for v in ids], [pr[v] for v in ids], [sorted(set(idx[u] for u in succ[v])) for v in ids]


def compress(pr):
    out, cur = {}, -1
    for p in sorted(set(pr)):
        cur += 1
        if cur % 2 != p % 2: cur += 1
        out[p] = cur
    return [out[p] for p in pr]


def gkk(n, owner, pr, succ, cap=None):
    cpr = compress(pr); B = n + 1
    w0 = [(B ** p) if p % 2 == 0 else -(B ** p) for p in cpr]
    phi = [0] * n
    pred = [[] for _ in range(n)]
    for v in range(n):
        for u in succ[v]: pred[u].append(v)
    iters = 0; maxbits = 0
    while True:
        # signs of the modified weights; N* = Min-attractor to < 0 edges over 0 edges
        W = [[w0[v] + phi[u] - phi[v] for u in succ[v]] for v in range(n)]
        inN = [False] * n
        cnt = [0] * n
        Q = []
        for v in range(n):
            ws = W[v]
            if owner[v] == 1:
                if any(w < 0 for w in ws): inN[v] = True; Q.append(v)
            else:
                if all(w < 0 for w in ws): inN[v] = True; Q.append(v)
                elif all(w <= 0 for w in ws): cnt[v] = sum(1 for w in ws if w == 0)
                else: cnt[v] = -1                       # has a > 0 edge: in P
        # zero-edge predecessors
        zp = [[] for _ in range(n)]
        for v in range(n):
            if inN[v]: continue
            for u, w in zip(succ[v], W[v]):
                if w == 0: zp[u].append(v)
        while Q:
            u = Q.pop()
            for v in zp[u]:
                if inN[v]: continue
                if owner[v] == 1:
                    if all(w >= 0 for w in W[v]):       # Min vertex of Z (no < 0 edge): a zero edge into N*
                        inN[v] = True; Q.append(v)
                else:
                    if cnt[v] > 0:
                        cnt[v] -= 1
                        if cnt[v] == 0: inN[v] = True; Q.append(v)
        # delta- and delta+
        dm = None   # delta^- (negative, the largest)
        dp = None   # delta^+ (positive, the least)
        for v in range(n):
            ws = W[v]
            if inN[v]:
                if owner[v] == 0:
                    for u, w in zip(succ[v], ws):
                        if not inN[u] and (dm is None or w > dm): dm = w
                else:
                    if all(w > 0 for u, w in zip(succ[v], ws) if inN[u]):       # S_N
                        x = min(ws)
                        if dm is None or x > dm: dm = x
            else:
                if owner[v] == 1:
                    for u, w in zip(succ[v], ws):
                        if inN[u] and (dp is None or w < dp): dp = w
                else:
                    if all(w < 0 for u, w in zip(succ[v], ws) if not inN[u]):   # S_P
                        x = max(ws)
                        if dp is None or x < dp: dp = x
        assert dm is None or dm < 0; assert dp is None or dp > 0
        if dm is None and dp is None:
            return iters, maxbits, inN, phi, 'reduced'
        delta = min(x for x in ((-dm) if dm is not None else None, dp) if x is not None)
        for v in range(n):
            if not inN[v]: phi[v] += delta
        iters += 1
        b = delta.bit_length()
        if b > maxbits: maxbits = b
        if cap and iters >= cap:
            return iters, maxbits, inN, phi, 'CAP'


def main():
    args = sys.argv[1:]; cap = None
    if args[0] == '--cap': cap = int(args[1]); args = args[2:]
    n, owner, pr, succ = read_pg(args[0])
    iters, maxbits, inN, phi, status = gkk(n, owner, pr, succ, cap)
    print('n %d m %d d %d iters %d maxbits %d WE %d %s' % (n, sum(map(len, succ)), len(set(pr)), iters, maxbits, n - sum(inN), status))


if __name__ == '__main__':
    main()
