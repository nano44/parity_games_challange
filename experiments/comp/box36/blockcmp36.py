#!/usr/bin/env python3
"""L-COMP box 36: exhaustive aggregate check. For every k >= 1 block of a Python (ENGINE=py, own36) sweep checkpoint OUT.ck, re-run the
block with the C engine (fast36 block mode) and compare the whole block-stats dict (genomes, maxratio + argmax genome/gate, maxkfx +
argmax, maxflip, maxT3, c2fail, hist). Usage: blockcmp36.py N M CKFILE"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fast36
N, M, ck = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; nb = ng = bad = 0
for line in open(ck):
    d = json.loads(line)
    if d["k"] == 0: continue
    c = fast36.run_block(N, d["lev"], d["D"], d["xts"], M)
    p = json.loads(json.dumps(d["st"]))
    nb += 1; ng += p["genomes"]
    if json.loads(json.dumps(c, sort_keys=True)) != json.loads(json.dumps(p, sort_keys=True)):
        bad += 1
        if bad <= 3: print("BLOCK MISMATCH", d["i"], "\n py", json.dumps(p, sort_keys=True)[:600], "\n c ", json.dumps(c, sort_keys=True)[:600])
print("blockcmp36", N, M, "blocks", nb, "genomes", ng, "mismatching blocks", bad)
