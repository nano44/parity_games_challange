#!/usr/bin/env python3
"""Box 46: print the |D| = 1 fallback-free gaps of levels.py with NO rise of LEV_C (instance-style detail).
Usage: norise.py STARTS SEED --list FILE [--nmax N] [--max K]"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import levels as L
from levels import load, step, start_pair, Engine, dual
def viol(E, g, frame, xi, j):
    """a shortest path r (as a vertex list x..c) with value(r) > xi[x], or None"""
    n = g.n; pred = [[] for _ in range(n)]
    for v in range(n):
        for w in frame[v]: pred[w].append(v)
    best = None
    for c in [c for c in range(n) if xi[c][0] == c]:
        rc = E.rank[c]; stack = [([c], 0)]
        while stack:
            p, mask = stack.pop(); x = p[0]
            if best and len(p) >= len(best): continue
            if E.key((c, mask, len(p) - 1)) > E.key(xi[x]): best = p; continue
            if len(p) - 1 == n - 1: continue
            for q in pred[x]:
                if q not in p: stack.append(([q] + p, mask | (E.bit[q] if E.rank[q] > rc else 0)))
    return best
def run(g, start, name, out):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(g.succ[v]) >= 2]
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        rows.append(dict(s=tuple(s), lam=tuple(x[0] for x in vs), t=tuple(t), q=tuple(sb[q] for q in Q), sb=tuple(sb), xi=vs, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and (rows[j + 1]["lam"], rows[j + 1]["t"]) == (rows[i]["lam"], rows[i]["t"]): j += 1
        a, b = i, j; i = j + 1; tau = rows[a]["t"]; eps = []; k = a
        while k <= b:
            e = k
            while e + 1 <= b and rows[e + 1]["q"] == rows[k]["q"]: e += 1
            eps.append((k, e)); k = e + 1
        byc = {}
        for (x, y) in eps: byc.setdefault(rows[x]["q"], []).append((x, y))
        for conf, lst in byc.items():
            D = [q for q, w in zip(Q, conf) if w != tau[q]]
            if len(D) != 1 or len(lst) < 2: continue
            sbC = rows[lst[0][0]]["sb"]; frame = [[sbC[v]] if g.owner[v] == 1 else list(g.succ[v]) for v in range(g.n)]
            for (x0, y0), (x1, y1) in zip(lst, lst[1:]):
                if sum(rows[k]["fb"] for k in range(y0, x1)): continue
                ly = L.level(E, g, frame, rows[y0]["xi"], (), 10 ** 7); lx = L.level(E, g, frame, rows[x1]["xi"], (), 10 ** 7)
                if lx <= ly < g.n - 1:
                    out.append(1)
                    print(f"== {name} start {start is not None} phase [{a},{b}] D={D} u->{conf[Q.index(D[0])]} tau(u)={tau[D[0]]} gap {y0}->{x1} LEV {ly}->{lx}")
                    for k in range(y0, x1 + 1):
                        dk = [q for q in Q if rows[k]["sb"][q] != tau[q]]
                        ch = [v for v in range(g.n) if k > y0 and rows[k]["s"][v] != rows[k - 1]["s"][v]]
                        print(f"   state {k}: D={dk} sigma-bar(D)={[rows[k]['sb'][q] for q in dk]} switched={ch}")
                    p = viol(E, g, frame, rows[x1]["xi"], lx + 1)
                    print(f"   violating H_C path at x1 (len {len(p) - 1}): {p}; Xi(x)={rows[x1]['xi'][p[0]]}")
if __name__ == "__main__":
    a = sys.argv[1:]; nmax, mxk = 20, 10
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1]))
    R0 = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
    names = [l.split()[0] for l in open(a[3]) if l.strip() and not l.startswith("#")]; out = []
    for nm in names:
        g = load(os.path.join(R0, nm))
        if g.n > nmax: continue
        for st in [None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                             {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]:
            try: run(g, st, nm, out)
            except RecursionError: pass
    print("NORISE", len(out))
