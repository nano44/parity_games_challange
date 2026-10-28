#!/usr/bin/env python3
"""L-NEW box 49 (successor 30), DATA: per phase of N5, the most Even switches of one Even vertex (SWE), the most sigma-bar changes of one Odd
vertex (SWO), the most Xi-changes of one vertex (XR), against n and the phase length L. A reader can inflate SWO and XR (docs/si/N5-ALT-box23.md
§8; docs/new/N5-READER-box49.md); this measures SWE on games without gadgets.
Usage: coresw.py STARTS SEED (--list FILE | files) [--nmax N]   (a .start file next to a game is used as its first start, else S3)"""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "experiments", "si", "root"))
from common import rows, phases, load, readstart
from collections import Counter

def run(g, st):
    E, R = rows(g, st); out = []
    for i, j in phases(R):
        swe, swo, xr = Counter(), Counter(), Counter()
        for k in range(i, j):
            a, b = R[k], R[k + 1]
            for v in range(g.n):
                if g.owner[v] == 0 and a["s"][v] != b["s"][v]: swe[v] += 1
                if g.owner[v] == 1 and a["sb"][v] != b["sb"][v]: swo[v] += 1
                if a["vs"][v] != b["vs"][v]: xr[v] += 1
        out.append((j - i, max(swe.values(), default=0), max(swo.values(), default=0), max(xr.values(), default=0)))
    return out

if __name__ == "__main__":
    a = sys.argv[1:]; nmax = 10 ** 9
    if "--nmax" in a: i = a.index("--nmax"); nmax = int(a[i + 1]); del a[i:i + 2]
    K = int(a[0]); RNG = random.Random(int(a[1])); a = a[2:]
    files = [os.path.join(ROOT, l.split()[0]) for l in open(a[1]) if l.strip() and not l.startswith("#")] if a[0] == "--list" else a
    best = dict(swe=(0, None), swe_n=(0.0, None), swo_n=(0.0, None), xr_n=(0.0, None)); runs = phs = 0
    for f in files:
        g = load(f)
        if g.n > nmax: continue
        sf = f[:-3] + ".start"
        sts = [readstart(sf) if os.path.exists(sf) else None] + [({v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 0},
                                                                  {v: RNG.choice(g.succ[v]) for v in range(g.n) if g.owner[v] == 1}) for _ in range(K)]
        for st in sts:
            try: res = run(g, st)
            except RecursionError: continue
            runs += 1
            for L, swe, swo, xr in res:
                phs += 1; tag = (os.path.relpath(f, ROOT), L)
                if swe > best["swe"][0]: best["swe"] = (swe, tag)
                for k, v in (("swe_n", swe), ("swo_n", swo), ("xr_n", xr)):
                    if v / g.n > best[k][0]: best[k] = (v / g.n, tag + (v, g.n))
    print(f"runs {runs} phases {phs}")
    for k, v in best.items(): print(k, v)
