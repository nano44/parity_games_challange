#!/usr/bin/env python3
"""PA** (exact) and its canonical rule on every psolQ failure of out/fail_n{n}.jsonl; both must be False on all of them.
Usage: pa2_fails.py n"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import peeling, pg
n = int(sys.argv[1]); tot = a = b = 0
for line in open(os.path.join("out", f"fail_n{n}.jsonl")):
    r = json.loads(line)
    if r["psolq"] == "solved":
        continue
    g = pg.Game(r["prio"], r["owner"], r["succ"]); tot += 1
    if peeling.both(g, r["ref"], peeling.pa2):
        a += 1; print("PA** TRUE on psolQ failure:", pg.dumps(g).replace("\n", " | "), flush=True)
    if peeling.both(g, r["ref"], peeling.pa2_greedy):
        b += 1; print("greedy2 TRUE on psolQ failure:", pg.dumps(g).replace("\n", " | "), flush=True)
print(f"n={n}: psolQ failures {tot}, PA** true on {a}, greedy2 true on {b}")
