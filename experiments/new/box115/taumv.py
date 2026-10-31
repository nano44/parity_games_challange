#!/usr/bin/env python3
"""L-NEW box 116: list N5's tau-moves (S4b) on one game: transition k, the Odd vertices that move (label old->new), |Itau_k|, whether
Isigma_k is empty, and the fallback flag. Usage: taumv.py G.pg [START]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box21"))
from n5x import load, step, start_pair, readstart, Engine, dual
g = load(sys.argv[1]); st = readstart(sys.argv[2]) if len(sys.argv) > 2 else None; n = g.n; own = g.owner
lab = [l.split('"')[1] if '"' in l else str(i) for i, l in enumerate([l for l in open(sys.argv[1]) if l.strip() and l.strip()[0].isdigit()])]
E, Ed = Engine(g), Engine(dual(g)); s, t = start_pair(g, E, Ed, st); k = 0
while True:
    r = step(g, E, Ed, list(s), list(t))
    if r is None: break
    ns, nt, Is, It, fb, _, _ = r
    if nt != t: print(f"k {k} |Is| {len(Is)} |It| {len(It)} fb {fb} moves " + " ".join(f"{lab[o]}:{lab[t[o]]}->{lab[nt[o]]}" for o in range(n) if nt[o] != t[o]))
    s, t = ns, nt; k += 1
print("iters", k)
