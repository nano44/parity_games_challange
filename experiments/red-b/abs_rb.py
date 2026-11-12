#!/usr/bin/env python3
"""L-RED-B's own engine for box 208 par. 10, Statement ABS (a shortest-path game; NOT a parity game, NOT IDEAL-CYC).
Object: vertices 0..n-1, target n-1 (no out-edge), every other vertex owned by Max or Min with 1..3 out-edges, integer
weights >= 0, no cycle of total weight 0 (games with one are rejected). For a positional Max strategy s, d_s(v) = least
weight of a path from v to the target when every Max vertex keeps only s(v) (infinity if none) - Dijkstra on the reversed
graph. HOWARD: every Max vertex moves to an edge of largest w + d_s, keeping its edge if that is one of them.
Must-0 counters (reference b = the last state; LAG_t = {v : d_t(v) < d_b(v)}; m_t = least d_t on LAG_t; FRONT_t):
  mono   (vertex, step): d falls
  phi    (step t < T): Phi_t = (m_t, -|FRONT_t|) does not rise strictly (or LAG_t is empty before the last state)
  lev    (state t < T): m_t is not w(z, y) + d_b(y) for an edge (z, y) of a Max vertex z in FRONT_t with y not lagging
  bound  (game): more than (edges of Max vertices) * n steps
  opt    (game, n <= 8): the last d is not the pointwise maximum of d_s over ALL Max strategies (enumeration)
Control ABS_CTRL=1: Max moves to a SMALLEST edge (must fire).  Usage: abs_rb.py <seed> <count> <nmax> [weights...]"""
import sys, os, random, heapq, itertools
INF = float("inf")

def gen(rng, nmax, W):
    while True:
        n = rng.randint(2, nmax); tgt = n - 1
        owner = [rng.randrange(2) for _ in range(n)]
        E = []
        for v in range(n - 1):
            k = rng.randint(1, 3)
            E.append([(rng.randrange(n), rng.choice(W)) for _ in range(k)])
        E.append([])
        # reject zero-weight cycles
        col = [0] * n; ok = True
        def dfs(v):
            col[v] = 1
            for (y, w) in E[v]:
                if w == 0:
                    if col[y] == 1: return False
                    if col[y] == 0 and not dfs(y): return False
            col[v] = 2; return True
        for v in range(n):
            if col[v] == 0 and not dfs(v): ok = False; break
        if ok: return n, owner, E

def dist(n, owner, E, s):
    rev = [[] for _ in range(n)]
    for v in range(n - 1):
        es = [E[v][s[v]]] if owner[v] == 0 else E[v]
        for (y, w) in es: rev[y].append((v, w))
    d = [INF] * n; d[n - 1] = 0; pq = [(0, n - 1)]
    while pq:
        dv, v = heapq.heappop(pq)
        if dv > d[v]: continue
        for (u, w) in rev[v]:
            if dv + w < d[u]: d[u] = dv + w; heapq.heappush(pq, (d[u], u))
    return d

def run(n, owner, E, rng, ctrl):
    s = [rng.randrange(len(E[v])) if v < n - 1 else 0 for v in range(n)]
    hist = []
    while True:
        d = dist(n, owner, E, s); hist.append((list(s), d))
        new = list(s); ch = False
        for z in range(n - 1):
            if owner[z] != 0: continue
            vals = [w + d[y] for (y, w) in E[z]]
            b = min(vals) if ctrl else max(vals)
            if vals[s[z]] == b: continue
            new[z] = rng.choice([i for i, x in enumerate(vals) if x == b]); ch = True
        if not ch or len(hist) > 5000: return hist
        s = new

def main():
    seed, count, nmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    W = [int(x) for x in sys.argv[4:]] or [0, 1, 2, 4, 8]
    ctrl = int(os.environ.get("ABS_CTRL", "0")); rng = random.Random(seed)
    c = {"mono": 0, "phi": 0, "lev": 0, "bound": 0, "opt": 0}; maxT = 0; games = 0
    for _ in range(count):
        n, owner, E = gen(rng, nmax, W); games += 1
        hist = run(n, owner, E, rng, ctrl); T = len(hist) - 1; maxT = max(maxT, T)
        db = hist[-1][1]
        nme = sum(len(E[v]) for v in range(n - 1) if owner[v] == 0)
        if T > nme * n: c["bound"] += 1
        prev = None
        for t in range(T):
            s, d = hist[t]; d2 = hist[t + 1][1]
            c["mono"] += sum(1 for v in range(n) if d2[v] < d[v])
            lag = [v for v in range(n) if d[v] < db[v]]
            if not lag: c["phi"] += 1; continue
            m = min(d[v] for v in lag); fr = [v for v in lag if d[v] == m]; lagset = set(lag)
            phi = (m, -len(fr))
            if prev is not None and not (phi > prev): c["phi"] += 1
            prev = phi
            if not any(owner[z] == 0 and E[z][s[z]][0] not in lagset and m == E[z][s[z]][1] + db[E[z][s[z]][0]] for z in fr):
                c["lev"] += 1
        if n <= 8 and not ctrl:
            mv = [v for v in range(n - 1) if owner[v] == 0]
            best = [-1] * n
            for ch in itertools.product(*[range(len(E[v])) for v in mv]):
                s = [0] * n
                for v, i in zip(mv, ch): s[v] = i
                d = dist(n, owner, E, s)
                for v in range(n):
                    if d[v] > best[v]: best[v] = d[v]
            if best != db: c["opt"] += 1
    print("ABS seed %d games %d nmax %d weights %s ctrl %d | " % (seed, games, nmax, W, ctrl) +
          " ".join("%s %d" % (k, c[k]) for k in c) + " | max T %d" % maxT)

if __name__ == "__main__":
    main()
