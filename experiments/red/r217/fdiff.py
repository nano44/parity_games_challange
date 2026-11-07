#!/usr/bin/env python3
"""L-RED 54 R217: first divergence between Howard on switchallexp G_n (fried.howard) and Howard on IDEAL-CYC of comp.compile_(n).
Usage: fdiff.py n"""
import sys, os
sys.path.insert(0, os.path.join(os.environ["WT3"], "experiments/new/box191"))
import idealcyc
from fried import game, howard
from comp import compile_
n = int(sys.argv[1]); V = game(n); nm = {v[0]: v[4] for v in V}; sc = {v[0]: v[3] for v in V}
T, traj = howard(V); G, ix = compile_(n); st = idealcyc.run(G)
inv = {i: s for s, i in ix.items()}
mv = {v: ix["M_" + nm[v]] for v in nm if ("M_" + nm[v]) in ix and V[v][2] == 0}
print("orig T", T, "genome T", len(st) - 1)
for t in range(max(len(traj), len(st))):
    a = traj[min(t, len(traj) - 1)]; b = st[min(t, len(st) - 1)]
    da = {nm[v]: nm[a[v]] for v in mv}; db = {nm[v]: nm[sc[v][b[mv[v]]]] for v in mv}
    diff = {k: (da[k], db[k]) for k in da if da[k] != db[k]}
    if diff:
        print("t", t, "first divergence (orig, genome):", diff)
        if t > 0:
            pa = traj[t - 1]; print("  orig switches at t:", {nm[v]: (nm[pa[v]], nm[a[v]]) for v in mv if pa[v] != a[v]})
            pb = st[t - 1]; print("  genome switches at t:", {nm[v]: (nm[sc[v][pb[mv[v]]]], nm[sc[v][b[mv[v]]]]) for v in mv if pb[mv[v]] != b[mv[v]]})
        break
