#!/usr/bin/env python3
"""L-RED R189 TRACE: per IDEAL step and mover: current option, available set (A), Xi chain of each face (beta ids, rank:parity), keys."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "..", "r187"), os.path.join(H, "..", "..", "r178")]
import ideal, fastcyc
G = json.load(open(sys.argv[1])); S, why = ideal.traj(G); N = G["N"]; lev = G["lev"]; O = G["opts"]
def chain(s, v, k):
    out = []; x, kk = v, k
    while True:
        b = O[x][kk][2]; out.append(f"{x}.{kk}:{G['br'][b]}{'e' if G['bp'][b] == 0 else 'o'}"); xt = O[x][kk][1]
        if xt < 0: return out
        x, kk = xt, s[xt]
def keys(s):
    key = [None] * N
    for v in sorted(range(N), key=lambda v: lev[v]):
        wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
    return key
for j in range(len(S)):
    s = S[j]; val, idx, _, _ = fastcyc.values(G, list(s)); K = keys(s)
    print(f"== state {j}" + (f" (moved {[v for v in range(N) if S[j][v] != S[j-1][v]]})" if j else ""))
    for v in range(N):
        A = [k for k in range(len(O[v])) if k == s[v] or val(N + idx[(v, k)]) > val(N + idx[(v, s[v])])]
        print(f"  m{v} L{lev[v]} on {s[v]} key {K[v]} A {A} " + " | ".join(f"f{k}(wt {O[v][k][0]}): " + ",".join(chain(s, v, k)) for k in range(len(O[v]))))
