#!/usr/bin/env python3
"""L-RED successor 23: XR per vertex per phase (docs/si/N5-ALT-box23.md §0: the number of transitions of a phase at which Xi(z) changes).
For the top vertex prints each change: t, top differing rank of the path set (+ entered / - left, parity), cycle-node change, length change.
Usage: xr.py GAME.pg START|S3 [--top K]"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import trace as T

def main():
    path, st = sys.argv[1], sys.argv[2]
    g = T.pg.parse("".join(l for l in open(path) if not l.lstrip().startswith("%")))
    start = ({}, {}) if st == "S3" else T.readstart(st)
    states = []; T.run(g, start, log=lambda *a: None, states=states)
    E = T.Engine(g); n = g.n
    vals = [E.evaluate(s)[0] for s, _ in states]
    phases = []; a = 0
    for t in range(1, len(states)):
        if states[t][1] != states[t - 1][1]: phases.append((a, t - 1)); a = t
    phases.append((a, len(states) - 1))
    best = (0, None, None)
    for (a, b) in phases:
        for z in range(n):
            xr = sum(1 for t in range(a, b) if vals[t][z] != vals[t + 1][z])
            if xr > best[0]: best = (xr, z, (a, b))
    xr, z, (a, b) = best
    rank_of = {E.rank[v]: v for v in range(n)}
    print("%s n=%d states=%d phases=%s  max XR=%d (%.2fn) at z=%d phase [%d,%d]" % (os.path.basename(path), n, len(states), [(p, q) for p, q in phases], xr, xr / n, z, a, b))
    for t in range(a, b):
        u, w = vals[t][z], vals[t + 1][z]
        if u == w: continue
        if u[0] != w[0]: print("  t=%d cycle node %d -> %d" % (t, u[0], w[0])); continue
        d = u[1] ^ w[1]
        if d:
            r = d.bit_length() - 1; v = rank_of[r]
            print("  t=%d top rank %d (v %d, prio %d %s) %s" % (t, r, v, g.prio[v], "even" if g.prio[v] % 2 == 0 else "odd", "entered" if w[1] >> r & 1 else "left"))
        else: print("  t=%d length %d -> %d" % (t, u[2], w[2]))

if __name__ == "__main__":
    main()
