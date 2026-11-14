#!/usr/bin/env python3
"""L-SI box 90: MULTIPLICITY family MW(n, L): m(y, z) = n at the race vertex R.
High letters h_1 < ... < h_n (level-1 one-option movers qh_k, W-target a dead sink D, Xi-target a clock-lane node: h_k arrives at state s*k + off).
Low letter z (level-1 qz, W-target u, Xi-target the Even-winning loop W, so Odd always exits by e_z): u has an X-option and, for each k, a delay
lane of length L to qh_k, so «z then h_k» is offered L + 1 steps after h_k arrives.
v and R pick among qh_k and qz; R also has the race option to Q (level-1, the least relevant letter y, W-target hv -> v, Xi-target R).
Per stage, R's tops are h_k, y, z, y: y re-enters under every re-entry of z (m(y, z) = n), and z is re-armed by every h_k.
Letter order (level 1, gate rank): y < z < h_1 < ... < h_n.  Usage: genm90.py n [L] > G.json (names on stderr)"""
import sys, json
n = int(sys.argv[1]); L = int(sys.argv[2]) if len(sys.argv) > 2 else 2; s = L + 4; off = 2
mv = []
def M(name, lev, opts, start=0, grank=None): mv.append(dict(name=name, lev=lev, opts=opts, start=start, grank=grank))
M("W", 0, [(None, "W", "win")]); M("D", 0, [(None, None, ("hiX", 3, 0))])
m = s * n + off + 2
for i in range(1, m + 1):
    M(f"a{i}", 0, [(None, f"a{i+1}" if i < m else "W", "lo"), (None, None, ("hiX", 0, i))], start=1)
for k in range(1, n + 1):
    M(f"qh{k}", 1, [("D", f"a{max(1, m - (s * k + off) + 1)}", ("q", k))], grank=2 + k)
M("qz", 1, [("u", "W", ("q", 0))], grank=1)
uo = [(None, None, ("hiX", 2, 0))]
for k in range(1, n + 1):
    for i in range(1, L + 1):
        M(f"b{k}_{i}", 0, [(None, f"b{k}_{i+1}" if i < L else f"qh{k}", "lo"), (None, None, ("hiX", 1, (k, i)))], start=1)
    uo.append((None, f"b{k}_1" if L > 0 else f"qh{k}", "lo"))
M("u", 0, uo)
M("v", 0, [(None, f"qh{k}", "lo") for k in range(1, n + 1)] + [(None, "qz", "lo")])
M("hv", 0, [(None, "v", "lo")])
M("Q", 1, [("hv", "R", ("qodd", 0))], grank=0)
M("R", 0, [(None, "Q", "race")] + [(None, f"qh{k}", "lo") for k in range(1, n + 1)] + [(None, "qz", "lo")])
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
    if k[0] == "qodd": return (2, 0)
    if k[0] == "q": return (2, 1 + k[1])
    if k == "race": return (3, 0)
    c, pos = k[1], k[2]
    return (4 + c, -pos if c == 0 else (pos if c != 1 else (pos[0], -pos[1])))
rank = sorted(range(len(kinds)), key=key); br = [0] * len(kinds)
for r, b in enumerate(rank): br[b] = r
bp = [1 if isinstance(kinds[b], tuple) and kinds[b][0] in ("q", "qodd") else 0 for b in range(len(kinds))]
json.dump(dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start), sys.stdout); print()
json.dump(idx, sys.stderr)
