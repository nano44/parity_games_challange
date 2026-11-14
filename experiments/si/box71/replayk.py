#!/usr/bin/env python3
"""L-SI box 71: independent replay of a k-flip optimum with L-NEW's box 150 Gen (level 0 restricted per bit): DP over (state, bit, flips
left) using Gen steps only; prints the best length, its start, bit sequence and number of bit changes. Usage: replayk.py genome.json k (-1 = unlimited)"""
import sys, json, itertools
from functools import lru_cache
sys.path.insert(0, '../box64'); from flipdp import Ext
ns = {"__file__": "../box64/ref/box150/check.py"}; exec(open(ns["__file__"]).read().split("\nif __name__")[0], ns); Gen, restrict = ns["Gen"], ns["restrict"]
G = json.load(open(sys.argv[1])); k = int(sys.argv[2]); E = Ext(G); K = k if k >= 0 else 64
@lru_cache(None)
def gstep(u, b):
    sa = E.full(u, b); H = restrict(G, E.L0, sa); S, _ = Gen(H).run(H["start"])
    return tuple(S[1][v] for v in E.UP) if len(S) > 1 else u
@lru_cache(None)
def V(u, b, r):
    w = gstep(u, b); best = (1 + V(w, b, r)[0], b) if w != u else (0, None)
    if r > 0:
        alt = V(u, 1 - b, r - 1)
        if alt[0] > best[0]: best = (alt[0], ('flip', 1 - b))
    return best
states = list(itertools.product(*[range(2) for _ in E.UP]))
u0, b0 = max(((u, b) for u in states for b in (0, 1)), key=lambda x: V(x[0], x[1], K)[0])
u, b, r, seq = u0, b0, K, []
while True:
    val, act = V(u, b, r)
    if act is None: break
    if act[0] == 'flip' if isinstance(act, tuple) else False: b, r = act[1], r - 1; continue
    seq.append(b); u = gstep(u, b)
print("Gen replay k", k, "length", len(seq), "start", u0, "bits", "".join(map(str, seq)), "changes", sum(1 for i in range(1, len(seq)) if seq[i] != seq[i - 1]))
