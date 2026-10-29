#!/usr/bin/env python3
"""L-RED successor 27 (Lead 2026-10-29 13:47Z STEP 1, the COUPLED family): per joint lambda-run counts of sigma-changes and
tau-changes. lambda = cycle-node map of Xi_sigma on G (depends on sigma only); lambda^U = cycle-node map of U_tau (tau's valuation on
G^d, depends on tau only). A joint lambda-run = a maximal block of consecutive states with (lambda, lambda^U) constant.
Engine: L-COMP's n5b, SPEC mode, unmodified. Usage: cpl.py GAME.pg [START|S3]"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "n5-second"))
import n5b


def labels(path):
    lab = {}
    for line in open(path):
        m = re.match(r'\s*(\d+)\s.*"(.*)"', line)
        if m:
            lab[int(m.group(1))] = m.group(2)
    return lab


def run(g, s0=None, t0=None, max_iter=100000):
    N = n5b.N5(g, "spec"); tr, fb = [], []
    N.run(s0, t0, max_iter=max_iter, trace=tr, fbtrace=fb)
    return N, tr, fb


def analyse(g, N, tr, fb):
    n = g.n
    S = [list(s) for s, _ in tr]; T = [list(t) for _, t in tr]
    lam = [tuple(x[0] for x in N.ev(N.SG, s)) for s in S]
    lamU = [tuple(x[0] for x in N.ev(N.SD, t)) for t in T]
    K = len(tr)
    blocks, a = [], 0
    for k in range(1, K + 1):
        if k == K or (lam[k], lamU[k]) != (lam[k - 1], lamU[k - 1]):
            blocks.append((a, k - 1)); a = k
    out = []
    for a, b in blocks:
        sc = sum(1 for t in range(a, b) if S[t] != S[t + 1])
        tc = sum(1 for t in range(a, b) if T[t] != T[t + 1])
        both = sum(1 for t in range(a, b) if S[t] != S[t + 1] and T[t] != T[t + 1])
        alt = 0; last = None                       # side changes: s-only / t-only / both, count switches of side
        for t in range(a, b):
            ds, dt = S[t] != S[t + 1], T[t] != T[t + 1]
            side = "b" if ds and dt else ("s" if ds else "t")
            if last is not None and side != last:
                alt += 1
            last = side
        out.append(dict(a=a, b=b, len=b - a, sc=sc, tc=tc, both=both, alt=alt, fb=sum(fb[a:b])))
    return out, lam, lamU


def report(path, start):
    g = n5b.pg.read(path)
    s0, t0 = (None, None) if start in (None, "S3") else n5b.read_start(start, g)
    N, tr, fb = run(g, s0, t0)
    bl, _, _ = analyse(g, N, tr, fb)
    best = max(bl, key=lambda r: (min(r["sc"], r["tc"]), r["len"]))
    tsc = sum(1 for t in range(len(tr) - 1) if tr[t][0] != tr[t + 1][0]); ttc = sum(1 for t in range(len(tr) - 1) if tr[t][1] != tr[t + 1][1])
    return dict(n=g.n, it=len(tr) - 1, fb=sum(fb), sc=tsc, tc=ttc, runs=len(bl), best=best), bl, (N, tr, fb)


if __name__ == "__main__":
    r, bl, _ = report(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "S3")
    print(f"n {r['n']} it {r['it']} fb {r['fb']} sigma-changes {r['sc']} tau-changes {r['tc']} joint-lambda-runs {r['runs']} | "
          f"best run {r['best']}")
    if "-v" in sys.argv:
        for x in bl:
            print(" ", x)
