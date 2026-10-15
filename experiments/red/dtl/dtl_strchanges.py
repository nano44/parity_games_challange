#!/usr/bin/env python3
"""GAP-A measurement (L-RED, R8 section 12; Lead 17:36Z): strategy changes of Even vertices at a FIXED sptl region vertex
set across searches. Needs the detector build (scratchpad oink-det: dtl.cpp with "SPTL top X", "DOM top X", "SOLVE
attractor" markers, REGION lines) run at -t -t -t: every sptl region is the block from "SPTL top X" to its "REGION top X"
line; its vertex set = top + the "attracted v by p (via w | forced | via tangle t)" lines in the block; an Even vertex's
strategy is w, or the strategy recorded in tangle t ("new tangle ... v->w" lines, tangles numbered in creation order).
For every (top, region vertex set) seen more than once, counts per Even vertex how often its strategy differs from its
previous occurrence at the same (top, set). Usage: dtl_strchanges.py DETOINK game.pg [--solver dtl|idtl]"""
import sys, re, subprocess, collections


def measure(out):
    """returns (regions, seen, changes, occ, sets_per_top) from a cleaned -t -t -t trace of the detector build"""
    tangles = {}          # tangle id -> {even vertex: strategy}
    block = None; regions = []   # (top, frozenset(vertices), {even vertex: str})
    for line in out.splitlines():
        line = re.sub(r"^\[\s*[0-9.]+\]\s*", "", line)
        m = re.match(r"new tangle \d+ \((\d+)\) \(depth \d+\) (.*) with \d+ escape", line)
        if m:
            tangles[int(m.group(1))] = {a: b for a, b in re.findall(r"(\S+)->(\S+)", m.group(2))}; continue
        if line.startswith("SPTL top "):
            block = {"top": line.split()[2], "vs": {line.split()[2]}, "str": {}}; continue
        if line.startswith("DOM top") or line.startswith("SOLVE attractor") or line.startswith("best vertices") or line.startswith("iteration") or line.startswith("current region"):
            block = None; continue
        if block is not None:
            m = re.match(r"attracted (\S+) by [01] \((.*)\)", line)
            if m:
                v, how = m.group(1), m.group(2); block["vs"].add(v)
                if how.startswith("via tangle"):
                    t = int(how.split()[-1]); 
                    if v in tangles.get(t, {}): block["str"][v] = tangles[t][v]
                elif how.startswith("via "): block["str"][v] = how[4:]
                continue
            if line.startswith("REGION top "):
                regions.append((block["top"], frozenset(block["vs"]), block["str"])); block = None
    seen = {}; changes = collections.Counter(); occ = collections.Counter(); sets_per_top = collections.defaultdict(set)
    for top, vs, st in regions:
        key = (top, vs); sets_per_top[top].add(vs); occ[key] += 1
        if key in seen:
            for v, w in st.items():
                if v in seen[key] and seen[key][v] != w: changes[(key, v)] += 1
            seen[key] = {**seen[key], **st}
        else: seen[key] = dict(st)
    return regions, seen, changes, occ, sets_per_top


if __name__ == "__main__":
    oink, path = sys.argv[1], sys.argv[2]; solver = "--" + (sys.argv[sys.argv.index("--solver") + 1] if "--solver" in sys.argv else "dtl")
    r = subprocess.run([oink, solver, "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", "-t", path], capture_output=True, text=True, timeout=600)
    out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
    regions, seen, changes, occ, sets_per_top = measure(out)
    n = len(set(v for _, vs, _ in regions for v in vs))
    mx = max(changes.values(), default=0)
    worst = max(changes, key=changes.get) if changes else None
    print(f"{path.split('/')[-1]} {solver}: {len(regions)} sptl regions, {len(seen)} distinct (top, set) pairs, repeated pairs {sum(1 for k in occ if occ[k] > 1)}, "
          f"max repeats of one pair {max(occ.values(), default=0)}, max distinct sets at one top {max((len(v) for v in sets_per_top.values()), default=0)}, "
          f"strategy changes at a fixed (top, set): total {sum(changes.values())}, max per vertex {mx}" + (f" (top {worst[0][0]}, vertex {worst[1]}, set size {len(worst[0][1])})" if worst else ""))
