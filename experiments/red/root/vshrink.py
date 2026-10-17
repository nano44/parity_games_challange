#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5): greedy VERTEX deletion keeping a property of root/depthfit.py (LALGR_DIR, DTL_ORDER).
KEEP = python expression over the depthfit dict m (default "m['maxd'] >= 1 and m['maxk'] >= 2 and not m['incomplete']").
Deleting v removes v and every edge into v (refused if a vertex would lose all successors); ids are renumbered in order,
priorities and owners kept. Repeats passes (highest id first) until none succeeds. Usage: vshrink.py BASE.pg OUT.pg"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import depthfit as P
keep = os.environ.get("KEEP", "m['maxd'] >= 1 and m['maxk'] >= 2 and not m['incomplete']")
lines = [l for l in open(sys.argv[1]).read().split("\n") if l.strip()]; rows = {}
for l in lines[1:]:
    a = l.rstrip(";").split(" "); rows[int(a[0])] = [int(a[1]), int(a[2]), [int(x) for x in a[3].split(",")]]
def write(rr, path):
    ids = sorted(rr); mp = {v: i for i, v in enumerate(ids)}
    with open(path, "w") as f:
        f.write(f"parity {len(ids) - 1};\n")
        for v in ids: f.write(f"{mp[v]} {rr[v][0]} {rr[v][1]} {','.join(str(mp[w]) for w in sorted(rr[v][2]))};\n")
def ok(rr):
    write(rr, sys.argv[2] + ".tmp")
    try: m = P.measure_game(P.pg.read(sys.argv[2] + ".tmp"), os.environ.get("DTL_ORDER", "stable"))
    except Exception: return False, None
    return eval(keep), m
sys.setrecursionlimit(100000)
good, m = ok(rows); assert good, m
changed = True
while changed:
    changed = False
    for v in sorted(rows, reverse=True):
        if v not in rows: continue
        trial = {u: [a, b, [w for w in c if w != v]] for u, (a, b, c) in rows.items() if u != v}
        if any(not c for _, _, c in trial.values()): continue
        g, m2 = ok(trial)
        if g:
            rows = trial; changed = True; write(rows, sys.argv[2]); m2.pop("tot", None); print("del", v, "n", len(rows), m2, flush=True)
print("done", flush=True)
