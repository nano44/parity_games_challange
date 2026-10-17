#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A data): fixed-context monotonicity. From a PATCHED-debug trace (`-t -t -t`, distance lines kept),
every depth-0 best_vertices call is recorded with its context R (unsolved vertices not yet removed in this search), its result
(stable / -1), the returned V and the pruning distance of every vertex (INF = survivor). Calls with the SAME R in different
same-player searches are compared in search order: as T grows, distances should not decrease, stable should not revert to -1,
and a stable V* should not lose vertices. Usage: dtl_contexts.py GAME.pg TRACE"""
import sys, re, collections
game, trace = sys.argv[1], sys.argv[2]
INF = 10**9
def vid(tok): return int(tok.split("->")[0][1:])
calls = []   # (search, player, frozenset R, kind, frozenset V, dist dict)
search = -1; player = None; depth = -1; unsolved = set(); removed = set(); dist = {}; mode = None
for line in open(trace):
    line = line.rstrip()
    m = re.match(r"iteration \d+-(even|odd)", line)
    if m: search += 1; player = m.group(1); depth = -1; removed = set(); dist = {}; continue
    m = re.match(r"ENTER depth (\d+)", line)
    if m: depth = int(m.group(1)); continue
    m = re.match(r"EXIT depth (\d+)", line)
    if m: depth = int(m.group(1)) - 1; continue
    m = re.match(r"current region:(.*)", line)
    if m and depth == 0 and not removed: unsolved = set(vid(t) for t in m.group(1).split()); continue
    if depth != 0: continue
    m = re.match(r"distance (\d+):(.*)", line)
    if m:
        for t in m.group(2).split(): dist[vid(t)] = int(m.group(1))
        continue
    if line.startswith("best vertices"):
        V = frozenset(int(t[1:]) for t in line.split()[2:] if t.startswith("v"))
        R = frozenset(unsolved - removed)
        calls.append((search, player, R, "S" if line.endswith("(stable)") else "m", V, dict(dist)))
        dist = {}; mode = "pending"; continue
    if line.startswith("X ∪= DomStable"): mode = "dom"; continue
    if line.startswith("X ∪= Dom(V)"): mode = "dis"; continue
    m = re.match(r"X ∪= attracted with threshold (\d+):(.*)", line)
    if m: removed |= set(vid(t) for t in m.group(2).split()); mode = None; continue
    m = re.match(r"domregion (\d+) (.*)", line)
    if m and mode == "dom": removed |= set(vid(t) for t in m.group(2).split()); continue
    m = re.match(r"region (\d+)(.*)", line)
    if m and mode == "dis": removed |= set(vid(t) for t in m.group(2).split()); continue
by_ctx = collections.defaultdict(list)
for c in calls: by_ctx[(c[1], c[2])].append(c)
recur = 0; pairs = 0; d_down = 0; d_up = 0; revert = 0; v_lost = 0; v_gain = 0; m_to_s = 0; mset_change = 0
for key, L in by_ctx.items():
    if len(L) < 2: continue
    recur += 1
    for a, b in zip(L, L[1:]):
        pairs += 1
        R = key[1]
        for v in R:
            x = a[5].get(v, INF); y = b[5].get(v, INF)
            if y < x: d_down += 1
            elif y > x: d_up += 1
        if a[3] == "S" and b[3] == "m": revert += 1
        if a[3] == "m" and b[3] == "S": m_to_s += 1
        if a[3] == "S" and b[3] == "S":
            v_lost += len(a[4] - b[4]); v_gain += len(b[4] - a[4])
        if a[3] == "m" and b[3] == "m" and a[4] != b[4]: mset_change += 1
# nested contexts: a later same-player call with R' a strict subset of an earlier call's R (any searches, not only consecutive)
nd_up = nd_down = nd_pairs = nd_revert = nd_lost = 0
for i, a in enumerate(calls):
    for b in calls[i + 1:]:
        if b[1] != a[1] or b[0] == a[0] or not (b[2] < a[2]): continue
        nd_pairs += 1
        for v in b[2]:
            x = a[5].get(v, INF); y = b[5].get(v, INF)
            if y < x: nd_down += 1
            elif y > x: nd_up += 1
        if a[3] == "S" and b[3] == "m": nd_revert += 1
        if a[3] == "S" and b[3] == "S": nd_lost += len((a[4] & b[2]) - b[4])
print(f"  nested contexts R' ⊂ R (later search): pairs {nd_pairs} | distances on R': up {nd_up}, DOWN {nd_down} | stable→−1 {nd_revert} | stable V* ∩ R' lost {nd_lost}")
print(f"{game}: depth-0 calls {len(calls)}, distinct (player, R) contexts {len(by_ctx)}, recurring {recur}, consecutive pairs {pairs} | distances: up {d_up}, DOWN {d_down} | stable->-1 reverts {revert}, -1->stable {m_to_s}, -1 set changed {mset_change} | stable V*: gained {v_gain}, LOST {v_lost}")
