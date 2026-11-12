#!/usr/bin/env python3
"""L-RED 65 R231 item 0: mover x0's play at every state (own engine): movers visited and top-block bits hit (e-vertices with bit
label), up to Lambda. Also lists every 'nesting edge': a segment of a play from a high-bit e-vertex to the next high-bit e-vertex,
given as the movers on it. Usage: blkplay231.py G.json x0 [lowbits]"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
G = json.load(open(sys.argv[1])); x0 = int(sys.argv[2]); lowb = int(sys.argv[3]) if len(sys.argv) > 3 else 2
out, V, O, own_ = own.run(G, 20000); n, prio, ow, succ, _, _ = own.build(G); N = G["N"]; M = len(O)
ev = sorted((V[("e", q)] for q in O), key=lambda v: prio[v]); pos = {v: i for i, v in enumerate(ev)}
tl = max(G["lev"]); b = sum(1 for q in O if G["lev"][q[0]] == tl); p0 = M - b
name = {v: k for k, v in V.items()}
nest = {}
for t, (s, vals, tau) in enumerate(out):
    nxt = [None] * n
    for v in range(n):
        nxt[v] = (s[v] if v < N else succ[v][0]) if ow[v] == 0 else tau[v]
    u = x0; seen = set(); walk = []
    while u not in seen:
        seen.add(u); k = name[u]
        if isinstance(k, tuple) and k[0] == "x": walk.append(f"x{k[1]}")
        elif isinstance(k, tuple) and k[0] == "e" and pos[u] >= p0: walk.append(f"[B{pos[u] - p0}]")
        u = nxt[u]
    walk.append(f"->{name[u] if not (isinstance(name[u], tuple) and name[u][0] == 'x') else 'x%d' % name[u][1]}")
    print(f"t {t}: " + " ".join(walk))
    hb = [i for i, w in enumerate(walk) if w.startswith("[B") and int(w[2:-1]) >= lowb]
    for i, j in zip(hb, hb[1:]):
        key = (walk[i], tuple(w for w in walk[i + 1:j] if w.startswith("x")), walk[j]); nest.setdefault(key, []).append(t)
print("nesting segments high-bit -> high-bit (movers between):")
for k, ts in nest.items(): print(" ", k, "states", ts)
