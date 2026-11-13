#!/usr/bin/env python3
"""Packet P-N5-KEY1P follow-up (L-NEW successor 77): total iteration count of N5 (n5v, SPEC mode) from S3 on Gamma3(G) (box 189's
builder) against RESULTS R124's Corollary EXACT-L (exactly L(G) + 3 iterations, one fallback) on genome files; L(G) from one217.OneP.
Counters (must be 0): exl (iterations != T_key + 3), fbn (number of fallbacks != 1), fbat (the fallback is not transition T_key + 1).
Usage: gk_total.py G.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [HERE, os.path.join(ROOT, "experiments", "new", "box215"), os.path.join(ROOT, "experiments", "new", "box195")]
os.environ.setdefault("EG195_ROOT", ROOT); os.environ.setdefault("KM_MODE", "spec")
import one217, keyside215 as ks
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = G.get("genome", G); T = len(one217.OneP(G).run("key")) - 1
    g0, _, _, V = ks.gamma3.build(G, ks.eg195.PADS); g = ks.eg195.topg(g0)
    E, Ed = ks.n5v.Engine(g), ks.n5v.Engine(ks.n5v.dual(g)); sigma, tau = ks.n5x.start_pair(g, E, Ed, None); it = 0; fbs = []
    while it <= 200000:
        res = ks.n5v.step(g, E, Ed, sigma, tau, "spec")
        if res is None: break
        it += 1
        if res[4]: fbs.append(it)
        sigma, tau = list(res[0]), list(res[1])
    print(f"{os.path.basename(fn)} N {G['N']} n {g.n} T_key {T} iterations {it} fallbacks_at {fbs} | exl {int(it != T + 3)} fbn {int(len(fbs) != 1)} fbat {int(fbs[:1] != [T + 1])}", flush=True)
