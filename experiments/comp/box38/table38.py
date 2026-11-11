#!/usr/bin/env python3
"""L-COMP box 38 item 2(a): table of the exhaustive sweep (out/sw_N<N>M<M>.jsonl). Per (N, M, U): genomes (unit: one genome; set: ALL
genomes of (N, M) in the box 33/36 space with that U), max T3 with [E-LEV] and without (T3 = N5'-xi iterations from S3 on Gamma3 before
the first fallback; total over that run). Also writes out/argmax/ the T3-argmax genome per (N, M, U, mode) (first in enumeration order).
Usage: table38.py N,M [N,M ...]"""
import sys, os, json, collections
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box36")]
import gen36
os.makedirs(os.path.join(H, "out", "argmax"), exist_ok=True)
print("| N, M | N + M | U | genomes | blocks | max T3 [E-LEV] | max T3 no E-LEV |")
print("| --- | --- | --- | --- | --- | --- | --- |")
for nm in sys.argv[1:]:
    N, M = map(int, nm.split(",")); T = collections.OrderedDict()
    recs = [json.loads(l) for l in open(os.path.join(H, "out", f"sw_N{N}M{M}.jsonl"))]
    nb = sum(1 for _ in gen36.blocks(N, M)); assert len({r["i"] for r in recs}) == nb, f"incomplete {N},{M}"
    for r in sorted(recs, key=lambda r: r["i"]):
        t = T.setdefault(r["U"], dict(g=0, b=0, e=-1, n=-1, ae=None, an=None))
        t["g"] += r["genomes"]; t["b"] += 1
        if r["T3e"] > t["e"]: t["e"] = r["T3e"]; t["ae"] = (r, r["arge"])
        if r["T3n"] > t["n"]: t["n"] = r["T3n"]; t["an"] = (r, r["argn"])
    for U in sorted(T):
        t = T[U]
        for mode, (r, inn) in (("elev", t["ae"]), ("noelev", t["an"])):
            G = gen36.make(N, r["lev"], r["D"], r["xts"], *inn)
            json.dump(G, open(os.path.join(H, "out", "argmax", f"T3_N{N}M{M}_U{U}_{mode}.json"), "w"), sort_keys=True)
        print(f"| {N}, {M} | {N + M} | {U} | {t['g']:,} | {t['b']} | {t['e']} | {t['n']} |")
