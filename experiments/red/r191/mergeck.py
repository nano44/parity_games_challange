#!/usr/bin/env python3
"""L-RED R191 MERGECK: checks Lemma MERGE-1 (docs/red/R191-rotation.md §2) on IDEAL runs: at every step t where exactly one mover y
moves, for every mover x and options k != k', if the order of face(x,k), face(x,k') differs between s_(t-1) and s_t then exactly one
of the two chains under s_(t-1) contains y, and that face is the one that gains. Usage: mergeck.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal, fastcyc
def chain(G, s, v, k):
    O = G["opts"]; out = set(); x, kk = v, k
    while True:
        xt = O[x][kk][1]
        if xt < 0: return out
        out.add(xt); x, kk = xt, s[xt]
tot = 0
for f in sys.argv[1:]:
    G = json.load(open(f)); S, why = ideal.traj(G, cap=20000); N = G["N"]; O = G["opts"]; bad = 0; ev = 0
    F = []
    for s in S:
        val, idx, _, _ = fastcyc.values(G, list(s)); F.append({(v, k): val(N + idx[(v, k)]) for v in range(N) for k in range(len(O[v]))})
    for t in range(1, len(S)):
        mv = [v for v in range(N) if S[t][v] != S[t - 1][v]]
        if len(mv) != 1: continue
        y = mv[0]
        for x in range(N):
            for k in range(len(O[x])):
                for k2 in range(k + 1, len(O[x])):
                    a0, a1 = F[t - 1][(x, k)] > F[t - 1][(x, k2)], F[t][(x, k)] > F[t][(x, k2)]
                    if a0 == a1: continue
                    ev += 1; ck, ck2 = y in chain(G, S[t - 1], x, k), y in chain(G, S[t - 1], x, k2)
                    gain = k if a1 else k2
                    if ck == ck2 or (gain == k) != ck: bad += 1
    tot += bad; print(f"{os.path.basename(f)}: L {len(S) - 1} single-mover order changes {ev} violations {bad}")
print(f"MERGECK total violations {tot}")
