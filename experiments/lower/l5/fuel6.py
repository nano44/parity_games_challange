#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): fuel of a (possibly non-doubling) level J. Per J-window: own type (pair J-1 member, direction), the type of the
enclosing (J-1)-window (pair J-2 member, direction), the moves of pair J; for every member of pair J that moves at step u (> window
start), the triggers = movers on its chains that moved at u - 1 (if its preference flipped at u - 1), else 'K' (key-gated);
for a member that does NOT move, whether its preference toward the window's key ever holds inside the window.
Usage: fuel6.py genome.json J"""
import sys, os, json
from collections import Counter, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run, val
from trace import keys
G = json.load(open(sys.argv[1])); J = int(sys.argv[2]); N = G['N']; d = N // 2
S = run(G, G['start']); T = len(S) - 1
K = [keys(G, s) for s in S]
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in K]
def pref(t, z): return val(G, S[t], z, 1 - S[t][z]) > val(G, S[t], z, S[t][z])
def chainset(s, x):
    out = set()
    for k in (0, 1):
        y = G['opts'][x][k][1]
        while y >= 0: out.add(y); y = G['opts'][y][s[y]][1]
    return out
def wins(j):
    bst = [t for t in range(1, T + 1) if O[t][j-1] != O[t-1][j-1]]; cuts = [1] + bst + [T + 1]
    return [(a, b - 1, tuple((x, S[a][x]) for x in (2*j-2, 2*j-1) if a > 1 and S[a][x] != S[a-1][x])) for a, b in zip(cuts, cuts[1:])]
up = wins(J - 1); tal = defaultdict(Counter)
for a, e, typ in wins(J):
    par = [ty for (aa, ee, ty) in up if aa <= a <= ee]; ptyp = par[0] if par else None
    c = O[a][J-1]   # key c_J in this window
    desc = []
    for x in (2*J, 2*J+1):
        mvs = [t for t in range(a, e + 1) if S[t][x] != S[t-1][x]]
        if mvs:
            u = mvs[0]
            if u >= 2 and pref(u - 1, x) and not pref(u - 2, x):
                tr = sorted(z for z in chainset(S[u-2], x) | chainset(S[u-1], x) if S[u-1][z] != S[u-2][z]); desc.append(f"{x}:mv<{tr}")
            else: desc.append(f"{x}:mv<K")
        else:
            on_c = S[a][x] == c
            ever = any(pref(t, x) for t in range(a - 1, e + 1)) if not on_c else None
            desc.append(f"{x}:{'already on c' if on_c else ('NO MOVE, pref ' + ('seen' if ever else 'never'))}")
    tal[(str(ptyp), str(typ))][' '.join(desc)] += 1
for k in sorted(tal):
    print("parent", k[0], "own", k[1])
    for dsc, n in tal[k].most_common(3): print("    ", n, dsc)
