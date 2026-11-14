#!/usr/bin/env python3
"""L-LOWER 5 (BOX L5): trigger chains with link types. For level J and each J-window: x2 moves at u2; walk back: for a mover z that
moved at step t, let v = the last step <= t-1 at which pref(z) became true (pref(z) under s_v true, under s_(v-1) false); if v = t-1 the
link is Xi (the preference flipped one step before the move: the next trigger = the movers on z's chains that moved at v); if v < t-1
the link is K (z waited for its key from v+1 to t; the key c_L flipped at t: report the lowest pair flipping at t). Follows the first
trigger (lowest index) up to depth 6. Tally chains by b-step type. Usage: trig.py genome.json J"""
import sys, os, json
from collections import Counter, defaultdict
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run, val
from trace import keys
G = json.load(open(sys.argv[1])); J = int(sys.argv[2]); N = G['N']; d = N // 2
S = run(G, G['start']); T = len(S) - 1
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
def pref(t, z): return val(G, S[t], z, 1 - S[t][z]) > val(G, S[t], z, S[t][z])
def chainset(s, x):
    out = set()
    for k in (0, 1):
        y = G['opts'][x][k][1]
        while y >= 0: out.add(y); y = G['opts'][y][s[y]][1]
    return out
def link(z, t, depth):
    if depth > 6 or t < 2: return f"{z}@{t}"
    v = t - 1
    while v - 1 >= 0 and pref(v - 1, z): v -= 1
    if v == t - 1:
        cs = chainset(S[v-1], z) | chainset(S[v], z) if v >= 1 else set()
        trg = sorted(x for x in cs if v >= 1 and S[v][x] != S[v-1][x])
        if not trg: return f"{z}@{t}<Ξ?"
        return f"{z}@{t}<Ξ " + link(trg[0], v, depth + 1) + (f"(+{len(trg)-1})" if len(trg) > 1 else "")
    fl = [l for l in range(d) if O[t][l] != O[t-1][l]]
    return f"{z}@{t}<K(wait {t-1-v}, pairs flipping {fl[:4]})"
p, q = 2*J, 2*J+1
bst = [t for t in range(1, T + 1) if O[t][J-1] != O[t-1][J-1]]; cuts = [1] + bst + [T + 1]
tal = defaultdict(Counter)
for a, b in zip(cuts, cuts[1:]):
    mv = [(t, x) for t in range(a, b) for x in (p, q) if S[t][x] != S[t-1][x]]
    typ = tuple((x, S[a][x]) for x in (p-2, q-2) if a > 1 and S[a][x] != S[a-1][x])
    if len(mv) != 2: continue
    (u1, x1), (u2, x2) = mv
    ch = link(x2, u2, 0)
    import re
    tal[typ][re.sub(r'@\d+', '', ch).replace(f'{x2}<', 'x2<', 1) + f" | pulse {u2-u1}"] += 1
for typ in sorted(tal, key=str):
    print("type", typ)
    for c, n in tal[typ].most_common(4): print("   ", n, ":", c)
