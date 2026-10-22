#!/usr/bin/env python3
"""(M-cross) and deletion-route measurement (L-RED, R8 section 12; Lead 17:53Z; proof lane DTL-proof.md 3(a) Lemma S).
Detector build at -t -t -t. First piece of a search = the sptl blocks between the first stable "best vertices" line and
the first "DOM top" marker; per top the LAST pass's region of that piece. Across consecutive same-player searches checks:
(A) first-piece top set only grows (minus solved vertices); (B) each top's region contains its earlier region minus solved;
(C) heads (the first-piece top holding a vertex) never move down (to a lower-priority top). Also counts DELETE events,
new tangles learned at a (top, set) pair seen before, and attributes them to searches after a deletion.
Usage: dtl_mcross.py DETOINK game.pg [--solver dtl|idtl] [--verbose]"""
import sys, re, subprocess, collections
oink, path = sys.argv[1], sys.argv[2]; solver = "--" + (sys.argv[sys.argv.index("--solver") + 1] if "--solver" in sys.argv else "dtl")
verbose = "--verbose" in sys.argv
r = subprocess.run([oink, solver, "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", "-t", path], capture_output=True, text=True, timeout=900)
out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
prio = {}
for line in open(path):
    m = re.match(r'^(\d+)\s+(\d+)\s+[01]\s+[\d,]+\s*(?:"([^"]*)")?', line.strip())
    if m: prio[m.group(3) or m.group(1)] = int(m.group(2))
def pr(lab):
    if lab in prio: return prio[lab]
    m = re.match(r"(\d+)/(\d+)", lab); return int(m.group(2)) if m else -1
searches = []; cur = None; block = None; phase = None; solved = set(); deletes = 0; tangle_at = {}; repeats_new = 0; repeats_after_del = 0; last_del_search = -1
for line in out.splitlines():
    line = re.sub(r"^\[\s*[0-9.]+\]\s*", "", line)
    m = re.match(r"iteration (\d+)-(even|odd)", line)
    if m:
        cur = {"idx": int(m.group(1)), "player": m.group(2), "reg": {}, "solved_before": set(solved), "dels": 0}; searches.append(cur); phase = "prune"; block = None; continue
    if cur is None: continue
    if line.startswith("best vertices:") and phase == "prune":
        # the proof's first piece has X empty: only a search whose FIRST pruning result is stable has one
        phase = "first" if "(stable)" in line else "later"
        cur["x0"] = "(stable)" in line; continue
    if line.startswith("DOM top") or line.startswith("SOLVE attractor"):
        if phase == "first": phase = "later"
        block = None
        if line.startswith("SOLVE attractor"): phase = "solve"
        continue
    if line.startswith("DELETE tangle"): deletes += 1; cur["dels"] += 1; last_del_search = cur["idx"]; continue
    if line.startswith("dominion"):
        solved.update(re.findall(r"(\S+?)(?:->\S+)?(?= |$)", line.split(")", 2)[-1].strip()) if ")" in line else []); continue
    if line.startswith("SPTL top ") and phase == "first":
        block = {"top": line.split()[2], "vs": {line.split()[2]}}; continue
    if block is not None:
        m2 = re.match(r"attracted (\S+) by", line)
        if m2: block["vs"].add(m2.group(1)); continue
        if line.startswith("REGION top "):
            cur["reg"][block["top"]] = frozenset(block["vs"]); block = None; continue
    if phase == "solve":
        m2 = re.match(r"attracted (\S+) by", line)
        if m2: solved.add(m2.group(1))
    m3 = re.match(r"new tangle \d+ \((\d+)\) \(depth (\d+)\) (.*) with", line)
    if m3 and phase == "first" and block is None:
        pass
    if m3 and phase == "first":
        pass
# new tangles at recurring (top, set): from the region records, a tangle learned at top in a search where (top, set) was seen before
seen = set()
for s_ in searches:
    for top, vs in s_["reg"].items():
        key = (top, vs)
        if key in seen: s_.setdefault("recur", []).append(top)
        seen.add(key)
viol = collections.Counter(); details = []
searches_x0 = [s_ for s_ in searches if s_.get("x0")]
for a, b in zip(searches_x0, searches_x0[1:]):
    if a["player"] != b["player"]: continue
    sol = b["solved_before"]
    lostt = [t for t in a["reg"] if t not in b["reg"] and t not in sol]
    if lostt: viol["A"] += len(lostt); details.append(f"s{a['idx']}->s{b['idx']} tops lost {lostt}")
    for t, vs in a["reg"].items():
        if t in b["reg"]:
            lost = (vs - sol) - b["reg"][t]
            if lost: viol["B"] += 1; details.append(f"s{a['idx']}->s{b['idx']} top {t} region lost {sorted(lost)[:8]}{'...' if len(lost) > 8 else ''} (dels in s{a['idx']}: {a['dels']})")
    head_a = {v: t for t, vs in a["reg"].items() for v in vs}; head_b = {v: t for t, vs in b["reg"].items() for v in vs}
    down = [(v, head_a[v], head_b[v]) for v in head_a if v in head_b and pr(head_b[v]) < pr(head_a[v])]
    if down: viol["C"] += len(down); details.append(f"s{a['idx']}->s{b['idx']} heads down {down[:5]}")
recur = sum(len(s_.get("recur", [])) for s_ in searches)
print(f"{path.split('/')[-1]} {solver}: searches {len(searches)}, with an X-empty first piece {len(searches_x0)}, first-piece tops total {sum(len(s_['reg']) for s_ in searches)}, deletions {deletes}, "
      f"(M-cross) violations: tops lost {viol['A']}, regions shrunk {viol['B']}, heads down {viol['C']}; recurring (top, set) occurrences {recur}")
if verbose:
    for d in details[:30]: print("  ", d)
