#!/usr/bin/env python3
"""L-COMP box 47: TOP-ADD lift of a JSON genome (box 30 / L-LOWER lift.py's rule, written for the JSON genome format): add k levels on top;
each new level has two movers with two options each, W-targets = the two lowest-index movers of the level below (in the two orders), Ξ-target X
(-1), β ranks above all old ones (new top level highest), parity even, gate indices fresh (above all old ones), start 0. An "eperm" is
extended by the identity on the new options. Usage: lift47.py in.json k out.json"""
import sys, json
G = json.load(open(sys.argv[1])); G = G.get("genome", G) if "N" not in G else G; k = int(sys.argv[2])
N, lev = G["N"], list(G["lev"]); opts = [list(map(list, o)) for o in G["opts"]]; gate = [list(g) for g in G["gate"]]
br, bp, start = list(G["br"]), list(G["bp"]), list(G["start"]); M = len(br); g0 = max(max(g) for g in gate) + 1; r0 = max(br) + 1
for j in range(k):
    top = max(lev); below = sorted(x for x in range(len(lev)) if lev[x] == top)[:2]
    if len(below) < 2: below = below * 2
    for p in range(2):
        x = len(lev); lev.append(top + 1); o = []; gg = []
        for kk in range(2):
            o.append([below[(p + kk) % 2], -1, M]); br.append(r0); bp.append(0); gg.append(g0); M += 1; r0 += 1; g0 += 1
        opts.append(o); gate.append(gg); start.append(0)
H = dict(N=len(lev), lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start)
if "eperm" in G: H["eperm"] = list(G["eperm"]) + list(range(len(G["eperm"]), M))
json.dump(H, open(sys.argv[3], "w"), sort_keys=True)
print("lift47 %s +%d levels: N %d M %d N+M %d" % (sys.argv[1], k, H["N"], M, H["N"] + M))
