#!/usr/bin/env python3
"""Box 192: replay of DEAD SEG-T. Runs N5'-xi (box190 n5v.py mode xi, unmodified) on a general game given as JSON [prio, owner, succ];
prints, per sigma-changing iteration k (DECOMP-G's S): label C / R / p, value monotonicity (all vertices), strictness, switched Even
vertices (v, old, new), whether each switch is improving, Howard-best, and whether v is its own cycle node (H0).
Usage: segt192.py GAME.json"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path[:0] = [os.path.join(ROOT, "experiments/new/box190")]
import n5v
pg = n5v.pg
G = json.load(open(sys.argv[1])); g = pg.Game(*G); n = g.n
st, fb, E = n5v.run(g, "xi")
print("n", n, "nE", sum(1 for v in range(n) if g.owner[v] == 0), "iterations", len(st) - 1, "fallbacks", fb)
sig = [st[0][0]] + [ns for (s, _), (ns, _) in zip(st, st[1:]) if ns != s]
ev = [E.evaluate(tuple(s)) for s in sig]; lab = ""
for k in range(1, len(sig)):
    (pv, ps), (vs, sb) = ev[k - 1], ev[k]
    mono = all(E.key(vs[v]) >= E.key(pv[v]) for v in range(n)); strict = any(E.key(vs[v]) > E.key(pv[v]) for v in range(n))
    C = any(pv[v][0] != vs[v][0] for v in range(n)); R = any(ps[v] != sb[v] for v in range(n) if g.owner[v] == 1)
    sw = [(v, sig[k - 1][v], sig[k][v]) for v in range(n) if g.owner[v] == 0 and sig[k][v] != sig[k - 1][v]]
    imp = all(E.key(pv[b]) > E.key(pv[a]) for v, a, b in sw)
    hb = [E.key(pv[b]) == max(E.key(pv[w]) for w in g.succ[v]) for v, a, b in sw]
    h0 = [pv[v][0] == v for v, a, b in sw]; l = "C" if C else ("R" if R else "p"); lab += l
    print(k, l, "mono", mono, "strict", strict, "switches", sw, "improving", imp, "howard-best", hb, "own-cycle-node", h0)
print("labels", lab, "max p-run", max(len(r) for r in lab.replace("R", "C").split("C")))
