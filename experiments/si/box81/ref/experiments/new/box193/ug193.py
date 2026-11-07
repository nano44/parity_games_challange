#!/usr/bin/env python3
"""Box 193 (L-NEW successor 61): Corollary UP-B data (doc Addendum 4). U(G) := the number of options (x, k) whose Xi-target is a mover
of level > lev(x) (strictly upward Xi-edges). Prints U(G) and the max ascents over all plays (asc193.py); UP-B needs max <= U(G).
Usage: ug193.py FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import asc193

if __name__ == "__main__":
    for f in sys.argv[1:]:
        G = json.load(open(f)); lev = G["lev"]
        U = sum(1 for x in range(G["N"]) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
        r = asc193.analyse(G)
        print(f"{os.path.basename(f)} U(G) {U} max ascents {r['maxasc']} {'OK' if r['maxasc'] <= U else 'VIOLATION'}")
