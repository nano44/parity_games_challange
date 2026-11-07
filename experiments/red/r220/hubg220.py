#!/usr/bin/env python3
"""L-RED 55 R220: P-N5-ASC §5 HUB-ASC-G check with own.py: for every vertex v and maximal interval I with Lambda(v) fixed (= w), with
B := max ascents of seq_t(v) on I and M_w := #e-vertices more relevant than w: D_E,I(v) <= F'_B(M_w)? Env EORD as in asc220.py.
Prints max D_E, the max ratio D_E / F'_B, violations. Usage: [EORD=rev] hubg220.py G.json ..."""
import sys, json, os
import own
def Fp(B, M):
    F = 1 + M * (M + 1) // 2
    for _ in range(B): F = (M * M + 3 * M + 1) * (1 + M * F * F)
    return F
for f in sys.argv[1:]:
    G = json.load(open(f))
    if not (isinstance(G, dict) and "opts" in G): continue
    N = G["N"]; out, V, O, ow = own.run(G); n, prio, o_, succ, _, _ = own.build(G); rk = own.VJ(prio).rk; evs = {V[("e", q)] for q in O}
    rows = []
    for t, (s, vals, tau) in enumerate(out):
        nxt = lambda v: (s[v] if v < N else (tau[v] if o_[v] == 1 else succ[v][0])); r = []
        for v in range(n):
            Pi = vals[v][1]; seq = []; seen = set(); u = v
            while u not in seen:
                seen.add(u)
                if u in evs and u in Pi: seq.append(u)
                u = nxt(u)
            r.append((vals[v][0], frozenset(seq), sum(1 for p, q in zip(seq, seq[1:]) if rk[q] > rk[p])))
        rows.append(r)
    viol = 0; mxD = 0; mxr = 0.0
    for v in range(n):
        t = 0
        while t < len(rows):
            u = t
            while u + 1 < len(rows) and rows[u + 1][v][0] == rows[t][v][0]: u += 1
            w = rows[t][v][0]; Mw = sum(1 for e in evs if rk[e] > rk[w])
            D = len({rows[i][v][1] for i in range(t, u + 1)}); B = max(rows[i][v][2] for i in range(t, u + 1))
            mxD = max(mxD, D); mxr = max(mxr, D / Fp(B, Mw)); viol += D > Fp(B, Mw); t = u + 1
    print(f"{f.split('/')[-1]} EORD {os.environ.get('EORD', 'lev')} max D_E {mxD} max D_E/F'_B {mxr:.3f} violations {viol}", flush=True)
