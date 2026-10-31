#!/usr/bin/env python3
"""L-SI (P-N5-ODD fixes entry 4, D-ODD-1 / F-1): reject a start pair that uses a non-edge or a vertex of the wrong owner.
n5x.start_pair (L-NEW box 21) applies start entries unchecked; every L-SI tool that reads a start calls check_start first.
As a script: startcheck.py GAME.pg START [GAME.pg START ...] -> 'START OK' or 'START BAD <file> <v>:<w> ...' per pair (exit 1 if any bad)."""
import sys

def bad_entries(g, st):
    """st = (sigma0 dict, tau0 dict) as n5x.readstart returns it. Returns [(v, w, why)]."""
    out = []
    if not st: return out
    for side, d in (("SIGMA0", st[0]), ("TAU0", st[1])):
        for v, w in d.items():
            if not 0 <= v < g.n: out.append((v, w, side + " vertex out of range")); continue
            if g.owner[v] != (0 if side == "SIGMA0" else 1): out.append((v, w, side + " wrong owner"))
            if w not in g.succ[v]: out.append((v, w, side + " non-edge"))
    return out

def check_start(g, st, path="start"):
    b = bad_entries(g, st)
    if b: raise SystemExit(f"START BAD {path}: " + " ".join(f"{v}:{w} ({why})" for v, w, why in b))

if __name__ == "__main__":
    import os
    HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "new", "box21"))
    from n5x import load, readstart
    bad = 0
    for gp, sp in zip(sys.argv[1::2], sys.argv[2::2]):
        b = bad_entries(load(gp), readstart(sp))
        print(f"START {'BAD' if b else 'OK'} {sp}" + "".join(f" {v}:{w}({why})" for v, w, why in b)); bad += bool(b)
    sys.exit(1 if bad else 0)
