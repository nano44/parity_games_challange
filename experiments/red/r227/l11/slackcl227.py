#!/usr/bin/env python3
"""L-RED 61 R227 item 1b: own re-measure of L-LOWER 11's DATA «no realized h >= 3 tower is TIGHT» (slack steps) and the helper-sharing
counts (L11 §3 table, §4). States and o-values from L-LOWER's simulator sim6 (env LOW = a worktree of claude/l-lower b6da086e); the
counting is mine, from L11's definitions:
  F_l = #steps t with o_l(t) != o_l(t-1); caps h = the longest prefix l = 0, 1, ... with F_l = 2^(l+2) - 2 (also printed: #l with equality anywhere);
  slack steps = #t in 1..T with o_(h-1)(t) == o_(h-1)(t-1)  (L11 §3: «o(h − 1) unchanged»);
  helpers = movers of pairs >= h; moving = changes at least once; client(y) = core pairs j with a mover x of pair j and a wiring path x -> ... -> y
  whose every vertex after x is a helper (my own DFS over xt, option targets of mover z = xt[2z], xt[2z+1], -1 = exit).
Usage: LOW=<worktree> slackcl227.py GENOME.txt ..."""
import sys, os
from collections import Counter
sys.path[:0] = [os.path.join(os.environ["LOW"], "experiments/lower/l6")]
from sim6 import rd, run
for p in sys.argv[1:]:
    D = rd(p); S, O = run(D); T = len(S) - 1; d = D["d"]
    F = [sum(1 for t in range(1, T + 1) if O[t][l] != O[t - 1][l]) for l in range(d)]
    h = 0
    while h < d and F[h] == 2 ** (h + 2) - 2: h += 1
    hany = sum(1 for l in range(d) if F[l] == 2 ** (l + 2) - 2)
    slack = sum(1 for t in range(1, T + 1) if O[t][h - 1] == O[t - 1][h - 1]) if h else None
    K = 2 * h; N = 2 * d; xt = D["xt"]
    moving = [y for y in range(K, N) if any(S[t][y] != S[t - 1][y] for t in range(1, T + 1))]
    cl = {y: set() for y in range(K, N)}
    for x in range(K):
        seen = set(); stack = [w for w in (xt[2 * x], xt[2 * x + 1]) if w >= K]
        while stack:
            z = stack.pop()
            if z in seen: continue
            seen.add(z); cl[z].add(x // 2); stack += [w for w in (xt[2 * z], xt[2 * z + 1]) if w >= K]
    hist = Counter(len(cl[y]) for y in moving)
    priv = [sum(1 for y in moving if cl[y] == {j}) for j in range(h)]
    print(os.path.basename(p), "d", d, "T", T, "F", F[:h + 2], "caps(prefix)", h, "caps(any)", hany, "slack", slack,
          "moving helpers", len(moving), "by #client levels", sorted(hist.items()), "private per level", priv, flush=True)
