#!/usr/bin/env python3
"""L-SI box 21 (successor 17): the abstract model ABS on graphs WITH cycles (docs/si/N5-GCX-box21.md §8). DATA tool, brute force (n <= 8).
Non-terminals 0..n-1 (any successors among non-terminals and terminals n..n+nt-1), terminals with constants h <= T, weights w. A strategy
is VALID if every play reaches a terminal (no cycle). Step: arena Al(v) = {s(v)} u {y : M(y) > M(s(v))}; among valid arena strategies take
one whose N is pointwise maximal (if none is pointwise maximal: NOPT, the game is skipped), preferring agreement with s. Counts steps.
Usage: abscyc.py --rand COUNT N SEED | --climb STEPS N SEED"""
import sys, random, itertools
from collections import Counter
C = Counter()

def plays(g, s):
    n, succ, w, h, T = g; M = [None] * n; N = [None] * n
    for v in range(n):
        path, x, seen = [], v, set()
        while x < n and x not in seen: seen.add(x); path.append(x); x = s[x]
        if x < n: return None                               # a cycle
        M[v], N[v] = sum(w[u] for u in path) + h[x - n], sum(w[u] for u in path) + T[x - n]
    return M, N

def step(g, s):
    n, succ = g[0], g[1]; M, N = plays(g, s)
    hv = lambda y: g[3][y - n] if y >= n else M[y]
    al = [[y for y in succ[v] if y == s[v] or hv(y) > hv(s[v])] for v in range(n)]
    best = None; cands = []
    for st in itertools.product(*al):
        r = plays(g, list(st))
        if r is None: continue
        cands.append((list(st), r[1]))
        best = r[1] if best is None else [max(a, b) for a, b in zip(best, r[1])]
    opt = [st for st, nn in cands if nn == best]
    if not opt: return None
    return max(opt, key=lambda st: sum(a == b for a, b in zip(st, s)))

def run(g, s, cap=200):
    k = 0
    while k < cap:
        s2 = step(g, s)
        if s2 is None: return None
        if s2 == s: return k
        s, k = s2, k + 1
    return k

def rgame(rng, n, nt):
    succ = [sorted(set(rng.sample([x for x in range(n + nt) if x != v], rng.randint(1, 3)))) for v in range(n)]
    for v in range(n):
        if not any(y >= n for y in succ[v]) and rng.random() < 0.5: succ[v].append(rng.randrange(n, n + nt))
    w = [rng.choice((1, -1)) * (1 << rng.randrange(0, 2 * n)) if rng.random() < 0.7 else 0 for v in range(n)]
    h = [rng.randrange(-(1 << (2 * n)), 1 << (2 * n)) for _ in range(nt)]
    T = [x + (rng.randrange(0, 1 << (2 * n)) if rng.random() < 0.7 else 0) for x in h]
    return (n, succ, w, h, T)

def valid_start(rng, g, tries=200):
    for _ in range(tries):
        s = [rng.choice(g[1][v]) for v in range(g[0])]
        if plays(g, s) is not None: return s
    return None

def main():
    a = sys.argv[1:]; cnt, n, seed = int(a[1]), int(a[2]), int(a[3]); rng = random.Random(seed)
    if a[0] == "--rand":
        mx = 0
        for _ in range(cnt):
            g = rgame(rng, n, rng.randint(2, 3)); s = valid_start(rng, g)
            if s is None: continue
            k = run(g, s)
            if k is None: C["NOPT"] += 1; continue
            C["games"] += 1; C["steps_gt_n"] += k > n; mx = max(mx, k)
        print(f"n={n}", " ".join(f"{x}={y}" for x, y in sorted(C.items())), "max_steps", mx)
    else:
        g = rgame(rng, n, 3); s = valid_start(rng, g)
        while s is None or run(g, s) is None: g = rgame(rng, n, 3); s = valid_start(rng, g)
        k = run(g, s)
        for _ in range(cnt):
            n_, succ, w, h, T = g; succ = [list(x) for x in succ]; w = list(w); h = list(h); T = list(T); r = rng.random(); v = rng.randrange(n)
            if r < 0.3: w[v] = rng.choice((1, -1, 0)) * (1 << rng.randrange(0, 2 * n))
            elif r < 0.5: succ[v] = sorted(set(succ[v] + [rng.choice([x for x in range(n + len(h)) if x != v])]))
            elif r < 0.6 and len(succ[v]) > 1: succ[v].remove(rng.choice(succ[v]))
            elif r < 0.8: i = rng.randrange(len(h)); h[i] = rng.randrange(-(1 << (2 * n)), 1 << (2 * n)); T[i] = max(T[i], h[i])
            else: i = rng.randrange(len(h)); T[i] = h[i] + rng.randrange(0, 1 << (2 * n))
            g2 = (n, succ, w, h, T); s2 = [x if x in succ[u] else rng.choice(succ[u]) for u, x in enumerate(s)]
            if rng.random() < 0.3: u = rng.randrange(n); s2[u] = rng.choice(succ[u])
            if plays(g2, s2) is None: continue
            k2 = run(g2, s2)
            if k2 is not None and k2 >= k: g, s, k = g2, s2, k2
        print(f"climb n={n} best steps {k}", " ".join(f"{x}={y}" for x, y in sorted(C.items())))
        print("GAME", g); print("START", s)

if __name__ == "__main__":
    main()
