#!/usr/bin/env python3
"""L-SI box 17: DATA for Lemma P^c_ok and Corollary FRZ-OK (docs/si/N5-RUND-box17.md §13). On a maximal fallback-free in-phase run S with
(h3_D) at every state (so lambda_W is constant: CR-D's (ii)), at coarse level L (env L, default -1 = full (c, P)):
  an Even edge (x, z) is OK on S if at no state k of S (k < last) it is FORBIDDEN at L: COARSE_L W_k(z) >_L COARSE_L W_k(sigma_k x) and
  not Xi_k(z) > Xi_k(sigma_k x).
  FRZ-OK: for t >= k_0 + n - 1 and every x whose W-play prefix at t (up to its cycle node) uses only OK Even edges (Odd edges are tau's),
  COARSE_L(W_t(x)) = COARSE_L(W_{k_0+n-1}(x)).
Reports the checks (pairs (t, x)), the share of (t, x) pairs covered, the CONTENT (pairs where COARSE_L(W) has a non-empty path part),
and violations FRZOK_V. MUT=1: the freeze is tested from k_0 + 1 (control). Usage: okfrz.py --one GAME [START] | --list FILE [KMIN]"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "fb2o"))
from n5x import step, start_pair, Engine, dual, load, readstart
from tcdir import lasso, wval
L = int(os.environ.get("L", "-1")); MUT = os.environ.get("MUT") == "1"
C = Counter(); VIOL = []

def ck(E, x):
    m = (x[1] >> (L + 1)) << (L + 1) if L >= 0 else x[1]
    return (E.rew[x[0]], E.weight(m))

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        D = [u for u in range(g.n) if g.owner[u] == 1 and sb[u] != t[u]]
        wn = (lambda s, t: (lambda v: s[v] if g.owner[v] == 0 else t[v]))(list(s), tuple(t))
        W = [wval(E, wn, v) for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), s=list(s), wn=wn, vs=vs, W=W, h3=all(vs[u][0] == W[u][0] for u in D),
                         fb=r[4] if r else 0))
        if r is None: break
        s, t = r[0], r[1]
    i = 0
    while i < len(rows):
        j = i
        while j + 1 < len(rows) and not rows[j]["fb"] and rows[j + 1]["key"] == rows[i]["key"]: j += 1
        base = i + (1 if MUT else g.n - 1)
        if j > base and all(rows[x]["h3"] for x in range(i, j + 1)): run(g, E, name, rows, i, j, base)
        i = j + 1

def run(g, E, name, rows, i, j, base):
    C["runs"] += 1
    bad = set()
    for k in range(i, j):
        R = rows[k]
        for x in range(g.n):
            if g.owner[x] != 0: continue
            a = R["s"][x]
            for z in set(g.succ[x]):
                if z != a and ck(E, R["W"][z]) > ck(E, R["W"][a]) and not E.key(R["vs"][z]) > E.key(R["vs"][a]): bad.add((x, z))
    C["forbidden_edges"] += len(bad)
    for tt in range(base + 1, j + 1):
        R = rows[tt]
        for x in range(g.n):
            pl, ci = lasso(R["wn"], x); c = R["W"][x][0]; pre = pl[:pl.index(c)]
            C["pairs"] += 1
            if any(g.owner[y] == 0 and (y, R["s"][y]) in bad for y in pre): continue
            C["covered"] += 1; C["content"] += ck(E, R["W"][x])[1] != 0
            if ck(E, R["W"][x]) != ck(E, rows[base]["W"][x]): C["FRZOK_V"] += 1; VIOL.append((name, i, tt, x))

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
    print(f"L={L}", " ".join(f"{k}={v}" for k, v in sorted(C.items())))
    for v in VIOL[:8]: print("VIOLATION", v)
    print("OKFRZ PASS" if not VIOL else "OKFRZ FAIL")

if __name__ == "__main__":
    main()
