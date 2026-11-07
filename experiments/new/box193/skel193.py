#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): Lemma SKELETON check on every forest of CS(M, A) (doc Addendum 1). tau(x) := max(chain(x) - {x}).
Checks for every item x: (a) the tau-path x, tau(x), tau(tau(x)), ... lies on chain(x) in this order; (b) every element z strictly
between tau^i(x) and tau^(i+1)(x) on chain(x) has tau(z) = tau^(i+1)(x) and z < tau^(i+1)(x); (c) number of ascents of chain(x)
>= number of nonempty segments. Usage: skel193.py M A"""
import sys, itertools

if __name__ == "__main__":
    M, A = int(sys.argv[1]), int(sys.argv[2]); items = range(1, M + 1); nf = bad = 0
    for par in itertools.product(range(M + 1), repeat=M):
        nx = dict(zip(items, par)); ch = {}; ok = True
        for i in items:
            seen = []; x = i
            while x and x not in seen: seen.append(x); x = nx[x]
            if x or sum(1 for p, q in zip(seen, seen[1:]) if q > p) > A: ok = False; break
            ch[i] = seen
        if not ok: continue
        nf += 1; tau = {x: max(ch[x][1:], default=0) for x in items}
        for x in items:
            c = ch[x]; sk = [x]
            while tau[sk[-1]]: sk.append(tau[sk[-1]])
            pos = [c.index(y) if y in c else -1 for y in sk]
            if -1 in pos or pos != sorted(pos): bad += 1; continue
            segs = 0
            for i in range(len(sk) - 1):
                seg = c[pos[i] + 1: pos[i + 1]]
                if seg: segs += 1
                if any(tau[z] != sk[i + 1] or z > sk[i + 1] for z in seg): bad += 1
            if sum(1 for p, q in zip(c, c[1:]) if q > p) < segs: bad += 1
    print(f"SKELETON CS(M {M}, A {A}): forests {nf}, violations {bad}")
