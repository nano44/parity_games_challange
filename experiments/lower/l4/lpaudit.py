#!/usr/bin/env python3
"""L-LOWER 4: LATE-PREF audit (docs/lower/L4-tower.md §4b). For each j with levels j and j+1 doubling: in every j-window, the moves
u1 < u2 of pair j, the check u2 >= u1 + 2, the preference flip of the second mover exactly at step u2 - 1, and the movers on the
second mover's two option chains (under s_(u2-2) and s_(u2-1)) that move at step u2 - 1, with their levels.
Usage: lpaudit.py genome.json [start]"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run, val
from trace import keys
G = json.load(open(sys.argv[1])); N = G["N"]; d = N // 2
s0 = [int(c) for c in sys.argv[2]] if len(sys.argv) > 2 else G["start"]
S = run(G, s0); T = len(S) - 1
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
F = [sum(O[t][l] != O[t-1][l] for t in range(1, T + 1)) for l in range(d)]
dbl = [l >= 1 and F[l] == 2 * F[l-1] + 2 for l in range(d)]
def pref_other_better(s, x): return val(G, s, x, 1 - s[x]) > val(G, s, x, s[x])
def chainset(s, x):
    out = set()
    for k in (0, 1):
        y = G["opts"][x][k][1]
        while y >= 0: out.add(y); y = G["opts"][y][s[y]][1]
    return out
viol = 0
print("T", T, "F", F)
for j in range(1, d - 1):
    if not (dbl[j] and dbl[j + 1]): continue
    p, q = 2*j, 2*j+1
    bst = [t for t in range(1, T + 1) if O[t][j-1] != O[t-1][j-1]]
    cuts = [1] + bst + [T + 1]
    out = []; src = {}
    for a, b in zip(cuts, cuts[1:]):
        if a >= b: continue
        mv = [(t, x) for t in range(a, b) for x in (p, q) if S[t][x] != S[t-1][x]]
        if len(mv) != 2: viol += 1; out.append("?"); continue
        (u1, x1), (u2, x2) = mv
        ok = u2 >= u1 + 2 and not pref_other_better(S[u2-2], x2) and pref_other_better(S[u2-1], x2)
        viol += not ok
        cs = chainset(S[u2-2], x2) | chainset(S[u2-1], x2)
        who = [x for x in cs if S[u2-1][x] != S[u2-2][x]]
        for x in who:
            lv = G["lev"][x]; key = "below" if lv < j - 1 else ("pair j-1" if lv == j - 1 else ("same" if lv == j else "above"))
            src[key] = src.get(key, 0) + 1
        out.append(f"{u1},{u2}:{x2}<-" + "/".join(f"{x}L{G['lev'][x]}" for x in sorted(who)))
    print(f"j {j}: windows {len(out)} sources {src}")
    print("   ", " ".join(out))
print("LATE-PREF violations", viol)
