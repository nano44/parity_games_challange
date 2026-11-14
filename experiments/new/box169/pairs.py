#!/usr/bin/env python3
"""all same-level pairs of one genome: flips, |W(reader)|, and the per-step causes of each flip: 'own' (p or q moved at that step),
'below' (neither moved; the order of their current W-targets flipped). Usage: pairs.py file.json [level]"""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(H, "..", "box167", "pmprime.py")).read().split("\nif __name__")[0])
G = json.load(open(sys.argv[1])); g = Gen(G); S, _ = g.run(G["start"]); W = wclos(G); keys = [g.keys(s) for s in S]
levs = [int(sys.argv[2])] if len(sys.argv) > 2 else sorted(set(G["lev"]))
for L in levs:
    ms = [v for v in range(G["N"]) if G["lev"][v] == L]
    for p, q in itertools.combinations(ms, 2):
        own = below = 0
        for t in range(1, len(S)):
            if (keys[t][p] < keys[t][q]) != (keys[t - 1][p] < keys[t - 1][q]):
                if S[t][p] != S[t - 1][p] or S[t][q] != S[t - 1][q]: own += 1
                else: below += 1
        print("level %d pair (%d,%d) flips %2d (own %2d, below %2d) |W(r)| %2d" % (L, p, q, own + below, own, below, len({p, q} | W[p] | W[q])))
