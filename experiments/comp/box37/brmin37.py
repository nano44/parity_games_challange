#!/usr/bin/env python3
"""L-COMP box 37: minimise the br permutation of the core (MWR8_2 + r34 br order + a47 bp) toward MWR8_2's br order.
The core order = MWR order composed with a list of transpositions (cycle decomposition, written as swaps of positions); greedy
one-at-a-time removal of a transposition if (Q flips, C) stays >= target. Output: the minimal swap list in named form."""
import sys, os, json, copy
from ablate37 import *
os.chdir(os.path.join(H, "../box36"))
SP = os.environ["SP"]; core = json.load(open(SP + "/core_named.json"))
for k in ("gate", "br"): core[k] = [tuple(q) for q in core[k]]
mb = [tuple(q) for q in Mw["br"]]; cb = core["br"]
# transpositions: start from mb, fix positions one by one
cur = list(mb); swaps = []
for i in range(len(cb)):
    if cur[i] != cb[i]:
        j = cur.index(cb[i]); cur[i], cur[j] = cur[j], cur[i]; swaps.append((cur[j], cur[i]))   # swap of two named options
assert cur == cb
def order(sw):
    o = list(mb)
    for a, b in sw:
        i, j = o.index(a), o.index(b); o[i], o[j] = o[j], o[i]
    return o
def ev(sw, extra=None):
    Nd = copy.deepcopy(core); Nd["br"] = order(sw); G = from_named(Nd); r = measure(G)
    return qflips(G, Nd, r["rows"]), r["C"], r["T3"], r["maxflip"], G, Nd
TGT = int(os.environ.get("TGT", "34"))
print("swaps", len(swaps), "check", ev(swaps)[:4])
keep = list(swaps)
for s in list(swaps):
    t = [x for x in keep if x != s]; r = ev(t)
    if r[0] >= TGT: keep = t
print("minimal swaps", len(keep), keep, ev(keep)[:4])
r = ev(keep); json.dump(r[5], open(SP + "/min_named.json", "w"), default=list); json.dump(r[4], open(SP + "/min.json", "w"))
