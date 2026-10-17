#!/usr/bin/env python3
"""Removal-order invariant test (L-RED, R8 section 12; Lead 18:18Z): "the SET of vertices removed from R before a given
vertex only grows across same-player searches". Detector build at -t -t -t: pieces leave R as DOM blocks ("DOM top X" +
its attracted lines) or as -1 cuts ("X ∪= attracted with threshold t: v ..."); the trace order of these pieces inside
one search (all recursion depths, in order) gives, for every vertex v removed in search s, before(v, s) = the vertices
removed earlier in s. Checks before(v, s) minus solved ⊆ before(v, s') for consecutive same-player searches s < s'.
Usage: dtl_pieces.py DETOINK game.pg [--solver dtl|idtl] [--verbose]"""
import sys, re, subprocess
oink, path = sys.argv[1], sys.argv[2]; solver = "--" + (sys.argv[sys.argv.index("--solver") + 1] if "--solver" in sys.argv else "dtl")
r = subprocess.run([oink, solver, "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", "-t", path], capture_output=True, text=True, timeout=900)
out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
searches = []; cur = None; mode = None; solved = set(); solving = False
for line in out.splitlines():
    line = re.sub(r"^\[\s*[0-9.]+\]\s*", "", line)
    m = re.match(r"iteration (\d+)-(even|odd)", line)
    if m: cur = {"idx": int(m.group(1)), "player": m.group(2), "order": [], "solved_before": set(solved)}; searches.append(cur); mode = None; solving = False; continue
    if cur is None: continue
    if line.startswith("SOLVE attractor"): solving = True; mode = None; continue
    if line.startswith("dominion"): solved.update(v for v in re.findall(r"(\S+)", line.split(")", 2)[-1]) if "->" not in v); solved.update(a for a, b in re.findall(r"(\S+)->(\S+)", line)); continue
    if solving:
        m2 = re.match(r"attracted (\S+) by", line)
        if m2: solved.add(m2.group(1))
        continue
    if line.startswith("DOM top "): mode = "dom"; cur["order"].append(line.split()[2]); continue
    if line.startswith("SPTL top ") or line.startswith("best vertices") or line.startswith("REGION top") or line.startswith("current region"): mode = None
    if "attracted with threshold" in line:
        vs = line.split(":", 1)[1].split(); cur["order"].extend(vs); mode = None; continue
    if mode == "dom":
        m2 = re.match(r"attracted (\S+) by", line)
        if m2: cur["order"].append(m2.group(1))
for s_ in searches:        # first removal occurrence per vertex only (the recursion re-lists vertices of Z)
    seen_ = set(); dedup = []
    for v in s_["order"]:
        if v not in seen_: seen_.add(v); dedup.append(v)
    s_["order"] = dedup
viol = 0; pairs = 0; examples = []
for a, b in zip(searches, searches[1:]):
    if a["player"] != b["player"]: continue
    pairs += 1
    posb = {v: i for i, v in enumerate(b["order"])}; sol = b["solved_before"]
    seen = set()
    for v in a["order"]:
        if v in posb and v not in sol:
            before_a = seen - sol; before_b = set(b["order"][:posb[v]])
            lost = before_a - before_b
            if lost:
                viol += 1
                if len(examples) < 5: examples.append(f"s{a['idx']}->s{b['idx']}: {v} removed after {sorted(lost)[:6]} in s{a['idx']} but before them in s{b['idx']}")
        seen.add(v)
print(f"{path.split('/')[-1]} {solver}: searches {len(searches)}, same-player pairs {pairs}, removed per search {[len(s_['order']) for s_ in searches][:8]}, "
      f"violations of 'removed-before set only grows': {viol}")
if "--verbose" in sys.argv:
    for e in examples: print("  ", e)
