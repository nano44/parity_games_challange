#!/usr/bin/env python3
"""L-COMP box 45 item (a): deep45.census on random genomes by this lane's law (box43/rand43.rgen: N + M <= NMMAX, Ξ-target X with
probability PX, else a uniform mover). One line per genome appended to OUT; resumable (the generator is replayed, finished names skipped).
Usage: rand45.py SEED COUNT NMMAX PX OUT   (env CMAX as deep45)"""
import sys, os, json, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "box43")]
import deep45, rand43
seed, cnt, nm, px, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
have = {l.split()[0] for l in open(out)} if os.path.exists(out) else set(); r = random.Random(seed)
for i in range(cnt):
    G = rand43.rgen(r, nm, px); name = "rand_s%d_nm%d_px%s_%d" % (seed, nm, sys.argv[4], i)
    if name in have: continue
    try: c = deep45.census(G)
    except Exception as e: c = {"ERROR": "%s %s" % (type(e).__name__, e)}
    with open(out, "a") as f: f.write("%s N+M %d C %d %s\n" % (name, G["N"] + sum(map(len, G["opts"])), deep45.CMAX, json.dumps(c)))
