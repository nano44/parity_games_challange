#!/usr/bin/env python3
"""FIB staircase genome (L-SI box 90). Letters c_1 < ... < c_d = e-faces of level-1 Odd nodes q_j (W-target u_j, Xi-target a clock-lane node).
A clock lane a_1..a_m (Even, -> next or -> X) reaches an Even-winning loop W; q_j's beta face points into it, so Odd's e-exit at q_j becomes
forced at time ~ s*j. v picks among q_j. u_j (W-target of c_j) chooses X or delay lanes to q_(j-2), q_(j-1).
WINDOW k: u_j has lanes to q_(j-k), ..., q_(j-1) (k = 2 is the FIB staircase); stage length s = k + 1; lane to q_(j-i) has
length s*i + (k - i + 1), so the low digits enter in the order c_(j-k), ..., c_(j-1), one per step, after c_j.
Usage: gen90.py d [k] [off] > G.json   (names map on stderr)"""
import sys, json
d = int(sys.argv[1]); k = int(sys.argv[2]) if len(sys.argv) > 2 else 2; s = k + 1
off = int(sys.argv[3]) if len(sys.argv) > 3 else 2
mv = []                       # list of dicts: name, lev, opts [(wt name|None, xt name|None, kind)], start
def M(name, lev, opts, start=0): mv.append(dict(name=name, lev=lev, opts=opts, start=start))
M("W", 0, [(None, "W", "win")])
m = s * d + off + 2
for i in range(1, m + 1):
    M(f"a{i}", 0, [(None, f"a{i+1}" if i < m else "W", "lo"), (None, None, ("hiX", 0, i))], start=1)
def lane(tag, L, target):
    for i in range(1, L + 1):
        M(f"{tag}_{i}", 0, [(None, f"{tag}_{i+1}" if i < L else target, "lo"), (None, None, ("hiX", 1, (tag, i)))], start=1)
    return f"{tag}_1" if L > 0 else target
for j in range(1, d + 1):
    # clock attach: a_i is Even-winning from time ~ m - i + 1; want q_j available at time s*j + off
    ai = max(1, m - (s * j + off) + 1)
    M(f"q{j}", 1, [(f"u{j}", f"a{ai}", ("q", j))])
for j in range(1, d + 1):
    opts = [(None, None, ("hiX", 2, j))]
    for i in range(k, 0, -1):
        if j - i >= 1: opts.append((None, lane(f"L{j}_{i}", s * i + (k - i + 1), f"q{j-i}"), "lo"))
    M(f"u{j}", 0, opts, start=0)
M("v", 0, [(None, f"q{j}", "lo") for j in range(1, d + 1)], start=0)
idx = {x["name"]: i for i, x in enumerate(mv)}
N = len(mv); opts = []; gate = []; lev = []; start = []; kinds = []
g = 0
for x in mv:
    lev.append(x["lev"]); start.append(x["start"]); o = []; gt = []
    for (wt, xt, kind) in x["opts"]:
        o.append([idx[wt] if wt else -1, idx[xt] if xt else -1, len(kinds)]); kinds.append(kind); gt.append(None)
    opts.append(o); gate.append(gt)
# gate indices: level-1 q_j in order of j (e-order); others arbitrary distinct
order = sorted(((x, k) for x in range(N) for k in range(len(opts[x]))), key=lambda q: (lev[q[0]], mv[q[0]]["name"].startswith("q") and int(mv[q[0]]["name"][1:]) or 0, q))
for gi, (x, k) in enumerate(order): gate[x][k] = gi
# beta ranks: lo (even, lowest), q (odd), win (even), hiX (even, highest): class 2 (u) > class 1 (lanes; decreasing along a lane) > class 0 (clock, decreasing)
B = len(kinds)
def key(b):
    k = kinds[b]
    if k == "lo": return (0, b)
    if k == "win": return (1, 0)
    if isinstance(k, tuple) and k[0] == "q": return (2, k[1])
    c, pos = k[1], k[2]
    if c == 0: return (3, -pos)
    if c == 1: return (4, str(pos[0]), -pos[1])
    return (5, pos)
rank = sorted(range(B), key=key); br = [0] * B
for r, b in enumerate(rank): br[b] = r
bp = [1 if isinstance(kinds[b], tuple) and kinds[b][0] == "q" else 0 for b in range(B)]
G = dict(N=N, lev=lev, opts=opts, gate=gate, br=br, bp=bp, start=start)
json.dump(G, sys.stdout); print()
json.dump({mv[i]["name"]: i for i in range(N)}, sys.stderr)
