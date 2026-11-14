#!/usr/bin/env python3
"""L-RED R195 MERGECK2: checks Lemma MERGE-1* (docs/red/R195-nest4.md §1; the descendant form of R191 MERGE-1): at a step t where exactly
one mover y of desc(x) moves, a change of the order of face(x,k), face(x,k') between s_(t-1) and s_t needs exactly one of the two
s_(t-1)-chains to contain y, and that face gains. Usage: mergeck2.py genome.json ..."""
import sys, os, json
H = os.path.dirname(os.path.abspath(__file__)); sys.path[:0] = [os.path.join(H, "..", "r187"), os.path.join(H, "..", "r178")]
import ideal, fastcyc
def chain(G, s, v, k):
    O = G["opts"]; out = set(); x, kk = v, k
    while True:
        xt = O[x][kk][1]
        if xt < 0: return out
        out.add(xt); x, kk = xt, s[xt]
tot = 0; evt = 0
for f in sys.argv[1:]:
    G = json.load(open(f)); S, why = ideal.traj(G, cap=20000); N = G["N"]; O = G["opts"]; bad = ev = 0
    desc = []
    for v in range(N):
        seen = set(); st = [v]
        while st:
            x = st.pop()
            for (_, xt, _) in O[x]:
                if xt >= 0 and xt not in seen: seen.add(xt); st.append(xt)
        desc.append(seen)
    F = []
    for s in S:
        val, idx, _, _ = fastcyc.values(G, list(s)); F.append({(v, k): val(N + idx[(v, k)]) for v in range(N) for k in range(len(O[v]))})
    for t in range(1, len(S)):
        mv = {v for v in range(N) if S[t][v] != S[t - 1][v]}
        for x in range(N):
            dm = mv & desc[x]
            if len(dm) != 1: continue
            y = next(iter(dm))
            for k in range(len(O[x])):
                for k2 in range(k + 1, len(O[x])):
                    a0, a1 = F[t - 1][(x, k)] > F[t - 1][(x, k2)], F[t][(x, k)] > F[t][(x, k2)]
                    if a0 == a1: continue
                    ev += 1; ck, ck2 = y in chain(G, S[t - 1], x, k), y in chain(G, S[t - 1], x, k2); gain = k if a1 else k2
                    if ck == ck2 or (gain == k) != ck: bad += 1
    tot += bad; evt += ev
print(f"MERGECK2 genomes {len(sys.argv) - 1} order changes {evt} violations {tot}")
