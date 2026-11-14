#!/usr/bin/env python3
"""Box 197 (L-NEW successor 65): print the e-set sequence (as bit words over its active e-vertices, most relevant first) of the (v, Lambda-interval)
with the most distinct e-sets on one genome. Usage: dump197.py G.json [TOP]"""
import sys, os, json
ROOT = os.environ.get("ROOT") or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")); os.environ.setdefault("EG195_ROOT", ROOT)
sys.path[:0] = [os.path.join(ROOT, p) for p in ("experiments/new/box195", "experiments/new/box191", "experiments/new/box189",
                "experiments/new/box190", "experiments/new/box21", "experiments/new", "experiments/si", "experiments/harness")]
import eg195, gamma3, n5v, n5x
G = json.load(open(sys.argv[1])); G = G.get("genome", G); TOP = int(sys.argv[2]) if len(sys.argv) > 2 else 3
g0, _, _, V = gamma3.build(G, eg195.PADS); g = eg195.topg(g0); n = g.n; name = {v: k for k, v in V.items()}
E, Ed = n5v.Engine(g), n5v.Engine(n5v.dual(g)); sigma, tau = n5x.start_pair(g, E, Ed, None)
evs = [v for v in range(n) if isinstance(name[v], tuple) and name[v][0] == "e"]; ES = sum(E.bit[v] for v in evs)
hist = []
while True:
    vs, sb = E.evaluate(tuple(sigma)); hist.append(vs)
    res = n5v.step(g, E, Ed, sigma, tau, "xi")
    if res is None or res[4]: break
    sigma, tau = res[0], res[1]
rows = []
for v in range(n):
    t = 0
    while t < len(hist):
        s = t
        while t + 1 < len(hist) and hist[t + 1][v][0] == hist[s][v][0]: t += 1
        seq = []
        for u in range(s, t + 1):
            x = hist[u][v][1] & ES
            if not seq or seq[-1][1] != x: seq.append((u, x))
        rows.append((len(seq), v, s, t, seq)); t += 1
rows.sort(key=lambda r: -r[0])
for D, v, s, t, seq in rows[:TOP]:
    act = sorted({f for _, x in seq for f in evs if x & E.bit[f]}, key=lambda f: -E.rank[f])
    print(f"vertex {name[v]} states {s}-{t} D {D} items (most relevant first) {[ (name[f][1], G['lev'][name[f][1][0]]) for f in act]}")
    for u, x in seq: print(f"  t {u:3d} " + "".join("1" if x & E.bit[f] else "." for f in act))
