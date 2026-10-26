#!/usr/bin/env python3
"""L-SI box 17: DATA for the class-relative freeze level (docs/si/N5-RUND-box17.md). At every state: D_k, the gates' honest and W values,
TWIN PAIRS (u, u' in D_k with lambda_Xi(u) = lambda_Xi(u') and lambda_W(u) = lambda_W(u')), and for each twin pair the RELATIVE
disagreement e(u, u') := (P(Xi u) ^ P(Xi u')) ^ (P(W u) ^ P(W u')), L_e := max over twin pairs of top(e) (-1 if none or e empty), against
M_D (max lev(Xi u, W u)) and the gates' cycle-node ranks. Per maximal fallback-free in-phase run: |S|, max |D|, max L_e, max M_D, the
top rank, and whether L_e is below every gate's cycle-node rank ("coherent": then routes compare the same way in both frames above the
cycle node). Usage: le.py --one GAME [START] | --list FILE [KMIN] (NMAX, RS env as rel.py)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval
INF = 10 ** 9
C = Counter(); OUT = []

def top(m): return m.bit_length() - 1 if m else -1

def lev(x, y):
    if x[0] != y[0]: return INF
    d = x[1] ^ y[1]
    return d.bit_length() - 1 if d else -1

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = [u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]]
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = {u: wval(E, wn, u) for u in D}
        h3 = all(vs[u][0] == W[u][0] for u in D)
        M = max([lev(vs[u], W[u]) for u in D], default=-1) if h3 else INF
        Le, tw = -1, 0
        for i, u in enumerate(D):
            for u2 in D[i + 1:]:
                if vs[u][0] == vs[u2][0] and W[u][0] == W[u2][0]:
                    tw += 1; Le = max(Le, top((vs[u][1] ^ vs[u2][1]) ^ (W[u][1] ^ W[u2][1])))
        cmin = min([E.rank[vs[u][0]] for u in D], default=INF)
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), D=len(D), M=M, Le=Le, tw=tw, cmin=cmin, h3=h3, fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        if j > i:
            S = rows[i:j + 1]; C["runs"] += 1
            Le = max(R["Le"] for R in S); M = max(R["M"] for R in S); tw = max(R["tw"] for R in S)
            coh = Le < min(R["cmin"] for R in S)
            C["twinruns"] += tw > 0; C["coherent_twinruns"] += tw > 0 and coh; C["Le_lt_M"] += tw > 0 and Le < M
            if len(S) >= g.n + 1 or tw > 0:
                OUT.append((name, i, j, len(S), g.n, "maxD", max(R["D"] for R in S), "twins", tw, "Le", Le, "M", M if M < INF else "INF",
                            "top", max(E.rank), "coherent", coh))
        i = j + 1

def main():
    a = sys.argv[1:]
    if a[0] == "--one":
        g = load(a[1]); check(g, a[1], readstart(a[2]) if len(a) > 2 else None)
    else:
        kmin = int(a[2]) if len(a) > 2 else 2
        for line in open(a[1]):
            f = line.strip()
            if not f: continue
            g = load(os.path.join(ROOT, f))
            if g.n > int(os.environ.get("NMAX", "48")) or sum(1 for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2) < kmin:
                continue
            check(g, f); rng = random.Random(f)
            for _ in range(int(os.environ.get("RS", "0"))):
                check(g, f + " rs", ({v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                     {v: rng.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}))
    print(" ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for x in OUT[:40]: print("RUN", x)

if __name__ == "__main__":
    main()
