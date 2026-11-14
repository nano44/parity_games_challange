#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): pulse and gap slack against a target height H. For each doubling level j (1 <= j <= H-2 and level j doubling in
the run) and each j-window W with successor W+: PULSE(W) = u2(W) - u1(W) and GAP(W) = u1(W+) - u2(W) (the (j+1)-window between the two
pulses). For H capped levels, PULSE-NEST (L-SI 42) needs PULSE >= H - j and GAP-NEST (§5) needs GAP >= H - j. Tally by opening b-step
type. Usage: slack.py genome.json H"""
import sys, os, json
from collections import defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run
from trace import keys
G = json.load(open(sys.argv[1])); H = int(sys.argv[2]); N = G['N']; d = N // 2
S = run(G, G['start']); T = len(S) - 1
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
F = [sum(O[t][l] != O[t-1][l] for t in range(1, T + 1)) for l in range(d)]
print("T", T, "F", F[:H + 1])
for j in range(1, H - 1):
    if F[j] != 2 * F[j-1] + 2: print("j", j, "not doubling"); continue
    p, q = 2*j, 2*j+1
    bst = [t for t in range(1, T + 1) if O[t][j-1] != O[t-1][j-1]]; cuts = [1] + bst + [T + 1]
    W = []
    for a, b in zip(cuts, cuts[1:]):
        mv = [t for t in range(a, b) for x in (p, q) if S[t][x] != S[t-1][x]]
        typ = tuple((x, S[a][x]) for x in (p-2, q-2) if a > 1 and S[a][x] != S[a-1][x])
        W.append((typ, mv))
    need = H - j; agg = defaultdict(lambda: [10**9, 10**9, 0, 0, 0])
    for i, (typ, mv) in enumerate(W):
        a = agg[typ]; a[4] += 1
        pu = mv[1] - mv[0]; a[0] = min(a[0], pu); a[2] += pu < need
        if i + 1 < len(W): ga = W[i+1][1][0] - mv[1]; a[1] = min(a[1], ga); a[3] += ga < need
    tot = sum(v[2] + v[3] for v in agg.values())
    print(f"j {j} need {need}: violations {tot}; per type (min pulse, min gap, #pulse<need, #gap<need, windows):",
          {str(k): v for k, v in sorted(agg.items(), key=lambda z: str(z[0]))})
