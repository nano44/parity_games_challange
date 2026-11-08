#!/usr/bin/env python3
"""L-RED 59 R225: print the (Lambda, Low | High) sequence of the max-excess hub of a genome (comp225.comp's best). Usage: show225.py G.json"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r221")]
import own, comp225
G = json.load(open(sys.argv[1])); N = G['N']
out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; inv = {v: k for k, v in V.items()}
evs = {V[("e", q)] for q in O}
lab = lambda e: "e%d.%d(L%d)" % (inv[e][1][0], inv[e][1][1], G['lev'][inv[e][1][0]])
c = comp225.comp(G); print(c); v = c['best']['vid']; print("hub", inv.get(v, ("x", v)))
for t, (s, vals, tau) in enumerate(out):
    nxt = lambda u: (s[u] if u < N else (tau[u] if o_[u] == 1 else succ[u][0]))
    seq = []; seen = set(); u = v
    while u not in seen:
        seen.add(u)
        if u in evs and u in vals[v][1]: seq.append(u)
        u = nxt(u)
    a = next((i + 1 for i in range(len(seq) - 1) if rk[seq[i + 1]] > rk[seq[i]]), len(seq))
    print(t, inv.get(vals[v][0]), [lab(e) for e in seq[:a]], '|', [lab(e) for e in seq[a:]])
