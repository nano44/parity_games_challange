#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): for a doubling level J: per J-window, the opening b-step type, PULSE = u2 - u1, window length, and the
second mover's trigger (movers on x2's chains moving at u2 - 1). Tally PULSE by type. Usage: pulses.py genome.json J"""
import sys, os, json
from collections import Counter, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run, val
from trace import keys
G = json.load(open(sys.argv[1])); J = int(sys.argv[2]); N = G['N']; d = N // 2
S = run(G, G['start']); T = len(S) - 1
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
p, q = 2*J, 2*J+1
def chainset(s, x):
    out = set()
    for k in (0, 1):
        y = G['opts'][x][k][1]
        while y >= 0: out.add(y); y = G['opts'][y][s[y]][1]
    return out
bst = [t for t in range(1, T + 1) if O[t][J-1] != O[t-1][J-1]]
cuts = [1] + bst + [T + 1]; tal = defaultdict(Counter); trig = defaultdict(Counter)
for a, b in zip(cuts, cuts[1:]):
    mv = [(t, x) for t in range(a, b) for x in (p, q) if S[t][x] != S[t-1][x]]
    typ = tuple((x, S[a][x]) for x in (p-2, q-2) if a > 1 and S[a][x] != S[a-1][x])
    if len(mv) != 2: tal[typ]['FAIL'] += 1; continue
    (u1, x1), (u2, x2) = mv; tal[typ][f"pulse {u2-u1} len {b-a}"] += 1
    if u2 >= 2:
        cs = chainset(S[u2-2], x2) | chainset(S[u2-1], x2) if u2 >= 2 else set()
        trig[typ][tuple(sorted(x for x in cs if S[u2-1][x] != S[u2-2][x]))] += 1
for typ in sorted(tal, key=str): print("type", typ, dict(tal[typ]), "triggers", dict(trig[typ]))
