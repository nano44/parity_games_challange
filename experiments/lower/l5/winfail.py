#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): for level J of a genome, per J-window (delimited by the flips of pair J-1): the opening b-step type (member of
pair J-1 that moved, its new option), the moves of pair J in the window (DOUBLE-EQ' (E4) needs exactly one each, first f then x2), and a
tally of failing windows by type. Usage: winfail.py genome.json J"""
import sys, os, json
from collections import Counter, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run, val
from trace import keys
G = json.load(open(sys.argv[1])); J = int(sys.argv[2]); N = G['N']; d = N // 2
S = run(G, G['start']); T = len(S) - 1
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
F = [sum(O[t][l] != O[t-1][l] for t in range(1, T + 1)) for l in range(d)]
p, q = 2*J, 2*J+1
bst = [t for t in range(1, T + 1) if O[t][J-1] != O[t-1][J-1]]
cuts = [1] + bst + [T + 1]
tally = defaultdict(Counter); rows = []
for i, (a, b) in enumerate(zip(cuts, cuts[1:])):
    if a >= b and i > 0: pass
    mv = [(t, x, S[t][x]) for t in range(a, b) for x in (p, q) if S[t][x] != S[t-1][x]]
    typ = tuple((x, S[a][x]) for x in (p-2, q-2) if a > 1 and S[a][x] != S[a-1][x])
    pat = ''.join('p' if x == p else 'q' for _, x, _ in mv)
    tally[typ][pat] += 1; rows.append((i, a, b - 1, typ, pat, [t for t, _, _ in mv]))
print("T", T, "F", F[:J+2], "windows of level", J, len(rows), "(cap needs", F[J-1] + 1, "windows x 2 moves)")
for typ, c in sorted(tally.items(), key=lambda z: str(z[0])): print(" type", typ, dict(c))
bad = [r for r in rows if len(r[4]) != 2]
print("failing windows (not exactly two moves):", len(bad))
for r in bad[:40]: print("  win", r[0], "steps", r[1], "-", r[2], "type", r[3], "moves", r[4] or '-', r[5])
