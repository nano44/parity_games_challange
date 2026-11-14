#!/usr/bin/env python3
"""box 80: INSERT-PASS. insert80.py in.json L > out.json: shift levels >= L up by one and insert at level L a pair (a, b) = (2L, 2L+1)
that never moves and is split (a on option 0, b on option 1), both options with Xi-target X; the start option carries +2^r1, the other
-2^r0 with two new ranks above all others; new gates above all others. Every W-target and Xi-target index is renumbered."""
import json, sys
G = json.load(open(sys.argv[1])); L = int(sys.argv[2]); N = G["N"]
ren = lambda y: y if y < 2 * L else y + 2
opts = []; gate = []; br = list(G["br"]); bp = list(G["bp"]); st = []
for x in range(N):
    if x == 2 * L:
        mx = max(br) + 1; gm = max(max(g) for g in G["gate"]) + 1
        for q in range(2):
            row = []
            for k in range(2):
                e = len(br); good = (k == q); br.append(mx + 2 * q + (1 if good else 0)); bp.append(0 if good else 1)
                row.append([2 * (L - 1) + k, -1, e])
            opts.append(row); gate.append([gm + 2 * q, gm + 2 * q + 1]); st.append(q)
    l = x // 2; lv = l + (1 if l >= L else 0)
    opts.append([[2 * (lv - 1) + k if lv > 0 else -1, ren(G["opts"][x][k][1]) if G["opts"][x][k][1] >= 0 else -1, G["opts"][x][k][2]] for k in range(2)])
    gate.append(list(G["gate"][x])); st.append(G["start"][x])
if L >= N // 2:
    raise SystemExit("L must be < d")
H = {"N": N + 2, "lev": [v // 2 for v in range(N + 2)], "deg": 2, "opts": opts, "gate": gate, "br": br, "bp": bp, "start": st}
json.dump(H, sys.stdout)
