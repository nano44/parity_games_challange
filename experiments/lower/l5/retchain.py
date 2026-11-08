#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): RETURN-CHAIN test. For each doubling level j (j+1 doubling too) and j-window: is the second mover x2_(j+1) of the
nested (j+1)-window [u1, u2-1] among x2_j's triggers (movers on x2_j's chains moving at u2-1)? Also the level of each trigger relative to
j. Usage: retchain.py genome.json"""
import sys, os, json
from collections import Counter, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run
from trace import keys
G = json.load(open(sys.argv[1])); N = G['N']; d = N // 2
S = run(G, G['start']); T = len(S) - 1
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
F = [sum(O[t][l] != O[t-1][l] for t in range(1, T + 1)) for l in range(d)]
dbl = [l >= 1 and F[l] == 2 * F[l-1] + 2 for l in range(d)]
def chainset(s, x):
    out = set()
    for k in (0, 1):
        y = G['opts'][x][k][1]
        while y >= 0: out.add(y); y = G['opts'][y][s[y]][1]
    return out
def windows(j):
    bst = [t for t in range(1, T + 1) if O[t][j-1] != O[t-1][j-1]]; cuts = [1] + bst + [T + 1]; W = []
    for a, b in zip(cuts, cuts[1:]):
        mv = [(t, x) for t in range(a, b) for x in (2*j, 2*j+1) if S[t][x] != S[t-1][x]]
        typ = tuple((x, S[a][x]) for x in (2*j-2, 2*j-1) if a > 1 and S[a][x] != S[a-1][x])
        W.append((typ, mv))
    return W
print("F", F[:12])
for j in range(1, d - 1):
    if not (dbl[j] and dbl[j+1]): continue
    W1 = windows(j + 1); ret = Counter(); rel = Counter()
    for typ, mv in windows(j):
        if len(mv) != 2: continue
        (u1, _), (u2, x2) = mv
        cs = chainset(S[u2-2], x2) | chainset(S[u2-1], x2)
        trg = [x for x in cs if S[u2-1][x] != S[u2-2][x]]
        for x in trg: rel[x // 2 - j] += 1
        nested = [m for ty, m in W1 if len(m) == 2 and m[0][0] >= u1 and m[1][0] <= u2 - 1]
        x2n = nested[-1][1][1] if nested else None
        ret[(str(typ), x2n in trg)] += 1
    print("j", j, "return-chain (type, x2_(j+1) is a trigger):", dict(ret), " trigger level - j:", dict(sorted(rel.items())))
