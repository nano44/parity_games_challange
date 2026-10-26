#!/usr/bin/env python3
"""L-SI box 21 (successor 17): the abstract model ABS of a pure C-interval after A's freeze (docs/si/N5-GCX-box21.md §7). DATA tool.
A DAG on non-terminals 0..n-1 (vertex v's successors are > v or terminals), terminals t with two values h(t) <= T(t) (honest / W; offset
T - h >= 0), vertex weights w(v). A strategy s picks one successor per non-terminal. M(v) / N(v) := w(path) + h / T of the terminal reached.
Step (S4a in this model): arena Al(v) = {s(v)} u {y : M(y) > M(s(v))}; s' := a W-optimal strategy using arena edges only (DP in reverse
topological order; ties keep s(v), else the smallest successor). Count steps to the fixed point; compare with n.
Also checks M and N non-decreasing (the model's M2 / WM; MONO_V must be 0) and Lemma ABS-HEIGHT (HEIGHT_V must be 0; control
ABSMUT=1 tests height - 1 and must fire on a climbed instance).
Usage: absmodel.py --rand COUNT N SEED | --climb STEPS N SEED"""
import sys, os, random
from collections import Counter
C = Counter(); ABSMUT = os.environ.get("ABSMUT") == "1"

def vals(g, s):
    n, succ, w, h, T = g; M = [0] * n; N = [0] * n
    for v in range(n - 1, -1, -1):
        y = s[v]
        if y >= n: M[v] = w[v] + h[y - n]; N[v] = w[v] + T[y - n]
        else: M[v] = w[v] + M[y]; N[v] = w[v] + N[y]
    return M, N

def height(g):
    n, succ = g[0], g[1]; hgt = [0] * n
    for v in range(n - 1, -1, -1): hgt[v] = 1 + max((hgt[y] if y < n else 0) for y in succ[v])
    return max(hgt)

def step(g, s):
    n, succ, w, h, T = g; M, N = vals(g, s)
    hv = lambda y: h[y - n] if y >= n else M[y]
    al = [[y for y in succ[v] if y == s[v] or hv(y) > hv(s[v])] for v in range(n)]
    best = [0] * n; s2 = list(s)
    for v in range(n - 1, -1, -1):
        tv = lambda y: T[y - n] if y >= n else best[y]
        bv = max(tv(y) for y in al[v])
        if tv(s[v]) == bv: s2[v] = s[v]
        else: s2[v] = min(y for y in al[v] if tv(y) == bv)
        best[v] = w[v] + bv
    return s2

def run(g, s, cap=10000):
    k = 0; M0, N0 = vals(g, s); hg = height(g) - (1 if ABSMUT else 0)
    while k < cap:
        s2 = step(g, s)
        if s2 == s:
            if k > hg: C["HEIGHT_V"] += 1                  # Lemma ABS-HEIGHT: steps <= height of the DAG (control ABSMUT=1: height - 1)
            return k
        M1, N1 = vals(g, s2)
        if any(a < b for a, b in zip(M1, M0)) or any(a < b for a, b in zip(N1, N0)): C["MONO_V"] += 1
        s, M0, N0, k = s2, M1, N1, k + 1
    return k

def rgame(rng, n, nt):
    succ = [sorted(set(rng.sample(range(v + 1, n + nt), min(rng.randint(1, 3), n + nt - v - 1)))) for v in range(n)]
    w = [rng.choice((1, -1)) * (1 << rng.randrange(0, 2 * n)) if rng.random() < 0.7 else 0 for v in range(n)]
    h = [rng.randrange(-(1 << (2 * n)), 1 << (2 * n)) for _ in range(nt)]
    T = [x + (rng.randrange(0, 1 << (2 * n)) if rng.random() < 0.7 else 0) for x in h]
    return (n, succ, w, h, T)

def main():
    a = sys.argv[1:]; cnt, n, seed = int(a[1]), int(a[2]), int(a[3]); rng = random.Random(seed)
    if a[0] == "--rand":
        worst = (0, None)
        for _ in range(cnt):
            g = rgame(rng, n, rng.randint(2, 4)); s = [rng.choice(g[1][v]) for v in range(n)]
            k = run(g, s); C["games"] += 1; C["steps_gt_n"] += k > n; C["steps_ge_n"] += k >= n
            if k > worst[0]: worst = (k, g, s)
        print(f"n={n}", " ".join(f"{k}={v}" for k, v in sorted(C.items())), "max_steps", worst[0])
    else:                                                  # hill-climb on the number of steps
        g = rgame(rng, n, 3); s = [rng.choice(g[1][v]) for v in range(n)]; k = run(g, s)
        for _ in range(cnt):
            n_, succ, w, h, T = g; succ = [list(x) for x in succ]; w = list(w); h = list(h); T = list(T); s2 = list(s); r = rng.random(); v = rng.randrange(n)
            if r < 0.3: w[v] = rng.choice((1, -1, 0)) * (1 << rng.randrange(0, 2 * n))
            elif r < 0.5 and v + 1 < n + len(h):
                y = rng.randrange(v + 1, n + len(h)); succ[v] = sorted(set(succ[v] + [y]))
            elif r < 0.6 and len(succ[v]) > 1: succ[v].remove(rng.choice(succ[v]))
            elif r < 0.8: i = rng.randrange(len(h)); h[i] = rng.randrange(-(1 << (2 * n)), 1 << (2 * n)); T[i] = max(T[i], h[i])
            else: i = rng.randrange(len(h)); T[i] = h[i] + rng.randrange(0, 1 << (2 * n))
            s2 = [x if x in succ[u] else rng.choice(succ[u]) for u, x in enumerate(s2)]
            if rng.random() < 0.3: u = rng.randrange(n); s2[u] = rng.choice(succ[u])
            g2 = (n, succ, w, h, T); k2 = run(g2, s2)
            if k2 >= k: g, s, k = g2, s2, k2
        print(f"climb n={n} best steps {k} (n = {n})", " ".join(f"{a}={b}" for a, b in sorted(C.items())))
        print("GAME", g); print("START", s)

if __name__ == "__main__":
    main()
