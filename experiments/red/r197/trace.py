#!/usr/bin/env python3
"""L-RED R197 TRACE: print an IDEAL run step by step: movers (name level:u/v, old->new option), carries (levels whose ranking R_l
flipped), and for each LAG move its wakers. Usage: trace.py genome.json"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [H, os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal
G = json.load(open(sys.argv[1])); N = G["N"]; O = G["opts"]; lev = G["lev"]; d = max(lev) + 1
S, why = ideal.traj(G, cap=20000)
nm = lambda v: f"{'uv'[v % 2]}{lev[v]}"
print("Xi:", " ".join(f"{nm(v)}:[" + ",".join(nm(o[1]) if o[1] >= 0 else "X" for o in O[v]) + "]" for v in range(N)), "pi", G.get("pi", G.get("xorder")))
def keys(s):
    key = [None] * N
    for v in sorted(range(N), key=lambda v: lev[v]):
        wt = O[v][s[v]][0]; key[v] = ((G["gate"][v][s[v]],) if wt < 0 else key[wt] + (G["gate"][v][s[v]],))
    return key
K = [keys(s) for s in S]
R = [[tuple(sorted((2 * l, 2 * l + 1), key=lambda v: k[v])) for l in range(d)] for k in K]
desc = []
for v in range(N):
    seen = set(); st = [v]
    while st:
        x = st.pop()
        for (_, xt, _) in O[x]:
            if xt >= 0 and xt not in seen: seen.add(xt); st.append(xt)
    desc.append(seen)
def korder(t, x): return tuple(sorted(range(len(O[x])), key=lambda k: (G["gate"][x][k],) if O[x][k][0] < 0 else K[t][O[x][k][0]] + (G["gate"][x][k],)))
mv = [set()] + [{v for v in range(N) if S[t][v] != S[t - 1][v]} for t in range(1, len(S))]
print("start", S[0])
for t in range(1, len(S)):
    car = [l for l in range(d) if R[t][l] != R[t - 1][l]]; out = []
    for v in sorted(mv[t], key=lambda v: lev[v]):
        s = f"{nm(v)} {S[t-1][v]}->{S[t][v]}"
        if t >= 2 and v not in mv[t - 1] and korder(t - 1, v) == korder(t, v): s += " LAG<" + ",".join(nm(y) for y in mv[t - 1] & desc[v]) + ">"
        out.append(s)
    print(f"t{t}: carries {car} | " + "; ".join(out))
print("end", why, "L", len(S) - 1)
