#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A data): the pruning distance at the FIRST best_vertices call of each search (same R = G' across
same-player searches without a dominion in between; only T grows). dist_s(v) = round in which v was pruned ("distance k:"
lines, release or debug trace, -t), INF if v survived (in V* or in the -1 return set). Checks monotonicity of dist in s.
Usage: dtl_distance.py GAME.pg TRACE"""
import sys, re
game, trace = sys.argv[1], sys.argv[2]
INF = 10**9
calls = []  # per search: (player, dist dict, best list, stable?)
cur = None; first_done = False; player = None
for line in open(trace):
    line = line.rstrip()
    m = re.match(r"iteration \d+-(even|odd)", line)
    if m: player = m.group(1); cur = {}; first_done = False; continue
    if cur is None or first_done: continue
    m = re.match(r"distance (\d+):(.*)", line)
    if m:
        for tok in m.group(2).split(): cur[int(tok[1:])] = int(m.group(1))
        continue
    m = re.match(r"best vertices:(.*)", line)
    if m:
        toks = m.group(1).split(); stable = toks and toks[-1] == "(stable)"
        best = [int(t[1:]) for t in toks if t.startswith("v")]
        calls.append((player, cur, best, stable)); first_done = True
viol = 0; ups = 0; same = 0; pairs = 0
for i in range(len(calls) - 1):
    pa, da, ba, sa = calls[i]; pb, db, bb, sb = calls[i + 1]
    if pa != pb: continue
    pairs += 1
    keys = set(da) | set(db) | set(ba) | set(bb)
    for v in keys:
        x = da.get(v, INF); y = db.get(v, INF)
        if v not in da and v not in ba: continue  # solved before search i
        if v not in db and v not in bb: continue  # solved between
        if y < x: viol += 1; print(f"  VIOLATION search {i}->{i+1} v{v}: {x} -> {y}")
        elif y > x: ups += 1
        else: same += 1
print(f"{game}: calls {len(calls)}; same-player consecutive pairs {pairs}: dist up {ups}, same {same}, DOWN {viol}")
for i, (p, d, b, s) in enumerate(calls):
    rounds = max(d.values()) if d else 0
    print(f"  search {i} {p}: rounds {rounds}, pruned {len(d)}, survivors {len(b)} {'stable' if s else '-1'}; profile " + " ".join(str(sum(1 for v in d if d[v] == k)) for k in range(1, rounds + 1)))
