#!/usr/bin/env python3
"""Box 214 Step A (L-NEW successor 75): level-by-level alignment of the towers H5 -> H6 -> HIT7 (box212/inst): per level the W-target pattern, the Xi-target pattern (level offset lev(xt) - l and side), beta priority and start bit; matches at every shift; and the per-level Xi offsets. Usage: python3 align214.py (any directory)."""
import os; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "box212", "inst"))
import json, sys, random, statistics
def load(f):
    G = json.load(open(f)); return G.get("genome", G)
def sig(G):
    lev = G["lev"]; d = max(lev) + 1; out = []
    # global rank of beta priority (br, bp) -> order-preserving, compare relative to level via rank among all
    pr = sorted(set((G["br"][b], G["bp"][b]) for b in range(len(G["br"]))))
    rk = {p: i for i, p in enumerate(pr)}
    for l in range(d):
        row = []
        for x in (2 * l, 2 * l + 1):
            for k, (wt, xt, b) in enumerate(G["opts"][x]):
                row.append((-1 if wt < 0 else wt - 2 * (l - 1), "X" if xt < 0 else (lev[xt] - l, xt % 2), G["bp"][b], G["start"][x] == k))
        out.append(tuple(row))
    return out, d
names = ["DBL4_d20_F30.json", "H5_d20_F62.json", "H6_d24_F126.json", "HIT7_d28_F254.json", "RECF4_d20_F60.json"]
S = {n: sig(load(n)) for n in names}
for a, b in [("H5_d20_F62.json", "H6_d24_F126.json"), ("H6_d24_F126.json", "HIT7_d28_F254.json"), ("H5_d20_F62.json", "HIT7_d28_F254.json")]:
    sa, da = S[a]; sb, db = S[b]
    best = []
    for sh in range(0, db - da + 1):
        m_full = sum(1 for l in range(da) if sa[l] == sb[l + sh])
        m_wt = sum(1 for l in range(da) if [r[0] for r in sa[l]] == [r[0] for r in sb[l + sh]])
        m_xt = sum(1 for l in range(da) if [r[1] for r in sa[l]] == [r[1] for r in sb[l + sh]])
        best.append((sh, m_full, m_wt, m_xt))
    print(a, "->", b, "levels", da, "of", db, "(shift, full-level matches, wt-pattern matches, xt-pattern matches):", best)
# per-level xt offset profile
for n in names[1:4]:
    s, d = S[n]; print(n, "xt-offsets per level:", [tuple(r[1][0] if r[1] != "X" else "X" for r in s[l]) for l in range(d)])
