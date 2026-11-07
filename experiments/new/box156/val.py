#!/usr/bin/env python3
"""box 156: re-simulate witness genomes with the box 150 simulator (independent of the z3 encoding); print T, M2, U and |Mv_t|."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, "..", "box150", "check.py")
ns = {"__file__": os.path.abspath(P), "__name__": "lib"}; src = open(P).read(); exec(src.split("if __name__")[0], ns)
def stats(G, start=None):
    g = ns["Gen"](G); S, _ = g.run(G["start"] if start is None else start); T = len(S) - 1
    mv = [sum(1 for v in range(g.N) if S[t][v] != S[t + 1][v]) for t in range(T)]
    U = ns["labels"](g, S)[2]
    return T, sum(1 for c in mv[:-1] if c >= 2), U, mv  # M2 over steps 1..T-1 (MULTI-CHARGE)
if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); T, M2, U, mv = stats(G); print(f, "N", G["N"], "T", T, "M2", M2, "U", U, "mv", mv)
