#!/usr/bin/env python3
"""L-COMP box 34 (b'): frontier table = for each target (C t, m t), the minimum N + M over every FINAL line in out/frontier/log/*.txt, and
monotone closure (a genome with C >= t+1 also has C >= t, so best(t) := min over t' >= t). Prints target, N + M, N, M, T3, C, maxm, file,
chain; --files prints just the frontier files (one per target)."""
import sys, os, glob, re, ast
H = os.path.dirname(os.path.abspath(__file__))
rows = []
for f in glob.glob(os.path.join(H, "out/frontier/log/*.txt")):
    for l in open(f):
        if not l.startswith("FINAL"): continue
        mt = re.match(r"FINAL (\S+) N (\d+) M (\d+) N\+M (\d+) measure (\{.*\}) frozen (\S+)", l.strip())
        key, N, M, NM, meas, fn = mt.groups(); m = ast.literal_eval(meas)
        rows.append(dict(key=key, N=int(N), M=int(M), NM=int(NM), m=m, fn=fn, chain=os.path.basename(f)))
out = {}
for kind, field in (("C", "C"), ("m", "maxm")):
    vals = sorted({r["m"][field] for r in rows})
    for t in range(2, max(vals) + 1):
        cand = [r for r in rows if r["m"][field] >= t and r["m"]["fallback"]]
        if cand: out[f"{kind}{t}"] = min(cand, key=lambda r: (r["NM"], r["fn"]))
if "--files" in sys.argv:
    for k, r in out.items(): print(k, r["fn"])
else:
    for k, r in sorted(out.items(), key=lambda kv: (kv[0][0], int(kv[0][1:]))):
        print(f"{k:4} N+M {r['NM']:4} N {r['N']:3} M {r['M']:3} T3 {r['m']['T3']:3} C {r['m']['C']:2} maxm {r['m']['maxm']} A {r['m']['maxalt']:2} {os.path.basename(r['fn'])} ({r['chain']})")
