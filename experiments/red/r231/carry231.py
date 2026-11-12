#!/usr/bin/env python3
"""L-RED 65 R231 item 1b: OWN implementation of L-NEW 70's CW(n) construction from its prose (box 206 Addendum C, C2, l-new f7b8bb66):
from MWR(n) (r229/genmw229.py WTGT=R, names on stderr), every high-bit mover qh_k (k < n, sorted by k) gets a new level-0 W-target c_k
in place of its W-target; c_k's options have Xi-targets qh_j (j > k, increasing) then X (-1), W-target -1, new beta ranks above all
existing ones (parity PAR), new gate indices after all existing ones, start = the X option. Env CW_REARM=<name|id>: Addendum D's re-arm option (Xi-target that vertex), parity CW_RPAR.  Usage: carry231.py MWR.json NAMES.json OUT.json [PAR]"""
import sys, json
G = json.load(open(sys.argv[1])); nm = json.load(open(sys.argv[2])); par = int(sys.argv[4]) if len(sys.argv) > 4 else 0
import os
RA = os.environ.get("CW_REARM")              # Addendum D variant: one more option per c_k (before X) with Xi-target RA (a name, or a mover id)
REARM = None if RA is None else (nm[RA] if RA in nm else int(RA)); RPAR = int(os.environ.get("CW_RPAR", str(par)))
qh = sorted((int(k[2:]), v) for k, v in nm.items() if k.startswith("qh") and k[2:].isdigit())
nbr = max(G["br"]) + 1; ngate = max(g for row in G["gate"] for g in row) + 1
for i in range(len(qh) - 1):
    x = qh[i][1]; c = G["N"]; G["N"] += 1; G["lev"].append(0); G["opts"].append([]); G["gate"].append([])
    extra = [REARM] if REARM is not None else []
    for xt in [y for _, y in qh[i + 1:]] + extra + [-1]:
        G["opts"][c].append([-1, xt, len(G["br"])]); G["br"].append(nbr); nbr += 1
        G["bp"].append(RPAR if (REARM is not None and xt == REARM and len(G["opts"][c]) == len(qh) - i) else par)
        G["gate"][c].append(ngate); ngate += 1
    G["start"].append(len(G["opts"][c]) - 1)
    assert len(G["opts"][x]) == 1; G["opts"][x][0][0] = c
json.dump(G, open(sys.argv[3], "w"))
