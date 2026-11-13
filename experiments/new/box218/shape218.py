#!/usr/bin/env python3
"""Box 218: CEIL-SHAPE and UP-CEIL counters on upward ladders (docs/new/N5-BITLADDER-box218.md §2). Model: one217.OneP (box 217).
For every genome file: T, k, and the must-0 counters
  upceil  a mover with sw(x) > 2^(min(lev + 1, d - lev)) - 1                                             (UP-CEIL; needs an upward genome)
  shape   a degree-2 mover x with sw(x) = |K(x)| - 1 >= 3, of level k - 1, whose Xi-targets are not two distinct movers, or one of
          which has fewer than 2^(k-1) - 1 value rises, or more rises than |PXi| - 1, or a level above d - k + 1   (CEIL-SHAPE (i), (ii))
  notup   an option whose Xi-target is not on a strictly higher level (the file is then not an upward genome; upceil is not tested)
Control SHAPE218_CTRL=1: the shape test is applied to every degree-2 mover of level >= 1 (not only the full ones): shape must fire.
Usage: shape218.py G.json ..."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, "..", "box217")); import one217
CTRL = os.environ.get("SHAPE218_CTRL") == "1"
for fn in sys.argv[1:]:
    G = json.load(open(fn)); G = G.get("genome", G); N, lev, opts = G["N"], G["lev"], G["opts"]; d = max(lev) + 1
    P = one217.OneP(G); S = P.run("key"); T = len(S) - 1
    sw = [sum(1 for t in range(T) if S[t + 1][x] != S[t][x]) for x in range(N)]
    vals = [P.values(s)[0] for s in S]; rises = [sum(1 for t in range(T) if vals[t + 1][x][0] > vals[t][x][0]) for x in range(N)]
    K = [0] * N; PX = [None] * N
    for x in sorted(range(N), key=lambda x: lev[x]): K[x] = len(opts[x]) if lev[x] == 0 else sum(K[w] for (w, _, _) in opts[x])
    def px(x):
        if PX[x] is None: PX[x] = sum(1 if y < 0 else px(y) for (_, y, _) in opts[x])
        return PX[x]
    for x in range(N): px(x)
    notup = sum(1 for x in range(N) for (_, y, _) in opts[x] if y >= 0 and lev[y] <= lev[x])
    upceil = 0 if notup else sum(1 for x in range(N) if sw[x] > (1 << min(lev[x] + 1, d - lev[x])) - 1)
    shape = 0; full = []
    for x in range(N):
        if len(opts[x]) != 2 or lev[x] < 1: continue
        isfull = sw[x] == K[x] - 1 and K[x] >= 4
        if isfull: full.append(x)
        if not (isfull or CTRL): continue
        k = lev[x] + 1; y0, y1 = opts[x][0][1], opts[x][1][1]; need = (1 << (k - 1)) - 1
        bad = y0 < 0 or y1 < 0 or y0 == y1
        if not bad:
            for y in (y0, y1): bad = bad or rises[y] < need or rises[y] > PX[y] - 1 or (not notup and lev[y] > d - k + 1)
        shape += int(bad)
    print(f"{os.path.basename(fn)} d {d} N {N} T {T} k {1 + max(lev[x] for x in full) if full else (1 if any(sw[x] == 1 and lev[x] == 0 for x in range(N)) else 0)} "
          f"full {full} | upceil {upceil} shape {shape} notup {notup} ctrl {int(CTRL)}")
