#!/usr/bin/env python3
"""L-SI box 18 (successor 14): DATA for note §23 (FRZ-type route freeze between rho-transitions). Inside each phase ((lambda_Xi, tau)
constant), cut every maximal fallback-free run at its rho-transitions (some Xi(q), q in Q, changes) and at sigma-bar|Q changes (epoch
boundaries, ties included). On each remaining interval I (consecutive non-fallback transitions with Xi|Q and sigma-bar|Q constant) report:
  len      transitions of I
  tex      transitions of I changing some Q-exit path (relay.qexits; Lemma ROOT's paths)
  xich     transitions of I changing Xi at some vertex of Reach(Q)
  last     the last transition index of I (from I's start) with an Xi change on Reach(Q) (-1: none)
Candidate statement FRZ-RHO (note §23): last < n - 1 on every interval (Xi on Reach(Q) freezes within n - 1 transitions once Xi|Q and
sigma-bar|Q are fixed). FRZ_RHO_V counts intervals with last >= n - 1; TEX_GT counts tex > n - 1.
Usage: frzrho.py --one GAME [START] [-v] | --list FILE [KMIN] (env RS, NMAX)"""
import sys, os, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "new", "box21")); sys.path.insert(0, HERE)
from n5x import step, start_pair, Engine, dual, load, readstart
from relay import qexits
C = Counter(); VIOL = []; VERB = "-v" in sys.argv

def reach(nxt, Qs, succ):
    out = set(Qs)
    for (q, y, path, x) in qexits(nxt, Qs, succ): out.update(path)
    return out

def check(g, name, start=None):
    E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, start); rows = []
    Q = [v for v in range(g.n) if g.owner[v] == 1 and len(set(g.succ[v])) >= 2]; Qs = set(Q)
    while len(rows) <= 3000:
        vs, sb = E.evaluate(tuple(s)); r = step(g, E, Ed, s, t)
        nxt = [s[v] if g.owner[v] == 0 else sb[v] for v in range(g.n)]
        rows.append(dict(key=(tuple(x[0] for x in vs), tuple(t)), vs=vs, sb=list(sb), nxt=nxt, fb=r[4] if r else 0,
                         qx=qexits(nxt, Qs, g.succ), R=reach(nxt, Qs, g.succ)))
        if r is None: break
        s, t = r[0], r[1]
    k = 0
    while k < len(rows) - 1:
        A, B = rows[k], rows[k + 1]
        cut = (A["fb"] or A["key"] != B["key"] or any(tuple(A["vs"][q]) != tuple(B["vs"][q]) for q in Q)
               or any(A["sb"][q] != B["sb"][q] for q in Q))
        if cut: C["cuts"] += 1; k += 1; continue
        j = k
        while j + 1 < len(rows) - 1:
            A2, B2 = rows[j + 1], rows[j + 2]
            if (A2["fb"] or A2["key"] != B2["key"] or any(tuple(A2["vs"][q]) != tuple(B2["vs"][q]) for q in Q)
                    or any(A2["sb"][q] != B2["sb"][q] for q in Q)): break
            j += 1
        interval(g, name, rows, k, j + 1, Q)
        k = j + 1

def interval(g, name, rows, a, b, Q):
    """transitions a -> a+1, ..., b-1 -> b"""
    ln = b - a; tex = xich = 0; last = -1
    for k in range(a, b):
        A, B = rows[k], rows[k + 1]
        if A["qx"] != B["qx"]: tex += 1
        if any(tuple(A["vs"][v]) != tuple(B["vs"][v]) for v in A["R"] | B["R"]): xich += 1; last = k - a
    C["intervals"] += 1; C["trans"] += ln; C["max_len"] = max(C["max_len"], ln); C["max_tex"] = max(C["max_tex"], tex)
    C["max_last"] = max(C["max_last"], last); C["max_xich"] = max(C["max_xich"], xich)
    if last >= g.n - 1: C["FRZ_RHO_V"] += 1; VIOL.append(("FRZ_RHO", name, a, ln, last, g.n))
    if tex > g.n - 1: C["TEX_GT"] += 1
    if VERB and ln >= 3: print(f"  I {name} @{a} len={ln} tex={tex} xich={xich} last={last} n={g.n}")

def main():
    a = [x for x in sys.argv[1:] if x != "-v"]
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
    for v in VIOL[:8]: print("VIOLATION", v)
    print("FRZRHO PASS" if not VIOL else "FRZRHO FAIL")

if __name__ == "__main__":
    main()
