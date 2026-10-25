#!/usr/bin/env python3
"""Box 34: fallback CLUSTERS (maximal runs of consecutive S4c transitions) along scope runs (P-N5-CLS §0: (h) at k, H2 at k+1,
w_{k+1} = w_k). Tests CONJECTURE CL1: inside one scope run, two clusters never share a level, where a cluster's level is the max M_k over
its fallbacks (and CLS1 makes levels non-increasing). Also tests: (TH) between two clusters of a scope run, θ rises at a level >= the
later cluster's level; the transition right after a cluster changes θ at exactly the cluster's level. Usage: fbclus.py game.pg ..."""
import sys, os, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from relfr import *

def bump(acc, k, d=1): acc[k] = acc.get(k, 0) + d
def mx(acc, k, v, *info):
    if v > acc.get(k, (-1,))[0]: acc[k] = (v,) + info

def scope_runs(rows, o):
    H2 = [h2(r["nxt"], o) for r in rows]
    hh = [r["h1"] and H2[i] and r["Xi"][o][0] == r["W"][o][0] for i, r in enumerate(rows)]
    ins = [rows[k]["ph"] == rows[k + 1]["ph"] and hh[k] and H2[k + 1] and rows[k]["w"] == rows[k + 1]["w"] for k in range(len(rows) - 1)]
    out = []; k = 0
    while k < len(ins):
        if not ins[k]: k += 1; continue
        j = k
        while j + 1 < len(ins) and ins[j + 1]: j += 1
        out.append(list(range(k, j + 1))); k = j + 1
    return out

def check(g, acc, name):
    rows, o = rows_w(g); n = g.n
    for tr in scope_runs(rows, o):
        cl = []; cur = []
        for k in tr:
            if rows[k]["fb"]: cur.append(k)
            elif cur: cl.append(cur); cur = []
        if cur: cl.append(cur)
        if not cl: continue
        bump(acc, "scope_runs_with_fb"); bump(acc, "clusters", len(cl))
        lv = [max(rows[k]["M"] for k in c) for c in cl]
        mx(acc, "max_clusters_per_scope_run", len(cl), n, name, tr[0]); mx(acc, "max_cluster_size", max(len(c) for c in cl), n, name)
        per = {}
        for l in lv: per[l] = per.get(l, 0) + 1
        mx(acc, "max_clusters_one_level", max(per.values()), n, name, tr[0])
        if max(per.values()) > 1: bump(acc, "CL1_FAIL"); acc.setdefault("ex_cl1", (name, tr[0], lv))
        if any(lv[i] < lv[i + 1] for i in range(len(lv) - 1)): bump(acc, "level_rise")
        for i in range(len(cl) - 1):
            a, b = cl[i][-1] + 1, cl[i + 1][0]; L = lv[i + 1]
            ok = any(rows[k]["th"] != rows[k + 1]["th"] and lev(rows[k]["Xi"][o], rows[k + 1]["Xi"][o]) >= L for k in range(a, b))
            if not ok: bump(acc, "TH_FAIL"); acc.setdefault("ex_th", (name, cl[i], cl[i + 1], L))
            bump(acc, "TH_checked")
        for i, c in enumerate(cl):
            k = c[-1] + 1
            if k + 1 < len(rows) and k in tr:
                if rows[k]["th"] != rows[k + 1]["th"] and lev(rows[k]["Xi"][o], rows[k + 1]["Xi"][o]) == lv[i]: bump(acc, "after_cluster_theta_at_M")
                else: bump(acc, "after_cluster_other")

if __name__ == "__main__":
    acc = {}; a = sys.argv[1:]
    for f in a:
        g = load(f)
        if sum(1 for u in range(g.n) if g.owner[u] == 1 and len(set(g.succ[u])) > 1) != 1: continue
        check(g, acc, os.path.basename(f))
    for k in sorted(acc): print(k, acc[k])
