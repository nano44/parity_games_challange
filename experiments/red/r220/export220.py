#!/usr/bin/env python3
"""L-RED 55 R220: write own.py's IDEAL-CYC arena of a genome (with env EORD) as a PGSolver .pg (frozen edges as single successors), and
print one witness play: the first (t, v) whose seq has more ascents than U(G). Usage: EORD=rev export220.py G.json OUT.pg"""
import sys, json, os
import own
G = json.load(open(sys.argv[1])); n, prio, ow, succ, V, O = own.build(G); N = G["N"]
open(sys.argv[2], "w").write(f"parity {n - 1};\n" + "".join(f"{v} {prio[v]} {ow[v]} {','.join(map(str, succ[v]))};\n" for v in range(n)))
lev = G["lev"]; U = sum(1 for x in range(N) for o in G["opts"][x] if o[1] >= 0 and lev[o[1]] > lev[x])
out, V2, O2, _ = own.run(G); rk = own.VJ(prio).rk; evs = {V[("e", q)]: q for q in O}
for t, (s, vals, tau) in enumerate(out):
    nxt = lambda v: (s[v] if v < N else (tau[v] if ow[v] == 1 else succ[v][0]))
    for v in range(n):
        seq, seen, u = [], set(), v
        while u not in seen:
            seen.add(u)
            if u in evs and u in vals[v][1]: seq.append(u)
            u = nxt(u)
        a = sum(1 for p, q in zip(seq, seq[1:]) if rk[q] > rk[p])
        if a > U:
            print(f"U(G) {U}; witness t {t} v {v}: seq (e-vertex: option (mover, k), mover level, priority) " + " ".join(f"{evs[e]}/lev{lev[evs[e][0]]}/pr{prio[e]}" for e in seq) + f"; ascents {a}")
            sys.exit(0)
