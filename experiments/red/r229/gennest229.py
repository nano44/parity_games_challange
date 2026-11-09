#!/usr/bin/env python3
"""L-RED 63 R229 item 7: COPY of L-SI gennest94.py (claude/l-si b1684cc6) with two extra LINK values (NON-common suffixes):
  Db : level j's High k has W-target level (j-1)'s delay-lane head b{k}_1 (-> qh_k of level j-1): each High reads a DIFFERENT lower High;
  Dbr: the same with the pairing reversed (High k -> lower b{n+1-k}_1).
Everything else is gennest94 unchanged (LINK unset / other values reproduce it byte for byte).
L-SI box 94: NESTED MW. Copies of box 90's MW(n, L) (genm90.py) at levels 1..H (prefix «l<j>_»), sharing the Even-winning loop W.
Level j's letters are more relevant than level j-1's (gate rank offset 100·j; env REV=1: LESS relevant, offset −100·j; same structure inside a level: y < z < h_1 < ... < h_n).
LINK (env, default "u"): how level j's counter reads level j-1:
  u : level j's race mover u_j gets one extra option -> level j-1's race gate mover qz_(j-1)  (u_j's value then changes when qz_(j-1)'s does)
  R : u_j gets an extra option -> level j-1's hub R_(j-1)
  D : level j's Highs' W-target D (dead sink) is replaced by level j-1's hub R_(j-1)  (the High's e-face continuation is the lower hub)
  Dz: level j's Highs' W-target is level j-1's race gate mover qz_(j-1)
  zR: level j's qz W-target is R_(j-1) instead of u_j (the race gate's continuation is the lower hub)
  v : level j's v_j (the e-face continuation of the race gate Q_j, via hv_j) gets an extra option -> R_(j-1)   [MW's flipping gate is Q_j]
  vQ: v_j gets an extra option -> Q_(j-1)
Clock: each level has its own clock lane; level j's Highs arrive with period s·SCALE^(j-1) (env SCALE, default 1) after OFFJ·(j-1).
DBL (env): levels 2..H are DOUBLER gadgets (v_j -> R_(j-1); hv_j -> v_j; gate Q_j: W-target hv_j, Xi-target R_j; R_j: race -> Q_j,
  plus -> v_j (DBL=v), -> R_(j-1) (DBL=p) or both (DBL=b)); DREL = grank step of y_j.
Usage: gennest94.py H n [L] > G.json (names on stderr).  H = 1 and LINK irrelevant reproduces genm90.py n L byte for byte."""
import sys, json, os
H = int(sys.argv[1]); n = int(sys.argv[2]); L = int(sys.argv[3]) if len(sys.argv) > 3 else 2
LINK = os.environ.get("LINK", "u"); SCALE = int(os.environ.get("SCALE", "1")); OFFJ = int(os.environ.get("OFFJ", "0"))
s = L + 4; off = 2
mv = []
def M(name, lev, opts, start=0, grank=None): mv.append(dict(name=name, lev=lev, opts=opts, start=start, grank=grank))
M("W", 0, [(None, "W", "win")])
def P(j, x): return x if j == 1 else f"l{j}_{x}"
DBL = os.environ.get("DBL", "")          # "" | "v" (R_j alt -> v_j) | "p" (R_j alt -> R_(j-1)) | "b" (both)
DREL = int(os.environ.get("DREL", "0"))   # grank offset of doubler j's letter y_j: DREL * j (negative: below level 1's y)
for j in range(1, H + 1):
    if DBL and j > 1:
        M(P(j, "v"), 0, [(None, P(j - 1, "R"), "lo")])
        M(P(j, "hv"), 0, [(None, P(j, "v"), "lo")])
        M(P(j, "Q"), 1, [(P(j, "hv"), P(j, "R"), ("qodd", j))], grank=DREL * j)
        ro = [(None, P(j, "Q"), ("race", j))]
        if DBL in ("v", "b"): ro.append((None, P(j, "v"), "lo"))
        if DBL in ("p", "b"): ro.append((None, P(j - 1, "R"), "lo"))
        M(P(j, "R"), 0, ro)
        continue
    sj = s * SCALE ** (j - 1); o2 = off + OFFJ * (j - 1); g0 = (-100 if os.environ.get("REV") else 100) * (j - 1)
    M(P(j, "D"), 0, [(None, None, ("hiX", 3, (j, 0)) if j > 1 else ("hiX", 3, 0))])
    m = sj * n + o2 + 2
    for i in range(1, m + 1):
        M(P(j, f"a{i}"), 0, [(None, P(j, f"a{i+1}") if i < m else "W", "lo"), (None, None, ("hiX", 0, i) if j == 1 else ("hiX", 0, (j, i)))], start=1)
    hw = P(j, "D")
    if j > 1 and LINK == "D": hw = P(j - 1, "R")
    if j > 1 and LINK == "Dz": hw = P(j - 1, "qz")
    for k in range(1, n + 1):
        if j > 1 and LINK in ("Db", "Dbr"): hw = P(j - 1, f"b{k if LINK == 'Db' else n + 1 - k}_1")
        M(P(j, f"qh{k}"), 1, [(hw, P(j, f"a{max(1, m - (sj * k + o2) + 1)}"), ("q", k) if j == 1 else ("q", (j, k)))], grank=g0 + 2 + k)
    zw = P(j - 1, "R") if (j > 1 and LINK == "zR") else P(j, "u")
    M(P(j, "qz"), 1, [(zw, "W", ("q", 0) if j == 1 else ("q", (j, 0)))], grank=g0 + 1)
    uo = [(None, None, ("hiX", 2, 0) if j == 1 else ("hiX", 2, (j, 0)))]
    for k in range(1, n + 1):
        for i in range(1, L + 1):
            M(P(j, f"b{k}_{i}"), 0, [(None, P(j, f"b{k}_{i+1}") if i < L else P(j, f"qh{k}"), "lo"),
                                     (None, None, ("hiX", 1, (k, i)) if j == 1 else ("hiX", 1, (100 * j + k, i)))], start=1)
        uo.append((None, P(j, f"b{k}_1") if L > 0 else P(j, f"qh{k}"), "lo"))
    if j > 1 and LINK == "u": uo.append((None, P(j - 1, "qz"), "lo"))
    if j > 1 and LINK == "R": uo.append((None, P(j - 1, "R"), "lo"))
    M(P(j, "u"), 0, uo)
    vo = [(None, P(j, f"qh{k}"), "lo") for k in range(1, n + 1)] + [(None, P(j, "qz"), "lo")]
    if j > 1 and LINK == "v": vo.append((None, P(j - 1, "R"), "lo"))
    if j > 1 and LINK == "vQ": vo.append((None, P(j - 1, "Q"), "lo"))
    M(P(j, "v"), 0, vo)
    M(P(j, "hv"), 0, [(None, P(j, "v"), "lo")])
    M(P(j, "Q"), 1, [(P(j, "hv"), P(j, "R"), ("qodd", 0) if j == 1 else ("qodd", j))], grank=g0)
    M(P(j, "R"), 0, [(None, P(j, "Q"), "race" if j == 1 else ("race", j))] + [(None, P(j, f"qh{k}"), "lo") for k in range(1, n + 1)] + [(None, P(j, "qz"), "lo")])
# H = 1 must reproduce genm90 byte for byte: genm90 creates W, D, a-lane, ... in that order (as here for j = 1).
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
    if k == "lo": return (0, 0, b)
    if k == "win": return (1, 0, 0)
    if k[0] == "qodd": return (2, 0, k[1])
    if k[0] == "q": return (2, 1, k[1]) if isinstance(k[1], int) else (2, 1 + k[1][0] * 1000, k[1][1])
    if k == "race": return (3, 0, 0)
    if k[0] == "race": return (3, k[1], 0)
    c, pos = k[1], k[2]
    if isinstance(pos, tuple) and c != 1: return (4 + c, pos[0], pos[1] if c != 0 else -pos[1])
    if c == 0: return (4, 0, -pos)
    if c == 1: return (5, pos[0], -pos[1])
    return (4 + c, 0, pos)
rank = sorted(range(len(kinds)), key=key); br = [0] * len(kinds)
for r, b in enumerate(rank): br[b] = r
bp = [1 if isinstance(kinds[b], tuple) and kinds[b][0] in ("q", "qodd") else 0 for b in range(len(kinds))]
json.dump(dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start), sys.stdout); print()
json.dump(idx, sys.stderr)
