#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): DOMINATOR audit (Lemma DOMINANCE-FREEZE, L5 §6). For level J: per J-window, for each member x of pair J, the set
of deciding elements (the beta of largest rank in the symmetric difference of x's two chains, R105 ENC) over the states of the window,
and whether x moved. Tally failing windows (not exactly two moves) by their deciding elements. Usage: domin.py genome.json J"""
import sys, os, json
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run
from trace import keys
G = json.load(open(sys.argv[1])); J = int(sys.argv[2]); N = G['N']; d = N // 2
S = run(G, G['start']); T = len(S) - 1
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
def chain(s, x, k):
    out = []
    while True:
        wt, xt, m = G['opts'][x][k]; out.append((G['br'][m], G['bp'][m], x, k))
        if xt < 0: return out
        x, k = xt, s[xt]
def dec(s, x):
    a = set(chain(s, x, 0)); b = set(chain(s, x, 1)); t = max(a ^ b); return t[:1] + t[2:]  # (rank, mover, option)
bst = [t for t in range(1, T + 1) if O[t][J-1] != O[t-1][J-1]]; cuts = [1] + bst + [T + 1]
tal = Counter(); okt = Counter()
for a, b in zip(cuts, cuts[1:]):
    mv = [t for t in range(a, b) for x in (2*J, 2*J+1) if S[t][x] != S[t-1][x]]
    ds = tuple(sorted({dec(S[t], x) for t in range(a - 1, b - 1) for x in (2*J, 2*J+1)}))
    (tal if len(mv) != 2 else okt)[ds] += 1
print("failing windows by deciding elements (rank, mover, option):")
for k, n in tal.most_common(): print("  ", n, k)
print("good windows: most common deciding sets:")
for k, n in okt.most_common(5): print("  ", n, k)
