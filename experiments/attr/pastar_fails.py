#!/usr/bin/env python3
"""PA* and greedy on every psolQ failure of an exhaustive run (out/fail_n{n}.jsonl): both must be False on all of them for
"PA* => psolQ solves" to hold on the whole enumeration. Usage: pastar_fails.py n"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import peeling, pg
n = int(sys.argv[1])
tot = ps = gr = 0
for line in open(os.path.join("out", f"fail_n{n}.jsonl")):
    r = json.loads(line)
    if r["psolq"] == "solved":
        continue
    g = pg.Game(r["prio"], r["owner"], r["succ"]); tot += 1
    if peeling.both(g, r["ref"], peeling.peeling):
        ps += 1; print("PA* TRUE on psolQ failure:", pg.dumps(g).replace("\n", " | "), flush=True)
    if peeling.both(g, r["ref"], peeling.greedy):
        gr += 1; print("greedy TRUE on psolQ failure:", pg.dumps(g).replace("\n", " | "), flush=True)
print(f"n={n}: psolQ failures {tot}, PA* true on {ps}, greedy true on {gr}")
