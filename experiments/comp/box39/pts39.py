#!/usr/bin/env python3
"""L-COMP box 39 item 3 input: Q_(>1) (depth39, scope all, one IDEAL-CYC run) and k (own36.kfvs) on every frozen BOX 37 / BOX 38 climb
best (box37/out/climb37/BEST_*.json, box38/out/climb38/BEST_*.json). Resumable: genomes already in OUT are skipped.
Usage: pts39.py OUT"""
import sys, os, json, glob, hashlib
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box36")]
import depth39, own36
OUT = sys.argv[1]; done = set()
if os.path.exists(OUT): done = {json.loads(l)["file"] for l in open(OUT)}
fs = sorted(glob.glob(os.path.join(H, "..", "box37/out/climb37/BEST_*.json")) + glob.glob(os.path.join(H, "..", "box38/out/climb38/BEST_*.json")))
for f in fs:
    b = os.path.basename(f)
    if b in done: continue
    G = json.load(open(f)); r = depth39.measure(G); r.pop("hist")
    rec = dict(file=b, box=37 if "climb37" in f else 38, sha1=hashlib.sha1(open(f, "rb").read()).hexdigest(), NM=G["N"] + sum(map(len, G["opts"])),
               k=own36.kfvs(G, 1), **r)
    with open(OUT, "a") as o: o.write(json.dumps(rec) + "\n")
print("DONE", len(fs))
