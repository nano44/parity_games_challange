#!/usr/bin/env python3
"""Box 208 (L-NEW successor 72): the abstract core of Lemma LEVEL, on its own engine (no VJ valuation, no genome, no code of another box).
A SHORTEST-PATH GAME: vertices 0..n-1 owned by Max or Min, a target, edges with integer weights >= 0. For a positional Max strategy s,
d_s(v) := the least weight of a path from v to the target in the graph where every Max vertex keeps only its edge s(v) (infinite if
there is none). HOWARD for Max: every Max vertex moves to an edge of largest w + d_s(successor), keeping its edge if that is one of
the largest; stop when nothing changes. Reference b = the last state; LAG, m, FRONT, Phi, STALL as in level208.py with d in place of
the class.
Must-0 counters (unit: states with a lagging vertex, unless stated):
  monofail (unit (vertex, step)): d falls;  phifail: Phi falls, or stays equal at a non-stall step;
  levfail: m_t is not w(z, y) + d_b(y) for an edge (z, y) of a Max vertex z;
  stall0 (only without zero-weight cycles): a stall;   stallnocyc: a stall without a cycle of weight-0 edges inside FRONT_t
  (Max vertex -> its edge at b, Min vertex -> its edge at t);
  boundfail (unit games, only without zero-weight cycles): more than (number of Max edges) * n Howard steps;
  optfail (unit games, n <= 9, only without zero-weight cycles): the last d is not the pointwise maximum of d_s over ALL Max strategies.
Descriptive: games, maxT, stalls. Control ABS_CTRL=1: Howard moves to an edge of SMALLEST w + d (monofail must fire).
Usage: abs208.py SEED COUNT NMAX ZERO   (ZERO = 0: every weight-0 edge goes to a higher index or to the target, so no weight-0 cycle;
ZERO = 1: weight-0 edges anywhere)."""
import sys, os, random, itertools, collections, heapq
CTRL = os.environ.get("ABS_CTRL") == "1"; INF = float("inf")

def gen(rng, nmax, zero):
    n = rng.randint(3, nmax); own = [rng.randrange(2) for _ in range(n)]; E = []
    for v in range(n):
        es = []
        for _ in range(rng.randint(1, 3)):
            y = rng.choice(list(range(n)) + [n]); w = rng.choice([0, 0, 1, 2, 4, 8, 16, 32])
            if w == 0 and not zero and y != n and y <= v: w = rng.choice([1, 2, 4, 8, 16, 32])
            es.append((y, w))
        E.append(es)
    return n, own, E

def dist(n, own, E, s):
    rev = [[] for _ in range(n + 1)]
    for v in range(n):
        for (y, w) in ([E[v][s[v]]] if own[v] == 0 else E[v]): rev[y].append((v, w))
    d = [INF] * (n + 1); d[n] = 0; pq = [(0, n)]
    while pq:
        dv, v = heapq.heappop(pq)
        if dv > d[v]: continue
        for (u, w) in rev[v]:
            if dv + w < d[u]: d[u] = dv + w; heapq.heappush(pq, (d[u], u))
    return d

def howard(n, own, E, s):
    hist = [(list(s), dist(n, own, E, s))]
    while len(hist) < 5000:
        s, d = hist[-1]; ns = list(s)
        for v in range(n):
            if own[v]: continue
            val = [w + d[y] for (y, w) in E[v]]; best = (min if CTRL else max)(val)
            if val[s[v]] != best: ns[v] = val.index(best)
        if ns == s: break
        hist.append((ns, dist(n, own, E, ns)))
    return hist

def check(n, own, E, hist, zero, c):
    b = len(hist) - 1; db = hist[b][1]; prev = None
    lev = set(w + db[y] for v in range(n) if own[v] == 0 for (y, w) in E[v])
    for t in range(b):
        s, d = hist[t]; d2 = hist[t + 1][1]
        c["monofail"] += sum(1 for v in range(n) if d2[v] < d[v])
        lag = [v for v in range(n) if d[v] != db[v]]
        if not lag: continue
        m = min(d[v] for v in lag); F = set(v for v in lag if d[v] == m); phi = (m, -len(F))
        stall = all(d2[v] == d[v] for v in F)
        if prev is not None and phi < prev[0]: c["phifail"] += 1
        if prev is not None and phi == prev[0] and not prev[1]: c["phifail"] += 1
        prev = (phi, stall)
        if m not in lev: c["levfail"] += 1
        if stall:
            c["stalls"] += 1
            if not zero: c["stall0"] += 1
            # weight-0 cycle inside F: Max vertex -> its edge at b; Min vertex -> an edge realising d at t
            def nx(v):
                if own[v] == 0: y, w = E[v][hist[b][0][v]]
                else: y, w = min(E[v], key=lambda e: e[1] + d[e[0]])
                return y if w == 0 else None
            ok = False
            for v0 in F:
                seen = set(); v = v0
                while v is not None and v in F and v not in seen: seen.add(v); v = nx(v)
                if v is not None and v in seen: ok = True; break
            if not ok: c["stallnocyc"] += 1
    if not zero:
        if b > sum(len(E[v]) for v in range(n) if own[v] == 0) * n: c["boundfail"] += 1
        if n <= 9:
            mx = [x for x in range(n) if own[x] == 0]; best = [0] * (n + 1)
            for ch in itertools.product(*[range(len(E[x])) for x in mx]):
                s = [0] * n
                for x, k in zip(mx, ch): s[x] = k
                dd = dist(n, own, E, s); best = [max(best[v], dd[v]) for v in range(n + 1)]
            if best != db: c["optfail"] += 1
    c["maxT"] = max(c["maxT"], b)

if __name__ == "__main__":
    seed, cnt, nmax, zero = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]); rng = random.Random(seed); c = collections.Counter()
    for _ in range(cnt):
        n, own, E = gen(rng, nmax, zero); s = [rng.randrange(len(E[v])) for v in range(n)]
        check(n, own, E, howard(n, own, E, s), zero, c)
    print("abs seed", seed, "games", cnt, "nmax", nmax, "zero", zero, "ctrl", int(CTRL),
          " ".join("%s %d" % (k, c[k]) for k in ("monofail", "phifail", "levfail", "stall0", "stallnocyc", "boundfail", "optfail", "stalls", "maxT")), flush=True)
