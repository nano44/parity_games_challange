#!/usr/bin/env python3
"""L-ALG (2026-10-16, GAP-A, Lead's budget candidates): from a PATCHED-debug trace WITH the `attracted ... via tangle k` lines
(-t -t -t, do not filter), per search: F_s = set of tangle ids that fire during the FIRST best_vertices call (R = G'), and the
first-call result signature; reports whether F_s grows monotonically, how many piece-0 changes there are and whether each is
accompanied by a new first-call firing (the CARRY statement), and the number of distinct depth-0 (context, result) pairs vs
searches (the trivial bound searches <= #pairs). Usage: dtl_firing.py GAME.pg TRACE"""
import sys, re, collections
game, trace = sys.argv[1], sys.argv[2]
def vid(tok): return int(tok.split("->")[0][1:])
searches = []  # dicts: player, F (set), sig (first call result), pairs (list of (R, kind, V))
cur = None; depth = -1; first_done = False; fired = set(); unsolved = set(); removed = set(); mode = None; dist = {}
for line in open(trace):
    line = re.sub(r"^\[ *[0-9.]*\] ", "", line.rstrip())
    m = re.match(r"iteration \d+-(even|odd)", line)
    if m:
        cur = {"player": m.group(1), "F": set(), "pairs": [], "sig": None}; searches.append(cur); depth = -1; first_done = False; fired = set(); removed = set(); dist = {}; continue
    if cur is None: continue
    m = re.match(r"ENTER depth (\d+)", line)
    if m: depth = int(m.group(1)); continue
    m = re.match(r"EXIT depth (\d+)", line)
    if m: depth = int(m.group(1)) - 1; continue
    m = re.match(r"current region:(.*)", line)
    if m and depth == 0 and not removed: unsolved = set(vid(t) for t in m.group(1).split()); continue
    m = re.search(r"via tangle (\d+)", line)
    if m:
        if depth == 0 and not first_done: fired.add(int(m.group(1)))
        continue
    if depth != 0: continue
    m = re.match(r"distance (\d+):(.*)", line)
    if m:
        for t in m.group(2).split(): dist[vid(t)] = int(m.group(1))
        continue
    if line.startswith("best vertices"):
        V = frozenset(int(t[1:]) for t in line.split()[2:] if t.startswith("v")); kind = "S" if line.endswith("(stable)") else "m"
        R = frozenset(unsolved - removed)
        cur["pairs"].append((R, kind, V, frozenset(dist.items())))
        if not first_done: cur["F"] = set(fired); cur["sig"] = (kind, V, frozenset(dist.items())); first_done = True
        dist = {}; mode = "pending"; continue
    if line.startswith("X ∪= DomStable"): mode = "dom"; continue
    if line.startswith("X ∪= Dom(V)"): mode = "dis"; continue
    m = re.match(r"X ∪= attracted with threshold (\d+):(.*)", line)
    if m: removed |= set(vid(t) for t in m.group(2).split()); mode = None; continue
    m = re.match(r"domregion (\d+) (.*)", line)
    if m and mode == "dom": removed |= set(vid(t) for t in m.group(2).split()); continue
    m = re.match(r"region (\d+)(.*)", line)
    if m and mode == "dis": removed |= set(vid(t) for t in m.group(2).split()); continue
# analysis per phase (same player, consecutive)
nonmono = 0; p0_changes = 0; p0_changes_with_new_fire = 0; allF = set()
for a, b in zip(searches, searches[1:]):
    if a["player"] != b["player"]: continue
    if not (a["F"] <= b["F"]): nonmono += 1
    if a["sig"] != b["sig"]:
        p0_changes += 1
        if b["F"] - a["F"]: p0_changes_with_new_fire += 1
for s in searches: allF |= s["F"]
pairs = set()
for s in searches:
    for R, kind, V, d in s["pairs"]: pairs.add((s["player"], R, kind, V))
pairs_full = set()
for s in searches:
    for R, kind, V, d in s["pairs"]: pairs_full.add((s["player"], R, kind, V, d))
print(f"{game}: searches {len(searches)} | first-call firing sets: non-monotone steps {nonmono}, |union| {len(allF)}, sizes {[len(s['F']) for s in searches]} | piece-0 changes {p0_changes}, of which with a NEW first-call firing {p0_changes_with_new_fire} | distinct depth-0 (context, result) pairs {len(pairs)} (with distances {len(pairs_full)}) vs searches {len(searches)}")
