#!/usr/bin/env python3
"""(r1) probe (L-RED, R8 section 12): is the first stable best-vertex set V* of consecutive searches of one player monotone
(V*_s minus solved vertices contained in V*_{s+1})? Parses Oink's -t -t trace ("iteration k-even/odd", "best vertices: ...
(stable)" or not, "dominion"). The FIRST pruning result of each search is compared (X empty). Prints the violations (vertices that were best in search s and are not in s+1 although unsolved).
Usage: dtl_vstar.py OINK game.pg [--solver dtl|idtl]   (exit code 0; prints 'violations: K')"""
import sys, re, subprocess
oink, path = sys.argv[1], sys.argv[2]; solver = "--" + (sys.argv[sys.argv.index("--solver") + 1] if "--solver" in sys.argv else "dtl")
r = subprocess.run([oink, solver, "--no-single", "--no-wcwc", "--no-loops", "-t", "-t", path], capture_output=True, text=True, timeout=120)
out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout + r.stderr)
searches = []     # (player, first stable V*, solved-after)
cur = None
for line in out.splitlines():
    line = re.sub(r"^\[\s*[0-9.]+\]\s*", "", line)
    m = re.match(r"iteration (\d+)-(even|odd)", line)
    if m:
        cur = {"player": m.group(2), "V": None, "solved": set()}; searches.append(cur); continue
    if cur is None: continue
    if line.startswith("distance ") and cur["V"] is None:          # pruning rounds of the FIRST best_vertices call (X empty)
        cur.setdefault("pruned", set()).update(re.findall(r"(\S+?)/\d+", line.split(":", 1)[1]))
    if line.startswith("best vertices:") and cur["V"] is None:      # the FIRST pruning result of the search (X empty)
        cur["V"] = set(re.findall(r"(\S+?)/\d+", line.split("best vertices:")[1])); cur["stable"] = "(stable)" in line
        cur.setdefault("pruned", set())
    if line.startswith("dominion"): cur["dom"] = True
viol = []
for a, b in zip(searches, searches[1:]):
    if a["player"] != b["player"] or a["V"] is None or b["V"] is None: continue
    lost = b.get("pruned", set()) - a.get("pruned", set())      # pruned in s+1 but not in s: non-monotone pruning
    if lost: viol.append((a, b, lost))
# a vertex may legitimately leave because it was solved; the trace does not list solved vertices, so report and let the
# reader check: we mark searches where a dominion was found in between
for a, b, lost in viol:
    print(f"newly pruned {sorted(lost)} between consecutive {a['player']} searches ({'dominion found in between' if a.get('dom') else 'no dominion in between'}; first results {'stable' if a.get('stable') else '-1'} -> {'stable' if b.get('stable') else '-1'}); V*_s = {sorted(a['V'])}, V*_s+1 = {sorted(b['V'])}" if "--verbose" in sys.argv else f"newly pruned {sorted(lost)} between consecutive {a['player']} searches ({'dominion found in between' if a.get('dom') else 'no dominion in between'}; first results {'stable' if a.get('stable') else '-1'} -> {'stable' if b.get('stable') else '-1'})")
print(f"{path.split('/')[-1]} {solver}: searches {len(searches)}, consecutive same-player pairs with a newly pruned vertex: {len(viol)}, without a dominion in between: {sum(1 for a, b, l in viol if not a.get('dom'))}")
