#!/usr/bin/env python3
"""L-RED successor 22: the abstract model of N5-ABSCYC-box22 §1 (cyclic, terminals with h <= T) WITHOUT GEN, with an INDEX tie rule
(N5's S4a picks, among W-optimal successors, by successor-list order; modelled here as: among the arena strategies whose N is pointwise
maximal, the one whose choice vector is lexicographically smallest in successor index). Searches for runs longer than n (and >= 2n).
Values: N and M are (weight, -length) pairs so that length ties behave like N5's (shorter better here; a sign choice, symmetric).
Usage: abstie.py --rand COUNT N SEED [SMALL] | --climb STEPS N SEED"""
import sys, random, itertools

def plays(g, s):
    n, succ, w, h, T = g; M = [None] * n; N = [None] * n
    for v in range(n):
        path, x, seen = [], v, set()
        while x < n and x not in seen: seen.add(x); path.append(x); x = s[x]
        if x < n: return None
        L = len(path)
        M[v] = (sum(w[u] for u in path) + h[x - n], -L); N[v] = (sum(w[u] for u in path) + T[x - n], -L)
    return M, N

def step(g, s):
    n, succ = g[0], g[1]; r = plays(g, s); M = r[0]
    hv = lambda y: (g[3][y - n], 0) if y >= n else M[y]
    al = [[y for y in succ[v] if y == s[v] or hv(y) > hv(s[v])] for v in range(n)]
    best = None; cands = []
    for st in itertools.product(*al):
        rr = plays(g, list(st))
        if rr is None: continue
        cands.append((list(st), rr[1]))
        best = rr[1] if best is None else [max(a, b) for a, b in zip(best, rr[1])]
    opt = [st for st, nn in cands if nn == best]
    if not opt: return None
    return min(opt)

def run(g, s, cap=200):
    k = 0
    while k < cap:
        s2 = step(g, s)
        if s2 is None: return None
        if s2 == s: return k
        s, k = s2, k + 1
    return k

def rgame(rng, n, nt, small):
    succ = [sorted(set(rng.sample([x for x in range(n + nt) if x != v], rng.randint(1, min(4, n + nt - 1))))) for v in range(n)]
    if small:
        w = [rng.randint(-1, 1) for v in range(n)]; h = [rng.randint(-2, 2) for _ in range(nt)]; T = [x + rng.randint(0, 2) for x in h]
    else:
        w = [rng.choice((1, -1, 0)) * (1 << rng.randrange(0, 2 * n)) for v in range(n)]
        h = [rng.randrange(-(1 << (2 * n)), 1 << (2 * n)) for _ in range(nt)]; T = [x + rng.randrange(0, 1 << (2 * n)) for x in h]
    return (n, succ, w, h, T)

def valid_start(rng, g, tries=200):
    for _ in range(tries):
        s = [rng.choice(g[1][v]) for v in range(g[0])]
        if plays(g, s) is not None: return s
    return None

def mutate(rng, g, s):
    n, succ, w, h, T = g; succ = [list(x) for x in succ]; w = list(w); h = list(h); T = list(T); v = rng.randrange(n); r = rng.random()
    if r < 0.3: w[v] = rng.randint(-1, 1)
    elif r < 0.5: succ[v] = sorted(set(succ[v] + [rng.choice([x for x in range(n + len(h)) if x != v])]))
    elif r < 0.6 and len(succ[v]) > 1: succ[v].remove(rng.choice(succ[v]))
    elif r < 0.8: i = rng.randrange(len(h)); h[i] = rng.randint(-2, 2); T[i] = max(T[i], h[i])
    else: i = rng.randrange(len(h)); T[i] = h[i] + rng.randint(0, 3)
    g2 = (n, succ, w, h, T); s2 = [x if x in succ[u] else rng.choice(succ[u]) for u, x in enumerate(s)]
    if rng.random() < 0.3: u = rng.randrange(n); s2[u] = rng.choice(succ[u])
    return g2, s2

def main():
    a = sys.argv[1:]; cnt, n, seed = int(a[1]), int(a[2]), int(a[3]); rng = random.Random(seed)
    if a[0] == "--rand":
        small = len(a) > 4 and a[4] == "1"; mx = 0; gt = 0; games = 0
        for _ in range(cnt):
            g = rgame(rng, n, rng.randint(2, 3), small); s = valid_start(rng, g)
            if s is None: continue
            k = run(g, s)
            if k is None: continue
            games += 1; gt += k > n
            if k > mx: mx = k; best = (g, s)
        print(f"n={n} games={games} runs_gt_n={gt} max_steps={mx}"); print("BEST", best)
    else:
        g = rgame(rng, n, 3, True); s = valid_start(rng, g)
        while s is None or run(g, s) is None: g = rgame(rng, n, 3, True); s = valid_start(rng, g)
        k = run(g, s)
        for _ in range(cnt):
            g2, s2 = mutate(rng, g, s)
            if plays(g2, s2) is None: continue
            k2 = run(g2, s2)
            if k2 is not None and k2 >= k: g, s, k = g2, s2, k2
        print(f"climb n={n} best steps {k}"); print("GAME", g); print("START", s)

if __name__ == "__main__":
    main()
