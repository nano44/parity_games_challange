#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): Lemma LOW-SHAPE check (doc Addendum 2) on every forest of CS(M, 1). tau(x) := max(chain(x) - {x}).
A LOW item x has x < tau(x). Checks: (a) chain(x) = a strictly descending run x = d_1 > ... > d_k (every d_j low with tau(d_j) = tau(x)),
then tau(x), then the tau-path of tau(x) exactly (no other element); (b) the tau-path below any item y with tau(y) < y is strictly
descending. Usage: low193.py M"""
import sys, itertools

if __name__ == "__main__":
    M = int(sys.argv[1]); items = range(1, M + 1); nf = bad = 0
    for par in itertools.product(range(M + 1), repeat=M):
        nx = dict(zip(items, par)); ch = {}; ok = True
        for i in items:
            seen = []; x = i
            while x and x not in seen: seen.append(x); x = nx[x]
            if x or sum(1 for p, q in zip(seen, seen[1:]) if q > p) > 1: ok = False; break
            ch[i] = seen
        if not ok: continue
        nf += 1; tau = {x: max(ch[x][1:], default=0) for x in items}
        def path(y):
            p = [y]
            while tau[p[-1]]: p.append(tau[p[-1]])
            return p
        for x in items:
            c = ch[x]
            if x < tau[x]:
                k = c.index(tau[x]); run = c[:k]
                if any(a <= b for a, b in zip(run, run[1:])) or any(not (d < tau[d] and tau[d] == tau[x]) for d in run): bad += 1
                if c[k:] != path(tau[x]): bad += 1
            p = path(x)
            if tau[x] and tau[x] < x and any(a <= b for a, b in zip(p, p[1:])): bad += 1
    print(f"LOW-SHAPE CS(M {M}, 1): forests {nf}, violations {bad}")
