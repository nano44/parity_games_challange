#!/usr/bin/env python3
"""L-RED box 8 (produced on Opus 5.5): greedy edge deletion that keeps a permgap.py property (LALGR_DIR, DTL_ORDER).
KEEP = python expression over the permgap dict m (default "m['maxk'] >= 2 and m['hit'] > 0 and not m['incomplete']").
Deletes one edge at a time (vertices keep >= 1 successor), keeps the deletion when KEEP still holds, repeats passes until
none succeeds; writes the current game to OUT after each success. Usage: shrink.py BASE.pg OUT.pg"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import permgap as P
keep = os.environ.get("KEEP", "m['maxk'] >= 2 and m['hit'] > 0 and not m['incomplete']")
lines = [l for l in open(sys.argv[1]).read().split("\n") if l.strip()]; hdr = lines[0]; rows = {}
for l in lines[1:]:
    a = l.rstrip(";").split(" "); rows[int(a[0])] = [int(a[1]), int(a[2]), [int(x) for x in a[3].split(",")]]
def write(rr, path):
    with open(path, "w") as f:
        f.write(hdr + "\n")
        for v in sorted(rr): f.write(f"{v} {rr[v][0]} {rr[v][1]} {','.join(map(str, sorted(rr[v][2])))};\n")
def ok(rr):
    write(rr, sys.argv[2] + ".tmp")
    try: m = P.measure_game(P.pg.read(sys.argv[2] + ".tmp"), os.environ.get("DTL_ORDER", "stable"))
    except Exception: return False, None
    return eval(keep), m
sys.setrecursionlimit(100000); rng = random.Random(1)
good, m = ok(rows); assert good, m
changed = True; npass = 0
while changed:
    changed = False; npass += 1
    es = [(v, w) for v in rows for w in rows[v][2]]; rng.shuffle(es)
    for v, w in es:
        if len(rows[v][2]) < 2 or w not in rows[v][2]: continue
        rows[v][2].remove(w); g, m2 = ok(rows)
        if g:
            changed = True; write(rows, sys.argv[2]); print("pass", npass, "del", v, w, "edges", sum(len(r[2]) for r in rows.values()), m2, flush=True)
        else: rows[v][2].append(w)
print("done", flush=True)
