#!/usr/bin/env python3
"""L-RED R212: locate an L^R_d witness (JSON, with start) in the r200 cube partition (SYM0=1 SYMB=1): apply the R202 symmetries
sigma_l (swap movers 2l, 2l+1; swap the options of the level-(l+1) movers; rename Xi-targets) to reach s_0(2l) >= s_0(2l+1) for l >= 1
and f0 <= f1 at level 0 (first-move times, 0 = never -> L+1); check T is unchanged under r187/ideal.py; print the cube keys
(levels 0, 1, 2) and their status in a state file. Usage: canon.py witness.json L state.json"""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187")]
import ideal
G = json.load(open(sys.argv[1])); L = int(sys.argv[2]); st = json.load(open(sys.argv[3]))
d = max(G["lev"]) + 1
def sigma(G, l):
    H = json.loads(json.dumps(G)); a, b = 2 * l, 2 * l + 1; ren = lambda x: b if x == a else a if x == b else x
    for key in ("opts", "gate"): H[key][a], H[key][b] = G[key][b], G[key][a]
    H["start"][a], H["start"][b] = G["start"][b], G["start"][a]
    for v in range(H["N"]):
        H["opts"][v] = [[o[0], ren(o[1]) if o[1] >= 0 else -1, o[2]] for o in H["opts"][v]]
    if l + 1 < d:
        for v in (2 * l + 2, 2 * l + 3):
            o0, o1 = H["opts"][v]; H["opts"][v] = [[o0[0], o1[1], o1[2]], [o1[0], o0[1], o0[2]]]
            H["gate"][v] = H["gate"][v][::-1]; H["start"][v] = 1 - H["start"][v]
    return H
def first(G):
    S, _ = ideal.traj(G); f = {}
    for v in range(G["N"]):
        ts = [t for t in range(1, len(S)) if S[t][v] != S[t - 1][v]]; f[v] = ts[0] if ts else 0
    return len(S) - 1, f
T0, f = first(G)
inf = lambda x: x if x else L + 1
if inf(f[0]) > inf(f[1]): G = sigma(G, 0)
for l in range(1, d):
    if not G["start"][2 * l] >= G["start"][2 * l + 1]: G = sigma(G, l)
T1, f = first(G)
print("T before", T0, "after", T1, "start", G["start"], "first moves", f)
keys = []
for depth in (1, 2, 3):
    k = ";".join(f"{v}:{f[v]}" for v in range(2 * depth)); keys.append(k)
    print(k, "->", st["done"].get(k, "not done"), "(split)" if k in st["split"] else "")
