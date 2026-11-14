#!/usr/bin/env python3
"""Box 192: value-count data under E-DOM (every e above every beta). Per run and vertex v: D(v) = distinct values of Omega_t(v);
D_E(v) = distinct (cycle node, e-part of Pi) pairs; IN(v) = max number of value changes of v inside one maximal stretch with
(cycle node, e-part) constant. Prints max over movers and over all vertices. Usage: dv192.py FILES.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import rpot192

def analyse(G):
    h, E, V, name, movers, ev = rpot192.states(G)
    ES = 0
    for v in range(h.n):
        if name[v][0] == "e": ES |= 1 << E.rank[v]
    res = {}
    for v in range(h.n):
        vals = [ev[t][0][v] for t in range(len(ev))]
        D = len(set(vals)); DE = len({(x[0], x[1] & ES) for x in vals})
        inner = best = 0
        for t in range(1, len(vals)):
            if (vals[t][0], vals[t][1] & ES) != (vals[t - 1][0], vals[t - 1][1] & ES): inner = 0
            elif vals[t] != vals[t - 1]: inner += 1; best = max(best, inner)
        res[v] = (D, DE, best)
    mv = [res[x] for x in movers]
    return len(ev) - 1, max(r[0] for r in mv), max(r[1] for r in mv), max(r[2] for r in res.values())

if __name__ == "__main__":
    for f in sys.argv[1:]:
        T, D, DE, IN = analyse(json.load(open(f)))
        print(f"{os.path.basename(f)} T {T} max mover D {D} max mover D_E {DE} max inner changes (e-part fixed, any vertex) {IN}")
