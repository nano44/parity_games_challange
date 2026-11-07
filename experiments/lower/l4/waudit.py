#!/usr/bin/env python3
"""L-LOWER 4: window audit. For each doubling level l (F(l) = 2F(l-1)+2) of a run, the (l+1)-windows (stretches between moves of
pair l), their type (S split / J together), whether D_l = cv(2l) - cv(2l+1) changes strictly inside, and which movers moved at those
steps on the current chains of pair l's two current Xi-targets ('t' tower pair <= l-2 by level, 'u' upward = level > l). Usage:
waudit.py genome.json"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'l3'))
from sim import run, val
from trace import keys
G = json.load(open(sys.argv[1])); N = G["N"]; d = N // 2; S = run(G, G["start"]); T = len(S) - 1
O = [[0 if k[2*l] < k[2*l+1] else 1 for l in range(d)] for k in (keys(G, s) for s in S)]
F = [sum(O[t][l] != O[t-1][l] for t in range(1, T + 1)) for l in range(d)]
print("T", T, "F", F)
def cv(s, x): return val(G, s, x, s[x])
def chain(s, x):
    out = []
    while True:
        y = G["opts"][x][s[x]][1]
        if y < 0: return out
        out.append(y); x = y
for l in range(1, d - 1):
    if F[l] != 2 * F[l-1] + 2: continue
    p, q = 2*l, 2*l+1
    mv = [t for t in range(1, T + 1) if S[t][p] != S[t-1][p] or S[t][q] != S[t-1][q]]
    bounds = mv + [T + 1]
    rows = []; fed = 0; nw = 0
    for a, b in zip(bounds, bounds[1:]):
        s = S[a]; typ = "S" if s[p] != s[q] else "J"
        D0 = cv(s, p) - cv(s, q); ch = [u for u in range(a + 1, b) if cv(S[u], p) - cv(S[u], q) != D0]
        nw += 1; fed += bool(ch)
        who = set()
        for u in ch[:1]:
            on = set(chain(S[u-1], p)) | set(chain(S[u-1], q)) | set(chain(S[u], p)) | set(chain(S[u], q))
            for x in on:
                if S[u][x] != S[u-1][x]: who.add(f"{x}({G['lev'][x]})")
        rows.append(f"{typ}[{a},{b-1}]{'+' if ch else '-'}{'/'.join(sorted(who)) if who else ''}")
    print(f"level {l} doubling: (l+1)-windows {nw}, D_l changes inside {fed}; targets p {[o[1] for o in G['opts'][p]]} q {[o[1] for o in G['opts'][q]]}")
    print("   ", " ".join(rows))
