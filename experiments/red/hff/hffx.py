#!/usr/bin/env python3
"""L-RED successor 21: exact checker for L-NEW 26's Lemma FB-RISE (both forms) and the gap rise of Theorem HON-FF
(docs/new/N5-HONFF-box47.md, l-new 385a5534 = trunk d67fdb87, sha1 544ae76a), written from its §0 definitions, not from L-NEW's code.
LEV(k) := largest j <= n-1 with Xi_k(x) >= value(r) for every x and every simple path r of G_tau (Odd vertices follow tau) with <= j edges
from x to a cycle node u of lambda (lambda(u) = u); value(r) = (u, P(r), |r|), P(r) = vertices of r before u ranked above u.
LEV_odd: the same with x Odd only. Computed EXACTLY: for each x, the minimum length of a simple path r with value(r) > Xi_k(x) (DFS over
simple paths, all of them; NMAX keeps it feasible); LEV = min(n-1, min over x of that length - 1).
Checks per phase (maximal run with (lambda, tau) constant):
  GEN_V  at every in-phase S4c fallback t -> t+1: LEV(t+1) >= min(LEV(t)+1, LEV_odd(t), n-1)
  HON_V  at every in-phase fallback t at or after a W-honest state h of the phase: LEV(t+1) >= min(LEV(h)+1, n-1)  (h = latest honest <= t)
  GAP_V  consecutive W-honest states h < h' of the phase with LEV(h) <= n-2: LEV(h') >= LEV(h)+1  (Theorem HON-FF's step; any gap)
  MON_V  LEV non-decreasing along the phase
Also counts W-honest states per phase against 4n^2 - 3n (HONCNT_V). MUT=1: GEN without the Odd term (control; should fail somewhere).
Usage: hffx.py --one GAME [START] | --list FILE [NMAX] (env RS)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "harness"))
from n5x import step, start_pair, Engine, dual, load, readstart
C = Counter(); VIOL = []; MUT = os.environ.get("MUT") == "1"

def minviol(E, g, tau, lam, Xi, x, cap):
    """min |r| over simple G_tau paths r from x to a cycle node u of lam with value(r) > Xi[x]; cap+1 if none with |r| <= cap."""
    best = [cap + 1]; kx = E.key(Xi[x]); cyc = {v for v in range(g.n) if lam[v] == v}
    succ = [g.succ[v] if g.owner[v] == 0 else [tau[v]] for v in range(g.n)]
    # targets: cycle nodes u whose best possible value could beat Xi[x]: rew(u) > rew(c) beats outright (shortest path decides);
    # u = c needs the path-set / length comparison (DFS); rew(u) < rew(c) can never beat.
    c = Xi[x][0]; INF = 10 ** 9
    def bfs_to(T):
        pred = [[] for _ in range(g.n)]
        for v in range(g.n):
            for w in set(succ[v]): pred[w].append(v)
        d = [INF] * g.n; fr = list(T)
        for t in T: d[t] = 0
        while fr:
            nf = []
            for w in fr:
                for v in pred[w]:
                    if d[v] == INF: d[v] = d[w] + 1; nf.append(v)
            fr = nf
        return d
    better = [u for u in cyc if E.rew[u] > E.rew[c]]
    if better:
        db = bfs_to(better)
        if db[x] < best[0]: best[0] = db[x]          # a shortest path is simple and its value beats Xi[x] (cycle node first)
    dc = bfs_to([c]) if c in cyc else [INF] * g.n
    cyc = {c} if c in cyc else set()
    path = [x]; onp = {x}
    def val_key(u):
        mask = 0
        for v in path[:-1]:
            if E.rank[v] > E.rank[u]: mask |= E.bit[v]
        return E.key((u, mask, len(path) - 1))
    def dfs(v):
        C["dfs"] += 1
        if C["dfs_budget"] and C["dfs"] > C["dfs_budget"]: raise TimeoutError
        L = len(path) - 1
        if L + dc[v] >= best[0]: return
        if v in cyc and val_key(v) > kx: best[0] = L; return
        if L + 1 >= best[0]: return
        for w in set(succ[v]):
            if w not in onp:
                path.append(w); onp.add(w); dfs(w); path.pop(); onp.discard(w)
    if x in cyc:   # the empty path: value (x, 0, 0) = Xi(x) exactly for a cycle node; longer paths still possible
        pass
    dfs(x)
    return best[0]

def levels(E, g, tau, lam, Xi):
    n = g.n; cap = n - 1; m_all = cap + 1; m_odd = cap + 1
    for x in range(n):
        m = minviol(E, g, tau, lam, Xi, x, cap)
        m_all = min(m_all, m)
        if g.owner[x] == 1: m_odd = min(m_odd, m)
    return min(n - 1, m_all - 1), min(n - 1, m_odd - 1)

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        hon_nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        for v in range(g.n):
            if E.key(playval(E, g, hon_nxt, v)) != E.key(vs[v]): C["SELFTEST_FAIL"] += 1
        rows.append(dict(s=tuple(s), tau=tuple(t), vs=vs, lam=tuple(x[0] for x in vs), fb=(r[4] if r else 0)))
        if r is None: break
        s, t = r[0], r[1]
    # W-honest: Xi_k = W_k, W_k = valuation of sigma_k in G_tau (Odd fixed to tau)
    for k, row in enumerate(rows):
        nxt = [row["s"][v] if g.owner[v] == 0 else row["tau"][v] for v in range(g.n)]
        row["honest"] = all(E.key(row["vs"][v]) == E.key(playval(E, g, nxt, v)) for v in range(g.n))
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["tau"]) == (rows[i]["lam"], rows[i]["tau"]): j += 1
        if any(rows[k]["fb"] for k in range(i, j)) or sum(rows[k]["honest"] for k in range(i, j + 1)) >= 2:
            try: phase(g, E, name, rows, i, j)
            except TimeoutError: C["UNK_phases"] += 1
        C["phases"] += 1; i = j + 1

def playval(E, g, nxt, v):
    order, seen = [], {}
    x = v
    while x not in seen: seen[x] = len(order); order.append(x); x = nxt[x]
    cyc = order[seen[x]:]; w = max(cyc, key=lambda u: E.rank[u])
    pre = order[:order.index(w)]
    mask = 0
    for u in pre:
        if E.rank[u] > E.rank[w]: mask |= E.bit[u]
    return (w, mask, len(pre))

def phase(g, E, name, rows, i, j):
    C["dfs"] = 0; C["dfs_budget"] = int(os.environ.get("BUDGET", "20000000"))
    lam = rows[i]["lam"]; tau = rows[i]["tau"]; LV = {}
    for k in range(i, j + 1): LV[k] = levels(E, g, tau, lam, rows[k]["vs"])
    n = g.n; lastH = None
    for k in range(i, j):
        if LV[k + 1][0] < LV[k][0]: C["MON_V"] += 1; VIOL.append(("MON", name, k))
    for k in range(i, j + 1):
        if rows[k]["honest"]:
            if lastH is not None and LV[lastH][0] <= n - 2:
                C["gaps"] += 1; C["gaps_with_fb"] += any(rows[t]["fb"] for t in range(lastH, k))
                if LV[k][0] < LV[lastH][0] + 1: C["GAP_V"] += 1; VIOL.append(("GAP", name, i, lastH, k, LV[lastH], LV[k]))
            lastH = k
        if k < j and rows[k]["fb"]:
            C["fb"] += 1; L, Lo = LV[k]
            need = min(L + 1, n - 1) if MUT else min(L + 1, Lo, n - 1)
            C["odd_binds"] += Lo <= L
            if LV[k + 1][0] < need: C["GEN_V"] += 1; VIOL.append(("GEN", name, i, k, LV[k], LV[k + 1]))
            if lastH is not None:
                C["fb_after_honest"] += 1
                if LV[k + 1][0] < min(LV[lastH][0] + 1, n - 1): C["HON_V"] += 1; VIOL.append(("HON", name, i, lastH, k, LV[lastH], LV[k + 1]))
    nh = sum(rows[k]["honest"] for k in range(i, j + 1))
    if nh > 4 * n * n - 3 * n: C["HONCNT_V"] += 1

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); st = readstart(a[2]) if len(a) > 2 else None
        check(g, a[1], st)
    else:
        nmax = int(a[2]) if len(a) > 2 else 20
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(f if os.path.isabs(f) else os.path.join(ROOT, f))
            if g.n > nmax: continue
            C["games"] += 1; check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    C.pop("dfs", None); C.pop("dfs_budget", None)
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:10]: print("VIOLATION", v)
    print("HFFX PASS" if not VIOL else "HFFX FAIL")

if __name__ == "__main__":
    main()
