#!/usr/bin/env python3
"""L-RED R207 ALLSTARTS: max run length T over ALL starts of the two-option movers (degree-1 movers have one option) of a genome
(T*(d) is a max over starts too). Prints the best T and start; with OUT=file writes the genome with that start. Usage: allstarts.py g.json"""
import sys, os, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
G = json.load(open(sys.argv[1])); two = [v for v in range(G["N"]) if len(G["opts"][v]) == 2]; best = None; hist = {}
for bits in itertools.product((0, 1), repeat=len(two)):
    s = [0] * G["N"]
    for v, b in zip(two, bits): s[v] = b
    G["start"] = s; T = len(ideal.traj(G)[0]) - 1; hist[T] = hist.get(T, 0) + 1
    if best is None or T > best[0]: best = (T, s)
print(sys.argv[1], "runs", sum(hist.values()), "max T", best[0], "start", best[1], "top T counts", sorted(hist.items())[-4:])
if os.environ.get("OUT"): G["start"] = best[1]; json.dump(G, open(os.environ["OUT"], "w"))
