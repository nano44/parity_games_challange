#!/usr/bin/env python3
"""L-SI box 90 route (ii): WAITING-HIGH chain WC(n, L). High letters h_1 < ... < h_n (level-1 qh_k). h_1 is free (beta -> Even-winning loop W).
For k >= 2, qh_k's beta face points to v, and h_(k-1)'s W-target D_(k-1) (Even: -> X, or -> qh_k) leads into qh_k: once v's play runs through
h_(k-1) and on into qh_k, the beta face closes a cycle through v that carries e(h_(k-1)) (Even-winning), so Odd must exit by e(h_k): h_k
is unlocked only by v's own play, i.e. it WAITS for v. The low letter z (qz, beta -> W, W-target u; u has an X option and a lane of length L
to every qh_k) is the low race. No clock. Usage: genw90.py n [L] > G.json (names on stderr)"""
import sys, json
n = int(sys.argv[1]); L = int(sys.argv[2]) if len(sys.argv) > 2 else 2
mv = []
def M(name, lev, opts, start=0, grank=None): mv.append(dict(name=name, lev=lev, opts=opts, start=start, grank=grank))
M("W", 0, [(None, "W", "win")])
for k in range(1, n + 1):
    M(f"D{k}", 0, [(None, None, ("hiX", 3, k))] + ([(None, f"qh{k+1}", "lo")] if k < n else []))
    M(f"qh{k}", 1, [(f"D{k}", "W" if k == 1 else "v", ("q", k))], grank=2 + k)
M("qz", 1, [("u", "W", ("q", 0))], grank=1)
uo = [(None, None, ("hiX", 2, 0))]
for k in range(1, n + 1):
    for i in range(1, L + 1):
        M(f"b{k}_{i}", 0, [(None, f"b{k}_{i+1}" if i < L else f"qh{k}", "lo"), (None, None, ("hiX", 1, (k, i)))], start=1)
    uo.append((None, f"b{k}_1" if L > 0 else f"qh{k}", "lo"))
M("u", 0, uo)
M("v", 0, [(None, f"qh{k}", "lo") for k in range(1, n + 1)] + [(None, "qz", "lo"), (None, None, ("hiX", 4, 0))], start=0)
idx = {x["name"]: i for i, x in enumerate(mv)}; N = len(mv)
opts, gate, lev, start, kinds = [], [], [], [], []
for x in mv:
    lev.append(x["lev"]); start.append(x["start"]); o = []
    for (wt, xt, kind) in x["opts"]:
        o.append([idx[wt] if wt else -1, idx[xt] if xt else -1, len(kinds)]); kinds.append(kind)
    opts.append(o); gate.append([None] * len(o))
order = sorted(((x, k) for x in range(N) for k in range(len(opts[x]))), key=lambda q: (lev[q[0]], mv[q[0]]["grank"] or 0, q))
for gi, (x, k) in enumerate(order): gate[x][k] = gi
def key(b):
    k = kinds[b]
    if k == "lo": return (0, b)
    if k == "win": return (1, 0)
    if k[0] == "q": return (2, k[1])
    c, pos = k[1], k[2]
    return (4 + c, pos if c != 1 else (pos[0], -pos[1]))
rank = sorted(range(len(kinds)), key=key); br = [0] * len(kinds)
for r, b in enumerate(rank): br[b] = r
bp = [1 if isinstance(kinds[b], tuple) and kinds[b][0] == "q" else 0 for b in range(len(kinds))]
json.dump(dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start), sys.stdout); print()
json.dump(idx, sys.stderr)
