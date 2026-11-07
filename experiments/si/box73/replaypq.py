#!/usr/bin/env python3
"""L-SI box 73: independent replay of a pq witness (genome JSON with "pq_witness") with L-NEW's box 150 Gen (read-only copy in box64/ref):
b-run from the start for flip_after steps (each step must move), then the (1-b)-run to its end. Prints pre, post, total and the states;
exit 1 if the replay disagrees with the stored total. Usage: replaypq.py genome.json"""
import sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64")); from flipdp import Ext
f = os.path.join(HERE, "..", "box64", "ref", "box150", "check.py")
ns = {"__file__": f}; exec(open(f).read().split("\nif __name__")[0], ns); Gen, restrict = ns["Gen"], ns["restrict"]
G = json.load(open(sys.argv[1])); W = G["pq_witness"]; E = Ext(G)
def gstep(u, b):
    sa = E.full(u, b); H = restrict(G, E.L0, sa); S, _ = Gen(H).run(H["start"])
    return tuple(S[1][v] for v in E.UP) if len(S) > 1 else u
u = tuple(W["start_up"]); b = W["bit"]; seq = [u]
for t in range(W["flip_after"]):
    n = gstep(seq[-1], b); assert n != seq[-1], "pre segment stops early"; seq.append(n)
post = 0
while True:
    n = gstep(seq[-1], 1 - b)
    if n == seq[-1]: break
    seq.append(n); post += 1
tot = W["flip_after"] + post
print("pre", W["flip_after"], "post", post, "total", tot, "stored", W["total"], "states", ["".join(map(str, x)) for x in seq])
sys.exit(0 if tot == W["total"] else 1)
