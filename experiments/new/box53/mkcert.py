#!/usr/bin/env python3
"""L-NEW box 53: write compact certificates (for cert.py) from a uni1 result file: one per infeasible game, the LIST file supplying starts.
Usage: mkcert.py RESULT.json LIST FAM OUTDIR [MAXN]"""
import sys, os, json
R = json.load(open(sys.argv[1]))   # a uni1 result from experiments/new/out/box53/; L = {l.split()[0]: (l.split()[1] if len(l.split()) > 1 else None) for l in open(sys.argv[2]) if l.split()}
fam = int(sys.argv[3]); out = sys.argv[4]; os.makedirs(out, exist_ok=True); maxn = int(sys.argv[5]) if len(sys.argv) > 5 else 10 ** 9
pre = lambda q: q if q.startswith("experiments/") or q.startswith("../") is False and os.path.exists(q) else "experiments/" + q
for r in R:
    if r["result"] != "INFEASIBLE" or not r.get("exact") or r["n"] > maxn: continue
    g = r["name"]; st = L.get(g)
    norm = lambda q: os.path.normpath(os.path.join("experiments", q)) if not q.startswith("experiments/") else q
    C = dict(game=norm(g), start=norm(st) if st else None, fam=fam, y=[[t, y] for _, t, y in r["y"]])
    fn = os.path.join(out, "f%d_%s.json" % (fam, os.path.basename(g)[:-3])); json.dump(C, open(fn, "w")); print(fn)
