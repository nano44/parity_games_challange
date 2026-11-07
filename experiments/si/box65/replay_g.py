#!/usr/bin/env python3
"""L-SI box 65: independent replay of a one-flip gain witness with L-NEW's box 150 Gen (read-only copy, ../box64/ref):
L_b(u) = Gen run of the genome with level 0 restricted to a configuration of bit b (box 64 flipdp.Ext.q only picks that configuration).
Prints M(u) = max_b L_b(u), the b-run from u, and t + L_(1-b)(s_t) for every t; gain = max - M(u).  Usage: replay_g.py genome.json u b"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box64"))
from flipdp import Ext
ns = {"__file__": os.path.join(HERE, "..", "box64", "ref", "box150", "check.py")}
exec(open(ns["__file__"]).read().split("\nif __name__")[0], ns); Gen, restrict = ns["Gen"], ns["restrict"]
G = json.load(open(sys.argv[1])); u = tuple(json.loads(sys.argv[2])); b = int(sys.argv[3]); E = Ext(G)
def run(u, b):
    sa = E.full(u, b); H = restrict(G, E.L0, sa); S, _ = Gen(H).run(H["start"]); return [tuple(st[v] for v in E.UP) for st in S]
M = max(len(run(u, 0)) - 1, len(run(u, 1)) - 1); seq = run(u, b)
vals = [t + len(run(st, 1 - b)) - 1 for t, st in enumerate(seq)]
print("M", M, "b-run length", len(seq) - 1, "t + L_(1-b)(s_t):", vals, "gain", max(vals) - M)
