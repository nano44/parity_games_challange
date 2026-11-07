#!/usr/bin/env python3
"""L-RED 54 R217: compile switchallexp G_n with E-DOM priorities from an edomclimb state (order/par JSON) and compare Howard T on the
modified ORIGINAL game with Howard on IDEAL-CYC of the compiled genome (box191 idealcyc), plus own.py. Usage: edomcomp.py n state.json OUT.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.environ["WT3"], "experiments/new/box191"))
import idealcyc, fried, comp, own
n, sf, out = int(sys.argv[1]), sys.argv[2], sys.argv[3]
from edomprio import apply
d = json.load(open(sf)); V0 = fried.game(n); V = apply(V0, d["order"], d["par"])
T, _ = fried.howard(V)
fried.game = lambda m: V; comp.game = lambda m: V
G, ix = comp.compile_(n); json.dump(G, open(out, "w"))
st = idealcyc.run(G); o, *_ = own.run(G)
print(f"E-DOM G_{n} ({os.path.basename(sf)}): Howard on original T {T} | genome N {G['N']} idealcyc T {len(st) - 1} own T {len(o) - 1}")
