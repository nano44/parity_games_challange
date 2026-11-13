#!/usr/bin/env python3
"""L-COMP box 47: drop the top j levels of a JSON genome (movers of level >= d - j removed with their options; a Ξ-target that was removed
becomes X (-1); gate, β rank and e-numbering (eperm) re-ranked over the kept options, order kept). Usage: trunc47.py in.json j out.json"""
import sys, json
G = json.load(open(sys.argv[1])); G = G if "N" in G else G["genome"]; j = int(sys.argv[2]); d = max(G["lev"]) + 1
keep = [x for x in range(G["N"]) if G["lev"][x] < d - j]; nx = {x: i for i, x in enumerate(keep)}
O = [(x, k) for x in keep for k in range(len(G["opts"][x]))]
rr = lambda v: {q: r for r, q in enumerate(sorted(v, key=v.get))}
gr = rr({q: G["gate"][q[0]][q[1]] for q in O}); brr = rr({q: G["br"][G["opts"][q[0]][q[1]][2]] for q in O})
opts, gate, br, bp = [], [], [0] * len(O), [0] * len(O); i = 0
for x in keep:
    oo, gg = [], []
    for k, (wt, xt, b) in enumerate(G["opts"][x]):
        oo.append([nx[wt] if wt >= 0 else -1, nx.get(xt, -1) if xt >= 0 else -1, i]); gg.append(gr[(x, k)]); br[i] = brr[(x, k)]; bp[i] = G["bp"][b]; i += 1
    opts.append(oo); gate.append(gg)
H = dict(N=len(keep), lev=[G["lev"][x] for x in keep], opts=opts, gate=gate, br=br, bp=bp, start=[G["start"][x] for x in keep])
if "eperm" in G:   # eperm[i] = e-slot of the i-th option in gate order; keep the relative order of the kept options' slots
    go = sorted(((x, k) for x in range(G["N"]) for k in range(len(G["opts"][x]))), key=lambda q: G["gate"][q[0]][q[1]])
    slot = {q: G["eperm"][i] for i, q in enumerate(go)}; kept = rr({q: slot[q] for q in O}); go2 = sorted(O, key=lambda q: gr[q])
    H["eperm"] = [kept[q] for q in go2]
json.dump(H, open(sys.argv[3], "w"), sort_keys=True)
print("trunc47 %s -%d levels: N %d M %d d %d" % (sys.argv[1], j, H["N"], len(O), d - j))
