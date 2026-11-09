#!/usr/bin/env python3
"""L-COMP box 37 item 1: ablation of r34 (BEST_C300_r34_C17_30d4ea76) toward its seed MWR8_2 in named space (align37 names).
Units: per MWR mover 'rev:<name>' (options + start back to MWR's), per new mover 'del:<name>' (cascade: options of kept movers that
point to a deleted mover get MWR's value if they exist there, else None), 'gate' (gate order of common options -> MWR order), 'br' (same).
Measure (fast36 bin/k): flips at gate (Q, 0), C, T3, max per-gate flips, k (own36.kfvs)."""
import sys, os, json, copy
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H); sys.path.insert(0, os.path.join(H, "..", "box36"))
from named37 import to_named, from_named
import fast36, own36
SP = os.environ["SP"]
BEST = os.environ.get("BEST", os.path.join(H, "../box36/out/climb/BEST_C300_r34_C17_30d4ea76.json"))   # env BEST/NAMES: other climb best
R = to_named(json.load(open(BEST)), json.load(open(os.environ.get("NAMES", SP + "/n_r34_C17_30d4ea76.json"))))
Mw = to_named(json.load(open(os.path.join(H, "../box36/inst/MWR8_2.json"))), json.load(open(SP + "/mwr8.names")))
mwm = {m[0]: m for m in Mw["movers"]}
def merge_order(rl, ml):
    """common options in MWR order, new ones after their nearest preceding entry of rl."""
    mset = set(ml); out = [q for q in ml if q in set(rl)]
    for i, q in enumerate(rl):
        if q not in mset:
            j = i - 1
            while j >= 0 and rl[j] not in mset and rl[j] not in out: j -= 1
            pos = out.index(rl[j]) + 1 if j >= 0 and rl[j] in out else 0
            out.insert(pos, q)
    return out
def build(units):
    Nd = copy.deepcopy(R); dele = {u[4:] for u in units if u.startswith("del:")}
    ch = True
    while ch:   # cascade over wt
        ch = False
        for m in Nd["movers"]:
            if m[0] not in dele and m[0] not in mwm and any(o["wt"] in dele for o in m[2]): dele.add(m[0]); ch = True
    Nd["movers"] = [m for m in Nd["movers"] if m[0] not in dele]
    for m in Nd["movers"]:
        if "rev:" + m[0] in units: m[2] = copy.deepcopy(mwm[m[0]][2]); m[3] = mwm[m[0]][3]
        for k, o in enumerate(m[2]):
            for f in ("wt", "xt"):
                if o[f] in dele:
                    mo = mwm.get(m[0]); o[f] = mo[2][k][f] if mo and k < len(mo[2]) else None
    ex = {(m[0], k) for m in Nd["movers"] for k in range(len(m[2]))}
    for key in ("gate", "br"):
        l = Nd[key]
        if key in units: l = merge_order(l, Mw[key])
        l = [q for q in l if q in ex]
        for q in sorted(ex - set(l)): l.append(q)   # options that came back from MWR revert: append (then fixed below)
        if key in units or True:
            # place MWR-reverted options that are missing from R's list by MWR order
            pass
        Nd[key] = l
    return from_named(Nd), Nd
def measure(G):
    T, fb, rows = fast36.one(G, bindir="bin/k"); C = fast36.LASTC
    idx = {}; fq = 0; mx = max((f for q, f, l in rows), default=0)
    return dict(T3=T, C=C, maxflip=mx, rows=rows)
def qflips(G, Nd, rows):
    qi = [i for i, m in enumerate(Nd["movers"]) if m[0] == "Q"][0]
    return max([f for q, f, l in rows if tuple(q) == (qi, 0)] or [0])
if __name__ == "__main__":
    os.chdir(os.path.join(H, "../box36"))
    diffs = []
    for m in R["movers"]:
        if m[0] not in mwm: diffs.append("del:" + m[0])
        elif m[2] != mwm[m[0]][2] or (len(m[2]) > 1 and m[3] != mwm[m[0]][3]): diffs.append("rev:" + m[0])
    diffs += ["gate", "br"]
    print("units", len(diffs), diffs)
    G, Nd = build([]); r = measure(G); print("base", qflips(G, Nd, r["rows"]), r["C"], r["T3"], r["maxflip"])
    for u in diffs:
        G, Nd = build([u]); r = measure(G); k = own36.kfvs(G, 1)
        print(f"{u:12s} Qflips {qflips(G, Nd, r['rows']):3d} C {r['C']:3d} T3 {r['T3']:3d} maxflip {r['maxflip']:3d} k {k} NM {G['N'] + sum(map(len, G['opts']))}", flush=True)
