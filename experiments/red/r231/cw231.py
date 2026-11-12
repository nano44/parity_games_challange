#!/usr/bin/env python3
"""L-RED 65 R231 item 1b: INDEPENDENT measure of L-NEW 70's CW(n) (box 206 Addendum C, l-new f7b8bb66) on L-RED's own engine
(r221q/own.py via blk231.analyse; no L-NEW code). Prints k, N + M, b, Dtop, D_mov, T, and max ascents over all plays of all vertices
(seq_t(v) = e-vertices of Pi_t(v) in play order; ascent = next element more relevant, RESULTS R121 (a)), max loud depth (dep231).
Usage: cw231.py G.json ..."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "r221q"))
import own
from blk231 import analyse, xi_k
from dep231 import measure, MUST0
for f in sys.argv[1:]:
    G = json.load(open(f)); A = analyse(G); N = G["N"]; M = A["M"]
    out, V, O, ow = own.run(G, 20000); n, prio, _, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    asc = 0
    for s, vals, tau in out:
        nxt = [(s[v] if v < N else succ[v][0]) if ow[v] == 0 else tau[v] for v in range(n)]
        for v in range(n):
            lam, Pi, _ = vals[v]; u = v; seq = []; seen = set()
            while u != lam and u not in seen:
                seen.add(u)
                if u in evs and u in Pi: seq.append(u)
                u = nxt[u]
            asc = max(asc, sum(1 for a, b in zip(seq, seq[1:]) if rk[b] > rk[a]))
    c = measure(G); f0 = sum(c[k] for k in MUST0)
    print(f"{os.path.basename(f)} k {xi_k(G)} N {N} M {M} N+M {N + M} b {A['b']} Dtop {max(len(set(A['blk'][x])) for x in range(N))} "
          f"D_mov {max(len(set(A['cls'][x])) for x in range(N))} T {A['T']} maxasc {asc} maxloud {max(c['hist'])} must0 {f0}", flush=True)
