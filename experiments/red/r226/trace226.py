#!/usr/bin/env python3
"""L-RED 60 R226: per-step trace of a genome under own.py (IDEAL-CYC Howard): chosen option per mover x, and Odd's face (e/b) per chosen gate.
Usage: trace226.py G.json"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own
G = json.load(open(sys.argv[1])); N = G['N']
out, V, O, ow = own.run(G); inv = {v: k for k, v in V.items()}
print("T", len(out) - 1)
for x in range(N): print("x%d L%d opts" % (x, G['lev'][x]), [tuple(o) for o in G['opts'][x]], "gate", G['gate'][x])
for t, (s, vals, tau) in enumerate(out):
    row = []
    for x in range(N):
        q = inv[s[x]][1]; g = s[x]; f = 'e' if tau[g] == V[("e", q)] else 'b'
        row.append("%d%s" % (q[1], f))
    print("%2d" % t, " ".join("x%d:%s" % (x, r) for x, r in enumerate(row)))
