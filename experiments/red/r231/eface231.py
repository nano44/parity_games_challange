#!/usr/bin/env python3
"""L-RED 65 R231 item (a): Addendum D obstruction check on L-RED's own engine. For each high-bit mover qh_k (names file) and its option j:
number of states at which Odd's sigma-bar at the gate takes the e-face (tau(g) = e_g), and whether Gamma has, under the state's strategy
pair, a cycle through e_(qh_k, j) (the play from e_g returns to e_g).  Usage: eface231.py G.json NAMES.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[2])); N = G["N"]
out, V, O, ow = own.run(G, 20000); n, prio, _, succ, _, _ = own.build(G)
qh = sorted((int(k[2:]), v) for k, v in nm.items() if k.startswith("qh") and k[2:].isdigit())
for k, x in qh:
    for j in range(len(G["opts"][x])):
        g, e = V[("g", (x, j))], V[("e", (x, j))]; eon = 0; cyc = 0
        for s, vals, tau in out:
            eon += tau[g] == e
            nxt = lambda u: (s[u] if u < N else succ[u][0]) if ow[u] == 0 else tau[u]
            u = succ[e][0]; seen = set()
            while u not in seen and u != e: seen.add(u); u = nxt(u) if u != g else e
            cyc += u == e
        print(f"qh{k} (mover {x}, opt {j}): e-face states {eon} / {len(out)}; states with a play e_g -> ... -> e_g (gate forced to e) {cyc}")
