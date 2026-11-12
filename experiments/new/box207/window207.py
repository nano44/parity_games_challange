#!/usr/bin/env python3
"""Box 207 (L-NEW successor 71): per-step flip trace against a vertex R on IDEAL-CYC. For every step t with no Lambda change and some gate
flip: whether class(R) changes at t, and per flipping gate (owner, option) + new face, eR / bR = [does the e-face's / beta-face's play reach
R at t-1, at t], gOnRplay = [is the gate on R's play at t-1, at t]. With --class: Lambda(R) and E(R) per state instead.
Usage: window207.py G.json R [--class]"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(HERE, "..", "box203"), os.path.join(HERE, "..", "box191")]
import gfc203, idealcyc
f = sys.argv[1]; G = json.load(open(f)); R = int(sys.argv[2])
H, n, E, V, gates = gfc203.hist_ideal(G); T = len(H) - 1; ST = idealcyc.run(G); h, s0, movers, inv = idealcyc.build(G)
iv = {v: k for k, v in V.items()}
em = 0
for k, v in V.items():
    if isinstance(k, tuple) and k[0] == "e": em |= E.bit[v]
r = V[("x", R)]
def succf(t):
    s = list(s0)
    for x in range(G["N"]): s[movers[x]] = V[("g", (x, ST[t][x]))]
    return lambda v: s[v] if h.owner[v] == 0 else H[t][1][v]
def play(t, v, force=None):
    f = succf(t); seen = []; 
    while v not in seen:
        seen.append(v); v = force.get(v, f(v)) if force else f(v)
    return seen
if "--class" in sys.argv:
    for t in range(T + 1):
        m = H[t][0][r][1]
        print(t, "Lambda(R)", iv[H[t][0][r][0]], "E(R)", [iv[w] for k, w in V.items() if isinstance(k, tuple) and k[0] == "e" and (m >> E.rank[w]) & 1])
    sys.exit(0)
for t in range(1, T + 1):
    if any(H[t][0][v][0] != H[t - 1][0][v][0] for v in range(n)): continue
    fl = [g for g in gates if H[t][1][g] != H[t - 1][1][g]]
    if not fl: continue
    cr = (H[t][0][r][0], H[t][0][r][1] & em) != (H[t - 1][0][r][0], H[t - 1][0][r][1] & em)
    desc = []
    for g in fl:
        q, a, b = gates[g]
        hits = [int(r in play(s, a)) for s in (t - 1, t)] + [int(r in play(s, b)) for s in (t - 1, t)]
        onR = [int(g in play(s, r)) for s in (t - 1, t)]
        desc.append("%s%s eR%s bR%s gOnRplay%s" % (q, "e" if H[t][1][g] == a else "b", hits[:2], hits[2:], onR))
    print(t, "Rclass-change" if cr else "NO-Rchange", "; ".join(desc))
