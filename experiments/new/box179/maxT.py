#!/usr/bin/env python3
"""L-NEW box 179: max run length over ALL starts of one genome (box150 simulator), with the arg-max start. Usage: maxT.py files..."""
import os, sys, json, itertools
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, "..", "box150", "check.py")
ns = {"__file__": P, "__name__": "lib"}; exec(open(P).read().split("\nif __name__")[0], ns); Gen = ns["Gen"]
for f in sys.argv[1:]:
    G = json.load(open(f)); g = Gen(G); best = (-1, None)
    for s in itertools.product((0, 1), repeat=G["N"]):
        S, _ = g.run(s); best = max(best, (len(S) - 1, s))
    print("%s maxT %d at %s" % (os.path.basename(f), best[0], "".join(map(str, best[1]))))
