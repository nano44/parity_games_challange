#!/usr/bin/env python3
"""L-RED box 10 (produced on Opus 5.5): abstract model of the inversion relay (R39 section 1) scored with the SAME depth rule as
L-ALG's dtl_stealdepth.analyze (re-implemented on the abstract records; prediction only, not a measurement). Levels
j = -1..D at steps k_{-1} < k_0 < ... (one round, descending tops). At visit x: hold h_j(x) = F_{j-1}(x) (w_j joins
k_{j-1}'s region when t_{j-1} fires), freeze g_j(x) = [x >= j + OFF] (v_j joins the clock region). F_j(x) = avail(x) and
not (h_j or g_j); excluded = avail and (h_j or g_j). Prints the event list with depths and the max depth.
Usage: relaymodel.py D [OFF] [VISITS]"""
import sys
D = int(sys.argv[1]); OFF = int(sys.argv[2]) if len(sys.argv) > 2 else 3; NV = int(sys.argv[3]) if len(sys.argv) > 3 else D + OFF + 3
L = list(range(-1, D + 1)); avail = lambda x: x >= 1
F, P = {}, {}                                          # F[j][x]; P[j][x] = prefix ∩ t_j as a set of names
for j in L:
    F[j], P[j] = [], []
    for x in range(NV):
        h = j > -1 and F[j - 1][x]; gz = x >= j + OFF
        P[j].append({n for n, c in (("w", h), ("v", gz)) if c})
        F[j].append(avail(x) and not (h or gz))
ev = []
for x in range(NV - 1):
    for j in L:
        if F[j][x] and avail(x + 1) and P[j][x + 1]: ev.append((x, j))
depth, last = {}, {}
for e in ev:
    i, j = e
    if j not in last: depth[e] = 0; last[j] = i; continue
    pj = last[j]; last[j] = i
    shr = [m for m in range(pj + 1, i) if P[j][m] - P[j][m + 1]]
    cs = [depth[c] for c in ev if c[0] in shr and c[1] < j and depth.get(c) is not None]   # c[1] < j: earlier step
    depth[e] = 1 + min(cs) if cs else None
for j in L: print(f"level {j:2d} fires", "".join("F" if f else ("X" if avail(x) else ".") for x, f in enumerate(F[j])))
print("events (pair, level, depth):", [(e[0], e[1], depth[e]) for e in ev])
print("max depth", max([v for v in depth.values() if v is not None], default=0))
