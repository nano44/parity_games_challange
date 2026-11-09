#!/usr/bin/env python3
"""L-COMP box 37: minimise a br order B toward MWR's order A by single-option relocations.
Skeleton = an LCS of A and B. Each non-skeleton option q sits after anchor_B(q) (nearest preceding skeleton option in B) or, when
reverted, after anchor_A(q) (in A). Greedy removal of relocations while Q flips >= TGT. Input: SP/<IN>_named.json. Output: SP/mv_named.json."""
import sys, os, json, copy
from ablate37 import *
os.chdir(os.path.join(H, "../box36"))
SP = os.environ["SP"]; IN = os.environ.get("IN", "min"); TGT = int(os.environ.get("TGT", "34"))
core = json.load(open(SP + f"/{IN}_named.json"))
for k in ("gate", "br"): core[k] = [tuple(q) for q in core[k]]
a = [tuple(q) for q in Mw["br"]]; b = core["br"]
n, m = len(a), len(b); L = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        L[i][j] = L[i + 1][j + 1] + 1 if a[i] == b[j] else max(L[i + 1][j], L[i][j + 1])
i = j = 0; sk = []
while i < n and j < m:
    if a[i] == b[j]: sk.append(a[i]); i += 1; j += 1
    elif L[i + 1][j] >= L[i][j + 1]: i += 1
    else: j += 1
sks = set(sk)
def anchor(order, q):
    p = order.index(q)
    while p > 0:
        p -= 1
        if order[p] in sks: return order[p]
    return None
moved = [q for q in b if q not in sks]
anc = {q: (anchor(a, q), anchor(b, q)) for q in moved}
def order(S):
    slots = {x: [] for x in [None] + sk}
    for q in b:
        if q in S: slots[anc[q][1]].append(q)
    for q in a:
        if q in anc and q not in S: slots[anc[q][0]].append(q)
    o = list(slots[None])
    for x in sk: o.append(x); o += slots[x]
    return o
def ev(S):
    Nd = copy.deepcopy(core); Nd["br"] = order(S); G = from_named(Nd); r = measure(G)
    return qflips(G, Nd, r["rows"]), r["C"], r["T3"], r["maxflip"], G, Nd
print("moved", len(moved), "full", ev(set(moved))[:4], flush=True)
S = set(moved)
for q in moved:
    r = ev(S - {q})
    if r[0] >= TGT: S -= {q}
r = ev(S)
print("minimal relocations", len(S), r[:4])
for q in b:
    if q in S: print("  ", q, "MWR after", anc[q][0], "-> after", anc[q][1])
json.dump(r[5], open(SP + "/mv_named.json", "w"), default=list); json.dump(r[4], open(SP + "/mv.json", "w"))
